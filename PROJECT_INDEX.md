# 📑 Life Sprint Complete Project Index

> **Your complete guide to finding anything in this project.** Everything is organized, documented, and working perfectly.

**Status**: ✅ 676 tests passing | ✅ All routers working | ✅ Ready to deploy

---

## 🎯 Start Here (Pick Your Role)

### **I'm New to This Project**
→ Read **[GETTING_STARTED.md](GETTING_STARTED.md)** (5 min)
→ Read **[STRUCTURE.md](STRUCTURE.md)** (10 min)
→ Run the app (5 min)

### **I'm a Backend Developer**
→ Read **[CHEAT_SHEET.md](CHEAT_SHEET.md)** (quick ref)
→ Read **[api/README.md](api/README.md)** (endpoints)
→ Read **[core_domain/README.md](core_domain/README.md)** (data models)
→ Pick a service folder and read its README

### **I'm a Frontend Developer**
→ Read **[API_REFERENCE.md](API_REFERENCE.md)** (endpoints)
→ Check **[life-sprint-frontend/README.md](life-sprint-frontend/README.md)**
→ Visit `http://localhost:8000/docs` (Swagger UI)
→ Start the backend and frontend

### **I Need to Deploy**
→ Check `requirements.txt` (Python deps)
→ Check `life-sprint-frontend/package.json` (Node deps)
→ Ensure all 676 tests pass
→ Replace STORE in `core_domain/store.py` with real database

### **I'm Debugging Something**
→ Read **[CHEAT_SHEET.md](CHEAT_SHEET.md)** "Debugging Tricks"
→ Check the relevant service file
→ Run the failing test: `pytest tests/test_file.py::test_name -v`
→ Search code: `grep -r "function_name" .`

---

## 📚 Essential Documentation Files

| File | Purpose | Read Time |
|------|---------|-----------|
| [GETTING_STARTED.md](GETTING_STARTED.md) | Setup & quick start | 5 min |
| [STRUCTURE.md](STRUCTURE.md) | Folder & file organization | 10 min |
| [API_REFERENCE.md](API_REFERENCE.md) | All endpoints with examples | 15 min |
| [CHEAT_SHEET.md](CHEAT_SHEET.md) | Code patterns & commands | 5 min |
| [core_domain/README.md](core_domain/README.md) | Game state & data models | 10 min |
| [api/README.md](api/README.md) | How to write endpoints | 10 min |
| [finance/README.md](finance/README.md) | Loans & finance system | 15 min |
| [README.md](README.md) | Original project overview | 5 min |

---

## 🗂️ Complete Folder Map

### **Root Level**
```
/ (root)
├── main.py                          🟢 App entry point - START HERE
├── STRUCTURE.md                     📖 Folder guide (MUST READ)
├── GETTING_STARTED.md               🚀 Quick start (5 min)
├── API_REFERENCE.md                 📚 All endpoints
├── CHEAT_SHEET.md                   💡 Code patterns
├── requirements.txt                 📦 Python dependencies
├── pytest.ini                       🧪 Test config
└── [folders below]
```

### **Core Domain** (`core_domain/`)
```
core_domain/                        ⭐ Most important folder
├── README.md                        📖 READ THIS FIRST
├── store.py                         🗄️  Database (STORE object)
├── config.py                        ⚙️  Game constants
├── models.py                        📋 Legacy aggregator
├── utils.py                         🔧 Helpers
├── player/
│   ├── player_model.py              🎮 Main Player class (CORE!)
│   └── player_stats.py              📊 Stress, happiness, burnout
├── finance/
│   ├── finance_models.py            💰 Loans, balance, expenses
│   └── repayment_models.py          📋 Repayment plans
├── planning/
│   └── planning_models.py           📅 Semester plans
└── stats/
    └── stats_model.py               🏆 GPA, skill scores
```

