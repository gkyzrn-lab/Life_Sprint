"""
Character customization: personality traits and backstory that affect gameplay.
"""

from typing import Dict, List
from pydantic import BaseModel

class PersonalityTrait(BaseModel):
    id: str
    name: str
    description: str
    affects: Dict  # How this trait modifies gameplay
    dialogue_style: str  # How NPCs respond to you

class Backstory(BaseModel):
    id: str
    name: str
    description: str
    starting_resources: Dict
    unique_opportunities: List[str]
    challenges: List[str]

# Personality Traits
PERSONALITY_TRAITS = {
    "extroverted": {
        "id": "extroverted",
        "name": "Extroverted",
        "description": "You gain energy from social interaction. Parties recharge you, isolation drains you.",
        "affects": {
            "social_events_stress": -20,  # Social events reduce stress
            "alone_time_stress": +10,  # Too much alone time increases stress
            "networking_effectiveness": 1.3,  # Better at building connections
            "study_group_bonus": 1.2,  # Learn better with others
            "solo_study_penalty": 0.9,  # Worse at studying alone
            "friend_making_speed": 1.5  # Make friends faster
        },
        "dialogue_style": "NPCs warm up to you quickly. More social invitations.",
        "conflicts_with": ["introverted"]
    },
    
    "introverted": {
        "id": "introverted",
        "name": "Introverted",
        "description": "You recharge through alone time. Socializing is draining but you excel at solo work.",
        "affects": {
            "social_events_stress": +20,  # Social events increase stress
            "alone_time_stress": -15,  # Alone time reduces stress
            "solo_study_bonus": 1.3,  # Better at studying alone
            "study_group_penalty": 0.8,  # Groups are overwhelming
            "deep_friendships": 1.5,  # Fewer but deeper connections
            "networking_anxiety": True  # Networking is harder but not impossible
        },
        "dialogue_style": "NPCs appreciate your thoughtful responses. Quality over quantity in friendships.",
        "conflicts_with": ["extroverted"]
    },
    
    "risk_taker": {
        "id": "risk_taker",
        "name": "Risk Taker",
        "description": "You chase opportunities aggressively. High risk, high reward lifestyle.",
        "affects": {
            "startup_success_chance": 1.5,  # More likely to succeed in risky ventures
            "investment_returns": 1.3,  # Higher investment gains
            "failure_stress": 1.4,  # But failures hit harder
            "conservative_options_boredom": +15,  # Safe choices feel boring (stress)
            "entrepreneurship_appeal": True,  # Unlocks startup/business opportunities
            "extreme_sport_options": True  # Unlocks adventure activities
        },
        "dialogue_style": "Mentors see your ambition. Some worry you're reckless.",
        "conflicts_with": ["cautious"]
    },
    
    "cautious": {
        "id": "cautious",
        "name": "Cautious",
        "description": "You think before you act. Lower highs, but also lower lows. Stability is your strength.",
        "affects": {
            "emergency_fund_discipline": 1.5,  # Better at saving
            "debt_avoidance": True,  # Less likely to take unnecessary loans
            "scholarship_application_thoroughness": 1.3,  # Better applications
            "risk_tolerance": 0.5,  # Avoid risky opportunities
            "steady_progress_bonus": 1.2,  # Consistency pays off
            "planning_effectiveness": 1.3  # Better at long-term planning
        },
        "dialogue_style": "Professors trust your reliability. Employers value your consistency.",
        "conflicts_with": ["risk_taker"]
    },
    
    "competitive": {
        "id": "competitive",
        "name": "Competitive",
        "description": "You're driven by comparison and winning. Rivalry motivates you.",
        "affects": {
            "rival_motivation_bonus": +30,  # When rival does well, you work harder
            "grades_matter_more": True,  # GPA affects stress more
            "sports_performance": 1.3,  # Excel in competitive activities
            "collaboration_difficulty": 0.8,  # Group projects are harder
            "achievement_satisfaction": 1.5,  # Achievements feel better
            "comparison_stress": +15  # Constantly comparing yourself
        },
        "dialogue_style": "Creates natural rivalries. Some respect your drive, others find it intense.",
        "conflicts_with": ["cooperative"]
    },
    
    "cooperative": {
        "id": "cooperative",
        "name": "Cooperative",
        "description": "You thrive on teamwork and helping others. Everyone's success is your success.",
        "affects": {
            "group_project_bonus": 1.4,  # Excel in team settings
            "tutoring_effectiveness": 1.5,  # Great at teaching others
            "networking_natural": True,  # People remember you fondly
            "competition_discomfort": +10,  # Competitive environments stress you
            "team_leadership_opportunities": True,  # More leadership roles
            "reputation_boost": 1.3  # Known as reliable team player
        },
        "dialogue_style": "People want you on their team. Professors ask you to help struggling students.",
        "conflicts_with": ["competitive"]
    },
    
    "creative": {
        "id": "creative",
        "name": "Creative",
        "description": "You think outside the box. Unconventional solutions and artistic expression come naturally.",
        "affects": {
            "creative_majors_bonus": 1.3,  # Excel in arts, design, creative fields
            "entrepreneurship_ideas": 1.4,  # More likely to start creative businesses
            "standardized_test_penalty": 0.9,  # Traditional tests are harder
            "project_based_bonus": 1.4,  # Excel at open-ended projects
            "side_hustle_creativity": True,  # Unlock creative income streams
            "burnout_from_routine": +10  # Repetitive work is draining
        },
        "dialogue_style": "Professors in creative fields notice you. Traditional employers may see you as 'different'.",
        "conflicts_with": ["analytical"]
    },
    
    "analytical": {
        "id": "analytical",
        "name": "Analytical",
        "description": "You love data, logic, and systematic thinking. Problems are puzzles to solve.",
        "affects": {
            "STEM_majors_bonus": 1.3,  # Excel in math, science, engineering
            "financial_planning_effectiveness": 1.4,  # Better money management
            "standardized_test_bonus": 1.2,  # Great at traditional tests
            "creative_assignments_challenge": 0.9,  # Struggle with ambiguity
            "data_driven_decisions": True,  # Better outcomes from analysis
            "research_opportunities": 1.3  # More research invitations
        },
        "dialogue_style": "STEM professors see your potential. You're valued for clear thinking.",
        "conflicts_with": ["creative"]
    },
    
    "resilient": {
        "id": "resilient",
        "name": "Resilient",
        "description": "You bounce back from setbacks quickly. Failure doesn't break you.",
        "affects": {
            "stress_recovery_rate": 1.5,  # Recover from stress faster
            "failure_impact": 0.6,  # Failures hurt less
            "comeback_motivation": 1.4,  # Perform better after setbacks
            "mental_health_stability": True,  # Less prone to burnout
            "risk_recovery": 1.3,  # Better at recovering from bad decisions
            "long_term_perseverance": 1.3  # Stick with difficult goals
        },
        "dialogue_style": "People admire your determination. Comeback stories define you.",
        "conflicts_with": []  # Resilient doesn't conflict with anything
    },
    
    "perfectionist": {
        "id": "perfectionist",
        "name": "Perfectionist",
        "description": "You set extremely high standards. Quality work, but at the cost of stress and time.",
        "affects": {
            "assignment_quality": 1.4,  # Higher quality work
            "time_per_assignment": 1.5,  # Takes 50% longer
            "stress_from_imperfection": +25,  # Any mistake is stressful
            "procrastination_from_fear": True,  # Fear of not being perfect delays starting
            "elite_opportunities": 1.2,  # Your work stands out
            "burnout_susceptibility": 1.4  # More prone to burnout
        },
        "dialogue_style": "Professors appreciate your work. But they worry about your stress levels.",
        "conflicts_with": []
    }
}

