"""
Educational achievement badges that teach financial literacy and life skills.
"""

from typing import Dict, List
from pydantic import BaseModel

class BadgeTier(str):
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"
    PLATINUM = "platinum"

class EducationalBadge(BaseModel):
    id: str
    name: str
    description: str
    educational_value: str  # What this teaches
    tier: str
    category: str
    requirements: Dict
    reward_description: str
    unlocked: bool = False
    progress: float = 0.0  # 0.0 to 1.0

# Financial Literacy Badges
FINANCIAL_BADGES = {
    "emergency_fund_starter": {
        "id": "emergency_fund_starter",
        "name": "🛡️ Emergency Fund Starter",
        "description": "Save $500 for emergencies",
        "educational_value": "Teaches importance of emergency funds. Even $500 can prevent credit card debt in small emergencies.",
        "tier": BadgeTier.BRONZE,
        "category": "financial_literacy",
        "requirements": {
            "savings_balance": 500
        },
        "reward_description": "Unlocks 'Emergency Fund Pro' badge path",
        "unlocked": False
    },
    
    "emergency_fund_pro": {
        "id": "emergency_fund_pro",
        "name": "🛡️ Emergency Fund Pro",
        "description": "Save 3 months of living expenses",
        "educational_value": "3-6 months expenses = true financial security. Can handle job loss, major repairs without debt.",
        "tier": BadgeTier.SILVER,
        "category": "financial_literacy",
        "requirements": {
            "savings_balance": 6000,  # Assuming $2000/month expenses
            "maintained_for_semesters": 2
        },
        "reward_description": "Reduced stress from financial events",
        "unlocked": False
    },
    
    "emergency_fund_master": {
        "id": "emergency_fund_master",
        "name": "🛡️ Emergency Fund Master",
        "description": "Save 6 months of living expenses",
        "educational_value": "6 months = elite financial security. Can handle almost any life crisis without panic.",
        "tier": BadgeTier.GOLD,
        "category": "financial_literacy",
        "requirements": {
            "savings_balance": 12000,
            "maintained_for_semesters": 4
        },
        "reward_description": "+10 stress resistance permanently",
        "unlocked": False
    },
    
    "loan_ninja_bronze": {
        "id": "loan_ninja_bronze",
        "name": "💰 Loan Ninja (Bronze)",
        "description": "Pay off any loan early",
        "educational_value": "Paying extra on loans saves massive interest. Even $50 extra/month makes a big difference.",
        "tier": BadgeTier.BRONZE,
        "category": "financial_literacy",
        "requirements": {
            "loans_paid_early": 1
        },
        "reward_description": "Unlocks loan payment calculator tool",
        "unlocked": False
    },
    
    "loan_ninja_silver": {
        "id": "loan_ninja_silver",
        "name": "💰 Loan Ninja (Silver)",
        "description": "Graduate with less than $20K debt",
        "educational_value": "Sub-$20K debt is manageable and paid off quickly. Allows career flexibility and life choices.",
        "tier": BadgeTier.SILVER,
        "category": "financial_literacy",
        "requirements": {
            "total_debt_at_graduation": {"max": 20000}
        },
        "reward_description": "Special 'Low Debt' ending path",
        "unlocked": False
    },
    
    "loan_ninja_gold": {
        "id": "loan_ninja_gold",
        "name": "💰 Loan Ninja (Gold)",
        "description": "Graduate debt-free!",
        "educational_value": "Zero debt = maximum freedom. You chose wisely: scholarships, work, budget schools. You're ahead of 90% of graduates.",
        "tier": BadgeTier.GOLD,
        "category": "financial_literacy",
        "requirements": {
            "total_debt_at_graduation": {"max": 0}
        },
        "reward_description": "Special 'Debt Free' ending + achievement showcase",
        "unlocked": False
    },
    
    "balance_pro_bronze": {
        "id": "balance_pro_bronze",
        "name": "⚖️ Balance Pro (Bronze)",
        "description": "Maintain work/life/study balance for 2 semesters",
        "educational_value": "Balance prevents burnout. Working 10-15 hours/week while maintaining grades and health is the sweet spot.",
        "tier": BadgeTier.BRONZE,
        "category": "life_skills",
        "requirements": {
            "semesters_balanced": 2,
            "min_gpa": 3.0,
            "max_stress": 70,
            "hours_worked_per_week": {"min": 10, "max": 20}
        },
        "reward_description": "+5% income from all jobs",
        "unlocked": False
    },
    
    "balance_pro_silver": {
        "id": "balance_pro_silver",
        "name": "⚖️ Balance Pro (Silver)",
        "description": "Maintain balance for 4 semesters",
        "educational_value": "Sustained balance = success. You've proven you can juggle multiple priorities long-term.",
        "tier": BadgeTier.SILVER,
        "category": "life_skills",
        "requirements": {
            "semesters_balanced": 4,
            "min_gpa": 3.2,
            "max_stress": 60,
            "hours_worked_per_week": {"min": 10, "max": 20}
        },
        "reward_description": "+10% income, employers notice your consistency",
        "unlocked": False
    },
    
    "budget_master": {
        "id": "budget_master",
        "name": "📊 Budget Master",
        "description": "Track expenses for 3 months and stay under budget",
        "educational_value": "Budgeting isn't restriction - it's intentionality. Knowing where money goes = power to redirect it.",
        "tier": BadgeTier.SILVER,
        "category": "financial_literacy",
        "requirements": {
            "tracked_expenses_months": 3,
            "stayed_under_budget": True
        },
        "reward_description": "Unlocks advanced financial analytics dashboard",
        "unlocked": False
    },
    
    "scholarship_hunter": {
        "id": "scholarship_hunter",
        "name": "🎯 Scholarship Hunter",
        "description": "Earn $5,000+ in scholarships",
        "educational_value": "Scholarships are FREE money. Every hour spent applying = $500+ earned. Best 'job' you'll ever have.",
        "tier": BadgeTier.GOLD,
        "category": "financial_literacy",
        "requirements": {
            "total_scholarships_earned": 5000
        },
        "reward_description": "Unlocks scholarship strategy guide",
        "unlocked": False
    },
    
    "investment_initiate": {
        "id": "investment_initiate",
        "name": "📈 Investment Initiate",
        "description": "Start investing (any amount) before graduation",
        "educational_value": "Starting early is everything. Even $50/month invested at 22 becomes $200K+ by retirement.",
        "tier": BadgeTier.GOLD,
        "category": "financial_literacy",
        "requirements": {
            "investment_account_opened": True,
            "contributed_any_amount": True
        },
        "reward_description": "Special post-graduation investment opportunities",
        "unlocked": False
    },
    
    "credit_score_champion": {
        "id": "credit_score_champion",
        "name": "⭐ Credit Score Champion",
        "description": "Maintain 750+ credit score for 2 semesters",
        "educational_value": "Excellent credit saves thousands in interest. You're in the top 25% of Americans.",
        "tier": BadgeTier.PLATINUM,
        "category": "financial_literacy",
        "requirements": {
            "credit_score": 750,
            "maintained_for_semesters": 2,
            "no_late_payments": True
        },
        "reward_description": "Best loan rates available permanently",
        "unlocked": False
    }
}

