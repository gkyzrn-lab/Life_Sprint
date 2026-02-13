"""Tax rules, expense definitions, and financial surprise mechanics.

This is the "surprise" mechanic that teaches real-world financial responsibility:
- Taxes are a surprise (players don't expect 25-35% of earnings to vanish)
- Living expenses add up fast
- Emergency expenses happen when you don't expect them
- Financial stress is real and affects health
"""

# 2026 US Federal Tax Brackets (single filer)
# Realistic tax brackets for young adult income
FEDERAL_TAX_BRACKETS = [
    {"min": 0, "max": 11000, "rate": 0.10},  # 10%
    {"min": 11000, "max": 44725, "rate": 0.12},  # 12%
    {"min": 44725, "max": 95375, "rate": 0.22},  # 22%
    {"min": 95375, "max": 182100, "rate": 0.24},  # 24%
    {"min": 182100, "max": 231250, "rate": 0.32},  # 32%
    {"min": 231250, "max": 578125, "rate": 0.35},  # 35%
    {"min": 578125, "max": float('inf'), "rate": 0.37},  # 37%
]

# State tax varies by state; we'll use average (3-5%)
STATE_TAX_RATES = {
    "ca": 0.093,  # California high
    "ny": 0.065,  # New York
    "tx": 0.0,    # Texas (no state income tax)
    "fl": 0.0,    # Florida (no state income tax)
    "general": 0.04,  # Average state tax
}

# FICA = Federal Insurance Contributions Act (Social Security + Medicare)
FICA_RATE = 0.0765  # 6.2% Social Security + 1.45% Medicare = 7.65%

# Standard deduction (reduces taxable income)
STANDARD_DEDUCTION = 14600  # 2026 estimate for single filer

# Tax surprise mechanic
TAX_SURPRISE = {
    "description": "Most young adults are shocked to learn that 25-35% of their earnings disappear to taxes",
    "typical_effective_rate": 0.28,  # 28% total taxes (federal + state + FICA)
    "entry_level_surprise": 0.25,  # 25% for low-income jobs
    "mid_career_surprise": 0.32,  # 32% for mid-tier jobs
    "high_career_surprise": 0.37,  # 37%+ for high earners
}

# Base monthly expenses by housing type
BASE_MONTHLY_EXPENSES = {
    "on_campus_dorm": {
        "rent": 500,  # included in housing cost
        "utilities": 0,  # included
        "food": 200,  # meal plan not included, extra food
        "transport": 30,  # campus bus pass
        "insurance": 20,  # renters insurance (cheap)
        "entertainment": 50,  # modest
        "phone": 50,
        "total": 350,
    },
    "off_campus_shared": {
        "rent": 600,  # split 2-3 ways
        "utilities": 60,  # split
        "food": 250,
        "transport": 60,  # bus or car
        "insurance": 30,  # renters
        "entertainment": 75,
        "phone": 50,
        "total": 1125,
    },
    "off_campus_alone": {
        "rent": 1200,  # full rent
        "utilities": 120,  # full utilities
        "food": 300,  # eating out more
        "transport": 100,  # car costs
        "insurance": 40,  # renters + car
        "entertainment": 100,
        "phone": 50,
        "total": 1910,
    },
    "with_parents": {
        "rent": 0,  # free
        "utilities": 0,
        "food": 150,  # contribute to household
        "transport": 80,  # gas or car payment
        "insurance": 20,
        "entertainment": 100,
        "phone": 50,
        "total": 400,
    },
}

# Unexpected expenses (the "surprise" part of the system)
UNEXPECTED_EXPENSE_POOL = {
    "medical": [
        {"name": "Emergency room visit", "amount": 800, "severity": "moderate"},
        {"name": "Root canal", "amount": 1200, "severity": "major"},
        {"name": "Mental health crisis intervention", "amount": 1500, "severity": "major"},
        {"name": "Prescription shortage", "amount": 200, "severity": "minor"},
        {"name": "Urgent care visit", "amount": 400, "severity": "moderate"},
    ],
    "car_repair": [
        {"name": "Brake job", "amount": 600, "severity": "moderate"},
        {"name": "Transmission problem", "amount": 3000, "severity": "major"},
        {"name": "Engine overheating repair", "amount": 1500, "severity": "major"},
        {"name": "Tire replacement", "amount": 400, "severity": "moderate"},
        {"name": "Battery replacement", "amount": 200, "severity": "minor"},
    ],
    "emergency": [
        {"name": "Flight home (family emergency)", "amount": 800, "severity": "major"},
        {"name": "Lost laptop replacement", "amount": 1000, "severity": "major"},
        {"name": "Broken phone (not covered by insurance)", "amount": 600, "severity": "moderate"},
        {"name": "Apartment flooded (security deposit at risk)", "amount": 500, "severity": "moderate"},
    ],
    "replacement": [
        {"name": "Clothes replacement (all in washer incident)", "amount": 400, "severity": "moderate"},
        {"name": "Kitchen appliance failure", "amount": 300, "severity": "moderate"},
        {"name": "Computer replacement", "amount": 1200, "severity": "major"},
    ],
}

