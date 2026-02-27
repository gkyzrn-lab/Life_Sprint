#!/usr/bin/env python3
"""
Life Purchases Store - Demo & Test Script
Shows how the store system works with responsive money spending
"""

from core_domain.store import STORE
from core_domain.player.player_model import Player, Housing, Job
from core_domain.stats.stats_model import Stats
from core_domain.finance.finance_models import Finance
from core_domain.health.health_models import Health
from core_domain.career.career_models import Career
from core_domain.housing.housing_models import HousingMarketState
from store.purchase_service import (
    make_purchase,
    get_player_purchase_history,
    suggest_purchases_for_player,
)
from catalogs.life_purchases import get_available_purchases, LIFE_PURCHASES


def create_test_player(balance=5000.0):
    """Create a test player with some money"""
    player = Player(
        id="test_player_1",
        name="Test Student",
        age=18,
        hs_gpa=3.5,
        parent_income=75000,
        major_id="cs",
        college_id="mit",
        semester=1,
        year_in_school=1,
        stats=Stats(),
        finance=Finance(balance=balance),
        health=Health(),
        career=Career(),
        housing_market=HousingMarketState(),
        housing=Housing(
            option_id="dorm",
            name="Dorm",
            monthly_cost=1000.0,
        ),
    )
    return player


def demo_1_list_purchases():
    """Demo 1: Show available purchases"""
    print("\n" + "="*60)
    print("DEMO 1: Available Purchases in Semester 1")
    print("="*60)
    
    player = create_test_player(5000)
    available = get_available_purchases(player.semester)
    
    print(f"\nAvailable items for semester {player.semester}:")
    print(f"Player balance: ${player.finance.balance:.2f}\n")
    
    for purchase in available:
        affordable = "✅ Can afford" if player.finance.balance >= purchase.cost else "❌ Too expensive"
        print(f"{purchase.emoji} {purchase.name:30s} ${purchase.cost:8.2f}  {affordable}")
        
        # Show effects
        for effect in purchase.effects:
            print(f"    → {effect.stat_name}: {effect.change:+.1f}")


def demo_2_make_purchase():
    """Demo 2: Make a purchase and see effects"""
    print("\n" + "="*60)
    print("DEMO 2: Making a Purchase & Effects")
    print("="*60)
    
    player = create_test_player(5000)
    STORE.put_player(player)
    
    print(f"\nInitial state:")
    print(f"  Balance: ${player.finance.balance:.2f}")
    print(f"  Stress: {player.stats.stress:.0f}")
    print(f"  Happiness: {player.stats.happiness:.0f}")
    print(f"  Mental health: {player.health.mental_health:.0f}")
    
    # Make a purchase
    print(f"\n→ Purchasing: Spa Day ($150)")
    result = make_purchase(player, "spa_day")
    
    if result.success:
        STORE.put_player(player)  # Save changes
        print(f"\n✅ Purchase successful!")
        print(f"\nEffects applied:")
        for stat, change in result.effects_applied.items():
            print(f"  {stat}: {change:+.1f}")
        
        print(f"\nFinal state:")
        print(f"  Balance: ${player.finance.balance:.2f} (was ${result.balance_before:.2f})")
        print(f"  Stress: {player.stats.stress:.0f} (reduced by {abs(result.effects_applied.get('stress', 0)):.0f})")
        print(f"  Happiness: {player.stats.happiness:.0f} (increased by {result.effects_applied.get('happiness', 0):.0f})")
        print(f"  Mental health: {player.health.mental_health:.0f}")
    else:
        print(f"\n❌ Purchase failed: {result.message}")


def demo_3_budget_constraints():
    """Demo 3: Show budget constraints matter"""
    print("\n" + "="*60)
    print("DEMO 3: Budget Constraints & Decisions")
    print("="*60)
    
    player = create_test_player(200)  # Limited budget
    STORE.put_player(player)
    
    print(f"\nPlayer has ${player.finance.balance:.2f} (limited budget)")
    print(f"Stress level: {player.stats.stress:.0f} (very stressed)")
    print(f"Happiness: {player.stats.happiness:.0f} (unhappy)")
    
    # Try expensive purchase
    print(f"\n→ Try to buy Therapy Sessions ($300)...")
    result = make_purchase(player, "therapy_sessions")
    if not result.success:
        print(f"❌ {result.message}")
    
    # Try affordable purchase
    print(f"\n→ Try to buy Coffee with Friends ($15)...")
    result = make_purchase(player, "coffee_with_friends")
    if result.success:
        STORE.put_player(player)
        print(f"✅ Successful!")
        print(f"  Balance: ${player.finance.balance:.2f}")
        print(f"  Stress: {player.stats.stress:.0f}")
        print(f"  Happiness: {player.stats.happiness:.0f}")


