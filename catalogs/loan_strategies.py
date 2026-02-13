"""Student loan payoff strategy calculator for Life Sprint.

Teaches students:
- Avalanche vs Snowball repayment methods
- Income-driven repayment plans
- Public Service Loan Forgiveness (PSLF)
- Refinancing trade-offs
- Extra payment impact
- Total interest cost comparison
"""

from typing import Dict, List, Optional, Literal
from pydantic import BaseModel, Field
import math


class LoanForComparison(BaseModel):
    """A student loan for strategy comparison."""
    loan_id: str
    name: str
    principal: float
    annual_interest_rate: float
    loan_type: Literal["federal_subsidized", "federal_unsubsidized", "private"]


class RepaymentStrategy(BaseModel):
    """A student loan repayment strategy."""
    strategy_name: Literal["avalanche", "snowball", "standard", "idr", "pslf"]
    description: str
    pros: List[str] = Field(default_factory=list)
    cons: List[str] = Field(default_factory=list)
    best_for: str = ""


class PayoffProjection(BaseModel):
    """Projection of loan payoff under a specific strategy."""
    strategy: str
    monthly_payment: float
    months_to_payoff: int
    total_paid: float
    total_interest: float
    
    # Year-by-year breakdown
    year_breakdown: List[Dict[str, float]] = Field(default_factory=list)
    
    # Educational insights
    interest_saved_vs_minimum: float = 0.0
    time_saved_months: int = 0


class ExtraPaymentImpact(BaseModel):
    """Impact of making extra payments."""
    extra_payment_monthly: float
    
    # Original vs with extra payments
    original_months: int
    new_months: int
    months_saved: int
    
    original_total_interest: float
    new_total_interest: float
    interest_saved: float
    
    # ROI
    total_extra_paid: float
    roi_ratio: float  # interest_saved / total_extra_paid


class LoanPayoffComparison(BaseModel):
    """Complete comparison of all repayment strategies."""
    loans: List[LoanForComparison]
    total_principal: float
    
    # Strategy projections
    avalanche_projection: PayoffProjection
    snowball_projection: PayoffProjection
    standard_projection: PayoffProjection
    idr_projection: Optional[PayoffProjection] = None
    
    # Recommendations
    best_for_savings: str  # Which strategy saves most money
    best_for_motivation: str  # Which gives quick wins
    best_for_forgiveness: str  # If eligible for PSLF
    
    # Extra payment scenarios
    extra_50_impact: ExtraPaymentImpact
    extra_100_impact: ExtraPaymentImpact
    extra_200_impact: ExtraPaymentImpact


