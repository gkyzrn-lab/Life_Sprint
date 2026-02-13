"""
Challenge modes and scenarios to increase replayability.
Different starting conditions and goals to make players want to play again.
"""

from typing import Dict, List
from enum import Enum

class ChallengeDifficulty(str, Enum):
    EASY = "easy"
    NORMAL = "normal"
    HARD = "hard"
    NIGHTMARE = "nightmare"

CHALLENGE_MODES = {
    "debt_free_challenge": {
        "id": "debt_free_challenge",
        "name": "💎 The Debt-Free Challenge",
        "tagline": "Graduate with $0 debt. Can you do it?",
        "description": "Most students graduate with $30K+ debt. You must graduate completely debt-free. No student loans allowed. Scholarships, work, and smart choices only.",
        "difficulty": ChallengeDifficulty.HARD,
        "rules": {
            "no_student_loans": True,
            "must_graduate": True,
            "max_debt_allowed": 0
        },
        "starting_modifiers": {
            "money": 2000,
            "scholarship_awareness": 1.5,  # Better at finding scholarships
            "financial_literacy_bonus": 1.3
        },
        "win_condition": {
            "graduated": True,
            "total_debt": {"max": 0}
        },
        "rewards": {
            "achievement": "debt_free_champion",
            "unlocks": "financial_freedom_ending",
            "bragging_rights": "Top 8% of players"
        },
        "why_replay": "Every run is different. Community college route? Work 30 hours/week? Scholarship grind? Full-ride hunt? Find your strategy!"
    },
    
    "speed_run": {
        "id": "speed_run",
        "name": "⚡ The 3-Year Speed Run",
        "tagline": "Graduate in 3 years instead of 4. Save a year of tuition!",
        "description": "Time is money. Graduate a year early by taking heavier course loads and summer classes. Intense, but you save $20K-60K.",
        "difficulty": ChallengeDifficulty.HARD,
        "rules": {
            "max_semesters": 6,  # 3 years
            "must_complete_all_requirements": True,
            "min_gpa": 2.0
        },
        "starting_modifiers": {
            "time_management_skill": 1.5,
            "stress_from_heavy_load": 1.3,
            "scholarship_for_summer": True
        },
        "win_condition": {
            "graduated": True,
            "semesters_completed": {"max": 6}
        },
        "rewards": {
            "achievement": "speed_demon",
            "money_saved": 30000,
            "early_career_start": True,
            "bragging_rights": "Finished before your classmates even started junior year"
        },
        "why_replay": "Optimize your path. Which courses? Summer strategy? Burnout management?"
    },
    
    "social_butterfly": {
        "id": "social_butterfly",
        "name": "🦋 The Social Butterfly",
        "tagline": "Build the ultimate network. Graduate with 100+ connections.",
        "description": "Relationships are everything. Focus on networking, friendships, and social events. Graduate with a massive professional network.",
        "difficulty": ChallengeDifficulty.NORMAL,
        "rules": {
            "must_graduate": True,
            "min_professional_connections": 100,
            "min_close_friends": 10
        },
        "starting_modifiers": {
            "extroversion_bonus": 1.4,
            "networking_effectiveness": 1.5,
            "social_stress_reduction": 0.7
        },
        "win_condition": {
            "graduated": True,
            "professional_connections": 100,
            "close_friends": 10,
            "social_events_attended": 50
        },
        "rewards": {
            "achievement": "ultimate_networker",
            "post_grad_job_offers": 5,
            "lifelong_connections": True,
            "bragging_rights": "You know everyone. Everyone knows you."
        },
        "why_replay": "Different friend groups, different outcomes. Romance? Rivals? Mentors?"
    },
    
    "straight_a_perfectionist": {
        "id": "straight_a_perfectionist",
        "name": "📚 The Perfectionist",
        "tagline": "4.0 GPA from start to finish. No room for error.",
        "description": "Maintain a perfect 4.0 GPA for all 4 years. One B kills the run. Intense academic pressure simulation.",
        "difficulty": ChallengeDifficulty.NIGHTMARE,
        "rules": {
            "must_maintain_4_0": True,
            "must_graduate": True,
            "one_b_ends_challenge": True
        },
        "starting_modifiers": {
            "study_effectiveness": 1.3,
            "stress_from_grades": 2.0,  # Double stress from academic pressure
            "perfectionism_trait": True
        },
        "win_condition": {
            "graduated": True,
            "final_gpa": 4.0,
            "no_grades_below_a": True
        },
        "rewards": {
            "achievement": "absolute_perfectionist",
            "grad_school_full_ride_offers": 3,
            "elite_job_offers": True,
            "bragging_rights": "Less than 1% of players achieve this"
        },
        "why_replay": "Can you handle the pressure? Different majors, different difficulty."
    },
    
    "balanced_life": {
        "id": "balanced_life",
        "name": "⚖️ The Balanced Life",
        "tagline": "Master the art of balance. Work, study, social, health - excel at ALL of them.",
        "description": "Most people sacrifice something. You won't. Maintain high GPA, active social life, good health, AND part-time job. The ultimate juggling act.",
        "difficulty": ChallengeDifficulty.HARD,
        "rules": {
            "must_graduate": True,
            "min_gpa": 3.5,
            "min_work_hours_per_semester": 160,  # ~10 hours/week
            "min_social_events_per_semester": 10,
            "max_stress_average": 60,
            "min_exercise_per_month": 12
        },
        "starting_modifiers": {
            "time_management_skill": 1.4,
            "energy_pool": 1.2,
            "stress_resistance": 1.3
        },
        "win_condition": {
            "graduated": True,
            "final_gpa": 3.5,
            "work_hours_total": 1280,  # 4 years * 2 semesters * 160
            "maintained_friendships": 5,
            "max_stress_ever": 70,
            "fitness_level": "good"
        },
        "rewards": {
            "achievement": "life_master",
            "post_grad_readiness": "exceptional",
            "no_regrets": True,
            "bragging_rights": "You actually had it all. Legendary."
        },
        "why_replay": "Different balance strategies. What works for you?"
    },
    
    "entrepreneur_path": {
        "id": "entrepreneur_path",
        "name": "🚀 The Entrepreneur",
        "tagline": "Start a profitable business while in college. Who needs a job?",
        "description": "Skip the traditional path. Start and grow a business to $5K/month revenue before graduation.",
        "difficulty": ChallengeDifficulty.HARD,
        "rules": {
            "must_start_business": True,
            "min_monthly_revenue": 5000,
            "must_graduate": True
        },
        "starting_modifiers": {
            "entrepreneurship_bonus": 1.5,
            "risk_tolerance": 1.4,
            "startup_failure_resilience": 1.3,
            "starting_capital": 3000
        },
        "win_condition": {
            "graduated": True,
            "business_monthly_revenue": 5000,
            "business_profitable": True
        },
        "rewards": {
            "achievement": "campus_tycoon",
            "skip_job_search": True,
            "financial_independence": True,
            "investor_interest": True,
            "bragging_rights": "Built a business while everyone else studied for exams"
        },
        "why_replay": "Different business ideas. E-commerce? Service? Tech? Each run unique."
    },
    
    "minimalist_challenge": {
        "id": "minimalist_challenge",
        "name": "🎯 The Minimalist",
        "tagline": "Graduate spending as little as possible. Extreme frugality.",
        "description": "Live on $1,000/month or less. Ramen noodles, library study rooms, free campus events only. How cheap can you go?",
        "difficulty": ChallengeDifficulty.NORMAL,
        "rules": {
            "max_monthly_spending": 1000,
            "must_graduate": True,
            "track_every_expense": True
        },
        "starting_modifiers": {
            "frugality_mindset": 1.5,
            "deal_finding_skill": 1.4,
            "minimalism_satisfaction": True
        },
        "win_condition": {
            "graduated": True,
            "average_monthly_spending": {"max": 1000},
            "savings_accumulated": 5000
        },
        "rewards": {
            "achievement": "extreme_saver",
            "post_grad_savings": 20000,
            "financial_freedom_early": True,
            "bragging_rights": "Lived on less than a medieval peasant and graduated debt-free"
        },
        "why_replay": "Find new ways to save. Optimize every dollar."
    },
    
    "party_school_survivor": {
        "id": "party_school_survivor",
        "name": "🎉 The Party School Survivor",
        "tagline": "Attend every social event AND maintain a 3.5 GPA. Live your best life.",
        "description": "They said you can't party and succeed. Prove them wrong. Max social life, high GPA, zero regrets.",
        "difficulty": ChallengeDifficulty.HARD,
        "rules": {
            "must_attend_80_percent_social_events": True,
            "min_gpa": 3.5,
            "must_graduate": True,
            "max_stress_violations": 0  # Can't burn out
        },
        "starting_modifiers": {
            "social_energy": 1.5,
            "recovery_speed": 1.4,
            "time_management_critical": 1.3,
            "extroversion_bonus": 1.5
        },
        "win_condition": {
            "graduated": True,
            "final_gpa": 3.5,
            "social_events_attended": 80,  # ~10 per semester
            "burned_out": False,
            "legendary_college_experience": True
        },
        "rewards": {
            "achievement": "legend_status",
            "network_size": 200,
            "memories_for_life": True,
            "bragging_rights": "Peaked in college and succeeded anyway"
        },
        "why_replay": "Every party has different outcomes. Who will you meet?"
    },
    
    "mental_health_champion": {
        "id": "mental_health_champion",
        "name": "🧘 The Mental Health Champion",
        "tagline": "Prioritize wellness above all. Keep stress under 40 for 4 years.",
        "description": "College doesn't have to be suffering. Maintain exceptional mental health throughout your entire college experience.",
        "difficulty": ChallengeDifficulty.NORMAL,
        "rules": {
            "max_stress_allowed": 40,
            "must_graduate": True,
            "min_therapy_sessions": 20,
            "min_exercise_sessions": 200,
            "min_sleep_hours_per_night": 7
        },
        "starting_modifiers": {
            "stress_resistance": 1.5,
            "self_care_priority": True,
            "wellness_knowledge": 1.4,
            "therapy_access": True
        },
        "win_condition": {
            "graduated": True,
            "max_stress_ever": 40,
            "mental_health_score": 90,
            "no_burnout_episodes": True
        },
        "rewards": {
            "achievement": "zen_master",
            "post_grad_wellness": "exceptional",
            "life_skills_mastered": True,
            "bragging_rights": "Graduated happy, healthy, and whole"
        },
        "why_replay": "Different wellness strategies. What works for your play style?"
    },
    
    "realistic_mode": {
        "id": "realistic_mode",
        "name": "😰 Realistic Mode (2025 Edition)",
        "tagline": "Current college costs, real job market, actual difficulty. No kid gloves.",
        "description": "Real tuition costs ($30K-60K/year), real job market competition, real stress levels. This is what college actually is right now.",
        "difficulty": ChallengeDifficulty.NIGHTMARE,
        "rules": {
            "tuition_realistic": True,  # Actual 2025 prices
            "job_market_realistic": True,  # High competition
            "mental_health_realistic": True,  # Actual stress levels
            "must_graduate": True
        },
        "starting_modifiers": {
            "tuition_multiplier": 2.0,  # Double cost
            "job_competition": 3.0,  # 3x harder to get jobs
            "stress_from_everything": 1.5,
            "scholarship_harder": 0.7
        },
        "win_condition": {
            "graduated": True,
            "employed_after_grad": True,
            "mental_health_stable": True
        },
        "rewards": {
            "achievement": "survived_reality",
            "bragging_rights": "You experienced what actual students face. Respect.",
            "reality_check": True
        },
        "why_replay": "See how real students struggle. Appreciate your own life more."
    }
}

