# Health achievements and milestones - celebratory progression system
# These unlock as players build healthy habits, keeping engagement high

HEALTH_ACHIEVEMENTS = {
    # Exercise Milestones
    "first_workout": {
        "id": "first_workout",
        "title": "Getting Started",
        "description": "Complete your first exercise session",
        "trigger_type": "exercises_completed",
        "trigger_value": 1,
        "reward": {
            "message": "💪 Great job! You took the first step toward better health!",
            "bonus_fitness_multiplier": 1.05,  # 5% boost to future fitness gains
            "unlock_info": "You're on your way to building a habit!",
        },
        "tier": "bronze",
    },
    "5k_runner": {
        "id": "5k_runner",
        "title": "Distance Runner",
        "description": "Exercise 5 times in total",
        "trigger_type": "exercises_completed",
        "trigger_value": 5,
        "reward": {
            "message": "🏃 Five down! You're building serious momentum!",
            "bonus_fitness_multiplier": 1.10,
            "stress_reduction_bonus": 2.0,
            "unlock_info": "Unlocked: Fitness Coach role unlock",
        },
        "tier": "silver",
    },
    "gym_rat": {
        "id": "gym_rat",
        "title": "Gym Regular",
        "description": "Visit the gym 10 times",
        "trigger_type": "gym_sessions",
        "trigger_value": 10,
        "reward": {
            "message": "🏋️ You're a gym regular now! Gym membership discount unlocked!",
            "gym_cost_reduction": 0.20,  # 20% cheaper gym membership
            "unlock_info": "Your local gym knows your name!",
        },
        "tier": "silver",
    },
    "workout_warrior": {
        "id": "workout_warrior",
        "title": "Workout Warrior",
        "description": "Complete 20 exercises total",
        "trigger_type": "exercises_completed",
        "trigger_value": 20,
        "reward": {
            "message": "⚡ BEAST MODE ACTIVATED! You're unstoppable!",
            "bonus_fitness_multiplier": 1.15,
            "permanent_health_regen": 1.0,  # Passive health improvement per semester
            "unlock_info": "You've mastered the habit of exercise",
        },
        "tier": "gold",
    },
    
    # Mental Health Milestones
    "mental_health_advocate": {
        "id": "mental_health_advocate",
        "title": "Mental Health Advocate",
        "description": "Attend 4 therapy sessions",
        "trigger_type": "therapy_sessions",
        "trigger_value": 4,
        "reward": {
            "message": "🧠 You're taking mental health seriously! That takes courage!",
            "therapy_cost_reduction": 0.15,  # 15% cheaper therapy
            "stress_reduction_bonus": 3.0,
            "unlock_info": "You understand that mental health matters",
        },
        "tier": "silver",
    },
    "zen_master": {
        "id": "zen_master",
        "title": "Zen Master",
        "description": "Attend 10 therapy/meditation sessions",
        "trigger_type": "mental_sessions",
        "trigger_value": 10,
        "reward": {
            "message": "🧘 You've achieved mental clarity! Stress no longer controls you.",
            "permanent_stress_reduction": 5.0,  # Base stress always 5 lower
            "mental_health_efficiency": 1.20,  # Therapy 20% more effective
            "unlock_info": "Unlocked: Inner Peace pathway",
        },
        "tier": "gold",
    },
    
    # Streak Milestones
    "on_fire": {
        "id": "on_fire",
        "title": "On Fire! 🔥",
        "description": "Build a 3-day exercise streak",
        "trigger_type": "exercise_streak",
        "trigger_value": 3,
        "reward": {
            "message": "🔥 Three days strong! You're building a real habit!",
            "fitness_multiplier": 1.08,
            "streak_motivation_bonus": 1.05,  # Streaks are 5% more powerful
        },
        "tier": "silver",
    },
    "unstoppable": {
        "id": "unstoppable",
        "title": "Unstoppable",
        "description": "Build a 7-day exercise streak",
        "trigger_type": "exercise_streak",
        "trigger_value": 7,
        "reward": {
            "message": "⭐ ONE WEEK OF CONSISTENCY! You're literally unstoppable now!",
            "fitness_multiplier": 1.15,
            "unlock_role": "fitness_coach",
            "unlock_info": "You've proven you can commit. The world sees your dedication.",
        },
        "tier": "gold",
    },
    
    # Preventive Care
    "clean_bill_of_health": {
        "id": "clean_bill_of_health",
        "title": "Clean Bill of Health",
        "description": "Go 4 semesters without any illness",
        "trigger_type": "healthy_streak",
        "trigger_value": 4,
        "reward": {
            "message": "✨ PERFECT HEALTH! Your immune system is legendary!",
            "illness_probability_reduction": 0.30,  # 30% less likely to get sick
            "permanent_health": 5.0,
            "unlock_info": "Your body is a fortress",
        },
        "tier": "gold",
    },
    "preventive_pro": {
        "id": "preventive_pro",
        "title": "Preventive Pro",
        "description": "Schedule 3 medical checkups",
        "trigger_type": "checkups_completed",
        "trigger_value": 3,
        "reward": {
            "message": "🏥 You understand prevention! Smart thinking!",
            "checkup_cost_reduction": 0.25,  # 25% cheaper checkups
            "illness_severity_reduction": 0.20,  # When sick, recover 20% faster
            "unlock_info": "You're ahead of the curve on healthcare",
        },
        "tier": "silver",
    },
    
    # Wisdom Milestones
    "health_wisdom": {
        "id": "health_wisdom",
        "title": "Health Wisdom",
        "description": "Combine: exercise 10x, therapy 5x, and checkup 2x",
        "trigger_type": "combined_health_action",
        "trigger_value": {"exercises": 10, "therapy": 5, "checkups": 2},
        "reward": {
            "message": "🌟 You've mastered the balanced life! Exercise, mental care, AND prevention!",
            "all_health_multiplier": 1.20,
            "gpa_bonus": 0.15,  # +0.15 GPA bonus from better health
            "unlock_info": "You understand that true health is holistic",
        },
        "tier": "platinum",
    },
}

# Achievement Tiers (for UI display)
ACHIEVEMENT_TIERS = {
    "bronze": {
        "color": "#CD7F32",
        "icon": "🥉",
        "description": "First steps"
    },
    "silver": {
        "color": "#C0C0C0",
        "icon": "🥈",
        "description": "Building momentum"
    },
    "gold": {
        "color": "#FFD700",
        "icon": "🥇",
        "description": "Mastery unlocked"
    },
    "platinum": {
        "color": "#E5E4E2",
        "icon": "💎",
        "description": "True balance"
    },
}