# Repayment strategy descriptions
REPAYMENT_STRATEGIES: Dict[str, RepaymentStrategy] = {
    "avalanche": RepaymentStrategy(
        strategy_name="avalanche",
        description="Pay minimums on all loans, then put extra toward highest interest rate loan first. Mathematically optimal.",
        pros=[
            "Saves the most money in interest",
            "Pays off debt fastest (mathematically)",
            "Objectively the best financial choice"
        ],
        cons=[
            "Can be demotivating if highest-rate loan is also largest",
            "Doesn't provide quick wins",
            "Requires discipline to stick with it"
        ],
        best_for="People motivated by math and long-term savings. Want to minimize total interest paid."
    ),
    "snowball": RepaymentStrategy(
        strategy_name="snowball",
        description="Pay minimums on all loans, then put extra toward smallest balance first. Provides psychological wins.",
        pros=[
            "Quick wins boost motivation",
            "See progress faster (eliminate loans one by one)",
            "Psychologically satisfying",
            "Simplifies finances as loans are paid off"
        ],
        cons=[
            "Costs more in total interest than avalanche",
            "May take slightly longer to be debt-free",
            "Not mathematically optimal"
        ],
        best_for="People who need motivational wins. Value psychological benefits over minor interest savings."
    ),
    "standard": RepaymentStrategy(
        strategy_name="standard",
        description="Pay equal amounts on all loans (10-year standard plan). Default federal loan repayment.",
        pros=[
            "Simple and straightforward",
            "Predictable monthly payment",
            "Pays off in exactly 10 years"
        ],
        cons=[
            "Pays more interest than targeted methods",
            "Doesn't optimize for savings",
            "No flexibility"
        ],
        best_for="People who want simplicity and don't want to think about optimization."
    ),
    "idr": RepaymentStrategy(
        strategy_name="idr",
        description="Income-Driven Repayment: payment = 10% of discretionary income. Federal loans only. Forgiveness after 20-25 years.",
        pros=[
            "Lower monthly payments if income is low",
            "Payment adjusts with income",
            "Potential forgiveness after 20-25 years",
            "Can't default if you recertify income annually"
        ],
        cons=[
            "Much more total interest paid",
            "Forgiven amount may be taxable",
            "Must recertify income every year (paperwork)",
            "Extends debt for decades",
            "Forgiveness is uncertain (policy changes)"
        ],
        best_for="Low income relative to debt. Planning to work in public service (PSLF). Can't afford standard payments."
    ),
    "pslf": RepaymentStrategy(
        strategy_name="pslf",
        description="Public Service Loan Forgiveness: Make 120 qualifying payments (10 years) while working for government/nonprofit, remaining balance forgiven tax-free.",
        pros=[
            "Complete forgiveness after 10 years",
            "Tax-free forgiveness",
            "Lower monthly payments via IDR",
            "Can save tens of thousands if high debt"
        ],
        cons=[
            "Must work for qualifying employer for 10 years",
            "Must be on income-driven repayment plan",
            "Must make 120 on-time payments",
            "Historically difficult to navigate (improving)",
            "Limits career flexibility"
        ],
        best_for="Working (or planning to work) for government or nonprofit. High debt relative to income. Committed to 10 years in public service."
    )
}


def calculate_minimum_payment(principal: float, annual_rate: float, months: int = 120) -> float:
    """Calculate minimum monthly payment for a loan.
    
    Standard 10-year repayment uses this formula.
    """
    if annual_rate == 0:
        return principal / months
    
    monthly_rate = annual_rate / 100 / 12
    payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return payment


