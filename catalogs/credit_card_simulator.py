"""Credit card danger simulator - teaches minimum payment trap and interest calculations."""

from typing import Dict, List, Optional, Literal, Any
from pydantic import BaseModel, Field
import math


class CreditCardSimulation(BaseModel):
    """A credit card debt simulation."""
    simulation_id: str
    initial_balance: float
    apr: float
    monthly_payment: float

    # Results tracking
    current_balance: float = 0
    total_amount_paid: float = 0
    total_interest_paid: float = 0
    months_to_payoff: int = 0
    month_by_month: List[Dict] = Field(default_factory=list)

    @property
    def total_interest(self) -> float:
        return self.total_interest_paid

    @property
    def total_paid(self) -> float:
        return self.total_amount_paid

    @property
    def annual_interest_rate(self) -> float:
        return self.apr


# Credit card traps (simple dicts)
CREDIT_CARD_TRAPS: Dict[str, Dict[str, Any]] = {
    "trap_minimum_payment": {
        "trap_name": "Minimum Payment Trap",
        "description": "Paying only the minimum keeps you in debt for years.",
        "financial_impact": 300,
    },
    "trap_high_interest": {
        "trap_name": "High Interest Rates",
        "description": "Credit card APRs make balances expensive quickly.",
        "financial_impact": 500,
    },
    "trap_0_apr_intro": {
        "trap_name": "0% APR Intro Trap",
        "description": "Promos end and high APR hits remaining balance.",
        "financial_impact": 250,
    },
    "trap_annual_fees": {
        "trap_name": "Annual Fee Trap",
        "description": "Fees can outweigh rewards if you don't maximize perks.",
        "financial_impact": 150,
    },
    "trap_late_fees": {
        "trap_name": "Late Fee Spiral",
        "description": "Late fees plus penalty APR create snowballing costs.",
        "financial_impact": 120,
    },
    "trap_balance_transfer": {
        "trap_name": "Balance Transfer Fees",
        "description": "Transfer fees add immediate debt even at 0% APR.",
        "financial_impact": 180,
    },
    "trap_interest_only": {
        "trap_name": "Interest-Only Payments",
        "description": "Minimums sometimes barely cover interest.",
        "financial_impact": 220,
    },
    "trap_overspending": {
        "trap_name": "Overspending",
        "description": "Easy credit encourages spending beyond your budget.",
        "financial_impact": 400,
    },
}


# Credit card myths (simple dicts)
CREDIT_CARD_MYTHS: Dict[str, Dict[str, str]] = {
    "myth_carrying_balance": {
        "myth": "You need to carry a balance to build credit.",
        "fact": "FALSE. You never need to pay interest to build credit.",
    },
    "myth_more_cards_better": {
        "myth": "Having more cards always improves your credit score.",
        "fact": "More cards can help, but hard inquiries and misuse can hurt.",
    },
    "myth_rewards_pay_interest": {
        "myth": "Rewards make carrying a balance worth it.",
        "fact": "FALSE. Rewards rarely beat 20%+ APR interest charges.",
    },
    "myth_bad_credit_recover": {
        "myth": "Bad credit fixes itself quickly.",
        "fact": "FALSE. Late payments can stay for years.",
    },
}


def simulate_credit_card_payoff(
    initial_balance: float,
    apr: float,
    monthly_payment: float,
) -> CreditCardSimulation:
    """Simulate paying off a credit card balance.
    """
    balance = initial_balance
    total_paid = 0.0
    total_interest = 0.0
    months = 0
    monthly_breakdown = []

    apr_rate = apr / 12 if apr < 1 else (apr / 100) / 12

    while balance > 0 and months < 600:  # Cap at 50 years
        months += 1
        interest_this_month = balance * apr_rate
        total_interest += interest_this_month
        balance += interest_this_month

        payment = max(monthly_payment, calculate_minimum_payment(balance, apr))
        payment = min(payment, balance)

        balance -= payment
        total_paid += payment

        monthly_breakdown.append({
            "month": months,
            "starting_balance": balance + payment,
            "interest_charged": interest_this_month,
            "payment": payment,
            "ending_balance": balance,
            "total_paid_to_date": total_paid,
            "total_interest_to_date": total_interest,
        })

        if balance < 0.01:
            balance = 0
            break

    return CreditCardSimulation(
        simulation_id=f"sim_{initial_balance}_{apr}",
        initial_balance=initial_balance,
        apr=apr,
        monthly_payment=monthly_payment,
        current_balance=balance,
        total_amount_paid=total_paid,
        total_interest_paid=total_interest,
        months_to_payoff=months,
        month_by_month=monthly_breakdown,
    )


