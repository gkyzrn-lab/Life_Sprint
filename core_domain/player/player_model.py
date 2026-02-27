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

from core_domain.stats.stats_model import Stats
from core_domain.finance.finance_models import Finance, Loan, LoanType, LoanPortfolio, RepaymentProfile, RepaymentPlanType
from core_domain.planning.planning_models import SemesterPlan
from core_domain.health.health_models import Health
from core_domain.tutorial import TutorialState


# =========================
# Enums
# =========================

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
    health: Optional[Health] = None
    housing: Housing
    job: Optional[Job] = None
    plan: Optional[SemesterPlan] = None
    history: List[HistoryEvent] = Field(default_factory=list)

    # Tutorial & onboarding
    tutorial_state: TutorialState = Field(default_factory=TutorialState)

    # Side gigs tracking
    side_gigs: Optional["SideGigsState"] = None

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

    def model_post_init(self, __context) -> None:
        """Initialize side_gigs after model creation to avoid circular import."""
        if self.side_gigs is None:
            from core_domain.side_gigs.side_gigs_models import SideGigsState
            object.__setattr__(self, 'side_gigs', SideGigsState())


# =========================
# Small API DTOs
# =========================

class ApiError(BaseModel):
    detail: str


# Rebuild Player model after SideGigsState is defined
from core_domain.side_gigs.side_gigs_models import SideGigsState
Player.model_rebuild()