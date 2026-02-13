"""Budgeting challenge system - teaches budget management and allocation."""

from typing import Dict, List, Optional, Literal, Any
from pydantic import BaseModel, Field


class BudgetCategory(BaseModel):
    """A budget spending category."""
    category_id: str
    category_name: str
    category_type: Literal["need", "want", "savings"]  # 50/30/20 rule
    
    description: str
    typical_percent_of_income: float  # For 50/30/20 or personalized
    examples: List[str] = Field(default_factory=list)


class Budget(BaseModel):
    """A monthly budget."""
    budget_id: str
    month: int
    year: int
    
    # Income
    monthly_income: float
    
    # Budget allocations
    needs_budget: float  # 50%
    wants_budget: float  # 30%
    savings_budget: float  # 20%
    
    # Actual spending by category
    actual_spending: Dict[str, float] = Field(default_factory=dict)
    
    # Results
    total_spent: float = 0
    remaining: float = 0
    over_budget: bool = False
    categories_over_budget: List[str] = Field(default_factory=list)


class BudgetChallenge(BaseModel):
    """A monthly budget challenge scenario."""
    challenge_id: str
    month: str
    
    # Starting conditions
    monthly_income: float
    starting_balance: float
    
    # Fixed expenses (must pay)
    rent_mortgage: float
    utilities: float
    insurance: float
    groceries: float
    transportation: float
    debt_minimum_payments: float
    
    # Variables (discretionary spending)
    dining_out_budget: float = 0
    entertainment_budget: float = 0
    shopping_budget: float = 0
    subscriptions: float = 0
    
    # Emergency/goals
    emergency_fund_goal: float = 0
    savings_goal: float = 0
    
    # Results
    total_expenses: float = 0
    surplus_deficit: float = 0
    challenge_outcome: Optional[str] = None


class BudgetMythFact(BaseModel):
    """Budget myths vs facts."""
    myth_id: str
    myth: str
    fact: str
    impact: Literal["major", "moderate", "minor"]


class BudgetTip(BaseModel):
    """A budgeting tip."""
    tip_id: str
    tip_name: str
    description: str
    example: str
    benefit: str
    difficulty: Literal["easy", "moderate", "hard"]


