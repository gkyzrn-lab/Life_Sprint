# 🚀 Getting Started with Life Sprint

> **New to this project?** Start here! This guide will have you up and running in 5 minutes.

---

## ⚡ Super Quick Start (5 Minutes)

### **Step 1: Start the Backend (Terminal 1)**
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
source .venv/bin/activate
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
✅ You'll see: `Uvicorn running on http://127.0.0.1:8000`

### **Step 2: Start the Frontend (Terminal 2)**
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint/life-sprint-frontend
npm run dev
```
✅ You'll see: `Local: http://localhost:3000`

### **Step 3: Open in Browser**
- Go to **http://localhost:3000**
- Create a player and start playing!

### **Step 4: Run Tests (Terminal 3, Optional)**
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
source .venv/bin/activate
pytest -q
```
✅ You'll see: `676 passed in 0.XX s`

**That's it!** 🎉 Your game is running!

---

## 📋 Installation (First Time Only)

### **Prerequisites**
- Python 3.9+ (check: `python --version`)
- Node.js 18+ (check: `node --version`)
- Git (check: `git --version`)

### **Backend Setup**
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint

# Create virtual environment (if needed)
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Install Python packages
pip install -r requirements.txt
```

### **Frontend Setup**
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint/life-sprint-frontend

# Install Node packages
npm install
```

---

## 🎮 What You Can Do Now

### **As a Player**
- Create your character
- Enroll in college
- Take courses and mini-games
- Plan semesters (housing, job, activities)
- Manage finances and loans
- Track your progress

### **As a Developer**
- ✅ All 676 tests pass
- ✅ Backend API fully functional
- ✅ Frontend fully responsive
- ✅ Ready to add new features

---

## 📁 Project Structure (Quick Map)

**Need to find something?** Read these in order:

1. **[STRUCTURE.md](STRUCTURE.md)** ← Detailed folder guide (read this!)
2. **main.py** ← How the app starts
3. **core_domain/store.py** ← Where data lives
4. **api/router_player.py** ← Example of an endpoint

---

## 🐛 Troubleshooting

### **Backend won't start**
```bash
# Kill any old processes
pkill -f uvicorn

# Try again
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### **Frontend won't start**
```bash
# Kill any old processes
pkill -f vite

# Try again
npm run dev
```

### **Port already in use**
```bash
# Find what's using port 8000
lsof -i :8000

# Kill it (replace 12345 with the PID)
kill -9 12345
```

### **Import errors or weird behavior**
```bash
# Make sure you're in the virtual environment
which python  # Should show .venv/bin/python

# Reinstall everything
pip install -r requirements.txt --force-reinstall
```

### **Tests failing**
```bash
# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_player.py -v
```

---

## 📚 Learning Path

### **30 Minutes**: Understand the basics
1. Read [STRUCTURE.md](STRUCTURE.md) (10 min)
2. Open [main.py](main.py) and read comments (5 min)
3. Skim [core_domain/models.py](core_domain/models.py) (5 min)
4. Skim [api/router_player.py](api/router_player.py) (5 min)
5. Skim [finance/service.py](finance/service.py) (5 min)

### **1 Hour**: Run your first test
1. Run: `pytest tests/test_player.py -v`
2. Read the test file: [tests/test_player.py](tests/test_player.py)
3. Change something in [core_domain/player/player_model.py](core_domain/player/player_model.py)
4. Run test again, see it fail
5. Revert change, see it pass

### **2 Hours**: Make your first change
1. Add a new endpoint in [api/router_player.py](api/router_player.py)
2. Test it with: `curl http://localhost:8000/player/health`
3. Write a test for it in [tests/test_player.py](tests/test_player.py)
4. Run `pytest -v` to verify

---

## 🔑 Key Concepts

### **Player (The Core Object)**
- Everything about a player lives in `core_domain/player/player_model.py`
- Changes made via services like `finance/service.py`
- Saved to STORE with `STORE.put_player(player)`
- Retrieved with `STORE.get_player(player_id)`

### **Services (The Business Logic)**
- Each feature has a service module
- Example: `finance/service.py`, `planning/service.py`, `academics/exam_service.py`
- Services mutate Player objects and handle calculations
- Routers call services to handle requests

### **Routers (The Endpoints)**
- Each feature has a router in `api/router_*.py`
- Routers validate input and call services
- Return JSON responses to the frontend
- Use HTTP methods: GET (read), POST (create), PUT (update), DELETE (remove)

### **Catalogs (The Static Data)**
- Colleges, jobs, houses, majors, etc.
- Loaded once at startup
- Never change during gameplay
- Used for validation and lookup

### **STORE (The Database)**
- In-memory for development
- Simple API: `STORE.put_player(p)` and `STORE.get_player(id)`
- Ready to swap for a real database later

---

## 🧪 Testing Quick Reference

```bash
# Run all tests
pytest -q

# Run with verbose output
pytest -v

# Run one file
pytest tests/test_player.py -v

# Run one test function
pytest tests/test_player.py::test_start_player -v

# Run with coverage report
pytest --cov=.

# Run and stop on first failure
pytest -x
```

---

## 🌐 API Quick Reference

### **Player Endpoints**
```
POST   /player/start              ← Create new player
GET    /player/{player_id}        ← Get player details
```

### **Planning Endpoints**
```
POST   /planning/save-plan        ← Save a semester plan
POST   /planning/lock-plan        ← Lock plan for semester
POST   /planning/emergency-change ← Mid-semester changes
GET    /planning/{player_id}/plan ← Get current plan
```

### **Finance Endpoints**
```
POST   /finance/borrow            ← Borrow for semester
POST   /finance/repay             ← Make loan payments
GET    /finance/{player_id}       ← View finances
```

### **Curriculum Endpoints**
```
GET    /curriculum/course/{course_id}     ← Course details
GET    /curriculum/games/{game_id}        ← Mini-game info
POST   /curriculum/games/submit           ← Submit game answers
```

### **More Endpoints?**
Go to **http://localhost:8000/docs** while backend is running. 📖

---

## 💡 Pro Tips

1. **Explore the API docs**: Visit `http://localhost:8000/docs` while backend runs
2. **Check browser console**: Press F12 → Console tab to see frontend errors
3. **View backend logs**: Look at terminal where backend is running
4. **Use curl for quick tests**: `curl http://localhost:8000/health`
5. **Read test files**: They show how to use every function
6. **Git workflow**: Always commit working code!

---

## 📞 Getting Help

1. **Check [STRUCTURE.md](STRUCTURE.md)** for folder layout
2. **Read the test file** for the feature you're working on
3. **Search the code** for similar implementations
4. **Check git history**: `git log --oneline` to see past changes
5. **Run with verbose flags**: `pytest -v`, `python -c "import X; print(X)"`

---

## ✅ Verify Everything Works

```bash
# 1. Tests pass
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
source .venv/bin/activate
pytest -q

# 2. Backend starts
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000 &
sleep 2
curl http://localhost:8000/health

# 3. Frontend builds
cd life-sprint-frontend
npm run build

# 4. Kill background processes
pkill -f uvicorn
```

Everything working? You're all set! 🎉

---

## 🚀 Next Steps

1. **Read [STRUCTURE.md](STRUCTURE.md)** to understand folders
2. **Start the app** (Backend + Frontend)
3. **Create a player** and play a bit
4. **Run the tests** to see everything passes
5. **Pick a feature** and read its code
6. **Make a small change** and test it

**You're ready to contribute to Life Sprint!** 🌟
