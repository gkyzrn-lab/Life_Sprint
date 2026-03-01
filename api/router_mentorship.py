"""
Mentorship & Networking Router

Provides:
- Virtual mentorship connections
- Industry networking events
- Skill development through mentorship
- Career advancement through networking
"""

from fastapi import APIRouter, HTTPException

from core_domain.store import STORE
from catalogs.mentorship_networking import (
    get_mentor_recommendations,
    get_networking_events_for_player,
    simulate_networking_event_outcome,
    calculate_mentorship_impact,
    NETWORKING_EVENTS_CATALOG,
    MENTORSHIP_BENEFITS,
)

router = APIRouter(prefix="/api/mentorship", tags=["mentorship"])


@router.get("/mentors/{player_id}")
def get_mentors_for_player(player_id: str):
    """
    Get recommended mentors for a player based on skills and career goals.
    
    Returns:
    - Top 3 recommended mentors
    - Match score and explanation
    - Mentor expertise and availability
    - Success record
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    mentors = get_mentor_recommendations(player)
    
    return {
        "player_id": player_id,
        "recommended_mentors": mentors,
        "benefits_of_mentorship": MENTORSHIP_BENEFITS["For Mentee"],
        "total_available_mentors": len(mentors),
    }


@router.post("/connect/{player_id}/{mentor_id}")
def request_mentorship(player_id: str, mentor_id: str):
    """
    Request mentorship connection with a specific mentor.
    
    In production, this would:
    - Check mentor availability
    - Create mentorship relationship
    - Set up first session
    - Notify mentor
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return {
        "status": "success",
        "message": f"Mentorship request sent to {mentor_id}",
        "mentor_response_expected_in": "24-48 hours",
        "focus_skills": ["General Career Guidance"],
        "next_steps": [
            "Wait for mentor response",
            "Mentor will propose first meeting time",
            "Prepare 3-5 questions for first session",
        ],
    }


@router.get("/networking-events/{player_id}")
def get_events_for_player(player_id: str):
    """
    Get upcoming networking events relevant to player's major and interests.
    
    Shows:
    - Upcoming industry events
    - Company participants
    - Expected attendance
    - Benefits of attending
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    events = get_networking_events_for_player(player)
    
    return {
        "player_id": player_id,
        "major": getattr(player, 'major_id', 'unknown'),
        "upcoming_events": events,
        "why_attend": [
            "Meet industry professionals",
            "Learn about career paths",
            "Get referrals and opportunities",
            "Expand professional network",
        ],
        "attendance_impact": {
            "career_confidence": "+15-30",
            "network_expansion": "3-5 meaningful connections",
            "opportunity_probability": "15-40% chance of concrete opportunity",
        },
    }


@router.post("/attend-event/{player_id}/{event_id}")
def attend_networking_event(player_id: str, event_id: str):
    """
    Simulate attending a networking event.
    
    Provides:
    - Random outcome (job lead, mentor, collaboration, etc.)
    - Impact on player stats
    - New connections made
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    # Simulate event outcome
    outcome = simulate_networking_event_outcome()
    
    outcomes = {
        "job_opportunity": {
            "description": "Company recruiter was impressed and offered interview",
            "next_step": "Schedule interview",
            "impact": {"career_confidence": 30, "salary_potential": 10000},
        },
        "mentor_connection": {
            "description": "Met experienced professional who offered mentorship",
            "next_step": "Schedule first mentorship meeting",
            "impact": {"skill_growth": 20, "career_confidence": 20},
        },
        "skill_insight": {
            "description": "Learned about in-demand skills for your field",
            "next_step": "Start learning recommended skills",
            "impact": {"knowledge": 15},
        },
        "project_collaboration": {
            "description": "Found collaborators for an exciting project",
            "next_step": "Plan first project meeting",
            "impact": {"experience": 25, "network": 15},
        },
    }
    
    outcome_data = outcomes.get(outcome, {})
    
    return {
        "event_id": event_id,
        "outcome": outcome,
        "description": outcome_data.get("description", ""),
        "next_step": outcome_data.get("next_step", ""),
        "impact": outcome_data.get("impact", {}),
        "new_connections_made": 3,
        "learning_points": 5,
    }


@router.get("/mentorship-benefits")
def mentorship_benefits_overview():
    """
    Get overview of mentorship program benefits for mentees and mentors.
    """
    return {
        "program_overview": "Virtual mentorship connecting experienced professionals with emerging talent",
        "benefits_for_mentees": list(MENTORSHIP_BENEFITS["For Mentee"].values()),
        "benefits_for_mentors": list(MENTORSHIP_BENEFITS["For Mentor"].values()),
        "typical_mentorship_duration": "6-12 months",
        "frequency": "2 sessions/month typical",
        "outcomes": {
            "successful_transitions": "60% of mentees secure better positions",
            "salary_improvement": "Average 15-20% salary increase after mentorship",
            "skill_growth": "Average +25% in targeted skill areas",
        },
    }


@router.get("/skill-pairing")
def skill_pairing_guide():
    """
    Get guide on which mentors to seek for specific skills.
    
    Shows:
    - Which skills pair well together
    - Recommended learning sequences
    - Expected learning timelines
    """
    from catalogs.mentorship_networking import MENTORSHIP_SKILL_MATRIX
    
    return {
        "skill_matrix": MENTORSHIP_SKILL_MATRIX,
        "guide": {
            "how_to_use": "Find your current strongest skill, see what pairs well",
            "tip": "Combining complementary skills increases career value exponentially",
            "example": "Python (programming) + Data Analysis = Data Scientist role",
            "acceleration": "Mentorship can reduce learning curve by 40-50%",
        },
    }


@router.get("/all-events")
def get_all_networking_events():
    """
    Get catalog of all available networking events.
    """
    return {
        "total_events": len(NETWORKING_EVENTS_CATALOG),
        "events": NETWORKING_EVENTS_CATALOG,
        "diversity_note": "Events span all major industries and skill levels",
    }


@router.get("/mentorship-impact")
def mentorship_impact_calculator(sessions: int):
    """
    Calculate projected impact of N mentorship sessions.
    """
    if sessions <= 0:
        raise HTTPException(status_code=400, detail="Sessions must be > 0")
    
    if sessions > 24:
        raise HTTPException(status_code=400, detail="Maximum projection is 24 sessions")
    
    # Simulate with average player
    from core_domain.player.player_model import Player
    from core_domain.stats.stats_model import Stats
    from core_domain.finance.finance_models import Finance
    from catalogs.housing import HOUSING_OPTIONS
    from uuid import uuid4
    
    dummy_player = Player(
        id=str(uuid4()),
        name="Dummy",
        age=20,
        hs_gpa=3.5,
        parent_income=70000,
        major_id="computer_science",
        college_id="nyu",
        semester=1,
        year_in_school=1,
        stats=Stats(),
        finance=Finance(balance=5000),
        housing=HOUSING_OPTIONS.get("dorm"),
        job=None,
        plan=None,
        history=[],
    )
    
    impact = calculate_mentorship_impact(sessions, dummy_player)
    
    return {
        "sessions": sessions,
        "impact": impact,
        "interpretation": {
            "gpa_improvement": f"GPA could improve by {impact['gpa_improvement']:.2f} points",
            "career_confidence": f"+{impact['career_confidence']:.0f} points in career confidence",
            "skill_growth": f"+{impact['skill_growth']:.0f} points in target skill",
            "network": f"Potential +{impact['network_expansion']:.0f} valuable connections",
        },
    }
