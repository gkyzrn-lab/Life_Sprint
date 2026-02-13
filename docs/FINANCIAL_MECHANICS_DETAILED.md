# 💰 Life Sprint Financial Mechanics - Detailed Exploration

## Overview

Life Sprint includes a comprehensive, realistic financial system modeling U.S. student loans with three loan types, interest accrual mechanics, grace periods, capitalization, and two repayment plan types. The system teaches players about debt management, the cost of higher education, and long-term financial consequences.

---

## 1. Core Financial Architecture

### Player Finance State
Each player maintains three financial components:

**Cash Balance** (`finance.balance`)
- Starting balance: $1,000
- Represents liquid cash available for spending
- Can go negative (debt allowed)
- Increased by: borrowing, income from jobs
- Decreased by: living expenses, loan repayments

**Monthly Expenses** (`finance.monthly_expenses`)
- Based on housing type and base expenses
- Base non-housing: $350/month
- Housing adds: $0 (on-campus), $400-$800/month (off-campus)
- Automatically deducted during semester progression

**Loan Portfolio** (`finance.loan_portfolio`)
- Container for all student loans
- Each loan tracks separately: principal, interest, type, state
- Multiple loans of same type possible (not typically, but architecture supports it)

---

## 2. Three Loan Types (Realistic U.S. Student Loan Model)

### Subsidized Loans
```
Interest Rate:        4.5% annual (0.045)
Max per Semester:     $2,750
Grace Period:         6 months
Repayment Period:     120 months (10 years)
In-School Interest:   NO ACCRUAL (government pays interest while in school)
Grace Period Interest: NO ACCRUAL
```

**Characteristics:**
- Lowest interest rate
- Government subsidizes interest while in school
- Most favorable loan type
- Limited annual borrowing cap

**Educational Value:**
- Shows how government assistance reduces debt burden
- Demonstrates the value of subsidized programs
- Teaches that free money (no interest accrual) exists for some borrowers

---

### Unsubsidized Loans
```
Interest Rate:        5.5% annual (0.055)
Max per Semester:     $5,500
Grace Period:         6 months
Repayment Period:     120 months (10 years)
In-School Interest:   YES ACCRUES to accrued_interest
Grace Period Interest: YES ACCRUES to accrued_interest
```

**Characteristics:**
- Moderate interest rate
- Student responsible for all interest (even while in school)
- Capitalization: accrued interest → principal when grace ends
- Higher borrowing cap than subsidized

**Educational Value:**
- Shows consequences of unsubsidized debt
- Demonstrates interest capitalization trap (interest on interest)
- Teaches that delaying payment increases total debt
- Common form of federal student lending

---

### Private Loans
```
Interest Rate:        8.5% annual (0.085)
Max per Semester:     $20,000 (essentially unlimited)
Grace Period:         0 months (NO GRACE)
Repayment Period:     120 months (10 years)
In-School Interest:   YES ACCRUES
No Grace Period:      Interest accrues immediately, no delay
```

**Characteristics:**
- Highest interest rate (nearly 2x subsidized)
- No grace period
- Immediate repayment obligation
- No borrowing limits (dangerous, unlimited access)
- Interest accrues from day 1

**Educational Value:**
- Shows dangers of private lending
- Demonstrates that unlimited credit is a trap
- Teaches predatory lending reality
- Shows why federal loans are preferred (students learn this the hard way)

---

## 3. Loan Lifecycle & State Transitions

### Phase 1: IN-SCHOOL (Student is Enrolled)

**What Happens:**
```
Player enrolled in college
    ↓
Needs $X for tuition/expenses
    ↓
Calls borrow_for_semester($X)
    ↓
Loans created/updated (if first time) OR existing loans increased
    ↓
Cash balance += borrowed amount
    ↓
Interest ACCRUES during semester (4 months):
  - Subsidized: NO accrual
  - Unsubsidized: accrued_interest += principal * (5.5% / 12) * 4
  - Private: accrued_interest += principal * (8.5% / 12) * 4
```

**Code Flow:**
```python
# Borrow in priority order: subsidized → unsubsidized → private
borrow_for_semester(player, $10,000)
  → subsidized: $2,750 (cap)
  → unsubsidized: $5,500 (cap)
  → private: $1,750 (remainder)
  → total: $10,000 (all covered)

# During semester progression
accrue_interest_in_school(player, months=4)
  → subsidized: NO interest
  → unsubsidized: accrued += $5,500 * 0.055/12 * 4 = ~$100.83
  → private: accrued += $1,750 * 0.085/12 * 4 = ~$49.58
```

