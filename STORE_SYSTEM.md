# Store System Documentation

## Overview
The store system provides 30+ real-life purchasable items that affect player stats, teaching financial decisions and trade-offs. Players can spend money on entertainment, technology, food, social activities, health, education, clothing, and transportation.

## Design Philosophy
- **Realistic Pricing**: Items cost what they would in real life
- **Trade-offs**: Most purchases have both positive and negative effects
- **Monthly Expenses**: Some items (subscriptions, memberships) recur monthly
- **Smart Recommendations**: AI suggests items based on player's current needs
- **Educational**: Warnings teach players about impulsive spending and budget consciousness

## Store Categories

### 1. Entertainment (5 items)
**Purpose**: Boost morale and reduce stress, but watch for time/money drain

| Item | Price | Key Effects | Warning |
|------|-------|-------------|---------|
| Movie Ticket | $15 | +morale, +social, -stress | One-time fun |
| Streaming Service | $15/mo | +morale, -study_time | Addictive, can binge |
| Concert Ticket | $75 | +morale, +social, +memories | Expensive for budget |
| Video Game | $60 | +morale, -productivity | Can be addictive |
| Theme Park | $120 | +morale, +social, -stress | Major expense |

**Educational Value**: Entertainment spending feels good but can spiral. Netflix $15/month = $180/year!

### 2. Technology (5 items)
**Purpose**: Boost productivity and connectivity, but watch for overspending

| Item | Price | Key Effects | Warning |
|------|-------|-------------|---------|
| Laptop | $1200 | +study_efficiency, +productivity | Major investment |
| Tablet | $500 | +study_efficiency, +portability | Less powerful than laptop |
| Smartphone | $800 | +social, +anxiety, -productivity | Distraction device |
| Noise-Canceling Headphones | $300 | +focus, +study_efficiency, -social_awareness | Isolation risk |
| Smartwatch | $400 | +productivity, +health_tracking, +anxiety | Another screen to check |

**Educational Value**: Technology promises productivity but often creates distractions and anxiety. A $800 phone might hurt your GPA more than help it.

### 3. Food (4 items)
**Purpose**: Balance nutrition, convenience, social life, and budget

| Item | Price | Key Effects | Warning |
|------|-------|-------------|---------|
| Fast Food | $8 | +convenience, -health, -nutrition | Unhealthy habit |
| Restaurant Meal | $25 | +morale, +social, -budget_consciousness | Adds up quickly |
| Meal Prep Kit | $80/week | +health, +nutrition, +budget_consciousness | Time investment required |
| Coffee Shop Visit | $6 | +focus, +social, -budget_consciousness | Daily habit = $180/month |

**Educational Value**: The $6 daily latte habit = $2,190/year! Meal prep kits teach budget-conscious eating.

### 4. Social (4 items)
**Purpose**: Build connections but watch for peer pressure spending

| Item | Price | Key Effects | Warning |
|------|-------|-------------|---------|
| Bar/Club Night | $60 | +social, -health, -focus | Hangover next day |
| Group Activity | $40 | +social, +morale, +friendship | One-time event |
| Dating App Premium | $25/mo | +social, -self_esteem, +anxiety | Can be shallow |
| Party Hosting | $100 | +social, +popularity, -budget_consciousness | Expensive to impress |

**Educational Value**: Social life is important, but peer pressure spending (bars, hosting) adds up. A night out = 4 hours of work.

### 5. Health (4 items)
**Purpose**: Invest in wellness but balance cost vs benefit

| Item | Price | Key Effects | Warning |
|------|-------|-------------|---------|
| Gym Membership | $40/mo | +health, -stress, +confidence | Must use consistently |
| Therapy Session | $150 | -stress, -anxiety, +mental_health | Expensive but valuable |
| Healthy Groceries | $80/week | +health, +nutrition, +energy | Ongoing expense |
| Vitamins | $20/mo | +health, +nutrition | Not a substitute for diet |

**Educational Value**: Health is an investment, not an expense. $40/month gym membership is cheaper than medical bills. Therapy is expensive but can prevent bigger problems.

### 6. Education (4 items)
**Purpose**: Invest in academic success, highest ROI long-term

| Item | Price | Key Effects | Warning |
|------|-------|-------------|---------|
| Textbook | $200 | +study_efficiency, +grades | Required but expensive |
| Tutoring Session | $50 | +grades, +confidence, +understanding | Ongoing cost |
| Online Course | $100 | +skills, +career_prospects | Time investment required |
| Study Group Snacks | $30 | +social, +study_motivation, +collaboration | Builds community |

**Educational Value**: Education spending has the highest long-term ROI. A $50 tutor might save your $5,000 scholarship.

### 7. Clothing (2 items)
**Purpose**: Balance self-expression with budget consciousness

| Item | Price | Key Effects | Warning |
|------|-------|-------------|---------|
| Designer Clothes | $300 | +confidence, +status, -budget_consciousness | Peer pressure trap |
| Basic Wardrobe | $150 | +confidence, +budget_consciousness | Practical choice |

**Educational Value**: Designer clothes boost status but drain budget. Basic wardrobe teaches value over branding.

### 8. Transportation (2 items)
**Purpose**: Balance independence with massive monthly costs

| Item | Price | Key Effects | Warning |
|------|-------|-------------|---------|
| Car Payment | $350/mo | +independence, -budget_consciousness, +stress | Insurance, gas, maintenance extra! |
| Bus Pass | $50/mo | +budget_consciousness, -independence, -convenience | Cheapest option |

**Educational Value**: Car payments are massive hidden costs. $350/month = $4,200/year + insurance ($1,200) + gas ($1,500) = $6,900/year minimum!

