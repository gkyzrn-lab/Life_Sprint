"""Tests for investment and compound interest system."""

import pytest
from catalogs.investments import (
    calculate_compound_interest,
    calculate_yearly_breakdown,
    compare_start_early_vs_late,
    calculate_employer_match_value,
    retirement_projection,
    calculate_monthly_needed_for_goal,
    get_investment_recommendation,
    INVESTMENT_VEHICLES,
    EmployerMatch
)


def test_investment_vehicles_exist():
    """Test that major investment vehicles are defined."""
    assert "savings_account" in INVESTMENT_VEHICLES
    assert "roth_ira" in INVESTMENT_VEHICLES
    assert "traditional_401k" in INVESTMENT_VEHICLES
    assert "index_funds" in INVESTMENT_VEHICLES


def test_investment_vehicle_structure():
    """Test that each vehicle has required educational content."""
    for vehicle in INVESTMENT_VEHICLES.values():
        assert vehicle.expected_annual_return > 0
        assert vehicle.risk_level in ["very_low", "low", "medium", "high"]
        assert vehicle.tax_treatment in ["taxable", "tax_deferred", "tax_free"]
        assert vehicle.liquidity in ["instant", "easy", "restricted", "locked_until_retirement"]
        assert len(vehicle.best_for) > 20
        assert len(vehicle.watch_out) > 20


def test_compound_interest_calculation():
    """Test basic compound interest calculation."""
    result = calculate_compound_interest(
        principal=1000,
        monthly_contribution=100,
        annual_return_rate=9.0,
        years=10
    )
    
    # Total contributions
    assert result["total_contributed"] == 1000 + (100 * 12 * 10)  # $13,000
    
    # Should have earnings from growth
    assert result["total_earnings"] > 0
    
    # Final balance should be more than contributions
    assert result["final_balance"] > result["total_contributed"]
    
    # Return multiple should be > 1
    assert result["return_multiple"] > 1.0


def test_compound_interest_long_term():
    """Test that long-term investing shows significant growth."""
    # $200/month for 40 years at 9% should grow substantially
    result = calculate_compound_interest(
        principal=0,
        monthly_contribution=200,
        annual_return_rate=9.0,
        years=40
    )
    
    # Total contributions: $96,000
    assert result["total_contributed"] == 200 * 12 * 40
    
    # Should grow to over $500k
    assert result["final_balance"] > 500000
    
    # Earnings should be much more than contributions
    assert result["total_earnings"] > result["total_contributed"] * 4


def test_yearly_breakdown():
    """Test year-by-year breakdown generation."""
    breakdown = calculate_yearly_breakdown(
        principal=0,
        monthly_contribution=500,
        annual_return_rate=9.0,
        years=10
    )
    
    # Should have 10 years
    assert len(breakdown) == 10
    
    # Each year should show growth
    for i in range(1, len(breakdown)):
        assert breakdown[i]["balance"] > breakdown[i-1]["balance"]
        assert breakdown[i]["total_contributed"] > breakdown[i-1]["total_contributed"]
        assert breakdown[i]["total_earnings"] >= breakdown[i-1]["total_earnings"]


def test_start_early_vs_late_comparison():
    """Test the dramatic impact of starting early."""
    comparison = compare_start_early_vs_late()
    
    # Person A starts at 22, Person B at 32
    assert comparison.person_a_age_start == 22
    assert comparison.person_b_age_start == 32
    
    # Person A contributes less total
    assert comparison.person_a_total_contributed < comparison.person_b_total_contributed
    
    # But Person A should end up with MORE money (power of compound interest!)
    assert comparison.person_a_balance_at_65 > comparison.person_b_balance_at_65
    
    # The advantage should be substantial (>$100k)
    assert comparison.person_a_advantage > 100000
    
    # Lesson should be present
    assert len(comparison.lesson) > 100


