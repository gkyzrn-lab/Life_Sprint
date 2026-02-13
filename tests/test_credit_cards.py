"""
Tests for credit card catalog and financial responsibility features.
"""

import pytest
from catalogs.credit_cards import (
    CREDIT_CARDS,
    BankTier,
    CreditCardCategory,
    get_card,
    get_cards_by_tier,
    get_cards_player_qualifies_for,
    calculate_monthly_perks_value,
    estimate_annual_cost_benefit,
    get_credit_building_advice,
    compare_cards,
    get_all_cards
)

def test_credit_cards_exist():
    """Test that credit card catalog is populated."""
    assert len(CREDIT_CARDS) >= 7  # We created 7 cards
    
    # Check each tier has cards
    premium_cards = [c for c in CREDIT_CARDS.values() if c["tier"] == BankTier.PREMIUM]
    standard_cards = [c for c in CREDIT_CARDS.values() if c["tier"] == BankTier.STANDARD]
    starter_cards = [c for c in CREDIT_CARDS.values() if c["tier"] == BankTier.STARTER]
    
    assert len(premium_cards) >= 2
    assert len(standard_cards) >= 2
    assert len(starter_cards) >= 3

def test_credit_card_structure():
    """Test that credit cards have all required fields."""
    required_fields = [
        "id", "bank_name", "card_name", "tier", "category", 
        "apr", "credit_limit_range", "perks", "requirements",
        "credit_building", "educational_info", "application_difficulty"
    ]
    
    for card_id, card in CREDIT_CARDS.items():
        for field in required_fields:
            assert field in card, f"Card {card_id} missing field: {field}"
        
        # Check APR is reasonable
        assert 0 <= card["apr"] <= 30, f"Card {card_id} has unrealistic APR: {card['apr']}"
        
        # Check credit limits make sense
        min_limit, max_limit = card["credit_limit_range"]
        assert min_limit <= max_limit, f"Card {card_id} has invalid credit limit range"
        assert min_limit >= 0, f"Card {card_id} has negative credit limit"

def test_tier_progression():
    """Test that tiers have appropriate characteristics."""
    premium = [c for c in CREDIT_CARDS.values() if c["tier"] == BankTier.PREMIUM]
    starter = [c for c in CREDIT_CARDS.values() if c["tier"] == BankTier.STARTER]
    standard = [c for c in CREDIT_CARDS.values() if c["tier"] == BankTier.STANDARD]
    
    # Premium cards are TRAPS - they have high fees AND high APRs to teach students to avoid them
    avg_premium_apr = sum(c["apr"] for c in premium) / len(premium)
    avg_starter_apr = sum(c["apr"] for c in starter if c["apr"] > 0) / len([c for c in starter if c["apr"] > 0])
    
    # Premium cards should have comparable or higher APR (they're traps!)
    assert avg_premium_apr >= 23, f"Premium cards should have high APR to teach they're expensive traps, got {avg_premium_apr}"
    
    # Premium cards should have higher credit limits
    premium_max = max(c["credit_limit_range"][1] for c in premium)
    starter_max = max(c["credit_limit_range"][1] for c in starter if c["credit_limit_range"][1] > 0)
    
    assert premium_max >= starter_max, "Premium cards should have higher limits"
    
    # Premium cards should have annual fees, basic cards should not
    premium_with_fees = sum(1 for c in premium if c.get("annual_fee", 0) > 0)
    assert premium_with_fees >= 1, "At least some premium cards should have annual fees"
    
    standard_no_fees = sum(1 for c in standard if c.get("annual_fee", 0) == 0)
    assert standard_no_fees == len(standard), "Standard cards should have no annual fees"
    
    starter_no_fees = sum(1 for c in starter if c.get("annual_fee", 0) == 0)
    assert starter_no_fees >= len(starter) - 1, "Most starter cards should have no annual fees"

def test_get_card():
    """Test retrieving specific credit card."""
    card = get_card("premium_rewards_platinum")
    assert card is not None
    assert card["bank_name"] == "Chase Sapphire"
    assert card["tier"] == BankTier.PREMIUM
    
    # Test non-existent card
    assert get_card("fake_card_id") is None

def test_get_cards_by_tier():
    """Test filtering cards by tier."""
    premium = get_cards_by_tier(BankTier.PREMIUM)
    assert len(premium) >= 2
    assert all(c["tier"] == BankTier.PREMIUM for c in premium)
    
    standard = get_cards_by_tier(BankTier.STANDARD)
    assert len(standard) >= 2
    assert all(c["tier"] == BankTier.STANDARD for c in standard)
    
    starter = get_cards_by_tier(BankTier.STARTER)
    assert len(starter) >= 3
    assert all(c["tier"] == BankTier.STARTER for c in starter)