**Example Scenario:**
```
Start Balance: $1,000
Borrow: $10,000
New Balance: $11,000

Expenses (rent, food, etc): $350/month × 4 = $1,400
After Semester: Balance = $11,000 - $1,400 = $9,600

Interest Accrued (unseen):
  - Subsidized: $0
  - Unsubsidized: $100.83
  - Private: $49.58
  - Total: $150.41 (added to accrued_interest, NOT yet in principal)
```

---

### Phase 2: GRACE PERIOD (Post-Graduation, Before Repayment)

**What Happens:**
```
Player graduates
    ↓
transition_loans_to_repayment() called
    ↓
Sets in_school = False for all loans
    ↓
Grace countdown begins (where applicable):
  - Subsidized/Unsubsidized: 6 months grace
  - Private: 0 months grace (immediate repayment)
    ↓
During grace countdown:
  - Subsidized: NO interest accrual
  - Unsubsidized/Private: CONTINUE accruing interest
    ↓
When grace months reach 0:
  - CAPITALIZATION: accrued_interest → principal
  - Minimum payment calculated
```

**Capitalization Example:**

Before Grace Ends:
```
Unsubsidized Loan
Principal: $5,500
Accrued Interest: $100.83 (from school)
Grace Months: 6

During 6-month grace, additional accrual:
$5,500 * 0.055/12 * 6 = $151.25

When grace ends (capitalization):
Principal: $5,500 + $100.83 + $151.25 = $5,752.08 ← NOW MUCH LARGER
Accrued Interest: $0 (capitalized)
```

**The Capitalization Trap:**
- "You owe more than you borrowed"
- This is a KEY teaching moment
- Students learn that delay increases total debt
- Interest accrued during grace is often a surprise to real students

---

### Phase 3: REPAYMENT (Post-Grace)

**What Happens:**
```
Grace period ends
    ↓
CAPITALIZATION occurs (if accrued_interest > 0)
    ↓
Minimum payment calculated using amortization formula
    ↓
Each month:
  1. Apply monthly interest to principal
  2. Determine payment budget (based on repayment plan)
  3. Allocate payment across loans (highest interest rate first)
  4. Deduct from player.finance.balance
  5. Decrement remaining months / principal
```

**Payment Allocation Algorithm:**

```
Repay budget available: $500/month

Loans in repayment (highest interest first):
1. Private at 8.5%: owes $1,750
2. Unsubsidized at 5.5%: owes $5,752

Allocation order:
  → Private gets first $500 (pay highest-rate debt first)
  → Unsubsidized waits until private paid off

After 1 month:
  Private: $1,750 → $1,250 (paid $500)
  Unsubsidized: $5,752 (payment pending)
```

This teaches financial literacy: **pay highest-interest debt first** (just like real financial advice).

---

## 4. Minimum Payment Calculation

### Amortization Formula

```python
Monthly Payment = P * (r * (1 + r)^n) / ((1 + r)^n - 1)

Where:
  P = principal (amount borrowed)
  r = monthly interest rate (annual / 12)
  n = number of remaining months
```

**Example:**
```
Principal: $10,000
Annual Interest: 5.5%
Remaining Months: 120

Monthly rate: 5.5% / 12 = 0.00458333
Monthly Payment = $10,000 * (0.00458333 * 1.00458333^120) / (1.00458333^120 - 1)
                ≈ $189.32

Over 120 months:
Total payments = $189.32 × 120 = $22,718.40
Total interest = $22,718.40 - $10,000 = $12,718.40
```

**Key Insight:**
- Long repayment period = more interest paid
- Standard 10-year plan is most common
- Players learn: longer payment = more expensive total cost

---

## 5. Two Repayment Plans

### Standard Repayment Plan (Default)
```
Monthly Payment = Sum of all minimum payments
                = amortized_payment() for each loan
                = FIXED amount per month
```

**Characteristics:**
- Pays off loans in 10 years (120 months)
- Same payment every month
- Highest total monthly cost
- Lowest total interest paid (shortest repayment period)
- Most common real-world choice

**Example:**
```
3 loans total:
  Subsidized: $105 min payment
  Unsubsidized: $189 min payment
  Private: $142 min payment

Total Monthly = $105 + $189 + $142 = $436
```

---

