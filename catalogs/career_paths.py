"""Career advancement paths and progression rules.

This defines:
- Promotion chains (entry → mid → senior → lead)
- Raise schedules (how much salary increases)
- Burnout mechanics (overwork leads to burnout)
- Performance factors (health, education, time in job affect advancement)
- Opportunities (leadership roles, skill unlocks)
"""

# Career progression paths: entry → mid → senior → lead
# Each path is realistic: can't skip levels, must earn through performance

CAREER_PATHS = {
    # Tech career path
    "tech_entry": {
        "title": "Junior Developer",
        "tier": "low",
        "base_salary": 65000,
        "promotion_to": "tech_mid",
        "promotion_requirements": {
            "semesters_in_role": 2,
            "min_gpa": 3.0,
            "min_performance": 70,
        }
    },
    "tech_mid": {
        "title": "Software Developer",
        "tier": "mid",
        "base_salary": 85000,
        "promotion_to": "tech_senior",
        "promotion_requirements": {
            "semesters_in_role": 3,
            "min_gpa": 3.2,
            "min_performance": 75,
        }
    },
    "tech_senior": {
        "title": "Senior Software Engineer",
        "tier": "high",
        "base_salary": 110000,
        "promotion_to": "tech_lead",
        "promotion_requirements": {
            "semesters_in_role": 3,
            "min_gpa": 3.3,
            "min_performance": 80,
        }
    },
    "tech_lead": {
        "title": "Engineering Lead / Manager",
        "tier": "startup",
        "base_salary": 140000,
        "promotion_to": None,
        "leadership": True,
    },
    
    # Finance/Business path
    "finance_entry": {
        "title": "Financial Analyst (Junior)",
        "tier": "low",
        "base_salary": 60000,
        "promotion_to": "finance_mid",
        "promotion_requirements": {
            "semesters_in_role": 2,
            "min_gpa": 3.1,
            "min_performance": 70,
        }
    },
    "finance_mid": {
        "title": "Financial Analyst",
        "tier": "mid",
        "base_salary": 78000,
        "promotion_to": "finance_senior",
        "promotion_requirements": {
            "semesters_in_role": 3,
            "min_gpa": 3.2,
            "min_performance": 75,
        }
    },
    "finance_senior": {
        "title": "Senior Analyst / Manager",
        "tier": "high",
        "base_salary": 105000,
        "promotion_to": "finance_lead",
        "promotion_requirements": {
            "semesters_in_role": 3,
            "min_gpa": 3.3,
            "min_performance": 80,
        }
    },
    "finance_lead": {
        "title": "Finance Director / VP",
        "tier": "startup",
        "base_salary": 135000,
        "promotion_to": None,
        "leadership": True,
    },
    
    # Education/Academia path
    "education_entry": {
        "title": "Teaching Assistant",
        "tier": "low",
        "base_salary": 25000,
        "promotion_to": "education_mid",
        "promotion_requirements": {
            "semesters_in_role": 2,
            "min_gpa": 3.2,
            "min_performance": 70,
        }
    },
    "education_mid": {
        "title": "Adjunct Instructor",
        "tier": "mid",
        "base_salary": 45000,
        "promotion_to": "education_senior",
        "promotion_requirements": {
            "semesters_in_role": 4,  # teaching takes longer
            "min_gpa": 3.3,
            "min_performance": 75,
        }
    },
    "education_senior": {
        "title": "Full-Time Instructor",
        "tier": "high",
        "base_salary": 65000,
        "promotion_to": "education_lead",
        "promotion_requirements": {
            "semesters_in_role": 4,
            "min_gpa": 3.4,
            "min_performance": 80,
        }
    },
    "education_lead": {
        "title": "Department Chair / Professor",
        "tier": "startup",
        "base_salary": 90000,
        "promotion_to": None,
        "leadership": True,
    },
    
    # Healthcare path
    "healthcare_entry": {
        "title": "Medical Assistant",
        "tier": "low",
        "base_salary": 32000,
        "promotion_to": "healthcare_mid",
        "promotion_requirements": {
            "semesters_in_role": 2,
            "min_gpa": 3.0,
            "min_performance": 70,
        }
    },
    "healthcare_mid": {
        "title": "Registered Nurse",
        "tier": "mid",
        "base_salary": 68000,
        "promotion_to": "healthcare_senior",
        "promotion_requirements": {
            "semesters_in_role": 3,
            "min_gpa": 3.1,
            "min_performance": 75,
        }
    },
    "healthcare_senior": {
        "title": "Senior Nurse / Specialist",
        "tier": "high",
        "base_salary": 92000,
        "promotion_to": "healthcare_lead",
        "promotion_requirements": {
            "semesters_in_role": 3,
            "min_gpa": 3.2,
            "min_performance": 80,
        }
    },
    "healthcare_lead": {
        "title": "Nursing Director / Physician",
        "tier": "startup",
        "base_salary": 125000,
        "promotion_to": None,
        "leadership": True,
    },
}

# Burnout mechanics
BURNOUT_MECHANICS = {
    "stress_to_burnout_rate": 0.15,  # 15% of job stress becomes burnout per semester
    "health_penalty_per_burnout": 0.5,  # -0.5 health per burnout point per semester
    "mental_health_penalty_per_burnout": 0.7,  # -0.7 mental health per burnout point
    "performance_penalty_per_burnout": 1.5,  # -1.5 performance per burnout point
    "burnout_cooldown_per_therapy": 10.0,  # therapy session reduces burnout by 10
    "burnout_recovery_base": 0.5,  # natural recovery is 0.5 per month of not overworking
    "critical_burnout_threshold": 75.0,  # at 75+, increased illness probability
}

