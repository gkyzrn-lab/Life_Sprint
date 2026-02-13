# Health-related medical costs, fitness options, conditions, and treatments

MEDICAL_COSTS = {
    "doctor_visit": 150.0,
    "specialist_visit": 300.0,
    "therapy_session": 100.0,
    "annual_checkup": 200.0,
    "urgent_care": 300.0,
    "emergency_room": 1500.0,
    "prescription": 50.0,
}

# Insurance reduces costs by this percentage
INSURANCE_COST_REDUCTION = 0.4  # 40% reduction with insurance

FITNESS_OPTIONS = {
    "gym_membership": {
        "id": "gym_membership",
        "name": "Gym Membership",
        "monthly_cost": 30.0,
        "fitness_gain_per_session": 5.0,
        "sessions_per_month": 4,
        "time_hours_per_week": 3.0,
    },
    "campus_gym": {
        "id": "campus_gym",
        "name": "Campus Gym (Free)",
        "monthly_cost": 0.0,
        "fitness_gain_per_session": 3.0,
        "sessions_per_month": 2,
        "time_hours_per_week": 2.0,
    },
    "running": {
        "id": "running",
        "name": "Running/Jogging",
        "monthly_cost": 0.0,
        "fitness_gain_per_session": 4.0,
        "sessions_per_month": 3,
        "time_hours_per_week": 2.5,
    },
    "yoga": {
        "id": "yoga",
        "name": "Yoga Classes",
        "monthly_cost": 50.0,
        "fitness_gain_per_session": 3.0,
        "mental_health_gain": 5.0,
        "sessions_per_month": 3,
        "time_hours_per_week": 1.5,
    },
}

# Health conditions that can occur - ACCELERATED for better game pacing
HEALTH_CONDITIONS = {
    "cold": {
        "id": "cold",
        "name": "Common Cold",
        "severity": "mild",
        "duration_weeks": 1,  # Was 1, stays 1 (fast recovery)
        "gpa_impact": -0.2,
        "stress_impact": 5.0,
        "health_loss": 15.0,
        "probability": 0.15,
    },
    "flu": {
        "id": "flu",
        "name": "Influenza",
        "severity": "moderate",
        "duration_weeks": 2,  # Reduced from 2 (already fast)
        "gpa_impact": -0.4,
        "stress_impact": 8.0,
        "health_loss": 25.0,
        "probability": 0.08,
    },
    "broken_arm": {
        "id": "broken_arm",
        "name": "Broken Arm",
        "severity": "severe",
        "duration_weeks": 4,  # REDUCED from 8 (faster recovery feels better)
        "gpa_impact": -0.3,
        "stress_impact": 12.0,
        "health_loss": 40.0,
        "medical_cost": 5000.0,
        "probability": 0.02,
    },
    "depression": {
        "id": "depression",
        "name": "Depression",
        "severity": "moderate",
        "duration_weeks": 6,  # REDUCED from 12 (therapy helps reduce this further)
        "gpa_impact": -0.5,
        "stress_impact": 20.0,
        "health_loss": 30.0,
        "mental_health_impact": -20.0,
        "probability": 0.10,
        "therapy_accelerates": True,  # Therapy sessions cut duration in half
    },
    "sleep_deprivation": {
        "id": "sleep_deprivation",
        "name": "Chronic Sleep Deprivation",
        "severity": "moderate",
        "duration_weeks": 2,  # REDUCED from 4 (gets better with rest)
        "gpa_impact": -0.3,
        "stress_impact": 15.0,
        "health_loss": 20.0,
        "probability": 0.20,
    },
}

# Therapy/mental health support
MENTAL_HEALTH_OPTIONS = {
    "campus_counseling": {
        "id": "campus_counseling",
        "name": "Campus Counseling Services",
        "cost_per_session": 0.0,  # Free
        "sessions_per_month": 2,
        "mental_health_gain": 8.0,
        "stress_reduction": 5.0,
        "time_hours_per_session": 1.0,
    },
    "therapist": {
        "id": "therapist",
        "name": "Private Therapist",
        "cost_per_session": 100.0,
        "sessions_per_month": 2,
        "mental_health_gain": 10.0,
        "stress_reduction": 7.0,
        "time_hours_per_session": 1.0,
    },
    "meditation": {
        "id": "meditation",
        "name": "Meditation App",
        "cost_per_month": 10.0,
        "sessions_per_month": 12,
        "mental_health_gain": 4.0,
        "stress_reduction": 3.0,
        "time_hours_per_session": 0.25,
    },
}

# Health maintenance checkups
PREVENTIVE_CARE = {
    "annual_checkup": {
        "id": "annual_checkup",
        "name": "Annual Physical Exam",
        "cost": 200.0,
        "health_gain": 10.0,
        "prevents_conditions": True,
        "condition_risk_reduction": 0.2,
    },
    "teeth_cleaning": {
        "id": "teeth_cleaning",
        "name": "Dental Cleaning",
        "cost": 100.0,
        "health_gain": 5.0,
    },
    "eye_exam": {
        "id": "eye_exam",
        "name": "Eye Exam",
        "cost": 150.0,
        "health_gain": 3.0,
    },
}

# Effects of sleep quality
SLEEP_EFFECTS = {
    "excellent": {
        "min_hours": 8,
        "gpa_modifier": 0.05,
        "stress_reduction": -5.0,
        "health_gain": 2.0,
        "happiness_gain": 5.0,
    },
    "good": {
        "min_hours": 7,
        "gpa_modifier": 0.02,
        "stress_reduction": -2.0,
        "health_gain": 1.0,
        "happiness_gain": 2.0,
    },
    "poor": {
        "max_hours": 6,
        "gpa_modifier": -0.05,
        "stress_increase": 5.0,
        "health_loss": 2.0,
        "happiness_loss": 3.0,
    },
    "terrible": {
        "max_hours": 4,
        "gpa_modifier": -0.10,
        "stress_increase": 10.0,
        "health_loss": 5.0,
        "happiness_loss": 8.0,
    },
}
