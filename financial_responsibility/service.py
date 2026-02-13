"""Financial responsibility service.

Handles:
- Tax calculations (federal, state, FICA)
- Monthly expense tracking
- Unexpected expense generation
- Emergency fund management
- Financial stress calculation
- Financial literacy progression
- Achievement unlocks
- Story triggers
"""

from core_domain.player.player_model import Player
from core_domain.finance.financial_responsibility import (
    FinancialResponsibility, TaxRecord, MonthlyExpense, UnexpectedExpense,
    FinancialAchievement, FinancialStress, FinancialLiteracy
)
from catalogs.financial_mechanics import (
    FEDERAL_TAX_BRACKETS, STATE_TAX_RATES, FICA_RATE, STANDARD_DEDUCTION,
    BASE_MONTHLY_EXPENSES, UNEXPECTED_EXPENSE_POOL, FINANCIAL_ACHIEVEMENTS,
    FINANCIAL_STRESS_MECHANICS, FINANCIAL_STORIES, FINANCIAL_LITERACY_TOPICS
)
import random


def calculate_taxes(gross_income: float, state: str = "general") -> dict:
    """
    Calculate federal, state, and FICA taxes on gross income.
    
    Returns:
        {federal_tax, state_tax, fica_tax, total_tax, net_income, effective_rate}
    """
    # Standard deduction reduces taxable income
    taxable_income = max(0, gross_income - STANDARD_DEDUCTION)
    
    # Federal tax (progressive brackets)
    federal_tax = 0.0
    remaining = taxable_income
    
    for i, bracket in enumerate(FEDERAL_TAX_BRACKETS):
        bracket_min = bracket["min"]
        bracket_max = bracket["max"]
        bracket_rate = bracket["rate"]
        
        if remaining <= 0:
            break
        
        # Calculate amount in this bracket
        if i == 0:
            taxable_in_bracket = min(remaining, bracket_max - bracket_min)
        else:
            prev_max = FEDERAL_TAX_BRACKETS[i-1]["max"]
            taxable_in_bracket = min(remaining, bracket_max - prev_max)
        
        federal_tax += taxable_in_bracket * bracket_rate
        remaining -= taxable_in_bracket
    
    # State tax (flat rate on taxable income)
    state_rate = STATE_TAX_RATES.get(state, STATE_TAX_RATES["general"])
    state_tax = taxable_income * state_rate
    
    # FICA tax (flat rate on ALL gross income, no deduction)
    fica_tax = gross_income * FICA_RATE
    
    # Total
    total_tax = federal_tax + state_tax + fica_tax
    net_income = gross_income - total_tax
    effective_rate = (total_tax / gross_income) if gross_income > 0 else 0.0
    
    return {
        "federal_tax": float(federal_tax),
        "state_tax": float(state_tax),
        "fica_tax": float(fica_tax),
        "total_tax": float(total_tax),
        "net_income": float(net_income),
        "effective_rate": float(effective_rate),
    }


def process_first_paycheck_tax_shock(player: Player) -> dict:
    """
    Called when player receives first real paycheck after having a job.
    Triggers tax awareness shock.
    """
    if not hasattr(player, 'financial_responsibility'):
        player.financial_responsibility = FinancialResponsibility()
    
    if player.financial_responsibility.financial_awareness_triggered:
        return {"already_triggered": True}
    
    # Calculate taxes on player's annual income
    annual_income = player.career.current_salary if hasattr(player, 'career') and player.career.current_salary else 50000
    
    taxes = calculate_taxes(annual_income)
    
    player.financial_responsibility.gross_annual_income = annual_income
    player.financial_responsibility.take_home_annual = taxes["net_income"]
    player.financial_responsibility.effective_tax_rate = taxes["effective_rate"]
    player.financial_responsibility.taxes_owed_this_year = taxes["total_tax"]
    player.financial_responsibility.financial_awareness_triggered = True
    
    # Update literacy
    player.financial_responsibility.literacy.tax_awareness = 60.0  # Big jump
    
    # Trigger story
    story = _trigger_story(player, "first_paycheck_shock")
    
    # Check achievements
    achievements = _check_financial_achievements(player)
    
    return {
        "gross_income": float(annual_income),
        "net_income": float(taxes["net_income"]),
        "taxes_paid": float(taxes["total_tax"]),
        "effective_rate": float(taxes["effective_rate"]),
        "take_home_percentage": float((taxes["net_income"] / annual_income) * 100),
        "story": story,
        "achievements_unlocked": achievements,
        "message": f"You expected ${annual_income:,.0f}. But after taxes, it's ${taxes['net_income']:,.0f}. That's {taxes['effective_rate']*100:.1f}% gone to taxes.",
    }


