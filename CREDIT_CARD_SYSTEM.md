# Credit Card System - Financial Responsibility for Students

## Overview
We've added a comprehensive credit card system to teach students financial responsibility, credit score building, and smart money management. The system includes **7 different credit cards** across 3 bank tiers, extensive educational content, and personalized recommendations.

---

## 🏦 Credit Card Tiers

### **Premium Tier** (Best Rates, Best Perks, Hardest to Get)
**Requirements:** Credit score 680-700+, Income $10,000-$12,000+  
**Annual Fees:** $75-$95 (but perks are worth $300-500/year!)

1. **Chase Sapphire Student Rewards Platinum**
   - APR: 15.99%
   - **Annual Fee: $95** (waived first year!)
   - Limit: $2,000-$5,000
   - Perks: 2% cashback, 3% on dining/travel, $25/month gym ($300/year), $10/month streaming ($120/year)
   - Signup Bonus: $200 (spend $500 in 3 months)
   - **Worth it if:** You use the gym ($300) + spend $400+/month
   - Best for: Students with established credit who want maximum rewards

2. **Citi Bank Student Cashback Elite**
   - APR: 16.49%
   - **Annual Fee: $75**
   - Limit: $1,500-$4,000
   - Perks: 1.5% cashback, 5% on groceries, 3% on gas, credit score monitoring
   - Signup Bonus: $150
   - **Worth it if:** You spend $125+/month on groceries (5% of $1,500 = $75)
   - Best for: Students who want cashback on everyday spending

### **Standard Tier** (Reasonable Rates, Good Perks, Moderate Requirements)
**Requirements:** Credit score 620-630+, Income $5,000-$6,000+  
**Annual Fees:** $0 (perfect for students!)

3. **Bank of America Student Visa Card**
   - APR: 19.99%
   - **Annual Fee: $0** ✅
   - Limit: $500-$2,000
   - Perks: 1% cashback, 2.5% online, Spotify Premium included ($10/month value)
   - Signup Bonus: $50
   - Best for: Students building credit for the first time

4. **Wells Fargo Student Cashback Card**
   - APR: 20.49%
   - **Annual Fee: $0** ✅
   - Limit: $500-$1,500
   - Perks: 1% cashback, cell phone protection, budgeting tools
   - Signup Bonus: $30
   - Best for: Students who need basic cashback and phone protection

### **Starter Tier** (Higher Rates, Easiest to Get)
**Requirements:** Low/no credit score, low/no income  
**Annual Fees:** $0 (no risk!)

5. **Discover Secured Student Card** ⭐ **BEST FOR BEGINNERS**
   - APR: 22.99%
   - **Annual Fee: $0** ✅
   - Limit: Based on $200 security deposit
   - Perks: 1% cashback, 2% on gas/restaurants, FREE FICO score, cashback match first year
   - **Get deposit back after 8 months of good payments!**
   - Best for: Students with NO credit history or bad credit

6. **Capital One Basic Student Card**
   - APR: 24.99%
   - **Annual Fee: $0** ✅
   - Limit: $300-$1,000
   - Perks: Credit monitoring, fraud alerts
   - Best for: Students who can't qualify for anything else

7. **NetSpend Student Prepaid Visa**
   - APR: 0% (prepaid, no credit!)
   - **Monthly Fee: $5**
   - Perks: No credit check, budget tracking, no overdraft fees
   - ⚠️ **Does NOT build credit** - training wheels only
   - Best for: Students who want spending control without credit risk

---

## 📚 Educational Content

### **Credit Card Explanations** (in [catalogs/explanations.py](catalogs/explanations.py))
1. **credit_card_basics** - Pay in full vs minimum payment trap
2. **credit_score_building** - How to build 700+ score in 6 months
3. **apr_explained** - Why APR matters and how to compare
4. **credit_utilization** - The 30% rule for credit limits
5. **annual_fees** - ⭐ NEW! When premium cards with fees are worth it

