"""
Visual demonstration of all 3 analytics improvements with rich output
"""

from core_domain.store import STORE
from core_domain.player.player_model import Player
from core_domain.stats.stats_model import Stats
from core_domain.finance.finance_models import Finance
from catalogs.housing import HOUSING_OPTIONS

from analytics.readiness_score import calculate_life_readiness_score
from analytics.achievement_badges import BADGES_BY_ID

# Create player with progression over 2 semesters
player = Player(
    id="visual_demo",
    name="Sarah Chen",
    age=19,
    hs_gpa=3.7,
    parent_income=75000,
    major_id="ba",
    college_id="cuny_baruch",
    semester=3,
    year_in_school=2,
    stats=Stats(),
    finance=Finance(balance=4500.0),
    housing=HOUSING_OPTIONS["dorm"],
    job=None,
    plan=None,
    completed_games=[
        # Semester 1: Starting out (6 games)
        {"game_id": "ba101_intro", "game_type": "scenario_decision", "score_percent": 72, "completed_at": 1},
        {"game_id": "ba101_team", "game_type": "team_builder", "score_percent": 68, "completed_at": 2},
        {"game_id": "ba101_budget", "game_type": "budget_challenge", "score_percent": 75, "completed_at": 3},
        {"game_id": "ba102_case", "game_type": "case_study", "score_percent": 70, "completed_at": 4},
        {"game_id": "ba102_market", "game_type": "market_sim", "score_percent": 73, "completed_at": 5},
        {"game_id": "ba102_accounting", "game_type": "accounting_balance", "score_percent": 65, "completed_at": 6},
        
        # Semester 2: Improving (7 games)
        {"game_id": "ba201_budget", "game_type": "budget_challenge", "score_percent": 82, "completed_at": 7},
        {"game_id": "ba201_cash", "game_type": "cash_flow", "score_percent": 85, "completed_at": 8},
        {"game_id": "ba201_team", "game_type": "team_builder", "score_percent": 80, "completed_at": 9},
        {"game_id": "ba202_profit", "game_type": "profit_loss", "score_percent": 88, "completed_at": 10},
        {"game_id": "ba202_negotiation", "game_type": "negotiation", "score_percent": 83, "completed_at": 11},
        {"game_id": "ba202_calc", "game_type": "calculator", "score_percent": 90, "completed_at": 12},
        {"game_id": "ba202_scenario", "game_type": "scenario_decision", "score_percent": 86, "completed_at": 13},
        
        # Semester 3: Mastery (6 games so far)
        {"game_id": "ba301_advanced_budget", "game_type": "budget_challenge", "score_percent": 92, "completed_at": 14},
        {"game_id": "ba301_cash_advanced", "game_type": "cash_flow", "score_percent": 94, "completed_at": 15},
        {"game_id": "ba301_profit_advanced", "game_type": "profit_loss", "score_percent": 91, "completed_at": 16},
        {"game_id": "ba301_team_leadership", "game_type": "team_builder", "score_percent": 88, "completed_at": 17},
        {"game_id": "ba301_negotiation_hard", "game_type": "negotiation", "score_percent": 90, "completed_at": 18},
        {"game_id": "ba301_case_complex", "game_type": "case_study", "score_percent": 93, "completed_at": 19},
    ],
    game_points=1580,
)

# Simulate semester 1 snapshot (stored from previous calculation)
player.readiness_history = [
    {
        "semester": 1,
        "overall_score": 64.3,
        "domains": {"finance": 68.0, "leadership": 62.0, "technical": 60.5, "critical_thinking": 71.0},
        "total_games": 6,
        "timestamp": None,
    },
    {
        "semester": 2,
        "overall_score": 74.8,
        "domains": {"finance": 80.5, "leadership": 74.0, "technical": 68.0, "critical_thinking": 79.5},
        "total_games": 13,
        "timestamp": None,
    }
]

STORE.put_player(player)

# Calculate current analytics
analytics = calculate_life_readiness_score(player)

print("╔" + "═" * 58 + "╗")
print("║" + " " * 12 + "📊 LIFE READINESS ANALYTICS DEMO" + " " * 13 + "║")
print("╚" + "═" * 58 + "╝")

print(f"\n👤 Player: {player.name}")
print(f"🎓 Semester: {player.semester} ({player.current_year_label})")
print(f"🎮 Total Games Played: {analytics.total_games_completed}")

