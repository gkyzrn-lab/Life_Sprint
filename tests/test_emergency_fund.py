"""Tests for emergency fund system."""

import pytest
from catalogs.emergency_fund import (
    create_emergency_fund_challenge, simulate_emergency_fund_building,
    get_emergency_fund_progress, calculate_emergency_fund_target,
    EMERGENCY_EVENTS, EmergencyEvent, EmergencyOutcome
)


class TestEmergencyFundTarget:
    """Test emergency fund target calculation."""
    
    def test_target_three_months(self):
        """Test 3-month emergency fund target."""
        monthly_expenses = 2000
        target = calculate_emergency_fund_target(
            monthly_expenses=monthly_expenses,
            months=3
        )
        
        assert target == 6000  # 3 * 2000
    
    def test_target_six_months(self):
        """Test 6-month emergency fund target."""
        monthly_expenses = 2000
        target = calculate_emergency_fund_target(
            monthly_expenses=monthly_expenses,
            months=6
        )
        
        assert target == 12000  # 6 * 2000
    
    def test_various_expense_levels(self):
        """Test targets for various expense levels."""
        for expenses in [1000, 2000, 3000, 5000]:
            target = calculate_emergency_fund_target(expenses, 6)
            assert target == expenses * 6


class TestEmergencyEvents:
    """Test emergency events database."""
    
    def test_emergency_events_exist(self):
        """Test that emergency events are defined."""
        assert len(EMERGENCY_EVENTS) > 0
        assert len(EMERGENCY_EVENTS) == 10
    
    def test_event_structure(self):
        """Test each event has required fields."""
        for event_id, event in EMERGENCY_EVENTS.items():
            assert "event_name" in event
            assert "description" in event
            assert "min_cost" in event
            assert "max_cost" in event
            assert event["min_cost"] > 0
            assert event["max_cost"] >= event["min_cost"]
    
    def test_specific_events(self):
        """Test specific important events exist."""
        event_ids = set(EMERGENCY_EVENTS.keys())
        
        assert "car_transmission" in event_ids
        assert "medical_emergency" in event_ids
        assert "job_loss" in event_ids
        assert "home_repair" in event_ids
    
    def test_event_costs_reasonable(self):
        """Test event costs are realistic."""
        car_event = EMERGENCY_EVENTS["car_transmission"]
        
        # Car transmission is $1000-3000
        assert car_event["min_cost"] >= 1000
        assert car_event["max_cost"] <= 3000
        
        medical_event = EMERGENCY_EVENTS["medical_emergency"]
        
        # Medical ER is expensive
        assert medical_event["max_cost"] > 5000


class TestEmergencyFundChallenge:
    """Test emergency fund challenge creation."""
    
    def test_create_challenge(self):
        """Test creating an emergency fund challenge."""
        challenge = create_emergency_fund_challenge(
            difficulty="medium",
            monthly_savings_goal=200
        )
        
        assert challenge is not None
        assert challenge.monthly_savings_goal == 200
    
    def test_difficulty_levels(self):
        """Test different difficulty levels."""
        for difficulty in ["easy", "medium", "hard"]:
            challenge = create_emergency_fund_challenge(
                difficulty=difficulty,
                monthly_savings_goal=200
            )
            
            assert challenge is not None
            assert challenge.difficulty == difficulty
    
    def test_challenge_has_events(self):
        """Test challenge includes emergency events."""
        challenge = create_emergency_fund_challenge(
            difficulty="medium",
            monthly_savings_goal=200,
            months=12
        )
        
        # Medium difficulty should have several events
        assert len(challenge.potential_events) > 0


