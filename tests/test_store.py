"""
Tests for the store catalog system.
"""

import pytest
from catalogs.store import (
    STORE_ITEMS,
    StoreCategory,
    get_store_item,
    get_items_by_category,
    get_affordable_items,
    purchase_item,
    calculate_monthly_expenses,
    get_smart_recommendations,
    get_all_items,
    get_item_count
)

def test_store_has_minimum_items():
    """Test that store has at least 25 items as requested."""
    assert len(STORE_ITEMS) >= 25, f"Store should have at least 25 items, has {len(STORE_ITEMS)}"

def test_all_categories_represented():
    """Test that all categories have items."""
    categories_found = set(item["category"] for item in STORE_ITEMS.values())
    
    assert StoreCategory.ENTERTAINMENT in categories_found
    assert StoreCategory.TECHNOLOGY in categories_found
    assert StoreCategory.FOOD in categories_found
    assert StoreCategory.SOCIAL in categories_found
    assert StoreCategory.HEALTH in categories_found
    assert StoreCategory.EDUCATION in categories_found

def test_item_structure():
    """Test that all items have required fields."""
    required_fields = ["id", "name", "category", "price", "description", "effects"]
    
    for item_id, item in STORE_ITEMS.items():
        for field in required_fields:
            assert field in item, f"Item {item_id} missing field: {field}"
        
        # Price should be reasonable
        assert item["price"] > 0, f"Item {item_id} has invalid price"
        assert item["price"] < 10000, f"Item {item_id} price too high"
        
        # Effects should be a dict
        assert isinstance(item["effects"], dict), f"Item {item_id} effects should be dict"
        assert len(item["effects"]) > 0, f"Item {item_id} should have at least one effect"

def test_get_store_item():
    """Test retrieving specific items."""
    laptop = get_store_item("laptop")
    assert laptop is not None
    assert laptop["name"] == "Student Laptop"
    assert laptop["price"] == 1200.00
    
    # Non-existent item
    assert get_store_item("fake_item") is None

def test_get_items_by_category():
    """Test filtering by category."""
    tech_items = get_items_by_category(StoreCategory.TECHNOLOGY)
    assert len(tech_items) >= 3
    assert all(item["category"] == StoreCategory.TECHNOLOGY for item in tech_items)
    
    food_items = get_items_by_category(StoreCategory.FOOD)
    assert len(food_items) >= 3
    
    social_items = get_items_by_category(StoreCategory.SOCIAL)
    assert len(social_items) >= 3

def test_get_affordable_items():
    """Test filtering by price."""
    # Rich student
    affordable_rich = get_affordable_items(1000.00)
    assert len(affordable_rich) > 10  # Should afford many items
    
    # Poor student
    affordable_poor = get_affordable_items(50.00)
    assert len(affordable_poor) > 0
    assert all(item["price"] <= 50.00 for item in affordable_poor)
    
    # Broke student
    affordable_broke = get_affordable_items(10.00)
    assert len(affordable_broke) == 0 or all(item["price"] <= 10.00 for item in affordable_broke)

def test_purchase_item_success():
    """Test successful purchase."""
    result = purchase_item(player_balance=500.00, item_id="movie_ticket")
    
    assert result["success"] is True
    assert result["new_balance"] == 485.00  # 500 - 15
    assert "effects" in result
    assert "morale" in result["effects"]

def test_purchase_item_insufficient_funds():
    """Test purchase with insufficient funds."""
    result = purchase_item(player_balance=10.00, item_id="laptop")
    
    assert result["success"] is False
    assert "Not enough money" in result["message"]

def test_purchase_item_not_found():
    """Test purchase of non-existent item."""
    result = purchase_item(player_balance=100.00, item_id="fake_item")
    
    assert result["success"] is False
    assert "not found" in result["message"].lower()

def test_effects_are_meaningful():
    """Test that items have meaningful stat effects."""
    # Movie should boost morale
    movie = get_store_item("movie_ticket")
    assert movie["effects"].get("morale", 0) > 0
    
    # Laptop should boost study efficiency
    laptop = get_store_item("laptop")
    assert laptop["effects"].get("study_efficiency", 0) > 0
    
    # Gym should boost health and reduce stress
    gym = get_store_item("gym_membership")
    assert gym["effects"].get("health", 0) > 0
    assert gym["effects"].get("stress", 0) < 0  # Negative stress = good
    
    # Phone should increase anxiety (realistic!)
    phone = get_store_item("smartphone")
    assert phone["effects"].get("anxiety", 0) > 0

def test_negative_effects_present():
    """Test that some items have realistic negative effects."""
    # Fast food should hurt health
    fast_food = get_store_item("fast_food")
    assert fast_food["effects"].get("health", 0) < 0
    
    # Gaming console should hurt focus
    console = get_store_item("gaming_console")
    assert console["effects"].get("focus", 0) < 0
    
    # Bar night should have multiple negative effects
    bar = get_store_item("bar_night")
    assert bar["effects"].get("health", 0) < 0

def test_education_items_exist():
    """Test that educational items are available."""
    tutoring = get_store_item("tutoring")
    assert tutoring is not None
    assert tutoring["effects"].get("grades", 0) > 0
    
    textbooks = get_store_item("textbooks_used")
    assert textbooks is not None
    
    online_course = get_store_item("online_course")
    assert online_course is not None
    assert online_course["effects"].get("tech_skills", 0) > 0

def test_social_items_boost_social_stat():
    """Test that social items actually boost social stats."""
    dance = get_store_item("dance_class")
    assert dance["effects"].get("social", 0) > 0
    
    concert = get_store_item("concert_ticket")
    assert concert["effects"].get("social", 0) > 0
    
    club = get_store_item("club_membership")
    assert club["effects"].get("social", 0) > 0