def test_employer_match_value():
    """Test employer 401k match calculation."""
    match = EmployerMatch(
        match_percentage=50.0,  # 50% match
        match_limit_percent_of_salary=6.0,  # up to 6% of salary
        vesting_schedule="immediate",
        vesting_description="Immediate vesting"
    )
    
    # If employee contributes 6% of $60k salary ($3,600)
    result = calculate_employer_match_value(
        annual_salary=60000,
        employee_contribution_percent=6.0,
        match=match
    )
    
    # Employer should match 50% of $3,600 = $1,800
    assert result["employer_match"] == pytest.approx(1800, rel=0.01)
    
    # Total contribution = $3,600 + $1,800 = $5,400
    assert result["total_contribution"] == pytest.approx(5400, rel=0.01)
    
    # Free money percent = 50%
    assert result["free_money_percent"] == pytest.approx(50, rel=0.01)
    
    # No lost match since contributing full 6%
    assert result["lost_match_this_year"] == 0


def test_employer_match_under_contributing():
    """Test lost match when under-contributing."""
    match = EmployerMatch(
        match_percentage=100.0,  # 100% match (dollar for dollar)
        match_limit_percent_of_salary=5.0,
        vesting_schedule="immediate",
        vesting_description="Immediate vesting"
    )
    
    # Employee only contributes 3% when they should contribute 5%
    result = calculate_employer_match_value(
        annual_salary=50000,
        employee_contribution_percent=3.0,
        match=match
    )
    
    # Lost match = 2% of salary = $1,000
    assert result["lost_match_this_year"] == pytest.approx(1000, rel=0.01)
    
    # Over 30 years, losing $30k+ (not including growth!)
    assert result["lost_match_over_30_years"] >= 30000


def test_retirement_projection_on_track():
    """Test retirement projection when on track."""
    projection = retirement_projection(
        current_age=25,
        retirement_age=65,
        current_savings=10000,
        monthly_contribution=500,
        annual_return=9.0
    )
    
    # Should have projection
    assert projection["years_until_retirement"] == 40
    assert projection["projected_balance_at_retirement"] > 1000000
    
    # Should be on track with $500/month for 40 years
    assert projection["on_track_for_comfortable_retirement"] == True
    assert projection["shortfall"] == 0
    assert projection["additional_monthly_needed"] == 0


def test_retirement_projection_not_on_track():
    """Test retirement projection when behind."""
    projection = retirement_projection(
        current_age=40,
        retirement_age=65,
        current_savings=20000,
        monthly_contribution=100,  # Too low
        annual_return=9.0
    )
    
    # Should show not on track
    assert projection["on_track_for_comfortable_retirement"] == False
    assert projection["shortfall"] > 0
    assert projection["additional_monthly_needed"] > 0


def test_monthly_needed_for_goal():
    """Test calculating monthly contribution needed for a goal."""
    # Need $500k in 30 years, starting from $0, at 9% return
    monthly_needed = calculate_monthly_needed_for_goal(
        current_savings=0,
        years=30,
        goal=500000,
        annual_return=9.0
    )
    
    # Should be achievable with reasonable monthly contribution
    assert 200 < monthly_needed < 400
    
    # If already have savings, should need less per month
    monthly_needed_with_savings = calculate_monthly_needed_for_goal(
        current_savings=50000,
        years=30,
        goal=500000,
        annual_return=9.0
    )
    
    assert monthly_needed_with_savings < monthly_needed


def test_investment_recommendation_emergency_fund_first():
    """Test that emergency fund is priority #1."""
    recommendation = get_investment_recommendation(
        age=25,
        emergency_fund_months=0,  # No emergency fund
        annual_income=50000,
        debt_amount=5000,
        has_employer_match=True
    )
    
    # First recommendation should be emergency fund
    first_priority = recommendation["recommendations"][0]
    assert first_priority["priority"] == 1
    assert "emergency" in first_priority["action"].lower()


