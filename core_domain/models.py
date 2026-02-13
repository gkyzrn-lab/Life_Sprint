# app/core/models.py

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional, Literal
from pydantic import BaseModel, Field


# =========================
# Enums
# =========================

class LoanType(str, Enum):
    subsidized = "subsidized"
    unsubsidized = "unsubsidized"
    private = "private"


class RepaymentPlanType(str, Enum):
    standard = "standard"
    idr = "idr"


# =========================
# History / Events
# =========================

class HistoryEvent(BaseModel):
    label: str
    semester: int
    details: Dict[str, float] = Field(default_factory=dict)


# =========================
# Stats
# =========================

class Stats(BaseModel):
    gpa: float = 0.0
    total_credits: int = 0

    stress: float = 20.0
    happiness: float = 70.0
    eq: float = 10.0

    burnout: float = 0.0

    # planning system
    emergency_tokens: int = 1


# =========================
# Finance / Loans
# =========================

class Loan(BaseModel):
    id: str
    loan_type: LoanType

    principal: float = 0.0
    annual_interest_rate: float = 0.0
    accrued_interest: float = 0.0

    # phase flags
    in_school: bool = True
    grace_months_remaining: int = 6

    # repayment
    repayment_months_remaining: int = 120
    minimum_payment: float = 0.0


class LoanPortfolio(BaseModel):
    loans: List[Loan] = Field(default_factory=list)


class RepaymentProfile(BaseModel):
    plan_type: RepaymentPlanType = RepaymentPlanType.standard

    # post-grad inputs
    annual_income: float = 0.0
    family_size: int = 1

    # simplified poverty/discretionary rules (tunable later)
    poverty_line_annual: float = 15000.0
    discretionary_multiplier: float = 1.5
    idr_percent: float = 0.10

    # cap IDR payment to standard (common design choice)
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


# =========================
# Catalog-linked models
# =========================

class Housing(BaseModel):
    option_id: str
    name: str
    monthly_cost: float
    gpa_modifier: float = 0.0
    social_modifier: float = 0.0


class Job(BaseModel):
    job_id: str
    title: str
    hourly_wage: float
    hours_per_week: int
    stress_per_semester: float
    network_gain: float
    tier: Literal["low", "mid", "high", "startup"]


class Activity(BaseModel):
    id: str
    name: str
    hours_per_week: int
    stress_delta_per_semester: float = 0.0
    happiness_delta_per_semester: float = 0.0
    cost_per_semester: float = 0.0


# =========================
# Planning
# =========================

class SemesterPlan(BaseModel):
    semester: int
    housing_option_id: str
    job_id: Optional[str] = None
    activities: List[str] = Field(default_factory=list)
    locked: bool = False


# =========================
# Player
# =========================

class Player(BaseModel):
    id: str
    name: str

    age: int
    hs_gpa: float
    parent_income: float

    major_id: str
    college_id: str

    semester: int = 1
    year_in_school: int = 1

    # state
    stats: Stats = Field(default_factory=Stats)
    finance: Finance = Field(default_factory=Finance)
    housing: Housing
    job: Optional[Job] = None
    plan: Optional[SemesterPlan] = None

    history: List[HistoryEvent] = Field(default_factory=list)


# =========================
# Small API DTOs (generic)
# =========================

class ApiError(BaseModel):
    detail: str