### **Mini-Lessons** (in [catalogs/mini_lessons.py](catalogs/mini_lessons.py))
1. **credit_cards_101** (Semester 2) - 60 seconds
   - The golden rule: Pay FULL balance = $0 interest
   - Real example: $1,000 laptop paid in full vs minimum payments

2. **building_credit_score** (Semester 3) - 55 seconds
   - What affects credit: Payment history (35%), Utilization (30%), Age (15%)
   - Fast track: One card, $20-50/month, pay in full, 6 months = 700+ score

3. **apr_and_interest** (Semester 4) - 50 seconds
   - Lower APR saves hundreds on same debt
   - Real comparison: $2,000 balance at 15% vs 25% APR

4. **credit_card_perks_lesson** (Semester 5) - 45 seconds
   - Perks are ONLY valuable if you never pay interest
   - Math: $420 in perks - $360 interest = Only $60 net benefit

---

## 🎯 Key Features

### **Smart Qualification System**
```python
from catalogs.credit_cards import get_cards_player_qualifies_for

player_state = {
    "credit_score": 650,
    "annual_income": 8000,
    "is_student": True,
    "balance": 500  # For security deposit
}

qualified_cards = get_cards_player_qualifies_for(player_state)
# Returns cards sorted by tier (best first) that player qualifies for
```

### **Credit Building Advice**
```python
from catalogs.credit_cards import get_credit_building_advice

advice = get_credit_building_advice(credit_score=0)
# Returns:
# - status: "No Credit History"
# - recommendation: "Start with secured card"
# - timeline: "6 months to establish score"
# - best_cards: ["starter_secured_card"]
# - tips: [4+ actionable tips for building credit]
```

### **Cost-Benefit Analysis**
```python
from catalogs.credit_cards import estimate_annual_cost_benefit

card = get_card("premium_rewards_platinum")
analysis = estimate_annual_cost_benefit(card, monthly_spending=500)
# Returns:
# {
#   "annual_fee": 95,
#   "first_year_fee": 0,  # Waived first year
#   "cashback_earned": 120.00,
#   "perks_annual_value": 420.00,  # Gym + streaming
#   "signup_bonus": 200,
#   "first_year_net_benefit": 740.00,  # Amazing first year!
#   "ongoing_annual_benefit": 445.00,  # Still great ongoing
#   "break_even_spending": 4750.00  # Need to spend this much to justify fee from cashback alone
# }

# Compare to no-fee card
standard_card = get_card("standard_student_visa")
standard_analysis = estimate_annual_cost_benefit(standard_card, monthly_spending=500)
# {
#   "annual_fee": 0,
#   "first_year_net_benefit": 230.00,
#   "ongoing_annual_benefit": 180.00,
# }

# Premium card wins by $265/year if you use the perks!
```

### **Card Comparison**
```python
from catalogs.credit_cards import compare_cards

comparison = compare_cards([
    "premium_rewards_platinum",
    "standard_student_visa",
    "starter_secured_card"
])
# Returns side-by-side comparison + winners in each category
```

---

## 🎮 Integration into Game

### **When to Offer Credit Cards**
1. **Low Budget Trigger** - When player has < $100 balance
2. **Semester 2+** - Not too early, students need basic financial education first
3. **Emergency Situations** - Unexpected expenses (car repair, medical bill)
4. **Building Credit** - When player has no credit history

### **Credit Score Tracking**
Add to Player model:
```python
class Player(BaseModel):
    credit_score: int = 0  # 0-850
    credit_cards: List[Dict] = []  # Active cards
    credit_history: List[Dict] = []  # Payment history
    
    # Track monthly for credit building
    monthly_payment_history: List[bool] = []  # True = on-time, False = late
```