def test_investment_recommendation_employer_match():
    """Test that employer match is prioritized."""
    recommendation = get_investment_recommendation(
        age=25,
        emergency_fund_months=4,  # Has emergency fund
        annual_income=50000,
        debt_amount=0,
        has_employer_match=True
    )
    
    # Should recommend 401k to get match
    has_401k_recommendation = any(
        "match" in rec["action"].lower() or "401k" in rec["action"].lower()
        for rec in recommendation["recommendations"]
    )
    assert has_401k_recommendation


def test_investment_recommendation_pay_debt():
    """Test that high-interest debt is prioritized."""
    recommendation = get_investment_recommendation(
        age=25,
        emergency_fund_months=4,
        annual_income=50000,
        debt_amount=10000,  # Has debt
        has_employer_match=False
    )
    
    # Should recommend paying off debt
    has_debt_recommendation = any(
        "debt" in rec["action"].lower()
        for rec in recommendation["recommendations"]
    )
    assert has_debt_recommendation


def test_investment_recommendation_roth_ira_for_young():
    """Test that Roth IRA is recommended for young people."""
    recommendation = get_investment_recommendation(
        age=25,  # Young
        emergency_fund_months=4,
        annual_income=60000,
        debt_amount=0,
        has_employer_match=True
    )
    
    # Should recommend Roth IRA
    has_roth_recommendation = any(
        "roth" in rec["action"].lower()
        for rec in recommendation["recommendations"]
    )
    assert has_roth_recommendation


def test_investment_vehicles_tax_treatments():
    """Test that tax treatments are correct."""
    # Roth IRA should be tax-free
    assert INVESTMENT_VEHICLES["roth_ira"].tax_treatment == "tax_free"
    
    # Traditional 401k should be tax-deferred
    assert INVESTMENT_VEHICLES["traditional_401k"].tax_treatment == "tax_deferred"
    
    # Savings should be taxable
    assert INVESTMENT_VEHICLES["savings_account"].tax_treatment == "taxable"


def test_investment_vehicles_risk_vs_return():
    """Test that higher risk = higher expected returns."""
    savings = INVESTMENT_VEHICLES["savings_account"]
    index_funds = INVESTMENT_VEHICLES["index_funds"]
    
    # Savings is very low risk, low return
    assert savings.risk_level == "very_low"
    assert savings.expected_annual_return < 5.0
    
    # Index funds are medium risk, higher return
    assert index_funds.risk_level == "medium"
    assert index_funds.expected_annual_return > savings.expected_annual_return


def test_investment_vehicles_contribution_limits():
    """Test that contribution limits are set correctly."""
    # Roth IRA has $7k limit (2026)
    assert INVESTMENT_VEHICLES["roth_ira"].annual_contribution_limit == 7000
    
    # 401k has $23k limit (2026)
    assert INVESTMENT_VEHICLES["traditional_401k"].annual_contribution_limit == 23000
    
    # Taxable brokerage has no limit
    assert INVESTMENT_VEHICLES["index_funds"].annual_contribution_limit is None


def test_compound_interest_zero_contributions():
    """Test growth with no new contributions (just initial principal)."""
    result = calculate_compound_interest(
        principal=10000,
        monthly_contribution=0,
        annual_return_rate=7.0,
        years=30
    )
    
    # Should roughly double every 10 years at 7%
    # $10k -> ~$76k in 30 years
    assert result["final_balance"] > 70000
    assert result["total_contributed"] == 10000
    assert result["total_earnings"] > 60000


def test_time_value_of_money():
    """Test that starting early beats contributing more later."""
    # Person A: $100/month for 40 years starting now
    early_start = calculate_compound_interest(0, 100, 9.0, 40)
    
    # Person B: $200/month for 20 years starting in 20 years
    # First 20 years: $0 contribution
    # Last 20 years: $200/month
    late_start = calculate_compound_interest(0, 200, 9.0, 20)
    
    # Person A should have MORE despite contributing half as much per month
    assert early_start["total_contributed"] == 100 * 12 * 40  # $48k
    assert late_start["total_contributed"] == 200 * 12 * 20  # $48k
    
    # But Person A should have significantly more money
    assert early_start["final_balance"] > late_start["final_balance"] * 2
