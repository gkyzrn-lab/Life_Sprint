# 🎮 Life Sprint - Educational Life Simulation Game

> **The strategic life planning game.** Make real decisions, face real consequences. Manage finances, plan your education, balance work and wellness.

**Status**: ✅ Production Ready | ✅ 676 tests passing | ✅ Fully Documented

---

## 🚀 Quick Start (2 Minutes)

### **Option 1: I just want to play**
```bash
# Backend
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
source .venv/bin/activate
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

# Frontend (new terminal)
cd /Users/oktaygokayzeren/Desktop/Life_Sprint/life-sprint-frontend
npm run dev
```

Then open: **http://localhost:3000**

### **Option 2: I'm a developer**
→ Read **[GETTING_STARTED.md](GETTING_STARTED.md)** (5 min guide)
→ Read **[PROJECT_INDEX.md](PROJECT_INDEX.md)** (complete index)
→ Read **[STRUCTURE.md](STRUCTURE.md)** (folder organization)

---

## 📚 Documentation Hub

| Document | Purpose | Audience |
|----------|---------|----------|
| **[GETTING_STARTED.md](GETTING_STARTED.md)** | Setup & quick start | Everyone |
| **[PROJECT_INDEX.md](PROJECT_INDEX.md)** | Complete file index | Developers |
| **[STRUCTURE.md](STRUCTURE.md)** | Folder organization | Developers |
| **[API_REFERENCE.md](API_REFERENCE.md)** | All endpoints | Frontend devs |
| **[CHEAT_SHEET.md](CHEAT_SHEET.md)** | Code patterns & commands | Backend devs |
| **[core_domain/README.md](core_domain/README.md)** | Game state & data | Backend devs |
| **[api/README.md](api/README.md)** | How to write endpoints | Backend devs |
| **[finance/README.md](finance/README.md)** | Loans & finance system | Finance feature devs |
| **[life-sprint-frontend/README.md](life-sprint-frontend/README.md)** | React frontend | Frontend devs |

---

## 🎯 What is Life Sprint?

A strategy and simulation game where you guide a student through college and beyond:

**Make Decisions:**
- Choose your college and major
- Plan each semester (classes, job, housing, activities)
- Decide on loans and finances
- Manage stress and wellness

**Face Consequences:**
- Work too hard → stress increases → GPA drops
- Borrow too much → loan payments crush your budget
- Neglect wellbeing → burnout hits hard
- Skip class → fail exams

**Compete:**
- Leaderboards (GPA, wealth, stress management)
- Achievements & badges
- Compare decisions with other players
- Seasonal challenges

---

## 🏗️ Tech Stack

| Layer | Tech | Role |
|-------|------|------|
| Frontend | React 18 + Vite | Modern UI |
| Backend | FastAPI (Python) | REST API |
| Database | In-memory (upgradeable) | Data persistence |
| Testing | pytest | 676 tests ✅ |
| Deployment | Docker-ready | Production |

---

## 📁 Project Structure

```
Life_Sprint/
├── main.py                          ← App entry point
├── core_domain/                     ← Game state & models ⭐
├── api/                             ← REST endpoints (25+ routers)
├── academics/                       ← Courses & exams
├── finance/                         ← Loans & money
├── planning/                        ← Semester planning
├── career/                          ← Career paths
├── catalogs/                        ← Static game data
├── tests/                           ← 676 tests ✅
├── life-sprint-frontend/            ← React UI
└── [docs]                           ← This documentation
```

**Full structure details**: [STRUCTURE.md](STRUCTURE.md) | **File index**: [PROJECT_INDEX.md](PROJECT_INDEX.md)

---

## 🚀 Getting Started (Choose Your Path)

### **I Just Want to Play**
1. Start backend (see Quick Start above)
2. Start frontend
3. Go to http://localhost:3000
4. Create a player and play!

### **I Want to Develop Features**
1. Read [GETTING_STARTED.md](GETTING_STARTED.md)
2. Read [STRUCTURE.md](STRUCTURE.md)
3. Read [CHEAT_SHEET.md](CHEAT_SHEET.md)
4. Pick a feature folder and read its README
5. Run tests: `pytest -v`

### **I'm Fixing a Bug**
1. Run the failing test: `pytest tests/test_file.py::test_name -v`
2. Find the code that's broken
3. Review the relevant README
4. Make the fix
5. Run tests again: `pytest -q`

### **I'm Deploying**
1. Ensure all 676 tests pass: `pytest -q`
2. Replace STORE in `core_domain/store.py` with your database
3. Set environment variables for production
4. Deploy backend on your server
5. Deploy frontend (built with `npm run build`)

---

## 💻 Commands You'll Use

```bash
# Start backend
source .venv/bin/activate
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

# Start frontend
cd life-sprint-frontend
npm run dev

# Run all tests
pytest -q

# Run with verbose output
pytest -v

# Check what's available
curl http://localhost:8000/docs  # Swagger UI
```

**More commands?** See [CHEAT_SHEET.md](CHEAT_SHEET.md)

---

## 🎮 Core Game Systems

### **Planning** 📅
Save semester plans with housing, job, activities, courses. Lock before exams.

### **Finance** 💰
Borrow loans (subsidized, unsubsidized, private). Manage cash flow. Make payments during repayment.

### **Academics** 📚
Take courses. Pass mini-games. Take final exams. Advance semesters.

### **Career** 💼
Match with career paths. Get recommendations. Develop skills.

### **Wellness** 🏥
Manage stress, happiness, burnout. Balance work and health.

### **Community** 👥
Join study groups. Form guilds. Collaborate on projects.

### **Analytics** 📊
Track your stats. Leaderboards. Achievements. Progress reports.

