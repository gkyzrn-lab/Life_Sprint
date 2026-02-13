"""Tests for credit card simulator."""

import pytest
from catalogs.credit_card_simulator import (
    simulate_credit_card_payoff, compare_payoff_strategies,
    get_payoff_insights, calculate_minimum_payment,
    CREDIT_CARD_TRAPS, CREDIT_CARD_MYTHS
)


class TestMinimumPaymentCalculation:
    """Test minimum payment calculation."""
    
    def test_minimum_payment_small_balance(self):
        """Test minimum payment on small balance."""
        payment = calculate_minimum_payment(100, 0.22)
        
        # Minimum should be at least $25
        assert payment >= 25
    
    def test_minimum_payment_large_balance(self):
        """Test minimum payment on large balance."""
        payment = calculate_minimum_payment(5000, 0.22)
        
        # Should be roughly 2% of balance
        assert payment > 100
        assert payment < 200
    
    def test_minimum_payment_zero_balance(self):
        """Test minimum payment with zero balance."""
        payment = calculate_minimum_payment(0, 0.22)
        assert payment == 0


class TestCreditCardPayoffSimulation:
    """Test credit card payoff scenarios."""
    
    def test_minimum_payment_trap(self):
        """Test the minimum payment trap - takes forever to pay off."""
        initial_balance = 1000
        apr = 0.22
        monthly_payment = 25  # Minimum payment
        
        simulation = simulate_credit_card_payoff(
            initial_balance=initial_balance,
            apr=apr,
            monthly_payment=monthly_payment
        )
        
        # Should take a long time (many months)
        months_to_payoff = len(simulation.month_by_month)
        assert months_to_payoff > 30  # Should take 30+ months
        
        # Should pay significant interest
        total_paid = simulation.total_amount_paid
        interest = total_paid - initial_balance
        assert interest > initial_balance * 0.30  # At least 30% interest
    
    def test_fixed_payment_better(self):
        """Test fixed payment is better than minimum."""
        initial_balance = 1000
        apr = 0.22
        
        minimum_sim = simulate_credit_card_payoff(
            initial_balance=initial_balance,
            apr=apr,
            monthly_payment=25
        )
        
        fixed_sim = simulate_credit_card_payoff(
            initial_balance=initial_balance,
            apr=apr,
            monthly_payment=100
        )
        
        # Fixed payment pays off faster
        assert len(fixed_sim.month_by_month) < len(minimum_sim.month_by_month)
        
        # Fixed payment pays less interest
        assert fixed_sim.total_amount_paid < minimum_sim.total_amount_paid
    
    def test_aggressive_payment_best(self):
        """Test aggressive payment is best."""
        initial_balance = 1000
        apr = 0.22
        
        minimum_sim = simulate_credit_card_payoff(
            initial_balance=initial_balance,
            apr=apr,
            monthly_payment=25
        )
        
        aggressive_sim = simulate_credit_card_payoff(
            initial_balance=initial_balance,
            apr=apr,
            monthly_payment=500
        )
        
        # Aggressive pays off much faster
        assert len(aggressive_sim.month_by_month) < len(minimum_sim.month_by_month)
        
        # Aggressive pays much less interest
        assert aggressive_sim.total_amount_paid < minimum_sim.total_amount_paid


class TestPayoffStrategies:
    """Test comparison of payoff strategies."""
    
    def test_compare_strategies(self):
        """Test strategy comparison."""
        comparison = compare_payoff_strategies(
            initial_balance=2000,
            apr=0.22
        )
        
        assert "minimum_only" in comparison
        assert "fixed_amount" in comparison
        assert "aggressive" in comparison
    
    def test_minimum_vs_fixed(self):
        """Test minimum vs fixed strategy difference."""
        comparison = compare_payoff_strategies(
            initial_balance=1000,
            apr=0.22
        )
        
        minimum = comparison["minimum_only"]["total_interest"]
        fixed = comparison["fixed_amount"]["total_interest"]
        
        # Fixed payment should have significantly less interest
        assert fixed < minimum * 0.5  # At least 50% less interest


