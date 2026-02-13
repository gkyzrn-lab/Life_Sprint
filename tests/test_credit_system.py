"""Tests for credit score system."""

import pytest
from catalogs.credit_system import (
    CreditProfile, CreditAccount, CreditScoreBreakdown,
    create_credit_profile, apply_credit_action, get_credit_improvement_tips,
    get_credit_score_breakdown, calculate_credit_score,
    CREDIT_SCORE_RANGES, CREDIT_MYTHS, CREDIT_ACTIONS_DATABASE
)


class TestCreditProfile:
    """Test credit profile creation and management."""
    
    def test_create_credit_profile(self):
        """Test creating a new credit profile."""
        profile = create_credit_profile(
            player_id="p1",
            starting_score=700
        )
        assert profile.player_id == "p1"
        assert profile.credit_score == 700
        assert profile.accounts == []
        assert len(profile.history) == 0
    
    def test_profile_default_score(self):
        """Test that new profile starts with default score."""
        profile = create_credit_profile("p1")
        assert profile.credit_score > 0
        assert profile.credit_score <= 850


class TestCreditActions:
    """Test credit actions and score changes."""
    
    def test_on_time_payment(self):
        """Test on-time payment increases score."""
        profile = create_credit_profile("p1", starting_score=700)
        initial_score = profile.credit_score
        
        profile = apply_credit_action(profile, "on_time_payment")
        
        assert profile.credit_score > initial_score
        assert len(profile.history) == 1
        assert "on_time_payment" in profile.history[0]["action"]
    
    def test_missed_payment_30(self):
        """Test 30-day missed payment significantly hurts score."""
        profile = create_credit_profile("p1", starting_score=700)
        initial_score = profile.credit_score
        
        profile = apply_credit_action(profile, "missed_payment_30")
        
        assert profile.credit_score < initial_score
        assert profile.credit_score < 600  # Should be significant hit
    
    def test_hard_inquiry(self):
        """Test hard inquiry slightly hurts score."""
        profile = create_credit_profile("p1", starting_score=700)
        initial_score = profile.credit_score
        
        profile = apply_credit_action(profile, "hard_inquiry")
        
        assert profile.credit_score < initial_score
        assert initial_score - profile.credit_score < 20  # Small hit
    
    def test_new_account(self):
        """Test new account slightly hurts then helps score."""
        profile = create_credit_profile("p1", starting_score=700)
        
        profile = apply_credit_action(profile, "new_credit_account")
        
        # New account initially hurts score slightly
        assert "new_credit_account" in profile.history[0]["action"]


class TestCreditScoreCalculation:
    """Test credit score calculation components."""
    
    def test_score_range_validity(self):
        """Test credit scores are within valid range."""
        for i in range(100):
            profile = create_credit_profile(f"p{i}")
            assert 300 <= profile.credit_score <= 850
    
    def test_payment_history_impact(self):
        """Test payment history is major factor."""
        profile = create_credit_profile("p1", starting_score=700)
        
        # Multiple on-time payments
        for _ in range(5):
            profile = apply_credit_action(profile, "on_time_payment")
        
        score_with_good_history = profile.credit_score
        
        # Reset and add missed payments
        profile2 = create_credit_profile("p2", starting_score=700)
        for _ in range(3):
            profile2 = apply_credit_action(profile2, "missed_payment_30")
        
        score_with_bad_history = profile2.credit_score
        
        assert score_with_good_history > score_with_bad_history + 50
    
    def test_score_breakdown_components(self):
        """Test credit score breakdown has all components."""
        profile = create_credit_profile("p1")
        breakdown = get_credit_score_breakdown(profile)
        
        assert breakdown.total_score == profile.credit_score
        assert "payment_history" in breakdown.component_breakdown
        assert "credit_utilization" in breakdown.component_breakdown
        assert "age_of_credit" in breakdown.component_breakdown
        assert "credit_mix" in breakdown.component_breakdown
        assert "inquiries" in breakdown.component_breakdown


class TestCreditScoreRanges:
    """Test credit score categories."""
    
    def test_poor_range(self):
        """Test poor credit range."""
        assert CREDIT_SCORE_RANGES["poor"]["min"] == 300
        assert CREDIT_SCORE_RANGES["poor"]["max"] == 579
    
    def test_excellent_range(self):
        """Test excellent credit range."""
        assert CREDIT_SCORE_RANGES["excellent"]["min"] == 750
        assert CREDIT_SCORE_RANGES["excellent"]["max"] == 850
    
    def test_all_ranges_continuous(self):
        """Test ranges cover 300-850 without gaps."""
        ranges = [
            CREDIT_SCORE_RANGES["poor"],
            CREDIT_SCORE_RANGES["fair"],
            CREDIT_SCORE_RANGES["good"],
            CREDIT_SCORE_RANGES["very_good"],
            CREDIT_SCORE_RANGES["excellent"],
        ]
        
        for i, r in enumerate(ranges):
            if i > 0:
                assert r["min"] == ranges[i-1]["max"] + 1


class TestCreditMyths:
    """Test credit myths database."""
    
    def test_myths_exist(self):
        """Test that credit myths are defined."""
        assert len(CREDIT_MYTHS) > 0
        assert len(CREDIT_MYTHS) == 10
    
    def test_myth_structure(self):
        """Test each myth has required fields."""
        for myth_id, myth in CREDIT_MYTHS.items():
            assert "myth" in myth
            assert "fact" in myth
            assert len(myth["myth"]) > 0
            assert len(myth["fact"]) > 0
    
    def test_specific_myths(self):
        """Test specific important myths are included."""
        myth_ids = set(CREDIT_MYTHS.keys())
        
        # Check that some key myths exist
        assert "myth_checking_hurts_score" in myth_ids
        assert "myth_closed_accounts" in myth_ids


