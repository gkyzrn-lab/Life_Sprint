"""Investment and compound interest system for Life Sprint.

Teaches students:
- Power of compound interest
- Starting early vs waiting
- Different investment vehicles (savings, Roth IRA, 401k, index funds)
- Employer 401k match (free money!)
- Risk vs return trade-offs
- Tax-advantaged accounts
"""

from typing import Dict, List, Optional, Literal
from pydantic import BaseModel, Field
import math


class InvestmentAccount(BaseModel):
    """An investment account with balance and returns."""
    account_id: str
    account_type: Literal["savings", "roth_ira", "traditional_401k", "taxable_brokerage"]
    balance: float = 0.0
    contributions_this_year: float = 0.0
    total_contributions: float = 0.0  # All time
    total_earnings: float = 0.0  # All time gains
    
    # Account limits
    annual_contribution_limit: Optional[float] = None
    
    # Investment allocation
    investment_type: Literal["savings_account", "conservative", "moderate", "aggressive", "index_funds"]
    expected_annual_return: float = 7.0  # Percent
    risk_level: Literal["very_low", "low", "medium", "high"]


class InvestmentVehicle(BaseModel):
    """A type of investment option."""
    vehicle_id: str
    name: str
    description: str
    expected_annual_return: float  # Percent
    risk_level: Literal["very_low", "low", "medium", "high"]
    tax_treatment: Literal["taxable", "tax_deferred", "tax_free"]
    liquidity: Literal["instant", "easy", "restricted", "locked_until_retirement"]
    
    # Limits and rules
    annual_contribution_limit: Optional[float] = None
    employer_match_available: bool = False
    early_withdrawal_penalty: bool = False
    
    # Educational
    best_for: str
    watch_out: str


class CompoundInterestScenario(BaseModel):
    """A scenario showing power of compound interest."""
    scenario_name: str
    description: str
    
    # Person A (starts early)
    person_a_age_start: int
    person_a_monthly_contribution: float
    person_a_years_contributing: int
    person_a_total_contributed: float
    person_a_balance_at_65: float
    
    # Person B (starts late)
    person_b_age_start: int
    person_b_monthly_contribution: float
    person_b_years_contributing: int
    person_b_total_contributed: float
    person_b_balance_at_65: float
    
    # Comparison
    time_advantage_years: int
    person_a_advantage: float
    
    lesson: str


class EmployerMatch(BaseModel):
    """401k employer match structure."""
    match_percentage: float  # e.g., 50% means employer puts in $0.50 per $1.00 you put in
    match_limit_percent_of_salary: float  # e.g., 6% means they match up to 6% of your salary
    vesting_schedule: Literal["immediate", "3_year_cliff", "5_year_graded"]
    vesting_description: str


# Investment vehicles catalog
INVESTMENT_VEHICLES: Dict[str, InvestmentVehicle] = {
    "savings_account": InvestmentVehicle(
        vehicle_id="savings_account",
        name="High-Yield Savings Account",
        description="FDIC-insured savings account. Safe but low returns. Good for emergency fund.",
        expected_annual_return=4.0,
        risk_level="very_low",
        tax_treatment="taxable",
        liquidity="instant",
        annual_contribution_limit=None,
        employer_match_available=False,
        early_withdrawal_penalty=False,
        best_for="Emergency fund (3-6 months expenses). Short-term savings goals. Money you might need soon.",
        watch_out="Doesn't beat inflation long-term. Not for retirement savings."
    ),
    
    "roth_ira": InvestmentVehicle(
        vehicle_id="roth_ira",
        name="Roth IRA",
        description="Individual retirement account. Contribute after-tax money, grows tax-free forever. Withdraw tax-free in retirement.",
        expected_annual_return=9.0,
        risk_level="medium",
        tax_treatment="tax_free",
        liquidity="restricted",
        annual_contribution_limit=7000,  # 2026 limit
        employer_match_available=False,
        early_withdrawal_penalty=True,
        best_for="Long-term retirement savings. Young people (tax-free growth for decades). Anyone expecting higher taxes in retirement.",
        watch_out="$7,000/year contribution limit. Income limits for eligibility. Money locked until 59.5 (with exceptions)."
    ),
    
    "traditional_401k": InvestmentVehicle(
        vehicle_id="traditional_401k",
        name="Traditional 401(k)",
        description="Employer-sponsored retirement account. Contribute pre-tax money (reduces taxable income now). Pay taxes when you withdraw in retirement.",
        expected_annual_return=9.0,
        risk_level="medium",
        tax_treatment="tax_deferred",
        liquidity="locked_until_retirement",
        annual_contribution_limit=23000,  # 2026 limit
        employer_match_available=True,
        early_withdrawal_penalty=True,
        best_for="Getting employer match (FREE MONEY!). Reducing taxable income now. High earners.",
        watch_out="Taxed when you withdraw. Required minimum distributions at 73. Early withdrawal = taxes + 10% penalty."
    ),
    
    "index_funds": InvestmentVehicle(
        vehicle_id="index_funds",
        name="Index Funds (S&P 500)",
        description="Low-cost funds that track market indexes. Diversified across hundreds of companies. Long-term average ~10% return.",
        expected_annual_return=10.0,
        risk_level="medium",
        tax_treatment="taxable",
        liquidity="easy",
        annual_contribution_limit=None,
        employer_match_available=False,
        early_withdrawal_penalty=False,
        best_for="Long-term growth (5+ years). Retirement savings. Passive investing. Low fees.",
        watch_out="Market volatility. Can lose money short-term. Taxed on dividends and capital gains. Don't panic sell in downturns."
    ),
    
    "conservative_bonds": InvestmentVehicle(
        vehicle_id="conservative_bonds",
        name="Conservative Bond Portfolio",
        description="Mix of government and corporate bonds. Lower risk but lower returns than stocks.",
        expected_annual_return=5.0,
        risk_level="low",
        tax_treatment="taxable",
        liquidity="easy",
        annual_contribution_limit=None,
        employer_match_available=False,
        early_withdrawal_penalty=False,
        best_for="Risk-averse investors. Older people close to retirement. Balancing a stock-heavy portfolio.",
        watch_out="Lower returns mean slower wealth building. Inflation risk. Interest rate risk."
    ),
}