def test_player_qualification_no_credit():
    """Test that players with no credit qualify for appropriate cards."""
    player_state = {
        "credit_score": 0,
        "annual_income": 0,
        "is_student": True,
        "balance": 300
    }
    
    qualified = get_cards_player_qualifies_for(player_state)
    
    # Should qualify for secured card and prepaid
    assert len(qualified) >= 2
    
    # Should include secured card
    secured_cards = [c for c in qualified if c["category"] == CreditCardCategory.SECURED]
    assert len(secured_cards) >= 1
    
    # Should NOT include premium cards
    premium_cards = [c for c in qualified if c["tier"] == BankTier.PREMIUM]
    assert len(premium_cards) == 0

def test_player_qualification_good_credit():
    """Test that players with good credit qualify for premium cards."""
    player_state = {
        "credit_score": 720,
        "annual_income": 15000,
        "is_student": True,
        "balance": 1000
    }
    
    qualified = get_cards_player_qualifies_for(player_state)
    
    # Should qualify for many cards
    assert len(qualified) >= 5
    
    # Should include premium cards
    premium_cards = [c for c in qualified if c["tier"] == BankTier.PREMIUM]
    assert len(premium_cards) >= 1
    
    # Cards should be sorted by tier (best first)
    tiers = [c["tier"] for c in qualified]
    tier_order = {BankTier.PREMIUM: 0, BankTier.STANDARD: 1, BankTier.STARTER: 2}
    tier_scores = [tier_order[t] for t in tiers]
    assert tier_scores == sorted(tier_scores), "Cards should be sorted by tier quality"

def test_player_qualification_fair_credit():
    """Test that players with fair credit get appropriate cards."""
    player_state = {
        "credit_score": 650,
        "annual_income": 8000,
        "is_student": True,
        "balance": 500
    }
    
    qualified = get_cards_player_qualifies_for(player_state)
    
    # Should qualify for standard and starter, not premium
    standard_cards = [c for c in qualified if c["tier"] == BankTier.STANDARD]
    starter_cards = [c for c in qualified if c["tier"] == BankTier.STARTER]
    premium_cards = [c for c in qualified if c["tier"] == BankTier.PREMIUM]
    
    assert len(standard_cards) >= 1
    assert len(starter_cards) >= 1
    assert len(premium_cards) == 0  # Score too low for premium

def test_security_deposit_requirement():
    """Test that secured cards require sufficient funds."""
    # Player with enough for deposit
    player_with_funds = {
        "credit_score": 0,
        "annual_income": 0,
        "is_student": True,
        "balance": 250
    }
    
    qualified = get_cards_player_qualifies_for(player_with_funds)
    secured_cards = [c for c in qualified if c.get("requires_security_deposit")]
    assert len(secured_cards) >= 1
    
    # Player without enough for deposit
    player_without_funds = {
        "credit_score": 0,
        "annual_income": 0,
        "is_student": True,
        "balance": 50
    }
    
    qualified_no_funds = get_cards_player_qualifies_for(player_without_funds)
    secured_cards_no_funds = [c for c in qualified_no_funds if c.get("requires_security_deposit")]
    assert len(secured_cards_no_funds) == 0

def test_calculate_monthly_perks_value():
    """Test calculation of monthly perks value."""
    premium_card = get_card("premium_rewards_platinum")
    perks_value = calculate_monthly_perks_value(premium_card)
    
    # Should include gym membership + streaming credits
    assert perks_value >= 35  # $25 gym + $10 streaming
    
    # Prepaid card should have no perks value
    prepaid = get_card("starter_prepaid_card")
    prepaid_value = calculate_monthly_perks_value(prepaid)
    assert prepaid_value == 0

def test_estimate_annual_cost_benefit():
    """Test annual cost/benefit calculation."""
    premium_card = get_card("premium_rewards_platinum")
    
    # Low spending
    low_spending = estimate_annual_cost_benefit(premium_card, 200)
    assert "cashback_earned" in low_spending
    assert "perks_annual_value" in low_spending
    assert "first_year_net_benefit" in low_spending
    assert "ongoing_annual_benefit" in low_spending
    assert "annual_fee" in low_spending
    
    # First year should be better (fee waived + signup bonus)
    assert low_spending["first_year_net_benefit"] > low_spending["ongoing_annual_benefit"]
    
    # High spending
    high_spending = estimate_annual_cost_benefit(premium_card, 1000)
    assert high_spending["cashback_earned"] > low_spending["cashback_earned"]
    
    # Break-even calculation
    assert "break_even_spending" in high_spending
    assert high_spending["break_even_spending"] is not None

def test_credit_building_advice_no_credit():
    """Test advice for building credit from scratch."""
    advice = get_credit_building_advice(0)
    
    assert advice["status"] == "No Credit History"
    assert "secured" in advice["recommendation"].lower()
    assert len(advice["best_cards"]) > 0
    assert len(advice["tips"]) >= 3
    assert "timeline" in advice

