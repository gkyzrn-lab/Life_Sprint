"""Credit card danger simulator - teaches minimum payment trap and interest calculations."""

from typing import Dict, List, Optional, Literal, Any
from pydantic import BaseModel, Field
import math


class CreditCardSimulation(BaseModel):
    """A credit card debt simulation."""
    simulation_id: str
    initial_balance: float
    annual_interest_rate: float  # APR
    
    # Payment strategy
    payment_strategy: Literal["minimum_only", "fixed_amount", "avalanche"] = "minimum_only"
    monthly_payment: float = 0  # For fixed_amount strategy
    
    # Results tracking
    current_balance: float = 0
    total_paid: float = 0
    total_interest_paid: float = 0
    months_to_payoff: int = 0
    monthly_breakdown: List[Dict] = Field(default_factory=list)


class CreditCardTrap(BaseModel):
    """A credit card trap/danger."""
    trap_id: str
    name: str
    description: str
    example_scenario: str
    financial_impact: str  # Dollar amount or percentage impact


class CreditCardMythFact(BaseModel):
    """Credit card myths vs facts."""
    myth_id: str
    myth: str
    fact: str
    impact: Literal["major", "moderate", "minor"]


# Credit card traps
CREDIT_CARD_TRAPS: Dict[str, CreditCardTrap] = {
    "minimum_payment_trap": CreditCardTrap(
        trap_id="minimum_payment_trap",
        name="Minimum Payment Trap",
        description="Paying only the minimum payment is designed to keep you in debt as long as possible. Most of your payment goes to interest, not principal.",
        example_scenario="$1,000 balance at 22% APR, paying $25/month minimum:\n- Takes 58 months (4.8 years) to pay off\n- You'll pay $1,456 total\n- Interest: $456 (45.6% of original balance)\n\nIf you paid $50/month:\n- Takes 23 months (1.9 years)\n- You'll pay $1,150 total\n- Interest: $150 (15% of original balance)",
        financial_impact="Doubling minimum payment = $306 less in interest = 63% savings"
    ),
    
    "high_interest_rate": CreditCardTrap(
        trap_id="high_interest_rate",
        name="High Interest Rate Trap",
        description="Credit card APRs average 22-25%, far higher than auto loans (4-7%), mortgages (3-5%), or student loans (4-8%).",
        example_scenario="$5,000 credit card balance:\n- At 22% APR, paying $100/month = $1,157 interest paid\n- At 6% APR (auto loan), same payment = $156 interest paid\n\nCredit cards cost 7.4x MORE than auto loans for same debt.",
        financial_impact="Average credit card balance: $3,843. Average interest: $847/year"
    ),
    
    "zero_percent_introductory": CreditCardTrap(
        trap_id="zero_percent_intro",
        name="0% APR Introductory Trap",
        description="Cards offer 0% APR for 6-12 months to get you to transfer balances or open accounts. When promo ends, you're charged the full APR (usually 22%+) on ANY remaining balance.",
        example_scenario="Transfer $5,000 balance to 0% APR card (12 months promo):\n- Pay $416/month to pay off in 12 months ✓\n- But if you pay $300/month:\n  - After 12 months, you still owe $1,400\n  - Then 22% APR kicks in on $1,400\n  - That $1,400 becomes much more expensive",
        financial_impact="Miss the deadline by one month? Immediate 22% APR applies to entire remaining balance"
    ),
    
    "annual_fees": CreditCardTrap(
        trap_id="annual_fees",
        name="Annual Fee Trap",
        description="Premium credit cards charge annual fees ($95-$450) claiming rewards benefits. Many people pay the fee but don't earn enough rewards to justify it.",
        example_scenario="'Premium' card: $450 annual fee\nPromised: 5% cashback on travel, 3% on dining\n\nTo break even, you need to spend:\n- $9,000 on 5% categories, OR\n- $15,000 on 3% categories\n\nIf you spend less or forget to use the bonus categories, you LOSE money.",
        financial_impact="Average waste: $150/year per annual fee card person keeps but doesn't use optimally"
    ),
    
    "late_fees": CreditCardTrap(
        trap_id="late_fees",
        name="Late Fee Spiral",
        description="Miss a payment by 1 day? Pay a late fee ($25-$38). Then your interest rate may increase to 22-29% penalty APR. One missed payment can cost you dearly.",
        example_scenario="$1,000 balance, miss payment by 1 day:\n- Late fee: $38\n- Penalty APR (29%) applies\n- Your $22/month interest becomes $24.17/month\n- Takes longer to pay off\n- One late payment cost you $38 + extra interest for months",
        financial_impact="One missed payment can increase total interest paid by 30-50%"
    ),
    
    "balance_transfer_fees": CreditCardTrap(
        trap_id="balance_transfer_fees",
        name="Balance Transfer Fee Trap",
        description="Transfer balance to 0% APR card sounds good, but they charge 3-5% fee upfront. On a $5,000 transfer, that's $150-$250 added to your debt immediately.",
        example_scenario="Transfer $5,000:\n- 3% fee = $150 added to your debt\n- You now owe $5,150, not $5,000\n- Even at 0% APR, you're starting from a higher balance\n\nAlternative: Pay $5,000 original card in 12 months",
        financial_impact="Balance transfer fee cuts your savings in half compared to paying original debt"
    ),
    
    "only_paying_interest": CreditCardTrap(
        trap_id="only_paying_interest",
        name="Paying Only Interest",
        description="Some people set up minimum payments but the minimum is so low that it ONLY covers interest. Your balance never shrinks.",
        example_scenario="$5,000 at 22% APR:\n- Monthly interest: $91.67\n- Minimum payment: $25 (typical)\n- Principal reduction: $0\n- You're paying interest forever\n\nWith interest-only payments, $5,000 takes infinite months (never paid off).",
        financial_impact="If minimum only covers interest, debt is impossible to escape"
    ),
    
    "overspending": CreditCardTrap(
        trap_id="overspending",
        name="Overspending Beyond Means",
        description="Credit cards make overspending easy because you don't see cash leaving. You can spend beyond your means and pay for it with interest for years.",
        example_scenario="30-year-old realizes:\n- Spent $50/month on coffee (credit card)\n- Over 5 years: $3,000 spent + $800 interest = $3,800 total\n- At 25 years old, they could have invested that $3,000\n- At 8% growth, it would now be worth $34,000\n- Cost of daily coffee = $34,000+ in lost wealth",
        financial_impact="Small overspending compounds: $50/month wasted = potential $34,000 loss to compound growth"
    ),
}