### Income-Driven Repayment (IDR)
```
Calculation:
  1. poverty_threshold = $15,000 * 1.5 * family_adjust
     (family_adjust = 1.0 + 0.35 * (family_size - 1))
  
  2. discretionary_income = max(0, annual_income - threshold)
  
  3. annual_payment = 10% * discretionary_income
  
  4. monthly_payment = annual_payment / 12
  
  5. (Optional cap) = min(idr_payment, standard_payment)
```

**Example: Fresh Graduate**
```
Annual Income: $35,000
Family Size: 1

Poverty Threshold: $15,000 * 1.5 * 1.0 = $22,500
Discretionary Income: $35,000 - $22,500 = $12,500
Annual Payment: 10% * $12,500 = $1,250
Monthly Payment: $1,250 / 12 ≈ $104

vs. Standard Min Payment: $436

IDR Benefit: $436 - $104 = $332/month savings
             = $39,840 over 10 years!
```

**With Family:**
```
Annual Income: $40,000
Family Size: 4

Family Adjust: 1.0 + 0.35 * 3 = 2.05
Poverty Threshold: $15,000 * 1.5 * 2.05 = $46,125
Discretionary Income: max(0, $40,000 - $46,125) = $0
Monthly Payment: $0

(Family protected from payments due to size)
```

**Educational Value:**
- Shows that low income can qualify for $0 payments
- Teaches that family size affects debt burden
- Demonstrates social safety nets for struggling borrowers
- Real-world: protects parents with young children

---

## 6. Interest Accrual Rules (Comprehensive)

### IN-SCHOOL Interest Accrual
```
For each month in school:
  Subsidized:
    Interest: NONE (government covers it)
    
  Unsubsidized:
    Accrued_Interest += Principal * (annual_rate / 12)
    
  Private:
    Accrued_Interest += Principal * (annual_rate / 12)
```

### GRACE PERIOD Interest Accrual
```
For each month in grace (months remaining > 0):
  Subsidized:
    Interest: NONE
    
  Unsubsidized:
    Accrued_Interest += Principal * (annual_rate / 12)
    
  Private:
    Accrued_Interest += Principal * (annual_rate / 12)
    (No grace anyway, but if there was...)
```

### REPAYMENT Interest Accrual
```
Each month after grace ends:
  For all loans in repayment:
    Principal += Principal * (annual_rate / 12)  ← Interest added to principal
    (Simplified model: accrued_interest already capitalized)
```

**Key Difference:**
- Pre-repayment: Interest accrues to `accrued_interest` field
- Post-repayment: Interest accrues directly to `principal` (and compounds)

---

## 7. Real-World Mechanics Simulated

### 1. Capitalization Trap
```
Student borrows $5,500 unsubsidized
In-school accrual (4 years): $5,500 * 5.5% * 4 = $1,210
Grace accrual (6 months): $5,500 * 5.5% / 12 * 6 = $151.25

Total before first repayment:
  Original: $5,500
  With interest: $6,861.25
  
Student owes 24% MORE than borrowed (just from accrual!)
```

**Educational Impact:** Students learn not to ignore loans during grace.

---

### 2. Interest-Only Torture
```
Private loan: $20,000 at 8.5%
Monthly interest accrual (in school/grace): 
  = $20,000 * 8.5% / 12 = $141.67 per month

Over 4 years + 6 month grace = 54 months:
  Total interest accrued = $141.67 * 54 = $7,650
  
Before making a single payment:
  Student owes: $27,650 (37% MORE!)
  
Capitalized principal: $27,650
Monthly payment on amortized 10-year: $289.27
Total repaid over 10 years: $289.27 * 120 = $34,712
Total interest during repayment: $34,712 - $27,650 = $7,062

TOTAL INTEREST COST: $7,650 + $7,062 = $14,712 (73% of original debt!)
```

**Lesson:** Private loans are expensive and compound quickly.

---

### 3. Payment Allocation (Avalanche Method)
```
Player owes:
  Loan A (Private 8.5%): $5,000
  Loan B (Unsubsidized 5.5%): $15,000
  Loan C (Subsidized 4.5%): $10,000

Payment available: $500/month

Month 1: Allocate to Loan A (highest rate) → A: $4,500, B: $15,000, C: $10,000
Month 2: Allocate to Loan A → A: $4,000, B: $15,000, C: $10,000
Month 3: Allocate to Loan A → A: $3,500, B: $15,000, C: $10,000
Month 4: Allocate to Loan A → A: $3,000, B: $15,000, C: $10,000
...
Month 11: Allocate to Loan A → A: $500 paid off, B: $15,000, C: $10,000
Month 12+: Allocate to Loan B (next highest)

Total Interest Saved (vs equal distribution): ~$1,200 over 10 years
```

