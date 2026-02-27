# Minimal college catalog. You can add more cities/tiers later.

COLLEGES = {
    "nyc_community": {
        "id": "nyc_community",
        "name": "LaGuardia Community College (CUNY)",
        "type": "community",
        "base_tuition_per_year": 5730.0,
        "notes": "Most affordable option, flexible schedule, can transfer credits; limited campus life and networking.",
        "networking_multiplier": 0.7,
        "job_opportunity_bonus": -10,
        "starting_salary_multiplier": 0.85,
        "benefits": [
            "Most affordable tuition",
            "Flexible class schedules",
            "Easy credit transfer to 4-year schools",
            "Lower class competition"
        ],
        "cons": [
            "Limited campus facilities",
            "Minimal networking events",
            "Fewer internship connections",
            "Less prestigious on resume"
        ],
        "career_paths": ["Entry-level positions", "Transfer to 4-year college", "Local businesses", "Trade careers"]
    },
    "nyc_public": {
        "id": "nyc_public",
        "name": "Hunter College (CUNY)",
        "type": "public",
        "base_tuition_per_year": 7340.0,
        "notes": "Excellent value public education; strong academics and diverse student body.",
        "networking_multiplier": 1.0,
        "job_opportunity_bonus": 0,
        "starting_salary_multiplier": 0.95,
        "benefits": [
            "Excellent value for money",
            "Strong academic reputation",
            "Diverse student community",
            "Good NYC connections"
        ],
        "cons": [
            "Larger class sizes",
            "Competitive course registration",
            "Limited on-campus housing",
            "Self-driven career support needed"
        ],
        "career_paths": ["NYC corporations", "Public sector", "Tech startups", "Graduate school"]
    },
    "nyc_mid_private": {
        "id": "nyc_mid_private",
        "name": "Pace University",
        "type": "private",
        "base_tuition_per_year": 49608.0,
        "notes": "Mid-tier private university; good career services and Manhattan location; moderate class sizes.",
        "networking_multiplier": 1.3,
        "job_opportunity_bonus": 15,
        "starting_salary_multiplier": 1.05,
        "benefits": [
            "Strong career services",
            "Manhattan location advantage",
            "Smaller class sizes",
            "Active alumni network"
        ],
        "cons": [
            "High tuition costs",
            "Competitive environment",
            "Heavy course workload",
            "Less prestigious than top-tier"
        ],
        "career_paths": ["Corporate America", "Finance industry", "Marketing firms", "Professional services"]
    },
    "nyc_private": {
        "id": "nyc_private",
        "name": "New York University (NYU)",
        "type": "private",
        "base_tuition_per_year": 60438.0,
        "notes": "Top-tier private university; prestigious reputation and excellent networking; competitive environment.",
        "networking_multiplier": 1.6,
        "job_opportunity_bonus": 30,
        "starting_salary_multiplier": 1.15,
        "benefits": [
            "Prestigious global reputation",
            "Elite alumni network",
            "Top-tier internship access",
            "Small classes with renowned professors"
        ],
        "cons": [
            "Very high tuition",
            "Intense academic pressure",
            "Competitive peer environment",
            "High cost of living expectations"
        ],
        "career_paths": ["Top tech companies", "Investment banking", "Consulting firms", "Fortune 500 leadership"]
    },
}