def calculate_compound_interest(
    principal: float,
    monthly_contribution: float,
    annual_return_rate: float,
    years: int
) -> Dict[str, float]:
    """Calculate compound interest with regular contributions.
    
    Args:
        principal: Starting balance
        monthly_contribution: Amount added each month
        annual_return_rate: Expected annual return (as percentage, e.g., 7.0 for 7%)
        years: Number of years to compound
    
    Returns:
        Dictionary with final balance, total contributions, and total earnings
    """
    
    monthly_rate = annual_return_rate / 100 / 12
    months = years * 12
    
    balance = principal
    total_contributed = principal
    
    # Add monthly contributions with compound growth
    for month in range(months):
        balance *= (1 + monthly_rate)  # Growth
        balance += monthly_contribution  # Contribution
        total_contributed += monthly_contribution
    
    total_earnings = balance - total_contributed
    
    return {
        "final_balance": balance,
        "total_contributed": total_contributed,
        "total_earnings": total_earnings,
        "return_multiple": balance / total_contributed if total_contributed > 0 else 0
    }


def calculate_yearly_breakdown(
    principal: float,
    monthly_contribution: float,
    annual_return_rate: float,
    years: int
) -> List[Dict[str, float]]:
    """Get year-by-year breakdown of investment growth.
    
    Returns list of dictionaries with year, balance, contributions, earnings.
    """
    
    monthly_rate = annual_return_rate / 100 / 12
    balance = principal
    total_contributed = principal
    
    yearly_data = []
    
    for year in range(1, years + 1):
        year_start_balance = balance
        year_contributions = 0.0
        
        # Simulate 12 months
        for month in range(12):
            balance *= (1 + monthly_rate)
            balance += monthly_contribution
            year_contributions += monthly_contribution
            total_contributed += monthly_contribution
        
        year_earnings = balance - year_start_balance - year_contributions
        
        yearly_data.append({
            "year": year,
            "age": 22 + year,  # Assuming starting at 22
            "balance": balance,
            "year_contributions": year_contributions,
            "year_earnings": year_earnings,
            "total_contributed": total_contributed,
            "total_earnings": balance - total_contributed
        })
    
    return yearly_data


