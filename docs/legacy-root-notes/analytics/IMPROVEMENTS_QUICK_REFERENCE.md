# 🚀 Analytics Improvements - Quick Reference

## For Players

### 📊 Viewing Your Analytics
1. Open Classroom view
2. Click "Analytics" tab
3. See your Life Readiness Score with all improvements

### 🎮 Following Recommendations
Look for "Recommended Practice" section:
- Shows 3-5 specific games matched to your level
- Course ID helps you find the game quickly
- Reason explains why it's recommended

### 🏆 Earning Badges
**Easy Badges (Start Here)**:
- 🎮 Game Explorer: Play 10 games
- 🚀 Career Ready: Reach 70% overall score
- 🌈 Well-Rounded: All domains at 60%+

**Challenge Badges**:
- 💰 Finance Guru (Bronze): 5 finance games @ 85%+
- 📈 Consistent Performer: 10 games in a row @ 70%+
- 🎯 High Achiever: 90% average across all games

**Elite Badges**:
- 👑 Game Legend: Complete 50+ games
- 💫 Domain Master: Any domain at 95+
- 🏅 Elite Candidate: 90%+ overall with all domains 75%+

### 📈 Tracking Progress
Check "Progress History" to see your scores over semesters:
- Green trend 📈 = Improving
- Blue arrow ➡️ = Stable
- Red trend 📉 = Declining

---

## For Developers

### Using Recommendations
```python
from analytics.readiness_score import calculate_life_readiness_score

analytics = calculate_life_readiness_score(player)

for rec in analytics.recommended_next_games:
    print(f"{rec['title']} ({rec['course_id']}) - {rec['reason']}")
```

### Checking Badges
```python
from analytics.achievement_badges import check_all_achievements

result = check_all_achievements(
    completed_games=player.completed_games,
    overall_score=analytics.overall_score,
    domain_scores=analytics.domains,
)

print(f"Badges: {result['badges']}")  # List of Badge objects
print(f"Newly earned: {result['newly_earned']}")
```

### Accessing History
```python
# History is stored on player object
for snapshot in player.readiness_history:
    print(f"Semester {snapshot['semester']}: {snapshot['overall_score']}/100")

# Or from API response
response = get_life_readiness_analytics(player_id)
history = response['readiness_history']
```

### API Endpoint
```bash
GET /curriculum/analytics/{player_id}
```

**Response**:
```json
{
  "player_id": "uuid",
  "player_name": "Alice",
  "semester": 3,
  "analytics": {
    "overall_score": 81.8,
    "recommended_next_games": [
      {
        "game_id": "ba301_budget",
        "title": "Budget Challenge",
        "course_id": "ba301",
        "reason": "Improves finance - Good match"
      }
    ],
    "achievement_badges": ["career_ready", "game_explorer"],
    "newly_earned_badges": ["game_explorer"]
  },
  "readiness_history": [
    {"semester": 1, "overall_score": 64.3, "domains": {...}},
    {"semester": 2, "overall_score": 74.8, "domains": {...}},
    {"semester": 3, "overall_score": 81.8, "domains": {...}}
  ]
}
```

---

## 🎯 Key Algorithms

### Difficulty Match Scoring
```python
# Map question difficulty (1-5) to score range (20-100)
game_difficulty_score = 20 + (avg_difficulty - 1) * 20

# Calculate match quality (peak at +10 points harder)
difficulty_diff = game_difficulty_score - player_domain_score
if -10 <= difficulty_diff <= 20:
    match_quality = 100 - abs(difficulty_diff - 10)
else:
    match_quality = max(0, 100 - abs(difficulty_diff) * 2)
```

### Streak Detection
```python
max_streak = 0
current_streak = 0

for game in completed_games:
    if game["score_percent"] >= threshold:
        current_streak += 1
        max_streak = max(max_streak, current_streak)
    else:
        current_streak = 0
```

### Snapshot Deduplication
```python
should_snapshot = True
if player.readiness_history:
    last = player.readiness_history[-1]
    if (last["semester"] == player.semester and 
        last["total_games"] == total_games):
        should_snapshot = False
```

---

## 🐛 Troubleshooting

### No Recommendations Showing
- Check if player has completed games
- Verify `areas_for_growth` is populated (need score variation)
- Confirm BA_COURSE_GAMES has games for the weak domain

### Badge Not Awarded
- Verify game type strings match GameType enum values
- Check average score calculation (accounting games can lower average)
- Ensure minimum game count met (varies by badge)
- Use [debug_badges.py](debug_badges.py) to trace domain grouping

### History Not Recording
- Check if semester or game count changed
- Verify `readiness_history` field exists on player
- Confirm analytics endpoint saves player with `STORE.put_player()`

---

## 📞 Support

**Files to Check**:
1. Backend logic: [analytics/readiness_score.py](analytics/readiness_score.py)
2. Badge system: [analytics/achievement_badges.py](analytics/achievement_badges.py)
3. Player model: [core_domain/player/player_model.py](core_domain/player/player_model.py)
4. API endpoint: [api/router_curriculum.py](api/router_curriculum.py#L1251-L1276)
5. Frontend UI: [LifeReadinessPanel.tsx](life-sprint-frontend/src/components/LifeReadinessPanel.tsx)

**Test Scripts**:
- Quick test: `python test_improvements.py`
- Visual demo: `python demo_improvements_visual.py`
- Badge debug: `python debug_badges.py`

---

**Version**: 1.0  
**Last Updated**: 2024  
**Status**: ✅ Production Ready