# Academic Achievement Badges
ACADEMIC_BADGES = {
    "straight_a_semester": {
        "id": "straight_a_semester",
        "name": "🎓 Straight A Semester",
        "description": "4.0 GPA for one semester",
        "educational_value": "Proves you can excel. But remember: grades aren't everything. Balance matters too.",
        "tier": BadgeTier.SILVER,
        "category": "academic",
        "requirements": {
            "semester_gpa": 4.0
        },
        "reward_description": "Scholarship opportunities increase",
        "unlocked": False
    },
    
    "deans_list": {
        "id": "deans_list",
        "name": "🏆 Dean's List",
        "description": "3.7+ GPA for 2 consecutive semesters",
        "educational_value": "Consistent excellence. This goes on your resume and matters to employers.",
        "tier": BadgeTier.GOLD,
        "category": "academic",
        "requirements": {
            "consecutive_semesters_high_gpa": 2,
            "min_gpa": 3.7
        },
        "reward_description": "Unlocks elite internship opportunities",
        "unlocked": False
    },
    
    "comeback_kid": {
        "id": "comeback_kid",
        "name": "💪 Comeback Kid",
        "description": "Raise GPA by 0.5+ in one semester",
        "educational_value": "Resilience matters more than perfection. Employers value growth and recovery from setbacks.",
        "tier": BadgeTier.BRONZE,
        "category": "academic",
        "requirements": {
            "gpa_improvement": 0.5
        },
        "reward_description": "Reduced stress from academic pressure",
        "unlocked": False
    }
}