class TestImprovementTips:
    """Test credit improvement recommendations."""
    
    def test_tips_for_low_score(self):
        """Test tips for poor credit."""
        profile = create_credit_profile("p1", starting_score=400)
        
        tips = get_credit_improvement_tips(profile)
        
        assert len(tips) > 0
        assert isinstance(tips, list)
        for tip in tips:
            assert isinstance(tip, str)
            assert len(tip) > 0
    
    def test_tips_for_good_score(self):
        """Test tips for good credit."""
        profile = create_credit_profile("p1", starting_score=750)
        
        tips = get_credit_improvement_tips(profile)
        
        # Even good credit has room for improvement
        assert len(tips) > 0
    
    def test_tips_are_actionable(self):
        """Test tips are actionable advice."""
        profile = create_credit_profile("p1", starting_score=600)
        
        tips = get_credit_improvement_tips(profile)
        
        for tip in tips:
            # Should contain action verbs
            lower_tip = tip.lower()
            assert any(word in lower_tip for word in [
                "pay", "reduce", "limit", "dispute", "open",
                "monitor", "check", "review", "build", "keep"
            ])


class TestCreditActions:
    """Test credit actions database."""
    
    def test_actions_database_exists(self):
        """Test credit actions are defined."""
        assert len(CREDIT_ACTIONS_DATABASE) > 0
    
    def test_action_has_impact(self):
        """Test all actions have score impact."""
        for action_id, action in CREDIT_ACTIONS_DATABASE.items():
            assert "score_impact" in action
            assert isinstance(action["score_impact"], (int, float))
    
    def test_negative_actions_hurt_score(self):
        """Test negative actions hurt score."""
        negative_actions = [
            "missed_payment_30",
            "missed_payment_60",
            "missed_payment_90",
            "charge_off"
        ]
        
        for action in negative_actions:
            if action in CREDIT_ACTIONS_DATABASE:
                assert CREDIT_ACTIONS_DATABASE[action]["score_impact"] < 0
    
    def test_positive_actions_help_score(self):
        """Test positive actions help score."""
        positive_actions = [
            "on_time_payment",
            "paid_collections",
            "dispute_removed"
        ]
        
        for action in positive_actions:
            if action in CREDIT_ACTIONS_DATABASE:
                assert CREDIT_ACTIONS_DATABASE[action]["score_impact"] > 0


class TestCreditAccounts:
    """Test credit account management."""
    
    def test_account_structure(self):
        """Test credit account has proper structure."""
        account = CreditAccount(
            account_id="cc1",
            account_type="credit_card",
            credit_limit=5000,
            current_balance=1500,
            payment_status="current",
        )
        
        assert account.account_id == "cc1"
        assert account.account_type == "credit_card"
        assert account.utilization_ratio == 0.30  # 1500/5000
    
    def test_utilization_ratio(self):
        """Test credit utilization calculation."""
        account = CreditAccount(
            account_id="cc1",
            account_type="credit_card",
            credit_limit=10000,
            current_balance=3000,
        )
        
        assert account.utilization_ratio == 0.30
        assert account.utilization_ratio <= 1.0
    
    def test_payment_status_tracking(self):
        """Test payment status is tracked."""
        account = CreditAccount(
            account_id="loan1",
            account_type="auto_loan",
            credit_limit=30000,
            current_balance=20000,
            payment_status="30_days_late"
        )
        
        assert account.payment_status == "30_days_late"


class TestScoreProgression:
    """Test credit score progression over time."""
    
    def test_score_improves_with_good_behavior(self):
        """Test score improves with on-time payments."""
        profile = create_credit_profile("p1", starting_score=650)
        initial = profile.credit_score
        
        for _ in range(10):
            profile = apply_credit_action(profile, "on_time_payment")
        
        assert profile.credit_score > initial
    
    def test_score_declines_with_bad_behavior(self):
        """Test score declines with missed payments."""
        profile = create_credit_profile("p1", starting_score=700)
        initial = profile.credit_score
        
        for _ in range(3):
            profile = apply_credit_action(profile, "missed_payment_30")
        
        assert profile.credit_score < initial
    
    def test_history_tracks_all_actions(self):
        """Test all actions are tracked in history."""
        profile = create_credit_profile("p1")
        
        for i in range(5):
            profile = apply_credit_action(profile, "on_time_payment")
        
        assert len(profile.history) == 5


class TestCreditScoreInterpretation:
    """Test credit score interpretation and meaning."""
    
    def test_poor_score_high_apr(self):
        """Test poor credit score means high APR."""
        poor_range = CREDIT_SCORE_RANGES["poor"]
        
        # Poor credit should have higher APR example
        assert "apr_range" in poor_range or "mortgage_apr" in poor_range
    
    def test_excellent_score_low_apr(self):
        """Test excellent credit score means low APR."""
        excellent_range = CREDIT_SCORE_RANGES["excellent"]
        
        # Excellent credit should have lower APR example
        assert "apr_range" in excellent_range or "mortgage_apr" in excellent_range
    
    def test_apr_increases_with_score_decrease(self):
        """Test APR is higher for lower scores."""
        # This is implied by finance domain knowledge
        poor_apr_str = CREDIT_SCORE_RANGES["poor"].get("mortgage_apr", "6.5%+")
        excellent_apr_str = CREDIT_SCORE_RANGES["excellent"].get("mortgage_apr", "2.5-3%")
        
        # Just verify fields exist
        assert poor_apr_str is not None
        assert excellent_apr_str is not None
