"""
Store & Finance Integration System

Connects store purchases with job income, tuition costs, and financial planning.
Creates strategic decision-making around money and purchases.

Key Features:
1. Income Projection - Show how much player will earn this semester from job
2. Tuition Impact - Show tuition burden relative to income
3. Subscription Tracking - Recurring items affect monthly budget
4. ROI Analysis - Show impact of stress-reducing purchases on job performance
5. Financial Warnings - Alert when purchases conflict with financial goals
"""

from typing import Dict, Optional, List, Tuple
from core_domain.player.player_model import Player
from catalogs.life_purchases import get_purchase, LIFE_PURCHASES
from catalogs.jobs import JOB_DEFS
from catalogs.colleges import COLLEGES


def calculate_semester_income(player: Player) -> float:
    """
    Calculate total income player will earn this semester from job.
    
    Income = hourly_wage × hours_per_week × 16 weeks
    Reduced by: performance rating (affects raises/overtime)
    """
    if not player.job or not player.career.current_job_id:
        return 0.0
    
    job = JOB_DEFS.get(player.career.current_job_id)
    if not job:
        return 0.0
    
    # Base income: hourly wage × hours × weeks per semester
    base_income = float(job.hourly_wage) * float(job.hours_per_week) * 16.0
    
    # Performance multiplier (affects actual earnings)
    # Low performance: 80% of base (people get fewer hours, fewer tips)
    # High performance: 120% of base (overtime, bonuses, tips)
    performance_mult = 0.8 + (player.career.performance_rating / 50.0) * 0.4
    performance_mult = max(0.7, min(1.3, performance_mult))  # Clamp to 70%-130%
    
    return base_income * performance_mult


def calculate_semester_tuition(player: Player) -> float:
    """Calculate tuition owed this semester."""
    college = COLLEGES.get(player.college_id)
    if not college:
        return 0.0
    
    yearly = float(college.get("base_tuition_per_year", 0.0))
    return yearly / 2.0  # Two semesters per year


def get_financial_summary(player: Player) -> Dict:
    """
    Get comprehensive financial summary for strategic decision-making.
    
    Returns:
    {
        "balance": current balance,
        "semester_income": projected income,
        "semester_tuition": amount owed,
        "income_after_tuition": balance + income - tuition,
        "monthly_budget": average monthly available money,
        "job_title": current job (or "No Job"),
        "job_hours": hours per week,
        "financial_health": "tight" | "comfortable" | "excellent"
    }
    """
    semester_income = calculate_semester_income(player)
    semester_tuition = calculate_semester_tuition(player)
    
    # Calculate subscription costs from purchases
    monthly_subscriptions = calculate_monthly_subscriptions(player)
    semester_subscription_cost = monthly_subscriptions * 4  # ~4 months per semester
    
    # Net available = balance + income - tuition - subscriptions
    available_after_essentials = (
        player.finance.balance + semester_income - semester_tuition - semester_subscription_cost
    )
    
    # Monthly budget (divide by ~4 months)
    monthly_available = available_after_essentials / 4.0
    
    # Determine financial health
    if monthly_available < 0:
        health = "critical"
    elif monthly_available < 500:
        health = "tight"
    elif monthly_available < 1500:
        health = "comfortable"
    else:
        health = "excellent"
    
    job_title = "No Job"
    job_hours = 0
    if player.job:
        job = JOB_DEFS.get(player.career.current_job_id)
        if job:
            job_title = job.title
            job_hours = job.hours_per_week
    
    return {
        "current_balance": float(player.finance.balance),
        "semester_income": float(semester_income),
        "semester_tuition": float(semester_tuition),
        "monthly_subscriptions": float(monthly_subscriptions),
        "income_after_essentials": float(available_after_essentials),
        "monthly_available": float(monthly_available),
        "job_title": job_title,
        "job_hours": job_hours,
        "performance_rating": float(player.career.performance_rating),
        "financial_health": health,
    }


def calculate_monthly_subscriptions(player: Player) -> float:
    """
    Calculate total monthly subscription costs from recurring purchases.
    Includes: gym ($120/mo), streaming service, coffee subscription, etc.
    """
    # Check purchase history for recurring items
    monthly_cost = 0.0
    subscriptions = {
        "gym_membership": 10.0,  # $120/year ÷ 12
        "streaming_subscription": 12.0,  # $12-15/month typical
        "meal_prep": 75.0,  # $300/month for meal service
    }
    
    for purchase_id, monthly_charge in subscriptions.items():
        # Check if player has purchased this this semester
        for event in player.history:
            if event.semester == player.semester and event.label == f"purchase:{purchase_id}":
                monthly_cost += monthly_charge
    
    return monthly_cost


