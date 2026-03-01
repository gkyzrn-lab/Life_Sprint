# 💰 Money Integration - Quick Reference

## What Changed?

| Before | After |
|--------|-------|
| "Can I afford this?" | "Should I buy this?" |
| Just check balance | Check 5 financial factors |
| Purchases isolated | Purchases affect job/tuition decisions |
| Money = abstract number | Money = concrete monthly budget |

## Key Formulas

### Monthly Available Money
```
(Current Balance + Semester Income - Semester Tuition - Monthly Subscriptions) ÷ 4 months
```

### Days of Work Needed
```
Purchase Cost ÷ Hourly Wage ÷ 8 hours per day
```

### Purchase ROI (Wellness Items)
```
Stress Reduction → Performance Improvement → Income Gain
Example: -20 stress → +3% performance → +$17.78 income/semester
```

## API Quick Start

```bash
# Get player's full financial situation
GET /api/store/financial-summary?player_id=abc123

# Can they afford a spa day?
GET /api/store/affordability/spa_day?player_id=abc123

# Is therapy worth the money?
GET /api/store/roi/therapy_sessions?player_id=abc123

# Get personalized financial advice
GET /api/store/recommendations?player_id=abc123

# Show complete dashboard
GET /api/store/dashboard?player_id=abc123
```

## What Impacts Purchasing Power?

```
Purchasing Power = (Balance + Job Income - Tuition - Monthly Subscriptions) ÷ 4

Increases by:
✅ Getting better-paying job
✅ Working more hours  
✅ Better job performance
✅ Lower tuition college
✅ Off-campus housing with roommates
✅ Canceling subscriptions

Decreases by:
❌ Taking lower-paying job
❌ Reducing work hours
❌ Poor job performance
❌ Higher tuition college
❌ Expensive housing
❌ Adding subscriptions
```

## Financial Health Tiers

| Health | Monthly Available | What It Means |
|--------|---|---|
| 🔴 Critical | < $0 | Spending more than income! Go into debt. MUST get job. |
| 🟡 Tight | $0-$500 | Very limited. Can only afford $15-30 items. No subscriptions. |
| 🟢 Comfortable | $500-$1,500 | Reasonable. Can afford items up to $150-300. |
| 🟢 Excellent | > $1,500 | Flexible. Can afford $1,000+ items and subscriptions. |

## Common Scenarios

### Scenario: Poor College Student
- Job: None
- Balance: $1,500
- Monthly available: -$417 (CRITICAL)
- **Problem**: Tuition costs more than savings!
- **Solution**: MUST get a job
- **Store impact**: Can't afford anything except cheap items ($15)

### Scenario: Working Student (Low Wage)
- Job: Barista $15/hr, 10 hrs/week
- Performance: 50/100 (mediocre)
- Monthly available: $420
- **Balanced**: Can afford basic purchases, must choose carefully
- **Store impact**: Coffee ($15) yes, spa ($150) maybe, laptop ($1200) no

### Scenario: Working Student (Good)
- Job: IT Helpdesk $19/hr, 10 hrs/week  
- Performance: 75/100 (good)
- Monthly available: $1,180
- **Comfortable**: Can buy items freely, some limits remain
- **Store impact**: Most items affordable, must save for expensive ones

### Scenario: Ambitious Student (Full Work)
- Job: Startup role $25/hr, 20 hrs/week
- Performance: 85/100 (excellent)
- Monthly available: $2,100
- **Excellent**: Can afford almost anything
- **Store impact**: All items accessible, focus on ROI not affordability

## ROI Interpretation Guide

```
Payback Period → ROI Summary

< 1 semester    → ⭐ Excellent ROI: Pays for itself quickly!
1-2 semesters   → ✅ Good ROI: Reasonable payback
2-4 semesters   → ℹ️ Moderate ROI: Takes a while to break even
> 4 semesters   → 🤔 Low ROI: Takes a long time to recoup
```

## Strategic Decision Tree

```
Want to buy something?

1. Check affordability
   ├─ Can afford now? → Go to 2
   └─ Can't afford? → Need {X} more days of work → Decision

2. Check impact on monthly budget
   ├─ New monthly budget good? → Go to 3
   └─ New monthly budget tight? → Decision

3. Check ROI (if wellness item)
   ├─ Positive ROI? → Good investment
   └─ Negative ROI? → Luxury purchase (that's ok!)

4. Make decision
   ✅ Buy → Enjoy benefits
   ⏸️  Wait → Save up first
```

## File Reference

**New Files:**
- `store/financial_integration.py` (445 lines) - Core integration logic
- `MONEY_INTEGRATION.md` - Full documentation
- `MONEY_INTEGRATION_SUMMARY.md` - Implementation details

**Modified Files:**
- `api/router_store.py` - 5 new endpoints

**Integration Points:**
- Works with: `catalogs/jobs.py`, `catalogs/colleges.py`, `core_domain/player.py`

## Testing the Integration

```python
from store.financial_integration import get_financial_summary

player = get_player(player_id)
summary = get_financial_summary(player)

print(f"Monthly Available: ${summary['monthly_available']:.2f}")
print(f"Financial Health: {summary['financial_health']}")
print(f"Semester Income: ${summary['semester_income']:.2f}")
```

## Next Steps for Frontend

To display integration data in UI:

1. **Financial Dashboard**
   - Show current balance
   - Show monthly available
   - Show financial health indicator
   - Show job info

2. **Purchase Screen**
   - Before item details, show affordability
   - Show days of work needed
   - Show monthly budget impact
   - Show warnings if risky

3. **ROI Visualizer**
   - For wellness items, show stress→performance→income gain
   - Show payback timeline
   - Help player decide if worth it

4. **Recommendations Panel**
   - Show personalized suggestions
   - "Your stress is high → therapy could help"
   - "Get better job to afford this"
   - "You're financially healthy → invest in career"

---

**Key Takeaway**: Money integration transforms store from "random spending" into "strategic financial planning system" that reflects real-world trade-offs.
