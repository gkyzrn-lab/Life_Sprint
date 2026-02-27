# 💰 Store ↔ Jobs ↔ Tuition Integration System

**Strategic Money Integration** - Connect life purchases with job income and tuition costs

## 🎯 Overview

Players now make **strategic financial decisions** based on:
- **Current job income** - How much they're earning per semester
- **Tuition burden** - How much college costs relative to income  
- **Monthly budget** - What they can actually afford after bills
- **Purchase ROI** - Whether a purchase pays for itself in earnings gains

This creates meaningful trade-offs:
- Do I buy expensive therapy now, or save for a laptop that enables better jobs?
- Can I afford this $150 spa day on my current hourly wage?
- Will reducing stress improve my job performance enough to earn back the cost?

## 📊 Key Features

### 1. Financial Summary
Shows player's comprehensive financial picture:
```
Job: IT Helpdesk (10 hrs/week, $19/hr)
Current Balance: $4,200
Semester Income: $3,952
Semester Tuition: $3,670
Monthly Available: $1,120
```

**Strategic Value**: Players see exactly how much discretionary money they have each month based on job + tuition.

### 2. Purchase Affordability Analysis
Before buying anything, system analyzes:
- Can they afford it NOW?
- How many days of work would it take?
- If recurring, what impact on monthly budget?
- Financial warnings about risky purchases

**Example Output:**
```
Spa Day ($150)
✅ Affordable | Requires 1.0 days of work
   Fits within monthly budget

Laptop ($1,200)
✅ Technically affordable but...
⚠️ Costs more than monthly available budget ($1,120)
   Should save up first, or increase income
```

### 3. ROI Analysis
For wellness purchases, calculates return-on-investment:
- Stress reduction percentage
- Impact on job performance
- Estimated income gain per semester  
- Payback period

**Example:**
```
Investment: Spa Day ($150)
Stress Reduction: -20 points
Performance Gain: +3% job effectiveness
Income Gain: +$17.78/semester
Payback Period: 8.4 semesters
```

This teaches: **Wellness isn't free spending—it's an investment that can pay off through better job performance.**

### 4. Income Optimization Recommendations
Personalized suggestions based on financial health:
- Low monthly budget? → "Suggest higher-paying job"
- High stress? → "Therapy could improve job performance → +$100/month"
- Excellent health? → "Can invest in career items (laptop, car)"

## 🔌 API Endpoints

### GET `/api/store/financial-summary?player_id=<id>`
Get comprehensive financial status.

**Response:**
```json
{
  "current_balance": 4200.00,
  "semester_income": 3952.00,
  "semester_tuition": 3670.00,
  "monthly_subscriptions": 0.00,
  "income_after_essentials": 4482.00,
  "monthly_available": 1120.50,
  "job_title": "IT Helpdesk (Campus)",
  "job_hours": 10,
  "performance_rating": 65.0,
  "financial_health": "comfortable"
}
```

### GET `/api/store/affordability/{purchase_id}?player_id=<id>`
Analyze if a purchase makes financial sense.

**Response:**
```json
{
  "purchase_id": "spa_day",
  "purchase_name": "Spa Day",
  "cost": 150.00,
  "can_afford_now": true,
  "shortage": 0.00,
  "is_recurring": false,
  "monthly_impact": 0.00,
  "new_monthly_budget": 1120.50,
  "days_of_income_required": 1.0,
  "financial_warning": null
}
```

### GET `/api/store/roi/{purchase_id}?player_id=<id>`
Get return-on-investment analysis.

**Response:**
```json
{
  "purchase_id": "spa_day",
  "purchase_name": "Spa Day",
  "investment": 150.00,
  "stress_reduction": -20.0,
  "estimated_performance_gain": 3.0,
  "estimated_income_gain_per_semester": 17.78,
  "payback_period_semesters": 8.4,
  "roi_summary": "🤔 Low ROI: Takes many semesters to recoup investment"
}
```

### GET `/api/store/recommendations?player_id=<id>`
Get personalized recommendations for improving financial situation.

**Response:**
```json
{
  "recommendations": [
    {
      "category": "income",
      "icon": "💼",
      "title": "Income is Tight",
      "suggestion": "Consider switching to higher-paying job or working more hours",
      "impact": "Could add $200-500/month",
      "priority": "high"
    },
    {
      "category": "wellbeing",
      "icon": "😌",
      "title": "Stress Reducing Purchases Help Income",
      "suggestion": "Therapy reduces stress → better job performance → possible raise",
      "roi": "Invest $300 now → potentially +$100/month long-term",
      "priority": "high"
    }
  ]
}
```

### GET `/api/store/dashboard?player_id=<id>`
Complete financial dashboard combining all integration data.

## 🎓 Educational Impact

### Lesson 1: Money Is Constrained
Players quickly realize: "I can't afford everything." This teaches resource allocation and prioritization.