def get_purchase_affordability_analysis(player: Player, purchase_id: str) -> Dict:
    """
    Analyze if a purchase makes financial sense.
    
    Returns affordability metrics:
    {
        "can_afford_now": boolean,
        "shortage": amount needed,
        "impact_on_monthly_budget": how it affects monthly spending,
        "is_recurring": if it has monthly costs,
        "days_of_income": how many days of work required,
        "financial_warning": message about financial impact
    }
    """
    purchase = get_purchase(purchase_id)
    if not purchase:
        return {"error": "Purchase not found", "purchase_name": "Unknown"}
    
    summary = get_financial_summary(player)
    
    # Can afford now?
    can_afford = player.finance.balance >= purchase.cost
    shortage = max(0, purchase.cost - player.finance.balance)
    
    # Income needed to cover it
    if player.job:
        job = JOB_DEFS.get(player.career.current_job_id)
        if job:
            hourly_wage = float(job.hourly_wage)
            hours_needed = purchase.cost / hourly_wage
            days_of_work = hours_needed / 8.0  # 8-hour workdays
        else:
            days_of_work = 0
    else:
        days_of_work = 0
    
    # Impact on monthly budget
    monthly_impact = 0.0
    is_recurring = False
    if purchase_id in ["gym_membership", "streaming_subscription", "meal_prep"]:
        # Get monthly cost from LIFE_PURCHASES
        p = LIFE_PURCHASES.get(purchase_id)
        if p and hasattr(p, 'monthly_cost'):
            monthly_impact = p.monthly_cost
            is_recurring = True
    
    new_monthly = summary["monthly_available"] - monthly_impact
    
    # Financial warning
    warning = None
    if shortage > 0:
        warning = f"⚠️ You're short ${shortage:.2f}. Need {days_of_work:.1f} more days of work to afford this."
    elif is_recurring and new_monthly < 400:
        warning = f"⚠️ This subscription would reduce your monthly budget to ${new_monthly:.2f}—very tight!"
    elif purchase.cost > summary["monthly_available"]:
        warning = f"⚠️ This costs more than your monthly available budget (${summary['monthly_available']:.2f}). Consider saving first."
    
    return {
        "purchase_id": purchase_id,
        "purchase_name": purchase.name,
        "cost": float(purchase.cost),
        "can_afford_now": can_afford,
        "shortage": float(shortage),
        "is_recurring": is_recurring,
        "monthly_impact": float(monthly_impact),
        "new_monthly_budget": float(new_monthly),
        "days_of_income_required": float(days_of_work),
        "financial_warning": warning,
    }


def get_income_optimization_recommendations(player: Player) -> List[Dict]:
    """
    Suggest ways to improve income vs current spending.
    
    Considers:
    - Low job hours? Suggest switching to higher-pay job
    - High stress? Therapy/spa reduces stress → better job performance → raises
    - Low GPA? Study materials might be worthwhile investment
    
    Returns list of actionable recommendations.
    """
    recommendations = []
    summary = get_financial_summary(player)
    
    # Low monthly budget?
    if summary["monthly_available"] < 300:
        recommendations.append({
            "category": "income",
            "icon": "💼",
            "title": "Income is Tight",
            "suggestion": "Consider switching to a higher-paying job or working more hours",
            "impact": "Could add $200-500/month",
            "priority": "high"
        })
    
    # High stress?
    if player.stats.stress > 70:
        recommendations.append({
            "category": "wellbeing",
            "icon": "😌",
            "title": "Stress Reducing Purchases Help Income",
            "suggestion": "Therapy ($300) or massage ($60) reduces stress → better job performance → possible raise",
            "roi": "Invest $300 now → potentially +$100/month long-term",
            "priority": "high"
        })
    
    # Good financial health?
    if summary["financial_health"] == "excellent":
        recommendations.append({
            "category": "investment",
            "icon": "🎯",
            "title": "You Can Afford Major Purchases",
            "suggestion": "Consider investing in laptop ($1200) for career, car ($8000) for flexibility",
            "impact": "These unlock career/lifestyle benefits",
            "priority": "medium"
        })
    
    # Performance is low?
    if summary["performance_rating"] < 40:
        recommendations.append({
            "category": "performance",
            "icon": "📈",
            "title": "Boost Your Job Performance",
            "suggestion": "Better sleep, less stress, and coffee could improve work quality → raises",
            "investment": "Small purchases ($15-60) could improve performance rating",
            "priority": "medium"
        })
    
    return recommendations


