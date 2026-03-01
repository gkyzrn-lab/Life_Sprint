"""
Tests for Job Market Intelligence System
"""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_industry_overview():
    """Test industry overview endpoint."""
    resp = client.get("/api/market-intelligence/industry-overview")
    assert resp.status_code == 200
    
    data = resp.json()
    assert "industries" in data
    assert "summary" in data
    assert "Technology" in data["industries"]
    assert "Finance" in data["industries"]
    
    # Verify industry structure
    tech = data["industries"]["Technology"]
    assert "growth_rate" in tech
    assert "hiring_intensity" in tech
    assert "top_roles" in tech
    assert len(tech["top_roles"]) >= 2


def test_skills_analysis():
    """Test skills demand analysis."""
    resp = client.get("/api/market-intelligence/skills-analysis")
    assert resp.status_code == 200
    
    data = resp.json()
    assert "top_10_skills" in data
    assert "skills_matrix" in data
    
    # Verify top skills
    assert len(data["top_10_skills"]) == 10
    for skill in data["top_10_skills"]:
        assert "skill" in skill
        assert "demand_score" in skill
        assert "salary_premium" in skill
        assert "trend" in skill


def test_emerging_opportunities():
    """Test emerging roles and opportunities."""
    resp = client.get("/api/market-intelligence/emerging-opportunities")
    assert resp.status_code == 200
    
    data = resp.json()
    assert "emerging_roles" in data
    assert len(data["emerging_roles"]) >= 4
    
    # Verify role structure
    for role in data["emerging_roles"]:
        assert "role" in role
        assert "growth" in role
        assert "avg_salary" in role
        assert "required_skills" in role


def test_salary_benchmarks():
    """Test salary benchmark data."""
    resp = client.get("/api/market-intelligence/salary-benchmarks")
    assert resp.status_code == 200
    
    data = resp.json()
    assert "progression" in data
    
    # Verify progression structure
    assert "Software Engineering" in data["progression"]
    eng = data["progression"]["Software Engineering"]
    assert "entry" in eng
    assert "2_years" in eng
    assert "5_years" in eng
    assert "senior" in eng


def test_market_trends():
    """Test job market trends analysis."""
    resp = client.get("/api/market-intelligence/market-trends")
    assert resp.status_code == 200
    
    data = resp.json()
    assert "trends" in data
    assert len(data["trends"]) >= 5
    assert "key_insights" in data
    assert "advice_for_graduates" in data


def test_field_outlook_technology():
    """Test field-specific outlook for Technology."""
    resp = client.get("/api/market-intelligence/field-outlook/Technology")
    assert resp.status_code == 200
    
    data = resp.json()
    assert data["field"] == "Technology"
    assert "overview" in data
    assert data["overview"]["demand_score"] >= 90


def test_field_outlook_finance():
    """Test field-specific outlook for Finance."""
    resp = client.get("/api/market-intelligence/field-outlook/Finance")
    assert resp.status_code == 200
    
    data = resp.json()
    assert data["field"] == "Finance"
    assert "overview" in data


def test_field_outlook_invalid():
    """Test that invalid field returns 404."""
    resp = client.get("/api/market-intelligence/field-outlook/InvalidField")
    assert resp.status_code == 404


def test_field_comparison():
    """Test comparison between two fields."""
    resp = client.get("/api/market-intelligence/comparison/Technology/Finance")
    assert resp.status_code == 200
    
    data = resp.json()
    assert "field1" in data
    assert "field2" in data
    assert "comparison" in data


def test_skill_market_guide_python():
    """Test market guide for Python skill."""
    resp = client.get("/api/market-intelligence/skills-guide/Python")
    assert resp.status_code == 200
    
    data = resp.json()
    assert data["skill"] == "Python"
    assert "demand_score" in data
    assert "industries" in data
    assert "salary_premium" in data


def test_skill_market_guide_sql():
    """Test market guide for SQL skill."""
    resp = client.get("/api/market-intelligence/skills-guide/SQL")
    assert resp.status_code == 200
    
    data = resp.json()
    assert data["skill"] == "SQL"


def test_skill_market_guide_invalid():
    """Test that invalid skill returns 404."""
    resp = client.get("/api/market-intelligence/skills-guide/InvalidSkill")
    assert resp.status_code == 404


def test_entry_level_guide():
    """Test entry-level professional guide."""
    resp = client.get("/api/market-intelligence/entry-level-guide")
    assert resp.status_code == 200
    
    data = resp.json()
    assert "best_majors" in data
    assert "critical_first_5_years" in data
    assert "typical_entry_salaries" in data
    assert "salary_growth_expectations" in data
    assert "key_insights" in data
    
    # Verify structure
    assert len(data["best_majors"]) >= 4
    assert len(data["critical_first_5_years"]) >= 3
    assert len(data["typical_entry_salaries"]) >= 3
