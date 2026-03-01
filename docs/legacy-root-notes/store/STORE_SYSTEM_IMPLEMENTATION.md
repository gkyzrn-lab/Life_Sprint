# Life Purchases Store System - Implementation Guide

## Overview

The **Life Purchases Store** is a real-world spending system that allows players to buy items that directly affect their stats and wellbeing. This creates **responsive money spending** where every purchase has meaningful consequences on gameplay.

## Architecture

### Core Components

1. **`catalogs/life_purchases.py`** - Static catalog of all purchasable items
   - 17 items across 6 categories
   - Modular `PurchaseEffect` system for flexible stat changes
   - Supports one-time purchases and repeatable items
   - Semester-based unlocking system

2. **`store/purchase_service.py`** - Business logic for purchases
   - Purchase validation (affordability, limits, requirements)
   - Effect application to player stats
   - Purchase history tracking
   - Smart suggestions based on player's current stats

3. **`api/router_store.py`** - REST API endpoints
   - List available purchases
   - Execute purchases
   - View purchase history
   - Get category information
   - Get smart suggestions

## Available Purchases (17 items)

### Social Category (4 items)
Improve happiness, reduce stress, build emotional connections.

| Item | Cost | Effects | Repeatable | Notes |
|------|------|---------|-----------|-------|
| Coffee with Friends ☕ | $15 | stress -5, happiness +10, eq +2, mental_health +5 | Yes, 4/sem | Budget-friendly way to relax |
| Dinner with Friends 🍽️ | $40 | stress -8, happiness +15, eq +4, mental_health +8, energy +5 | Yes, 2/sem | More substantial social activity |
| Concert Tickets 🎵 | $85 | stress -12, happiness +25, energy +10, mental_health +10 | Yes, 1/sem | Major stress relief & fun |
| Movie Night 🎬 | $25 | stress -4, happiness +8, energy +3 | Yes, 3/sem | Casual entertainment |

### Health Category (5 items)
Improve fitness, energy, and physical wellbeing.

| Item | Cost | Effects | Repeatable | Notes |
|------|------|---------|-----------|-------|
| Gym Membership 💪 | $120/sem | fitness +20, stress -10, energy +15, mental_health +12, happiness +8 | Yes, 1/sem | Ongoing fitness & stress relief |
| Therapy Sessions 🧠 | $300 | mental_health +20, stress -15, eq +8, happiness +12 | Yes, 1/sem | Professional mental health support |
| Spa Day 🧖 | $150 | stress -20, mental_health +15, happiness +18, energy +8 | Yes, 1/sem | Ultimate stress relief |
| Meditation App 🧘 | $60/year | stress -8, mental_health +15, eq +5 | Yes, 1/sem | Daily mental health tool |
| Nutritionist Session 🥗 | $200 | fitness +8, energy +10, mental_health +8, stress -5 | Yes, 1/sem | Professional nutrition guidance |

### Practical Category (3 items)
Major investments with long-term benefits.

| Item | Cost | Effects | Repeatable | Notes |
|------|------|---------|-----------|-------|
| Used Car 🚗 | $8000 | stress -5, happiness +10, time_management +5 | No, 1 total | Significant financial commitment |
| Laptop 💻 | $1200 | time_management +8, stress -3, technical_skills +2 | No, 1 total | Improves productivity & skills |
| Apartment Upgrade 🏠 | $5000 | mental_health +15, happiness +12, sleep_quality +10, stress -8 | No, 1 total | Big quality of life improvement |

### Self-Care/Fun Category (5 items)
Recreation and personal development.

| Item | Cost | Effects | Repeatable | Notes |
|------|------|---------|-----------|-------|
| Professional Wardrobe 👔 | $500 | communication_skills +5, happiness +8, stress -3 | Yes, 1/sem | Boost confidence in social/work |
| Online Course 📚 | $200 | technical_skills +8, business_acumen +6, happiness +5 | Yes, 2/sem | Skill development & career prep |
| Vacation 🌴 | $600 | stress -25, mental_health +25, happiness +20, energy +20, eq +5 | Yes, 1/sem | Ultimate stress relief & recharge |
| Gaming Console 🎮 | $400 | stress -8, happiness +15, energy +5 | No, 1 total | Entertainment & relaxation |

## Game Design: Responsive Money Spending

### How Money Becomes "Responsive"

1. **Stress Triggers Purchases**
   - High stress → suggests therapy, spa, vacation
   - Player must decide: skip or spend money to feel better?

2. **Happiness Deficiency**
   - Low happiness → social activities become more valuable
   - Player balances work/study with life activities

3. **Semester Progression Unlocks Items**
   - Later semesters unlock car, vacation
   - Creates natural progression of expenses

4. **One-Time Investments**
   - Car ($8000), laptop ($1200), apartment upgrade ($5000) are major decisions
   - Need to save money strategically
   - Create meaningful financial trade-offs

5. **Repeatable Budgeting**
   - Coffee ($15), dinner ($40) test weekly budgeting
   - Gym ($120) vs therapy ($300) - prioritize what matters
   - Max per semester prevents spamming

### Example Gameplay Loop

```
Semester 1:
- Start with $5000
- Studies cause stress to rise to 75
- Can't afford major purchases (car, apartment)
- Must balance: coffee ($15) or save money?
- Therapy ($300) would help but cuts into savings
- Player learns value of stress management vs financial planning

Semester 2:
- Unlock vacation ($600), car ($8000)
- Probably has $8000+ saved or earned from side gigs
- Decision: buy car now or invest in apartment later?
- Each purchase has permanent effects on happiness, stress
- Creates rich strategic decision-making
```