# Financial achievements
FINANCIAL_ACHIEVEMENTS = {
    "first_tax_filing": {
        "achievement_id": "first_tax_filing",
        "title": "Taxes Are Real 💸",
        "milestone_type": "responsibility",
        "description": "Filed your first tax return. You now understand: taxes are a big surprise.",
        "tier": "bronze",
    },
    "emergency_fund_starter": {
        "achievement_id": "emergency_fund_starter",
        "title": "Safety Net",
        "milestone_type": "savings",
        "description": "Built a 1-month emergency fund. Unexpected expenses won't break you.",
        "tier": "bronze",
    },
    "emergency_fund_solid": {
        "achievement_id": "emergency_fund_solid",
        "title": "Prepared 🛡️",
        "milestone_type": "savings",
        "description": "3-month emergency fund. You can handle most unexpected expenses.",
        "tier": "silver",
    },
    "budget_master": {
        "achievement_id": "budget_master",
        "title": "Budget Master",
        "milestone_type": "budget_master",
        "description": "Tracked expenses for entire year. You know exactly where your money goes.",
        "tier": "silver",
    },
    "debt_free": {
        "achievement_id": "debt_free",
        "title": "Debt Free! 🎉",
        "milestone_type": "debt_free",
        "description": "Paid off all credit card and emergency debt. Only student loans remain.",
        "tier": "gold",
    },
    "ten_thousand_saved": {
        "achievement_id": "ten_thousand_saved",
        "title": "$10k Saved",
        "milestone_type": "wealth",
        "description": "$10,000 in emergency fund + investments. You're building real wealth.",
        "tier": "gold",
    },
    "financial_responsibility": {
        "achievement_id": "financial_responsibility",
        "title": "Financial Adult 💼",
        "milestone_type": "responsibility",
        "description": "Low financial stress, budget under control, emergency fund solid, debt minimal.",
        "tier": "platinum",
    },
}

# Financial stress mechanics
FINANCIAL_STRESS_MECHANICS = {
    "debt_ratio_thresholds": {
        "healthy": 0.2,  # debt < 20% of annual income = low stress
        "concerned": 0.5,  # 20-50% = moderate stress
        "stressed": 1.0,  # 50-100% = high stress
        "crisis": float('inf'),  # >100% = bankruptcy risk
    },
    "emergency_fund_thresholds": {
        "excellent": 6,  # 6+ months of expenses
        "good": 3,  # 3-6 months
        "okay": 1,  # 1-3 months
        "insufficient": 0.25,  # <1 month
        "none": 0,  # zero savings
    },
    "health_impact_per_stress": {
        "mental_health": -1.0,  # -1 mental health per stress point per semester
        "physical_health": -0.3,  # -0.3 physical health per stress point (less direct)
        "sleep_quality": -0.8,  # affects sleep/recovery
    },
}

# Financial literacy progression
FINANCIAL_LITERACY_TOPICS = {
    "taxes": {
        "name": "Understanding Taxes",
        "trigger": "first_paycheck_after_taxes",
        "insights": [
            "Federal income tax is progressive (higher income = higher rate)",
            "State taxes vary by location (some states have no income tax)",
            "FICA (Social Security + Medicare) is 7.65% of all earnings",
            "Total effective tax rate is usually 25-35% for young adults",
            "Taxes are withheld from paycheck (you won't see them coming)",
        ],
    },
    "budgeting": {
        "name": "Budgeting Basics",
        "trigger": "first_unexpected_expense",
        "insights": [
            "Unexpected expenses WILL happen",
            "Emergency fund should cover 3-6 months of living expenses",
            "Monthly expenses add up fast",
            "Fixed costs (rent) vs variable costs (food, entertainment)",
            "Budget should account for 10-20% of income going to savings",
        ],
    },
    "debt": {
        "name": "Debt Management",
        "trigger": "debt_ratio_above_threshold",
        "insights": [
            "Debt-to-income ratio should be < 30% for healthy finances",
            "Credit card debt is dangerous (20%+ interest rates)",
            "Student loans are manageable but need repayment strategy",
            "Emergency debt (credit card) should be priority to pay off",
            "High debt increases stress and affects health",
        ],
    },
    "wealth": {
        "name": "Building Wealth",
        "trigger": "saved_10000_or_more",
        "insights": [
            "Emergency fund comes FIRST before investing",
            "Compound interest is your friend (save early, invest often)",
            "Small consistent savings > large sporadic deposits",
            "Wealth building is boring but it works",
            "Financial security reduces stress and improves quality of life",
        ],
    },
}

