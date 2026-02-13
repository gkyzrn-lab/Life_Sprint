from __future__ import annotations

from uuid import uuid4
from typing import Optional, List

from fastapi import HTTPException

from core_domain.player.player_model import Player
from core_domain.finance.finance_models import Loan, LoanType, RepaymentPlanType
from finance.loan_products import LOAN_PRODUCTS
from finance.calculators import amortized_payment, compute_idr_monthly_payment


# =========================
# Loan helpers
# =========================

def _get_or_create_loan(player: Player, loan_type: LoanType) -> Loan:
    for l in player.finance.loan_portfolio.loans:
        if l.loan_type == loan_type:
            return l

    p = LOAN_PRODUCTS[loan_type.value]
    new_loan = Loan(
        id=str(uuid4()),
        loan_type=loan_type,
        principal=0.0,
        annual_interest_rate=float(p["annual_interest_rate"]),
        accrued_interest=0.0,
        in_school=True,
        grace_months_remaining=int(p["grace_months"]),
        repayment_months_remaining=int(p["repayment_months"]),
        minimum_payment=0.0,
    )
    player.finance.loan_portfolio.loans.append(new_loan)
    return new_loan


def _total_principal_and_interest(player: Player) -> float:
    total = 0.0
    for l in player.finance.loan_portfolio.loans:
        total += float(l.principal) + float(l.accrued_interest)
    return total


def _eligible_for_repayment(l: Loan) -> bool:
    return (not l.in_school) and l.grace_months_remaining == 0 and l.principal > 0


# =========================
# Borrowing
# =========================

def borrow_for_semester(player: Player, needed_amount: float) -> float:
    """
    Borrow money into player.finance.balance using product caps:
    subsidized -> unsubsidized -> private.

    Returns borrowed_total.
    """
    needed = max(0.0, float(needed_amount))
    if needed <= 0:
        return 0.0

    borrowed_total = 0.0

    for lt in [LoanType.subsidized, LoanType.unsubsidized, LoanType.private]:
        if needed <= 0:
            break

        product = LOAN_PRODUCTS[lt.value]
        cap = float(product["max_per_semester"])
        take = min(needed, cap)
        if take <= 0:
            continue

        loan = _get_or_create_loan(player, lt)
        loan.principal += take

        player.finance.balance += take
        borrowed_total += take
        needed -= take

    return borrowed_total


# =========================
# Interest accrual (in school)
# =========================

def accrue_interest_in_school(player: Player, months: int) -> None:
    """
    Accrue in-school interest:
      - subsidized: NO interest accrual
      - unsubsidized/private: accrue to accrued_interest
    """
    m = max(0, int(months))
    if m == 0:
        return

    for loan in player.finance.loan_portfolio.loans:
        if loan.principal <= 0:
            continue
        if not loan.in_school:
            continue

        if loan.loan_type == LoanType.subsidized:
            continue

        r = float(loan.annual_interest_rate) / 12.0
        loan.accrued_interest += float(loan.principal) * r * m


# =========================
# Transition to repayment (graduation / leaving school)
# =========================

def transition_loans_to_repayment(player: Player) -> None:
    """
    Call this when player graduates (or leaves school).
    Sets loans to in_school=False. Grace countdown begins (if any).
    Does NOT instantly capitalize; capitalization happens when grace ends.
    """
    for loan in player.finance.loan_portfolio.loans:
        if loan.principal <= 0 and loan.accrued_interest <= 0:
            continue
        loan.in_school = False


def _advance_grace_and_start_repayment(player: Player, months: int) -> None:
    """
    Step time forward for loans that are out of school.
    During grace:
      - unsubsidized/private accrue interest into accrued_interest
      - subsidized: no interest during grace (v1 simplified; common behavior)
    When grace reaches 0:
      - capitalize accrued_interest into principal
      - set minimum_payment (standard amortized)
    """
    m = max(0, int(months))
    if m == 0:
        return

    for loan in player.finance.loan_portfolio.loans:
        if loan.principal <= 0 and loan.accrued_interest <= 0:
            continue
        if loan.in_school:
            continue

        remaining = m

        # Grace months
        if loan.grace_months_remaining > 0:
            use = min(remaining, int(loan.grace_months_remaining))

            if loan.loan_type != LoanType.subsidized:
                r = float(loan.annual_interest_rate) / 12.0
                loan.accrued_interest += float(loan.principal) * r * use

            loan.grace_months_remaining -= use
            remaining -= use

        # If grace ended, start repayment (set min payment once)
        if loan.grace_months_remaining == 0 and loan.minimum_payment == 0.0:
            # capitalize
            if loan.accrued_interest > 0:
                loan.principal += float(loan.accrued_interest)
                loan.accrued_interest = 0.0

            loan.minimum_payment = amortized_payment(
                principal=float(loan.principal),
                annual_rate=float(loan.annual_interest_rate),
                months=int(loan.repayment_months_remaining),
            )