# Budget categories
BUDGET_CATEGORIES: Dict[str, BudgetCategory] = {
    # NEEDS (50%)
    "housing": BudgetCategory(
        category_id="housing",
        category_name="Housing",
        category_type="need",
        description="Rent or mortgage, property tax, maintenance",
        typical_percent_of_income=30,
        examples=["Rent", "Mortgage", "HOA fees", "Home repairs", "Property tax"]
    ),
    
    "food": BudgetCategory(
        category_id="food",
        category_name="Groceries",
        category_type="need",
        description="Food for cooking at home",
        typical_percent_of_income=8,
        examples=["Groceries", "Bulk items", "Costco"]
    ),
    
    "utilities": BudgetCategory(
        category_id="utilities",
        category_name="Utilities",
        category_type="need",
        description="Electricity, water, gas, internet",
        typical_percent_of_income=5,
        examples=["Electric bill", "Water bill", "Internet", "Phone"]
    ),
    
    "transportation": BudgetCategory(
        category_id="transportation",
        category_name="Transportation",
        category_type="need",
        description="Car payment, gas, insurance, maintenance",
        typical_percent_of_income=10,
        examples=["Car payment", "Gas", "Car insurance", "Maintenance"]
    ),
    
    "insurance": BudgetCategory(
        category_id="insurance",
        category_name="Insurance",
        category_type="need",
        description="Health, auto, home, life insurance",
        typical_percent_of_income=7,
        examples=["Health insurance", "Auto insurance", "Life insurance", "Renters"]
    ),
    
    "personal_care": BudgetCategory(
        category_id="personal_care",
        category_name="Personal Care",
        category_type="need",
        description="Hygiene, haircuts, medications",
        typical_percent_of_income=2,
        examples=["Haircuts", "Medications", "Hygiene products"]
    ),
    
    # WANTS (30%)
    "dining_out": BudgetCategory(
        category_id="dining_out",
        category_name="Dining Out",
        category_type="want",
        description="Restaurants, coffee shops, food delivery",
        typical_percent_of_income=10,
        examples=["Restaurants", "Coffee shops", "DoorDash", "Takeout"]
    ),
    
    "entertainment": BudgetCategory(
        category_id="entertainment",
        category_name="Entertainment",
        category_type="want",
        description="Movies, games, hobbies, concerts",
        typical_percent_of_income=8,
        examples=["Movies", "Concerts", "Gaming", "Hobbies"]
    ),
    
    "shopping": BudgetCategory(
        category_id="shopping",
        category_name="Shopping",
        category_type="want",
        description="Clothes, gadgets, non-essential items",
        typical_percent_of_income=7,
        examples=["Clothing", "Gadgets", "Decoration", "Accessories"]
    ),
    
    "subscriptions": BudgetCategory(
        category_id="subscriptions",
        category_name="Subscriptions",
        category_type="want",
        description="Netflix, Spotify, apps, memberships",
        typical_percent_of_income=5,
        examples=["Netflix", "Spotify", "Gym", "Apps", "Streaming services"]
    ),
    
    # SAVINGS (20%)
    "emergency_fund": BudgetCategory(
        category_id="emergency_fund",
        category_name="Emergency Fund",
        category_type="savings",
        description="Build 3-6 months of expenses",
        typical_percent_of_income=10,
        examples=["Savings account", "Emergency fund"]
    ),
    
    "retirement": BudgetCategory(
        category_id="retirement",
        category_name="Retirement",
        category_type="savings",
        description="401k, IRA, long-term investing",
        typical_percent_of_income=10,
        examples=["401k", "IRA", "Investments", "Pension"]
    ),
}


# Budgeting myths
BUDGET_MYTHS: Dict[str, BudgetMythFact] = {
    "myth_budget_restrictive": BudgetMythFact(
        myth_id="myth_budget_restrictive",
        myth="Budgets are too restrictive and take the fun out of life.",
        fact="Budgets do the opposite! They give you permission to spend on wants within limits. Without a budget, you don't know if you can afford that $200 purchase.",
        impact="major"
    ),
    
    "myth_budget_for_poor": BudgetMythFact(
        myth_id="myth_budget_for_poor",
        myth="You only need a budget if you're broke.",
        fact="Wrong. Millionaires budget religiously. Budgets are how you decide money allocation. No budget = no intentional spending = money disappears.",
        impact="major"
    ),
    
    "myth_needs_vs_wants": BudgetMythFact(
        myth_id="myth_needs_vs_wants",
        myth="Phone/internet are 'wants' so I can skip them.",
        fact="In modern life, phone and internet are 'needs' for communication and often job requirements. Budgets should reflect YOUR life, not generic rules.",
        impact="moderate"
    ),
    
    "myth_zero_based": BudgetMythFact(
        myth_id="myth_zero_based",
        myth="You need to spend every dollar of your budget or it's wasted.",
        fact="If your budget is $200 entertainment and you only spend $150, GREAT! You saved $50. Budgets are ceilings, not targets.",
        impact="moderate"
    ),
    
    "myth_budget_weekly": BudgetMythFact(
        myth_id="myth_budget_weekly",
        myth="You need to balance your budget perfectly every week.",
        fact="Think monthly or quarterly. Some weeks you spend more, some less. As long as monthly average matches budget, you're fine.",
        impact="minor"
    ),
}