# Financial stories (moments of realization)
FINANCIAL_STORIES = {
    "first_paycheck_shock": {
        "story_id": "first_paycheck_shock",
        "title": "Wait... Where's My Money? 😲",
        "trigger": "first_paycheck_after_taxes",
        "message": "Your paycheck arrives. You calculated $2,000 gross. But it's only $1,450 take-home. Federal tax, state tax, Social Security, Medicare... nearly 30% is gone. To taxes. You didn't even see it coming.",
        "tone": "shock",
        "effect_stress": 15,
        "effect_literacy": 30,  # Major tax awareness boost
    },
    "unexpected_medical": {
        "story_id": "unexpected_medical",
        "title": "Medical Bill 💊",
        "trigger": "medical_emergency",
        "message": "The emergency room bill arrives. $1,200. Even with the 'discount for uninsured,' it's brutal. Your emergency fund has just been decimated. You realize: one accident, one illness, one wrong turn, and you're in debt.",
        "tone": "cautionary",
        "effect_stress": 20,
        "effect_literacy": 25,  # Budget/emergency fund awareness
    },
    "rent_crunch": {
        "story_id": "rent_crunch",
        "title": "Rent Is Due Tomorrow 🏠",
        "trigger": "rent_approaching_tight_budget",
        "message": "Rent is due tomorrow and you've got exactly enough. No buffer. One unexpected expense and you're borrowing money on credit cards at 20% interest. This is what people mean by 'living paycheck to paycheck.'",
        "tone": "urgent",
        "effect_stress": 25,
    },
    "debt_realization": {
        "story_id": "debt_realization",
        "title": "The Debt Spiral",
        "trigger": "credit_card_debt_above_3000",
        "message": "You add up your debt: $5,000 in credit cards at 22% interest, $30,000 in student loans, $800 you owe your parents. You do the math: it'll take 5+ years to pay this off if you don't earn much more. The weight is real.",
        "tone": "cautionary",
        "effect_stress": 30,
    },
    "unexpected_car_repair": {
        "story_id": "unexpected_car_repair",
        "title": "The Car Breaks Down",
        "trigger": "car_emergency_expense",
        "message": "Your car needs a transmission repair: $2,500. You don't have it. You consider: Do you use a credit card (20% interest)? Skip meals? Borrow from family? You're learning the hard way: one large unexpected expense can derail your whole financial plan.",
        "tone": "cautionary",
        "effect_stress": 25,
    },
    "emergency_fund_saves": {
        "story_id": "emergency_fund_saves",
        "title": "Crisis Averted 🛡️",
        "trigger": "emergency_fund_covered_unexpected",
        "message": "Your laptop dies. $1,000 repair. But you have an emergency fund with $1,200 in it. You handle it without credit cards, without stress, without derailing your goals. This is why emergency funds exist. You're on the right track.",
        "tone": "triumphant",
        "effect_stress": -10,
        "effect_literacy": 20,
    },
    "tax_bill_surprise": {
        "story_id": "tax_bill_surprise",
        "title": "Tax Day 📋",
        "trigger": "tax_filing",
        "message": "Tax season arrives. You owe another $400 because of 1099 income (freelance work). You thought taxes were already handled. Nope. Self-employment taxes are YOUR responsibility. You learn: taxes are complicated.",
        "tone": "cautionary",
        "effect_stress": 15,
    },
    "freedom_moment": {
        "story_id": "freedom_moment",
        "title": "Financial Peace 😌",
        "trigger": "low_stress_solid_budget",
        "message": "You check your accounts: $6,000 emergency fund, debt down to just student loans, monthly budget under control, $200/month going to savings. For the first time, you don't feel money stress. This is what financial stability feels like.",
        "tone": "triumphant",
        "effect_stress": -20,
        "effect_literacy": 15,
    },
}

# Tax filing mechanics
TAX_FILING = {
    "filing_deadline": "April 15",  # in game, happens at certain month
    "standard_deduction": STANDARD_DEDUCTION,
    "surprise_additional_tax_percentage": 0.05,  # 5% extra owed from miscalculation
    "quarterly_estimated_taxes": 0.25,  # if freelance income, owe quarterly
}
