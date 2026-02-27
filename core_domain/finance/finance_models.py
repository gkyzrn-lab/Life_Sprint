from __future__ import annotations

from enum import Enum
from typing import List
from pydantic import BaseModel, Field, computed_field


class LoanType(str, Enum):
    subsidized = "subsidized"
    unsubsidized = "unsubsidized"
    private = "private"


class RepaymentPlanType(str, Enum):
    standard = "standard"
    idr = "idr"


class Loan(BaseModel):
    id: str
    loan_type: LoanType

    principal: float = 0.0
    annual_interest_rate: float = 0.0
    accrued_interest: float = 0.0

    # phases
    in_school: bool = True
    grace_months_remaining: int = 6

    # repayment
    repayment_months_remaining: int = 120
    minimum_payment: float = 0.0


class LoanPortfolio(BaseModel):
    loans: List[Loan] = Field(default_factory=list)

    @computed_field
    @property
    def total_balance(self) -> float:
        """Total outstanding balance (principal + accrued interest)."""
        return sum(l.principal + l.accrued_interest for l in self.loans)


class RepaymentProfile(BaseModel):
    plan_type: RepaymentPlanType = RepaymentPlanType.standard

    # post-grad inputs
    annual_income: float = 0.0
    family_size: int = 1

    # simplified poverty/discretionary rules (tunable later)
    poverty_line_annual: float = 15000.0
    discretionary_multiplier: float = 1.5
    idr_percent: float = 0.10

    # cap IDR payment to standard
    payment_cap_to_standard: bool = True


class Finance(BaseModel):
    balance: float = 0.0

    # baseline costs
    monthly_expenses: float = 0.0
    tuition_per_semester: float = 0.0
    scholarship_per_semester: float = 0.0

    # student loans
    loan_portfolio: LoanPortfolio = Field(default_factory=LoanPortfolio)
    repayment_profile: RepaymentProfile = Field(default_factory=RepaymentProfile)
