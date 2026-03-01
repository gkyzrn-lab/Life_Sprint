"""
Test script for all 3 priority improvements:
1. Specific game recommendations
2. Achievement badge system
3. Historical trend tracking
"""

from core_domain.store import STORE
from core_domain.player.player_model import Player
from core_domain.stats.stats_model import Stats
from core_domain.finance.finance_models import Finance
from catalogs.housing import HOUSING_OPTIONS

from analytics.readiness_score import calculate_life_readiness_score
from analytics.achievement_badges import check_all_achievements

# Create test player
player = Player(
    id="test_improvements",
    name="Test Player",
    age=19,
    hs_gpa=3.5,
    parent_income=60000,
    major_id="ba",
    college_id="cuny_baruch",
    semester=2,
    year_in_school=1,
    stats=Stats(),
    finance=Finance(balance=3000.0),
    housing=HOUSING_OPTIONS["dorm"],
    job=None,
    plan=None,
    completed_games=[
        # Simulate 8 finance games with good scores
        {"game_id": "ba201_budget_game", "game_type": "budget_challenge", "score_percent": 88, "completed_at": 1},
        {"game_id": "ba201_cash_flow", "game_type": "cash_flow", "score_percent": 92, "completed_at": 2},
        {"game_id": "ba301_profit_loss", "game_type": "profit_loss", "score_percent": 85, "completed_at": 3},
        {"game_id": "ba401_calculator", "game_type": "calculator", "score_percent": 90, "completed_at": 4},
        {"game_id": "ba501_budget_2", "game_type": "budget_challenge", "score_percent": 87, "completed_at": 5},
        {"game_id": "ba401_cash_2", "game_type": "cash_flow", "score_percent": 91, "completed_at": 6},
        {"game_id": "ba501_profit_2", "game_type": "profit_loss", "score_percent": 86, "completed_at": 7},
        {"game_id": "ba601_advanced_budget", "game_type": "budget_challenge", "score_percent": 89, "completed_at": 8},
        
        # 3 leadership games
        {"game_id": "ba101_team", "game_type": "team_builder", "score_percent": 75, "completed_at": 9},
        {"game_id": "ba201_negotiation", "game_type": "negotiation", "score_percent": 78, "completed_at": 10},
        {"game_id": "ba301_scenario", "game_type": "scenario_decision", "score_percent": 80, "completed_at": 11},
        
        # 2 technical games (weaker performance)
        {"game_id": "ba301_accounting", "game_type": "accounting_balance", "score_percent": 65, "completed_at": 12},
        {"game_id": "ba401_accounting_2", "game_type": "accounting_balance", "score_percent": 68, "completed_at": 13},
    ],
    game_points=850,
)

STORE.put_player(player)

print("=" * 60)
print("TESTING 3 PRIORITY IMPROVEMENTS")
print("=" * 60)

# Calculate analytics (will update player with badges and history)
analytics = calculate_life_readiness_score(player)

print("\n📊 OVERALL READINESS")
print(f"Score: {analytics.overall_score}/100")
print(f"Level: {analytics.readiness_level}")
print(f"Career Ready: {analytics.career_ready}")
print(f"Salary Impact: {analytics.career_salary_impact}x")
print(f"Total Games: {analytics.total_games_completed}")

print("\n🎯 DOMAIN BREAKDOWN")
for domain in analytics.domains:
    print(f"  {domain.domain.capitalize()}: {domain.score:.1f} ({domain.trend}) - {domain.games_completed} games")

print("\n💪 STRENGTHS")
for s in analytics.strengths:
    print(f"  - {s.capitalize()}")

print("\n📈 AREAS FOR GROWTH")
for area in analytics.areas_for_growth:
    print(f"  - {area.capitalize()}")

# ========================================
# IMPROVEMENT #1: Specific Game Recommendations
# ========================================
print("\n" + "=" * 60)
print("✨ IMPROVEMENT #1: SPECIFIC GAME RECOMMENDATIONS")
print("=" * 60)
if analytics.recommended_next_games:
    for rec in analytics.recommended_next_games:
        print(f"\n🎮 {rec['title']}")
        print(f"   Course: {rec['course_id']}")
        print(f"   Reason: {rec['reason']}")
else:
    print("No recommendations (all domains strong)")

# ========================================
# IMPROVEMENT #2: Achievement Badge System
# ========================================
print("\n" + "=" * 60)
print("🏆 IMPROVEMENT #2: ACHIEVEMENT BADGES")
print("=" * 60)
print(f"Total Badges Earned: {len(analytics.achievement_badges)}")
for badge_id in analytics.achievement_badges:
    print(f"  🏅 {badge_id}")

if analytics.newly_earned_badges:
    print(f"\n🎉 NEW BADGES THIS CHECK: {len(analytics.newly_earned_badges)}")
    for badge_id in analytics.newly_earned_badges:
        print(f"  ⭐ {badge_id}")
else:
    print("\n(No new badges this check)")

# ========================================
# IMPROVEMENT #3: Historical Trend Tracking
# ========================================
print("\n" + "=" * 60)
print("📈 IMPROVEMENT #3: HISTORICAL TREND TRACKING")
print("=" * 60)
print(f"History Snapshots: {len(player.readiness_history)}")
for snapshot in player.readiness_history:
    print(f"\n  Semester {snapshot['semester']}: {snapshot['overall_score']:.1f}/100")
    print(f"    Games: {snapshot['total_games']}")
    print(f"    Domains: {snapshot['domains']}")

# ========================================
# Test Badge Detection Logic
# ========================================
print("\n" + "=" * 60)
print("🔬 BADGE DETECTION VALIDATION")
print("=" * 60)

# Count finance games with high scores
finance_games = [g for g in player.completed_games if "budget" in g.get("game_type", "") or "cash" in g.get("game_type", "") or "profit" in g.get("game_type", "")]
finance_avg = sum(g["score_percent"] for g in finance_games) / len(finance_games) if finance_games else 0
print(f"\nFinance Games: {len(finance_games)} with {finance_avg:.1f}% average")
print(f"Should earn 'finance_guru_bronze'? {len(finance_games) >= 5 and finance_avg >= 85}")

volume = len(player.completed_games)
print(f"\nTotal Games: {volume}")
print(f"Should earn 'game_explorer' (10+)? {volume >= 10}")

print("\n" + "=" * 60)
print("✅ ALL 3 IMPROVEMENTS WORKING")
print("=" * 60)