**Lesson:** Debt strategy matters—pay high-rate debt first.

---

### 4. IDR Forgiveness (Implicit)
```
Player on IDR with:
  Income: $30,000
  Family Size: 1

Payment threshold: $22,500
Discretionary: $30,000 - $22,500 = $7,500
10% of discretionary: $750/year = $62.50/month

After 25 years of IDR payments:
  Total paid: $62.50 * 12 * 25 = $18,750
  Original debt: $80,000
  Remaining balance: $80,000 (potentially forgiven under real IDR)

Note: Game doesn't implement full 25-year forgiveness
      but shows the mechanism (low payments for low income)
```

**Lesson:** Income-driven plans can help with overwhelming debt, but balance is owed eventually.

---

## 8. API Endpoints (How to Use Finances)

### Endpoint 1: `/finance/borrow` (POST)
```
Request:
{
  "player_id": "abc123",
  "needed_amount": 10000
}

Response:
{
  "player_id": "abc123",
  "borrowed_total": 10000,
  "remaining_uncovered": 0,
  "new_balance": 11000,
  "loans": [
    {
      "id": "loan1",
      "loan_type": "subsidized",
      "principal": 2750,
      "accrued_interest": 0,
      ...
    },
    ...
  ]
}

Flow:
  Player needs tuition $10,000
  → Fills gap with loans (subsidized first)
  → Receives cash immediately
  → Interest begins accruing (depending on loan type)
```

---

### Endpoint 2: `/finance/accrue-in-school-interest` (POST)
```
Request:
{
  "player_id": "abc123",
  "months": 4
}

Response:
{
  "player_id": "abc123",
  "months": 4,
  "loans": [
    {
      "principal": 5500,
      "accrued_interest": 100.83,
      ...
    }
  ]
}

Purpose:
  Called at end of each semester (4 months)
  Simulates interest accrual during school
  Subsidized: no change
  Unsubsidized/Private: accrued_interest increases
```

---

### Endpoint 3: `/finance/start-repayment` (POST)
```
Request:
{
  "player_id": "abc123"
}

Response:
{
  "player_id": "abc123",
  "status": "loans moved out of school (grace countdown begins)",
  "loans": [...]
}

Purpose:
  Called when player graduates
  Transitions all loans to in_school = False
  Grace period begins (6 months for most, 0 for private)
  Interest continues accruing during grace
  When grace ends: capitalization + min payment calculation
```

---

### Endpoint 4: `/finance/set-repayment-profile` (POST)
```
Request:
{
  "player_id": "abc123",
  "plan_type": "idr",
  "annual_income": 35000,
  "family_size": 2
}

Response:
{
  "player_id": "abc123",
  "repayment_profile": {
    "plan_type": "idr",
    "annual_income": 35000,
    "family_size": 2
  }
}

Purpose:
  Player sets up repayment strategy after graduation
  Chooses: standard (fixed) or idr (income-based)
  Income/family size determine payment amount
  Can change anytime
```

---

### Endpoint 5: `/finance/repay-months` (POST)
```
Request:
{
  "player_id": "abc123",
  "months": 12
}

Response:
{
  "player_id": "abc123",
  "months": 12,
  "total_paid": 4320,
  "ending_balance": 5200,
  "total_principal_remaining": 45000,
  "loans": [...]
}

Purpose:
  Simulates paying loans for N months
  Automatically handles:
    - Grace period countdown
    - Capitalization when grace ends
    - Monthly interest accrual in repayment
    - Payment allocation (highest-rate first)
    - Minimum payment calculation
  Deducts from player.finance.balance
```

---

## 9. Default Starting Finances

```python
Player starts with:
  balance: $1,000 (starting cash)
  monthly_expenses: $350 (base) + housing
  tuition_per_semester: $5,000-$15,000 (by college tier)
  scholarship_per_semester: $0 (before scholarships awarded)
  
Loan portfolio: Empty (created on first borrow)
Repayment profile: 
  plan_type: "standard"
  annual_income: $0
  family_size: 1
```

**Game Progression:**
```
Semester 1: Borrow $X for tuition → loans created
Semesters 2-4: Continue borrowing → loans grow
Graduation: transition_loans_to_repayment() → grace period starts
Post-grad: set_repayment_profile() → choose repayment strategy
Years 1-10: repay_months() → gradually pay down debt
```

---

## 10. Educational Lessons Embedded