def compare_start_early_vs_late() -> CompoundInterestScenario:
    """Generate the classic 'start early vs start late' comparison.
    
    Shows dramatic impact of starting to invest in your 20s vs 30s.
    """
    
    # Person A: Starts at 22, invests until 32 (10 years), then stops
    person_a_years_investing = 10
    person_a_monthly = 200
    person_a_stops_at_age = 32
    
    # Calculate Person A: invest for 10 years, then let it grow for 33 more years
    person_a_after_contributing = calculate_compound_interest(
        principal=0,
        monthly_contribution=person_a_monthly,
        annual_return_rate=9.0,
        years=person_a_years_investing
    )
    
    # Then let it grow with no contributions until 65
    person_a_final = calculate_compound_interest(
        principal=person_a_after_contributing["final_balance"],
        monthly_contribution=0,
        annual_return_rate=9.0,
        years=65 - person_a_stops_at_age
    )
    
    # Person B: Starts at 32, invests until 65 (33 years)
    person_b_years_investing = 33
    person_b_monthly = 200
    
    person_b_final = calculate_compound_interest(
        principal=0,
        monthly_contribution=person_b_monthly,
        annual_return_rate=9.0,
        years=person_b_years_investing
    )
    
    return CompoundInterestScenario(
        scenario_name="Start Early vs Start Late",
        description="Person A invests $200/month for 10 years (age 22-32), then stops. Person B waits until 32, then invests $200/month for 33 years until retirement.",
        person_a_age_start=22,
        person_a_monthly_contribution=person_a_monthly,
        person_a_years_contributing=person_a_years_investing,
        person_a_total_contributed=person_a_monthly * 12 * person_a_years_investing,
        person_a_balance_at_65=person_a_final["final_balance"],
        person_b_age_start=32,
        person_b_monthly_contribution=person_b_monthly,
        person_b_years_contributing=person_b_years_investing,
        person_b_total_contributed=person_b_monthly * 12 * person_b_years_investing,
        person_b_balance_at_65=person_b_final["final_balance"],
        time_advantage_years=10,
        person_a_advantage=person_a_final["final_balance"] - person_b_final["final_balance"],
        lesson=f"Person A contributed ${person_a_monthly * 12 * person_a_years_investing:,.0f} and has ${person_a_final['final_balance']:,.0f} at 65. Person B contributed ${person_b_monthly * 12 * person_b_years_investing:,.0f} (3.3x more!) but only has ${person_b_final['final_balance']:,.0f}. Starting 10 years earlier gave Person A ${person_a_final['final_balance'] - person_b_final['final_balance']:,.0f} more despite contributing ${person_b_final['total_contributed'] - person_a_final['total_contributed']:,.0f} LESS. Time in market beats timing the market!"
    )


def calculate_employer_match_value(
    annual_salary: float,
    employee_contribution_percent: float,
    match: EmployerMatch
) -> Dict[str, float]:
    """Calculate the value of employer 401k match.
    
    This is literally free money!
    """
    
    employee_contribution = annual_salary * (employee_contribution_percent / 100)
    
    # Calculate employer match
    # Example: 50% match up to 6% of salary
    # If you contribute 8%, they match 50% of first 6% = 3% of salary
    eligible_salary_for_match = annual_salary * (match.match_limit_percent_of_salary / 100)
    employer_match_amount = min(employee_contribution, eligible_salary_for_match) * (match.match_percentage / 100)
    
    # Total contribution
    total_contribution = employee_contribution + employer_match_amount
    
    # Calculate lost match if contributing less
    optimal_contribution_percent = match.match_limit_percent_of_salary
    lost_match = 0.0
    if employee_contribution_percent < optimal_contribution_percent:
        lost_match = (optimal_contribution_percent - employee_contribution_percent) / 100 * annual_salary * (match.match_percentage / 100)
    
    return {
        "employee_contribution": employee_contribution,
        "employer_match": employer_match_amount,
        "total_contribution": total_contribution,
        "free_money_percent": (employer_match_amount / employee_contribution * 100) if employee_contribution > 0 else 0,
        "lost_match_this_year": lost_match,
        "lost_match_over_30_years": lost_match * 30  # Simplified (not compounded)
    }


def retirement_projection(
    current_age: int,
    retirement_age: int,
    current_savings: float,
    monthly_contribution: float,
    annual_return: float = 9.0
) -> Dict[str, any]:
    """Project retirement savings.
    
    Shows if player is on track for retirement.
    """
    
    years_until_retirement = retirement_age - current_age
    
    projection = calculate_compound_interest(
        principal=current_savings,
        monthly_contribution=monthly_contribution,
        annual_return_rate=annual_return,
        years=years_until_retirement
    )
    
    # Rule of thumb: need 25x annual expenses for retirement (4% withdrawal rule)
    # Assume expenses = 70% of final salary
    # Simplified: assume $50k/year expenses = need $1.25M
    comfortable_retirement = 1_250_000
    
    on_track = projection["final_balance"] >= comfortable_retirement
    
    if projection["final_balance"] < comfortable_retirement:
        shortfall = comfortable_retirement - projection["final_balance"]
        # How much more per month?
        additional_monthly_needed = calculate_monthly_needed_for_goal(
            current_savings=current_savings,
            years=years_until_retirement,
            goal=comfortable_retirement,
            annual_return=annual_return
        ) - monthly_contribution
    else:
        additional_monthly_needed = 0
        shortfall = 0
    
    return {
        "projected_balance_at_retirement": projection["final_balance"],
        "total_contributed": projection["total_contributed"],
        "total_earnings": projection["total_earnings"],
        "on_track_for_comfortable_retirement": on_track,
        "comfortable_retirement_target": comfortable_retirement,
        "shortfall": shortfall,
        "additional_monthly_needed": max(0, additional_monthly_needed),
        "years_until_retirement": years_until_retirement
    }