def simulate_payoff(
    loans: List[LoanForComparison],
    strategy: Literal["avalanche", "snowball", "standard"],
    extra_monthly_payment: float = 0.0
) -> PayoffProjection:
    """Simulate loan payoff under a specific strategy.
    
    Args:
        loans: List of loans to pay off
        strategy: Which strategy to use
        extra_monthly_payment: Extra amount to pay beyond minimums
    
    Returns:
        Projection with timeline and total cost
    """
    
    # Copy loans so we don't mutate originals
    remaining_loans = [
        {"id": l.loan_id, "name": l.name, "balance": l.principal, "rate": l.annual_interest_rate}
        for l in loans
    ]
    
    # Calculate minimum payment for each loan (10-year standard)
    for loan in remaining_loans:
        loan["minimum"] = calculate_minimum_payment(loan["balance"], loan["rate"], 120)
    
    total_minimum = sum(l["minimum"] for l in remaining_loans)
    total_payment = total_minimum + extra_monthly_payment
    
    # Sort loans based on strategy
    if strategy == "avalanche":
        # Highest rate first
        remaining_loans.sort(key=lambda l: l["rate"], reverse=True)
    elif strategy == "snowball":
        # Smallest balance first
        remaining_loans.sort(key=lambda l: l["balance"])
    # standard = pay proportionally (no sorting needed)
    
    # Simulate month by month
    month = 0
    total_paid = 0.0
    year_breakdown = []
    current_year_paid = 0.0
    current_year_principal = 0.0
    current_year_interest = 0.0
    
    while remaining_loans and month < 600:  # Cap at 50 years for safety
        month += 1
        
        # Accrue interest on all loans
        for loan in remaining_loans:
            monthly_rate = loan["rate"] / 100 / 12
            interest_this_month = loan["balance"] * monthly_rate
            loan["balance"] += interest_this_month
        
        # Make payment
        payment_remaining = total_payment
        
        if strategy == "standard":
            # Pay proportionally across all loans
            for loan in remaining_loans:
                if payment_remaining <= 0:
                    break
                payment_to_this_loan = min(payment_remaining, loan["minimum"], loan["balance"])
                
                # Calculate interest vs principal
                monthly_rate = loan["rate"] / 100 / 12
                interest_portion = loan["balance"] * monthly_rate / (1 + monthly_rate)
                principal_portion = payment_to_this_loan - interest_portion
                
                loan["balance"] -= payment_to_this_loan
                payment_remaining -= payment_to_this_loan
                total_paid += payment_to_this_loan
                current_year_paid += payment_to_this_loan
                current_year_interest += interest_portion
                current_year_principal += principal_portion
        
        else:
            # Avalanche or Snowball: pay minimums on all, then target one
            # First, pay minimums
            for loan in remaining_loans[1:]:  # All except first (target)
                if payment_remaining <= 0:
                    break
                payment_to_this_loan = min(payment_remaining, loan["minimum"], loan["balance"])
                
                monthly_rate = loan["rate"] / 100 / 12
                interest_portion = loan["balance"] * monthly_rate / (1 + monthly_rate)
                principal_portion = payment_to_this_loan - interest_portion
                
                loan["balance"] -= payment_to_this_loan
                payment_remaining -= payment_to_this_loan
                total_paid += payment_to_this_loan
                current_year_paid += payment_to_this_loan
                current_year_interest += interest_portion
                current_year_principal += principal_portion
            
            # Then, put remaining toward target loan (first in sorted list)
            if payment_remaining > 0 and remaining_loans:
                target_loan = remaining_loans[0]
                payment_to_target = min(payment_remaining, target_loan["balance"])
                
                monthly_rate = target_loan["rate"] / 100 / 12
                interest_portion = target_loan["balance"] * monthly_rate / (1 + monthly_rate) if monthly_rate > 0 else 0
                principal_portion = payment_to_target - interest_portion
                
                target_loan["balance"] -= payment_to_target
                payment_remaining -= payment_to_target
                total_paid += payment_to_target
                current_year_paid += payment_to_target
                current_year_interest += interest_portion
                current_year_principal += principal_portion
        
        # Remove paid-off loans
        remaining_loans = [l for l in remaining_loans if l["balance"] > 0.01]
        
        # Re-sort after paying off loans (for snowball/avalanche)
        if strategy == "avalanche":
            remaining_loans.sort(key=lambda l: l["rate"], reverse=True)
        elif strategy == "snowball":
            remaining_loans.sort(key=lambda l: l["balance"])
        
        # Track yearly breakdown
        if month % 12 == 0:
            year_breakdown.append({
                "year": month // 12,
                "total_paid": current_year_paid,
                "principal_paid": current_year_principal,
                "interest_paid": current_year_interest,
                "remaining_balance": sum(l["balance"] for l in remaining_loans)
            })
            current_year_paid = 0.0
            current_year_principal = 0.0
            current_year_interest = 0.0
    
    total_principal = sum(l.principal for l in loans)
    total_interest = total_paid - total_principal
    
    return PayoffProjection(
        strategy=strategy,
        monthly_payment=total_payment,
        months_to_payoff=month,
        total_paid=total_paid,
        total_interest=total_interest,
        year_breakdown=year_breakdown
    )


def calculate_idr_payment(annual_income: float, family_size: int = 1) -> float:
    """Calculate Income-Driven Repayment monthly payment.
    
    Simplified: 10% of discretionary income.
    Discretionary income = AGI - 150% of poverty line.
    """
    # 2026 poverty line (estimated)
    poverty_line = 15000 + (5000 * (family_size - 1))
    discretionary_threshold = poverty_line * 1.5
    
    discretionary_income = max(0, annual_income - discretionary_threshold)
    monthly_payment = (discretionary_income * 0.10) / 12
    
    return max(monthly_payment, 0)


