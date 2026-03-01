# 📖 Complete API Reference

> All endpoints available in Life Sprint backend. Auto-generated from code.

**Base URL:** `http://localhost:8000`

---

## 📋 Quick Navigation

- [Player Management](#player-management) - Create & manage players
- [Planning](#planning) - Semester plans, housing, jobs
- [Finance](#finance) - Loans, borrowing, repayment
- [Academics](#academics) - Courses, exams, tutorials
- [Career](#career) - Career paths & recommendations
- [Health & Wellness](#health--wellness) - Stress, happiness
- [Community](#community) - Study groups, guilds, projects
- [Analytics](#analytics) - Stats, leaderboards, achievements
- [Miscellaneous](#miscellaneous) - Catalogs, store, utilities

---

## Player Management

### Create Player
```
POST /player/start

Request:
{
  "name": "John Doe",
  "college_id": "cuny_baruch",
  "major_id": "finance",
  "age": 18,
  "hs_gpa": 3.5,
  "parent_income": 75000,
  "starting_balance": 5000,
  "housing_option_id": "dorm",
  "job_id": null
}

Response:
{
  "id": "uuid-here",
  "name": "John Doe",
  "semester": 1,
  "year_in_school": 1,
  "stats": {...},
  "finance": {...},
  "housing": {...}
}
```

### Get Player
```
GET /player/{player_id}

Response:
{
  "id": "uuid-here",
  "name": "John Doe",
  ... all player data
}
```

---

## Planning

### Save Semester Plan (Draft)
```
POST /planning/save-plan

Request:
{
  "player_id": "uuid-here",
  "semester": 1,
  "housing_option_id": "dorm",
  "job_id": "barista",
  "activities": ["coding-club", "debate-team"]
}

Response:
{
  "semester": 1,
  "housing_option_id": "dorm",
  "job_id": "barista",
  "activities": ["coding-club", "debate-team"],
  "locked": false
}
```

### Lock Plan (Required before progression)
```
POST /planning/lock-plan

Request:
{
  "player_id": "uuid-here",
  "semester": 1
}

Response:
{
  "semester": 1,
  "locked": true
}
```

### Emergency Change (Mid-semester with penalty)
```
POST /planning/emergency-change

Request:
{
  "player_id": "uuid-here",
  "semester": 1,
  "housing_option_id": "apartment",
  "job_id": "tutor",
  "activities": ["coding-club"],
  "cause_id": "family-emergency",
  "random_cause": false
}

Response:
{
  "message": "Emergency change applied",
  "penalty_stress": 10,
  "tokens_remaining": 2
}
```

### Forecast Plan (Preview without saving)
```
POST /planning/forecast-plan

Request:
{
  "player_id": "uuid-here",
  "housing_option_id": "dorm",
  "job_id": "barista",
  "activities": ["coding-club"]
}

Response:
{
  "weekly_load": {
    "course_hours": 25,
    "job_hours": 16,
    "activity_hours": 5,
    "total_hours": 46,
    "overload": 14,
    "stress_impact": 8.5
  },
  "warnings": ["Severe overload: expect burnout risk"]
}
```

---

## Finance

### View Player Finances
```
GET /finance/{player_id}

Response:
{
  "balance": 5000,
  "monthly_expenses": 1200,
  "tuition_per_semester": 3000,
  "loan_portfolio": {
    "loans": [
      {
        "id": "uuid",
        "loan_type": "subsidized",
        "principal": 5500,
        "accrued_interest": 0,
        "annual_interest_rate": 4.5
      }
    ]
  },
  "repayment_profile": {
    "plan_type": "standard",
    "annual_income": 40000,
    "family_size": 1
  }
}
```

### Borrow for Semester
```
POST /finance/borrow

Request:
{
  "player_id": "uuid-here",
  "amount_needed": 3000
}

Response:
{
  "borrowed": 3000,
  "loans": {
    "subsidized": 2625,
    "unsubsidized": 375,
    "private": 0
  },
  "new_balance": 8000
}
```

### Make Loan Payment
```
POST /finance/repay

Request:
{
  "player_id": "uuid-here",
  "months": 12
}

Response:
{
  "total_paid": 1500,
  "loans_status": [
    {
      "loan_type": "subsidized",
      "remaining_principal": 4000,
      "minimum_payment": 125
    }
  ],
  "balance_remaining": 6500
}
```

### Set Repayment Plan
```
POST /finance/set-repayment-profile

Request:
{
  "player_id": "uuid-here",
  "plan_type": "idr",
  "annual_income": 45000,
  "family_size": 1,
  "payment_cap_to_standard": true
}

Response:
{
  "plan_type": "idr",
  "annual_income": 45000,
  "monthly_payment": 200
}
```

---

## Academics

### Get Course Information
```
GET /curriculum/course/{course_id}

Response:
{
  "id": "ba101",
  "name": "Principles of Business",
  "major_id": "business_admin",
  "semester": 1,
  "credits": 3,
  "description": "...",
  "topics": [
    {
      "name": "Business Fundamentals",
      "emoji": "📊",
      "description": "..."
    }
  ],
  "mini_games": [
    {
      "id": "game-1",
      "name": "Scenario Decision",
      "type": "scenario_decision"
    }
  ]
}
```

### Generate Final Exam
```
POST /exams/generate

Request:
{
  "player_id": "uuid-here",
  "semester": 1,
  "num_questions": 3
}

Response:
{
  "major_id": "finance",
  "semester": 1,
  "topic_tags": ["derivative", "portfolio", "valuation"],
  "questions": [
    {
      "id": "q1",
      "text": "What is a derivative?",
      "choices": [
        {"id": "a", "text": "Answer A"},
        {"id": "b", "text": "Answer B"}
      ]
    }
  ]
}
```

### Grade Exam with Feedback
```
POST /exams/grade-with-feedback

Request:
{
  "player_id": "uuid-here",
  "semester": 1,
  "answers": [
    {
      "question_id": "q1",
      "chosen_choice_id": "a"
    }
  ]
}

Response:
{
  "exam_result": {
    "correct_count": 2,
    "total_questions": 3,
    "score_percent": 66.67
  },
  "passed": false,
  "message": "You scored 66.67%. Review the answers below.",
  "feedback": [
    {
      "question_id": "q1",
      "question_text": "What is a derivative?",
      "student_answer": "Wrong Answer",
      "is_correct": false,
      "correct_answer": "Correct Answer"
    }
  ]
}
```

### Get Mini-Game
```
GET /curriculum/games/{game_id}

Response:
{
  "id": "game-1",
  "name": "Accounting Balance",
  "type": "accounting_balance",
  "course_id": "ba102",
  "difficulty": "medium",
  "questions": [
    {
      "id": "q1",
      "text": "Debit which account?",
      "correct_answer": "assets"
    }
  ]
}
```

### Submit Mini-Game
```
POST /curriculum/games/submit

Request:
{
  "player_id": "uuid-here",
  "game_id": "game-1",
  "answers": [
    {
      "question_id": "q1",
      "answer": "assets"
    }
  ]
}

Response:
{
  "score": 85,
  "correct": 17,
  "total": 20,
  "feedback": "Great job! You understand debit/credit mechanics.",
  "xp_earned": 50,
  "badge_unlocked": "accounting-expert"
}
```

---

## Career

### Get Career Paths
```
GET /career/{player_id}/paths

Response:
{
  "current_major": "finance",
  "available_paths": [
    {
      "id": "investment-banker",
      "name": "Investment Banking",
      "required_skills": ["analysis", "communication"],
      "salary_range": "80000-200000",
      "market_demand": "high"
    }
  ]
}
```

### Get Career Recommendations
```
GET /career/recommendations/{player_id}

Response:
{
  "player_id": "uuid",
  "major_id": "finance",
  "gpa": 3.5,
  "recommendations": [
    {
      "career": "Financial Analyst",
      "fit_score": 92,
      "salary_range": "60000-120000",
      "skills_to_develop": ["Python", "SQL"]
    }
  ]
}
```

### Get Market Intelligence
```
GET /market-intelligence/overview

Response:
{
  "emerging_fields": [
    {
      "field": "Data Science",
      "growth_rate": "45%",
      "avg_salary": "95000"
    }
  ],
  "trending_skills": ["Python", "Data Analysis", "AI/ML"]
}
```

---

## Health & Wellness

### Get Health Status
```
GET /health/{player_id}

Response:
{
  "stress": 45,
  "happiness": 75,
  "burnout": 20,
  "sleep_quality": "good",
  "physical_health": "healthy",
  "recommendations": [
    "Try meditation for stress relief",
    "Exercise 3x per week"
  ]
}
```

### Manage Stress
```
POST /health/{player_id}/manage-stress

Request:
{
  "activity": "meditation",
  "duration_minutes": 30
}

Response:
{
  "stress_before": 45,
  "stress_after": 35,
  "impact": -10,
  "message": "Meditation helped! You feel more relaxed."
}
```

---

## Community

### Get Study Groups
```
GET /community/{player_id}/study-groups

Response:
{
  "available": [
    {
      "id": "sg1",
      "name": "Calculus Study Group",
      "members": 5,
      "topic": "Calculus",
      "schedule": "Wed & Fri 7pm"
    }
  ]
}
```

### Join Study Group
```
POST /community/{player_id}/join-study-group

Request:
{
  "group_id": "sg1"
}

Response:
{
  "message": "Joined Calculus Study Group",
  "group": {
    "id": "sg1",
    "members": 6
  }
}
```

### Get Guilds
```
GET /community/{player_id}/guilds

Response:
{
  "available_guilds": [
    {
      "id": "guild1",
      "name": "Coders Unite",
      "members": 12,
      "benefits": ["Networking", "Collaboration"]
    }
  ],
  "my_guilds": [
    {
      "id": "guild1",
      "role": "member"
    }
  ]
}
```

---

## Analytics

### Get Analytics Dashboard
```
GET /analytics/{player_id}/dashboard

Response:
{
  "player_id": "uuid",
  "overall_score": 8250,
  "rank": 42,
  "achievements_unlocked": 15,
  "total_achievements": 50,
  "recent_stats": {
    "courses_completed": 12,
    "gpa": 3.5,
    "stress_trend": "decreasing"
  }
}
```

### Get Leaderboard
```
GET /analytics/leaderboard?category=overall&limit=10

Response:
{
  "category": "overall",
  "entries": [
    {
      "rank": 1,
      "player_name": "Top Player",
      "score": 15000,
      "badges": 25
    }
  ]
}
```

### Unlock Achievement
```
POST /analytics/{player_id}/unlock-achievement

Request:
{
  "achievement_id": "first-loan"
}

Response:
{
  "message": "Achievement Unlocked: First Loan!",
  "xp_earned": 100,
  "total_xp": 1250
}
```

---

## Miscellaneous

### Get All Catalogs
```
GET /catalogs/

Response:
{
  "colleges": {...},
  "majors": {...},
  "housing": {...},
  "jobs": {...},
  "activities": {...}
}
```

### Get Specific Catalog
```
GET /catalogs/colleges
GET /catalogs/majors
GET /catalogs/housing
GET /catalogs/jobs
GET /catalogs/activities
```

### Health Check
```
GET /health

Response:
{
  "status": "healthy",
  "version": "0.1.0"
}
```

### Root Endpoint (All Routes)
```
GET /

Response:
{
  "status": "ok",
  "message": "Life Sprint Backend running",
  "total_routes": 150,
  "routes": [
    {
      "path": "/player/start",
      "methods": ["POST"],
      "name": "start_player"
    }
  ]
}
```

---

## Error Responses

All errors follow this format:

```
{
  "detail": "Descriptive error message"
}
```

Common status codes:
- **200**: OK
- **201**: Created
- **400**: Bad Request (invalid input)
- **404**: Not Found (player/resource doesn't exist)
- **422**: Validation Error (missing required fields)
- **500**: Server Error

---

## Testing the API

### Using curl
```bash
# Create player
curl -X POST http://localhost:8000/player/start \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Player",
    "college_id": "cuny_baruch",
    "major_id": "finance"
  }'

# Get player
curl http://localhost:8000/player/{player_id}

# Check health
curl http://localhost:8000/health
```

### Using Swagger UI
Visit: **http://localhost:8000/docs**

- Click on any endpoint
- Click "Try it out"
- Fill in parameters
- Click "Execute"

### Using Python
```python
import requests

# Create player
resp = requests.post('http://localhost:8000/player/start', json={
    'name': 'Test',
    'college_id': 'cuny_baruch',
    'major_id': 'finance'
})
player = resp.json()
print(player['id'])

# Get player
resp = requests.get(f'http://localhost:8000/player/{player["id"]}')
print(resp.json())
```

---

## Quick Reference: Common Requests

```bash
# 1. Create a player
PLAYER_ID=$(curl -s -X POST http://localhost:8000/player/start \
  -H 'Content-Type: application/json' \
  -d '{"name":"Player","college_id":"cuny_baruch","major_id":"finance"}' | \
  python -c "import sys, json; print(json.load(sys.stdin)['id'])")

# 2. Save a plan
curl -X POST http://localhost:8000/planning/save-plan \
  -H 'Content-Type: application/json' \
  -d "{\"player_id\":\"$PLAYER_ID\",\"semester\":1,\"housing_option_id\":\"dorm\",\"job_id\":null,\"activities\":[]}"

# 3. Lock the plan
curl -X POST http://localhost:8000/planning/lock-plan \
  -H 'Content-Type: application/json' \
  -d "{\"player_id\":\"$PLAYER_ID\",\"semester\":1}"

# 4. Generate exam
curl -X POST http://localhost:8000/exams/generate \
  -H 'Content-Type: application/json' \
  -d "{\"player_id\":\"$PLAYER_ID\",\"semester\":1}"

# 5. Get analytics
curl http://localhost:8000/analytics/$PLAYER_ID/dashboard
```

---

**Last Updated:** March 2026  
**Version:** 0.1.0  
**Status:** ✅ All endpoints tested and working