class TestCreditCardTraps:
    """Test credit card traps database."""
    
    def test_traps_exist(self):
        """Test that credit card traps are defined."""
        assert len(CREDIT_CARD_TRAPS) > 0
        assert len(CREDIT_CARD_TRAPS) == 8
    
    def test_trap_structure(self):
        """Test each trap has required fields."""
        for trap_id, trap in CREDIT_CARD_TRAPS.items():
            assert "trap_name" in trap
            assert "description" in trap
            assert "financial_impact" in trap
            assert trap["financial_impact"] > 0  # Cost money
    
    def test_specific_traps(self):
        """Test specific important traps exist."""
        trap_ids = set(CREDIT_CARD_TRAPS.keys())
        
        assert "trap_minimum_payment" in trap_ids
        assert "trap_high_interest" in trap_ids
        assert "trap_0_apr_intro" in trap_ids
        assert "trap_annual_fees" in trap_ids
    
    def test_minimum_payment_trap_impact(self):
        """Test minimum payment trap has significant impact."""
        minimum_trap = CREDIT_CARD_TRAPS["trap_minimum_payment"]
        
        # Minimum payment trap should cost at least $200+
        assert minimum_trap["financial_impact"] > 200


class TestCreditCardMyths:
    """Test credit card myths."""
    
    def test_myths_exist(self):
        """Test credit card myths are defined."""
        assert len(CREDIT_CARD_MYTHS) > 0
        assert len(CREDIT_CARD_MYTHS) == 4
    
    def test_myth_structure(self):
        """Test each myth has required fields."""
        for myth_id, myth in CREDIT_CARD_MYTHS.items():
            assert "myth" in myth
            assert "fact" in myth
            assert len(myth["myth"]) > 0
            assert len(myth["fact"]) > 0
    
    def test_carrying_balance_myth(self):
        """Test carrying balance myth is debunked."""
        myths = {k: v for k, v in CREDIT_CARD_MYTHS.items()}
        
        # Find the carrying balance myth
        found = False
        for myth_id, myth_data in myths.items():
            if "carrying" in myth_data["myth"].lower() or "balance" in myth_data["myth"].lower():
                assert "FALSE" in myth_data["fact"] or "false" in myth_data["fact"].lower()
                found = True
        
        assert found, "Carrying balance myth should be included"


class TestPayoffInsights:
    """Test payoff strategy insights."""
    
    def test_insights_provided(self):
        """Test that insights are provided."""
        insights = get_payoff_insights(
            initial_balance=1000,
            apr=0.22,
            monthly_budget=100
        )
        
        assert len(insights) > 0
        assert isinstance(insights, list)
    
    def test_insights_are_actionable(self):
        """Test insights provide actionable advice."""
        insights = get_payoff_insights(
            initial_balance=5000,
            apr=0.25,
            monthly_budget=200
        )
        
        for insight in insights:
            # Should be string with advice
            assert isinstance(insight, str)
            assert len(insight) > 0
    
    def test_insights_show_urgency(self):
        """Test insights highlight urgency of high-interest debt."""
        insights = get_payoff_insights(
            initial_balance=2000,
            apr=0.29,  # High APR
            monthly_budget=50
        )
        
        # Should warn about slow payoff
        insights_text = " ".join(insights).lower()
        assert any(word in insights_text for word in [
            "slow", "long", "years", "expensive", "interest"
        ])


