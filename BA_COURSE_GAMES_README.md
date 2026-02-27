# BA Course Enhancement System - Mini-Games & Interactive Learning

## Overview

This system enhances the Business Administration (BA) major with:

1. **Mini-Games for Interactive Learning** - Students play engaging games to understand course concepts
2. **Beautiful Course Topics Display** - Visually formatted topic descriptions with real-world examples
3. **Points & Achievement System** - Students earn points by completing games and achieving high scores

## Features

### 1. Mini-Games (7 Game Types)

Each BA course includes 1-2 mini-games targeting key concepts:

#### Game Types
- **Scenario Decision** - Choose the best business decision in realistic scenarios
- **Accounting Balance** - Puzzle-style balance sheet challenges
- **Market Simulation** - Supply/demand curve interactions
- **Team Builder** - Leadership and team dynamics challenges
- **Case Study** - Analyze business cases and identify solutions
- **Budget Challenge** - Allocate limited resources optimally
- **Negotiation** - Practice business negotiation skills
- **Marketing Campaign** - Create targeted marketing strategies

### 2. Course Coverage

Currently available for all BA semester 1-4 courses:

**Semester 1:**
- ba101 (Intro Business) - 2 games
- ba102 (Accounting Principles) - 2 games
- econ101 (Microeconomics) - 1 game

**Semester 2:**
- ba201 (Business Communication) - 1 game
- econ102 (Macroeconomics) - covered in econ101
- ba202 (Financial Accounting) - 1 game

**Semester 3:**
- ba301 (Management Principles) - 1 game
- ba302 (Marketing Fundamentals) - 1 game
- ba303 (Organizational Behavior) - covered in ba301

**Semester 4:**
- ba401 (Corporate Finance) - 1 game
- ba402 (Strategic Management) - 1 game
- ba403 (Operations Management) - covered in ba402

### 3. Course Topics Display

Each BA course has enhanced topic descriptions with:
- **Topic Name** - Clear, focused topic
- **Description** - Technical definition
- **Real-World Example** - How this applies in actual business
- **Icon** - Visual indicator for quick recognition

Example topics:
- "Business Types & Structures" 🏢
- "The Accounting Equation" ⚖️
- "Supply & Demand" 📦
- "Leadership Styles" 👑
- etc.

## API Endpoints

### Get Course Information
```
GET /curriculum/course/{course_id}
```
Returns course info including mini-games and formatted topics.

**Example Response:**
```json
{
  "id": "ba101",
  "title": "Intro Business",
  "mini_games": [
    {
      "id": "ba101_startup_game",
      "title": "Startup Structure Challenge",
      "description": "You're launching a new tech company. Choose the right business structure...",
      "topic": "Business Types & Structure",
      "game_type": "scenario_decision",
      "estimated_duration_minutes": 10,
      "question_count": 3
    }
  ],
  "formatted_topics": {
    "title": "Intro Business",
    "description": "Foundations of business...",
    "topics": [
      {
        "name": "Business Types & Structures",
        "description": "Sole proprietorships, partnerships, LLCs...",
        "real_world": "Why does Jeff Bezos's Amazon choose to be incorporated?",
        "icon": "🏢"
      }
    ]
  }
}
```

### Get Mini-Games for Course
```
GET /curriculum/games/course/{course_id}
```

Returns list of available games with metadata.

### Get Game Details
```
GET /curriculum/games/{game_id}
```

Returns full game with all questions (without answers to prevent cheating).

### Play Mini-Game
```
POST /curriculum/games/submit
```

Submit answers and receive:
- Score percentage
- Points earned
- Correct/incorrect feedback
- Key learning points

**Request:**
```json
{
  "game_id": "ba101_startup_game",
  "course_id": "ba101",
  "answers": [
    {"question_id": "q1", "selected_option_index": 2},
    {"question_id": "q2", "selected_option_index": 1},
    {"question_id": "q3", "selected_option_index": 1}
  ],
  "time_spent_minutes": 8
}
```

**Response:**
```json
{
  "game_id": "ba101_startup_game",
  "course_id": "ba101",
  "score_percent": 100.0,
  "points_earned": 45,
  "correct_answers": 3,
  "total_questions": 3,
  "passed": true,
  "feedback": [
    {
      "question_id": "q1",
      "is_correct": true,
      "learning_point": "Business structures and liability protection"
    }
  ],
  "key_learnings": ["Business structures and liability protection", ...],
  "total_game_points": 125,
  "message": "🎉 Great job! You scored 100.0% and earned 45 points!"
}
```

## Game Scoring

Each game has configurable scoring:
- **Points per correct answer** - Default: 10-15 points
- **Points for incorrect answer** - Default: -2 points (can be negative)
- **Min passing score** - Default: 70%
- **Time tracking** - Records how long student spent

## Implementation Details