def compare_payoff_strategies(
    initial_balance: float,
    apr: float,
) -> Dict[str, Dict[str, Any]]:
    """Compare different payoff strategies."""
    minimum_sim = simulate_credit_card_payoff(initial_balance, apr, 25)
    fixed_sim = simulate_credit_card_payoff(initial_balance, apr, 100)
    aggressive_sim = simulate_credit_card_payoff(initial_balance, apr, 250)

    return {
        "minimum_only": {
            "months_to_payoff": minimum_sim.months_to_payoff,
            "total_interest": minimum_sim.total_interest_paid,
        },
        "fixed_amount": {
            "months_to_payoff": fixed_sim.months_to_payoff,
            "total_interest": fixed_sim.total_interest_paid,
        },
        "aggressive": {
            "months_to_payoff": aggressive_sim.months_to_payoff,
            "total_interest": aggressive_sim.total_interest_paid,
        },
    }


def calculate_minimum_payment(balance: float, apr: float, min_percent: float = 0.025) -> float:
    """Calculate minimum payment for a balance."""
    if balance <= 0:
        return 0
    return max(balance * min_percent, 25)


def get_payoff_insights(initial_balance: float, apr: float, monthly_budget: float) -> List[str]:
    """Provide actionable payoff insights."""
    insights = []
    minimum_payment = calculate_minimum_payment(initial_balance, apr)

    if monthly_budget <= minimum_payment:
        insights.append("Increase your payment above the minimum to avoid years of interest.")
    else:
        insights.append("Paying above the minimum reduces interest dramatically.")

    if apr >= 0.22:
        insights.append("High APR alert: prioritize this balance to save on interest.")

    if initial_balance > 3000:
        insights.append("Consider a payoff plan or balance transfer if you can pay it off quickly.")

    return insights


def get_trap(trap_id: str) -> Optional[Dict[str, Any]]:
    """Get a specific credit card trap."""
    return CREDIT_CARD_TRAPS.get(trap_id)


def get_all_traps() -> List[Dict[str, Any]]:
    """Get all credit card traps."""
    return list(CREDIT_CARD_TRAPS.values())


def get_myth(myth_id: str) -> Optional[Dict[str, str]]:
    """Get a specific myth."""
    return CREDIT_CARD_MYTHS.get(myth_id)


def get_all_myths() -> List[Dict[str, str]]:
    """Get all myths."""
    return list(CREDIT_CARD_MYTHS.values())


def get_payoff_insights_from_simulation(simulation: CreditCardSimulation) -> Dict[str, Any]:
    """Get insights from a payoff simulation."""

    monthly_rate = (simulation.annual_interest_rate / 100) / 12
    avg_monthly_interest = simulation.total_interest_paid / max(simulation.months_to_payoff, 1)

    return {
        "payoff_time_years": round(simulation.months_to_payoff / 12, 1),
        "payoff_time_months": simulation.months_to_payoff,
        "total_interest_percent": round((simulation.total_interest_paid / simulation.initial_balance) * 100, 1),
        "avg_monthly_interest": round(avg_monthly_interest, 2),
        "interest_as_percent_of_paid": round((simulation.total_interest_paid / simulation.total_paid) * 100, 1),
        "monthly_rate_percent": round(monthly_rate * 100, 2),
    }