def get_challenge(challenge_id: str) -> Dict:
    """Get a specific challenge mode."""
    return CHALLENGE_MODES.get(challenge_id)

def get_challenges_by_difficulty(difficulty: ChallengeDifficulty) -> List[Dict]:
    """Get all challenges of a specific difficulty."""
    return [c for c in CHALLENGE_MODES.values() if c.get("difficulty") == difficulty]

def get_all_challenges() -> Dict[str, Dict]:
    """Get all challenge modes."""
    return CHALLENGE_MODES

def check_challenge_victory(challenge_id: str, player_state: Dict) -> tuple[bool, List[str]]:
    """
    Check if player has met victory conditions for a challenge.
    
    Returns:
        (won: bool, unmet_conditions: List[str])
    """
    challenge = get_challenge(challenge_id)
    if not challenge:
        return False, ["Challenge not found"]
    
    win_conditions = challenge.get("win_condition", {})
    unmet = []
    
    for condition, required_value in win_conditions.items():
        player_value = player_state.get(condition, 0)
        
        if isinstance(required_value, dict):
            # Handle min/max conditions
            if "min" in required_value and player_value < required_value["min"]:
                unmet.append(f"{condition} must be at least {required_value['min']}, you have {player_value}")
            if "max" in required_value and player_value > required_value["max"]:
                unmet.append(f"{condition} must be at most {required_value['max']}, you have {player_value}")
        elif isinstance(required_value, bool):
            if player_value != required_value:
                unmet.append(f"{condition} must be {required_value}")
        else:
            # Numeric requirement
            if player_value < required_value:
                unmet.append(f"{condition} must be {required_value}, you have {player_value}")
    
    return len(unmet) == 0, unmet