# Budgeting tips
BUDGETING_TIPS: Dict[str, BudgetTip] = {
    "50_30_20_rule": BudgetTip(
        tip_id="50_30_20_rule",
        tip_name="50/30/20 Rule",
        description="Allocate 50% to needs, 30% to wants, 20% to savings",
        example="$3,000 income: $1,500 needs, $900 wants, $600 savings",
        benefit="Simple framework that covers all your bases and forces savings",
        difficulty="easy"
    ),
    
    "envelope_method": BudgetTip(
        tip_id="envelope_method",
        tip_name="Envelope Method",
        description="Allocate physical or digital 'envelopes' for each category. When envelope is empty, stop spending.",
        example="Dining out budget = $300. Once you spend $300 at restaurants, no more until next month.",
        benefit="Forces discipline. Can't overspend in one category without moving money from another.",
        difficulty="moderate"
    ),
    
    "zero_based_budget": BudgetTip(
        tip_id="zero_based_budget",
        tip_name="Zero-Based Budget",
        description="Assign every dollar a job. Income - Expenses = $0 (not left unaccounted)",
        example="$3,000 income: $1,500 needs, $500 wants, $600 savings, $400 debt payoff = $0 remaining",
        benefit="Forces intentional decisions. No money left unaccounted for.",
        difficulty="hard"
    ),
    
    "track_actual_spending": BudgetTip(
        tip_id="track_actual_spending",
        tip_name="Track Actual Spending",
        description="Write down or track every purchase. Compare to budget.",
        example="Budget $300 dining out. Actual: $350. Now you know you overspent and need to adjust.",
        benefit="Data-driven decisions. See where money actually goes vs. where you think it goes.",
        difficulty="moderate"
    ),
    
    "cut_subscriptions": BudgetTip(
        tip_id="cut_subscriptions",
        tip_name="Audit Subscriptions Quarterly",
        description="List all recurring subscriptions (Netflix, Spotify, gym, apps). Cancel unused ones.",
        example="Audit reveals: 3 streaming services you forgot about = $45/month = $540/year",
        benefit="Average person wastes $100+/year on unused subscriptions. Quick savings.",
        difficulty="easy"
    ),
    
    "income_changes": BudgetTip(
        tip_id="income_changes",
        tip_name="Recalculate Budget When Income Changes",
        description="When you get a raise, new job, or lose income, update your budget immediately.",
        example="Got 10% raise (+$300/month). Increase savings/debt payoff by $300, not wants.",
        benefit="Prevents lifestyle creep. Extra income goes to goals, not lifestyle inflation.",
        difficulty="easy"
    ),
    
    "separate_accounts": BudgetTip(
        tip_id="separate_accounts",
        tip_name="Separate Savings Accounts by Goal",
        description="Create different accounts for emergency fund, vacation, emergency car repair, etc.",
        example="3 savings accounts: Emergency fund, car repair, vacation. Easier to track progress.",
        benefit="Psychological win seeing progress toward each goal. Less temptation to spend.",
        difficulty="moderate"
    ),
}


def create_budget(
    monthly_income: float,
    budgeting_method: Literal["50_30_20", "custom"] = "50_30_20"
) -> Budget:
    """Create a budget for a player."""
    
    if budgeting_method == "50_30_20":
        needs = monthly_income * 0.50
        wants = monthly_income * 0.30
        savings = monthly_income * 0.20
    else:
        # Custom - assume balanced
        needs = monthly_income * 0.50
        wants = monthly_income * 0.30
        savings = monthly_income * 0.20
    
    return Budget(
        budget_id=f"budget_{monthly_income}_{budgeting_method}",
        month=1,
        year=2026,
        monthly_income=monthly_income,
        needs_budget=needs,
        wants_budget=wants,
        savings_budget=savings,
        actual_spending={},
        total_spent=0,
        remaining=monthly_income
    )


def add_spending_to_budget(
    budget: Budget,
    category: str,
    amount: float
) -> Budget:
    """Add spending to a category in the budget."""
    
    if category not in budget.actual_spending:
        budget.actual_spending[category] = 0
    
    budget.actual_spending[category] += amount
    budget.total_spent += amount
    budget.remaining = budget.monthly_income - budget.total_spent
    
    return budget