### Lesson 2: Income Matters
The job they choose directly affects what they can buy. Changes the entire game dynamic:
- Low-paying job? Very limited spending
- High-paying job? More freedom but higher stress
- No job? Essentially trapped (unless they save)

### Lesson 3: Wellness Is An Investment
Buying therapy doesn't just improve mental health—it can improve job performance, which improves income. Shows the connection between wellbeing and financial success.

### Lesson 4: Strategic Decision Making
Players learn to ask: "Is this purchase worth it?"
- Coffee ($15) = impulse buy but affordable
- Spa day ($150) = stress relief vs. save for laptop
- Laptop ($1200) = big investment but enables better jobs

### Lesson 5: Trade-offs Are Real
Real-world trade-offs become visible:
- Work more hours → more money but more stress
- Buy wellness → feel better but less money
- Expensive college → higher tuition but better opportunities

## 💡 Implementation Details

### Income Calculation
```python
semester_income = hourly_wage × hours_per_week × 16 weeks × performance_multiplier

# Performance affects actual earnings (70%-130% of base)
# Low performance: fewer hours, fewer tips
# High performance: overtime, bonuses, better tips
```

### Financial Health Categories
- **Critical**: Monthly available < $0 (spending exceeds income)
- **Tight**: Monthly available < $500 (very limited discretionary spending)
- **Comfortable**: Monthly available < $1500 (reasonable flexibility)
- **Excellent**: Monthly available > $1500 (significant purchasing power)

### ROI Calculation for Wellness Purchases
```python
stress_reduction = purchase effects → stress stat change

# Lower stress = better job performance
performance_improvement = stress_reduction × 0.15

# Performance gain = potential income increase
income_gain = (performance_improvement / 100) × semester_income × 0.15

# Payback period = when does the raise recoup investment
payback_semesters = purchase_cost / income_gain
```

## 🎮 Example Gameplay Scenarios

### Scenario 1: High Stress Player
- Current stress: 85/100
- Job: $15/hr barista, $1440/semester
- Monthly available: $180
- Recommendation: "Your stress is killing your productivity. Therapy ($300) could improve performance → potential +$100/month income"
- Decision point: Spend $300 now to earn potentially more later?

### Scenario 2: Low Income Player  
- No job, balance: $2000
- Monthly available: -$417 (spending more than income!)
- Can only afford cheap items ($15-30)
- Can't afford therapist ($300) or laptop ($1200)
- Recommendation: "Get a job. Even minimum wage ($14.50/hr = $3696/semester) makes a huge difference"

### Scenario 3: High Performance Player
- Good job: $20/hr, excellent performance (90/100)
- Monthly available: $1500+
- Can afford all purchases
- ROI on wellness purchases positive because they get raises more easily
- Strategic: "You're doing great! Invest in career items (laptop) to unlock better jobs"

## 🔄 Integration With Other Systems

| System | Integration | Impact |
|--------|-------------|--------|
| **Jobs** | Store shows job income in affordability analysis | Players see concrete tradeoff: job choice → purchasing power |
| **Tuition** | Semester tuition deducted from available money | Players feel college cost pressure |
| **Loans** | Borrowing affects monthly budget calculations | Debt reduces available spending money |
| **Career** | Job performance rating affects actual earnings | Wellness → performance → income |
| **Stress/Health** | Wellness purchases show ROI through job performance | Wellbeing = investment, not luxury |

## 🚀 Future Enhancements

1. **Career Paths Impact**  
   - Computer Science jobs pay more but have higher stress
   - Teaching jobs pay less but lower stress
   - Different ROI for same wellness purchase based on major

2. **Negotiation System**  
   - Good performance → can negotiate raise
   - Salary negotiation training shows lifetime impact
   - Students learn: "That $5k raise means $200k+ over lifetime"

3. **Emergency Fund Mechanics**
   - Medical emergency costs money
   - Without emergency fund, must go into debt
   - Wellness purchases can prevent emergencies (health spending)

4. **Subscription Tracking**
   - Gym, streaming, meal prep become recurring monthly costs
   - Players must budget for subscriptions
   - Can't just "stop" gym mid-semester (penalty fee)

5. **Gig Economy Integration**
   - Side gigs (DoorDash, freelance) add income
   - Variable income (some weeks good, some bad)
   - Must budget conservatively based on average, not peak

## 📈 Success Metrics

Track if integration is working:
1. **Purchase Affordability Awareness**: Do players check affordability before buying?
2. **Strategic Job Selection**: Do players pick jobs based on financial need?
3. **ROI Understanding**: Do players understand wellness purchases as investments?
4. **Budget Consciousness**: Do players plan spending around monthly available budget?
5. **Income Awareness**: Do players understand how their job affects purchasing power?

---

**Result**: Store is no longer "arbitrary spending" but integrated into core game loop:
- Job choice → Income → What you can buy → Wellbeing → Job performance → Better income