# Career Preparation Badges
CAREER_BADGES = {
    "intern_explorer": {
        "id": "intern_explorer",
        "name": "💼 Intern Explorer",
        "description": "Complete your first internship",
        "educational_value": "First real-world experience. You're now ahead of 50% of graduates who never interned.",
        "tier": BadgeTier.BRONZE,
        "category": "career",
        "requirements": {
            "internships_completed": 1
        },
        "reward_description": "Better internship offers become available",
        "unlocked": False
    },
    
    "intern_veteran": {
        "id": "intern_veteran",
        "name": "💼 Intern Veteran",
        "description": "Complete 2+ internships",
        "educational_value": "Multiple internships = top job market candidate. You're in the top 20% of applicants.",
        "tier": BadgeTier.SILVER,
        "category": "career",
        "requirements": {
            "internships_completed": 2
        },
        "reward_description": "Job offers before graduation likely",
        "unlocked": False
    },
    
    "network_builder": {
        "id": "network_builder",
        "name": "🤝 Network Builder",
        "description": "Build network of 20+ professional connections",
        "educational_value": "70% of jobs come from networking. You're building real career capital.",
        "tier": BadgeTier.SILVER,
        "category": "career",
        "requirements": {
            "professional_connections": 20
        },
        "reward_description": "Increased chance of job referrals",
        "unlocked": False
    }
}

# Health & Wellness Badges
WELLNESS_BADGES = {
    "stress_manager": {
        "id": "stress_manager",
        "name": "🧘 Stress Manager",
        "description": "Keep stress under 50 for an entire semester",
        "educational_value": "Managing stress = better performance. You've learned a life skill most adults struggle with.",
        "tier": BadgeTier.SILVER,
        "category": "wellness",
        "requirements": {
            "max_stress_semester": 50,
            "semester_complete": True
        },
        "reward_description": "+10 max energy, better focus",
        "unlocked": False
    },
    
    "fitness_enthusiast": {
        "id": "fitness_enthusiast",
        "name": "💪 Fitness Enthusiast",
        "description": "Exercise 3x/week for 4 months",
        "educational_value": "Regular exercise improves grades by 0.4 GPA on average. It's a performance enhancer, not luxury.",
        "tier": BadgeTier.GOLD,
        "category": "wellness",
        "requirements": {
            "exercise_sessions_per_week": 3,
            "weeks_maintained": 16
        },
        "reward_description": "+15 stress resistance, +0.2 GPA bonus",
        "unlocked": False
    },
    
    "sleep_champion": {
        "id": "sleep_champion",
        "name": "😴 Sleep Champion",
        "description": "Get 7-9 hours sleep for 30 consecutive days",
        "educational_value": "Sleep = memory consolidation. You're literally upgrading your brain every night.",
        "tier": BadgeTier.GOLD,
        "category": "wellness",
        "requirements": {
            "hours_sleep_per_night": {"min": 7, "max": 9},
            "consecutive_days": 30
        },
        "reward_description": "+0.3 GPA bonus, better decision making",
        "unlocked": False
    }
}

# Combine all badges
ALL_BADGES = {
    **FINANCIAL_BADGES,
    **ACADEMIC_BADGES,
    **CAREER_BADGES,
    **WELLNESS_BADGES
}

def get_badge(badge_id: str) -> Dict:
    """Get a specific badge definition."""
    return ALL_BADGES.get(badge_id)

def get_badges_by_category(category: str) -> Dict[str, Dict]:
    """Get all badges in a category."""
    return {k: v for k, v in ALL_BADGES.items() if v.get("category") == category}

def get_badges_by_tier(tier: str) -> Dict[str, Dict]:
    """Get all badges of a specific tier."""
    return {k: v for k, v in ALL_BADGES.items() if v.get("tier") == tier}

def check_badge_requirements(badge_id: str, player_stats: Dict) -> tuple[bool, float]:
    """
    Check if player meets badge requirements.
    
    Returns:
        (earned: bool, progress: float 0.0-1.0)
    """
    badge = get_badge(badge_id)
    if not badge:
        return False, 0.0
    
    requirements = badge.get("requirements", {})
    met_requirements = []
    total_requirements = len(requirements)
    
    for req_key, req_value in requirements.items():
        player_value = player_stats.get(req_key, 0)
        
        if isinstance(req_value, dict):
            # Handle min/max requirements
            if "min" in req_value and "max" in req_value:
                met = req_value["min"] <= player_value <= req_value["max"]
            elif "min" in req_value:
                met = player_value >= req_value["min"]
            elif "max" in req_value:
                met = player_value <= req_value["max"]
            else:
                met = False
        elif isinstance(req_value, bool):
            met = player_value == req_value
        else:
            # Numeric requirement - player must meet or exceed
            met = player_value >= req_value
        
        met_requirements.append(met)
    
    earned = all(met_requirements)
    progress = sum(met_requirements) / total_requirements if total_requirements > 0 else 0.0
    
    return earned, progress

def get_all_badge_categories() -> List[str]:
    """Get list of all badge categories."""
    categories = set()
    for badge in ALL_BADGES.values():
        categories.add(badge.get("category", "other"))
    return sorted(list(categories))