def test_credit_building_advice_poor():
    """Test advice for poor credit."""
    advice = get_credit_building_advice(580)
    
    assert advice["status"] == "Poor Credit"
    assert len(advice["tips"]) >= 3
    assert "pay" in advice["tips"][0].lower() and "time" in advice["tips"][0].lower()  # Payment history is #1

def test_credit_building_advice_good():
    """Test advice for good credit."""
    advice = get_credit_building_advice(710)
    
    assert advice["status"] == "Good Credit"
    assert "premium" in advice["recommendation"].lower()
    assert len(advice["best_cards"]) > 0

def test_credit_building_advice_excellent():
    """Test advice for excellent credit."""
    advice = get_credit_building_advice(760)
    
    assert advice["status"] == "Excellent Credit"
    assert len(advice["best_cards"]) >= 2
    # Should include premium cards
    assert any("premium" in card_id for card_id in advice["best_cards"])

def test_compare_cards():
    """Test side-by-side card comparison."""
    card_ids = ["premium_rewards_platinum", "standard_student_visa", "starter_secured_card"]
    comparison = compare_cards(card_ids)
    
    assert "cards" in comparison
    assert len(comparison["cards"]) == 3
    
    assert "winner_categories" in comparison
    assert "lowest_apr" in comparison["winner_categories"]
    assert "highest_cashback" in comparison["winner_categories"]
    assert "easiest_approval" in comparison["winner_categories"]
    
    # Premium should have best cashback (check for "premium" anywhere in the name or "platinum")
    highest_cashback = comparison["winner_categories"]["highest_cashback"].lower()
    assert "premium" in highest_cashback or "platinum" in highest_cashback
    
    # Secured should be easiest to approve
    assert "secured" in comparison["winner_categories"]["easiest_approval"].lower()

def test_educational_info():
    """Test that all cards have educational content."""
    for card_id, card in CREDIT_CARDS.items():
        edu_info = card["educational_info"]
        
        assert "best_for" in edu_info, f"Card {card_id} missing 'best_for'"
        assert "warning" in edu_info, f"Card {card_id} missing 'warning'"
        assert "tip" in edu_info, f"Card {card_id} missing 'tip'"
        
        # Educational content should be substantial
        assert len(edu_info["best_for"]) > 20
        assert len(edu_info["warning"]) > 20
        assert len(edu_info["tip"]) > 20

def test_credit_building_flags():
    """Test that cards properly indicate credit building capabilities."""
    for card_id, card in CREDIT_CARDS.items():
        credit_building = card["credit_building"]
        
        assert "reports_to_bureaus" in credit_building
        assert "credit_score_impact" in credit_building
        
        # Prepaid card should not build credit
        if card.get("is_prepaid"):
            assert credit_building["reports_to_bureaus"] == False
            assert credit_building["credit_score_impact"] == "none"
        else:
            # All other cards should build credit
            assert credit_building["reports_to_bureaus"] == True
            assert credit_building["credit_score_impact"] in ["low", "medium", "high"]

def test_apr_reflects_tier():
    """Test that APR reflects educational design - premium cards are expensive traps."""
    for card_id, card in CREDIT_CARDS.items():
        tier = card["tier"]
        apr = card["apr"]
        
        if tier == BankTier.PREMIUM and apr > 0:
            # Premium cards should have HIGH APR (23-25%) to teach they're expensive traps
            assert apr >= 23, f"Premium card {card_id} should have high APR (23-25%), got: {apr}"
            assert apr <= 25, f"Premium card {card_id} has unrealistic APR: {apr}"
        
        if tier == BankTier.STARTER and apr > 0:
            assert apr >= 18, f"Starter card {card_id} has suspiciously low APR: {apr}"

def test_perks_reflect_tier():
    """Test that premium cards have better perks."""
    premium = [c for c in CREDIT_CARDS.values() if c["tier"] == BankTier.PREMIUM]
    starter = [c for c in CREDIT_CARDS.values() if c["tier"] == BankTier.STARTER]
    
    # Premium cards should have higher cashback
    premium_cashback = [c["perks"].get("cashback_rate", 0) for c in premium]
    starter_cashback = [c["perks"].get("cashback_rate", 0) for c in starter]
    
    avg_premium_cashback = sum(premium_cashback) / len(premium_cashback) if premium_cashback else 0
    avg_starter_cashback = sum(starter_cashback) / len(starter_cashback) if starter_cashback else 0
    
    assert avg_premium_cashback >= avg_starter_cashback

def test_all_categories_represented():
    """Test that we have cards in all major categories."""
    categories_found = set(c["category"] for c in CREDIT_CARDS.values())
    
    assert CreditCardCategory.STUDENT in categories_found
    assert CreditCardCategory.CASHBACK in categories_found
    assert CreditCardCategory.SECURED in categories_found

def test_get_all_cards():
    """Test getting all cards."""
    all_cards = get_all_cards()
    assert len(all_cards) == len(CREDIT_CARDS)
    assert all_cards == CREDIT_CARDS