### **Monthly Credit Card Flow**
```python
def process_credit_card_month(player: Player):
    for card in player.credit_cards:
        balance = card["balance"]
        min_payment = max(25, balance * 0.02)
        
        # Player chooses: pay full, pay more, or pay minimum
        choice = present_payment_options(balance, min_payment, player.balance)
        
        if choice == "full":
            player.balance -= balance
            card["balance"] = 0
            player.credit_score += 2  # Perfect payment!
            player.monthly_payment_history.append(True)
            
        elif choice == "minimum":
            player.balance -= min_payment
            card["balance"] -= min_payment
            # Add interest!
            interest = card["balance"] * (card["apr"] / 12 / 100)
            card["balance"] += interest
            player.monthly_payment_history.append(True)
            
            # Show warning about interest cost
            show_explanation("minimum_payment_trap")
            
        elif choice == "miss":
            # Missed payment - MAJOR consequences!
            player.credit_score -= 25
            player.monthly_payment_history.append(False)
            card["late_fees"] += 35
            show_explanation("credit_score_building")  # Education moment!
```

### **Credit Score Calculation**
```python
def calculate_credit_score(player: Player) -> int:
    if not player.credit_cards:
        return 0
    
    # Payment history (35%)
    on_time = sum(player.monthly_payment_history[-12:])  # Last 12 months
    total = len(player.monthly_payment_history[-12:])
    payment_score = (on_time / total) * 35 if total > 0 else 0
    
    # Credit utilization (30%)
    total_limit = sum(card["limit"] for card in player.credit_cards)
    total_balance = sum(card["balance"] for card in player.credit_cards)
    utilization = total_balance / total_limit if total_limit > 0 else 0
    
    # Under 10% = perfect, over 50% = bad
    if utilization < 0.10:
        util_score = 30
    elif utilization < 0.30:
        util_score = 25
    elif utilization < 0.50:
        util_score = 15
    else:
        util_score = 5
    
    # Credit age (15%) - simplified
    age_score = min(player.current_semester * 2.5, 15)
    
    # Credit mix (10%) - has card = 10
    mix_score = 10 if player.credit_cards else 0
    
    # New credit (10%) - simplified
    new_credit_score = 10
    
    total = payment_score + util_score + age_score + mix_score + new_credit_score
    
    # Scale to 300-850
    return int(300 + (total / 100) * 550)
```

---

## 📊 Educational Impact

### **Learning Outcomes**
Students will learn:
1. ✅ **Credit Card Mechanics** - APR, minimum payments, interest compounding
2. ✅ **Credit Score Building** - Payment history > everything else
3. ✅ **Financial Discipline** - Pay in full or pay the price
4. ✅ **Comparison Shopping** - How to evaluate card offers
5. ✅ **Risk Management** - When to use credit vs cash
6. ✅ **Long-term Thinking** - Today's choices = tomorrow's credit score

### **Real-World Preparation**
- **Secured Cards** - Perfect for students with no credit
- **Realistic APRs** - Actual rates students will see (15-25%)
- **Real Perks** - Gym, streaming, cashback matches real offers
- **Consequences** - Late payments hurt score, interest compounds
- **Recovery** - Secured cards can graduate to unsecured

---

## 🧪 Testing

**Test Coverage:** 39 tests, 100% passing
- Credit card catalog structure (22 tests)
- Educational content quality (17 tests)

Run tests:
```bash
pytest tests/test_credit_cards.py tests/test_credit_education.py -v
```

---

## 🚀 Next Steps for Integration

### **1. Backend API Endpoints** (in [api/](api/))
```python
# api/router_credit_cards.py

@router.get("/credit-cards/available")
def get_available_cards(player_id: str):
    """Get credit cards player qualifies for."""
    player = get_player(player_id)
    player_state = {
        "credit_score": player.credit_score,
        "annual_income": calculate_annual_income(player),
        "is_student": True,
        "balance": player.finance.balance
    }
    return get_cards_player_qualifies_for(player_state)

@router.post("/credit-cards/apply")
def apply_for_card(player_id: str, card_id: str):
    """Apply for a credit card."""
    # Check qualification, add to player, handle security deposit

@router.post("/credit-cards/make-payment")
def make_payment(player_id: str, card_id: str, amount: float):
    """Make a credit card payment."""
    # Process payment, update balance, calculate interest, update credit score
```

