# Life Readiness Score System

## Overview

The Life Readiness Score is a comprehensive analytics system that evaluates a player's preparedness for post-graduation life challenges based on their mini-game performance across five skill domains:

1. **💰 Finance** (30% weight) - Money management, budgeting, investing, debt
2. **👥 Leadership** (25% weight) - Management, communication, team dynamics
3. **⚙️ Technical** (20% weight) - Domain-specific hard skills (coding, accounting, engineering)
4. **🧠 Critical Thinking** (20% weight) - Problem solving, decision making, analysis
5. **⚖️ Ethics** (5% weight) - Ethical reasoning, stakeholder awareness, social responsibility

## Architecture

### Backend (`analytics/readiness_score.py`)

**Core Function**: `calculate_life_readiness_score(player: Player) -> LifeReadinessScore`

**Scoring Algorithm**:
1. **Domain Grouping**: Maps game types to skill domains via `GAME_TYPE_TO_DOMAINS`
2. **Recency Weighting**: Recent games weighted more heavily (exponential decay: 0.5x → 1.0x)
3. **Consistency Adjustment**: High variance penalized up to 10% (rewards consistent performance)
4. **Volume Bonus**: 10+ games in a domain = 5% bonus (encourages thorough practice)
5. **Trend Detection**: Compares first 3 vs last 3 games to identify improvement/decline

**Readiness Levels**:
- **🏆 Expert** (85-100): Exceptional mastery across domains
- **✅ Proficient** (70-84): Career-ready, strong foundational skills
- **📈 Developing** (50-69): Building competence, needs more practice
- **🌱 Beginner** (0-49): Early stage, significant growth needed

**Career Impact**:
- Score < 50: 0.85x - 1.0x salary multiplier (reduced earning potential)
- Score 50-70: 1.0x salary multiplier (baseline)
- Score 70+: 1.0x - 1.2x salary multiplier (enhanced earning potential)

### API Endpoint

**GET** `/api/curriculum/analytics/{player_id}`

**Response**:
```json
{
  "player_id": "abc123",
  "player_name": "Alex Student",
  "semester": 3,
  "analytics": {
    "overall_score": 81.1,
    "domains": [
      {
        "domain": "finance",
        "score": 80.3,
        "games_completed": 2,
        "recent_performance": 80.3,
        "trend": "stable"
      },
      ...
    ],
    "total_games_completed": 5,
    "average_game_score": 83.6,
    "readiness_level": "proficient",
    "strengths": ["technical", "leadership"],
    "areas_for_growth": ["finance", "critical_thinking"],
    "career_ready": true,
    "career_salary_impact": 1.11,
    "recommended_next_games": ["Practice more finance challenges"]
  }
}
```

### Frontend Component (`LifeReadinessPanel.tsx`)

**Features**:
- **Overall Score Display**: Large circular score indicator with color-coded readiness level
- **Domain Breakdown**: Progress bars for each skill domain with trend indicators
- **Strengths & Growth Areas**: Visual insights into top/bottom performing domains
- **Career Readiness Status**: Clear indicator of whether player meets 70% career threshold
- **Salary Impact Indicator**: Shows how readiness translates to earning potential
- **Recommendations**: Suggests domains needing practice

**Visual Design**:
- Purple gradient background with glassmorphism effects
- Color-coded scores (green 85+, blue 70+, orange 50+, red <50)
- Animated progress bars
- Responsive grid layout

## Integration Points

### GameBoard.tsx
- New "📊 Analytics" tab in main navigation
- Renders `<LifeReadinessPanel playerId={player.id} />` when tab selected
- Panel updates in real-time as player completes more games

### Game Type Mapping

Games contribute to domains based on their type:

**Finance Domain**:
- `BUDGET_CHALLENGE`, `CALCULATOR`, `CASH_FLOW`, `PROFIT_LOSS`
- `ACCOUNTING_BALANCE` (also technical)
- `MARKET_SIM` (also critical thinking)

**Leadership Domain**:
- `TEAM_BUILDER`, `NEGOTIATION`, `SCENARIO_DECISION`
- `MARKETING_CAMPAIGN` (also critical thinking)

**Technical Domain**:
- `CODE_DEBUG`, `CODE_TRACE`, `CODE_BUILDER`, `DATA_STRUCTURE_VIZ`
- `CIRCUIT_SIM`, `PHYSICS_LAB`, `FORCE_DIAGRAM`, `CAD_BUILDER`
- `ALGORITHM_RACE`, `SYSTEM_DESIGN` (also critical thinking)

**Critical Thinking Domain**:
- `CASE_STUDY` (also ethics)
- `DESIGN_CHALLENGE` (also technical)
- Cross-cutting: `NEGOTIATION`, `SCENARIO_DECISION`, `MARKET_SIM`, etc.

**Ethics Domain**:
- `CASE_STUDY` (stakeholder scenarios)
- `BOSS_BATTLE`, `REAL_WORLD_PROJECT` (comprehensive)

