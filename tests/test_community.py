"""
Tests for Community & Collaboration System

Coverage:
- Study group matching and recommendations
- Guild discovery and membership
- Collaborative project opportunities
- Community achievements
- Social activities
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
    """Create a test player for community tests."""
    player = Player(
        id=str(uuid4()),
        name="Community Builder",
        age=20,
        hs_gpa=3.5,
        parent_income=65000,
        major_id="computer_science",
        college_id="nyu",
        semester=2,
        year_in_school=1,
        stats=Stats(),
        finance=Finance(balance=5000),
        housing=HOUSING_OPTIONS["dorm"],
        job=None,
        plan=None,
        history=[],
    )
    STORE.put_player(player)
    return player


def test_get_study_groups(test_player):
    """Test retrieving study group recommendations."""
    response = client.get(f"/api/community/study-groups/{test_player.id}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "player_id" in data
    assert "major" in data
    assert "recommended_study_groups" in data
    assert "total_recommendations" in data
    
    groups = data["recommended_study_groups"]
    assert len(groups) > 0
    
    for group in groups:
        assert "name" in group
        assert "match_score" in group
        assert "current_members" in group


def test_get_study_groups_nonexistent_player():
    """Test study groups with non-existent player."""
    response = client.get("/api/community/study-groups/nonexistent-12345")
    
    assert response.status_code == 404


def test_join_study_group(test_player):
    """Test joining a study group."""
    response = client.post(
        f"/api/community/study-groups/join/{test_player.id}/Data Structures Study Circle"
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["status"] == "success"
    assert "group_name" in data
    assert "next_steps" in data
    assert data["meeting_frequency"] == "Weekly"


def test_join_study_group_nonexistent_player():
    """Test joining study group with non-existent player."""
    response = client.post(
        f"/api/community/study-groups/join/nonexistent-12345/Test Group"
    )
    
    assert response.status_code == 404


def test_get_guilds(test_player):
    """Test retrieving guild recommendations."""
    response = client.get(f"/api/community/guilds/{test_player.id}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "player_id" in data
    assert "available_guilds" in data
    assert "total_recommendations" in data
    assert "guild_benefits" in data
    
    guilds = data["available_guilds"]
    assert len(guilds) > 0
    
    for guild in guilds:
        assert "name" in guild
        assert "type" in guild


def test_get_guilds_nonexistent_player():
    """Test guilds with non-existent player."""
    response = client.get("/api/community/guilds/nonexistent-12345")
    
    assert response.status_code == 404


def test_join_guild(test_player):
    """Test joining a guild."""
    response = client.post(
        f"/api/community/guilds/join/{test_player.id}/CS Competitive Programming Guild"
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["status"] == "success"
    assert "guild_name" in data
    assert "member_count" in data
    assert "guild_level" in data


def test_join_guild_nonexistent_player():
    """Test joining guild with non-existent player."""
    response = client.post(
        f"/api/community/guilds/join/nonexistent-12345/Test Guild"
    )
    
    assert response.status_code == 404


def test_get_projects(test_player):
    """Test retrieving collaborative project opportunities."""
    response = client.get(f"/api/community/projects/{test_player.id}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "player_id" in data
    assert "available_projects" in data
    assert "total_opportunities" in data
    assert "project_benefits" in data
    
    projects = data["available_projects"]
    assert len(projects) > 0
    
    for project in projects:
        assert "name" in project
        assert "type" in project
        assert "required_roles" in project


def test_get_projects_nonexistent_player():
    """Test projects with non-existent player."""
    response = client.get("/api/community/projects/nonexistent-12345")
    
    assert response.status_code == 404


def test_apply_to_project(test_player):
    """Test applying to a collaborative project."""
    response = client.post(
        f"/api/community/projects/apply/{test_player.id}/AI-Powered Education Platform?role=Backend Developer"
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["status"] == "success"
    assert "project_name" in data
    assert "expected_response" in data
    assert "next_steps" in data


def test_apply_to_project_nonexistent_player():
    """Test project application with non-existent player."""
    response = client.post(
        f"/api/community/projects/apply/nonexistent-12345/Test Project"
    )
    
    assert response.status_code == 404


def test_get_collaboration_partners(test_player):
    """Test getting suggested collaboration partners."""
    response = client.get(
        f"/api/community/collaboration-partners/{test_player.id}/AI-Powered Education Platform"
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert "suggested_partners" in data
    assert "selection_tip" in data
    
    partners = data["suggested_partners"]
    assert len(partners) > 0
    
    for partner in partners:
        assert "name" in partner
        assert "strength" in partner
        assert "compatibility_score" in partner


def test_get_collaboration_partners_nonexistent_player():
    """Test collaboration partners with non-existent player."""
    response = client.get(
        f"/api/community/collaboration-partners/nonexistent-12345/Test Project"
    )
    
    assert response.status_code == 404


def test_get_community_achievements():
    """Test retrieving community achievement badges."""
    response = client.get("/api/community/achievements")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "total_achievements" in data
    assert "achievements" in data
    assert "rarity_distribution" in data
    
    achievements = data["achievements"]
    assert len(achievements) > 0
    
    for achievement in achievements:
        assert "name" in achievement
        assert "icon" in achievement
        assert "rarity" in achievement


def test_get_social_activities():
    """Test retrieving social bonding activities."""
    response = client.get("/api/community/social-activities")
    
    assert response.status_code == 200
    data = response.json()
    
    assert "total_activities" in data
    assert "activities" in data
    assert "impact" in data
    
    activities = data["activities"]
    assert len(activities) > 0
    
    for activity in activities:
        assert "name" in activity
        assert "format" in activity
        assert "bonding_score" in activity


def test_attend_social_activity(test_player):
    """Test attending a social bonding activity."""
    response = client.post(
        f"/api/community/attend-activity/{test_player.id}/Weekly Coffee Chat"
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["status"] == "success"
    assert "activity_name" in data
    assert "attendance_confirmed" in data
    assert "benefits" in data


def test_attend_social_activity_nonexistent_player():
    """Test attending activity with non-existent player."""
    response = client.post(
        f"/api/community/attend-activity/nonexistent-12345/Test Activity"
    )
    
    assert response.status_code == 404


def test_community_impact_calculation(test_player):
    """Test community impact calculation."""
    response = client.get(
        f"/api/community/community-impact/{test_player.id}?groups=2&guild_level=2&projects=1"
    )
    
    assert response.status_code == 200
    data = response.json()
    
    assert "player_id" in data
    assert "scenario" in data
    assert "impact_on_stats" in data
    assert "career_impact" in data
    
    impact = data["impact_on_stats"]
    assert "gpa_boost" in impact
    assert "confidence_boost" in impact
    assert "network_expansion" in impact


def test_community_impact_nonexistent_player():
    """Test impact calculation with non-existent player."""
    response = client.get("/api/community/community-impact/nonexistent-12345")
    
    assert response.status_code == 404


def test_community_impact_scaling(test_player):
    """Test that impact scales with participation level."""
    # Low participation
    response_low = client.get(
        f"/api/community/community-impact/{test_player.id}?groups=1&guild_level=1&projects=0"
    )
    
    # High participation
    response_high = client.get(
        f"/api/community/community-impact/{test_player.id}?groups=3&guild_level=3&projects=2"
    )
    
    assert response_low.status_code == 200
    assert response_high.status_code == 200
    
    data_low = response_low.json()
    data_high = response_high.json()
    
    # Extract numeric values for comparison
    def extract_number(s):
        return float(''.join(c for c in s if c.isdigit() or c == '.'))
    
    # High participation should have higher impact
    low_confidence = extract_number(data_low["impact_on_stats"]["confidence_boost"])
    high_confidence = extract_number(data_high["impact_on_stats"]["confidence_boost"])
    assert high_confidence > low_confidence


def test_study_group_diversity():
    """Test that study groups cover multiple disciplines."""
    # Create players with different majors
    majors = ["computer_science", "finance", "biology", "psychology"]
    
    for major in majors:
        player = Player(
            id=str(uuid4()),
            name=f"Student {major}",
            age=20,
            hs_gpa=3.5,
            parent_income=60000,
            major_id=major,
            college_id="nyu",
            semester=1,
            year_in_school=1,
            stats=Stats(),
            finance=Finance(balance=5000),
            housing=HOUSING_OPTIONS["dorm"],
            job=None,
            plan=None,
            history=[],
        )
        STORE.put_player(player)
        
        response = client.get(f"/api/community/study-groups/{player.id}")
        assert response.status_code == 200
        
        groups = response.json()["recommended_study_groups"]
        assert len(groups) > 0


def test_guild_membership_benefits(test_player):
    """Test that guild membership provides clear benefits."""
    response = client.post(
        f"/api/community/guilds/join/{test_player.id}/CS Competitive Programming Guild"
    )
    
    assert response.status_code == 200
    data = response.json()
    
    # Check for welcome bonuses
    assert "welcome_bonus" in data
    assert "credits" in data["welcome_bonus"]
    assert "skill_boost" in data["welcome_bonus"]


def test_project_roles_diversity():
    """Test that projects need diverse roles."""
    response = client.get(f"/api/community/projects/nonexistent-test")
    
    # Will 404 but we can check the projects directly
    from catalogs.community_collaboration import PROJECT_OPPORTUNITIES
    
    all_roles = set()
    for project in PROJECT_OPPORTUNITIES:
        all_roles.update(project["required_roles"])
    
    # Should have diverse roles
    assert len(all_roles) > 3
    assert "Full-stack Dev" in all_roles or "Backend Developer" in all_roles


def test_collaboration_partner_compatibility():
    """Test that suggested partners have compatibility scores."""
    test_player_id = "test-123"
    test_player_obj = Player(
        id=test_player_id,
        name="Test",
        age=20,
        hs_gpa=3.5,
        parent_income=60000,
        major_id="computer_science",
        college_id="nyu",
        semester=1,
        year_in_school=1,
        stats=Stats(),
        finance=Finance(balance=5000),
        housing=HOUSING_OPTIONS["dorm"],
        job=None,
        plan=None,
        history=[],
    )
    STORE.put_player(test_player_obj)
    
    response = client.get(
        f"/api/community/collaboration-partners/{test_player_id}/AI-Powered Education Platform"
    )
    
    assert response.status_code == 200
    data = response.json()
    
    for partner in data["suggested_partners"]:
        assert 0 <= partner["compatibility_score"] <= 100