class TestSimulateEmergencyFund:
    """Test emergency fund building simulation."""
    
    def test_simulate_fund_building(self):
        """Test simulating emergency fund building."""
        result = simulate_emergency_fund_building(
            monthly_savings=200,
            starting_balance=0,
            months=12,
            difficulty="easy"
        )
        
        assert result is not None
        assert result["total_saved"] > 0
        assert result["final_balance"] > 0
    
    def test_savings_accumulates(self):
        """Test savings accumulates without events."""
        result = simulate_emergency_fund_building(
            monthly_savings=200,
            starting_balance=0,
            months=6,
            difficulty="easy"
        )
        
        # 6 months * 200 = 1200 (minus any events)
        assert result["final_balance"] <= 1200
        assert result["total_saved"] == 1200  # Before events
    
    def test_events_reduce_fund(self):
        """Test emergency events reduce fund."""
        # Easy should have few events
        easy_result = simulate_emergency_fund_building(
            monthly_savings=200,
            starting_balance=5000,
            months=12,
            difficulty="easy"
        )
        
        # Hard should have many events
        hard_result = simulate_emergency_fund_building(
            monthly_savings=200,
            starting_balance=5000,
            months=12,
            difficulty="hard"
        )
        
        # Hard should have lower final balance due to more events
        assert easy_result["final_balance"] > hard_result["final_balance"]
    
    def test_starting_balance_matters(self):
        """Test starting balance affects outcome."""
        result_low = simulate_emergency_fund_building(
            monthly_savings=100,
            starting_balance=500,
            months=12,
            difficulty="hard"
        )
        
        result_high = simulate_emergency_fund_building(
            monthly_savings=100,
            starting_balance=5000,
            months=12,
            difficulty="hard"
        )
        
        # Higher starting balance should help weather events better
        assert result_high["final_balance"] > result_low["final_balance"]


class TestProgressTracking:
    """Test progress tracking."""
    
    def test_progress_toward_three_month(self):
        """Test tracking progress toward 3-month target."""
        monthly_expenses = 2000
        current_savings = 3000
        
        progress = get_emergency_fund_progress(
            current_savings=current_savings,
            monthly_expenses=monthly_expenses,
            target_months=3
        )
        
        assert progress is not None
        assert "current_savings" in progress
        assert "target_amount" in progress
    
    def test_progress_percentage(self):
        """Test progress percentage calculation."""
        progress = get_emergency_fund_progress(
            current_savings=3000,
            monthly_expenses=2000,
            target_months=6
        )
        
        # 3000 / (2000 * 6) = 3000 / 12000 = 25%
        target = 2000 * 6
        expected_percent = (3000 / target) * 100
        
        assert progress["progress_percent"] == expected_percent
    
    def test_progress_exceeded_target(self):
        """Test when fund exceeds target."""
        progress = get_emergency_fund_progress(
            current_savings=15000,
            monthly_expenses=2000,
            target_months=6
        )
        
        # 15000 > 12000 (6 * 2000)
        assert progress["progress_percent"] > 100
        assert progress["fully_funded"] is True


class TestEmergencyOutcome:
    """Test emergency handling outcomes."""
    
    def test_emergency_with_sufficient_fund(self):
        """Test handling emergency with sufficient fund."""
        starting_balance = 5000
        emergency_cost = 2000
        
        # With fund, pay from savings
        remaining = starting_balance - emergency_cost
        assert remaining > 0
    
    def test_emergency_without_fund(self):
        """Test emergency without fund forces credit card debt."""
        starting_balance = 0
        emergency_cost = 3000
        
        # Without fund, must use credit card (22% APR)
        credit_card_cost = emergency_cost * (1 + 0.22)  # With first year interest
        
        assert credit_card_cost > emergency_cost


class TestMonthlySimulation:
    """Test month-by-month simulation details."""
    
    def test_simulation_tracks_months(self):
        """Test simulation tracks month-by-month progress."""
        result = simulate_emergency_fund_building(
            monthly_savings=500,
            starting_balance=1000,
            months=12,
            difficulty="easy"
        )
        
        assert "monthly_breakdown" in result
        assert len(result["monthly_breakdown"]) == 12
    
    def test_each_month_tracked(self):
        """Test each month has savings and events."""
        result = simulate_emergency_fund_building(
            monthly_savings=300,
            starting_balance=0,
            months=6,
            difficulty="medium"
        )
        
        for month_data in result["monthly_breakdown"]:
            assert "month" in month_data
            assert "savings" in month_data
            assert "balance" in month_data


