# 💰 Finance Module - Loans, Borrowing & Repayment

Handles all money-related game mechanics: loans, borrowing, interest, repayment plans.

## 📁 Files

```
finance/
├── service.py           ← Main logic (START HERE!)
├── loan_products.py     ← Loan types & terms
├── calculators.py       ← Math (amortization, IDR payments)
└── __init__.py
```

## 🎮 How Finance Works

### 1. **Borrowing for Semester**
```python
from finance.service import borrow_for_semester

# Player needs money for tuition
borrowed = borrow_for_semester(player, 5000)
# Returns: 5000
# Automatically allocated: subsidized → unsubsidized → private
```

**Key facts:**
- Money borrowed is added to `player.finance.balance`
- Automatically fills subsidized loans first (lowest interest)
- Then unsubsidized, then private (if available)
- Each loan type has a cap (see `loan_products.py`)

### 2. **Interest Accrual (In School)**
```python
from finance.service import accrue_interest_in_school

# At end of semester
accrue_interest_in_school(player, months=4)
```

**Key facts:**
- Subsidized: NO interest (government pays)
- Unsubsidized: Interest accrues to `accrued_interest` field
- Private: Interest accrues
- Interest is calculated: `principal * (annual_rate / 12) * months`

### 3. **Graduation → Repayment**
```python
from finance.service import transition_loans_to_repayment

# When player graduates
transition_loans_to_repayment(player)
# Sets in_school=False for all loans
# Grace period countdown begins (usually 6 months)
```

### 4. **Grace Period**
```python
# During grace (unsubsidized/private):
# - Interest accrues (but not applied to principal yet)
# - Subsidized loans: no interest

# When grace ends:
# - Accrued interest added to principal (capitalization)
# - Minimum payment calculated (standard amortization)
```

### 5. **Making Payments**
```python
from finance.service import repay_months

# Player makes payments for 12 months
paid = repay_months(player, months=12)
# Returns: total amount paid
```

**Process each month:**
1. Advance grace countdown (if still in grace)
2. Apply monthly interest to principal
3. Determine payment amount (based on plan type)
4. Allocate payment (highest interest rate first)
5. Deduct from `player.finance.balance`

## 📊 Loan Types

From `loan_products.py`:

| Type | APR | Grace Months | Cap/Semester | Notes |
|------|-----|--------------|--------------|-------|
| Subsidized | 4.5% | 6 | $2,625 | Gov't pays interest in school |
| Unsubsidized | 5.5% | 6 | $7,500 | Interest accrues in school |
| Private | 7.0% | 6 | $20,000 | No special terms |

## 🧮 Key Calculations

### Amortized Payment (Standard Repayment)
```python
from finance.calculators import amortized_payment

# Calculate fixed monthly payment
monthly = amortized_payment(
    principal=100000,
    annual_rate=0.05,
    months=120
)
# Returns: ~943.56 per month
```

Formula:
```
M = P * [r(1+r)^n] / [(1+r)^n - 1]

Where:
- M = monthly payment
- P = principal
- r = monthly interest rate (annual/12)
- n = number of months
```

### IDR Payment (Income-Driven Repayment)
```python
from finance.calculators import compute_idr_monthly_payment

# Calculate IDR payment based on income
payment = compute_idr_monthly_payment(repayment_profile)
# Generally: 10-15% of discretionary income
```

## 🛠️ Important Functions

### `borrow_for_semester(player, needed_amount) → float`
Borrow money, return amount actually borrowed.

```python
# Player needs $5,000
borrowed = borrow_for_semester(player, 5000)
# Returns: 5000 (added to balance)

# Player needs $100,000 (over annual cap)
borrowed = borrow_for_semester(player, 100000)
# Returns: 45750 (actual cap per year)
```

### `accrue_interest_in_school(player, months) → None`
Add interest during school years.

```python
# End of semester (4 months)
accrue_interest_in_school(player, 4)
# Unsubsidized loans get interest added to accrued_interest
```

### `transition_loans_to_repayment(player) → None`
Called when player graduates.

```python
transition_loans_to_repayment(player)
# All loans: in_school = False
# Grace countdown starts
```

### `repay_months(player, months) → float`
Simulate N months of repayment, return amount paid.

```python
# Make 12 months of payments
paid = repay_months(player, 12)
# Returns: actual amount paid (might be less if insufficient balance)
```

### `set_repayment_profile(player, plan_type, annual_income, family_size) → None`
Configure repayment plan.