def set_monthly_expenses(player: Player, housing_type: str = "on_campus_dorm") -> dict:
    """Set player's monthly expenses based on housing type."""
    if not hasattr(player, 'financial_responsibility'):
        player.financial_responsibility = FinancialResponsibility()
    
    expense_template = BASE_MONTHLY_EXPENSES.get(housing_type, BASE_MONTHLY_EXPENSES["on_campus_dorm"])
    
    player.financial_responsibility.monthly_expenses = []
    
    for category, amount in expense_template.items():
        if category == "total":
            continue
        
        expense = MonthlyExpense(
            category=category,
            name=category.replace("_", " ").title(),
            amount=float(amount),
        )
        player.financial_responsibility.monthly_expenses.append(expense)
    
    player.financial_responsibility.total_monthly_cost = float(expense_template["total"])
    
    # Set emergency fund goal (4 months of expenses)
    player.financial_responsibility.emergency_fund_goal = float(expense_template["total"] * 4)
    
    return {
        "housing_type": housing_type,
        "monthly_total": float(expense_template["total"]),
        "annual_cost": float(expense_template["total"] * 12),
        "emergency_fund_goal": float(expense_template["total"] * 4),
        "expenses": [
            {"category": e.category, "name": e.name, "amount": float(e.amount)}
            for e in player.financial_responsibility.monthly_expenses
        ],
    }


def generate_unexpected_expense(player: Player, force_category: str = None) -> dict:
    """
    Generate an unexpected expense (surprise mechanic).
    
    This is intentionally unpredictable to teach financial preparedness.
    """
    if not hasattr(player, 'financial_responsibility'):
        player.financial_responsibility = FinancialResponsibility()
    
    # Choose category
    if force_category:
        category = force_category
    else:
        category = random.choice(list(UNEXPECTED_EXPENSE_POOL.keys()))
    
    # Choose expense from pool
    expense_options = UNEXPECTED_EXPENSE_POOL[category]
    expense_data = random.choice(expense_options)
    
    # Create expense
    expense_id = f"{category}_{player.semester}_{len(player.financial_responsibility.unexpected_expenses)}"
    unexpected = UnexpectedExpense(
        expense_id=expense_id,
        name=expense_data["name"],
        amount=float(expense_data["amount"]),
        category=category,
        semester=player.semester,
        severity=expense_data["severity"],
        resolved=False,
    )
    
    player.financial_responsibility.unexpected_expenses.append(unexpected)
    player.financial_responsibility.total_unexpected_costs += unexpected.amount
    
    # Check if emergency fund can cover it
    can_cover = player.financial_responsibility.emergency_fund >= unexpected.amount
    
    if can_cover:
        player.financial_responsibility.emergency_fund -= unexpected.amount
        unexpected.resolved = True
        story = _trigger_story(player, "emergency_fund_saves")
        stress_increase = 0
    else:
        # Can't cover - go into debt
        shortfall = unexpected.amount - player.financial_responsibility.emergency_fund
        player.financial_responsibility.emergency_fund = 0
        player.financial_responsibility.emergency_debt += shortfall
        player.financial_responsibility.total_non_student_debt += shortfall
        
        # Trigger appropriate story
        if category == "medical":
            story = _trigger_story(player, "unexpected_medical")
        elif category == "car_repair":
            story = _trigger_story(player, "unexpected_car_repair")
        else:
            story = None
        
        stress_increase = 15 if expense_data["severity"] == "minor" else 25 if expense_data["severity"] == "moderate" else 40
        player.financial_responsibility.financial_stress.stress_level += stress_increase
    
    # Update literacy
    player.financial_responsibility.literacy.budget_skill += 10
    if not player.financial_responsibility.literacy.experienced_major_expense:
        player.financial_responsibility.literacy.experienced_major_expense = True
    
    return {
        "expense_id": expense_id,
        "name": unexpected.name,
        "amount": float(unexpected.amount),
        "category": category,
        "severity": expense_data["severity"],
        "can_cover": can_cover,
        "emergency_fund_remaining": float(player.financial_responsibility.emergency_fund),
        "debt_incurred": float(shortfall) if not can_cover else 0.0,
        "stress_increase": stress_increase,
        "story": story,
    }


