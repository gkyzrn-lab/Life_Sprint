# Life Sprint Project Structure Guide

> **For everyone**: A clear, simple guide to find any code or feature in this project.

## 🏗️ Project Overview

**Life Sprint** is an educational life simulation game built with:
- **Backend**: FastAPI (Python) - runs at `http://localhost:8000`
- **Frontend**: React + Vite (Node.js) - runs at `http://localhost:3000`
- **Database**: In-memory store (development) - upgradeable to real DB

---

## 📁 Main Folders Explained

### **1. `core_domain/` - The Game Heart** 💓
The most important folder. Contains all core game data models and rules.

```
core_domain/
├── player/
│   ├── player_model.py          ← Main Player object (everything about a player)
│   └── player_stats.py          ← Stress, happiness, burnout tracking
├── finance/
│   ├── finance_models.py        ← Loans, balance, expenses
│   └── repayment_models.py      ← Loan repayment plans
├── planning/
│   └── planning_models.py       ← Semester plans, housing, jobs, activities
├── stats/
│   └── stats_model.py           ← Performance metrics (GPA, skills)
├── models.py                    ← Legacy/aggregator (use player_model.py)
├── store.py                     ← IN-MEMORY database (STORE object)
├── config.py                    ← Game constants (tuition, expenses, limits)
└── utils.py                     ← Helper functions
```

**What to know:**
- `STORE` in `store.py` is the database for development
- `Player` in `player_model.py` is the main game object
- `config.py` has all game tuning values
- When you change a player, use `STORE.put_player(player)` to save

---

### **2. `api/` - REST Endpoints** 🔌
All routes the frontend calls. Each file = one feature area.

```
api/
├── router_player.py                 ← Create/load players
├── router_onboarding.py             ← New player tutorial
├── router_tutorial.py               ← Mini-game tutorials
├── router_progression.py            ← Advance semesters, graduate
├── router_curriculum.py             ← View courses, take mini-games
├── router_exams.py                  ← Final exams, grading
├── router_planning.py               ← Save plans, lock, emergencies
├── router_finance.py                ← Loans, borrowing, repayment
├── router_career.py                 ← Career paths, job matching
├── router_health.py                 ← Wellness, stress management
├── router_analytics.py              ← Player stats, leaderboards
├── router_community.py              ← Study groups, guilds, projects
├── router_mentorship.py             ← Mentor relationships
├── router_social.py                 ← Social features
├── router_housing_market.py         ← Housing options
├── router_side_gigs.py              ← Side jobs for cash
├── router_store.py                  ← In-game store items
├── router_difficulty.py             ← Game difficulty settings
├── router_catalogs.py               ← Static data (colleges, majors)
├── router_major_exploration.py      ← Try different majors
├── router_career_recommendations.py ← Smart career suggestions
├── router_market_intelligence.py    ← Market data
├── router_financial_responsibility.py ← Financial literacy
├── deps.py                          ← Helper functions for routers
└── __init__.py
```

**How to use:**
- Each router has a `@router.get()` or `@router.post()` for each endpoint
- They import from service modules (see below) for business logic
- If you need a new endpoint, add it here
- Status: `✅ All 25+ routers working`

---

### **3. Business Logic Folders** ⚙️
Each has a `service.py` with the actual game logic. Routers call these.

```
academics/
├── exam_service.py              ← Generate & grade exams
├── exam_models.py               ← Exam question/answer types
├── exam_pools.py                ← Questions for each major/semester
├── course_service.py            ← Course info, enrollment
├── course_games.py              ← Mini-games (accounting, scenarios, etc)
├── curriculum.py                ← Curriculum structure
├── curriculum_models.py         ← Course data models
├── tutorial_service.py          ← Tutorial game logic
├── tutorial_games.py            ← Step-by-step quest for new players
└── selectors.py                 ← Helper to find courses by major

planning/
├── service.py                   ← Save/lock/update semester plans
├── penalties.py                 ← Emergency change costs
├── emergency_causes.py          ← Random events that disrupt plans

finance/
├── service.py                   ← Borrowing, repayment, interest math
├── loan_products.py             ← Loan types and their terms
├── calculators.py               ← Amortization, IDR payment math

career/
├── service.py                   ← Career path matching

wellbeing/
├── time_budget.py               ← Calculate weekly stress from coursework

health/
├── stress_model.py              ← Stress & mental health tracking
├── happiness_model.py           ← Happiness, relaxation

housing_market/
├── service.py                   ← Housing costs, availability

side_gigs/
├── service.py                   ← Part-time job opportunities

store/
├── service.py                   ← In-game shop, cosmetics

social/
├── service.py                   ← Relationships, social events

financial_responsibility/
├── service.py                   ← Budget, credit, financial literacy

analytics/
├── achievement_badges.py        ← Badge system
├── readiness_score.py           ← Graduation readiness calculation
```