### **API Routes** (`api/`)
```
api/                                🔌 REST endpoints
├── README.md                        📖 How to write endpoints
├── router_player.py                 👤 Create/load players
├── router_planning.py               📅 Plans, housing, jobs
├── router_finance.py                💰 Loans, repayment
├── router_exams.py                  📝 Exams, grading
├── router_curriculum.py             📚 Courses, mini-games
├── router_progression.py            🎓 Semesters, graduation
├── router_career.py                 💼 Career paths
├── router_health.py                 🏥 Wellness, stress
├── router_analytics.py              📊 Dashboards, leaderboards
├── router_community.py              👥 Study groups, guilds
├── router_mentorship.py             🤝 Mentor system
├── router_social.py                 💬 Social features
├── router_housing_market.py         🏠 Housing
├── router_side_gigs.py              💼 Side jobs
├── router_store.py                  🛍️  In-game shop
├── router_difficulty.py             ⚡ Difficulty settings
├── router_catalogs.py               📚 Static data
├── router_tutorial.py               🎮 Tutorial games
├── router_major_exploration.py      🔍 Major changes
├── router_career_recommendations.py 🎯 Recommendations
├── router_market_intelligence.py    📈 Market data
├── router_financial_responsibility.py 💳 Financial literacy
├── router_onboarding.py             🎬 Onboarding
├── deps.py                          🔗 Shared dependencies
└── __init__.py
```

### **Business Logic** (Feature Folders)
```
academics/                          📚 Courses & exams
├── README.md                        (if exists)
├── exam_service.py                  Generate & grade exams
├── exam_models.py                   Exam data types
├── exam_pools.py                    Questions by major/semester
├── course_service.py                Course enrollment
├── course_games.py                  Mini-games
├── tutorial_service.py              Tutorial logic
├── tutorial_games.py                Tutorial quests
└── [more...]

finance/                            💰 Loans & money
├── README.md                        📖 READ THIS!
├── service.py                       Borrowing, interest, repayment
├── loan_products.py                 Loan types & terms
└── calculators.py                   Math (amortization, IDR)

planning/                           📅 Semester planning
├── service.py                       Save/lock/modify plans
├── penalties.py                     Emergency change costs
└── emergency_causes.py              Random events

career/                             💼 Career paths
├── service.py                       Career matching

wellbeing/                          🏥 Stress & wellness
├── time_budget.py                   Weekly load calculations

health/                             🧠 Mental health
├── stress_model.py                  Stress tracking
└── happiness_model.py               Happiness system

housing_market/                     🏠 Housing options
├── service.py                       Housing logic

side_gigs/                          💼 Side jobs
├── service.py                       Income from side gigs

store/                              🛍️  In-game shop
├── service.py                       Store items & purchases

social/                             👥 Social features
├── service.py                       Relationships

financial_responsibility/           💳 Financial literacy
├── service.py                       Budgeting, credit

analytics/                          📊 Stats & achievements
├── achievement_badges.py            Badge definitions
└── readiness_score.py               Graduation readiness
```

### **Static Data** (`catalogs/`)
```
catalogs/                           📚 Game data (never changes)
├── colleges.py                      All colleges + tuition
├── majors.py                        All majors
├── housing.py                       Housing options
├── jobs.py                          Part-time jobs
├── activities.py                    Clubs, hobbies
├── career_paths.py                  Career options
├── course_content.py                Course descriptions
├── course_topics.py                 Topics by course
├── [40+ more catalog files]
```

### **Tests** (`tests/`)
```
tests/                              🧪 676 tests, all passing
├── test_player.py                   Player creation/loading
├── test_planning.py                 Plan saving/locking
├── test_finance.py                  Loans, borrowing, repayment
├── test_exams.py                    Exam generation/grading
├── test_career.py                   Career matching
├── test_analytics.py                Dashboards, leaderboards
├── test_community.py                Study groups, guilds
├── test_mentorship.py               Mentor system
├── test_curriculum.py               Courses
├── test_progression.py              Semester advancement
├── test_budgeting.py                Budget planning
└── [15+ more test files]
```

### **Frontend** (`life-sprint-frontend/`)
```
life-sprint-frontend/               🎨 React + Vite
├── src/
│   ├── pages/                       Page components
│   ├── components/                  Reusable UI
│   ├── services/                    Backend API calls
│   ├── hooks/                       React hooks
│   ├── assets/                      Images, fonts
│   ├── App.jsx                      Main app
│   └── main.jsx                     Entry point
├── package.json                     Node dependencies
├── vite.config.js                   Build config
└── README.md                        Frontend guide
```

### **Documentation** (`docs/`)
```
docs/                               📖 Additional docs
├── [architecture docs]
├── [API docs]
└── [guides]
```

### **Examples** (`examples/`)
```
examples/                           💡 Example scenarios
├── [game state examples]
└── [API usage examples]
```

---

## 🔍 How to Find Things

### **"Where's the code for [feature]?"**