def check_budget_status(budget: Budget) -> Dict[str, Any]:
    """Check if budget categories are under control."""
    
    # Estimate category type totals
    needs_total = sum(v for k, v in budget.actual_spending.items() 
                      if k in ["housing", "food", "utilities", "transportation", "insurance", "personal_care"])
    wants_total = sum(v for k, v in budget.actual_spending.items() 
                      if k in ["dining_out", "entertainment", "shopping", "subscriptions"])
    savings_total = sum(v for k, v in budget.actual_spending.items() 
                        if k in ["emergency_fund", "retirement"])
    
    return {
        "needs": {
            "budget": budget.needs_budget,
            "actual": needs_total,
            "over_budget": needs_total > budget.needs_budget,
            "remaining": budget.needs_budget - needs_total
        },
        "wants": {
            "budget": budget.wants_budget,
            "actual": wants_total,
            "over_budget": wants_total > budget.wants_budget,
            "remaining": budget.wants_budget - wants_total
        },
        "savings": {
            "budget": budget.savings_budget,
            "actual": savings_total,
            "over_budget": savings_total > budget.savings_budget,
            "remaining": budget.savings_budget - savings_total
        },
        "total_spent": budget.total_spent,
        "total_budget": budget.monthly_income,
        "remaining": budget.remaining,
        "on_track": not (needs_total > budget.needs_budget or wants_total > budget.wants_budget)
    }


def get_budget_insights(budget: Budget) -> Dict[str, Any]:
    """Get insights about spending patterns."""
    
    status = check_budget_status(budget)
    
    insights = []
    
    if status["needs"]["over_budget"]:
        insights.append(f"⚠️ Needs are over budget by ${status['needs']['remaining'] * -1:.2f}")
    
    if status["wants"]["over_budget"]:
        insights.append(f"📊 Wants are over budget by ${status['wants']['remaining'] * -1:.2f}")
    
    if status["savings"]["actual"] == 0:
        insights.append("❌ Not saving anything this month! Prioritize savings to build wealth.")
    elif status["savings"]["actual"] < status["savings"]["budget"] * 0.8:
        insights.append(f"📉 Savings are only ${status['savings']['actual']:.2f}. Try to hit ${status['savings']['budget']:.2f}")
    else:
        insights.append(f"✅ On track with savings! ${status['savings']['actual']:.2f} saved.")
    
    if status["remaining"] > 0:
        insights.append(f"💰 Extra ${status['remaining']:.2f} remaining. Add to savings or invest!")
    elif status["remaining"] < 0:
        insights.append(f"⚠️ Over budget by ${status['remaining'] * -1:.2f}. Cut spending or find more income.")
    
    return {
        "status": status,
        "insights": insights
    }


def get_category(category_id: str) -> Optional[BudgetCategory]:
    """Get a budget category."""
    return BUDGET_CATEGORIES.get(category_id)


def get_all_categories() -> List[BudgetCategory]:
    """Get all budget categories."""
    return list(BUDGET_CATEGORIES.values())


def get_categories_by_type(category_type: str) -> List[BudgetCategory]:
    """Get categories by type (need, want, savings)."""
    return [c for c in BUDGET_CATEGORIES.values() if c.category_type == category_type]


def get_tip(tip_id: str) -> Optional[BudgetTip]:
    """Get a budgeting tip."""
    return BUDGETING_TIPS.get(tip_id)


def get_all_tips() -> List[BudgetTip]:
    """Get all budgeting tips."""
    return list(BUDGETING_TIPS.values())


def get_myth(myth_id: str) -> Optional[BudgetMythFact]:
    """Get a budgeting myth."""
    return BUDGET_MYTHS.get(myth_id)


def get_all_myths() -> List[BudgetMythFact]:
    """Get all budgeting myths."""
    return list(BUDGET_MYTHS.values())