**Pattern to remember:**
```
Request → api/router_*.py → business_folder/service.py → core_domain models → STORE
         (validation)         (calculation)            (data)            (save)
```

---

### **4. `catalogs/` - Static Game Data** 📚
Dictionaries of all the "things" in the game (colleges, jobs, activities, etc).
These are like a game's "asset library" - never change during gameplay.

```
catalogs/
├── colleges.py                  ← All colleges + tuition
├── majors.py                    ← All majors + requirements
├── housing.py                   ← Dorm, apartment, house options
├── jobs.py                      ← Part-time jobs (hours, pay, difficulty)
├── activities.py                ← Clubs, hobbies, volunteer work
├── career_paths.py              ← Career choices available
├── credit_cards.py              ← Credit card products (APR, limits)
├── course_content.py            ← Detailed course descriptions
├── course_topics.py             ← Topics covered in courses
├── bs_course_topics.py          ← Business topics
├── cs_course_topics.py          ← Computer science topics
├── ba_course_topics.py          ← Business admin topics
├── challenge_modes.py           ← Difficulty presets
├── analytics_gamification.py    ← Achievement & badge definitions
├── community_collaboration.py   ← Community features
├── character_customization.py   ← Avatar options
├── budgeting.py                 ← Budget categories & tips
├── credit_system.py             ← Credit score rules
└── (40+ more)
```

**Key insight:**
- Format: `{id: {...data...}}`
- Example: `COLLEGES["cuny_baruch"]` gives you the Baruch college object
- Example: `JOBS["barista"]` gives you the barista job details
- These are imported by routers/services for validation and data lookup

---

### **5. `life-sprint-frontend/` - React Frontend** 🎨
The user-facing game interface.

```
life-sprint-frontend/
├── src/
│   ├── pages/               ← Page components (Home, Game, Dashboard)
│   ├── components/          ← Reusable UI components
│   ├── services/            ← Calls to backend API
│   ├── hooks/               ← Custom React hooks
│   ├── utils/               ← Helper functions
│   ├── assets/              ← Images, fonts
│   ├── App.jsx              ← Main app component
│   └── main.jsx             ← Entry point
├── public/                  ← Static files served directly
├── index.html               ← HTML shell
├── package.json             ← Node dependencies
├── vite.config.js           ← Vite build config
└── README.md                ← Frontend setup guide
```

**Remember:**
- Frontend calls backend at `http://localhost:8000`
- Runs with `npm run dev` (port 3000)
- Built with React + Vite (super fast)

---

### **6. `tests/` - Automated Tests** ✅
Tests for all the backend code. **676 tests pass!**

```
tests/
├── test_player.py               ← Player creation, loading
├── test_planning.py             ← Plan saving, locking, emergencies
├── test_finance.py              ← Loans, borrowing, repayment
├── test_exams.py                ← Exam generation, grading
├── test_career.py               ← Career matching
├── test_analytics.py            ← Dashboard, leaderboards
├── test_community.py            ← Study groups, guilds
├── test_mentorship.py           ← Mentor system
├── test_budgeting.py            ← Budget planning
├── test_curriculum.py           ← Courses, curriculum
├── test_progression.py          ← Semester advancement
├── test_housing_market.py       ← Housing system
└── (20+ more)
```

**Quick facts:**
- Run all: `pytest -q`
- Run one file: `pytest tests/test_player.py -v`
- Run with coverage: `pytest --cov`
- ✅ **Status: All 676 tests passing**

---