def analyze_purchase_roi(player: Player, purchase_id: str) -> Dict:
    """
    Analyze return-on-investment for a purchase.
    
    For stress-reducing items (therapy, spa, massage):
    - Reduces stress → better job performance → potential wage increase
    - Calculate: Investment → Stress reduction → Income gain over semester
    
    For skill/career items (laptop, car):
    - Enables new job opportunities
    - Calculate: Investment → Opportunity unlock → Long-term income gain
    """
    purchase = get_purchase(purchase_id)
    if not purchase:
        return {}
    
    # Estimate stress reduction and performance impact
    stress_reduction = sum(
        e.change for e in purchase.effects if e.stat_name == "stress"
    )
    
    # Performance improvement (lower stress = better performance)
    performance_improvement = abs(stress_reduction) * 0.15  # Each stress point reduces 15% of performance boost
    
    # Estimate wage increase (performance improvement × base wage)
    current_income = calculate_semester_income(player)
    potential_raise = (performance_improvement / 100.0) * current_income * 0.15  # 15% max raise
    
    # Payback period (when does the raise recoup the investment?)
    if potential_raise > 0:
        payback_semesters = purchase.cost / potential_raise
    else:
        payback_semesters = float('inf')
    
    return {
        "purchase_id": purchase_id,
        "purchase_name": purchase.name,
        "investment": float(purchase.cost),
        "stress_reduction": float(stress_reduction),
        "estimated_performance_gain": float(performance_improvement),
        "estimated_income_gain_per_semester": float(potential_raise),
        "payback_period_semesters": float(min(payback_semesters, 10)),  # Cap at 10 semesters
        "roi_summary": _get_roi_summary(purchase.cost, potential_raise),
    }


def _get_roi_summary(cost: float, gain: float) -> str:
    """Create human-readable ROI summary."""
    if gain == 0:
        return "No direct income impact, but improves wellbeing"
    
    payback = cost / gain if gain > 0 else float('inf')
    
    if payback < 1:
        return f"⭐ Excellent ROI: Pays for itself in {payback:.1f} semesters"
    elif payback < 2:
        return f"✅ Good ROI: Pays for itself in {payback:.1f} semesters"
    elif payback < 4:
        return f"ℹ️ Moderate ROI: Pays for itself in {payback:.1f} semesters"
    else:
        return "🤔 Low ROI: Takes many semesters to recoup investment"


def create_financial_dashboard_data(player: Player) -> Dict:
    """
    Create comprehensive financial dashboard for UI.
    Combines all financial integration data for display.
    """
    summary = get_financial_summary(player)
    recommendations = get_income_optimization_recommendations(player)
    
    return {
        "financial_summary": summary,
        "recommendations": recommendations,
        "warning": _get_financial_warning(player, summary),
        "opportunities": _get_financial_opportunities(player, summary),
    }


def _get_financial_warning(player: Player, summary: Dict) -> Optional[str]:
    """Generate critical financial warning if needed."""
    if summary["financial_health"] == "critical":
        return "🚨 CRITICAL: You're spending more than you earn this semester! Consider taking a higher-paying job."
    elif summary["income_after_essentials"] < 0:
        return "⚠️ WARNING: Tuition + subscriptions exceed your income. You'll go into debt."
    elif summary["monthly_available"] < 200:
        return "⚠️ Tight Budget: Limited discretionary spending this semester."
    return None


def _get_financial_opportunities(player: Player, summary: Dict) -> List[str]:
    """Identify financial opportunities."""
    opportunities = []
    
    if player.career.performance_rating > 70:
        opportunities.append(f"💰 High Performance! Negotiate for a raise (+10-15% possible)")
    
    if summary["financial_health"] in ["comfortable", "excellent"]:
        opportunities.append(f"💳 Good Financial Position: Can invest in career items")
    
    if player.stats.stress < 30 and player.stats.happiness > 70:
        opportunities.append(f"✨ Excellent Wellbeing: Work quality high → bonus/raise likely")
    
    return opportunities
