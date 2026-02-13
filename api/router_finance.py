from __future__ import annotations

from fastapi import APIRouter

from api.deps import require_player
from finance.dtos import (
    BorrowForSemesterRequest,
    SetRepaymentProfileRequest,
    RepayMonthsRequest,
)
from finance.service import (
    borrow_for_semester,
    set_repayment_profile,
    repay_months,
    transition_loans_to_repayment,
    accrue_interest_in_school,
)

router = APIRouter(prefix="/finance", tags=["finance"])


@router.post("/borrow")
def finance_borrow(req: BorrowForSemesterRequest):
    p = require_player(req.player_id)
    borrowed = borrow_for_semester(p, req.needed_amount)

    remaining = max(0.0, float(req.needed_amount) - float(borrowed))
    return {
        "player_id": p.id,
        "borrowed_total": float(borrowed),
        "remaining_uncovered": float(remaining),
        "new_balance": float(p.finance.balance),
        "loans": [l.model_dump() for l in p.finance.loan_portfolio.loans],
    }


@router.post("/accrue-in-school-interest")
def finance_accrue_in_school(player_id: str, months: int = 4):
    p = require_player(player_id)
    accrue_interest_in_school(p, months=months)
    return {
        "player_id": p.id,
        "months": int(months),
        "loans": [l.model_dump() for l in p.finance.loan_portfolio.loans],
    }


@router.post("/start-repayment")
def finance_start_repayment(player_id: str):
    p = require_player(player_id)
    transition_loans_to_repayment(p)
    return {
        "player_id": p.id,
        "status": "loans moved out of school (grace countdown begins where applicable)",
        "loans": [l.model_dump() for l in p.finance.loan_portfolio.loans],
    }


@router.post("/set-repayment-profile")
def finance_set_profile(req: SetRepaymentProfileRequest):
    p = require_player(req.player_id)
    set_repayment_profile(p, req.plan_type, req.annual_income, req.family_size)
    return {
        "player_id": p.id,
        "repayment_profile": p.finance.repayment_profile.model_dump(),
    }


@router.post("/repay-months")
def finance_repay(req: RepayMonthsRequest):
    p = require_player(req.player_id)
    total_paid = repay_months(p, months=req.months)
    total_principal_remaining = sum(float(l.principal) for l in p.finance.loan_portfolio.loans)

    return {
        "player_id": p.id,
        "months": int(req.months),
        "total_paid": float(total_paid),
        "ending_balance": float(p.finance.balance),
        "total_principal_remaining": float(total_principal_remaining),
        "loans": [l.model_dump() for l in p.finance.loan_portfolio.loans],
    }
