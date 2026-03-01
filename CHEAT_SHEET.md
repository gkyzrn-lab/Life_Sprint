# 🛠️ Developer Cheat Sheet

> Quick reference for common development tasks. Print this out!

---

## 🎯 Most Important Files to Know

| File | Purpose | Edit When |
|------|---------|-----------|
| `main.py` | App startup & router registration | Adding new routers |
| `core_domain/store.py` | Database (STORE object) | Switching to real DB |
| `core_domain/config.py` | Game constants & tuning | Changing game balance |
| `core_domain/player/player_model.py` | Player data structure | Adding player attributes |
| `api/router_player.py` | Example: perfect endpoint | Learning how to write endpoints |
| `finance/service.py` | Example: complex business logic | Learning how to write services |
| `tests/test_player.py` | Example: good tests | Learning how to test |

---

## 🚀 Startup Commands (Copy & Paste)

### Terminal 1: Backend
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
source .venv/bin/activate
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Terminal 2: Frontend
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint/life-sprint-frontend
npm run dev
```

### Terminal 3: Tests (watch mode)
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
source .venv/bin/activate
pytest -v --tb=short --looponfail
```

---

## 📝 Common Code Patterns

### Pattern 1: Add an Endpoint
```python
# File: api/router_something.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core_domain.store import STORE

router = APIRouter(prefix="/something", tags=["something"])

class MyRequest(BaseModel):
    player_id: str
    amount: float

@router.post("/do-something")
def do_something(req: MyRequest):
    # 1. Get player from STORE
    player = STORE.require_player(req.player_id)
    
    # 2. Call service logic
    from something.service import my_logic
    result = my_logic(player, req.amount)
    
    # 3. Save player
    STORE.put_player(player)
    
    # 4. Return response
    return {"status": "ok", "result": result}
```

### Pattern 2: Write a Service
```python
# File: something/service.py

from fastapi import HTTPException
from core_domain.player.player_model import Player, HistoryEvent
from core_domain.utils import safe_details

def my_logic(player: Player, amount: float) -> float:
    """Do something with player and return result."""
    
    # 1. Validate
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    
    # 2. Change player state
    player.finance.balance += amount
    
    # 3. Log to history
    player.history.append(
        HistoryEvent(
            label="My Logic Applied",
            semester=player.semester,
            details=safe_details({"amount": amount})
        )
    )
    
    # 4. Return result
    return player.finance.balance
```

### Pattern 3: Write a Test
```python
# File: tests/test_something.py

import pytest
from core_domain.store import STORE
from core_domain.player.player_model import Player
from something.service import my_logic

@pytest.fixture(autouse=True)
def cleanup():
    """Clear STORE before each test."""
    STORE.players.clear()
    yield
    STORE.players.clear()

def test_my_logic():
    # 1. Setup
    player = Player(id="test1", name="Test", ...)
    STORE.put_player(player)
    
    # 2. Execute
    result = my_logic(player, 100)
    
    # 3. Assert
    assert result > 0
    assert player.finance.balance == 5100  # if starting at 5000
    
    # 4. Verify saved
    loaded = STORE.get_player("test1")
    assert loaded.finance.balance == 5100
```

### Pattern 4: Validate Catalog IDs
```python
# Always validate before using catalog data!

from catalogs.colleges import COLLEGES
from fastapi import HTTPException

def validate_college(college_id: str):
    if college_id not in COLLEGES:
        available = ', '.join(sorted(COLLEGES.keys()))
        raise HTTPException(
            status_code=422,
            detail=f"Invalid college_id '{college_id}'. Available: {available}"
        )

# Then use it
validate_college("cuny_baruch")
college = COLLEGES["cuny_baruch"]
```

---

## 🧪 Testing Commands

```bash
# Run all tests
pytest -q

# Run with verbose output
pytest -v

# Run one file
pytest tests/test_player.py -v

# Run one test
pytest tests/test_player.py::test_start_player -v

# Run and show print statements
pytest -v -s

# Run and stop on first failure
pytest -x

# Run with coverage
pytest --cov=. --cov-report=html

# Watch mode (re-run on file change)
pytest-watch -n

# Show slowest tests
pytest --durations=10
```

---

## 🐛 Debugging Tricks

### Print debugging
```python
print(f"DEBUG: value = {value}")
pytest -v -s  # Run tests with print output
```

### Use breakpoint (Python 3.7+)
```python
breakpoint()  # Pauses execution, opens debugger
```

### Check what's in STORE
```python
from core_domain.store import STORE
print(STORE.players.keys())  # All player IDs
```

### Test a single scenario
```python
# In Python REPL:
from core_domain.store import STORE
from api.router_player import start_player
from pydantic import BaseModel

result = start_player({
    "name": "Test",
    "college_id": "cuny_baruch",
    "major_id": "finance"
})
print(result.id)
```