def test_health_items_reduce_stress():
    """Test that health items help with stress."""
    yoga = get_store_item("yoga_class")
    assert yoga["effects"].get("stress", 0) < 0  # Reduces stress
    
    therapy = get_store_item("therapy_session")
    assert therapy["effects"].get("stress", 0) < 0
    assert therapy["effects"].get("anxiety", 0) < 0

def test_calculate_monthly_expenses():
    """Test monthly expense calculation."""
    # No subscriptions
    assert calculate_monthly_expenses([]) == 0.0
    
    # One subscription
    monthly = calculate_monthly_expenses(["gym_membership"])
    assert monthly == 40.00
    
    # Multiple subscriptions
    monthly_multi = calculate_monthly_expenses([
        "gym_membership",
        "streaming_subscription",
        "car_payment"
    ])
    assert monthly_multi == 40.00 + 15.00 + 350.00  # $405 total

def test_price_ranges_realistic():
    """Test that prices are in realistic ranges."""
    # Cheap items (under $20)
    cheap_items = [item for item in STORE_ITEMS.values() if item["price"] < 20]
    assert len(cheap_items) >= 3
    
    # Mid-range items ($20-$100)
    mid_items = [item for item in STORE_ITEMS.values() if 20 <= item["price"] <= 100]
    assert len(mid_items) >= 8
    
    # Expensive items (over $200)
    expensive_items = [item for item in STORE_ITEMS.values() if item["price"] > 200]
    assert len(expensive_items) >= 5

def test_warnings_present():
    """Test that items have educational warnings."""
    # Check that most items have warnings
    items_with_warnings = [item for item in STORE_ITEMS.values() if "warning" in item]
    assert len(items_with_warnings) >= len(STORE_ITEMS) * 0.7  # At least 70%

def test_smart_recommendations_high_stress():
    """Test recommendations for high stress."""
    player_stats = {"stress": 80, "gpa": 3.0, "social": 50}
    recommendations = get_smart_recommendations(500.00, player_stats)
    
    # Should recommend stress relief
    rec_ids = [r["item_id"] for r in recommendations]
    assert "yoga_class" in rec_ids or "gym_membership" in rec_ids

def test_smart_recommendations_low_gpa():
    """Test recommendations for struggling students."""
    player_stats = {"stress": 40, "gpa": 2.2, "social": 50}
    recommendations = get_smart_recommendations(500.00, player_stats)
    
    # Should recommend tutoring
    rec_ids = [r["item_id"] for r in recommendations]
    assert "tutoring" in rec_ids

def test_smart_recommendations_isolated():
    """Test recommendations for socially isolated students."""
    player_stats = {"stress": 40, "gpa": 3.0, "social": 20}
    recommendations = get_smart_recommendations(500.00, player_stats)
    
    # Should recommend social activities
    rec_ids = [r["item_id"] for r in recommendations]
    assert "club_membership" in rec_ids or "dance_class" in rec_ids

def test_repeatable_vs_onetime():
    """Test that items correctly mark repeatability."""
    # One-time purchases
    laptop = get_store_item("laptop")
    assert laptop["repeatable"] is False
    
    phone = get_store_item("smartphone")
    assert phone["repeatable"] is False
    
    # Repeatable purchases
    movie = get_store_item("movie_ticket")
    assert movie["repeatable"] is True
    
    restaurant = get_store_item("restaurant_nice")
    assert restaurant["repeatable"] is True

def test_get_all_items():
    """Test getting all items."""
    all_items = get_all_items()
    assert len(all_items) == len(STORE_ITEMS)
    assert all_items == STORE_ITEMS

def test_get_item_count():
    """Test item count."""
    count = get_item_count()
    assert count == len(STORE_ITEMS)
    assert count >= 25

def test_expensive_items_have_warnings():
    """Test that expensive items have strong warnings."""
    expensive_items = [item for item in STORE_ITEMS.values() if item["price"] > 300]
    
    for item in expensive_items:
        assert "warning" in item, f"Expensive item {item['id']} should have warning"

def test_technology_items():
    """Test that tech items boost productivity/efficiency."""
    laptop = get_store_item("laptop")
    assert laptop["effects"].get("study_efficiency", 0) > 0 or laptop["effects"].get("productivity", 0) > 0
    
    headphones = get_store_item("noise_canceling_headphones")
    assert headphones["effects"].get("focus", 0) > 0

def test_food_items_variety():
    """Test variety in food options."""
    food_items = get_items_by_category(StoreCategory.FOOD)
    
    # Should have healthy and unhealthy options
    prices = [item["price"] for item in food_items]
    assert min(prices) < 20  # Cheap option
    assert max(prices) > 40  # Nice option

def test_balanced_effects():
    """Test that items have balanced effects (not all positive)."""
    # Count items with any negative effects
    items_with_negatives = []
    for item in STORE_ITEMS.values():
        has_negative = any(v < 0 for v in item["effects"].values())
        if has_negative:
            items_with_negatives.append(item)
    
    # At least 20% of items should have some negative effect (realistic!)
    assert len(items_with_negatives) >= len(STORE_ITEMS) * 0.2

def test_entertainment_vs_education_tradeoff():
    """Test that entertainment and education have different effects."""
    video_game = get_store_item("video_game")
    tutoring = get_store_item("tutoring")
    
    # Gaming should hurt focus/study
    assert video_game["effects"].get("focus", 0) < 0 or video_game["effects"].get("social", 0) < 0
    
    # Tutoring should help grades
    assert tutoring["effects"].get("grades", 0) > 0