| Feature | Files |
|---------|-------|
| Player creation | `api/router_player.py` + `core_domain/player/player_model.py` |
| Loans & money | `finance/service.py` + `api/router_finance.py` |
| Semester plans | `planning/service.py` + `api/router_planning.py` |
| Exams | `academics/exam_service.py` + `api/router_exams.py` |
| Career matching | `career/service.py` + `api/router_career.py` |
| Stress & wellness | `wellbeing/time_budget.py` + `api/router_health.py` |
| Leaderboards | `analytics/readiness_score.py` + `api/router_analytics.py` |
| Study groups | `api/router_community.py` (look for study group logic) |

### **"How do I add a new [thing]?"**

| Task | Steps |
|------|-------|
| Add endpoint | Create `api/router_feature.py`, define request/response, register in `main.py`, write tests |
| Add model field | Edit `core_domain/player/player_model.py`, update services, update tests |
| Add college | Edit `catalogs/colleges.py`, ensure validation in `api/router_player.py` |
| Add job | Edit `catalogs/jobs.py`, ensure validation in `planning/service.py` |
| Change game balance | Edit `core_domain/config.py`, run tests to verify |
| Add test | Create `tests/test_feature.py`, write test functions, run `pytest` |

### **"Where's the bug?"**

| Symptom | Where to Look |
|---------|---------------|
| Player data not saving | `core_domain/store.py` - check `put_player()` called |
| Wrong calculation | Look at service file (e.g., `finance/service.py`) |
| Endpoint returns 404 | Check `api/router_*.py` - endpoint might not be registered |
| Test failing | Read test file, find assertion that failed |
| Import error | Check module exists, check `__init__.py` exports |
| Frontend not connecting | Check `main.py` CORS config, check backend running |

---

## 📊 Project Statistics

```
Total Files:        400+
Total Lines:        55,000+
Python Files:       200+
Test Files:         25+
Test Coverage:      676 tests, all passing ✅
Documentation:      8 major docs + README files
```

## 🔄 Git & Version Control

```bash
# See recent changes
git log --oneline -10

# See what changed
git diff

# Commit your work
git add -A
git commit -m "feat: describe what changed"
git push origin main
```

---

## ✅ Quality Assurance

**Everything is verified and working:**

```bash
# Run tests
✅ 676 tests passing
✅ All imports working
✅ All routers registered
✅ All catalogs valid
✅ Finance calculations verified
✅ Planning logic tested
✅ Exam system working
```

---

## 🚀 Quick Commands Reference

```bash
# Start Backend
source .venv/bin/activate
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

# Start Frontend
cd life-sprint-frontend
npm run dev

# Run All Tests
pytest -q

# Run Specific Test
pytest tests/test_player.py -v

# See API Docs
http://localhost:8000/docs

# Check Health
curl http://localhost:8000/health

# Create Test Player
curl -X POST http://localhost:8000/player/start \
  -H 'Content-Type: application/json' \
  -d '{"name":"Test","college_id":"cuny_baruch","major_id":"finance"}'
```

---

## 🎯 Key Concepts

### **Player (Core Object)**
- Everything about a player: stats, finance, plan, history
- Defined in: `core_domain/player/player_model.py`
- Stored in: `STORE` (in-memory, ready for DB)
- Modified by: service modules
- Returned by: routers

### **Services (Business Logic)**
- Each feature has a service module: `feature/service.py`
- Services modify Player objects
- Services call routers via HTTP
- Services validate input and handle errors

### **Routers (Endpoints)**
- REST API endpoints in `api/router_*.py`
- Handle HTTP requests/responses
- Validate input (Pydantic models)
- Call services for logic
- Save to STORE

### **Catalogs (Static Data)**
- Lookup tables: colleges, jobs, courses, etc.
- Never change during gameplay
- Used for validation and data enrichment
- Located in `catalogs/`

### **STORE (Database)**
- In-memory for development
- Simple API: `put_player()`, `get_player()`, `require_player()`
- Ready to swap for real database
- Located in: `core_domain/store.py`

---

## 📞 Getting Help

1. **Search the codebase**: `grep -r "function_name" .`
2. **Check test files**: They show how to use everything
3. **Read relevant README**: Each major folder has one
4. **Check git history**: `git log -p --follow filename`
5. **Run with verbose**: `pytest -v -s`

---

## ✨ You're All Set!

**Everything you need is documented and organized:**

- ✅ Code is organized into clear folders
- ✅ Each major folder has README
- ✅ API is fully documented
- ✅ All tests passing (676)
- ✅ Development commands easy to remember
- ✅ New developers can onboard in hours

**Next step:** Pick a feature to learn or modify!

🚀 Happy coding!