def compare_all_strategies(
    loans: List[LoanForComparison],
    annual_income: float = 50000,
    family_size: int = 1
) -> LoanPayoffComparison:
    """Compare all repayment strategies side-by-side.
    
    Returns complete comparison with recommendations.
    """
    
    total_principal = sum(l.principal for l in loans)
    
    # Simulate each strategy
    avalanche = simulate_payoff(loans, "avalanche", extra_monthly_payment=0)
    snowball = simulate_payoff(loans, "snowball", extra_monthly_payment=0)
    standard = simulate_payoff(loans, "standard", extra_monthly_payment=0)
    
    # IDR calculation (simplified)
    idr_monthly = calculate_idr_payment(annual_income, family_size)
    
    # For IDR, if payment is very low, it may not even cover interest (negative amortization)
    # Simplified: assume 25-year forgiveness
    idr_projection = None
    if all(l.loan_type.startswith("federal") for l in loans):
        # Rough estimate: low payment over 25 years
        total_idr_paid = idr_monthly * 12 * 25
        idr_projection = PayoffProjection(
            strategy="idr",
            monthly_payment=idr_monthly,
            months_to_payoff=300,  # 25 years
            total_paid=total_idr_paid,
            total_interest=total_idr_paid - total_principal,
            year_breakdown=[]
        )
    
    # Extra payment scenarios
    extra_50 = simulate_payoff(loans, "avalanche", extra_monthly_payment=50)
    extra_100 = simulate_payoff(loans, "avalanche", extra_monthly_payment=100)
    extra_200 = simulate_payoff(loans, "avalanche", extra_monthly_payment=200)
    
    # Calculate impact of extra payments
    extra_50_impact = ExtraPaymentImpact(
        extra_payment_monthly=50,
        original_months=avalanche.months_to_payoff,
        new_months=extra_50.months_to_payoff,
        months_saved=avalanche.months_to_payoff - extra_50.months_to_payoff,
        original_total_interest=avalanche.total_interest,
        new_total_interest=extra_50.total_interest,
        interest_saved=avalanche.total_interest - extra_50.total_interest,
        total_extra_paid=50 * extra_50.months_to_payoff,
        roi_ratio=(avalanche.total_interest - extra_50.total_interest) / (50 * extra_50.months_to_payoff)
    )
    
    extra_100_impact = ExtraPaymentImpact(
        extra_payment_monthly=100,
        original_months=avalanche.months_to_payoff,
        new_months=extra_100.months_to_payoff,
        months_saved=avalanche.months_to_payoff - extra_100.months_to_payoff,
        original_total_interest=avalanche.total_interest,
        new_total_interest=extra_100.total_interest,
        interest_saved=avalanche.total_interest - extra_100.total_interest,
        total_extra_paid=100 * extra_100.months_to_payoff,
        roi_ratio=(avalanche.total_interest - extra_100.total_interest) / (100 * extra_100.months_to_payoff)
    )
    
    extra_200_impact = ExtraPaymentImpact(
        extra_payment_monthly=200,
        original_months=avalanche.months_to_payoff,
        new_months=extra_200.months_to_payoff,
        months_saved=avalanche.months_to_payoff - extra_200.months_to_payoff,
        original_total_interest=avalanche.total_interest,
        new_total_interest=extra_200.total_interest,
        interest_saved=avalanche.total_interest - extra_200.total_interest,
        total_extra_paid=200 * extra_200.months_to_payoff,
        roi_ratio=(avalanche.total_interest - extra_200.total_interest) / (200 * extra_200.months_to_payoff)
    )
    
    # Calculate interest saved vs minimum for each strategy
    avalanche.interest_saved_vs_minimum = standard.total_interest - avalanche.total_interest
    snowball.interest_saved_vs_minimum = standard.total_interest - snowball.total_interest
    avalanche.time_saved_months = standard.months_to_payoff - avalanche.months_to_payoff
    snowball.time_saved_months = standard.months_to_payoff - snowball.months_to_payoff
    
    # Recommendations
    best_for_savings = "avalanche"  # Always mathematically optimal
    best_for_motivation = "snowball"  # Quick wins
    best_for_forgiveness = "pslf" if any(l.loan_type.startswith("federal") for l in loans) else "none"
    
    return LoanPayoffComparison(
        loans=loans,
        total_principal=total_principal,
        avalanche_projection=avalanche,
        snowball_projection=snowball,
        standard_projection=standard,
        idr_projection=idr_projection,
        best_for_savings=best_for_savings,
        best_for_motivation=best_for_motivation,
        best_for_forgiveness=best_for_forgiveness,
        extra_50_impact=extra_50_impact,
        extra_100_impact=extra_100_impact,
        extra_200_impact=extra_200_impact
    )