def get_challenge_progress(challenge_id: str, player_state: Dict) -> Dict:
    """
    Get player's progress toward challenge completion.
    
    Returns:
        {
            "condition_name": {
                "required": value,
                "current": value,
                "percentage": 0.0-1.0,
                "met": bool
            }
        }
    """
    challenge = get_challenge(challenge_id)
    if not challenge:
        return {}
    
    win_conditions = challenge.get("win_condition", {})
    progress = {}
    
    for condition, required_value in win_conditions.items():
        player_value = player_state.get(condition, 0)
        
        if isinstance(required_value, dict):
            if "min" in required_value:
                req = required_value["min"]
                pct = min(1.0, player_value / req) if req > 0 else 0.0
                met = player_value >= req
            elif "max" in required_value:
                req = required_value["max"]
                pct = 1.0 if player_value <= req else 0.0
                met = player_value <= req
            else:
                continue
        elif isinstance(required_value, bool):
            req = required_value
            pct = 1.0 if player_value == required_value else 0.0
            met = player_value == required_value
        else:
            req = required_value
            pct = min(1.0, player_value / req) if req > 0 else 0.0
            met = player_value >= req
        
        progress[condition] = {
            "required": req,
            "current": player_value,
            "percentage": pct,
            "met": met
        }
    
    return progress