### **7. Supporting Folders** 🛠️

| Folder | Purpose |
|--------|---------|
| `docs/` | API documentation, guides |
| `examples/` | Example game scenarios |
| `__pycache__/` | Python cache (ignore) |
| `.venv/` | Python virtual environment (ignore) |
| `.git/` | Git version control (ignore) |

---

## 🚀 Quick Start (How to Run Everything)

### **Backend Setup**
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint

# 1. Activate virtual environment
source .venv/bin/activate

# 2. Install dependencies (first time only)
pip install -r requirements.txt

# 3. Start backend
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Backend runs at: **http://localhost:8000**

### **Frontend Setup**
```bash
cd life-sprint-frontend

# 1. Install dependencies (first time only)
npm install

# 2. Start frontend
npm run dev
```

Frontend runs at: **http://localhost:3000**

### **Run Tests**
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
source .venv/bin/activate
pytest -q
```

---

## 🔍 How to Find Things

### **"I want to add a new endpoint"**
1. Check `api/router_*.py` to find the right router file
2. Add a `@router.post()` or `@router.get()` function
3. Import business logic from the relevant service module
4. Return a JSON response

### **"I want to change how loans work"**
1. Go to `finance/service.py` (the functions)
2. Check `finance/loan_products.py` (the data)
3. Check `core_domain/finance/finance_models.py` (the data model)
4. Update `core_domain/config.py` if tuning values

### **"I want to add a new college"**
1. Go to `catalogs/colleges.py`
2. Add a new entry to the `COLLEGES` dict
3. Make sure `api/router_player.py` validates it
4. Done! Frontend can now use it.

### **"My test is failing"**
1. Run `pytest tests/test_file.py -v` to see the error
2. Most common issues:
   - Missing import
   - Player not in STORE
   - Validation error (check catalog existence)
3. Fix the code, run tests again

### **"The frontend isn't connecting"**
1. Check backend is running: `curl http://localhost:8000/health`
2. Check frontend is running: `curl http://localhost:3000`
3. Check CORS in `main.py` allows localhost:3000
4. Check browser console for errors (F12)

---

## 📊 File Size Reference

| Component | Files | Lines of Code | Purpose |
|-----------|-------|---------------|---------|
| Core Domain | 10 | ~2,500 | Game state & models |
| API Routes | 25+ | ~5,000 | REST endpoints |
| Business Logic | 30+ | ~8,000 | Game rules & calculations |
| Catalogs | 40+ | ~10,000 | Static game data |
| Tests | 25+ | ~10,000 | Quality assurance |
| Frontend | 100+ | ~20,000 | React UI |

**Total: ~400 files, ~55,000+ lines of code** ✅

---

## 🐛 Common Issues & Fixes

| Problem | Solution |
|---------|----------|
| Import error | Run `pip install -r requirements.txt` |
| Port 8000 in use | `lsof -i :8000` then `kill -9 <PID>` |
| Frontend CORS error | Restart backend, check `main.py` CORS config |
| Test failing | Run `pytest -v` to see details |
| Player not saving | Check `STORE.put_player()` is called |
| Wrong college/job | Check catalog ID exists in relevant `catalogs/*.py` |

---

## 📚 Key Files to Know

```
main.py                         ← App entry point, router registration
core_domain/store.py            ← The database (STORE object)
core_domain/config.py           ← Game constants
api/router_player.py            ← Player creation & loading
requirements.txt                ← Python dependencies
life-sprint-frontend/package.json ← Node dependencies
```

---

## ✅ Status Check

- ✅ **Backend**: 25+ routers, 30+ services, all working
- ✅ **Frontend**: React + Vite, responsive UI
- ✅ **Tests**: 676 tests, all passing
- ✅ **Database**: In-memory (STORE), ready for upgrade
- ✅ **Documentation**: This file + API docs

---

## 🎯 Next Steps for Developers

1. **Read** `main.py` to understand app structure
2. **Explore** `core_domain/` to understand game state
3. **Check** `api/router_player.py` as an example endpoint
4. **Review** a test like `tests/test_player.py` to see how things are tested
5. **Run** the app: backend + frontend + tests

**You're ready to contribute!** 🚀