# Credit card myths
CREDIT_CARD_MYTHS: Dict[str, CreditCardMythFact] = {
    "myth_carrying_balance": CreditCardMythFact(
        myth_id="myth_carrying_balance",
        myth="You need to carry a balance to build credit.",
        fact="COMPLETELY FALSE. You do NOT need to pay interest to build credit. Use the card and pay it off in full. Paying interest is never necessary for credit building.",
        impact="major"
    ),
    
    "myth_more_cards_better": CreditCardMythFact(
        myth_id="myth_more_cards_better",
        myth="Having more credit cards means better credit score.",
        fact="NOT REALLY. Each hard inquiry (when applying for a card) lowers your score. More accounts can help slightly with credit mix and utilization, but each new card's hard inquiry offsets benefits.",
        impact="moderate"
    ),
    
    "myth_rewards_pay_interest": CreditCardMythFact(
        myth_id="myth_rewards_pay_interest",
        myth="Credit card rewards make it worth carrying a balance.",
        fact="FALSE. 2% cash back doesn't justify 22% interest. If you're paying interest, you're losing money. Only use rewards on cards you pay off completely.",
        impact="major"
    ),
    
    "myth_bad_credit_recover": CreditCardMythFact(
        myth_id="myth_bad_credit_recover",
        myth="Your credit recovers quickly once you fix it.",
        fact="FALSE. Late payments stay on your report for 7 years. Payment history is 35% of your score. Bad credit takes years to recover from.",
        impact="major"
    ),
}