# =========================
# Repayment
# =========================

def _total_standard_min_payment(player: Player) -> float:
    total = 0.0
    for l in player.finance.loan_portfolio.loans:
        if _eligible_for_repayment(l):
            total += float(l.minimum_payment)
    return total


def _apply_monthly_interest_for_repayment(player: Player) -> None:
    """
    For loans in repayment (grace ended), accrue monthly interest directly into principal.
    This matches the simplified engine where principal represents current balance.
    """
    for loan in player.finance.loan_portfolio.loans:
        if not _eligible_for_repayment(loan):
            continue
        r = float(loan.annual_interest_rate) / 12.0
        loan.principal += float(loan.principal) * r


def _allocate_payment(player: Player, payment: float) -> float:
    """
    Allocate payment across eligible loans:
      - highest interest rate first
      - pay down principal (interest already accrued into principal this month)
    Returns amount actually used.
    """
    budget = max(0.0, float(payment))
    if budget <= 0:
        return 0.0

    eligible: List[Loan] = [l for l in player.finance.loan_portfolio.loans if _eligible_for_repayment(l)]
    if not eligible:
        return 0.0

    # prioritize higher interest
    eligible.sort(key=lambda x: float(x.annual_interest_rate), reverse=True)

    used = 0.0
    remaining = budget

    for loan in eligible:
        if remaining <= 0:
            break
        if loan.principal <= 0:
            continue

        pay = min(remaining, float(loan.principal))
        loan.principal -= pay
        remaining -= pay
        used += pay

        # decrement remaining months in repayment (simple)
        if loan.principal <= 1e-6:
            loan.principal = 0.0
            loan.repayment_months_remaining = 0
            loan.minimum_payment = 0.0
        else:
            loan.repayment_months_remaining = max(0, int(loan.repayment_months_remaining) - 1)

    return used


def repay_months(player: Player, months: int) -> float:
    """
    Simulate repayment for N months.
    Requirements:
      - loans must be out of school (transition_loans_to_repayment called)
      - grace handled automatically
      - payment deducted from player.finance.balance (if available)

    Returns total_paid across the months.
    """
    m = max(1, int(months))
    total_paid = 0.0

    for _ in range(m):
        # advance grace and initialize min payment if grace ends
        _advance_grace_and_start_repayment(player, months=1)

        # apply monthly interest to loans in repayment
        _apply_monthly_interest_for_repayment(player)

        # determine payment budget
        profile = player.finance.repayment_profile

        if profile.plan_type == RepaymentPlanType.idr:
            pay_budget = compute_idr_monthly_payment(profile)

            # Optional cap at standard payment
            if profile.payment_cap_to_standard:
                pay_budget = min(pay_budget, _total_standard_min_payment(player))
        else:
            pay_budget = _total_standard_min_payment(player)

        # can't pay more than cash on hand (v1). later you can allow negative balance.
        pay_budget = min(float(player.finance.balance), float(pay_budget))
        if pay_budget <= 0:
            continue

        # allocate payment
        used = _allocate_payment(player, pay_budget)

        # deduct cash based on used (in case no eligible loans)
        if used > 0:
            player.finance.balance -= used
            total_paid += used

    return total_paid


# =========================
# API-friendly operations
# =========================

def set_repayment_profile(player: Player, plan_type: str, annual_income: float, family_size: int = 1) -> None:
    pt = plan_type.strip().lower()
    if pt not in ("standard", "idr"):
        raise HTTPException(status_code=400, detail="plan_type must be 'standard' or 'idr'.")

    player.finance.repayment_profile.plan_type = RepaymentPlanType.idr if pt == "idr" else RepaymentPlanType.standard
    player.finance.repayment_profile.annual_income = max(0.0, float(annual_income))
    player.finance.repayment_profile.family_size = max(1, int(family_size))
