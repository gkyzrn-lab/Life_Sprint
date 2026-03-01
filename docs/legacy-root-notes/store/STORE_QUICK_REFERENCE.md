# Store System - Quick Reference

## Running the System

### Start Backend
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
source .venv/bin/activate
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Run Demos
```bash
python store_demo.py
```

## API Quick Reference

### Get Available Purchases
```bash
curl "http://localhost:8000/api/store/available?player_id=player1" | jq
```

### Buy Something
```bash
curl -X POST "http://localhost:8000/api/store/purchase/coffee_with_friends?player_id=player1" | jq
```

### View Purchase History
```bash
curl "http://localhost:8000/api/store/history?player_id=player1" | jq
```

### Get Suggestions
```bash
curl "http://localhost:8000/api/store/suggestions?player_id=player1" | jq
```

## All 18 Purchases

### Semester 1 (10 available)
1. ☕ Coffee with Friends - $15
2. 🍽️ Dinner with Friends - $40
3. 🎵 Concert Tickets - $85
4. 🍿 Movie Night - $25
5. 💪 Gym Membership - $120
6. 🧠 Therapy Sessions - $300
7. 🧖 Spa Day - $150
8. 🧘 Meditation App - $60
9. 💻 Quality Laptop - $1200
10. 🥗 Nutritionist Consultation - $200

### Semester 2+ (8 more)
11. 🚗 Used Car - $8000
12. 🏠 Better Apartment - $5000
13. 👔 Professional Wardrobe - $500
14. 🎓 Online Course - $200
15. ✈️ Weekend Getaway - $600
16. 🎮 Gaming Console - $400
17. ⛺ Weekend Camping - $200
18. 🎸 Music Lessons - $250

## Key Stats Affected

| Stat | Affected By |
|------|-------------|
| stress | Coffee, concert, spa, vacation, gym, therapy, laptop, etc. |
| happiness | Dinner, concert, movie, gym, spa, vacation, gaming, etc. |
| mental_health | Therapy, spa, meditation, apartment, camping, etc. |
| fitness | Gym, nutrition, spa |
| eq (emotional) | Coffee, dinner, therapy, meditation, music, etc. |
| energy_level | Concert, spa, gym, vacation, nutrition, etc. |
| technical_skills | Laptop, online course |
| communication_skills | Wardrobe, music lessons |
| time_management | Laptop, car |

## Purchase Rules

### Affordability
- Must have enough money to buy
- Returns error if balance < cost

### One-Time Purchases
- Can only buy once per playthrough: car, laptop, apartment, gaming console
- Trying to buy again returns error

### Max Per Semester
- Coffee: 4 times max per semester
- Dinner: 2 times max per semester
- Concert: 1 time max per semester
- Movie: 3 times max per semester
- Gym: 1 time max per semester
- Therapy: 1 time max per semester
- Spa: 1 time max per semester
- Others: no max (repeatable)

### Semester Unlocking
- Sem 1: 10 items available
- Sem 2+: All 18 items available
- Car unlocks semester 2
- Vacation unlocks semester 2
- Music lessons unlock semester 3

## Effects Example

**Coffee with Friends ($15)**
- stress: -5
- happiness: +10
- eq: +2
- mental_health: +5

**Gym Membership ($120/sem)**
- fitness: +20
- stress: -10
- energy_level: +15
- mental_health: +12
- happiness: +8

**Used Car ($8000, one-time)**
- stress: -5
- happiness: +10
- time_management: +5

## Smart Suggestions Logic

The system suggests purchases based on current stats:

```python
if stress > 70:
    suggest stress_relief_items()
if happiness < 50:
    suggest fun_items()
if fitness < 40:
    suggest health_items()
if mental_health < 50:
    suggest wellness_items()
```

## File Structure

```
Life_Sprint/
├── catalogs/
│   └── life_purchases.py       # 18 purchase definitions
├── store/
│   ├── __init__.py
│   └── purchase_service.py     # Purchase logic
├── api/
│   └── router_store.py         # 6 API endpoints
├── store_demo.py               # 7 demo scenarios
└── LIFE_PURCHASES_COMPLETE.md  # This guide
```

## Important Notes

1. **All purchases in player history** - Every purchase is recorded with effects
2. **Stat clamping** - Stats automatically clamp to valid ranges (0-100)
3. **Purchase immediately affects stats** - No delays or cooldowns
4. **Balance changes immediately** - Money deducted on purchase
5. **No refunds** - Purchases are final (unless you implement undo)

## Troubleshooting

### "Insufficient funds" error
- Player doesn't have enough money
- Need to earn via side gigs, jobs, scholarships
- Check: `player.finance.balance`

### "You've already purchased this" error
- It's a one-time purchase (car, laptop, etc.)
- Can't buy it again in same playthrough

### "Purchase not available yet" error
- Item locked to later semester
- Try again in semester 2+
- Check: `purchase.requires_semester_min`

### "You've reached the limit for this item" error
- Already bought max per semester (e.g., coffee = 4/sem)
- Try again next semester

## Integration Example

```python
# In your game loop:
from store.purchase_service import make_purchase
from core_domain.store import STORE

player = STORE.get_player("player_id")

# Try to buy something
result = make_purchase(player, "coffee_with_friends")

if result.success:
    STORE.put_player(player)  # Save changes
    print(f"✅ {result.message}")
else:
    print(f"❌ {result.message}")  # Tell user why it failed
```

## Testing Commands

```bash
# Check all imports work
python -c "from catalogs.life_purchases import LIFE_PURCHASES; print(len(LIFE_PURCHASES))"

# Check store service
python -c "from store.purchase_service import make_purchase; print('✅')"

# Check API router
python -c "from api.router_store import router; print(len(router.routes))"

# Check app startup
python -c "from main import app; print(f'Routes: {len(app.routes)}')"

# Run full test suite
python store_demo.py
```

---

**Total System**: 18 purchases, 6 API endpoints, 7 demos, ✅ tested and working