### See all routes registered
```bash
curl http://localhost:8000/  # See all routes with methods
```

---

## 📊 File Statistics

**Run this to see project stats:**
```bash
# Count all Python files
find . -name "*.py" -type f | wc -l

# Count all lines of code
find . -name "*.py" -type f -exec wc -l {} + | tail -1

# Count tests only
find tests/ -name "*.py" -type f -exec wc -l {} + | tail -1

# See file sizes
du -sh core_domain/ api/ finance/ academics/
```

---

## 🔄 Git Workflow

```bash
# See current status
git status

# See recent changes
git log --oneline -10

# Add all changes
git add -A

# Commit
git commit -m "feat: add new feature

- Detailed description
- What changed
- Why it changed"

# Push
git push origin main

# See diff before committing
git diff
```

---

## 🎯 Performance Tips

```python
# ❌ Bad: Loop and append
for item in items:
    player.history.append(item)  # Slow!

# ✅ Good: Use extend
player.history.extend(items)  # Fast!

# ❌ Bad: Lookup in list
if item in large_list:  # O(n)
    pass

# ✅ Good: Use dict/set
if item in items_set:  # O(1)
    pass
```

---

## 🚨 Common Mistakes to Avoid

| ❌ Don't | ✅ Do | Why |
|---------|------|-----|
| `STORE.players[id]` | `STORE.require_player(id)` | Better error handling |
| `import *` | `from module import X` | Clearer dependencies |
| Hardcode IDs | Use catalog lookups | Data consistency |
| Skip validation | Validate all input | Security & stability |
| Mutate without saving | `STORE.put_player()` | Persist changes |
| Side effects in imports | Keep imports clean | App startup resilience |

---

## 📚 Documentation to Read

1. **[STRUCTURE.md](STRUCTURE.md)** - Folder organization
2. **[GETTING_STARTED.md](GETTING_STARTED.md)** - Setup & basics
3. **[API_REFERENCE.md](API_REFERENCE.md)** - All endpoints
4. **This file** - Development patterns

---

## 💡 Pro Commands

### Kill stuck processes
```bash
# Find processes
ps aux | grep -E "uvicorn|vite"

# Kill by name
pkill -f uvicorn
pkill -f vite
pkill -f "npm run dev"
```

### Check if ports are in use
```bash
lsof -i :8000    # Backend
lsof -i :3000    # Frontend
lsof -i :5173    # Vite dev server
```

### Start everything at once
```bash
# Terminal 1
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
source .venv/bin/activate
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000 &

# Terminal 2
cd /Users/oktaygokayzeren/Desktop/Life_Sprint/life-sprint-frontend
npm run dev &

# Terminal 3 (optional tests)
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
source .venv/bin/activate
pytest -v --tb=short
```

### Quick test curl script
```bash
#!/bin/bash
PLAYER_ID=$(curl -s -X POST http://localhost:8000/player/start \
  -H 'Content-Type: application/json' \
  -d '{
    "name":"TestPlayer",
    "college_id":"cuny_baruch",
    "major_id":"finance",
    "hs_gpa":3.5,
    "parent_income":70000,
    "starting_balance":5000,
    "housing_option_id":"dorm"
  }' | python -c "import sys,json; print(json.load(sys.stdin)['id'])")

echo "Created player: $PLAYER_ID"

# Test endpoint
curl http://localhost:8000/player/$PLAYER_ID
```

---

## ✅ Pre-Commit Checklist

Before pushing code:

- [ ] Tests pass: `pytest -q`
- [ ] No import errors: `python -c "import main"`
- [ ] Code follows patterns
- [ ] Functions have docstrings
- [ ] No `print()` left for debugging
- [ ] Commit message is clear
- [ ] All related tests updated

---

## 🎓 Learning Order

1. **Week 1**: Read STRUCTURE.md, GETTING_STARTED.md, run the app
2. **Week 2**: Read & understand main.py, core_domain/, one test file
3. **Week 3**: Write a test for existing code
4. **Week 4**: Add a new endpoint
5. **Week 5**: Add a new feature end-to-end

---

## 📞 Quick Help

**"How do I...?"**

- Add an endpoint? → Copy `api/router_player.py` as template
- Fix a test? → `pytest tests/test_file.py::test_name -v`
- See what changed? → `git diff`
- Find a function? → `grep -r "function_name" .`
- Check API? → Visit `http://localhost:8000/docs`
- See errors? → Check terminal where server runs, check F12 in browser
- Import something? → Find it, check if it's exported in `__init__.py`

---

**Print this out and keep it on your desk!** 🖨️
