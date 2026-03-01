# 📚 Core Domain - The Game Heart

This is the most important folder in the entire project. It contains all core game state, data models, and constants.

## 🏗️ What's Here

- **Player State**: Everything about a player (stats, finance, housing, etc.)
- **Game Rules**: Constants, calculations, business logic
- **Database**: In-memory store for development
- **Data Models**: Pydantic models for type safety

## 📁 Structure

```
core_domain/
├── player/                    ← Player data & management
│   ├── player_model.py        ← Main Player class (START HERE!)
│   └── player_stats.py        ← Stress, happiness, burnout
├── finance/                   ← Financial data models
│   ├── finance_models.py      ← Loans, balance, expenses
│   └── repayment_models.py    ← Repayment plans
├── planning/
│   └── planning_models.py     ← Semester plans
├── stats/
│   └── stats_model.py         ← GPA, skill scores
├── models.py                  ← Legacy aggregator
├── store.py                   ← 🔑 IN-MEMORY DATABASE
├── config.py                  ← 🔑 GAME CONSTANTS
└── utils.py                   ← Helper functions
```

## 🔑 Key Files

### `player/player_model.py`
**Most important file in the entire project!**
- Defines the `Player` class
- Contains all player attributes
- Used everywhere

Example:
```python
from core_domain.player.player_model import Player

player = Player(id="123", name="John", ...)
player.finance.balance = 5000
```

### `store.py`
**The database for development**

```python
from core_domain.store import STORE

# Save player
STORE.put_player(player)

# Load player
player = STORE.require_player("player_id")  # Raises if not found
player = STORE.get_player("player_id")      # Returns None if not found
```

### `config.py`
**Game tuning & constants**

Change these to balance the game:
- `WEEKLY_TIME_BUDGET` - Max hours per week
- `SEM_MONTHS` - Months per semester
- `MAX_STRESS` - Max stress value
- `DEFAULT_START_BALANCE` - Starting money
- `DEFAULT_BASE_MONTHLY_NONHOUSING_EXPENSES` - Monthly costs

## 🎮 How It All Works

```
API Request
    ↓
Router (api/router_*.py)
    ↓
Service (finance/service.py, etc.)
    ↓
Mutates Player object
    ↓
STORE.put_player(player)  ← Save to database
```

## 💾 Understanding STORE

```python
# In-memory database for development
STORE.players = {
    "player_id_1": Player(...),
    "player_id_2": Player(...),
}

# Usage:
player = STORE.require_player("player_id_1")  # Gets player or raises error
player = STORE.get_player("player_id_1")      # Gets player or None
STORE.put_player(player)                       # Saves player
```

**Note**: Ready to upgrade to real database? Just replace STORE implementation without changing callers!

## 🏆 Important Patterns

### Pattern 1: Modifying a Player
```python
from core_domain.store import STORE

player = STORE.require_player("player_id")
player.finance.balance += 100
player.stats.stress -= 5
STORE.put_player(player)  # MUST save!
```

### Pattern 2: Validating Enum Values
```python
from core_domain.finance.finance_models import LoanType

loan_type = LoanType.subsidized  # Type-safe!
```

### Pattern 3: Creating History Records
```python
from core_domain.player.player_model import HistoryEvent
from core_domain.utils import safe_details

player.history.append(
    HistoryEvent(
        label="Did Something",
        semester=player.semester,
        details=safe_details({
            "key": "value",
            "amount": 100.50
        })
    )
)
```

## 📊 Data Models at a Glance

| Model | File | Purpose |
|-------|------|---------|
| `Player` | `player/player_model.py` | Main player object |
| `Stats` | `player/player_stats.py` | GPA, stress, happiness |
| `Finance` | `finance/finance_models.py` | Balance, loans, expenses |
| `Loan` | `finance/finance_models.py` | Individual loan |
| `SemesterPlan` | `planning/planning_models.py` | Semester plan with housing/job |

## 🧪 Testing Core Domain

All core domain tests are in `tests/test_player.py`, `tests/test_finance.py`, etc.

```bash
# Test core domain
pytest tests/test_player.py -v
pytest tests/test_finance.py -v
```

## ✅ Checklist for Adding Player Attributes

If you want to add a new attribute to Player:

1. [ ] Edit `core_domain/player/player_model.py`
2. [ ] Add field to `Player` class
3. [ ] Initialize it in `__init__` or default
4. [ ] Update any services that need to use it
5. [ ] Add test in `tests/test_player.py`
6. [ ] Update routers that return Player

## 🚀 Best Practices

✅ **DO:**
- Load players with `STORE.require_player(id)`
- Save players with `STORE.put_player(player)`
- Use enums for fixed values (LoanType, RepaymentPlanType)
- Add HistoryEvent records when changing player state
- Validate all calculations

❌ **DON'T:**
- Access `STORE.players` directly (use methods)
- Create Player objects without proper initialization
- Modify player without calling `STORE.put_player()`
- Hardcode magic numbers (use `config.py`)
- Skip validation of user input

## 🔗 Related Files

- **Using finance?** → `finance/service.py`, `finance/calculators.py`
- **Using planning?** → `planning/service.py`
- **Using academics?** → `academics/exam_service.py`
- **Testing?** → `tests/test_*.py`

## 📖 Read Next

1. [Player Model](./player/player_model.py) - Core Player class
2. [Store](./store.py) - Database system
3. [Config](./config.py) - Game constants
4. [Finance Models](./finance/finance_models.py) - Loan structures