def calculate_monthly_needed_for_goal(
    current_savings: float,
    years: int,
    goal: float,
    annual_return: float = 9.0
) -> float:
    """Calculate monthly contribution needed to reach a goal.
    
    Useful for: "How much do I need to save per month to have $X by retirement?"
    """
    
    monthly_rate = annual_return / 100 / 12
    months = years * 12
    
    # Future value of current savings
    fv_of_current = current_savings * ((1 + monthly_rate) ** months)
    
    # Remaining amount needed from contributions
    needed_from_contributions = goal - fv_of_current
    
    if needed_from_contributions <= 0:
        return 0  # Already have enough
    
    # Monthly contribution formula (future value of annuity)
    # FV = PMT * ((1 + r)^n - 1) / r
    # Solve for PMT
    monthly_contribution = needed_from_contributions * monthly_rate / ((1 + monthly_rate) ** months - 1)
    
    return monthly_contribution


def get_investment_recommendation(
    age: int,
    emergency_fund_months: float,
    annual_income: float,
    debt_amount: float,
    has_employer_match: bool
) -> Dict[str, any]:
    """Get personalized investment recommendation based on financial situation.
    
    Returns recommended investment strategy and priority order.
    """
    
    recommendations = []
    
    # Priority 1: Emergency fund
    if emergency_fund_months < 3:
        monthly_expenses = annual_income / 12 * 0.3  # Rough estimate
        emergency_fund_goal = monthly_expenses * 3
        recommendations.append({
            "priority": 1,
            "action": "Build emergency fund in high-yield savings",
            "target": f"${emergency_fund_goal:,.0f} (3 months expenses)",
            "reason": "Emergency fund prevents debt spiral when unexpected expenses hit.",
            "vehicle": "savings_account"
        })
    
    # Priority 2: Employer match (if available)
    if has_employer_match:
        recommendations.append({
            "priority": 2,
            "action": "Contribute to 401k up to employer match",
            "target": "At least match percentage (usually 3-6% of salary)",
            "reason": "Employer match is FREE MONEY. 100% instant return! Never leave this on the table.",
            "vehicle": "traditional_401k"
        })
    
    # Priority 3: Pay off high-interest debt
    if debt_amount > 0:
        # Assume credit card debt or high-interest loans
        recommendations.append({
            "priority": 3,
            "action": "Pay off high-interest debt (>7% APR)",
            "target": f"Pay off ${debt_amount:,.0f}",
            "reason": "Paying off 20% APR debt = guaranteed 20% return. Better than any investment.",
            "vehicle": None
        })
    
    # Priority 4: Roth IRA
    if age < 40:
        recommendations.append({
            "priority": 4,
            "action": "Max out Roth IRA",
            "target": "$7,000/year ($583/month)",
            "reason": "Tax-free growth for decades. Your 65-year-old self will thank you.",
            "vehicle": "roth_ira"
        })
    
    # Priority 5: Additional 401k contributions
    recommendations.append({
        "priority": 5,
        "action": "Increase 401k contributions beyond match",
        "target": "10-15% of salary",
        "reason": "Tax-deferred growth. Reduces taxable income now. Automate savings.",
        "vehicle": "traditional_401k"
    })
    
    # Priority 6: Taxable brokerage (index funds)
    recommendations.append({
        "priority": 6,
        "action": "Invest in taxable brokerage (index funds)",
        "target": "Any extra after maxing tax-advantaged accounts",
        "reason": "Additional wealth building. More flexible than retirement accounts.",
        "vehicle": "index_funds"
    })
    
    return {
        "recommendations": recommendations,
        "summary": f"Age {age}: Follow this priority order. Don't skip steps (e.g., don't invest in stocks before building emergency fund)."
    }
