# Quick Start: Games & Exam Feedback Examples

## Example 1: Get a Game for a Lesson

```bash
curl http://localhost:8000/curriculum/lessons/lesson_1/game | jq
```

**Response:**
```json
{
  "game_id": "game_cs101_01",
  "lesson_id": "lesson_1",
  "title": "Variable Type Guess",
  "game_type": "interactive",
  "description": "Identify the correct data type for different values...",
  "objectives": [
    "Understand different data types",
    "Recognize how to categorize values",
    "Learn type syntax in Python"
  ],
  "difficulty": "beginner",
  "estimated_duration_minutes": 5,
  "content": {
    "rounds": [
      {
        "value": "42",
        "correct_type": "integer",
        "explanation": "42 is a whole number with no decimal point"
      },
      ...
    ],
    "type_options": ["integer", "string", "float", "boolean"],
    "points_per_correct": 10
  }
}
```

---

## Example 2: Get All Games in a Course

```bash
curl http://localhost:8000/curriculum/courses/cs101/games | jq
```

**Response:**
```json
{
  "course_id": "cs101",
  "total_games": 5,
  "games": [
    {
      "game_id": "game_cs101_01",
      "lesson_id": "lesson_1",
      "title": "Variable Type Guess",
      "game_type": "interactive",
      "description": "Identify the correct data type for different values...",
      "difficulty": "beginner",
      "estimated_duration_minutes": 5
    },
    {
      "game_id": "game_cs101_02",
      "lesson_id": "lesson_2",
      "title": "Decision Tree Builder",
      "game_type": "puzzle",
      "description": "Build decision logic by arranging if/elif/else conditions...",
      "difficulty": "beginner",
      "estimated_duration_minutes": 7
    },
    ...
  ]
}
```

---

## Example 3: Submit Game Results

```bash
curl -X POST http://localhost:8000/curriculum/lessons/lesson_1/game/submit \
  -H "Content-Type: application/json" \
  -d '{
    "score": 45,
    "max_score": 50
  }' | jq
```

**Response:**
```json
{
  "game_id": "game_cs101_01",
  "lesson_id": "lesson_1",
  "score": 45,
  "max_score": 50,
  "percentage": 90.0,
  "passed": true,
  "message": "Game completed!",
  "objectives_covered": [
    "Understand different data types",
    "Recognize how to categorize values",
    "Learn type syntax in Python"
  ],
  "next_lesson": null
}
```

---

## Example 4: Exam Submission - Failed (Shows Correct Answers)

```bash
curl -X POST http://localhost:8000/exams/submit \
  -H "Content-Type: application/json" \
  -d '{
    "player_id": "player-uuid-here",
    "semester": 1,
    "answers": [
      {"question_id": "cs_s1_q1", "chosen_choice_id": "b"},
      {"question_id": "cs_s1_q2", "chosen_choice_id": "c"},
      {"question_id": "cs_s1_q3", "chosen_choice_id": "b"}
    ]
  }' | jq '.exam_result, .passed, .message, .feedback'
```

**Response (showing only relevant fields):**
```json
{
  "exam_result": {
    "correct_count": 1,
    "total_questions": 3,
    "score_percent": 33.33333333333333
  },
  "passed": false,
  "message": "You scored 33.3%. Review the correct answers below and try again.",
  "feedback": [
    {
      "question_id": "cs_s1_q1",
      "question_text": "Which best describes a variable?",
      "student_answer": "A type of loop",
      "is_correct": false,
      "correct_answer": "A named storage for data",
      "correct_answer_id": "a"
    },
    {
      "question_id": "cs_s1_q2",
      "question_text": "Which construct repeats code while a condition is true?",
      "student_answer": "print",
      "is_correct": false,
      "correct_answer": "while",
      "correct_answer_id": "b"
    },
    {
      "question_id": "cs_s1_q3",
      "question_text": "Why do we write functions?",
      "student_answer": "To make code longer",
      "is_correct": false,
      "correct_answer": "To reuse and organize logic",
      "correct_answer_id": "a"
    }
  ]
}
```

---

## Example 5: Exam Submission - Passed (No Feedback)

```bash
curl -X POST http://localhost:8000/exams/submit \
  -H "Content-Type: application/json" \
  -d '{
    "player_id": "player-uuid-here",
    "semester": 1,
    "answers": [
      {"question_id": "cs_s1_q1", "chosen_choice_id": "a"},
      {"question_id": "cs_s1_q2", "chosen_choice_id": "b"},
      {"question_id": "cs_s1_q3", "chosen_choice_id": "a"}
    ]
  }' | jq '.exam_result, .passed, .message, .feedback'
```

**Response:**
```json
{
  "exam_result": {
    "correct_count": 3,
    "total_questions": 3,
    "score_percent": 100.0
  },
  "passed": true,
  "message": "Excellent work! You passed with 100.0%!",
  "feedback": []
}
```

---

## Key Differences Between Passing and Failing

| Aspect | Failed (< 70%) | Passed (≥ 70%) |
|--------|---|---|
| `passed` | `false` | `true` |
| Message | "Review the correct answers below..." | "Excellent work! You passed with X%!" |
| `feedback` array | ✅ **Contains all questions** | ✅ **Empty** |
| Shows correct answers | ✅ **YES** | ❌ No (they got it!) |
| GPA updated | ✅ Yes | ✅ Yes |
| Credits awarded | ✅ Yes | ✅ Yes |

---

## Integration Example: Frontend Workflow

1. **Before exam:** Get games for the course
   ```javascript
   GET /curriculum/courses/cs101/games
   ```

2. **Optional:** Play games to learn
   ```javascript
   GET /curriculum/lessons/lesson_1/game
   POST /curriculum/lessons/lesson_1/game/submit
   ```

3. **Take exam:** Generate and submit
   ```javascript
   POST /exams/generate
   POST /exams/submit  // If failed, shows correct answers!
   ```

4. **On failure:** Display feedback
   ```javascript
   if (!result.passed) {
     result.feedback.forEach(item => {
       console.log(`Q: ${item.question_text}`);
       console.log(`You said: ${item.student_answer}`);
       console.log(`Correct: ${item.correct_answer}`); // NEW!
     });
   }
   ```

---

## Adding New Games

Edit `catalogs/lesson_games.py`:

```python
LESSON_GAMES = {
    "lesson_6": {  # Your lesson ID
        "game_id": "game_cs101_06",
        "lesson_id": "lesson_6",
        "title": "Your Game Title",
        "game_type": "interactive",  # or puzzle, coding, matching, simulation
        "description": "What this game teaches",
        "objectives": [
            "Learning objective 1",
            "Learning objective 2"
        ],
        "difficulty": "beginner",  # or intermediate, advanced
        "estimated_duration_minutes": 7,
        "content": {
            # Your game-specific structure
            "rounds": [
                {
                    "question": "...",
                    "options": ["a", "b", "c"],
                    "correct": 0
                }
            ]
        }
    }
}
```

The game automatically becomes available:
- `GET /curriculum/lessons/lesson_6/game`
- `GET /curriculum/courses/{course_id}/games` (if lesson is in course)