## API Endpoints

### 1. List Available Purchases
```
GET /api/store/available
```

Returns all purchases available for current semester, with:
- Purchase details
- Cost
- Effects on each stat
- Affordability status (can player buy it?)
- Current player balance

**Response:**
```json
{
  "purchases": [
    {
      "purchase_id": "coffee_with_friends",
      "name": "Coffee with Friends",
      "emoji": "☕",
      "cost": 15.0,
      "category": "social",
      "is_affordable": true,
      "current_balance": 5000.0,
      "effects": [
        {"stat": "stress", "change": -5},
        {"stat": "happiness", "change": 10}
      ]
    }
  ]
}
```

### 2. Make a Purchase
```
POST /api/store/purchase/{purchase_id}
```

Execute a purchase, applying effects and deducting money.

**Response:**
```json
{
  "success": true,
  "message": "✅ Purchased 'Coffee with Friends' for $15.00. Effects: stress: -5.0, happiness: 10.0, eq: 2.0, mental_health: 5.0",
  "purchase": {
    "id": "coffee_with_friends",
    "name": "Coffee with Friends",
    "cost": 15.0
  },
  "balance_before": 5000.0,
  "balance_after": 4985.0,
  "effects": {
    "stress": -5.0,
    "happiness": 10.0,
    "eq": 2.0,
    "mental_health": 5.0
  }
}
```

### 3. View Purchase History
```
GET /api/store/history
```

All purchases made this playthrough, with effects applied.

### 4. Get Categories
```
GET /api/store/categories
```

List all purchase categories: social, health, wellness, fun, practical, self-care

### 5. Get Smart Suggestions
```
GET /api/store/suggestions
```

AI-generated suggestions based on player's current stats:
- High stress → stress relief items
- Low happiness → fun items
- Low fitness → health items
- Low mental health → wellness items

**Response:**
```json
{
  "suggestions": [
    {
      "purchase_id": "therapy_sessions",
      "name": "Therapy Sessions",
      "emoji": "🧠",
      "cost": 300,
      "reason": "Mental health low (45) - seek support",
      "is_affordable": true
    }
  ]
}
```

## Integration with Game Systems

### Finance System
- Purchases deduct from `player.finance.balance`
- Invalid if player has insufficient funds
- Creates meaningful financial constraints

### Stats System
- Purchases modify player stats in-place:
  - `stress`, `happiness`, `eq`, `burnout`
  - `technical_skills`, `communication_skills`, `time_management`, `business_acumen`
  - `energy_level`

### Health System
- Purchases modify health attributes:
  - `mental_health`, `fitness`, `sleep_quality`, `health`

### History System
- Each purchase recorded in `player.history` with:
  - Purchase ID, name, cost
  - All effects applied
  - Semester it occurred

### Limits System
- **One-time purchases**: Can only buy once per playthrough (car, laptop, apartment)
- **Max per semester**: Coffee limited to 4/semester, dinner to 2/semester
- **Semester unlocking**: Car requires semester 2+

## Design Philosophy

### Cost-Benefit Tradeoffs
- Cheap items ($15-25): Small effects, repeatable
- Medium items ($60-300): Significant effects, limited per semester
- Expensive items ($500-8000): Major impacts, one-time or once per semester

### Strategic Decisions
- Save for car/apartment or spend on wellness?
- Stress relief now vs financial security later?
- What's worth the money investment?

### Realism
- Items tied to real college/early career experiences
- Prices roughly realistic ($15 coffee, $300 therapy, $8000 car)
- Effects mirror actual impact on life (car reduces stress, therapy improves mental health)

## Future Enhancements

1. **Event-Triggered Purchases**
   - Birthday → free vacation opportunity
   - Bad test → therapy suggestion
   - Got a job → professional wardrobe suggestion

2. **Purchase Chains**
   - Gym membership unlocks "Personal Trainer" ($500)
   - Car unlocks "Road Trip" ($800)
   - Therapy sessions unlock "Meditation Retreat" ($1000)

3. **Dynamic Pricing**
   - Sales/discounts during certain semesters
   - Inflation over time
   - Seasonal items (seasonal items only in fall, etc.)

4. **Permanent Upgrades**
   - Car stays in inventory, reduces stress permanently
   - Apartment upgrade permanent quality of life boost
   - Laptop makes studies faster

5. **Multiplayer Trading**
   - Sell used car to another player?
   - Share gym membership cost?
   - Gift purchases to friends?

## Testing the System

### Syntax Check
```bash
source .venv/bin/activate
python -m py_compile store/purchase_service.py api/router_store.py
```

### Run Backend
```bash
source .venv/bin/activate
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Test Endpoints
```bash
# Get available purchases
curl http://localhost:8000/api/store/available?player_id=player1

# Make a purchase
curl -X POST http://localhost:8000/api/store/purchase/coffee_with_friends?player_id=player1

# Get history
curl http://localhost:8000/api/store/history?player_id=player1

# Get suggestions
curl http://localhost:8000/api/store/suggestions?player_id=player1
```

## Summary

The **Life Purchases Store** makes money spending **responsive to player actions** by:

1. ✅ Creating financial constraints (only so much money)
2. ✅ Linking purchases to meaningful stat changes
3. ✅ Forcing strategic decisions (spend or save?)
4. ✅ Providing 17 realistic items across 6 categories
5. ✅ Implementing purchase limits and semester unlocking
6. ✅ Offering smart suggestions based on player state
7. ✅ Recording complete purchase history
8. ✅ Integrating with all player systems (stats, health, finance)

**Money matters in this game.** Every dollar spent has consequences, rewards, and trade-offs.