### **2. Frontend UI Components**
- **Credit Card Picker** - Browse qualified cards with comparison
- **Payment Dialog** - Monthly payment choices with interest preview
- **Credit Score Dashboard** - Track score over time with tips
- **Education Pop-ups** - Show lessons when relevant

### **3. Game Loop Integration**
```python
# Every semester end
if player.credit_cards:
    process_credit_card_payments(player)
    
# Low budget trigger
if player.balance < 100 and player.current_semester >= 2:
    trigger_event("credit_card_offer")
    
# Build credit education
if player.current_semester == 3 and player.credit_score == 0:
    show_lesson("building_credit_score")
```

---

## 💡 Design Philosophy

1. **Education First** - Every card has warnings, tips, and real examples
2. **Realistic Consequences** - Interest compounds, late payments hurt
3. **Progressive Complexity** - Secured cards → Standard → Premium
4. **No Judgment** - Mistakes are learning opportunities
5. **Empowerment** - Students graduate knowing how to use credit responsibly
6. **⭐ Annual Fees = Reality** - Premium cards charge fees because perks cost money. Students learn to calculate if fees are worth it based on their spending habits.

---

## 💳 Annual Fee Strategy (Realistic Like Real Life)

### **Why Premium Cards Have Fees:**
- Gym memberships cost the bank $25/month = $300/year
- High cashback rates (2-3%) cost money to maintain
- Travel insurance, purchase protection = real costs
- Annual fees ($75-$95) help cover these perks

### **Why Basic Cards Are Free:**
- Lower cashback (1%)
- Fewer perks
- Banks make money from merchant fees + interest (if you carry balances)
- Perfect for students who just want to build credit

### **Teaching Moment:**
Students learn to ask: "Will I use $95 worth of perks?"
- Use gym daily = $300 value ✅
- 2% on $5,000 spending = $100 value ✅
- Total: $400 value for $95 fee = Worth it!

But if you don't use gym:
- 2% on $3,000 = $60 value
- $60 - $95 fee = -$35 (losing money!) ❌
- Better to get no-fee card with 1% = $30 profit ✅

### **Real-World Preparation:**
This teaches students the EXACT calculation they'll need in real life when comparing:
- Chase Sapphire Reserve ($550 fee)
- American Express Gold ($250 fee)  
- Discover It Student ($0 fee)

---

## 📖 Related Features

This credit card system works well with:
- **Emergency Fund** (from [catalogs/explanations.py](catalogs/explanations.py)) - Buffer against needing credit
- **Financial Badges** (from [catalogs/educational_badges.py](catalogs/educational_badges.py)) - "Credit Builder" badge
- **Challenge Modes** (from [catalogs/challenge_modes.py](catalogs/challenge_modes.py)) - "Debt-Free Challenge"
- **Random Events** (from [catalogs/random_events.py](catalogs/random_events.py)) - "Unexpected expense" tests credit decisions

---

## 🎓 Teaching Moments

### **Best Practices to Reinforce:**
- "Pay FULL balance every month" - repeated in every lesson
- "Under 30% utilization" - show score impact in real-time
- "Never miss a payment" - 35% of score comes from this
- "Start with secured card" - best path for no credit

### **Common Mistakes to Prevent:**
- Minimum payment trap - show total cost calculator
- Multiple card applications - hard inquiries hurt score
- Maxing out cards - utilization tanks score
- Missing payments - -25 score points, $35 late fee

---

## 📈 Success Metrics

**Student Outcomes:**
- Can explain APR and interest calculation
- Knows what builds credit score (payment history #1)
- Understands secured vs unsecured cards
- Can compare card offers (APR, perks, fees)
- Graduates with 700+ credit score (if they started building early)

---

## Summary

This credit card system provides:
- **7 realistic credit card products** across 3 tiers
- **8 educational explanations** about credit and debt
- **4 mini-lessons** delivered progressively through semesters
- **Smart qualification system** based on credit score and income
- **Credit score simulation** with realistic building mechanics
- **39 comprehensive tests** ensuring quality

Students learn by doing: apply for cards, make payments, see credit score change, experience consequences, and graduate with real financial knowledge. 🎓💳