def contribute_to_emergency_fund(player: Player, amount: float) -> dict:
    """Player contributes to emergency fund."""
    if not hasattr(player, 'financial_responsibility'):
        player.financial_responsibility = FinancialResponsibility()
    
    player.financial_responsibility.emergency_fund += amount
    
    # Check achievements
    achievements = _check_financial_achievements(player)
    
    # Calculate months of coverage
    months_covered = (player.financial_responsibility.emergency_fund / player.financial_responsibility.total_monthly_cost) if player.financial_responsibility.total_monthly_cost > 0 else 0
    
    return {
        "contributed": float(amount),
        "emergency_fund_total": float(player.financial_responsibility.emergency_fund),
        "emergency_fund_goal": float(player.financial_responsibility.emergency_fund_goal),
        "percent_to_goal": float((player.financial_responsibility.emergency_fund / player.financial_responsibility.emergency_fund_goal) * 100) if player.financial_responsibility.emergency_fund_goal > 0 else 0,
        "months_covered": float(months_covered),
        "achievements_unlocked": achievements,
    }


def pay_off_debt(player: Player, amount: float, debt_type: str = "emergency") -> dict:
    """Pay off emergency or credit card debt."""
    if not hasattr(player, 'financial_responsibility'):
        player.financial_responsibility = FinancialResponsibility()
    
    if debt_type == "emergency":
        paid = min(amount, player.financial_responsibility.emergency_debt)
        player.financial_responsibility.emergency_debt -= paid
        player.financial_responsibility.total_non_student_debt -= paid
    elif debt_type == "credit_card":
        paid = min(amount, player.financial_responsibility.credit_card_debt)
        player.financial_responsibility.credit_card_debt -= paid
        player.financial_responsibility.total_non_student_debt -= paid
    else:
        return {"error": "Unknown debt type"}
    
    # Check achievements
    achievements = _check_financial_achievements(player)
    
    return {
        "paid": float(paid),
        "debt_remaining": float(player.financial_responsibility.emergency_debt + player.financial_responsibility.credit_card_debt),
        "achievements_unlocked": achievements,
    }