### Lesson 1: Debt Compounds
```
"Your interest accrues even when you're in school"
→ Subsidized loans avoid this (government pays)
→ Unsubsidized loans don't (you pay compound interest)
→ Private loans are worst (highest rate + immediate accrual)
```

### Lesson 2: Capitalization Surprises
```
"You owe more than you borrowed"
→ Interest accrued while in school + during grace
→ Gets added to principal
→ Interest then accrues ON TOP of that
→ Total debt can be 30-40% more than borrowed
```

### Lesson 3: Grace Periods Don't Stop Accrual
```
"Grace doesn't mean interest-free"
→ For unsubsidized/private loans
→ Grace delays repayment, not interest
→ Interest still accumulates and gets capitalized
→ Only subsidized loans truly have interest-free grace
```

### Lesson 4: Highest-Rate Debt First
```
"Pay down expensive loans first"
→ Private loans (8.5%) before Unsubsidized (5.5%)
→ Saves significant interest
→ Algorithm implements financially-optimal strategy
```

### Lesson 5: Income Affects Debt Burden
```
"Your income determines what you can pay"
→ Standard plan: fixed payment regardless of income
→ IDR plan: adjusts to income
→ Low income → very low payments (or $0)
→ High income → full standard payment or more
```

### Lesson 6: Career Choice Matters (Indirectly)
```
"Your major → job → income → repayment ability"
→ CS graduates can repay aggressively
→ History graduates might struggle (lower income)
→ Same debt load, very different repayment experiences
→ Career choice affects life beyond just salary
```

---

## 11. Configuration & Tuning

### Core Constants
```python
# core_domain/config.py
DEFAULT_START_BALANCE = 1000.0
DEFAULT_BASE_MONTHLY_NONHOUSING_EXPENSES = 350.0
SEM_MONTHS = 4  # months of interest per semester
```

### Loan Product Tuning
```python
# finance/loan_products.py
LOAN_PRODUCTS = {
    "subsidized": {
        "annual_interest_rate": 0.045,      # Can adjust
        "max_per_semester": 2750.0,         # Cap per semester
        "grace_months": 6,                  # Grace period
        "repayment_months": 120,            # 10 years
    },
    "unsubsidized": {
        "annual_interest_rate": 0.055,      # Slightly higher
        "max_per_semester": 5500.0,
        "grace_months": 6,
        "repayment_months": 120,
    },
    "private": {
        "annual_interest_rate": 0.085,      # Much higher
        "max_per_semester": 20000.0,        # Essentially unlimited
        "grace_months": 0,                  # NO GRACE
        "repayment_months": 120,
    },
}
```

### IDR Calculation Tuning
```python
# core_domain/finance/finance_models.py
poverty_line_annual: float = 15000.0           # Can adjust
discretionary_multiplier: float = 1.5          # Income safety margin
idr_percent: float = 0.10                      # 10% of discretionary
payment_cap_to_standard: bool = True           # Cap IDR at standard max
```

**Tuning Ideas:**
1. Increase loan caps (more expensive education)
2. Adjust interest rates (simulate different economic periods)
3. Change IDR poverty threshold (harder/easier qualification)
4. Add grace periods to private loans (less realistic but more forgiving)
5. Vary college tuition costs by major (STEM higher, humanities lower)

---

## 12. Real-World Accuracy

### What's Realistic
✅ Three loan types with accurate interest rates (2024 rates)
✅ Grace periods (6 months standard federal)
✅ Capitalization mechanics
✅ Standard amortization (10-year fixed payment)
✅ Income-Driven Repayment formula (similar to REPAYE)
✅ Highest-interest-rate-first payment allocation
✅ In-school interest for unsubsidized loans
✅ No grace for private loans