## Smart Recommendation System

The store includes an AI that recommends items based on player stats:

### High Stress Detection
```python
if player.stats.stress > 70:
    recommends: ["therapy_session", "gym_membership", "movie_ticket"]
    reason: "Your stress is high - invest in mental health and relaxation"
```

### Low GPA Detection
```python
if player.stats.gpa < 2.5:
    recommends: ["tutoring_session", "textbook", "online_course"]
    reason: "Your grades need attention - invest in education"
```

### Social Isolation Detection
```python
if player.stats.social < 30:
    recommends: ["group_activity", "bar_night", "party_hosting"]
    reason: "You're isolated - spend on social connections"
```

### Low Health Detection
```python
if player.stats.health < 40:
    recommends: ["gym_membership", "healthy_groceries", "therapy_session"]
    reason: "Your health needs attention"
```

## Purchase Mechanics

### One-Time vs Recurring
- **One-Time**: Movie tickets, laptops, textbooks (buy once, own forever)
- **Monthly**: Gym memberships, streaming services, meal prep kits (auto-deduct monthly)

### Affordability Check
```python
# Before purchase
affordable_items = get_affordable_items(player.finance.balance)
# Only shows items within budget
```

### Effect Application
```python
# Purchasing applies effects immediately
result = purchase_item(player, "gym_membership")
# player.stats.health += 10
# player.stats.stress -= 15
# player.finance.balance -= 40
# player.finance.monthly_expenses += 40  # recurring
```

## Integration with Credit Card System

The store teaches realistic spending with credit cards:

### Scenario 1: Smart Spending
```
Balance: $500
Purchase: Textbook ($200) with Student Cashback Card
Effect: -$200 balance, +1% cashback ($2), +grades
Lesson: Using credit for education with low APR is smart
```

### Scenario 2: Impulsive Spending
```
Balance: $200
Purchase: Concert ticket ($75) + Bar night ($60) on Premium Platinum Card
Effect: -$135 balance + 24.99% APR starts accruing
Lesson: Entertainment spending on high-APR premium cards is expensive
```

### Scenario 3: Monthly Expense Trap
```
Monthly Subscriptions:
- Streaming: $15/mo
- Gym: $40/mo
- Meal Prep: $80/week = $320/mo
- Car Payment: $350/mo
Total: $725/mo minimum
Lesson: Recurring expenses add up fast!
```

## Monthly Expense Calculator

Players can view their total recurring costs:

```python
monthly_total = calculate_monthly_expenses(player.purchases)
# Returns: $725

Breakdown:
- streaming_service: $15
- gym_membership: $40
- meal_prep_kit: $320
- car_payment: $350
```

## Educational Warnings

Every expensive or risky item includes warnings:

| Item | Warning | Teaching Moment |
|------|---------|----------------|
| Premium Credit Card | "TRAP unless wealthy" | Annual fees + high APR = expensive |
| Car Payment | "Insurance, gas, maintenance extra!" | Hidden costs beyond monthly payment |
| Designer Clothes | "Peer pressure trap" | Status spending vs practical spending |
| Streaming Service | "Addictive, can binge" | Time drain vs productivity |
| Smartphone | "Distraction device" | Connectivity vs focus |
| Dating App | "Can be shallow" | Digital vs real connections |

## Best Practices for Game Design

1. **Start with Low Balance**: Force tough choices between entertainment and necessities
2. **Introduce Monthly Expenses Gradually**: Let players feel the trap of subscriptions
3. **Show Opportunity Cost**: "This concert = 2 tutoring sessions = 0.5 GPA points"
4. **Reward Smart Decisions**: Education spending should boost GPA/career significantly
5. **Punish Impulsive Spending**: Social/entertainment spending should have real downsides
6. **Credit Card Integration**: High-APR card + store spending = debt spiral lesson

## API Endpoints (Future)

```python
# Get all store items
GET /api/store/items

# Get items by category
GET /api/store/items?category=entertainment

# Get affordable items for player
GET /api/store/affordable/{player_id}

# Get smart recommendations
GET /api/store/recommendations/{player_id}

# Purchase item
POST /api/store/purchase
{
  "player_id": "abc123",
  "item_id": "gym_membership",
  "payment_method": "credit_card_id"  # optional
}

# View monthly expenses
GET /api/store/monthly-expenses/{player_id}
```

## Testing Coverage

The store system has 28 comprehensive tests:
- ✅ Minimum 25 items (30 actually)
- ✅ All 8 categories represented
- ✅ Realistic price ranges
- ✅ Meaningful stat effects (positive and negative)
- ✅ Affordability checks
- ✅ Purchase mechanics (success, insufficient funds, not found)
- ✅ Smart recommendations based on player stats
- ✅ Monthly expense calculations
- ✅ Warning messages for expensive items
- ✅ Repeatable vs one-time purchase flags
- ✅ Balanced effects (20%+ items have negatives)

## Future Enhancements

1. **Seasonal Items**: Holiday sales, back-to-school deals
2. **Bulk Discounts**: Buy 5 textbooks, get 10% off
3. **Peer Pressure System**: Friends invite to expensive events
4. **Buyer's Remorse**: Return items within 24 hours for 50% refund
5. **Quality Tiers**: Cheap laptop ($500) vs premium ($1200) with different effects
6. **Store Events**: Black Friday (50% off technology), Prime Day
7. **Achievement System**: "Budget Master" (never overspend), "Education Investor" (buy all education items)

---

**Summary**: The store system teaches real-world financial decisions through 30+ items with realistic prices, stat trade-offs, monthly expenses, and smart recommendations. Combined with the credit card system (especially those expensive premium traps!), students learn that every purchase has opportunity costs and consequences.
