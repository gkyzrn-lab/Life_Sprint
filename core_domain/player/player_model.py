from __future__ import annotations

from typing import Dict, List, Optional, Literal
from pydantic import BaseModel, Field

from core_domain.stats.stats_model import Stats
from core_domain.finance.finance_models import Finance
from core_domain.planning.planning_models import SemesterPlan
from core_domain.health.health_models import Health
from core_domain.career.career_models import Career
from core_domain.finance.financial_responsibility import FinancialResponsibility
from core_domain.housing.housing_models import HousingMarketState
from core_domain.side_gigs.side_gigs_models import SideGigsState
from core_domain.tutorial import TutorialState


class HistoryEvent(BaseModel):
    label: str
    semester: int
    details: Dict[str, float] = Field(default_factory=dict)


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

    stats: Stats = Field(default_factory=Stats)
    finance: Finance = Field(default_factory=Finance)
    health: Health = Field(default_factory=Health)
    career: Career = Field(default_factory=Career)
    financial_responsibility: FinancialResponsibility = Field(default_factory=FinancialResponsibility)
    housing_market: HousingMarketState = Field(default_factory=HousingMarketState)
    side_gigs: SideGigsState = Field(default_factory=SideGigsState)

    housing: Housing
    job: Optional[Job] = None

    plan: Optional[SemesterPlan] = None

    # Course completion tracking
    completed_courses: List[str] = Field(default_factory=list)  # List of completed course IDs
    semester_exam_taken: Dict[str, bool] = Field(default_factory=dict)  # semester -> bool

    history: List[HistoryEvent] = Field(default_factory=list)
    tutorial_state: TutorialState = Field(default_factory=TutorialState)
