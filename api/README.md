# 🔌 API Routes - REST Endpoints

All HTTP endpoints that the frontend (and external apps) can call.

## 🏗️ Structure

```
api/
├── router_player.py                 ← Player lifecycle (create, load)
├── router_onboarding.py             ← New player experience
├── router_planning.py               ← Plans, housing, jobs, emergencies
├── router_finance.py                ← Loans, borrowing, repayment
├── router_exams.py                  ← Exams, grading, results
├── router_curriculum.py             ← Courses, curriculum, mini-games
├── router_progression.py            ← Semesters, graduation, leveling
├── router_career.py                 ← Career paths, job matching
├── router_health.py                 ← Wellness, stress management
├── router_analytics.py              ← Dashboards, leaderboards, achievements
├── router_community.py              ← Study groups, guilds, projects
├── router_mentorship.py             ← Mentor relationships
├── router_social.py                 ← Social features, relationships
├── router_housing_market.py         ← Housing options
├── router_side_gigs.py              ← Side jobs, income
├── router_store.py                  ← In-game shop, cosmetics
├── router_difficulty.py             ← Difficulty settings
├── router_catalogs.py               ← Static data (colleges, majors, etc)
├── router_major_exploration.py      ← Try different majors
├── router_career_recommendations.py ← Smart recommendations
├── router_market_intelligence.py    ← Market data, trends
├── router_financial_responsibility.py ← Financial literacy
├── router_tutorial.py               ← Tutorial games
├── deps.py                          ← Shared dependencies
└── __init__.py
```

## 🎯 How Routers Work

Each router file handles one feature area:

```python
# File: api/router_something.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core_domain.store import STORE

router = APIRouter(prefix="/something", tags=["something"])

class MyRequest(BaseModel):
    """Data coming FROM the client"""
    player_id: str
    amount: float

@router.post("/do-something")
def do_something(req: MyRequest):
    """
    Endpoint that does something.
    
    1. Validate request (FastAPI does this automatically)
    2. Get player from STORE
    3. Call service logic
    4. Save player
    5. Return response
    """
    
    # 1. Get player (will 404 if not found)
    player = STORE.require_player(req.player_id)
    
    # 2. Call service
    from something.service import my_logic
    result = my_logic(player, req.amount)
    
    # 3. Save
    STORE.put_player(player)
    
    # 4. Return
    return {
        "status": "ok",
        "result": result,
        "new_balance": player.finance.balance
    }
```

## 🔑 Important Routers to Know

### `router_player.py` - START HERE
- `POST /player/start` - Create new player
- `GET /player/{player_id}` - Get player details

**Why important?** Every game session starts here. Model for all other routers.

### `router_planning.py`
- `POST /planning/save-plan` - Save draft plan
- `POST /planning/lock-plan` - Lock plan for semester
- `POST /planning/emergency-change` - Mid-semester changes

**Why important?** Core gameplay loop depends on planning.

### `router_finance.py`
- `POST /finance/borrow` - Borrow for semester
- `POST /finance/repay` - Make loan payments
- `GET /finance/{player_id}` - View finances

**Why important?** Complex calculations, critical for game balance.

### `router_exams.py`
- `POST /exams/generate` - Generate exam questions
- `POST /exams/grade` - Grade submitted exam
- `POST /exams/grade-with-feedback` - Grade with feedback

**Why important?** Academic progression system.

## 📋 Common Endpoint Patterns

### Pattern 1: Simple Get
```python
@router.get("/{item_id}")
def get_item(item_id: str):
    # Just return data, no player modification
    return {"id": item_id, "data": "..."}
```

### Pattern 2: Player Action
```python
@router.post("/action")
def do_action(req: MyRequest):
    player = STORE.require_player(req.player_id)
    # ... modify player ...
    STORE.put_player(player)
    return {"status": "ok", "player": player}
```

### Pattern 3: List Items
```python
@router.get("/items")
def list_items(player_id: str):
    # Return list of items
    return {"items": [...]}
```

