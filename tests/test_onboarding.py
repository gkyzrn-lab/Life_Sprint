"""
Tests for onboarding and tutorial system.

Covers:
- Tutorial retrieval and metadata
- Tutorial progress tracking
- Tooltip management
- Context-specific tutorial recommendations
"""

import pytest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_get_tutorial_sequence():
    """Test fetching the recommended tutorial sequence."""
    response = client.get("/onboarding/tutorial-sequence")
    assert response.status_code == 200
    
    data = response.json()
    assert "sequence" in data
    assert "total_steps" in data
    assert data["total_steps"] == 8
    
    # Verify first few steps
    step_ids = [s["step_id"] for s in data["sequence"]]
    assert step_ids[0] == "intro_welcome"
    assert step_ids[1] == "time_budget_explain"


def test_get_tutorial_by_id():
    """Test fetching a single tutorial step by ID."""
    response = client.get("/onboarding/tutorial/intro_welcome")
    assert response.status_code == 200
    
    data = response.json()
    assert data["step_id"] == "intro_welcome"
    assert data["title"] == "Welcome to Life Sprint!"
    assert "description" in data
    assert "context" in data


def test_get_tutorial_not_found():
    """Test that requesting non-existent tutorial returns 404."""
    response = client.get("/onboarding/tutorial/nonexistent_step")
    assert response.status_code == 404


def test_get_tooltips():
    """Test fetching all available tooltips."""
    response = client.get("/onboarding/tooltips")
    assert response.status_code == 200
    
    data = response.json()
    assert "what_is_gpa" in data
    assert "what_is_stress" in data
    assert "what_is_balance" in data


def test_get_tooltip_by_id():
    """Test fetching a single tooltip by ID."""
    response = client.get("/onboarding/tooltip/what_is_gpa")
    assert response.status_code == 200
    
    data = response.json()
    assert data["tooltip_id"] == "what_is_gpa"
    assert "GPA" in data["label"]
    assert "Grade Point Average" in data["content"]


def test_get_context_tutorials():
    """Test fetching tutorials for a specific context."""
    response = client.get("/onboarding/tutorials/context/player_start")
    assert response.status_code == 200
    
    data = response.json()
    assert data["context"] == "player_start"
    assert "tutorials" in data
    assert len(data["tutorials"]) > 0
    
    # Verify one tutorial is intro_welcome
    step_ids = [t["step_id"] for t in data["tutorials"]]
    assert "intro_welcome" in step_ids


def test_player_creation_with_tutorial_state():
    """Test that new players have tutorial state initialized."""
    start_req = {
        "name": "Tutorial Test Player",
        "college_id": "nyc_public",
        "major_id": "cs",
        "housing_option_id": "dorm",
        "job_id": None,
    }
    response = client.post("/player/start", json=start_req)
    assert response.status_code == 200
    
    player = response.json()
    assert "tutorial_state" in player
    assert player["tutorial_state"]["tutorials_enabled"] is True
    assert player["tutorial_state"]["completed_steps"] == []
    assert player["tutorial_state"]["dismissed_tooltips"] == []


def test_complete_tutorial_step():
    """Test marking a tutorial step as complete."""
    # Create a player
    start_req = {
        "name": "Tutorial Complete Test",
        "college_id": "nyc_public",
        "major_id": "cs",
        "housing_option_id": "dorm",
    }
    player_response = client.post("/player/start", json=start_req)
    player_id = player_response.json()["id"]
    
    # Mark tutorial as complete
    response = client.post(
        "/onboarding/tutorial/complete",
        json={"player_id": player_id, "step_id": "intro_welcome"}
    )
    assert response.status_code == 200
    
    data = response.json()
    assert "intro_welcome" in data["completed_steps"]
    assert data["completion_percentage"] > 0


def test_dismiss_tooltip():
    """Test dismissing a tooltip."""
    # Create a player
    start_req = {
        "name": "Tooltip Dismiss Test",
        "college_id": "nyc_public",
        "major_id": "cs",
        "housing_option_id": "dorm",
    }
    player_response = client.post("/player/start", json=start_req)
    player_id = player_response.json()["id"]
    
    # Dismiss tooltip
    response = client.post(
        "/onboarding/tooltip/dismiss",
        json={"player_id": player_id, "tooltip_id": "what_is_gpa"}
    )
    assert response.status_code == 200
    
    data = response.json()
    assert "what_is_gpa" in data["dismissed_tooltips"]


def test_get_tutorial_progress():
    """Test fetching tutorial progress for a player."""
    # Create a player
    start_req = {
        "name": "Progress Test",
        "college_id": "nyc_public",
        "major_id": "cs",
        "housing_option_id": "dorm",
    }
    player_response = client.post("/player/start", json=start_req)
    player_id = player_response.json()["id"]
    
    # Complete several tutorials
    client.post(
        "/onboarding/tutorial/complete",
        json={"player_id": player_id, "step_id": "intro_welcome"}
    )
    client.post(
        "/onboarding/tutorial/complete",
        json={"player_id": player_id, "step_id": "time_budget_explain"}
    )
    
    # Get progress
    response = client.get(f"/onboarding/{player_id}/progress")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data["completed_steps"]) == 2
    assert data["completion_percentage"] > 20  # 2 out of 8 steps


def test_enable_disable_tutorials():
    """Test enabling and disabling tutorials."""
    # Create a player
    start_req = {
        "name": "Enable/Disable Test",
        "college_id": "nyc_public",
        "major_id": "cs",
        "housing_option_id": "dorm",
    }
    player_response = client.post("/player/start", json=start_req)
    player_id = player_response.json()["id"]
    
    # Verify tutorials start enabled
    response = client.get(f"/onboarding/{player_id}/progress")
    assert response.json()["tutorials_enabled"] is True
    
    # Disable tutorials
    response = client.post(f"/onboarding/{player_id}/disable-tutorials")
    assert response.status_code == 200
    assert response.json()["tutorials_enabled"] is False
    
    # Re-enable tutorials
    response = client.post(f"/onboarding/{player_id}/enable-tutorials")
    assert response.status_code == 200
    assert response.json()["tutorials_enabled"] is True