def update_financial_stress(player: Player) -> dict:
    """
    Calculate financial stress based on debt ratio, emergency fund, expenses.
    Called each semester.
    """
    if not hasattr(player, 'financial_responsibility'):
        player.financial_responsibility = FinancialResponsibility()
    
    stress = player.financial_responsibility.financial_stress
    
    # Calculate debt ratio
    annual_income = player.financial_responsibility.gross_annual_income or 50000
    total_debt = player.financial_responsibility.total_non_student_debt
    stress.debt_ratio = total_debt / annual_income if annual_income > 0 else 0
    
    # Calculate emergency fund months
    monthly_cost = player.financial_responsibility.total_monthly_cost or 1000
    stress.emergency_fund_months = player.financial_responsibility.emergency_fund / monthly_cost if monthly_cost > 0 else 0
    
    # Calculate stress level
    base_stress = 20.0  # Everyone has some financial stress
    
    # Debt stress
    if stress.debt_ratio > 1.0:
        base_stress += 40
    elif stress.debt_ratio > 0.5:
        base_stress += 25
    elif stress.debt_ratio > 0.2:
        base_stress += 10
    
    # Emergency fund stress
    if stress.emergency_fund_months < 0.5:
        base_stress += 30
    elif stress.emergency_fund_months < 1.0:
        base_stress += 20
    elif stress.emergency_fund_months < 3.0:
        base_stress += 10
    
    stress.stress_level = min(100, base_stress)
    
    # Bankruptcy risk
    if stress.debt_ratio > 2.0:
        stress.bankruptcy_risk = 0.8
    elif stress.debt_ratio > 1.5:
        stress.bankruptcy_risk = 0.5
    elif stress.debt_ratio > 1.0:
        stress.bankruptcy_risk = 0.2
    else:
        stress.bankruptcy_risk = 0.0
    
    # Apply health penalties
    health_impact = stress.stress_level * FINANCIAL_STRESS_MECHANICS["health_impact_per_stress"]["physical_health"] / 100
    mental_impact = stress.stress_level * FINANCIAL_STRESS_MECHANICS["health_impact_per_stress"]["mental_health"] / 100
    
    player.health.health = max(0, player.health.health + health_impact)
    player.health.mental_health = max(0, player.health.mental_health + mental_impact)
    
    # Trigger stories
    stories = []
    if stress.stress_level > 60:
        story = _trigger_story(player, "rent_crunch")
        if story:
            stories.append(story)
    
    if stress.debt_ratio > 0.8:
        story = _trigger_story(player, "debt_realization")
        if story:
            stories.append(story)
    
    if stress.stress_level < 30 and stress.emergency_fund_months > 3:
        story = _trigger_story(player, "freedom_moment")
        if story:
            stories.append(story)
    
    return {
        "stress_level": float(stress.stress_level),
        "debt_ratio": float(stress.debt_ratio),
        "emergency_fund_months": float(stress.emergency_fund_months),
        "bankruptcy_risk": float(stress.bankruptcy_risk),
        "health_impact": float(health_impact),
        "mental_health_impact": float(mental_impact),
        "stories_triggered": stories,
    }


def _check_financial_achievements(player: Player) -> list[dict]:
    """Check all financial achievements and unlock new ones."""
    unlocked = []
    
    # First tax filing
    if player.financial_responsibility.has_had_tax_filing and "first_tax_filing" not in [a.achievement_id for a in player.financial_responsibility.unlocked_achievements]:
        achievement = _unlock_achievement(player, "first_tax_filing")
        if achievement:
            unlocked.append(achievement)
    
    # Emergency fund starter (1 month)
    if player.financial_responsibility.financial_stress.emergency_fund_months >= 1 and "emergency_fund_starter" not in [a.achievement_id for a in player.financial_responsibility.unlocked_achievements]:
        achievement = _unlock_achievement(player, "emergency_fund_starter")
        if achievement:
            unlocked.append(achievement)
    
    # Emergency fund solid (3 months)
    if player.financial_responsibility.financial_stress.emergency_fund_months >= 3 and "emergency_fund_solid" not in [a.achievement_id for a in player.financial_responsibility.unlocked_achievements]:
        achievement = _unlock_achievement(player, "emergency_fund_solid")
        if achievement:
            unlocked.append(achievement)
    
    # Debt free
    if player.financial_responsibility.total_non_student_debt == 0 and player.financial_responsibility.total_unexpected_costs > 0 and "debt_free" not in [a.achievement_id for a in player.financial_responsibility.unlocked_achievements]:
        achievement = _unlock_achievement(player, "debt_free")
        if achievement:
            unlocked.append(achievement)
    
    # $10k saved
    if player.financial_responsibility.emergency_fund >= 10000 and "ten_thousand_saved" not in [a.achievement_id for a in player.financial_responsibility.unlocked_achievements]:
        achievement = _unlock_achievement(player, "ten_thousand_saved")
        if achievement:
            unlocked.append(achievement)
    
    # Financial responsibility (platinum)
    if (player.financial_responsibility.financial_stress.stress_level < 30 and
        player.financial_responsibility.financial_stress.emergency_fund_months >= 3 and
        player.financial_responsibility.total_non_student_debt < 1000 and
        "financial_responsibility" not in [a.achievement_id for a in player.financial_responsibility.unlocked_achievements]):
        achievement = _unlock_achievement(player, "financial_responsibility")
        if achievement:
            unlocked.append(achievement)
    
    return unlocked