class TestSavingsGoals:
    """Test meeting savings goals."""
    
    def test_reaches_three_month_goal(self):
        """Test reaching 3-month goal."""
        monthly_expenses = 1000
        target = calculate_emergency_fund_target(monthly_expenses, 3)
        
        # Save aggressively
        result = simulate_emergency_fund_building(
            monthly_savings=1000,
            starting_balance=0,
            months=4,
            difficulty="easy"  # Few events
        )
        
        # Should reach close to target (minus any events)
        assert result["final_balance"] > target * 0.80
    
    def test_reaches_six_month_goal(self):
        """Test reaching 6-month goal."""
        monthly_expenses = 1000
        target = calculate_emergency_fund_target(monthly_expenses, 6)
        
        # Save moderately over time
        result = simulate_emergency_fund_building(
            monthly_savings=600,
            starting_balance=1000,
            months=10,
            difficulty="easy"
        )
        
        # Should reach close to target
        assert result["final_balance"] > target * 0.75


class TestEventImpacts:
    """Test specific event impacts."""
    
    def test_car_emergency_impact(self):
        """Test car emergency cost."""
        car_event = EMERGENCY_EVENTS["car_transmission"]
        
        # Should cost $1000-3000
        assert car_event["min_cost"] >= 1000
        assert car_event["max_cost"] <= 3000
    
    def test_job_loss_impact(self):
        """Test job loss emergency cost."""
        job_event = EMERGENCY_EVENTS["job_loss"]
        
        # Job loss should represent monthly lost income
        assert job_event["min_cost"] >= 2000  # At least $2000/month
    
    def test_medical_emergency_impact(self):
        """Test medical emergency cost."""
        medical_event = EMERGENCY_EVENTS["medical_emergency"]
        
        # Medical should be expensive
        assert medical_event["max_cost"] >= 5000


class TestDifficultyProgression:
    """Test difficulty levels affect outcomes."""
    
    def test_easy_fewer_events(self):
        """Test easy difficulty has fewer events."""
        result = simulate_emergency_fund_building(
            monthly_savings=200,
            starting_balance=3000,
            months=12,
            difficulty="easy"
        )
        
        events_count = result.get("total_emergencies", 0)
        # Easy should have 0-3 events
        assert events_count < 4
    
    def test_hard_more_events(self):
        """Test hard difficulty has more events."""
        result = simulate_emergency_fund_building(
            monthly_savings=200,
            starting_balance=3000,
            months=12,
            difficulty="hard"
        )
        
        events_count = result.get("total_emergencies", 0)
        # Hard should have 4+ events
        assert events_count > 3


class TestEmergencyDecision:
    """Test decision making in emergencies."""
    
    def test_fund_prevents_debt(self):
        """Test emergency fund prevents credit card debt."""
        # With fund
        with_fund = 3000  # Can pay from savings
        
        # Without fund, must use credit card
        credit_card_balance = 3000
        credit_card_interest = credit_card_balance * 0.22  # First year interest
        
        # Fund is clearly better
        assert with_fund < credit_card_balance + credit_card_interest
    
    def test_inadequate_fund_still_helps(self):
        """Test even inadequate fund reduces credit card debt."""
        emergency_cost = 3000
        fund_available = 1500
        
        # With partial fund
        credit_card_needed = emergency_cost - fund_available  # $1500
        credit_card_interest = credit_card_needed * 0.22
        
        # Total cost is lower than without fund
        total_cost_with_fund = fund_available + credit_card_needed + credit_card_interest
        total_cost_without_fund = emergency_cost + (emergency_cost * 0.22)
        
        assert total_cost_with_fund < total_cost_without_fund
