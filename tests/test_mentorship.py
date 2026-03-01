"""
Tests for Mentorship & Networking System

Coverage:
- Mentor recommendations
- Networking event listing
- Event attendance outcomes
- Benefits calculations
- Skill pairing guidance
"""

import pytest
from fastapi.testclient import TestClient
from uuid import uuid4

from main import app
from core_domain.store import STORE
from core_domain.player.player_model import Player
from core_domain.stats.stats_model import Stats
from core_domain.finance.finance_models import Finance
from catalogs.housing import HOUSING_OPTIONS

client = TestClient(app)


@pytest.fixture
def test_player():
    """Create a test player for mentorship tests."""
    player = Player(
        id=str(uuid4()),
        name="Test Mentee",
        age=20,
        hs_gpa=3.6,
        parent_income=75000,
        major_id="computer_science",
        college_id="nyu",
        semester=2,
        year_in_school=1,
        stats=Stats(),
        finance=Finance(balance=8000),
        housing=HOUSING_OPTIONS["dorm"],
        job=None,
        plan=None,
        history=[],
    )
    STORE.put_player(player)
    return player


def test_get_mentor_recommendations(test_player):
    """Test retrieving mentor recommendations for a player."""
    response = client.get(f"/api/mentorship/mentors/{test_player.id}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "player_id" in data
    assert "recommended_mentors" in data
    assert "benefits_of_mentorship" in data
    assert "total_available_mentors" in data
    
    # CS major should get mentors
    mentors = data["recommended_mentors"]
    assert len(mentors) > 0
    assert len(mentors) <= 3  # Top 3
    
    # Each mentor should have required fields
    for mentor in mentors:
        assert "mentor_id" in mentor
        assert "name" in mentor
        assert "fit_score" in mentor


def test_get_mentor_recommendations_nonexistent_player():
    """Test mentor recommendations with non-existent player."""
    response = client.get(f"/api/mentorship/mentors/nonexistent-id-12345")
    
    assert response.status_code == 404


def test_request_mentorship(test_player):
    """Test requesting mentorship connection."""
    response = client.post(
        f"/api/mentorship/connect/{test_player.id}/mentor-001"
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["status"] == "success"
    assert "message" in data
    assert "next_steps" in data
    assert len(data["next_steps"]) > 0


def test_request_mentorship_nonexistent_player():
    """Test mentorship request with non-existent player."""
    response = client.post(
        f"/api/mentorship/connect/nonexistent-id-12345/mentor-001"
    )
    
    assert response.status_code == 404


def test_get_networking_events(test_player):
    """Test retrieving networking events for a player."""
    response = client.get(f"/api/mentorship/networking-events/{test_player.id}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "player_id" in data
    assert "major" in data
    assert "upcoming_events" in data
    assert "why_attend" in data
    assert "attendance_impact" in data
    
    # Should have some events for CS major
    events = data["upcoming_events"]
    assert len(events) > 0
    
    # Each event should have required fields
    for event in events:
        assert "name" in event
        assert "industry" in event


def test_get_networking_events_nonexistent_player():
    """Test networking events with non-existent player."""
    response = client.get(f"/api/mentorship/networking-events/nonexistent-id-12345")
    
    assert response.status_code == 404


def test_attend_networking_event(test_player):
    """Test attending a networking event."""
    response = client.post(
        f"/api/mentorship/attend-event/{test_player.id}/event-tech-mixer"
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert "event_id" in data
    assert "outcome" in data
    assert "description" in data
    assert "next_step" in data
    assert "impact" in data
    assert "new_connections_made" in data
    
    # Outcome should be one of the valid types
    valid_outcomes = ["job_opportunity", "mentor_connection", "skill_insight", "project_collaboration"]
    assert data["outcome"] in valid_outcomes
    
    # Impact should contain metrics
    impact = data["impact"]
    assert isinstance(impact, dict)


def test_attend_networking_event_nonexistent_player():
    """Test event attendance with non-existent player."""
    response = client.post(
        f"/api/mentorship/attend-event/nonexistent-id-12345/event-001"
    )
    
    assert response.status_code == 404


def test_mentorship_benefits_overview():
    """Test getting mentorship program benefits overview."""
    response = client.get("/api/mentorship/mentorship-benefits")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "program_overview" in data
    assert "benefits_for_mentees" in data
    assert "benefits_for_mentors" in data
    assert "outcomes" in data
    
    # Check structure - should be lists of strings
    assert isinstance(data["benefits_for_mentees"], list)
    assert isinstance(data["benefits_for_mentors"], list)
    assert len(data["benefits_for_mentees"]) > 0


def test_skill_pairing_guide():
    """Test skill pairing guide."""
    response = client.get("/api/mentorship/skill-pairing")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "skill_matrix" in data
    assert "guide" in data
    
    # Skill matrix should map skills to complementary skills
    matrix = data["skill_matrix"]
    assert isinstance(matrix, dict)
    
    # At least one skill should be in matrix
    if matrix:
        first_skill = next(iter(matrix.keys()))
        assert isinstance(matrix[first_skill], list)


def test_get_all_networking_events():
    """Test getting all available networking events."""
    response = client.get("/api/mentorship/all-events")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "total_events" in data
    assert "events" in data
    assert data["total_events"] > 0
    assert len(data["events"]) == data["total_events"]


def test_mentorship_impact_calculator():
    """Test mentorship impact calculation."""
    response = client.get("/api/mentorship/mentorship-impact?sessions=6")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["sessions"] == 6
    assert "impact" in data
    assert "interpretation" in data
    
    impact = data["impact"]
    assert "gpa_improvement" in impact
    assert "career_confidence" in impact
    assert "skill_growth" in impact


def test_mentorship_impact_zero_sessions():
    """Test impact calculator rejects 0 sessions."""
    response = client.get("/api/mentorship/mentorship-impact?sessions=0")
    
    assert response.status_code == 400


def test_mentorship_impact_excessive_sessions():
    """Test impact calculator rejects > 24 sessions."""
    response = client.get("/api/mentorship/mentorship-impact?sessions=25")
    
    assert response.status_code == 400


def test_mentorship_impact_multiple_sessions():
    """Test impact calculation scales with session count."""
    response_3 = client.get("/api/mentorship/mentorship-impact?sessions=3")
    response_12 = client.get("/api/mentorship/mentorship-impact?sessions=12")
    
    assert response_3.status_code == 200
    assert response_12.status_code == 200
    
    data_3 = response_3.json()
    data_12 = response_12.json()
    
    # More sessions should yield more benefit
    assert data_12["impact"]["gpa_improvement"] > data_3["impact"]["gpa_improvement"]
    assert data_12["impact"]["career_confidence"] > data_3["impact"]["career_confidence"]


def test_network_event_diversity():
    """Test that networking events cover multiple industries."""
    response = client.get("/api/mentorship/all-events")
    
    assert response.status_code == 200
    data = response.json()
    events = data["events"]
    
    # Collect industries
    industries = set()
    for event in events:
        if "industry" in event:
            industries.add(event["industry"])
    
    # Should have diversity
    assert len(industries) > 1


def test_mentor_recommendations_different_majors(test_player):
    """Test that mentor recommendations work for different majors."""
    # Test for CS major
    response_cs = client.get(f"/api/mentorship/mentors/{test_player.id}")
    assert response_cs.status_code == 200
    
    # Create and test finance major student
    finance_player = Player(
        id=str(uuid4()),
        name="Finance Student",
        age=21,
        hs_gpa=3.7,
        parent_income=100000,
        major_id="finance",
        college_id="nyu",
        semester=2,
        year_in_school=1,
        stats=Stats(),
        finance=Finance(balance=10000),
        housing=HOUSING_OPTIONS["dorm"],
        job=None,
        plan=None,
        history=[],
    )
    STORE.put_player(finance_player)
    
    response_finance = client.get(f"/api/mentorship/mentors/{finance_player.id}")
    assert response_finance.status_code == 200
    
    # Both should get mentors
    cs_mentors = response_cs.json()["recommended_mentors"]
    finance_mentors = response_finance.json()["recommended_mentors"]
    
    # They should be lists (may be empty if no mentors match)
    assert isinstance(cs_mentors, list)
    assert isinstance(finance_mentors, list)


def test_event_attendance_consistency(test_player):
    """Test that event attendance returns consistent structure."""
    # Attend same event multiple times - should always have valid structure
    for _ in range(3):
        response = client.post(
            f"/api/mentorship/attend-event/{test_player.id}/event-tech-mixer"
        )
        
        assert response.status_code == 200
        data = response.json()
        
        # All required fields present
        assert "outcome" in data
        assert "description" in data
        assert "impact" in data
        assert data["new_connections_made"] > 0