def _unlock_achievement(player: Player, achievement_id: str) -> dict | None:
    """Unlock a financial achievement."""
    if achievement_id not in FINANCIAL_ACHIEVEMENTS:
        return None
    
    achievement_def = FINANCIAL_ACHIEVEMENTS[achievement_id]
    
    achievement = FinancialAchievement(
        achievement_id=achievement_id,
        title=achievement_def["title"],
        milestone_type=achievement_def["milestone_type"],
        achieved_semester=player.semester,
        description=achievement_def["description"],
    )
    
    player.financial_responsibility.unlocked_achievements.append(achievement)
    
    return {
        "achievement_id": achievement_id,
        "title": achievement_def["title"],
        "description": achievement_def["description"],
        "tier": achievement_def.get("tier", "bronze"),
    }


def _trigger_story(player: Player, story_id: str) -> dict | None:
    """Trigger a financial story."""
    if story_id not in FINANCIAL_STORIES:
        return None
    
    if story_id in player.financial_responsibility.stories_shown:
        return None
    
    story_def = FINANCIAL_STORIES[story_id]
    player.financial_responsibility.stories_shown.append(story_id)
    
    # Apply effects
    if "effect_stress" in story_def:
        player.financial_responsibility.financial_stress.stress_level += story_def["effect_stress"]
    
    if "effect_literacy" in story_def:
        player.financial_responsibility.literacy.tax_awareness += story_def.get("effect_literacy", 0) * 0.3
        player.financial_responsibility.literacy.budget_skill += story_def.get("effect_literacy", 0) * 0.4
        player.financial_responsibility.literacy.debt_management += story_def.get("effect_literacy", 0) * 0.3
    
    return {
        "story_id": story_id,
        "title": story_def["title"],
        "message": story_def["message"],
        "tone": story_def["tone"],
    }


def get_financial_summary(player: Player) -> dict:
    """Get complete financial responsibility summary."""
    if not hasattr(player, 'financial_responsibility'):
        player.financial_responsibility = FinancialResponsibility()
    
    fr = player.financial_responsibility
    
    return {
        "income": {
            "gross_annual": float(fr.gross_annual_income),
            "take_home_annual": float(fr.take_home_annual),
            "effective_tax_rate": float(fr.effective_tax_rate),
            "monthly_take_home": float(fr.take_home_annual / 12) if fr.take_home_annual > 0 else 0,
        },
        "expenses": {
            "monthly_total": float(fr.total_monthly_cost),
            "annual_total": float(fr.total_monthly_cost * 12),
            "breakdown": [
                {"category": e.category, "name": e.name, "amount": float(e.amount)}
                for e in fr.monthly_expenses
            ],
        },
        "emergency_fund": {
            "current": float(fr.emergency_fund),
            "goal": float(fr.emergency_fund_goal),
            "percent_to_goal": float((fr.emergency_fund / fr.emergency_fund_goal) * 100) if fr.emergency_fund_goal > 0 else 0,
            "months_covered": float(fr.financial_stress.emergency_fund_months),
        },
        "debt": {
            "credit_card": float(fr.credit_card_debt),
            "emergency": float(fr.emergency_debt),
            "total_non_student": float(fr.total_non_student_debt),
            "debt_ratio": float(fr.financial_stress.debt_ratio),
        },
        "stress": {
            "level": float(fr.financial_stress.stress_level),
            "status": _stress_status(fr.financial_stress.stress_level),
            "bankruptcy_risk": float(fr.financial_stress.bankruptcy_risk),
        },
        "literacy": {
            "tax_awareness": float(fr.literacy.tax_awareness),
            "budget_skill": float(fr.literacy.budget_skill),
            "debt_management": float(fr.literacy.debt_management),
            "investment_knowledge": float(fr.literacy.investment_knowledge),
            "lessons_learned": fr.literacy.lessons_learned,
        },
        "achievements": [
            {"id": a.achievement_id, "title": a.title, "semester": a.achieved_semester}
            for a in fr.unlocked_achievements
        ],
        "unexpected_expenses_history": [
            {"name": e.name, "amount": float(e.amount), "category": e.category, "semester": e.semester, "resolved": e.resolved}
            for e in fr.unexpected_expenses
        ],
    }


def _stress_status(level: float) -> str:
    if level < 20:
        return "Low"
    elif level < 40:
        return "Moderate"
    elif level < 60:
        return "High"
    elif level < 80:
        return "Severe"
    else:
        return "CRITICAL"