def simulate_credit_card_payoff(
    initial_balance: float,
    annual_interest_rate: float,
    payment_strategy: Literal["minimum_only", "fixed_amount", "aggressive"],
    monthly_payment: float = 0,
    minimum_percent: float = 0.02
) -> CreditCardSimulation:
    """Simulate paying off a credit card balance.
    
    Args:
        initial_balance: Starting balance
        annual_interest_rate: APR (e.g., 22.0 for 22%)
        payment_strategy: How to pay
        monthly_payment: For fixed_amount strategy
        minimum_percent: Minimum as % of balance (typically 1-2%)
    
    Returns:
        Simulation results with month-by-month breakdown
    """
    
    balance = initial_balance
    total_paid = 0.0
    total_interest = 0.0
    months = 0
    monthly_breakdown = []
    
    monthly_rate = (annual_interest_rate / 100) / 12
    
    while balance > 0 and months < 600:  # Cap at 50 years
        months += 1
        
        # Calculate interest this month
        interest_this_month = balance * monthly_rate
        total_interest += interest_this_month
        balance += interest_this_month
        
        # Determine payment
        if payment_strategy == "minimum_only":
            # Minimum is 2% of balance or $25, whichever is greater
            payment = max(balance * minimum_percent, 25)
        elif payment_strategy == "fixed_amount":
            payment = monthly_payment
        elif payment_strategy == "aggressive":
            # Pay everything
            payment = balance
        else:
            payment = 0
        
        # Cap payment at remaining balance
        payment = min(payment, balance)
        
        balance -= payment
        total_paid += payment
        
        # Ensure balance doesn't go negative due to rounding
        balance = max(0, balance)
        
        # Track month
        monthly_breakdown.append({
            "month": months,
            "starting_balance": balance + payment,
            "interest_charged": interest_this_month,
            "payment": payment,
            "ending_balance": balance,
            "total_paid_to_date": total_paid,
            "total_interest_to_date": total_interest
        })
        
        # Stop if balance is essentially zero
        if balance < 0.01:
            break
    
    return CreditCardSimulation(
        simulation_id=f"sim_{initial_balance}_{annual_interest_rate}_{payment_strategy}",
        initial_balance=initial_balance,
        annual_interest_rate=annual_interest_rate,
        payment_strategy=payment_strategy,
        monthly_payment=monthly_payment,
        current_balance=balance,
        total_paid=total_paid,
        total_interest_paid=total_interest,
        months_to_payoff=months,
        monthly_breakdown=monthly_breakdown
    )


def compare_payoff_strategies(
    initial_balance: float,
    annual_interest_rate: float,
    minimum_payment: float = 25,
    target_monthly: float = 50,
    aggressive_monthly: float = 200
) -> Dict[str, CreditCardSimulation]:
    """Compare different payoff strategies."""
    
    return {
        "minimum_only": simulate_credit_card_payoff(
            initial_balance, annual_interest_rate, "minimum_only", minimum_payment
        ),
        "moderate": simulate_credit_card_payoff(
            initial_balance, annual_interest_rate, "fixed_amount", target_monthly
        ),
        "aggressive": simulate_credit_card_payoff(
            initial_balance, annual_interest_rate, "fixed_amount", aggressive_monthly
        ),
    }


def calculate_minimum_payment(balance: float, apr: float, min_percent: float = 0.02) -> float:
    """Calculate minimum payment for a balance."""
    return max(balance * min_percent, 25)


def get_trap(trap_id: str) -> Optional[CreditCardTrap]:
    """Get a specific credit card trap."""
    return CREDIT_CARD_TRAPS.get(trap_id)


def get_all_traps() -> List[CreditCardTrap]:
    """Get all credit card traps."""
    return list(CREDIT_CARD_TRAPS.values())


def get_myth(myth_id: str) -> Optional[CreditCardMythFact]:
    """Get a specific myth."""
    return CREDIT_CARD_MYTHS.get(myth_id)


def get_all_myths() -> List[CreditCardMythFact]:
    """Get all myths."""
    return list(CREDIT_CARD_MYTHS.values())


def get_payoff_insights(simulation: CreditCardSimulation) -> Dict[str, Any]:
    """Get insights from a payoff simulation."""
    
    monthly_rate = (simulation.annual_interest_rate / 100) / 12
    avg_monthly_interest = simulation.total_interest_paid / max(simulation.months_to_payoff, 1)
    
    insights = {
        "payoff_time_years": round(simulation.months_to_payoff / 12, 1),
        "payoff_time_months": simulation.months_to_payoff,
        "total_interest_percent": round((simulation.total_interest_paid / simulation.initial_balance) * 100, 1),
        "avg_monthly_interest": round(avg_monthly_interest, 2),
        "interest_as_percent_of_paid": round((simulation.total_interest_paid / simulation.total_paid) * 100, 1),
        "monthly_rate_percent": round(monthly_rate * 100, 2),
    }
    
    return insights