```python
# Switch to income-driven repayment
set_repayment_profile(
    player,
    plan_type="idr",
    annual_income=45000,
    family_size=1
)
```

## 🔑 Key Data Structures

### Player Finance
```python
player.finance = Finance(
    balance=5000,              # Cash on hand
    monthly_expenses=1200,     # Costs to pay each month
    tuition_per_semester=3000, # Tuition bill
    scholarship_per_semester=0,# Scholarship amount
    loan_portfolio=LoanPortfolio(...),  # All loans
    repayment_profile=RepaymentProfile(...)  # How to repay
)
```

### Individual Loan
```python
loan = Loan(
    id="uuid",
    loan_type=LoanType.subsidized,
    principal=5500,              # Current balance
    annual_interest_rate=0.045,
    accrued_interest=0,          # Interest not yet in principal
    in_school=True,
    grace_months_remaining=6,
    repayment_months_remaining=120,
    minimum_payment=945.23
)
```

### Repayment Profile
```python
profile = RepaymentProfile(
    plan_type=RepaymentPlanType.standard,  # or idr
    annual_income=45000,
    family_size=1,
    payment_cap_to_standard=True  # IDR capped at standard
)
```

## 🧪 Common Use Cases

### Use Case 1: Player borrows for semester
```python
# Tuition is $3,000, player has $2,000
# Borrow the difference
borrow_for_semester(player, 1000)
player.finance.balance  # Now: 3000
```

### Use Case 2: End of semester
```python
# Accrue interest (if not graduating)
accrue_interest_in_school(player, 4)

# OR if graduating:
transition_loans_to_repayment(player)
```

### Use Case 3: During repayment (post-graduation)
```python
# Each month
repay_months(player, 1)

# Or multiple months at once
repay_months(player, 12)
```

### Use Case 4: Switch repayment plan
```python
# Change to income-driven repayment
set_repayment_profile(player, "idr", annual_income=50000, family_size=1)

# Next payment calculation uses new plan
repay_months(player, 1)  # Uses IDR formula
```

## 📈 Loan Lifecycle

```
1. BORROWING
   - Player needs money
   - borrow_for_semester() called
   - Loans created/expanded
   - Money added to balance

2. IN SCHOOL
   - accrue_interest_in_school() called each semester
   - Subsidized: no interest
   - Unsubsidized/Private: interest adds to accrued_interest
   - balance decreases as player spends

3. GRADUATION
   - transition_loans_to_repayment() called
   - in_school = False
   - Grace period countdown begins

4. GRACE PERIOD
   - If unsubsidized/private: interest keeps accruing
   - When grace ends: interest capitalized into principal

5. REPAYMENT
   - repay_months() called regularly
   - Interest applied to principal each month
   - Payment allocated (highest rate first)
   - Until paid off (principal = 0)
```

## ⚠️ Important Rules

1. **Capitalization**: Only happens when grace ends, not at start
2. **Subsidized Special**: No interest during school OR grace
3. **Highest Rate First**: Payment prioritizes highest interest loans
4. **Balance Limited**: Can't pay more than cash on hand (v1)
5. **Grace Optional**: Some loans might have 0 grace months

## 🧪 Testing Finance

```bash
pytest tests/test_finance.py -v
```

Key test areas:
- Borrowing with caps
- Interest accrual
- Grace period logic
- Repayment allocation
- IDR vs Standard payments

## 🔗 Related Code

- **Models**: `core_domain/finance/finance_models.py`
- **Config**: `core_domain/config.py` (tuition constants)
- **Router**: `api/router_finance.py` (endpoints)
- **Tests**: `tests/test_finance.py`

## 💡 Pro Tips

1. Always check `loan.principal > 0` before processing (some might be paid off)
2. Use `_total_principal_and_interest()` to see total debt
3. Interest rates are annual (divide by 12 for monthly)
4. `player.finance.balance` is cash on hand (not net worth)
5. Test with `borrow_for_semester()` first, it's simpler

## ✅ Checklist: Modifying Finance Logic

1. [ ] Understand current implementation in `service.py`
2. [ ] Check affected loan types in `loan_products.py`
3. [ ] Review calculations in `calculators.py`
4. [ ] Update relevant test in `tests/test_finance.py`
5. [ ] Run: `pytest tests/test_finance.py -v`
6. [ ] Test manual scenario with small numbers
7. [ ] Check repayment works end-to-end
