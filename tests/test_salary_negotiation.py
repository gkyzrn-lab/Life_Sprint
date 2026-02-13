"""Tests for salary negotiation system."""

import pytest
from catalogs.salary_negotiation import (
    calculate_lifetime_earnings_impact,
    evaluate_negotiation,
    get_negotiation_tip,
    get_market_data,
    NegotiationScenario,
    NegotiationStrategy,
    NEGOTIATION_TIPS,
    MARKET_DATA
)


def test_market_data_exists():
    """Test that market data is available for common positions."""
    assert len(MARKET_DATA) >= 5
    assert "software_engineer_entry" in MARKET_DATA
    assert "software_engineer_mid" in MARKET_DATA


def test_market_data_structure():
    """Test market data has correct structure."""
    swe_data = MARKET_DATA["software_engineer_entry"]
    assert swe_data.percentile_50 > swe_data.percentile_25
    assert swe_data.percentile_75 > swe_data.percentile_50
    assert swe_data.percentile_90 > swe_data.percentile_75


def test_lifetime_earnings_calculation():
    """Test lifetime earnings impact calculation."""
    result = calculate_lifetime_earnings_impact(
        base_salary=70000,
        negotiated_salary=75000,
        years=40,
        annual_raise_percent=3.0
    )
    
    assert result["immediate_gain"] == 5000
    assert result["lifetime_gain"] > 200000  # Should be ~$336k
    assert result["gain_multiplier"] > 50  # $5k becomes $300k+


def test_negotiation_tips_exist():
    """Test that negotiation tips are comprehensive."""
    assert len(NEGOTIATION_TIPS) >= 10
    
    # Critical tips must exist
    assert "always_negotiate" in NEGOTIATION_TIPS
    assert "research_first" in NEGOTIATION_TIPS
    assert "competing_offers" in NEGOTIATION_TIPS
    
    # Check impact levels
    critical_tips = [t for t in NEGOTIATION_TIPS.values() if t.impact_level == "critical"]
    assert len(critical_tips) >= 3


def test_get_negotiation_tip():
    """Test retrieving specific tips."""
    tip = get_negotiation_tip("always_negotiate")
    assert tip is not None
    assert tip.impact_level == "critical"
    assert "always" in tip.title.lower()


def test_accept_without_negotiating():
    """Test accepting offer immediately without negotiation."""
    scenario = NegotiationScenario(
        scenario_id="test_1",
        job_title="Software Engineer",
        company_name="TechCo",
        initial_offer=70000,
        market_median=75000,
        market_75th=85000,
        company_size="medium",
        company_urgency="medium",
        your_leverage="medium"
    )
    
    strategy = NegotiationStrategy(
        strategy_type="accept"
    )
    
    outcome = evaluate_negotiation(scenario, strategy)
    
    assert outcome.success == True
    assert outcome.final_salary == 70000
    assert outcome.immediate_gain == 0
    assert outcome.negotiation_score == 0
    assert len(outcome.lessons_learned) > 0
    assert "without negotiating" in outcome.lessons_learned[0].lower()


def test_successful_negotiation():
    """Test successful salary negotiation."""
    scenario = NegotiationScenario(
        scenario_id="test_2",
        job_title="Software Engineer",
        company_name="TechCo",
        initial_offer=70000,
        market_median=75000,
        market_75th=85000,
        company_size="medium",
        company_urgency="high",  # They need you
        your_leverage="high"  # You have competing offers
    )
    
    strategy = NegotiationStrategy(
        strategy_type="negotiate_salary",
        requested_salary=75000,
        justification="market rate",
        tone="collaborative"
    )
    
    outcome = evaluate_negotiation(
        scenario,
        strategy,
        player_communication_skills=80,
        player_confidence=75
    )
    
    assert outcome.success == True
    assert outcome.final_salary > 70000
    assert outcome.immediate_gain > 0
    assert outcome.lifetime_earnings_gain > 100000


def test_aggressive_tone_hurts_negotiation():
    """Test that aggressive tone reduces success."""
    scenario = NegotiationScenario(
        scenario_id="test_3",
        job_title="Software Engineer",
        company_name="TechCo",
        initial_offer=70000,
        market_median=75000,
        market_75th=85000,
        company_size="medium",
        company_urgency="medium",
        your_leverage="medium"
    )
    
    strategy_aggressive = NegotiationStrategy(
        strategy_type="negotiate_salary",
        requested_salary=75000,
        tone="aggressive"
    )
    
    strategy_collaborative = NegotiationStrategy(
        strategy_type="negotiate_salary",
        requested_salary=75000,
        tone="collaborative"
    )
    
    outcome_aggressive = evaluate_negotiation(scenario, strategy_aggressive, 70, 70)
    outcome_collaborative = evaluate_negotiation(scenario, strategy_collaborative, 70, 70)
    
    # Collaborative should generally do better
    assert outcome_collaborative.negotiation_score >= outcome_aggressive.negotiation_score


def test_unrealistic_request():
    """Test negotiating for way above market."""
    scenario = NegotiationScenario(
        scenario_id="test_4",
        job_title="Software Engineer",
        company_name="TechCo",
        initial_offer=70000,
        market_median=75000,
        market_75th=85000,
        company_size="medium",
        company_urgency="low",
        your_leverage="low"
    )
    
    strategy = NegotiationStrategy(
        strategy_type="negotiate_salary",
        requested_salary=120000,  # Way too high
        tone="collaborative"
    )
    
    outcome = evaluate_negotiation(scenario, strategy, 60, 60)
    
    # Should either fail or get much less than asked
    if outcome.success:
        assert outcome.final_salary < 120000
    # Might fail entirely


def test_low_skills_hurt_negotiation():
    """Test that low communication skills hurt negotiation."""
    scenario = NegotiationScenario(
        scenario_id="test_5",
        job_title="Software Engineer",
        company_name="TechCo",
        initial_offer=70000,
        market_median=75000,
        market_75th=85000,
        company_size="medium",
        company_urgency="medium",
        your_leverage="medium"
    )
    
    strategy = NegotiationStrategy(
        strategy_type="negotiate_salary",
        requested_salary=75000,
        tone="collaborative"
    )
    
    outcome_low_skills = evaluate_negotiation(scenario, strategy, 30, 30)
    outcome_high_skills = evaluate_negotiation(scenario, strategy, 90, 90)
    
    # High skills should do better
    assert outcome_high_skills.final_salary >= outcome_low_skills.final_salary


def test_get_market_data():
    """Test market data retrieval."""
    data = get_market_data("software_engineer_entry")
    assert data is not None
    assert data.percentile_50 > 0
    
    invalid_data = get_market_data("nonexistent")
    assert invalid_data is None


def test_negotiation_tips_educational_value():
    """Test that tips contain educational content."""
    for tip in NEGOTIATION_TIPS.values():
        assert len(tip.title) > 0
        assert len(tip.description) > 50  # Substantial description
        assert len(tip.example) > 0
        assert tip.impact_level in ["low", "medium", "high", "critical"]


def test_lifetime_earnings_substantial():
    """Test that small negotiations have big lifetime impact."""
    # Even $5k negotiation should be significant
    result = calculate_lifetime_earnings_impact(65000, 70000, 40, 3.0)
    
    # $5k negotiation should compound to $300k+
    assert result["immediate_gain"] == 5000
    assert result["lifetime_gain"] > 250000
    assert result["gain_multiplier"] > 50
