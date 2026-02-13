"""Tests for student loan payoff strategies."""

import pytest
from catalogs.loan_strategies import (
    LoanForComparison,
    calculate_minimum_payment,
    simulate_payoff,
    calculate_idr_payment,
    compare_all_strategies,
    get_strategy_recommendation,
    REPAYMENT_STRATEGIES
)


def test_repayment_strategies_exist():
    """Test that all major repayment strategies are defined."""
    assert "avalanche" in REPAYMENT_STRATEGIES
    assert "snowball" in REPAYMENT_STRATEGIES
    assert "standard" in REPAYMENT_STRATEGIES
    assert "idr" in REPAYMENT_STRATEGIES
    assert "pslf" in REPAYMENT_STRATEGIES


def test_strategy_pros_and_cons():
    """Test that each strategy has pros and cons."""
    for strategy in REPAYMENT_STRATEGIES.values():
        assert len(strategy.pros) >= 2
        assert len(strategy.cons) >= 2
        assert len(strategy.best_for) > 0


def test_minimum_payment_calculation():
    """Test minimum payment calculation for 10-year standard."""
    # $10,000 loan at 5% over 10 years
    payment = calculate_minimum_payment(10000, 5.0, 120)
    
    # Should be around $106/month
    assert 100 < payment < 115
    
    # Zero interest
    payment_zero = calculate_minimum_payment(10000, 0.0, 120)
    assert payment_zero == pytest.approx(10000 / 120, rel=0.01)


def test_avalanche_saves_more_than_snowball():
    """Test that avalanche method saves more interest than snowball."""
    loans = [
        LoanForComparison(
            loan_id="loan1",
            name="High Interest Small",
            principal=3000,
            annual_interest_rate=7.5,
            loan_type="federal_unsubsidized"
        ),
        LoanForComparison(
            loan_id="loan2",
            name="Low Interest Large",
            principal=20000,
            annual_interest_rate=3.5,
            loan_type="federal_subsidized"
        )
    ]
    
    avalanche = simulate_payoff(loans, "avalanche", 50)  # Add extra payment
    snowball = simulate_payoff(loans, "snowball", 50)
    
    # Avalanche should pay less total interest (or very close)
    # With significantly different rates and balances, avalanche should win
    assert avalanche.total_interest <= snowball.total_interest + 100  # Allow small margin
    assert avalanche.months_to_payoff <= snowball.months_to_payoff


def test_extra_payments_save_money():
    """Test that extra payments reduce interest and time."""
    loans = [
        LoanForComparison(
            loan_id="loan1",
            name="Test Loan",
            principal=20000,
            annual_interest_rate=6.0,
            loan_type="federal_unsubsidized"
        )
    ]
    
    no_extra = simulate_payoff(loans, "avalanche", 0)
    with_extra = simulate_payoff(loans, "avalanche", 100)
    
    # Extra payments should:
    # 1) Reduce total interest paid
    assert with_extra.total_interest < no_extra.total_interest
    # 2) Reduce time to payoff
    assert with_extra.months_to_payoff < no_extra.months_to_payoff
    # 3) Reduce total amount paid
    assert with_extra.total_paid < no_extra.total_paid


def test_idr_payment_calculation():
    """Test income-driven repayment payment calculation."""
    # Low income
    payment_low = calculate_idr_payment(annual_income=30000, family_size=1)
    assert payment_low < 200  # Should be low
    
    # Higher income
    payment_high = calculate_idr_payment(annual_income=80000, family_size=1)
    assert payment_high > payment_low
    
    # Larger family reduces payment
    payment_large_family = calculate_idr_payment(annual_income=80000, family_size=4)
    assert payment_large_family < payment_high


def test_compare_all_strategies():
    """Test comprehensive strategy comparison."""
    loans = [
        LoanForComparison(
            loan_id="loan1",
            name="Loan A",
            principal=10000,
            annual_interest_rate=6.8,
            loan_type="federal_unsubsidized"
        ),
        LoanForComparison(
            loan_id="loan2",
            name="Loan B",
            principal=5000,
            annual_interest_rate=4.5,
            loan_type="federal_subsidized"
        ),
        LoanForComparison(
            loan_id="loan3",
            name="Loan C",
            principal=15000,
            annual_interest_rate=7.9,
            loan_type="federal_unsubsidized"
        )
    ]
    
    comparison = compare_all_strategies(loans, annual_income=50000)
    
    # Should have projections for all strategies
    assert comparison.avalanche_projection is not None
    assert comparison.snowball_projection is not None
    assert comparison.standard_projection is not None
    assert comparison.idr_projection is not None  # All federal loans
    
    # Total principal should match
    assert comparison.total_principal == 30000
    
    # Avalanche should be recommended for savings
    assert comparison.best_for_savings == "avalanche"
    
    # Snowball for motivation
    assert comparison.best_for_motivation == "snowball"


