"""
Mental Health Crisis System Models

IMPORTANT: This system is designed to be EDUCATIONAL and SUPPORTIVE.
It teaches teens that:
- Mental health struggles are real and common
- Seeking help is the RIGHT choice
- Treatment works
- Taking time off is okay
- Resources are available 24/7

This system emphasizes that HELP IS AVAILABLE and RECOVERY IS POSSIBLE.
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime


class MentalHealthCrisis(BaseModel):
    """
    Crisis state tracking and intervention system.
    
    DESIGN PHILOSOPHY:
    - Crisis is detected BEFORE it becomes dangerous
    - System ALWAYS offers help and resources
    - Seeking help is REWARDED (achievements, positive outcomes)
    - Recovery is REALISTIC and ACHIEVABLE
    """
    crisis_level: int = 0  # 0-100 (0=no crisis, 100=severe crisis)
    crisis_active: bool = False
    intervention_offered: bool = False
    intervention_accepted: bool = False
    
    # Crisis factors (all 0-100)
    stress_accumulated: float = 0.0  # From academics, work, finances
    burnout_level: float = 0.0  # From overwork
    social_isolation: float = 0.0  # Lack of support network
    financial_stress: float = 0.0  # Money worries
    sleep_deprivation: float = 0.0  # Chronic lack of sleep
    
    # Crisis history
    crisis_count: int = 0
    last_crisis_date: Optional[str] = None
    intervention_count: int = 0
    
    # Emergency contacts shown (for educational purposes)
    emergency_resources_shown: bool = False


class TherapyTreatment(BaseModel):
    """
    Therapy treatment tracking.
    
    Therapy is EFFECTIVE and helps reduce crisis risk.
    """
    in_therapy: bool = False
    therapy_type: Literal["none", "individual", "group", "intensive"] = "none"
    sessions_attended: int = 0
    sessions_scheduled: int = 0
    therapy_start_date: Optional[str] = None
    
    # Costs (realistic but shows value)
    cost_per_session: float = 0.0  # $100-$200 per session typically
    insurance_coverage: float = 0.0  # 0.0-0.8 (0-80% covered)
    total_spent: float = 0.0
    
    # Effectiveness (therapy WORKS)
    mental_health_improvement: float = 0.0  # Cumulative improvement
    crisis_risk_reduction: float = 0.0  # How much therapy reduces crisis risk
    coping_skills_learned: int = 0  # Number of coping strategies


class MedicationTreatment(BaseModel):
    """
    Medication treatment tracking.
    
    Shows realistic trade-offs: medication helps but has side effects.
    Emphasis: Benefits typically outweigh side effects for those who need it.
    """
    on_medication: bool = False
    medication_type: Literal["none", "antidepressant", "anti_anxiety", "both"] = "none"
    medication_name: str = ""  # Generic name (e.g., "SSRI antidepressant")
    start_date: Optional[str] = None
    weeks_on_medication: int = 0
    
    # Costs
    monthly_cost: float = 0.0  # $20-$200/month depending on insurance
    insurance_coverage: float = 0.0
    total_spent: float = 0.0
    
    # Benefits (medication HELPS for those who need it)
    mental_health_baseline_increase: float = 0.0  # +10-30 points typical
    crisis_threshold_increase: float = 0.0  # Higher threshold before crisis
    effectiveness: float = 0.0  # 0.0-1.0 (how well it's working)
    
    # Side effects (realistic but not overwhelming)
    side_effects: List[str] = []  # e.g., ["fatigue", "nausea", "weight_gain"]
    side_effect_severity: float = 0.0  # 0.0-1.0
    adjustment_period: bool = True  # First 2-4 weeks are hardest
    
    # Important: Side effects typically DECREASE over time, benefits INCREASE


class SemesterLeave(BaseModel):
    """
    Taking time off for mental health recovery.
    
    This is a VALID and HEALTHY choice when crisis is severe.
    """
    on_leave: bool = False
    leave_type: Literal["none", "partial", "full_semester", "medical_withdrawal"] = "none"
    leave_start_date: Optional[str] = None
    leave_end_date: Optional[str] = None
    weeks_on_leave: int = 0
    
    # Financial impact (realistic)
    tuition_refund_percent: float = 0.0  # Depends on when you withdraw
    financial_aid_affected: bool = False
    total_cost: float = 0.0  # Net cost of taking leave
    
    # Recovery during leave (time off HELPS)
    recovery_rate_multiplier: float = 2.0  # Recover 2x faster on leave
    stress_reduction: float = 0.0  # How much stress was reduced
    mental_health_improvement: float = 0.0
    
    # Academic impact
    graduation_delayed_semesters: int = 0
    courses_dropped: List[str] = []
    gpa_protected: bool = True  # Medical withdrawal doesn't affect GPA


class CrisisIntervention(BaseModel):
    """
    Record of a crisis intervention (when system detects high crisis level).
    
    ALWAYS includes resources and offers help.
    """
    intervention_id: str
    date: str
    crisis_level_at_intervention: float
    
    # What triggered the intervention
    primary_cause: str
    contributing_factors: List[str]
    
    # Resources shown
    resources_provided: List[str]  # Always includes 988 and Crisis Text Line
    
    # Player's choice
    action_taken: Literal["accepted_help", "declined_help", "took_leave", "continued_with_support"]
    
    # Outcome
    crisis_resolved: bool
    mental_health_after: float
    help_was_effective: bool = True  # Emphasis: help WORKS


class MentalHealthResource(BaseModel):
    """
    Mental health resources (educational and supportive).
    """
    resource_id: str
    name: str
    description: str
    contact: str  # Phone number or URL
    available_24_7: bool
    cost: Literal["free", "insurance", "sliding_scale", "paid"]


class CrisisAchievement(BaseModel):
    """
    Achievements for seeking help and recovering.
    
    DESIGN: Rewards seeking help, not suffering.
    """
    achievement_id: str
    name: str
    description: str
    date_earned: str
    tier: Literal["bronze", "silver", "gold", "platinum"]


class CrisisStory(BaseModel):
    """
    Narrative moments related to mental health.
    
    TONE: Supportive, educational, hopeful.
    """
    story_id: str
    title: str
    message: str
    timestamp: str
    tone: Literal["cautionary", "supportive", "educational", "triumphant"]
    resources_included: bool = False


class MentalHealthCrisisState(BaseModel):
    """
    Complete mental health crisis state for a player.
    
    IMPORTANT: This system is designed to HELP, not punish.
    """
    crisis: MentalHealthCrisis = Field(default_factory=MentalHealthCrisis)
    therapy: TherapyTreatment = Field(default_factory=TherapyTreatment)
    medication: MedicationTreatment = Field(default_factory=MedicationTreatment)
    leave: SemesterLeave = Field(default_factory=SemesterLeave)
    
    # Interventions and resources
    interventions: List[CrisisIntervention] = []
    achievements: List[CrisisAchievement] = []
    stories: List[CrisisStory] = []
    
    # Support system
    has_support_network: bool = False
    support_network_strength: int = 0  # 0-100
    knows_resources: bool = False  # Has player been shown resources?
    
    # Recovery tracking
    recovery_milestones: List[str] = []
    days_since_last_crisis: int = 0
    longest_stable_period: int = 0
    
    def calculate_crisis_level(self) -> float:
        """
        Calculate current crisis level from all factors.
        
        DESIGN: Crisis is detected EARLY so intervention happens BEFORE danger.
        """
        # Weighted factors
        crisis = (
            self.crisis.stress_accumulated * 0.25 +
            self.crisis.burnout_level * 0.20 +
            self.crisis.social_isolation * 0.20 +
            self.crisis.financial_stress * 0.15 +
            self.crisis.sleep_deprivation * 0.20
        )
        
        # Protective factors REDUCE crisis
        if self.therapy.in_therapy:
            crisis -= self.therapy.crisis_risk_reduction
        
        if self.medication.on_medication and self.medication.effectiveness > 0.5:
            crisis -= self.medication.crisis_threshold_increase
        
        if self.has_support_network:
            crisis -= self.support_network_strength * 0.3
        
        return max(0, min(100, crisis))
    
    def should_trigger_intervention(self) -> bool:
        """
        Determine if crisis intervention should be triggered.
        
        DESIGN: Trigger EARLY (at 60-70) so help is offered BEFORE severe crisis.
        """
        crisis_level = self.calculate_crisis_level()
        
        # Trigger intervention if:
        # 1. Crisis level >= 60 (moderate to high)
        # 2. Multiple factors are high simultaneously
        # 3. Rapid increase in crisis level
        
        if crisis_level >= 60 and not self.crisis.intervention_offered:
            return True
        
        # Multiple high-risk factors
        high_risk_factors = sum([
            self.crisis.stress_accumulated > 70,
            self.crisis.burnout_level > 70,
            self.crisis.social_isolation > 70,
            self.crisis.financial_stress > 70,
            self.crisis.sleep_deprivation > 70,
        ])
        
        if high_risk_factors >= 3:
            return True
        
        return False