def get_strategy_recommendation(
    loans: List[LoanForComparison],
    annual_income: float,
    personality: Literal["analytical", "motivational", "struggling"],
    career_plan: Literal["public_service", "private_sector", "unsure"]
) -> Dict[str, any]:
    """Get personalized strategy recommendation based on player profile.
    
    Args:
        loans: Player's loans
        annual_income: Current or expected income
        personality: What motivates the player
        career_plan: Career trajectory
    
    Returns:
        Recommended strategy with explanation
    """
    
    total_debt = sum(l.principal for l in loans)
    debt_to_income_ratio = total_debt / annual_income if annual_income > 0 else float('inf')
    has_federal_loans = any(l.loan_type.startswith("federal") for l in loans)
    
    # Decision logic
    if career_plan == "public_service" and has_federal_loans and debt_to_income_ratio > 1.5:
        return {
            "recommended_strategy": "pslf",
            "reason": "You plan to work in public service and have high debt. PSLF could save you tens of thousands.",
            "action_items": [
                "Enroll in an income-driven repayment plan (IDR)",
                "Submit Employment Certification Form annually",
                "Make sure your employer qualifies (government/nonprofit 501(c)(3))",
                "Track your 120 qualifying payments",
                "Don't refinance federal loans (you'll lose PSLF eligibility)"
            ],
            "watch_out": "PSLF requires 10 years of qualifying employment. If you leave public service, you lose eligibility."
        }
    
    elif debt_to_income_ratio > 2.0 and has_federal_loans:
        return {
            "recommended_strategy": "idr",
            "reason": "Your debt is very high relative to income. Income-driven repayment will make payments manageable.",
            "action_items": [
                "Apply for IDR plan (PAYE, IBR, or SAVE)",
                "Recertify your income every year",
                "Understand that forgiven amount after 20-25 years may be taxable",
                "As income grows, consider switching to avalanche method"
            ],
            "watch_out": "You'll pay much more interest over time. This is a 'survive now' strategy, not an 'optimize' strategy."
        }
    
    elif personality == "analytical":
        return {
            "recommended_strategy": "avalanche",
            "reason": "You value optimization. Avalanche saves the most money and pays off debt fastest.",
            "action_items": [
                "List all loans by interest rate (highest to lowest)",
                "Pay minimums on all loans",
                "Put any extra money toward highest-rate loan",
                "Once that's paid off, move to next highest rate",
                "Track your interest savings to stay motivated"
            ],
            "watch_out": "Can feel slow if your highest-rate loan is also your largest. Trust the math."
        }
    
    elif personality == "motivational":
        return {
            "recommended_strategy": "snowball",
            "reason": "You need quick wins. Snowball gives you the satisfaction of eliminating loans one by one.",
            "action_items": [
                "List all loans by balance (smallest to largest)",
                "Pay minimums on all loans",
                "Put any extra money toward smallest loan",
                "Celebrate when you pay off each loan!",
                "Roll that payment into the next smallest loan"
            ],
            "watch_out": "You'll pay slightly more interest than avalanche, but the motivation boost is worth it for many people."
        }
    
    else:
        # Default: avalanche is mathematically best
        return {
            "recommended_strategy": "avalanche",
            "reason": "When in doubt, avalanche is the mathematically optimal choice for most people.",
            "action_items": [
                "List all loans by interest rate",
                "Pay minimums on all loans",
                "Attack highest-rate loan with extra payments",
                "Consider making biweekly payments (26 per year = 13 months of payments)"
            ],
            "watch_out": "If you need motivational wins, consider snowball instead. The 'best' strategy is the one you stick with."
        }