def test_extra_payment_impact():
    """Test that extra payment scenarios are calculated."""
    loans = [
        LoanForComparison(
            loan_id="loan1",
            name="Test",
            principal=20000,
            annual_interest_rate=6.0,
            loan_type="federal_unsubsidized"
        )
    ]
    
    comparison = compare_all_strategies(loans)
    
    # Should have 3 extra payment scenarios
    assert comparison.extra_50_impact.extra_payment_monthly == 50
    assert comparison.extra_100_impact.extra_payment_monthly == 100
    assert comparison.extra_200_impact.extra_payment_monthly == 200
    
    # Each should save progressively more
    assert comparison.extra_200_impact.interest_saved > comparison.extra_100_impact.interest_saved
    assert comparison.extra_100_impact.interest_saved > comparison.extra_50_impact.interest_saved
    
    # ROI should be positive
    assert comparison.extra_50_impact.roi_ratio > 0
    assert comparison.extra_100_impact.roi_ratio > 0


def test_strategy_recommendation_public_service():
    """Test recommendation for public service career path."""
    loans = [
        LoanForComparison(
            loan_id="loan1",
            name="Large Federal Loan",
            principal=80000,
            annual_interest_rate=6.8,
            loan_type="federal_unsubsidized"
        )
    ]
    
    recommendation = get_strategy_recommendation(
        loans=loans,
        annual_income=45000,
        personality="analytical",
        career_plan="public_service"
    )
    
    # Should recommend PSLF for high debt + public service
    assert recommendation["recommended_strategy"] == "pslf"
    assert "public service" in recommendation["reason"].lower()


def test_strategy_recommendation_high_debt():
    """Test recommendation for very high debt."""
    loans = [
        LoanForComparison(
            loan_id="loan1",
            name="Huge Loan",
            principal=150000,
            annual_interest_rate=7.0,
            loan_type="federal_unsubsidized"
        )
    ]
    
    recommendation = get_strategy_recommendation(
        loans=loans,
        annual_income=50000,
        personality="struggling",
        career_plan="private_sector"
    )
    
    # Debt-to-income ratio > 2.0, should recommend IDR
    assert recommendation["recommended_strategy"] == "idr"


def test_strategy_recommendation_analytical_personality():
    """Test recommendation for analytical personality."""
    loans = [
        LoanForComparison(
            loan_id="loan1",
            name="Moderate Loan",
            principal=30000,
            annual_interest_rate=6.0,
            loan_type="federal_unsubsidized"
        )
    ]
    
    recommendation = get_strategy_recommendation(
        loans=loans,
        annual_income=60000,
        personality="analytical",
        career_plan="private_sector"
    )
    
    # Should recommend avalanche for analytical types
    assert recommendation["recommended_strategy"] == "avalanche"


def test_strategy_recommendation_motivational_personality():
    """Test recommendation for motivational personality."""
    loans = [
        LoanForComparison(
            loan_id="loan1",
            name="Moderate Loan",
            principal=30000,
            annual_interest_rate=6.0,
            loan_type="federal_unsubsidized"
        )
    ]
    
    recommendation = get_strategy_recommendation(
        loans=loans,
        annual_income=60000,
        personality="motivational",
        career_plan="unsure"
    )
    
    # Should recommend snowball for motivational types
    assert recommendation["recommended_strategy"] == "snowball"


def test_payoff_projection_structure():
    """Test that payoff projections have correct structure."""
    loans = [
        LoanForComparison(
            loan_id="loan1",
            name="Test",
            principal=10000,
            annual_interest_rate=5.0,
            loan_type="federal_unsubsidized"
        )
    ]
    
    projection = simulate_payoff(loans, "avalanche", 0)
    
    assert projection.strategy == "avalanche"
    assert projection.monthly_payment > 0
    assert projection.months_to_payoff > 0
    assert projection.total_paid > 10000  # Principal + interest
    assert projection.total_interest > 0
    assert len(projection.year_breakdown) > 0


def test_yearly_breakdown():
    """Test that year breakdown is generated."""
    loans = [
        LoanForComparison(
            loan_id="loan1",
            name="Test",
            principal=20000,
            annual_interest_rate=6.0,
            loan_type="federal_unsubsidized"
        )
    ]
    
    projection = simulate_payoff(loans, "standard", 0)
    
    # Should have multiple years of data
    assert len(projection.year_breakdown) >= 5
    
    # Each year should have required fields
    year_data = projection.year_breakdown[0]
    assert "year" in year_data
    assert "total_paid" in year_data
    assert "principal_paid" in year_data
    assert "interest_paid" in year_data
    assert "remaining_balance" in year_data


def test_educational_value_of_strategies():
    """Test that strategies teach important lessons."""
    for strategy_name, strategy in REPAYMENT_STRATEGIES.items():
        # Each strategy should teach something
        assert len(strategy.description) > 50
        assert len(strategy.best_for) > 20
        
        # Should have balanced pros and cons
        assert 1 <= len(strategy.pros) <= 6
        assert 1 <= len(strategy.cons) <= 6
