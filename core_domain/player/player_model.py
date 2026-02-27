# core_domain/player/player_model.py  (IMPROVED)
# ================================================================
# KEY CHANGES vs original:
#   1. Stats: added health, sleep_quality, network_score (were missing)
#   2. Stats: burnout now triggers consequences via property
#   3. Player: added completed_courses, semester_exams_passed (game needs these)
#   4. Player: added time_budget tracking per semester
#   5. Player: added scholarship_history for audit trail
#   6. Finance: added total_debt_at_graduation for end-game summary
#   7. SemesterPlan: added time allocation fields (the core time-budget mechanic)
# ================================================================

from __future__ import annotations
from enum import Enum
from typing import Dict, List, Optional, Set, Literal
from pydantic import BaseModel, Field, computed_field


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


class BurnoutLevel(str, Enum):
    none = "none"          # 0-25
    mild = "mild"          # 26-50
    moderate = "moderate"  # 51-75
    severe = "severe"      # 76-100 → forces course drop


# =========================
# History / Events
# =========================

class HistoryEvent(BaseModel):
    label: str
    semester: int
    details: Dict[str, float] = Field(default_factory=dict)


# =========================
# Stats  (IMPROVED)
# =========================

class Stats(BaseModel):
    # Academic
    gpa: float = 0.0
    total_credits: int = 0

    # Wellbeing — all 0-100 scale
    stress: float = 20.0        # higher = worse
    happiness: float = 70.0     # higher = better
    health: float = 80.0        # NEW: physical health score
    sleep_quality: float = 75.0 # NEW: affects GPA & health each semester
    network_score: float = 0.0  # NEW: built by socializing/clubs/internships

    # Burnout
    eq: float = 10.0
    burnout: float = 0.0        # 0-100; at 76+ forces a course drop

    # Planning
    emergency_tokens: int = 1

    @computed_field
    @property
    def burnout_level(self) -> BurnoutLevel:
        if self.burnout <= 25:
            return BurnoutLevel.none
        if self.burnout <= 50:
            return BurnoutLevel.mild
        if self.burnout <= 75:
            return BurnoutLevel.moderate
        return BurnoutLevel.severe

    @computed_field
    @property
    def is_burned_out(self) -> bool:
        """Severe burnout forces a course drop next semester."""
        return self.burnout > 75

    @computed_field
    @property
    def gpa_modifier(self) -> float:
        """
        Composite modifier applied to exam grade points each semester.
        Poor sleep and high stress drag GPA down; good health lifts it.
        Range: roughly -0.5 to +0.3
        """
        sleep_effect = (self.sleep_quality - 75.0) / 100.0   # -0.75 to +0.25
        stress_effect = -(self.stress - 20.0) / 200.0         # 0 at baseline, down to -0.4
        health_effect = (self.health - 80.0) / 500.0          # small positive nudge
        return round(sleep_effect + stress_effect + health_effect, 3)


# =========================
# Finance / Loans  (unchanged, minor additions)
# =========================

class Loan(BaseModel):
    id: str
    loan_type: LoanType
    principal: float = 0.0
    annual_interest_rate: float = 0.0
    accrued_interest: float = 0.0
    in_school: bool = True
    grace_months_remaining: int = 6
    repayment_months_remaining: int = 120
    minimum_payment: float = 0.0


class LoanPortfolio(BaseModel):
    loans: List[Loan] = Field(default_factory=list)

    @computed_field
    @property
    def total_balance(self) -> float:
        return round(sum(l.principal + l.accrued_interest for l in self.loans), 2)

    @computed_field
    @property
    def total_monthly_payment(self) -> float:
        return round(sum(l.minimum_payment for l in self.loans if not l.in_school), 2)


class RepaymentProfile(BaseModel):
    plan_type: RepaymentPlanType = RepaymentPlanType.standard
    annual_income: float = 0.0
    family_size: int = 1
    poverty_line_annual: float = 15000.0
    discretionary_multiplier: float = 1.5
    idr_percent: float = 0.10
    payment_cap_to_standard: bool = True


class ScholarshipRecord(BaseModel):
    """NEW: Track each scholarship award for audit and display."""
    name: str
    semester: int
    amount: float
    reason: str = ""  # e.g. "GPA >= 3.5", "Need-based"


