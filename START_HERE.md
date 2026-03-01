# 🎯 START HERE - Your Life Sprint Guide

> **You are here** because someone gave you this project and said "it works." Let's prove it! 👋

---

## ⚡ First 5 Minutes: Get It Running

### **Step 1: Start the Backend**
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
source .venv/bin/activate
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

**You should see:**
```
Uvicorn running on http://127.0.0.1:8000
```

### **Step 2: Start the Frontend (New Terminal)**
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint/life-sprint-frontend
npm run dev
```

**You should see:**
```
  ➜  Local:   http://localhost:3000
```

### **Step 3: Open in Browser**
Go to: **http://localhost:3000**

### **Step 4: Verify It Works**
- Create a player
- See dashboard appear
- You're good! ✅

---

## 📚 Next Steps (Choose Your Path)

### **Path A: I Just Want to Play**
→ You're done! Enjoy the game! 🎮

### **Path B: I Need to Understand the Code** (Developers)
1. **Read** [STRUCTURE.md](STRUCTURE.md) (10 minutes)
   - Understand folder organization
   - See what's in each folder
   
2. **Skim** [PROJECT_INDEX.md](PROJECT_INDEX.md) (5 minutes)
   - Find where features are
   - Quick reference for looking things up

3. **Keep Handy** [CHEAT_SHEET.md](CHEAT_SHEET.md)
   - Common code patterns
   - Testing commands
   - Debugging tricks

### **Path C: I Need to Make a Change** (Developers)
1. Read [CHEAT_SHEET.md](CHEAT_SHEET.md) - code patterns
2. Find the code using [PROJECT_INDEX.md](PROJECT_INDEX.md)
3. Write a test first
4. Make the change
5. Run `pytest -q` to verify

### **Path D: I Need to Deploy** (DevOps)
1. Check [GETTING_STARTED.md](GETTING_STARTED.md) - environment setup
2. Review code in `core_domain/store.py` - currently in-memory
3. Replace STORE with your database
4. Deploy backend and frontend
5. Run `pytest -q` to verify in production

---

## 📖 All Documentation (Find What You Need)

| Document | Best For | Time |
|----------|----------|------|
| **[GETTING_STARTED.md](GETTING_STARTED.md)** | Everyone | 5 min |
| **[STRUCTURE.md](STRUCTURE.md)** | Developers | 10 min |
| **[PROJECT_INDEX.md](PROJECT_INDEX.md)** | Developers | 5 min |
| **[API_REFERENCE.md](API_REFERENCE.md)** | Frontend devs | 15 min |
| **[CHEAT_SHEET.md](CHEAT_SHEET.md)** | Backend devs | 5 min |
| **[CLEANUP_SUMMARY.md](CLEANUP_SUMMARY.md)** | Project leads | 10 min |

---

## 🎮 Quick Game Overview

**Life Sprint** is a strategy game where you:
- 🎓 Choose a college and major
- 📚 Take courses and pass exams
- 💼 Get jobs and earn money
- 💰 Manage loans and finances
- 📅 Plan semesters (housing, activities, job)
- 😌 Balance stress and wellness
- 🎯 Compete on leaderboards

**The catch:** Everything has consequences! Work too hard → stress increases → grades drop.

---

## ✅ Verify Everything Works

```bash
# Run all tests
pytest -q

# You should see:
# 676 passed in 0.XX s
```

**All 676 tests passing?** You're good! ✅

---

## 🤔 Common Questions

### **"Backend won't start"**
```bash
# Kill any old process
pkill -f uvicorn

# Try again
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### **"Frontend won't start"**
```bash
# Make sure you're in the right folder
cd /Users/oktaygokayzeren/Desktop/Life_Sprint/life-sprint-frontend

# Install dependencies (first time)
npm install

# Start
npm run dev
```

### **"It says port 8000 is in use"**
```bash
# Find what's using it
lsof -i :8000

# Kill it (replace 12345 with the PID)
kill -9 12345
```

### **"Tests are failing"**
```bash
# Run with details
pytest tests/test_file.py -v

# Look at the error message
# Most common: missing import or player not in database
```