---

## ✅ Quality Assurance

- **676 tests** - all passing ✅
- **25+ routers** - all working ✅
- **30+ service modules** - all tested ✅
- **40+ catalogs** - validated ✅
- **100% documentation** - every folder has README ✅

---

## 🤝 Contributing

### **Before You Start**
1. Read [CHEAT_SHEET.md](CHEAT_SHEET.md) for code patterns
2. Check [PROJECT_INDEX.md](PROJECT_INDEX.md) to find related code
3. Run existing tests: `pytest -q`

### **Making a Change**
1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make your changes
3. Write or update tests
4. Run tests: `pytest -v`
5. Commit: `git commit -m "feat: description"`
6. Push: `git push origin feature/my-feature`
7. Create pull request

### **Code Quality**
- All tests must pass (`pytest -q`)
- Code must follow existing patterns
- New features need tests
- Docstrings required for new functions
- No unused imports

---

## 📞 Support & Questions

**Need help?**
1. Check [PROJECT_INDEX.md](PROJECT_INDEX.md) to find the code
2. Read the relevant README (each folder has one)
3. Check test files for usage examples
4. Search the code: `grep -r "function_name" .`
5. Run with verbose: `pytest -v -s`

**Found a bug?**
1. Create a failing test first
2. Make the minimal fix
3. Ensure all tests pass
4. Document what changed

---

## 📜 License

This project is part of the Life Sprint educational initiative.

---

## 🎓 Learning Resources

This codebase is designed for learning. Every major component has documentation:

- **[STRUCTURE.md](STRUCTURE.md)** - Project organization
- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Setup & basics
- **[PROJECT_INDEX.md](PROJECT_INDEX.md)** - Complete file index
- **[CHEAT_SHEET.md](CHEAT_SHEET.md)** - Common patterns
- **[API_REFERENCE.md](API_REFERENCE.md)** - All endpoints
- **Folder READMEs** - In-depth guides for each system

---

## 🚀 Next Steps

**New to the project?**
→ Start with [GETTING_STARTED.md](GETTING_STARTED.md)

**Want to contribute?**
→ Read [CHEAT_SHEET.md](CHEAT_SHEET.md) then pick an issue

**Need to deploy?**
→ Check the setup in [GETTING_STARTED.md](GETTING_STARTED.md) deployment section

**Want to understand architecture?**
→ Read [PROJECT_INDEX.md](PROJECT_INDEX.md)

---

## 📊 By The Numbers

- **55,000+** lines of code
- **400+** files
- **676** tests ✅
- **25+** API routers
- **30+** service modules
- **40+** catalogs
- **100%** documentation

---

**Made with ❤️ for students everywhere.** 🎓

Happy coding! 🚀

            "options": options,
        }

    def select_college(self, college_data: Dict):
        """
        Lock in college selection.
        """
        self.player.college = college_data
        self.player.semester = 1

    def run_college_semester(self) -> Dict:
        """
        Run one full college semester.
        """

        # -------------------------
        # Curriculum preview (UI)
        # -------------------------
        preview = get_curriculum_preview(
            self.player.college["id"],
            self.player.major,
            self.player.semester,
        )

        # -------------------------
        # Exams (logic)
        # -------------------------
        exam_results = run_semester_exams(self.player)
        self.player.stats.gpa = exam_results["gpa"]

        # -------------------------
        # Work opportunities
        # -------------------------
        available_work = get_available_work(self.player)

        # -------------------------
        # Advance semester
        # -------------------------
        self.player.semester += 1
        self.turn += 1

        payload = {
            "phase": "college",
            "semester_completed": self.player.semester - 1,
            "curriculum_preview": preview,
            "exam_results": exam_results,
            "available_work": available_work,
            "player_snapshot": self._player_snapshot(),
        }

        self._log_history("college_semester_completed", payload)
        return payload

    # =================================================
    # WORK & INTERNSHIPS
    # =================================================

    def take_part_time_work(self, job: Dict) -> Dict:
        """
        Apply part-time job effects.
        """
        apply_work_effects(self.player, job)

        payload = {
            "type": "part_time_job_taken",
            "job": job["name"],
            "player_snapshot": self._player_snapshot(),
        }

        self._log_history("part_time_job", payload)
        return payload

    def attempt_internship(self, internship_id: str, answers: Dict[int, int]) -> Dict:
        """
        Attempt an internship with interview answers.
        """
        result = attempt_internship(self.player, internship_id, answers)

        if result["accepted"]:
            payload = {
                "type": "internship_accepted",
                "internship": result["internship"]["company"],
                "player_snapshot": self._player_snapshot(),
            }
        else:
            payload = {
                "type": "internship_rejected",
                "internship": result["internship"]["company"],
                "feedback": result["feedback"],
                "player_snapshot": self._player_snapshot(),
            }

        self._log_history(payload["type"], payload)
        return payload

    # =================================================
    # INTERNAL UTILITIES
    # =================================================

    def _player_snapshot(self) -> Dict:
        """
        UI-safe snapshot of player state.
        """
        return {
            "semester": self.player.semester,
            "college": self.player.college.get("name") if self.player.college else None,
            "major": self.player.major,
            "gpa": round(self.player.stats.gpa, 2),
            "stress": self.player.stats.stress,
            "personality": self.player.personality,
            "modern_skills": vars(self.player.modern_skills),
            "finance": {
                "balance": self.player.finance.balance,
            },
        }

    def _log_history(self, event_type: str, payload: Dict):
        """
        Central history logging.
        """
        self.player.history.append({
            "turn": self.turn,
            "event_type": event_type,
            "data": payload,
        })
