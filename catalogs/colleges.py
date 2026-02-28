# Minimal college catalog. You can add more cities/tiers later.

COLLEGES = {
    "cuny_baruch": {
        "id": "cuny_baruch",
        "name": "CUNY Baruch College",
        "type": "public",
        "base_tuition_per_year": 7520.0,
        "curriculum_type": "cuny_baruch",  # Maps to curriculum.py
        "offered_majors": ["ba", "accounting", "finance", "economics", "liberal_arts"],  # Business-focused public college
        "notes": "Top-ranked public business school with excellent NYC connections. Affordable but requires strong self-direction.",
        "networking_multiplier": 1.0,
        "job_opportunity_bonus": 0,
        "starting_salary_multiplier": 0.95,
        "benefits": [
            "Most affordable tuition",
            "Excellent value for money",
            "Strong NYC business connections",
            "Diverse, motivated student body",
            "Lower financial stress"
        ],
        "cons": [
            "Large class sizes (100+ students)",
            "Limited on-campus housing",
            "Competitive course registration",
            "Less hand-holding from advisors",
            "Fewer resources than private schools"
        ],
        "career_paths": ["NYC corporations", "Finance & accounting", "Public sector", "Small business", "Graduate school"]
    },
    "nyu": {
        "id": "nyu",
        "name": "New York University",
        "curriculum_type": "nyu",  # Maps to curriculum.py
        "offered_majors": ["cs", "ba", "engineering", "data_science", "economics", "finance", "communications", "psychology"],  # Comprehensive private university
        "type": "private",
        "base_tuition_per_year": 62000.0,
        "notes": "Elite private university with global prestige. Excellent resources and networking but very expensive.",
        "networking_multiplier": 1.5,
        "job_opportunity_bonus": 25,
        "starting_salary_multiplier": 1.12,
        "benefits": [
            "Prestigious global reputation",
            "Elite alumni network",
            "Excellent career services",
            "Smaller class sizes",
            "World-class professors",
            "Top-tier internship access"
        ],
        "cons": [
            "Very high tuition ($240K+ total)",
            "High academic pressure",
            "Competitive peer environment",
            "Expensive NYC lifestyle expected",
            "Heavy loan burden post-graduation"
        ],
        "career_paths": ["Investment banking", "Top tech companies", "Consulting firms", "Corporate leadership", "Startups"]
    },
    "columbia": {
        "id": "columbia",
        "name": "Columbia University",
        "curriculum_type": "columbia",  # Maps to curriculum.py
        "offered_majors": ["cs", "ba", "engineering", "data_science", "economics", "finance", "mathematics", "psychology", "politics", "history"],  # Full Ivy League offerings
        "type": "ivy_league",
        "base_tuition_per_year": 70200.0,
        "notes": "Ivy League institution with unmatched prestige and network. Most challenging and expensive option.",
        "networking_multiplier": 2.0,
        "job_opportunity_bonus": 50,
        "starting_salary_multiplier": 1.25,
        "benefits": [
            "Ivy League prestige opens doors everywhere",
            "Unmatched alumni network (CEOs, founders, leaders)",
            "World-renowned faculty",
            "Premium career placement services",
            "Exclusive networking events",
            "Highest starting salaries"
        ],
        "cons": [
            "Extremely high tuition ($270K+ total)",
            "Most academically challenging (hardest curves)",
            "Intense competition with brilliant peers",
            "High stress and burnout risk",
            "Pressure to maintain top performance",
            "Massive debt if no financial aid"
        ],
        "career_paths": ["Fortune 500 executives", "Investment banking (Goldman, JP Morgan)", "Top law/med schools", "Silicon Valley leadership", "Government & policy"]
    },
}