### What's Simplified
⚠️ IDR forgiveness not implemented (real: 25-year forgiveness)
⚠️ No income-based minimum payment floors (real: varies by plan type)
⚠️ No tax implications of forgiven debt (real: taxable income)
⚠️ No interest deduction limits (real: can deduct up to $2,500)
⚠️ No option to consolidate loans (real: very common)
⚠️ Loan origination fees not included (real: ~1%)
⚠️ No graduated repayment (real: payments increase over time)
⚠️ Unlimited balance allowed (real: eventually you can't pay, debt relief occurs)

---

## 13. Game Flow: Complete Financial Journey

```
AGE 18 (Start College)
├─ balance: $1,000
├─ First semester: Borrow $6,000
│  └─ Subsidized: $2,750
│  └─ Unsubsidized: $3,250
│  └─ balance: $7,000
└─ Pay living expenses: $350 × 4 = $1,400
   └─ balance: $5,600

AGE 18-22 (College Years - Each Semester)
├─ Accrue interest in school
│  └─ Subsidized: $0 (government pays)
│  └─ Unsubsidized: ~$60 (accrues)
│  └─ Total debt grows invisibly
├─ Borrow more (if needed) OR work jobs
│  └─ Income from job + borrowing covers expenses
└─ End of 4 years:
   └─ Borrowed total: ~$24,000
   └─ Accrued interest: ~$3,000 (capitalization pending)
   └─ Student doesn't realize true debt yet

AGE 22 (Graduation)
├─ transition_loans_to_repayment()
├─ Grace period begins (6 months)
│  └─ Interest continues accruing
│  └─ No payments required YET
└─ During grace: Interest accrues additional $500

AGE 22.5 (End of Grace)
├─ Capitalization:
│  └─ Principal + accrued_interest → Principal
│  └─ New principal: ~$27,500 (more than borrowed!)
├─ Minimum payment calculated: ~$260/month
├─ set_repayment_profile() (player chooses standard or IDR)
└─ Ready to repay

AGE 22.5-32.5 (Repayment Years 1-10)
├─ Each month:
│  ├─ Minimum payment due: $260
│  ├─ Player may have income (CS: $80K, History: $45K)
│  ├─ IDR payment varies by income:
│  │  └─ CS grad: ~$667/month (can pay extra → faster payoff)
│  │  └─ History grad: ~$200/month (barely makes headway)
│  └─ Loans gradually paid down
└─ End of 10 years:
   └─ CS graduate debt-free
   └─ History graduate still owes $15,000 (20+ year trajectory)

AGE 32.5+ (Post-Repayment)
├─ Debt eliminated or forgiven (25 years under IDR)
├─ Financial freedom (or continued burden)
└─ Lesson: Career choice affects long-term financial health
```

---

## 14. Why This Matters Educationally

Life Sprint's financial system teaches that:

1. **Borrowing is not free** - Interest compounds, especially unsubsidized
2. **Timing matters** - Grace period doesn't stop interest on some loans
3. **Type matters** - Private loans are expensive; subsidized loans are valuable
4. **Career choice cascades** - Income from major affects 10+ year repayment timeline
5. **Sacrifice is real** - $300-$600/month in loan payments means less money for life
6. **Strategy works** - Paying highest-rate debt first saves thousands
7. **Income protection exists** - IDR plans help low-income borrowers
8. **Nothing is free** - Government support (subsidized loans) is valuable but limited

Young players playing this game learn in **4 minutes of gameplay** what takes college students **years to understand about debt**.

---

## 15. Future Enhancement Ideas

### Phase 2: More Complexity
```
1. Scholarships reduce borrowing needs
2. Work-study income adds to player.finance.balance
3. Tuition varies by major (engineering: $18K, humanities: $10K)
4. Loan consolidation option (combines loans into single payment)
5. Public Service Loan Forgiveness (10 years if in government job)
6. Tax deduction for loan interest ($2,500/year)
```

### Phase 3: Real Consequences
```
1. Debt-to-income ratio affects housing (can't borrow for house)
2. Credit score tracking (loan payment history matters)
3. Personal/business decisions constrained by debt
4. Marriage/family planning affected by debt burden
5. Bankruptcy mechanics (ultimate escape, but scarring)
```

### Phase 4: Policy Exploration
```
1. Sliding scale tuition (income-based payment)
2. Debt forgiveness programs (public service, teaching, medicine)
3. Loan forgiveness percentage changes (simulate policy changes)
4. Interest rate changes (simulate market conditions)
5. Grace period variations by economic conditions
```

---

## Summary: Life Sprint Finance is a Teaching Tool

The financial system isn't just mechanics—it's a **structured learning environment** where:

- **Risk is real** (borrow $80K, owe $100K+)
- **Consequences are felt** (high stress job pays off debt faster)
- **Optimization is rewarded** (pay high-rate debt first, choose right plan)
- **Trade-offs are clear** (income > spending > debt reduction)
- **Complexity increases gradually** (borrow → accrue → capitalize → repay)

Players learn personal finance through **direct experience** rather than lectures, which is far more effective for long-term retention and decision-making.

---

**Status**: Fully Implemented & Realistic  
**Learning Goals**: Debt management, income-career linkage, financial strategy  
**Realism Level**: High (matches 2024 U.S. federal/private loan mechanics)