# Backstories
BACKSTORIES = {
    "first_generation": {
        "id": "first_generation",
        "name": "First-Generation College Student",
        "description": "You're the first in your family to attend college. Huge opportunity, massive pressure.",
        "story": "Your parents worked multiple jobs so you could be here. You carry their dreams on your shoulders. No one in your family understands what you're going through, but they're proud beyond words.",
        "starting_resources": {
            "money": 1000,  # Limited starting funds
            "family_financial_support": 200,  # per semester
            "emotional_support": "high",
            "network_connections": 0,  # No family connections in professional world
            "pressure": 80  # High pressure to succeed
        },
        "unique_opportunities": [
            "first_gen_scholarships",  # Access to first-gen specific scholarships
            "first_gen_mentorship_programs",
            "underdog_narrative"  # Compelling story for applications
        ],
        "challenges": [
            "imposter_syndrome_events",
            "guilt_about_spending_money",
            "family_doesnt_understand_stress",
            "no_professional_network_to_start"
        ],
        "affects": {
            "scholarship_eligibility": 1.3,  # More scholarship options
            "guilt_from_spending": +15,  # Extra stress when spending money
            "motivation_from_family": 1.4,  # Family pride motivates you
            "networking_disadvantage": 0.7  # Harder to network without connections
        }
    },
    
    "legacy_student": {
        "id": "legacy_student",
        "name": "Legacy Student",
        "description": "Your parents (or siblings) went here. You have connections, expectations, and a reputation to uphold.",
        "story": "You grew up hearing stories about this campus. Your name opens doors... but also invites comparisons. 'Oh, you're Sarah Chen's kid? She was brilliant!' The bar is high.",
        "starting_resources": {
            "money": 5000,
            "family_financial_support": 1500,  # per semester
            "network_connections": 30,  # Built-in professional network
            "pressure": 70,  # Pressure to live up to legacy
            "mentor_connections": 3  # Family friends as mentors
        },
        "unique_opportunities": [
            "family_network_internships",
            "alumni_connections",
            "legacy_specific_scholarships",
            "easier_fraternity_sorority_access"
        ],
        "challenges": [
            "living_in_shadow_events",
            "spoiled_rich_kid_assumptions",
            "pressure_to_follow_family_path",
            "guilt_about_advantages"
        ],
        "affects": {
            "internship_access": 1.5,  # Family connections help
            "networking_ease": 1.4,  # Doors open easier
            "pressure_from_expectations": +20,  # Must maintain family reputation
            "need_to_prove_yourself": True  # Desire to succeed on own merit
        }
    },
    
    "scholarship_kid": {
        "id": "scholarship_kid",
        "name": "Full-Ride Scholar",
        "description": "You earned a full scholarship through merit. You're here because you're brilliant, and everyone knows it.",
        "story": "You worked your ass off in high school. Perfect GPA, leadership, volunteer work, the whole package. The scholarship letter was life-changing. Now you have to maintain that 3.7 GPA or you lose everything.",
        "starting_resources": {
            "money": 2000,
            "tuition_covered": True,
            "family_financial_support": 300,
            "pressure": 90,  # MUST maintain GPA
            "academic_reputation": "high",
            "gpa_requirement": 3.7  # Must maintain or lose scholarship
        },
        "unique_opportunities": [
            "honors_program_access",
            "research_opportunities_early",
            "professor_mentorship_priority",
            "graduate_school_recommendations"
        ],
        "challenges": [
            "gpa_pressure_intense",
            "scholarship_loss_fear",
            "imposter_syndrome_events",
            "no_room_for_failure"
        ],
        "affects": {
            "academic_pressure": +30,  # GPA drops are devastating
            "study_motivation": 1.5,  # Highly motivated
            "stress_from_grades": 1.5,  # Grades affect stress more
            "tuition_savings": 40000,  # Huge advantage
            "professor_respect": 1.4  # Professors know you're top-tier
        }
    },
    
    "transfer_student": {
        "id": "transfer_student",
        "name": "Transfer Student",
        "description": "You started at community college to save money. Now you're here, a semester behind on friendships but ahead on financial wisdom.",
        "story": "While everyone else was paying $60K/year as freshmen, you were at community college paying $3K. You saved $120K. Now you transfer in, and everyone already has friend groups. Starting from scratch, but with way less debt.",
        "starting_resources": {
            "money": 8000,  # Saved money from CC
            "debt": 5000,  # Instead of $40K
            "credits_completed": 60,
            "friend_network": 0,  # Starting fresh socially
            "financial_savvy": "high"
        },
        "unique_opportunities": [
            "transfer_student_programs",
            "financially_wise_decisions",
            "unique_perspective_essays",
            "appreciate_opportunities_more"
        ],
        "challenges": [
            "social_integration_difficulty",
            "missing_freshman_bonding",
            "playing_catch_up_socially",
            "credit_transfer_issues"
        ],
        "affects": {
            "debt_savings": 35000,  # Massive financial advantage
            "social_integration_speed": 0.6,  # Harder to make friends
            "financial_decision_quality": 1.4,  # Better money choices
            "maturity_bonus": 1.2,  # More mature perspective
            "networking_delay": 2  # Behind on professional networking
        }
    },
    
    "international_student": {
        "id": "international_student",
        "name": "International Student",
        "description": "You're far from home, navigating a new culture, language, and educational system. Isolated but determined.",
        "story": "Your family invested everything for you to study here. You're 8,000 miles from home. Different culture, different language, different everything. You face challenges others don't even see, but you're resilient.",
        "starting_resources": {
            "money": 3000,
            "family_financial_support": 2000,  # High cost to family
            "cultural_adjustment_stress": 60,
            "language_barrier": "moderate",
            "visa_restrictions": True,  # Can't work as freely
            "homesickness": 70
        },
        "unique_opportunities": [
            "international_student_scholarships",
            "cultural_diversity_asset",
            "unique_perspective_value",
            "international_network",
            "multilingual_advantage"
        ],
        "challenges": [
            "cultural_adjustment_events",
            "homesickness_waves",
            "visa_work_restrictions",
            "cultural_misunderstandings",
            "isolation_from_family"
        ],
        "affects": {
            "cultural_adjustment_stress": +25,  # Extra stress from adjustment
            "homesickness_events": True,  # Periodic homesickness
            "work_restrictions": 0.5,  # Limited work options
            "unique_perspective_bonus": 1.3,  # Valued in diversity contexts
            "language_challenges": 0.9,  # Slight penalty in communication-heavy tasks
            "resilience_bonus": 1.4  # Overcoming huge challenges builds character
        }
    },
    
    "working_class": {
        "id": "working_class",
        "name": "Working Class Background",
        "description": "You understand the value of money because you've seen your family struggle. Every dollar counts.",
        "story": "You've had a job since age 15. You watched your parents budget carefully, make sacrifices, and still sometimes come up short. You know exactly what it takes to earn a dollar. That perspective is both a burden and a superpower.",
        "starting_resources": {
            "money": 2000,
            "family_financial_support": 400,
            "work_ethic": "exceptional",
            "financial_wisdom": "high",
            "pressure_to_succeed": 75,
            "job_experience": 3  # Years of prior work experience
        },
        "unique_opportunities": [
            "need_based_scholarships",
            "work_study_priority",
            "hardship_narrative",
            "strong_work_ethic_recognized",
            "grit_valued_by_employers"
        ],
        "challenges": [
            "must_work_during_school",
            "family_financial_emergencies",
            "guilt_about_education_cost",
            "class_culture_gap"
        ],
        "affects": {
            "work_ethic": 1.4,  # Better at balancing work and school
            "financial_decisions": 1.3,  # Make smarter money choices
            "job_performance": 1.3,  # Employers notice your work ethic
            "stress_from_money": 1.3,  # Financial issues hit harder
            "must_work_hours_per_week": 15,  # Need to work more
            "scholarship_eligibility": 1.4  # More aid available
        }
    }
}