class TestPayoffTiming:
    """Test payoff timing and duration."""
    
    def test_payoff_under_one_year_aggressive(self):
        """Test aggressive payment pays off in under a year."""
        simulation = simulate_credit_card_payoff(
            initial_balance=500,
            apr=0.22,
            monthly_payment=300
        )
        
        months = len(simulation.month_by_month)
        assert months < 12
    
    def test_payoff_takes_years_minimum(self):
        """Test minimum payment takes years."""
        simulation = simulate_credit_card_payoff(
            initial_balance=2000,
            apr=0.22,
            monthly_payment=25
        )
        
        months = len(simulation.month_by_month)
        years = months / 12
        assert years > 2  # Should take over 2 years


class TestInterestCalculation:
    """Test interest calculation accuracy."""
    
    def test_apr_applied_correctly(self):
        """Test APR is applied correctly."""
        initial_balance = 1000
        apr = 0.22
        monthly_rate = apr / 12
        
        simulation = simulate_credit_card_payoff(
            initial_balance=initial_balance,
            apr=apr,
            monthly_payment=100
        )
        
        # First month should have approximately right interest
        first_month = simulation.month_by_month[0]
        expected_interest = initial_balance * monthly_rate
        
        # Allow 10% margin for rounding
        assert abs(first_month["interest_charged"] - expected_interest) < expected_interest * 0.10
    
    def test_higher_apr_means_more_interest(self):
        """Test higher APR results in more total interest."""
        low_apr_sim = simulate_credit_card_payoff(
            initial_balance=1000,
            apr=0.10,
            monthly_payment=100
        )
        
        high_apr_sim = simulate_credit_card_payoff(
            initial_balance=1000,
            apr=0.25,
            monthly_payment=100
        )
        
        low_interest = low_apr_sim.total_amount_paid - 1000
        high_interest = high_apr_sim.total_amount_paid - 1000
        
        assert high_interest > low_interest


class TestPaymentAllocation:
    """Test how payments are allocated."""
    
    def test_payment_covers_interest(self):
        """Test payment covers interest."""
        simulation = simulate_credit_card_payoff(
            initial_balance=1000,
            apr=0.22,
            monthly_payment=50
        )
        
        # Payment should cover interest and reduce principal
        first_month = simulation.month_by_month[0]
        assert first_month["payment"] >= first_month["interest_charged"]
    
    def test_excess_payment_reduces_principal(self):
        """Test excess payment reduces principal."""
        simulation = simulate_credit_card_payoff(
            initial_balance=1000,
            apr=0.22,
            monthly_payment=200
        )
        
        first_month = simulation.month_by_month[0]
        # Principal reduction = payment - interest
        principal_reduction = first_month["payment"] - first_month["interest_charged"]
        assert principal_reduction > 0


class TestZeroAprScenario:
    """Test 0% APR scenarios."""
    
    def test_zero_apr_no_interest(self):
        """Test 0% APR has no interest charges."""
        simulation = simulate_credit_card_payoff(
            initial_balance=1000,
            apr=0.0,
            monthly_payment=100
        )
        
        # Total should just be the payment amount
        assert simulation.total_interest == 0
    
    def test_zero_apr_payoff_time(self):
        """Test 0% APR payoff time."""
        simulation = simulate_credit_card_payoff(
            initial_balance=1000,
            apr=0.0,
            monthly_payment=100
        )
        
        # Should pay off in exactly 10 months (1000/100)
        months = len(simulation.month_by_month)
        assert months == 10


class TestHighBalanceScenario:
    """Test high balance scenarios."""
    
    def test_high_balance_long_payoff(self):
        """Test high balance takes long to pay off."""
        simulation = simulate_credit_card_payoff(
            initial_balance=10000,
            apr=0.22,
            monthly_payment=100
        )
        
        months = len(simulation.month_by_month)
        # Should take over 1 year
        assert months > 12
    
    def test_high_balance_high_interest(self):
        """Test high balance pays significant interest."""
        simulation = simulate_credit_card_payoff(
            initial_balance=10000,
            apr=0.22,
            monthly_payment=100
        )
        
        interest = simulation.total_amount_paid - 10000
        # Should pay at least 30% in interest
        assert interest > 10000 * 0.30