class Finance(BaseModel):
    balance: float = 0.0
    monthly_expenses: float = 0.0
    tuition_per_semester: float = 0.0
    scholarship_per_semester: float = 0.0

    # NEW: full scholarship history
    scholarship_history: List[ScholarshipRecord] = Field(default_factory=list)

    # NEW: snapshot at graduation for end-game summary
    total_debt_at_graduation: Optional[float] = None

    loan_portfolio: LoanPortfolio = Field(default_factory=LoanPortfolio)
    repayment_profile: RepaymentProfile = Field(default_factory=RepaymentProfile)

    @computed_field
    @property
    def total_scholarships_earned(self) -> float:
        return round(sum(s.amount for s in self.scholarship_history), 2)


# =========================
# Catalog-linked models (unchanged)
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

    @computed_field
    @property
    def weekly_earnings(self) -> float:
        return round(self.hourly_wage * self.hours_per_week, 2)

    @computed_field
    @property
    def semester_earnings(self) -> float:
        """Approx 16 weeks per semester."""
        return round(self.weekly_earnings * 16, 2)


class Activity(BaseModel):
    id: str
    name: str
    hours_per_week: int
    stress_delta_per_semester: float = 0.0
    happiness_delta_per_semester: float = 0.0
    cost_per_semester: float = 0.0


# =========================
# Time Budget  (NEW — core mechanic)
# =========================

WEEKLY_HOURS_TOTAL = 168

class TimeBudget(BaseModel):
    """
    Tracks the 168-hour weekly time budget.
    Class time + study + work + activities + sleep + personal must fit.
    """
    sleep_hours: float = 56.0          # 8 hrs/night default
    class_hours: float = 0.0           # set from curriculum
    study_hours: float = 0.0           # player allocated
    work_hours: float = 0.0            # from job
    activity_hours: float = 0.0        # clubs, gym, etc.
    personal_hours: float = 0.0        # eating, hygiene, commute

    @computed_field
    @property
    def total_committed(self) -> float:
        return (self.sleep_hours + self.class_hours + self.study_hours
                + self.work_hours + self.activity_hours + self.personal_hours)

    @computed_field
    @property
    def free_hours(self) -> float:
        return round(WEEKLY_HOURS_TOTAL - self.total_committed, 1)

    @computed_field
    @property
    def is_overloaded(self) -> bool:
        return self.total_committed > WEEKLY_HOURS_TOTAL

    @computed_field
    @property
    def overload_hours(self) -> float:
        return round(max(0.0, self.total_committed - WEEKLY_HOURS_TOTAL), 1)


# =========================
# Planning  (IMPROVED)
# =========================

class SemesterPlan(BaseModel):
    semester: int
    housing_option_id: str
    job_id: Optional[str] = None
    activities: List[str] = Field(default_factory=list)
    locked: bool = False

    # NEW: explicit time allocations
    time_budget: TimeBudget = Field(default_factory=TimeBudget)

    # NEW: player's intended study hours (used in stress calc)
    intended_study_hours_per_week: float = 15.0


# =========================
# Player  (IMPROVED)
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

    # NEW: academic progress tracking (game NEEDS these)
    completed_courses: List[str] = Field(default_factory=list)
    semester_exams_passed: List[int] = Field(default_factory=list)

    # NEW: courses dropped due to burnout
    dropped_courses: List[Dict] = Field(default_factory=list)

    @computed_field
    @property
    def current_year_label(self) -> str:
        labels = {1: "Freshman", 2: "Sophomore", 3: "Junior", 4: "Senior"}
        return labels.get(self.year_in_school, f"Year {self.year_in_school}")

    @computed_field
    @property
    def has_passed_current_exam(self) -> bool:
        return self.semester in self.semester_exams_passed

    @computed_field
    @property
    def can_progress(self) -> bool:
        return self.has_passed_current_exam

    @computed_field
    @property
    def is_graduated(self) -> bool:
        return self.semester > 8

    @computed_field
    @property
    def estimated_graduation_debt(self) -> float:
        return round(self.finance.loan_portfolio.total_balance, 2)


# =========================
# Small API DTOs
# =========================

class ApiError(BaseModel):
    detail: str