**Boss Battles & Special Games**:
- `BOSS_BATTLE`: Contributes to ALL domains
- `REAL_WORLD_PROJECT`: All domains except ethics
- `TIMED_CHALLENGE`: Technical only

## Usage Flow

1. **Player completes mini-games** → Results stored in `player.completed_games` list
2. **Player opens Analytics tab** → Frontend calls `/curriculum/analytics/{player_id}`
3. **Backend calculates scores** → Analyzes `completed_games` history
4. **Frontend displays dashboard** → Shows overall score, domain breakdowns, insights

## Future Enhancements

### Planned Features (V2):
- **Historical Trend Chart**: Line graph showing readiness score over time
- **Peer Comparison**: Anonymous percentile ranking vs other players
- **Achievement Badges**: Unlock badges for domain mastery milestones
- **Personalized Game Recommendations**: Smart suggestions based on weak domains
- **Career Path Alignment**: Show how readiness matches specific career trajectories
- **Skill Gap Analysis**: Compare current skills to job requirements

### Potential Improvements:
- Add temporal decay (old games count less toward current readiness)
- Weight boss battles more heavily (comprehensive assessment)
- Add domain-specific achievement tracking
- Create mini-challenges to quickly boost weak domains
- Add shareable readiness report for resume/LinkedIn

## Testing

### Backend Test:
```bash
cd /path/to/Life_Sprint
.venv/bin/python -c "
from analytics.readiness_score import calculate_life_readiness_score
from core_domain.player.player_model import Player
# ... create test player with completed_games ...
analytics = calculate_life_readiness_score(player)
print(f'Score: {analytics.overall_score}')
"
```

### API Test:
```bash
# Assuming player_id exists in STORE
curl http://localhost:8000/api/curriculum/analytics/{player_id}
```

### Frontend Test:
1. Start frontend: `cd life-sprint-frontend && npm run dev`
2. Login with player who has completed games
3. Click "📊 Analytics" tab
4. Verify score calculation and domain displays

## Technical Notes

### Performance:
- Calculation is O(n*m) where n = completed games, m = domains
- For typical players (< 100 games), calculation completes in < 10ms
- No database queries needed (uses in-memory `player.completed_games`)

### Data Dependencies:
- Requires `player.completed_games` list with: `game_id`, `game_type`, `score_percent`, `completed_at`
- Game types must match entries in `academics.course_games.GameType` enum
- Domain mapping defined in `GAME_TYPE_TO_DOMAINS` constant

### Edge Cases Handled:
- Empty `completed_games` → Returns 0 scores, beginner level, empty recommendations
- Unknown game types → Skipped gracefully in domain calculations
- Single domain with games → Still calculates overall score with available data
- Missing or malformed game data → Filtered out without crashing

## Integration Checklist

✅ Backend analytics module created (`analytics/readiness_score.py`)  
✅ Domain mapping defined for all game types  
✅ API endpoint added (`GET /curriculum/analytics/{player_id}`)  
✅ TypeScript types added to `api.ts`  
✅ Frontend component created (`LifeReadinessPanel.tsx`)  
✅ Analytics tab integrated into GameBoard navigation  
✅ Backend calculation tested with sample data  
✅ All files compile without errors  

## Files Modified/Created

### New Files:
- `analytics/__init__.py` - Package marker
- `analytics/readiness_score.py` - Score calculation engine (218 lines)
- `life-sprint-frontend/src/components/LifeReadinessPanel.tsx` - UI component (328 lines)

### Modified Files:
- `api/router_curriculum.py` - Added `/analytics/{player_id}` endpoint
- `life-sprint-frontend/src/utils/api.ts` - Added types and API function
- `life-sprint-frontend/src/components/GameBoard.tsx` - Added Analytics tab

## Key Formulas

### Weighted Domain Score:
```
score = (Σ(score_i × recency_weight_i)) / Σ(recency_weight_i) × consistency_factor
where:
  recency_weight_i = 0.5 + 0.5 × (i / (n-1))  [0.5 for oldest, 1.0 for newest]
  consistency_factor = max(0.9, 1.0 - std_dev/200)  [max 10% penalty]
```

### Overall Readiness Score:
```
overall = (0.30×finance + 0.25×leadership + 0.20×technical + 0.20×critical + 0.05×ethics)
```

### Career Salary Impact:
```
if score < 50:  multiplier = 0.85 + (score/50) × 0.15     [0.85 - 1.0]
if 50 ≤ score < 70:  multiplier = 1.0                      [baseline]
if score ≥ 70:  multiplier = 1.0 + ((score-70)/20) × 0.2  [1.0 - 1.2]
```

## Related Systems

- **Mini-Game System** (`academics/course_games.py`) - Source of game completion data
- **Career Consequences** (`api/router_curriculum.py`) - Uses similar domain concepts
- **Player Progression** (`core_domain/player/player_model.py`) - Stores completion history
- **Stats System** (`core_domain/stats/stats_model.py`) - Life impact calculations

---

**Status**: ✅ COMPLETE - Feature #8 fully implemented and validated  
**Version**: 1.0  
**Last Updated**: 2026-02-28