def get_trait(trait_id: str) -> Dict:
    """Get a specific personality trait."""
    return PERSONALITY_TRAITS.get(trait_id)

def get_backstory(backstory_id: str) -> Dict:
    """Get a specific backstory."""
    return BACKSTORIES.get(backstory_id)

def get_compatible_traits(selected_traits: List[str]) -> List[Dict]:
    """
    Get list of traits compatible with already selected traits.
    """
    if not selected_traits:
        return list(PERSONALITY_TRAITS.values())
    
    compatible = []
    for trait_id, trait in PERSONALITY_TRAITS.items():
        conflicts = trait.get("conflicts_with", [])
        if not any(conflict in selected_traits for conflict in conflicts):
            compatible.append(trait)
    
    return compatible

def apply_trait_effects(base_stats: Dict, traits: List[str]) -> Dict:
    """
    Apply personality trait modifiers to base stats.
    """
    modified_stats = base_stats.copy()
    
    for trait_id in traits:
        trait = get_trait(trait_id)
        if not trait:
            continue
        
        affects = trait.get("affects", {})
        for stat, modifier in affects.items():
            if isinstance(modifier, (int, float)):
                if stat in modified_stats:
                    if stat.endswith("_bonus") or stat.endswith("_penalty"):
                        # Multiplier
                        modified_stats[stat] = modified_stats.get(stat, 1.0) * modifier
                    else:
                        # Additive
                        modified_stats[stat] = modified_stats.get(stat, 0) + modifier
            elif isinstance(modifier, bool):
                modified_stats[stat] = modifier
    
    return modified_stats

def apply_backstory_effects(base_stats: Dict, backstory_id: str) -> Dict:
    """
    Apply backstory starting resources and modifiers.
    """
    backstory = get_backstory(backstory_id)
    if not backstory:
        return base_stats
    
    modified_stats = base_stats.copy()
    
    # Apply starting resources
    starting = backstory.get("starting_resources", {})
    for resource, value in starting.items():
        modified_stats[resource] = value
    
    # Apply effects
    affects = backstory.get("affects", {})
    for stat, modifier in affects.items():
        if isinstance(modifier, (int, float)):
            if isinstance(modifier, float) and modifier < 10:  # Likely a multiplier
                modified_stats[stat] = modified_stats.get(stat, 1.0) * modifier
            else:
                modified_stats[stat] = modified_stats.get(stat, 0) + modifier
        elif isinstance(modifier, bool):
            modified_stats[stat] = modifier
    
    return modified_stats

def get_all_traits() -> Dict[str, Dict]:
    """Get all personality traits."""
    return PERSONALITY_TRAITS

def get_all_backstories() -> Dict[str, Dict]:
    """Get all backstories."""
    return BACKSTORIES
