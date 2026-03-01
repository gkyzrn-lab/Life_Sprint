"""
Test player with enough high-scoring games to earn finance_guru_bronze
"""
from core_domain.store import STORE
from core_domain.player.player_model import Player
from core_domain.stats.stats_model import Stats
from core_domain.finance.finance_models import Finance
from catalogs.housing import HOUSING_OPTIONS

from analytics.readiness_score import calculate_life_readiness_score

# Create test player with 6 high-scoring finance games
player = Player(
    id="test_badges_qualified",
    name="Badge Earner",
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
        # 6 pure finance games with 85%+ scores
        {"game_id": "ba201_budget_1", "game_type": "budget_challenge", "score_percent": 88, "completed_at": 1},
        {"game_id": "ba201_cash_flow_1", "game_type": "cash_flow", "score_percent": 92, "completed_at": 2},
        {"game_id": "ba301_profit_loss_1", "game_type": "profit_loss", "score_percent": 85, "completed_at": 3},
        {"game_id": "ba501_budget_2", "game_type": "budget_challenge", "score_percent": 87, "completed_at": 4},
        {"game_id": "ba401_cash_2", "game_type": "cash_flow", "score_percent": 91, "completed_at": 5},
        {"game_id": "ba601_advanced_budget", "game_type": "budget_challenge", "score_percent": 89, "completed_at": 6},
        
        # 5 leadership games to trigger leader_bronze
        {"game_id": "ba101_team_1", "game_type": "team_builder", "score_percent": 86, "completed_at": 7},
        {"game_id": "ba201_team_2", "game_type": "team_builder", "score_percent": 88, "completed_at": 8},
        {"game_id": "ba201_negotiation", "game_type": "negotiation", "score_percent": 87, "completed_at": 9},
        {"game_id": "ba301_scenario", "game_type": "scenario_decision", "score_percent": 85, "completed_at": 10},
        {"game_id": "ba401_team_3", "game_type": "team_builder", "score_percent": 89, "completed_at": 11},
        
        # 1 more for 12 total (trigger game_explorer and consistent_performer)
        {"game_id": "ba301_case", "game_type": "case_study", "score_percent": 90, "completed_at": 12},
    ],
    game_points=1200,
)

STORE.put_player(player)

analytics = calculate_life_readiness_score(player)

print("=" * 60)
print("BADGE QUALIFICATION TEST")
print("=" * 60)
print(f"\nOverall Score: {analytics.overall_score}/100")
print(f"Total Games: {analytics.total_games_completed}")

print("\n🏆 BADGES EARNED:")
for badge_id in sorted(analytics.achievement_badges):
    print(f"  ✅ {badge_id}")

# Validate expected badges
expected_badges = {"finance_guru_bronze", "leader_bronze", "game_explorer", "career_ready", "well_rounded"}
actual_badges = set(analytics.achievement_badges)

print("\n🔍 BADGE VALIDATION:")
for expected in expected_badges:
    status = "✅" if expected in actual_badges else "❌"
    print(f"  {status} {expected}")

missing = expected_badges - actual_badges
extra = actual_badges - expected_badges

if missing:
    print(f"\n⚠️  Missing expected badges: {missing}")
if extra:
    print(f"\n🎁 Extra badges earned: {extra}")

if not missing:
    print("\n🎉 ALL EXPECTED BADGES AWARDED CORRECTLY!")