def demo_4_purchase_limits():
    """Demo 4: Max per semester limits"""
    print("\n" + "="*60)
    print("DEMO 4: Purchase Limits (Max Per Semester)")
    print("="*60)
    
    player = create_test_player(10000)  # Lots of money
    STORE.put_player(player)
    
    purchase_id = "coffee_with_friends"  # Max 4 per semester
    purchase = LIFE_PURCHASES[purchase_id]
    
    print(f"\nItem: {purchase.name} (max {purchase.max_per_semester} per semester)")
    print(f"Balance: ${player.finance.balance:.2f}\n")
    
    # Buy 4 times
    for i in range(5):
        print(f"Purchase attempt {i+1}...")
        result = make_purchase(player, purchase_id)
        if result.success:
            STORE.put_player(player)
            print(f"  ✅ Bought! Balance: ${player.finance.balance:.2f}")
        else:
            print(f"  ❌ {result.message}")


def demo_5_smart_suggestions():
    """Demo 5: Smart purchase suggestions based on stats"""
    print("\n" + "="*60)
    print("DEMO 5: Smart Suggestions Based on Stats")
    print("="*60)
    
    player = create_test_player(5000)
    
    # Make player very stressed
    player.stats.stress = 90
    player.stats.happiness = 20
    player.health.fitness = 30
    
    print(f"\nPlayer state:")
    print(f"  Stress: {player.stats.stress:.0f} (very high) 😰")
    print(f"  Happiness: {player.stats.happiness:.0f} (very low) 😞")
    print(f"  Fitness: {player.health.fitness:.0f} (very low) 💪")
    
    print(f"\n→ Getting smart suggestions...")
    suggestions = suggest_purchases_for_player(player)
    
    print(f"\n{len(suggestions)} suggestions:")
    for purchase, reason in suggestions:
        print(f"\n{purchase.emoji} {purchase.name:30s} ${purchase.cost:8.2f}")
        print(f"   Reason: {reason}")


def demo_6_semester_progression():
    """Demo 6: Items unlock in later semesters"""
    print("\n" + "="*60)
    print("DEMO 6: Semester-Based Unlocking")
    print("="*60)
    
    for semester in [1, 2, 3, 4]:
        available = get_available_purchases(semester)
        print(f"\nSemester {semester}: {len(available)} items available")
        
        # Show some key items
        car_available = any(p.purchase_id == "used_car" for p in available)
        vacation_available = any(p.purchase_id == "vacation" for p in available)
        
        status = "✅ Available" if car_available else "❌ Not yet"
        print(f"  Used Car ($8000): {status}")
        
        status = "✅ Available" if vacation_available else "❌ Not yet"
        print(f"  Vacation ($600): {status}")


def demo_7_purchase_history():
    """Demo 7: Purchase history tracking"""
    print("\n" + "="*60)
    print("DEMO 7: Purchase History Tracking")
    print("="*60)
    
    player = create_test_player(5000)
    STORE.put_player(player)
    
    # Make several purchases
    purchases_to_make = ["coffee_with_friends", "gym_membership", "movie_night"]
    
    print(f"\nMaking purchases...\n")
    for purchase_id in purchases_to_make:
        result = make_purchase(player, purchase_id)
        if result.success:
            STORE.put_player(player)
            print(f"✅ {result.purchase.name}: ${result.purchase.cost:.2f}")
    
    # Show history
    print(f"\n→ Purchase history:")
    history = get_player_purchase_history(player)
    
    for i, event in enumerate(history, 1):
        print(f"\n{i}. {event.details.get('purchase_name')}")
        print(f"   Semester: {event.semester}")
        print(f"   Cost: ${event.details.get('cost', 0):.2f}")
        print(f"   Balance after: ${event.details.get('balance_after', 0):.2f}")


def main():
    """Run all demos"""
    print("\n" + "🎮 " * 20)
    print("LIFE SPRINT: STORE SYSTEM DEMO")
    print("🎮 " * 20)
    
    demo_1_list_purchases()
    demo_2_make_purchase()
    demo_3_budget_constraints()
    demo_4_purchase_limits()
    demo_5_smart_suggestions()
    demo_6_semester_progression()
    demo_7_purchase_history()
    
    print("\n" + "="*60)
    print("✅ DEMOS COMPLETE")
    print("="*60)
    print("\n📚 Key Features:")
    print("  ✓ 18 realistic items across 6 categories")
    print("  ✓ Budget constraints force strategic decisions")
    print("  ✓ Purchase limits prevent spamming")
    print("  ✓ Semester unlocking creates progression")
    print("  ✓ Smart suggestions based on player stats")
    print("  ✓ Full purchase history tracking")
    print("  ✓ Responsive money spending tied to wellbeing")
    print()


if __name__ == "__main__":
    main()
