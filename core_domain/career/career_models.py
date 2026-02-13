"""Career progression models for Life Sprint.

Tracks:
- Current position (title, level, salary)
- Career history (promotions, raises, timeline)
- Performance metrics (semesters at job, growth trajectory)
- Achievements (milestones unlocked)
- Burnout state (affects health, affects performance)
"""

from __future__ import annotations

from typing import List, Optional, Literal
from pydantic import BaseModel, Field


class CareerAchievement(BaseModel):
    """A career milestone (promotion, raise, leadership opportunity)."""
    achievement_id: str
    title: str
    milestone_type: Literal["promotion", "raise", "leadership", "skill_unlock", "opportunity"]
    achieved_semester: int
    description: str
    salary_bump: float = 0.0  # raise amount
    title_new: Optional[str] = None  # new job title after promotion
    unlocks: List[str] = Field(default_factory=list)  # what jobs/opportunities unlock


class CareerHistory(BaseModel):
    """A single career event (started job, got promoted, etc)."""
    event_type: Literal["hired", "promotion", "raise", "quit"]
    job_id: str
    job_title: str
    semester: int
    salary_before: float
    salary_after: float
    reason: str = ""  # "promotion", "market adjustment", "quit for better opportunity"


class Career(BaseModel):
    """Complete career state for a player."""
    # Current position
    current_job_id: Optional[str] = None
    current_job_title: Optional[str] = None
    current_salary: float = 0.0
    semesters_at_current_job: int = 0
    
    # Performance
    performance_rating: float = 50.0  # 0-100, affected by health/stress
    
    # Burnout (0-100)
    # 0 = thriving, 50 = normal, 100 = burnout (severe health impact)
    burnout_level: float = 0.0
    
    # Career progression tracking
    total_jobs_held: int = 0
    promotions_earned: int = 0
    total_raises: float = 0.0  # cumulative raise amount
    
    # History
    history: List[CareerHistory] = Field(default_factory=list)
    
    # Achievements
    unlocked_achievements: List[CareerAchievement] = Field(default_factory=list)
    
    # Story tracking
    stories_shown: List[str] = Field(default_factory=list)
    
    # Career milestones
    first_promotion_semester: Optional[int] = None
    highest_salary_achieved: float = 0.0
    career_prestige: float = 0.0  # 0-100, based on job tiers and achievement
    
    # Locks (for balancing)
    # Can't get promoted again until you've been in job for N semesters
    next_promotion_eligible_semester: int = 1
    
    def get_earnings_this_semester(self, hours_per_week: int) -> float:
        """Calculate earnings for one semester (4 months)."""
        return self.current_salary * hours_per_week * 16  # 4 weeks/month * 4 months
