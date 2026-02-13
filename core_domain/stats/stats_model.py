from pydantic import BaseModel


class Stats(BaseModel):
    gpa: float = 0.0
    total_credits: int = 0

    stress: float = 20.0
    happiness: float = 70.0
    eq: float = 10.0

    burnout: float = 0.0

    # planning / emergency system
    emergency_tokens: int = 1

    # Skills (for side gigs and career progression)
    technical_skills: float = 0.0  # Coding, design, etc. (0-100)
    communication_skills: float = 50.0  # Writing, presentation, etc. (0-100)
    time_management: float = 40.0  # Organization, efficiency (0-100)
    business_acumen: float = 0.0  # Business strategy, marketing (0-100)
    energy_level: float = 100.0  # Energy for work (0-100, replenishes with sleep)
