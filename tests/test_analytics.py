"""
Tests for Analytics & Gamification System

Coverage:
- Player analytics dashboards
- Leaderboards and rankings
- Achievement system
- Career milestones
- Decision impact analysis
- Graduation readiness
- XP and leveling system
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
    """Create a test player for analytics tests."""
    player = Player(
        id=str(uuid4()),
        name="Analytics Pro",
        age=21,
        hs_gpa=3.6,
        parent_income=80000,
        major_id="computer_science",
        college_id="nyu",
        semester=3,
        year_in_school=2,
        stats=Stats(),
        finance=Finance(balance=15000),
        housing=HOUSING_OPTIONS["dorm"],
        job=None,
        plan=None,
        history=[],
    )
    STORE.put_player(player)
    return player


def test_get_analytics_dashboard(test_player):
    """Test retrieving analytics dashboard."""
    response = client.get(f"/api/analytics/dashboard/{test_player.id}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "player_id" in data
    assert "player_name" in data
    assert "level" in data
    assert "total_xp" in data
    assert "key_metrics" in data
    assert "achievements_earned" in data


def test_get_analytics_dashboard_nonexistent():
    """Test analytics dashboard with non-existent player."""
    response = client.get("/api/analytics/dashboard/nonexistent-12345")
    
    assert response.status_code == 404


def test_get_player_rank(test_player):
    """Test retrieving player rank."""
    response = client.get(f"/api/analytics/rank/{test_player.id}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "player_id" in data
    assert "rankings" in data
    assert "overall_percentile" in data
    
    rankings = data["rankings"]
    assert "gpa_percentile" in rankings
    assert "happiness_percentile" in rankings
    assert "career_readiness" in rankings


def test_get_player_rank_nonexistent():
    """Test player rank with non-existent player."""
    response = client.get("/api/analytics/rank/nonexistent-12345")
    
    assert response.status_code == 404


def test_get_leaderboard():
    """Test retrieving leaderboard."""
    response = client.get("/api/analytics/leaderboards/overall_xp")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "category" in data
    assert "leaderboard" in data
    assert data["category"] == "overall_xp"
    
    leaderboard = data["leaderboard"]
    assert len(leaderboard) > 0
    
    # Check first entry
    if leaderboard:
        assert "rank" in leaderboard[0]
        assert "name" in leaderboard[0]


def test_get_leaderboard_categories():
    """Test all available leaderboard categories."""
    categories = [
        "overall_xp",
        "gpa",
        "career_readiness",
        "community_impact",
        "financial_health",
        "happiness",
        "graduation_readiness",
    ]
    
    for category in categories:
        response = client.get(f"/api/analytics/leaderboards/{category}")
        assert response.status_code == 200


def test_get_invalid_leaderboard():
    """Test invalid leaderboard category."""
    response = client.get("/api/analytics/leaderboards/invalid_category")
    
    assert response.status_code == 400


def test_get_all_achievements():
    """Test retrieving all achievements."""
    response = client.get("/api/analytics/achievements")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "total_achievements" in data
    assert "achievements" in data
    assert "rarity_breakdown" in data
    
    achievements = data["achievements"]
    assert len(achievements) > 0
    
    for achievement in achievements:
        assert "name" in achievement
        assert "icon" in achievement
        assert "rarity" in achievement


def test_unlock_achievement(test_player):
    """Test unlocking an achievement."""
    response = client.post(
        f"/api/analytics/achievement/unlock/{test_player.id}/honor_student"
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["status"] == "unlocked"
    assert "achievement_name" in data
    assert "xp_earned" in data


def test_unlock_invalid_achievement(test_player):
    """Test unlocking invalid achievement."""
    response = client.post(
        f"/api/analytics/achievement/unlock/{test_player.id}/invalid_achievement"
    )
    
    assert response.status_code == 404


def test_unlock_achievement_nonexistent_player():
    """Test achievement unlock with non-existent player."""
    response = client.post(
        "/api/analytics/achievement/unlock/nonexistent-12345/honor_student"
    )
    
    assert response.status_code == 404


def test_get_career_milestones():
    """Test retrieving career milestones."""
    response = client.get("/api/analytics/career-milestones")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "total_milestones" in data
    assert "milestones" in data
    assert "progression_path" in data
    
    milestones = data["milestones"]
    assert len(milestones) > 0
    
    for milestone in milestones:
        assert "milestone" in milestone
        assert "xp_reward" in milestone


def test_analyze_decision():
    """Test decision impact analysis."""
    response = client.get("/api/analytics/decision-analysis/academic?outcome=success")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "decision_type" in data
    assert "outcome" in data
    assert "impact_on_stats" in data
    assert "severity" in data


def test_analyze_decision_failure():
    """Test decision impact for failure outcome."""
    response = client.get("/api/analytics/decision-analysis/financial?outcome=failure")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["outcome"] == "failure"
    impact = data["impact_on_stats"]
    # Failure should have negative impacts
    assert len(impact) > 0


def test_analyze_invalid_decision_type():
    """Test invalid decision type."""
    response = client.get("/api/analytics/decision-analysis/invalid_type")
    
    assert response.status_code == 400


def test_get_xp_system():
    """Test retrieving XP system information."""
    response = client.get("/api/analytics/xp-system")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "activities" in data
    assert "level_progression" in data
    assert "max_level" in data
    
    # Check that activities have XP values
    for activity_id, activity_data in data["activities"].items():
        assert "xp" in activity_data
        assert "description" in activity_data


def test_record_decision(test_player):
    """Test recording a decision."""
    response = client.post(
        f"/api/analytics/decision-record/{test_player.id}?decision_type=academic&outcome=success&notes=Good semester"
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["status"] == "recorded"
    assert "decision_record" in data
    assert data["decision_record"]["decision_type"] == "academic"


def test_record_decision_nonexistent_player():
    """Test decision recording with non-existent player."""
    response = client.post(
        "/api/analytics/decision-record/nonexistent-12345?decision_type=career&outcome=success"
    )
    
    assert response.status_code == 404


def test_get_graduation_readiness(test_player):
    """Test graduation readiness assessment."""
    response = client.get(f"/api/analytics/graduation-readiness/{test_player.id}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "player_id" in data
    assert "readiness_score" in data
    assert "recommendations" in data
    
    readiness = data["readiness_score"]
    assert "overall_readiness" in readiness
    assert "academic_readiness" in readiness
    assert "career_readiness" in readiness
    assert "financial_readiness" in readiness


def test_graduation_readiness_nonexistent():
    """Test graduation readiness with non-existent player."""
    response = client.get("/api/analytics/graduation-readiness/nonexistent-12345")
    
    assert response.status_code == 404


def test_get_impact_tracking(test_player):
    """Test decision-outcome impact tracking."""
    response = client.get(f"/api/analytics/impact-tracking/{test_player.id}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "player_id" in data
    assert "total_decisions_tracked" in data
    assert "success_rate" in data
    assert "decision_breakdown" in data
    assert "insights" in data


def test_impact_tracking_nonexistent():
    """Test impact tracking with non-existent player."""
    response = client.get("/api/analytics/impact-tracking/nonexistent-12345")
    
    assert response.status_code == 404


def test_get_progression_summary(test_player):
    """Test overall progression summary."""
    response = client.get(f"/api/analytics/progression-summary/{test_player.id}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "player_id" in data
    assert "player_name" in data
    assert "current_semester" in data
    assert "overall_progress" in data
    assert "key_achievements" in data
    assert "graduation_confidence" in data


def test_progression_summary_nonexistent():
    """Test progression summary with non-existent player."""
    response = client.get("/api/analytics/progression-summary/nonexistent-12345")
    
    assert response.status_code == 404


def test_leaderboard_limit():
    """Test leaderboard with different limits."""
    response_5 = client.get("/api/analytics/leaderboards/overall_xp?limit=5")
    response_20 = client.get("/api/analytics/leaderboards/overall_xp?limit=20")
    
    assert response_5.status_code == 200
    assert response_20.status_code == 200


def test_achievements_rarity_distribution():
    """Test achievement rarity breakdown."""
    response = client.get("/api/analytics/achievements")
    
    assert response.status_code == 200
    data = response.json()
    
    rarity = data["rarity_breakdown"]
    total = sum(rarity.values())
    assert total > 0


def test_decision_categories_coverage():
    """Test decision analysis covers all categories."""
    categories = ["academic", "financial", "health", "social", "career"]
    
    for category in categories:
        response = client.get(f"/api/analytics/decision-analysis/{category}")
        assert response.status_code == 200
        data = response.json()
        assert data["decision_type"] == category


def test_multiple_decisions_recorded(test_player):
    """Test recording multiple decisions for player."""
    decisions = [
        ("academic", "success"),
        ("career", "success"),
        ("financial", "failure"),
        ("health", "success"),
    ]
    
    for decision_type, outcome in decisions:
        response = client.post(
            f"/api/analytics/decision-record/{test_player.id}?decision_type={decision_type}&outcome={outcome}"
        )
        assert response.status_code == 200
