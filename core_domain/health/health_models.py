# Health system models for Life Sprint
from pydantic import BaseModel, Field
from typing import Optional, Literal


class HealthCondition(BaseModel):
    """Represents a temporary health condition"""
    condition_id: str
    name: str
    severity: Literal["mild", "moderate", "severe"]
    duration_weeks: int
    gpa_impact: float = 0.0
    stress_impact: float = 0.0
    cost: float = 0.0
    requires_medical_visit: bool = False


class HealthHistory(BaseModel):
    """Track health events"""
    event_id: str
    event_type: str  # "exercise", "illness", "therapy", "checkup", "injury"
    severity: Optional[str] = None
    cost: float = 0.0
    health_impact: float = 0.0
    stress_impact: float = 0.0
    semester: int = 0


class Achievement(BaseModel):
    """Represents an unlocked achievement"""
    achievement_id: str
    title: str
    tier: str  # bronze, silver, gold, platinum
    unlocked_semester: int
    reward_description: str


class Health(BaseModel):
    """Core health stat system"""
    health: float = 80.0  # 0-100 scale
    fitness: float = 50.0  # 0-100 (exercise level)
    sleep_quality: float = 70.0  # 0-100 (how well they sleep)
    mental_health: float = 70.0  # 0-100 (depression/anxiety)
    
    # Tracking
    exercises_this_semester: int = 0
    therapy_sessions_attended: int = 0
    last_checkup_semester: Optional[int] = None
    current_conditions: list[HealthCondition] = Field(default_factory=list)
    health_history: list[HealthHistory] = Field(default_factory=list)
    
    # Preventive care
    gym_membership_active: bool = False
    therapy_enrolled: bool = False
    medical_insurance: bool = True  # Affects costs
    
    # ===== NEW: Gamification & Engagement =====
    # Streaks
    current_exercise_streak: int = 0
    best_exercise_streak: int = 0
    exercise_streak_broken_semester: Optional[int] = None
    
    current_therapy_streak: int = 0
    best_therapy_streak: int = 0
    
    # Achievements
    unlocked_achievements: list[Achievement] = Field(default_factory=list)
    total_exercises_all_time: int = 0  # For achievement tracking
    total_therapy_sessions_all_time: int = 0
    total_checkups_all_time: int = 0
    
    # Modifiers from achievements
    fitness_multiplier: float = 1.0
    stress_reduction_bonus: float = 0.0
    mental_health_efficiency: float = 1.0
    illness_probability_reduction: float = 0.0
    gpa_health_bonus: float = 0.0  # GPA bonus from health achievements
    checkup_cost_reduction: float = 0.0
    illness_severity_reduction: float = 0.0
    permanent_health_regen: float = 0.0
    all_health_multiplier: float = 1.0
    
    # Stories shown
    stories_shown: list[str] = Field(default_factory=list)
    
    # Streak multiplier for current streak (increases as streak grows)
    streak_power: float = 1.0