# Performance modifiers
PERFORMANCE_MODIFIERS = {
    "health_factor": 0.03,  # +0.03 performance per health point (max +15 at health=50)
    "mental_health_factor": 0.02,  # +0.02 performance per mental health point
    "gpa_factor": 10.0,  # GPA directly scales performance: 3.5 GPA = +35 performance base
    "time_in_job_bonus": 5.0,  # +5 performance per semester in same role (up to 20)
    "burnout_penalty": 1.5,  # -1.5 performance per burnout point
}

# Achievement definitions for career milestones
CAREER_ACHIEVEMENTS = {
    "first_promotion": {
        "achievement_id": "first_promotion",
        "title": "Got Promoted! 📈",
        "milestone_type": "promotion",
        "description": "Earned your first promotion through hard work and performance.",
        "tier": "bronze",
    },
    "five_promotions": {
        "achievement_id": "five_promotions",
        "title": "Climber",
        "milestone_type": "promotion",
        "description": "5 promotions - you're moving up the ladder fast!",
        "tier": "silver",
    },
    "hundred_k_salary": {
        "achievement_id": "hundred_k_salary",
        "title": "Six Figures! 💰",
        "milestone_type": "raise",
        "description": "Reached $100k+ annual salary.",
        "tier": "gold",
    },
    "leadership_role": {
        "achievement_id": "leadership_role",
        "title": "Manager / Lead",
        "milestone_type": "leadership",
        "description": "Promoted to a leadership position - managing teams now.",
        "tier": "gold",
    },
    "avoid_burnout": {
        "achievement_id": "avoid_burnout",
        "title": "Work-Life Balance Achieved",
        "milestone_type": "opportunity",
        "description": "Stayed healthy and productive without burning out.",
        "tier": "silver",
    },
    "comeback_after_burnout": {
        "achievement_id": "comeback_after_burnout",
        "title": "Resilient 💪",
        "milestone_type": "opportunity",
        "description": "Recovered from burnout and got back on track.",
        "tier": "silver",
    },
    "perfect_performance": {
        "achievement_id": "perfect_performance",
        "title": "Employee of the Semester",
        "milestone_type": "opportunity",
        "description": "Achieved 95+ performance rating for an entire semester.",
        "tier": "gold",
    },
}

# Career stories - narrative moments triggered by career events
CAREER_STORIES = {
    "first_job": {
        "story_id": "first_job",
        "title": "First Day",
        "trigger": "hired",
        "condition": "first_job_ever",
        "message": "You walk into your new job, nervous but excited. They show you your desk, introduce you around. You realize: this is real life now.",
        "tone": "hopeful",
    },
    "first_paycheck": {
        "story_id": "first_paycheck",
        "title": "First Paycheck ✓",
        "trigger": "earnings_milestone",
        "condition": "after_first_month_of_work",
        "message": "Your first paycheck hits your account. Seeing your own earned money is... different. You built this.",
        "tone": "triumphant",
    },
    "promotion_earned": {
        "story_id": "promotion_earned",
        "title": "Congratulations!",
        "trigger": "promotion",
        "condition": "promotion_unlocked",
        "message": "Your manager calls you in. 'Your performance has been exceptional. We'd like to promote you.' You did it.",
        "tone": "triumphant",
        "effect": {"performance": 10, "mental_health": 5},
    },
    "burnout_warning": {
        "story_id": "burnout_warning",
        "title": "Something's Off",
        "trigger": "burnout_milestone",
        "condition": "burnout > 60",
        "message": "You're exhausted. Everything feels harder. Your manager notices you're not yourself. Maybe you need to talk to someone.",
        "tone": "cautionary",
    },
    "burnout_critical": {
        "story_id": "burnout_critical",
        "title": "🚨 You Need Help",
        "trigger": "burnout_critical",
        "condition": "burnout > 85",
        "message": "You can barely get out of bed. Work feels impossible. This isn't sustainable. You NEED to take action—therapy, time off, something.",
        "tone": "urgent",
    },
    "career_milestone": {
        "story_id": "career_milestone",
        "title": "You've Come Far",
        "trigger": "career_reflection",
        "condition": "promotions > 3",
        "message": "You think back to where you started. The positions you've held, the people you've met, the raises you've earned. You're building a real career.",
        "tone": "reflective",
    },
    "health_impact_on_job": {
        "story_id": "health_impact_on_job",
        "title": "Sick Days Add Up",
        "trigger": "health_affecting_performance",
        "condition": "health < 40 AND working",
        "message": "You're calling in sick again. You notice your manager's expression—they're starting to see you differently. Your health is affecting your reputation.",
        "tone": "cautionary",
    },
    "overwork_realization": {
        "story_id": "overwork_realization",
        "title": "Is It Worth It?",
        "trigger": "burnout_reflection",
        "condition": "burnout > 50 AND salary > 80000",
        "message": "More money, but you're miserable. You wonder: what's the point of earning if you're not living? Maybe it's time to reassess.",
        "tone": "reflective",
    },
}

# Job tier multipliers (higher tier = higher quality of life, more stress potential)
JOB_TIER_MODIFIERS = {
    "low": {
        "prestige": 1.0,
        "burnout_multiplier": 0.8,  # lower stress
        "pay_multiplier": 1.0,
    },
    "mid": {
        "prestige": 1.5,
        "burnout_multiplier": 1.0,
        "pay_multiplier": 1.3,
    },
    "high": {
        "prestige": 2.0,
        "burnout_multiplier": 1.3,  # higher stress potential
        "pay_multiplier": 1.7,
    },
    "startup": {
        "prestige": 2.5,
        "burnout_multiplier": 1.6,  # high stress, high reward
        "pay_multiplier": 2.1,
    },
}
