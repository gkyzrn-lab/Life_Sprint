"""
Tests for Career Recommendations System
"""

from fastapi.testclient import TestClient
from uuid import uuid4

from main import app
from core_domain.store import STORE
from core_domain.player.player_model import Player
from core_domain.stats.stats_model import Stats
from core_domain.finance.finance_models import Finance
from catalogs.housing import HOUSING_OPTIONS

client = TestClient(app)


def create_test_player(major_id: str = "computer_science", gpa: float = 3.5) -> Player:
    """Create a test player with specified major and GPA."""
    player = Player(
        id=str(uuid4()),
        name="Test Player",
        age=20,
        hs_gpa=gpa,  # Use hs_gpa field
        parent_income=75000,
        major_id=major_id,
        college_id="nyu",
        semester=1,
        year_in_school=1,
        stats=Stats(),
        finance=Finance(balance=5000),
        housing=HOUSING_OPTIONS.get("dorm"),  # Default housing
        job=None,
        plan=None,
        history=[],
    )
    STORE.put_player(player)
    return player


def test_career_recommendations_endpoint():
    """Test that recommendations endpoint returns proper recommendations."""
    player = create_test_player(major_id="computer_science", gpa=3.7)
    
    resp = client.get(f"/api/career/recommendations/{player.id}")
    assert resp.status_code == 200
    
    data = resp.json()
    assert "player_id" in data
    assert "major" in data
    assert "gpa" in data
    assert "recommendations" in data
    
    recs = data["recommendations"]
    assert "primary_recommendation" in recs
    assert "alternative_recommendations" in recs
    assert "market_insights" in recs
    assert "salary_projections" in recs


def test_career_recommendations_for_cs_major():
    """Test that CS major gets tech recommendations."""
    player = create_test_player(major_id="computer_science", gpa=3.8)
    
    resp = client.get(f"/api/career/recommendations/{player.id}")
    assert resp.status_code == 200
    
    data = resp.json()
    primary = data["recommendations"]["primary_recommendation"]
    
    # CS grads should get tech/data recommendations
    assert primary["path_id"] in ["tech_entry", "data_entry", "ai_entry"]
    assert primary["alignment_score"] >= 70


def test_career_recommendations_for_finance_major():
    """Test that Finance major gets finance recommendations."""
    player = create_test_player(major_id="finance", gpa=3.6)
    
    resp = client.get(f"/api/career/recommendations/{player.id}")
    assert resp.status_code == 200
    
    data = resp.json()
    primary = data["recommendations"]["primary_recommendation"]
    
    # Finance major should get finance/business recommendations
    assert primary["path_id"] in ["finance_entry", "trading_entry", "business_entry"]


def test_career_recommendations_gpa_impact():
    """Test that higher GPA improves alignment scores."""
    player_low = create_test_player(major_id="computer_science", gpa=2.5)
    player_high = create_test_player(major_id="computer_science", gpa=3.9)
    
    resp_low = client.get(f"/api/career/recommendations/{player_low.id}")
    resp_high = client.get(f"/api/career/recommendations/{player_high.id}")
    
    assert resp_low.status_code == 200
    assert resp_high.status_code == 200
    
    score_low = resp_low.json()["recommendations"]["primary_recommendation"]["alignment_score"]
    score_high = resp_high.json()["recommendations"]["primary_recommendation"]["alignment_score"]
    
    # Higher GPA should yield higher score
    assert score_high > score_low


def test_market_overview_endpoint():
    """Test job market overview endpoint."""
    resp = client.get("/api/career/market-overview")
    assert resp.status_code == 200
    
    data = resp.json()
    assert "summary" in data
    assert "hottest_fields" in data
    assert "emerging_trends" in data
    assert "salary_insights" in data
    
    # Verify hottest fields structure
    assert len(data["hottest_fields"]) >= 3
    for field in data["hottest_fields"]:
        assert "field" in field
        assert "demand" in field
        assert "growth_rate" in field


def test_major_alignment_endpoint():
    """Test major-to-career alignment endpoint."""
    resp = client.get("/api/career/major-alignment/computer_science")
    assert resp.status_code == 200
    
    data = resp.json()
    assert data["major"] == "computer_science"
    assert "recommended_paths" in data
    assert "total_paths" in data
    
    # CS should have multiple paths
    assert len(data["recommended_paths"]) >= 2


def test_salary_comparison_endpoint():
    """Test salary comparison endpoint."""
    resp = client.get("/api/career/salary-comparison")
    assert resp.status_code == 200
    
    data = resp.json()
    assert "comparisons" in data
    
    # Verify salary structure
    for comparison in data["comparisons"]:
        assert "field" in comparison
        assert "entry_salary" in comparison
        assert "mid_salary" in comparison
        assert "senior_salary" in comparison


def test_skill_roadmap_endpoint():
    """Test skill roadmap for specific career paths."""
    resp = client.get("/api/career/skill-roadmap/tech_entry")
    assert resp.status_code == 200
    
    data = resp.json()
    assert "path" in data
    assert "critical_skills" in data
    assert "progression" in data
    
    # Verify skills structure
    assert len(data["critical_skills"]) >= 2
    for skill in data["critical_skills"]:
        assert "name" in skill
        assert "timeframe" in skill
        assert "resources" in skill
    
    # Verify progression levels
    assert len(data["progression"]) >= 3
    for level in data["progression"]:
        assert "level" in level
        assert "timeline" in level


def test_skill_roadmap_invalid_path():
    """Test skill roadmap with invalid path returns 404."""
    resp = client.get("/api/career/skill-roadmap/invalid_path_xyz")
    assert resp.status_code == 404


def test_player_not_found():
    """Test that non-existent player returns 404."""
    resp = client.get("/api/career/recommendations/invalid-player-id")
    assert resp.status_code == 404


def test_alternative_recommendations():
    """Test that alternative recommendations are provided."""
    player = create_test_player(major_id="computer_science", gpa=3.7)
    
    resp = client.get(f"/api/career/recommendations/{player.id}")
    assert resp.status_code == 200
    
    data = resp.json()
    alts = data["recommendations"]["alternative_recommendations"]
    
    # Should have 1-2 alternatives
    assert len(alts) >= 1
    
    # Alternatives should have lower scores than primary
    primary_score = data["recommendations"]["primary_recommendation"]["alignment_score"]
    for alt in alts:
        assert alt["alignment_score"] <= primary_score


def test_salary_projections():
    """Test salary projection data in recommendations."""
    player = create_test_player(major_id="computer_science", gpa=3.8)
    
    resp = client.get(f"/api/career/recommendations/{player.id}")
    assert resp.status_code == 200
    
    data = resp.json()
    projections = data["recommendations"]["salary_projections"]
    
    assert "entry_level_salary" in projections
    assert "mid_career_salary" in projections
    assert "senior_level_salary" in projections
    assert "years_to_senior" in projections
    
    # Verify salary progression
    assert projections["mid_career_salary"] > projections["entry_level_salary"]
    assert projections["senior_level_salary"] > projections["mid_career_salary"]


def test_skill_development_roadmap():
    """Test skill development recommendations."""
    player = create_test_player(major_id="computer_science", gpa=3.8)
    
    resp = client.get(f"/api/career/recommendations/{player.id}")
    assert resp.status_code == 200
    
    data = resp.json()
    skills = data["recommendations"]["skill_development"]
    
    # Should have skill recommendations for CS major
    assert len(skills) >= 1
    
    for skill in skills:
        assert "skill" in skill
        assert "importance" in skill
        assert "action" in skill
