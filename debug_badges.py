"""Debug badge detection for finance games"""
from analytics.achievement_badges import _check_domain_mastery_badges, GAME_TYPE_TO_DOMAINS, LifeReadinessDomain
from academics.course_games import GameType

# Test data - same as test_improvements.py
completed_games = [
    {"game_id": "ba201_budget_game", "game_type": "budget_challenge", "score_percent": 88},
    {"game_id": "ba201_cash_flow", "game_type": "cash_flow", "score_percent": 92},
    {"game_id": "ba301_profit_loss", "game_type": "profit_loss", "score_percent": 85},
    {"game_id": "ba401_calculator", "game_type": "calculator", "score_percent": 90},
    {"game_id": "ba501_budget_2", "game_type": "budget_challenge", "score_percent": 87},
    {"game_id": "ba401_cash_2", "game_type": "cash_flow", "score_percent": 91},
    {"game_id": "ba501_profit_2", "game_type": "profit_loss", "score_percent": 86},
    {"game_id": "ba601_advanced_budget", "game_type": "budget_challenge", "score_percent": 89},
    {"game_id": "ba101_team", "game_type": "team_builder", "score_percent": 75},
    {"game_id": "ba201_negotiation", "game_type": "negotiation", "score_percent": 78},
    {"game_id": "ba301_scenario", "game_type": "scenario_decision", "score_percent": 80},
    {"game_id": "ba301_accounting", "game_type": "accounting_balance", "score_percent": 65},
    {"game_id": "ba401_accounting_2", "game_type": "accounting_balance", "score_percent": 68},
]

print("Testing badge detection:")
print(f"Total games: {len(completed_games)}")

# Check what domains each game maps to
print("\nGame type -> domain mapping:")
for game in completed_games:
    gt_str = game["game_type"]
    try:
        gt_enum = GameType(gt_str)
        domains = GAME_TYPE_TO_DOMAINS.get(gt_enum, [])
        print(f"  {gt_str}: {domains}")
    except ValueError as e:
        print(f"  {gt_str}: ERROR - {e}")

# Check domain mastery badges
badges = _check_domain_mastery_badges(completed_games)
print(f"\nDomain mastery badges earned: {badges}")

# Manual check: count finance games
finance_games = []
for game in completed_games:
    gt_str = game["game_type"]
    try:
        gt_enum = GameType(gt_str)
        domains = GAME_TYPE_TO_DOMAINS.get(gt_enum, [])
        if "finance" in domains:
            finance_games.append(game)
    except ValueError:
        pass

print(f"\nFinance games found: {len(finance_games)}")
for g in finance_games:
    print(f"  {g['game_type']}: {g['score_percent']}%")

if finance_games:
    avg = sum(g["score_percent"] for g in finance_games) / len(finance_games)
    print(f"Average: {avg:.1f}%")
    print(f"Qualifies for finance_guru_bronze? {len(finance_games) >= 5 and avg >= 85}")