### File Structure
```
academics/
  course_games.py          # Mini-game definitions and logic
  course_service.py        # Enhanced to include games & topics

catalogs/
  ba_course_topics.py      # BA course topic descriptions & formatting

api/
  router_curriculum.py     # API endpoints for games
```

### Course Games Structure
```python
MiniGame(
  id: str                    # Unique game ID
  course_id: str             # Which course
  topic: str                 # What topic it teaches
  game_type: GameType        # Type of game
  title: str                 # Display name
  description: str           # What player will do
  questions: List[GameQuestion]  # 2-5 questions per game
  points_per_correct: int    # Points for correct answer
  min_passing_score: float   # % needed to pass (70%)
)
```

## Frontend Integration

### Display Course with Games
1. Call `GET /curriculum/course/{course_id}`
2. Extract `formatted_topics` for topic display
3. Extract `mini_games` to show available games
4. Display topic cards with real-world examples
5. Show game cards with difficulty, duration, question count

### Play a Game
1. Call `GET /curriculum/games/{game_id}` to load questions
2. Display questions in sequence or all at once
3. Track time spent
4. Call `POST /curriculum/games/submit` with answers
5. Display results with emoji feedback 🎉 or 💡

### Example UI Flow
```
┌─────────────────────────────────────┐
│  Intro Business (ba101)             │
├─────────────────────────────────────┤
│  Description: Foundations of...     │
│  3 Credits | Difficulty: 3/10       │
│                                     │
│  📚 COURSE TOPICS                  │
│  🏢 Business Types & Structures     │
│    → Real-world: Why Amazon Inc?   │
│  👥 Stakeholders & Ethics           │
│    → Real-world: Factory closure?   │
│                                     │
│  🎮 MINI-GAMES (2)                 │
│  ┌─────────────────────────────┐   │
│  │ Startup Structure Challenge │   │
│  │ 3 questions • 10 min • 🟡⚪⚪ │   │
│  │ [PLAY GAME]                 │   │
│  └─────────────────────────────┘   │
│  ┌─────────────────────────────┐   │
│  │ Stakeholder Navigation      │   │
│  │ 2 questions • 8 min • 🟡⚪⚪  │   │
│  │ [PLAY GAME]                 │   │
│  └─────────────────────────────┘   │
│                                     │
│  Your Points: 125 / 200             │
└─────────────────────────────────────┘
```

## Expansion Plan

### Phase 1 (Current)
✅ BA major courses (Semesters 1-4)
✅ Mini-games for key concepts
✅ Real-world examples
✅ Points system

### Phase 2 (Future)
- CS major course games
- Engineering major course games
- Liberal Arts major course games
- More diverse game types
- Leaderboards by course
- Badges for completing games

### Phase 3
- Adaptive difficulty (games adjust based on performance)
- Peer competition challenges
- Collaborative mini-games
- Video explanations of solutions
- Study group integration

## Development Notes

### Adding a New Game
1. Create `MiniGame` instance in `BA_COURSE_GAMES[course_id]`
2. Add 3-5 `GameQuestion` items with correct answers
3. Set `points_per_correct` and `min_passing_score`
4. Test via API endpoint
5. Frontend will auto-discover via `/curriculum/games/course/{course_id}`

### Adding a New Course Topic
1. Add entry to `BA_COURSE_TOPICS` dict in `ba_course_topics.py`
2. Include 5 key topics with descriptions and real-world examples
3. Icons auto-selected based on topic name
4. Display auto-formatted via `format_course_topics_for_display()`

### Testing
```bash
# Test imports
python -c "import academics.course_games; import catalogs.ba_course_topics"

# Get course with games
curl http://localhost:8000/curriculum/course/ba101

# Get games for course
curl http://localhost:8000/curriculum/games/course/ba101

# Load specific game
curl http://localhost:8000/curriculum/games/ba101_startup_game

# Submit game answers
curl -X POST http://localhost:8000/curriculum/games/submit \
  -H "Content-Type: application/json" \
  -d '{
    "game_id": "ba101_startup_game",
    "course_id": "ba101",
    "answers": [{"question_id": "q1", "selected_option_index": 2}],
    "time_spent_minutes": 8
  }'
```

## Design Philosophy

### Educational Value
- Each game teaches specific, testable concepts
- Multiple game types prevent monotony
- Real-world context helps retention
- Immediate feedback reinforces learning

### Engagement
- Gamification with points and feedback
- Visual feedback (emojis, messages)
- Achievable challenges (70% pass rate)
- Progress tracking

### Simplicity
- Each game has 2-5 questions max
- 8-13 minute estimated duration
- Clear scoring rules
- No complex mechanics

## Next Steps for User

To expand this system further:

1. **For CS Major**: Create CS course games following same pattern
2. **For Engineering**: Create Engineering course games
3. **For Liberal Arts**: Create Liberal Arts course games
4. **Enhanced Display**: Update frontend components to show topics beautifully
5. **Analytics**: Track which games students struggle with
6. **Adaptive Difficulty**: Make questions harder after correct answers

The foundation is solid and extensible!