### Pattern 4: Validation
```python
@router.post("/something")
def do_something(req: MyRequest):
    # Validate catalog IDs
    if req.housing_id not in HOUSING_OPTIONS:
        raise HTTPException(status_code=404, detail="Housing not found")
    
    # Validate player
    if not STORE.get_player(req.player_id):
        raise HTTPException(status_code=404, detail="Player not found")
    
    # Continue...
```

## 🔄 Request/Response Pattern

**Request (from frontend):**
```python
class MyRequest(BaseModel):
    player_id: str = Field(..., description="Player ID")
    amount: float = Field(..., gt=0, description="Positive amount")
```

**Response (to frontend):**
```python
return {
    "status": "ok",
    "message": "Operation successful",
    "data": {...},
    "player": player.model_dump()
}
```

## 🧪 Testing Routers

```bash
# Test with curl
curl -X POST http://localhost:8000/player/start \
  -H 'Content-Type: application/json' \
  -d '{"name":"Test","college_id":"cuny_baruch","major_id":"finance"}'

# Test with Python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
response = client.post("/player/start", json={...})
assert response.status_code == 200
```

## ✅ Checklist: Adding a New Router

1. [ ] Create `api/router_newfeature.py`
2. [ ] Define request/response Pydantic models
3. [ ] Write endpoint functions with `@router.get/post/put/delete`
4. [ ] Import and validate catalog IDs if needed
5. [ ] Call service logic from appropriate service module
6. [ ] Save to STORE if modifying player
7. [ ] Add proper error handling (HTTPException)
8. [ ] Register router in `main.py` with `_try_include`
9. [ ] Write tests in `tests/test_newfeature.py`
10. [ ] Test with curl or Swagger UI (`/docs`)

## 🔗 Connecting Parts

```
Frontend Request
    ↓
api/router_*.py (validation, input parsing)
    ↓
service_module/service.py (business logic)
    ↓
core_domain models (data structures)
    ↓
catalogs/*.py (static data lookup)
    ↓
STORE (save/load)
    ↓
Response to Frontend
```

## 💡 Common Mistakes

| ❌ Don't | ✅ Do | Why |
|---------|------|-----|
| Forget `STORE.put_player()` | Always save after modify | Changes persist |
| Use `STORE.players` directly | Use `STORE.require_player()` | Proper error handling |
| No input validation | Validate in Pydantic models | Security & UX |
| Missing docstrings | Add docstrings | API docs auto-generated |
| Silent failures | Raise HTTPException | Client knows what failed |
| Hardcode IDs | Look up in catalogs | Data integrity |

## 🐛 Debugging Routers

```python
# Add debug prints (use -s flag in tests)
print(f"DEBUG: player = {player}")
print(f"DEBUG: balance = {player.finance.balance}")

# Use breakpoint() for interactive debugging
breakpoint()  # Pauses execution

# Check router was registered
curl http://localhost:8000/  # See all routes
```

## 📚 View API Documentation

While backend is running:
```
http://localhost:8000/docs
```

Click any endpoint to:
- See parameters
- See response structure
- Try it out with test data

## 🎯 Best Practices

✅ **DO:**
- Keep routers thin (mostly validation & calling services)
- Use Pydantic for all request/response types
- Validate player_id exists before proceeding
- Raise HTTPException for errors
- Return meaningful error messages
- Add docstrings to all endpoints

❌ **DON'T:**
- Put business logic in routers
- Access database directly (use STORE)
- Forget to save player with `put_player()`
- Return raw exceptions (use HTTPException)
- Skip input validation
- Mix concerns (router + service + models)

## 📖 Related Documentation

- **Service Logic?** → See `finance/service.py`, `planning/service.py`
- **Data Models?** → See `core_domain/player/player_model.py`
- **Testing?** → See `tests/test_player.py`
- **Static Data?** → See `catalogs/`
- **API Usage?** → See [API_REFERENCE.md](../API_REFERENCE.md)