print("\n" + "─" * 60)
print("📈 OVERALL READINESS")
print("─" * 60)

# Visual score bar
score = analytics.overall_score
bar_length = 40
filled = int(score / 100 * bar_length)
bar = "█" * filled + "░" * (bar_length - filled)
color_emoji = "🟢" if score >= 85 else "🔵" if score >= 70 else "🟡" if score >= 50 else "🔴"

print(f"\n{color_emoji} Score: {score}/100 [{bar}]")
print(f"🎯 Level: {analytics.readiness_level.upper()}")
print(f"💼 Career Ready: {'YES ✅' if analytics.career_ready else 'Not yet ⏳'}")
print(f"💰 Salary Impact: {analytics.career_salary_impact}x")

print("\n" + "─" * 60)
print("🎯 DOMAIN BREAKDOWN")
print("─" * 60)

for domain in analytics.domains:
    d_score = domain.score
    d_bar_filled = int(d_score / 100 * 20)
    d_bar = "█" * d_bar_filled + "░" * (20 - d_bar_filled)
    trend_emoji = {"improving": "📈", "stable": "➡️", "declining": "📉"}.get(domain.trend, "➡️")
    
    print(f"\n{domain.domain.replace('_', ' ').title()}")
    print(f"  Score: {d_score:.1f}/100 [{d_bar}] {trend_emoji}")
    print(f"  Games: {domain.games_completed} | Recent: {domain.recent_performance:.1f}%")

print("\n" + "─" * 60)
print("🎮 RECOMMENDED NEXT CHALLENGES")
print("─" * 60)

if analytics.recommended_next_games:
    for i, rec in enumerate(analytics.recommended_next_games, 1):
        print(f"\n{i}. 📚 {rec['title']}")
        print(f"   Course: {rec['course_id'].upper()} | {rec['reason']}")
else:
    print("\n🌟 Amazing! All domains are strong - keep it up!")

print("\n" + "─" * 60)
print("🏆 ACHIEVEMENT BADGES")
print("─" * 60)

if analytics.achievement_badges:
    print(f"\n🎖️  Total: {len(analytics.achievement_badges)} badges earned\n")
    
    # Group by category
    by_category = {}
    for badge_id in analytics.achievement_badges:
        badge = BADGES_BY_ID.get(badge_id)
        if badge:
            cat = badge.category
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(badge)
    
    for category, badges in by_category.items():
        print(f"\n{category.replace('_', ' ').title()}:")
        for badge in badges:
            new_marker = " ⭐ NEW!" if badge.id in analytics.newly_earned_badges else ""
            print(f"  {badge.icon} {badge.name}{new_marker}")
            print(f"     {badge.description}")
else:
    print("\n🎯 No badges yet - keep playing to earn your first!")

if analytics.newly_earned_badges:
    print("\n" + "═" * 60)
    print(f"🎉 YOU EARNED {len(analytics.newly_earned_badges)} NEW BADGE{'S' if len(analytics.newly_earned_badges) != 1 else ''}!")
    print("═" * 60)

print("\n" + "─" * 60)
print("📊 HISTORICAL PROGRESS")
print("─" * 60)

if len(player.readiness_history) >= 2:
    print("\nReadiness Score Over Time:\n")
    for snapshot in player.readiness_history:
        sem = snapshot["semester"]
        score = snapshot["overall_score"]
        games = snapshot["total_games"]
        
        # Mini bar chart
        bar_filled = int(score / 100 * 30)
        bar = "█" * bar_filled + "░" * (30 - bar_filled)
        
        print(f"Semester {sem}: {score:5.1f}/100 [{bar}] ({games} games)")
    
    # Calculate improvement
    first = player.readiness_history[0]["overall_score"]
    latest = player.readiness_history[-1]["overall_score"]
    improvement = latest - first
    improvement_emoji = "📈" if improvement > 0 else "📉" if improvement < 0 else "➡️"
    
    print(f"\n{improvement_emoji} Overall Improvement: {improvement:+.1f} points")
    print(f"   From {first:.1f} → {latest:.1f}")
else:
    print("\n⏳ Play more games across semesters to see your progress curve!")

print("\n" + "╔" + "═" * 58 + "╗")
print("║" + " " * 16 + "✅ ALL IMPROVEMENTS LIVE" + " " * 19 + "║")
print("╚" + "═" * 58 + "╝")