### **"I changed something and it broke"**
```bash
# Run tests to see what failed
pytest -v

# Read the error message
# Go find the code that's broken (use PROJECT_INDEX.md)
# Check similar code for the pattern
# Fix it
# Run tests again
```

---

## 🗂️ Essential Folders to Know

```
core_domain/    ← Game data & rules (most important!)
api/            ← REST endpoints
finance/        ← Money & loans system
planning/       ← Semester plans
academics/      ← Courses & exams
catalogs/       ← Static data (colleges, jobs, etc)
tests/          ← Tests (676 of them!)
```

**See each folder's README for details!** →  [STRUCTURE.md](STRUCTURE.md)

---

## 💻 Useful Commands (Copy & Paste)

```bash
# Start backend
source .venv/bin/activate
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

# Start frontend
cd life-sprint-frontend && npm run dev

# Run tests
pytest -q

# Run with details
pytest -v

# Test one file
pytest tests/test_player.py -v

# Check API docs
curl http://localhost:8000/docs

# Create a player
curl -X POST http://localhost:8000/player/start \
  -H 'Content-Type: application/json' \
  -d '{
    "name":"TestPlayer",
    "college_id":"cuny_baruch",
    "major_id":"finance",
    "hs_gpa":3.5,
    "parent_income":70000,
    "starting_balance":5000,
    "housing_option_id":"dorm"
  }'
```

---

## 📊 Project at a Glance

```
✅ 676 tests - ALL PASSING
✅ 25+ API endpoints - ALL WORKING
✅ Complete documentation - 9 major guides
✅ Clean code structure - logical folders
✅ Zero hard-coded values - all configurable
✅ Ready for production - just replace STORE with DB
```

---

## 🎓 Learning Path (Recommended)

### **30 minutes: Learn the Basics**
1. Read [STRUCTURE.md](STRUCTURE.md) (10 min)
2. Skim `main.py` (5 min)
3. Skim `core_domain/player/player_model.py` (5 min)
4. Skim `api/router_player.py` (5 min)
5. Run the app and create a player (5 min)

### **1 hour: Understand the Flow**
1. Read [PROJECT_INDEX.md](PROJECT_INDEX.md) (5 min)
2. Read `finance/README.md` (15 min)
3. Trace through a payment flow in the code (20 min)
4. Write a test for existing code (20 min)

### **2 hours: Make a Change**
1. Pick a small feature (finding the code)
2. Read [CHEAT_SHEET.md](CHEAT_SHEET.md) patterns
3. Write a test for your change first
4. Implement the change
5. Run `pytest -q` to verify

---

## 🚀 You're Ready!

**Pick what you want to do:**

- **Just play?** → Start backend + frontend, go to http://localhost:3000 ✅
- **Understand code?** → Read [STRUCTURE.md](STRUCTURE.md) then [PROJECT_INDEX.md](PROJECT_INDEX.md) ✅
- **Make a change?** → Read [CHEAT_SHEET.md](CHEAT_SHEET.md) then find code using [PROJECT_INDEX.md](PROJECT_INDEX.md) ✅
- **Deploy?** → Read [GETTING_STARTED.md](GETTING_STARTED.md) deployment section ✅
- **Help a teammate?** → Point them to this file! ✅

---

## 📞 Got Stuck?

1. **Check [PROJECT_INDEX.md](PROJECT_INDEX.md)** - Find the code
2. **Search the code** - `grep -r "something" .`
3. **Read test files** - They show how to use everything
4. **Run with verbose** - `pytest -v -s`
5. **Check git history** - `git log -p filename`

---

## 🎉 Welcome to Life Sprint!

Everything is organized, tested, and documented. You've got all the tools you need.

**Next step:** Pick a path above and dive in! 🚀

---

**Questions?** Check:
- [STRUCTURE.md](STRUCTURE.md) - Folder organization
- [PROJECT_INDEX.md](PROJECT_INDEX.md) - Find files
- [CHEAT_SHEET.md](CHEAT_SHEET.md) - Code patterns
- Test files - See how things work
- Git history - See what changed

Happy coding! 🌟
