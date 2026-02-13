"""Credit score system for Life Sprint.

Teaches students:
- How credit scores are calculated
- Building credit from zero
- Impact of payment history, credit utilization, age of accounts
- Hard vs soft inquiries
- Credit repair and recovery
- Real-world credit consequences
"""

from typing import Dict, List, Optional, Literal, Any
from pydantic import BaseModel, Field
import random


class CreditAccount(BaseModel):
    """A credit account."""
    account_id: str
    account_type: Literal["credit_card", "auto_loan", "student_loan", "mortgage", "store_card"]
    
    # Account details
    credit_limit: float = 0  # For credit cards
    original_balance: float = 0  # For loans
    current_balance: float = 0
    minimum_payment: float = 0
    
    # Payment history
    payment_status: Literal["on_time", "30_days_late", "60_days_late", "90_days_late", "charged_off"] = "on_time"
    months_on_time: int = 0
    months_late: int = 0
    
    # Account age
    opened_date: int = 0  # months ago
    
    # Interest rate
    interest_rate: float = 0


class CreditProfile(BaseModel):
    """Player's credit profile."""
    player_id: str
    
    # Score
    credit_score: int = 300  # Ranges 300-850
    
    # Accounts
    accounts: List[CreditAccount] = Field(default_factory=list)
    
    # Score factors breakdown
    payment_history_score: int = 0  # 35% weight
    utilization_ratio: float = 0.0  # 30% weight
    average_account_age: int = 0  # 15% weight
    credit_mix: int = 0  # 10% weight (0-100)
    hard_inquiries: int = 0  # 10% weight (more = lower)
    
    # History
    total_late_payments: int = 0
    collections_accounts: int = 0
    bankruptcies: int = 0
    
    # Positive actions
    on_time_payments: int = 0


class CreditAction(BaseModel):
    """An action that affects credit."""
    action_id: str
    action_type: Literal["make_payment", "miss_payment", "open_account", 
                        "close_account", "max_out_card", "pay_down_balance",
                        "hard_inquiry", "collection_event"]
    
    description: str
    impact_on_score: int  # Can be negative or positive
    time_to_recover: int = 0  # Months until impact lessens


class CreditMythFact(BaseModel):
    """Credit myth vs fact."""
    myth_id: str
    myth: str
    fact: str
    category: Literal["score_building", "damage_prevention", "account_management", "inquiry_types"]
    impact: Literal["major", "moderate", "minor"]


class CreditScoreBreakdown(BaseModel):
    """Detailed breakdown of credit score."""
    total_score: int
    
    # Component scores (0-100)
    payment_history: int  # 35% weight
    credit_utilization: int  # 30% weight
    length_of_history: int  # 15% weight
    credit_mix: int  # 10% weight
    hard_inquiries: int  # 10% weight
    
    # Detailed info
    component_breakdown: Dict[str, Any]


# Credit score factors
CREDIT_SCORE_RANGES = {
    "excellent": (750, 850),
    "very_good": (700, 749),
    "good": (670, 699),
    "fair": (580, 669),
    "poor": (300, 579),
}

CREDIT_SCORE_MEANING = {
    "excellent": {
        "description": "Excellent credit. Get approved for most loans with best rates.",
        "mortgage_rate_approx": "2.5-3.0%",
        "credit_card_apr": "8-12%",
        "auto_loan_apr": "2-4%",
        "approval_likelihood": "95%+",
    },
    "very_good": {
        "description": "Very good credit. Likely to be approved for loans with competitive rates.",
        "mortgage_rate_approx": "3.0-3.5%",
        "credit_card_apr": "12-16%",
        "auto_loan_apr": "4-6%",
        "approval_likelihood": "90%+",
    },
    "good": {
        "description": "Good credit. Should be approved but may not get best rates.",
        "mortgage_rate_approx": "3.5-4.5%",
        "credit_card_apr": "16-20%",
        "auto_loan_apr": "6-10%",
        "approval_likelihood": "80%+",
    },
    "fair": {
        "description": "Fair credit. May be approved but with higher rates and stricter terms.",
        "mortgage_rate_approx": "5.0-6.5%",
        "credit_card_apr": "20-25%",
        "auto_loan_apr": "10-15%",
        "approval_likelihood": "50%+",
    },
    "poor": {
        "description": "Poor credit. Likely to be denied or face very unfavorable terms.",
        "mortgage_rate_approx": "6.5%+",
        "credit_card_apr": "25%+",
        "auto_loan_apr": "15%+",
        "approval_likelihood": "<30%",
    },
}


# Credit myths and facts
CREDIT_MYTHS: Dict[str, CreditMythFact] = {
    "myth_checking_credit": CreditMythFact(
        myth_id="myth_checking_credit",
        myth="Checking your own credit score hurts your credit.",
        fact="FALSE. Checking your own credit (soft inquiry) does NOT hurt your score. Only hard inquiries from lenders count. Check your credit free at annualcreditreport.com once per year.",
        category="inquiry_types",
        impact="major"
    ),
    
    "myth_no_credit_best": CreditMythFact(
        myth_id="myth_no_credit_best",
        myth="Having no credit is better than having bad credit.",
        fact="FALSE. No credit = no credit history = credit score of 0 or not calculable. Lenders prefer bad credit (shows history) over no credit. You need to BUILD credit to have any.",
        category="score_building",
        impact="major"
    ),
    
    "myth_carry_balance": CreditMythFact(
        myth_id="myth_carry_balance",
        myth="You should carry a balance on credit cards to build credit.",
        fact="FALSE. You do NOT need to pay interest to build credit. Pay full balance each month. Carrying a balance costs money and damages your utilization ratio. Just use the card and pay it off.",
        category="account_management",
        impact="major"
    ),
    
    "myth_close_cards": CreditMythFact(
        myth_id="myth_close_cards",
        myth="Closing old credit cards helps your credit score.",
        fact="FALSE. Closing cards HURTS your score because: 1) Reduces available credit (raises utilization ratio), 2) Shortens average account age. KEEP old cards open (even with $0 balance).",
        category="damage_prevention",
        impact="major"
    ),
    
    "myth_hard_inquiry_impact": CreditMythFact(
        myth_id="myth_hard_inquiry_impact",
        myth="Hard inquiries have a major long-term impact on credit.",
        fact="PARTIALLY TRUE. Hard inquiries drop score 5-10 points but impact decreases after 3 months and disappears after 12 months. Multiple hard inquiries in 14 days count as ONE (for auto/mortgage shopping).",
        category="inquiry_types",
        impact="moderate"
    ),
    
    "myth_divorce_credit": CreditMythFact(
        myth_id="myth_divorce_credit",
        myth="Divorce automatically removes your spouse from your joint credit accounts.",
        fact="FALSE. Divorce doesn't automatically change credit responsibility. You must formally remove the other person or refinance debt in your name only. Otherwise you're still liable.",
        category="account_management",
        impact="major"
    ),
    
    "myth_debt_disappear": CreditMythFact(
        myth_id="myth_debt_disappear",
        myth="Negative items disappear from credit report after 3 years.",
        fact="FALSE. Most negative items stay for 7 years. Bankruptcies stay for 10 years. Payment history is the largest factor (35%), so late payments hurt for YEARS.",
        category="damage_prevention",
        impact="major"
    ),
    
    "myth_paying_old_debt": CreditMythFact(
        myth_id="myth_paying_old_debt",
        myth="Paying off old debt immediately improves your credit score.",
        fact="PARTIALLY TRUE. Paying off CURRENT debt improves score. Paying off old collections accounts in good standing on your report might actually LOWER score temporarily (refreshes the damage).",
        category="damage_prevention",
        impact="moderate"
    ),
    
    "myth_income_affects_credit": CreditMythFact(
        myth_id="myth_income_affects_credit",
        myth="Your income affects your credit score.",
        fact="FALSE. Income does NOT appear on credit reports and does NOT affect credit scores. Only borrowing/payment behavior matters. Debt-to-income ratio matters for loan approval, not credit score.",
        category="score_building",
        impact="moderate"
    ),
    
    "myth_credit_repair_companies": CreditMythFact(
        myth_id="myth_credit_repair_companies",
        myth="Credit repair companies can remove accurate negative information from your credit report.",
        fact="FALSE. Credit repair companies are usually scams. If information is accurate, it cannot be removed (except after 7 years naturally). Dispute inaccuracies yourself for free at creditkarma.com or annualcreditreport.com.",
        category="account_management",
        impact="major"
    ),
}


# Credit actions and their impacts
CREDIT_ACTIONS_DATABASE: Dict[str, CreditAction] = {
    "on_time_payment": CreditAction(
        action_id="on_time_payment",
        action_type="make_payment",
        description="Make a payment on time",
        impact_on_score=5,  # Positive
        time_to_recover=0
    ),
    
    "missed_payment_30": CreditAction(
        action_id="missed_payment_30",
        action_type="miss_payment",
        description="Miss a payment by 30+ days",
        impact_on_score=-100,
        time_to_recover=12  # Stays on report 7 years, but impact lessens
    ),
    
    "missed_payment_60": CreditAction(
        action_id="missed_payment_60",
        action_type="miss_payment",
        description="Miss a payment by 60+ days",
        impact_on_score=-150,
        time_to_recover=24
    ),
    
    "new_credit_card": CreditAction(
        action_id="new_credit_card",
        action_type="open_account",
        description="Open a new credit card account",
        impact_on_score=-5,  # Small drop from hard inquiry
        time_to_recover=3
    ),
    
    "hard_inquiry": CreditAction(
        action_id="hard_inquiry",
        action_type="hard_inquiry",
        description="Lender does a hard inquiry",
        impact_on_score=-5,
        time_to_recover=12
    ),
    
    "high_utilization": CreditAction(
        action_id="high_utilization",
        action_type="max_out_card",
        description="Max out a credit card (100% utilization)",
        impact_on_score=-40,
        time_to_recover=3  # Recovers quickly when paid down
    ),
    
    "high_utilization_extended": CreditAction(
        action_id="high_utilization_extended",
        action_type="max_out_card",
        description="Keep credit card maxed out for 3+ months",
        impact_on_score=-60,
        time_to_recover=6
    ),
    
    "pay_down_balance": CreditAction(
        action_id="pay_down_balance",
        action_type="pay_down_balance",
        description="Pay down credit card balance (reduce utilization)",
        impact_on_score=+20,
        time_to_recover=1  # Quick improvement
    ),
    
    "charge_off": CreditAction(
        action_id="charge_off",
        action_type="collection_event",
        description="Account charged off (sent to collections)",
        impact_on_score=-200,
        time_to_recover=60  # 7 years on report
    ),
    
    "bankruptcy": CreditAction(
        action_id="bankruptcy",
        action_type="collection_event",
        description="File bankruptcy",
        impact_on_score=-250,
        time_to_recover=120  # 7-10 years on report
    ),
}


def create_credit_profile(player_id: str) -> CreditProfile:
    """Create a new credit profile for a player."""
    return CreditProfile(
        player_id=player_id,
        credit_score=0,  # No credit history
        accounts=[],
        payment_history_score=0,
        utilization_ratio=0.0,
        average_account_age=0,
        credit_mix=0,
        hard_inquiries=0,
        total_late_payments=0,
        collections_accounts=0,
        bankruptcies=0,
        on_time_payments=0
    )


def calculate_credit_score(profile: CreditProfile) -> int:
    """Calculate credit score based on profile.
    
    Score range: 300-850
    Components:
    - Payment history: 35%
    - Credit utilization: 30%
    - Length of history: 15%
    - Credit mix: 10%
    - Hard inquiries: 10%
    """
    
    # If no credit history, return 0 (not calculable)
    if len(profile.accounts) == 0:
        return 0
    
    # Payment history (35%)
    if profile.on_time_payments + profile.total_late_payments == 0:
        payment_score = 0
    else:
        on_time_pct = profile.on_time_payments / (profile.on_time_payments + profile.total_late_payments)
        # 100% on time = 850, 90% = 750, 80% = 650, etc
        payment_score = int(300 + (on_time_pct * 550))
    
    # Credit utilization (30%)
    if profile.utilization_ratio == 0:
        utilization_score = 750  # $0 balance is ideal
    else:
        # 0-10% = excellent, 10-30% = very good, 30-50% = good, 50%+ = bad
        if profile.utilization_ratio <= 0.10:
            utilization_score = 850
        elif profile.utilization_ratio <= 0.30:
            utilization_score = 800
        elif profile.utilization_ratio <= 0.50:
            utilization_score = 700
        elif profile.utilization_ratio <= 1.0:
            utilization_score = 500
        else:  # Over 100%
            utilization_score = 300
    
    # Length of history (15%)
    age_months = profile.average_account_age
    if age_months >= 96:  # 8+ years
        age_score = 850
    elif age_months >= 60:  # 5+ years
        age_score = 750
    elif age_months >= 24:  # 2+ years
        age_score = 650
    elif age_months >= 6:  # 6+ months
        age_score = 500
    else:
        age_score = 300
    
    # Credit mix (10%)
    # Count different account types
    account_types = len(set(a.account_type for a in profile.accounts))
    credit_mix_score = min(300 + (account_types * 100), 850)
    
    # Hard inquiries (10%)
    # More inquiries = lower score
    inquiry_score = max(300, 850 - (profile.hard_inquiries * 10))
    
    # Negative events (permanent impact)
    negative_impact = (profile.total_late_payments * 30) + (profile.collections_accounts * 100) + (profile.bankruptcies * 250)
    
    # Calculate weighted score
    base_score = (
        (payment_score * 0.35) +
        (utilization_score * 0.30) +
        (age_score * 0.15) +
        (credit_mix_score * 0.10) +
        (inquiry_score * 0.10)
    )
    
    final_score = int(base_score - negative_impact)
    final_score = max(300, min(850, final_score))
    
    return final_score


def get_credit_score_category(score: int) -> str:
    """Get credit score category."""
    for category, (min_score, max_score) in CREDIT_SCORE_RANGES.items():
        if min_score <= score <= max_score:
            return category
    return "poor"


def apply_credit_action(profile: CreditProfile, action: CreditAction) -> CreditProfile:
    """Apply an action to a credit profile."""
    
    if action.action_type == "make_payment":
        profile.on_time_payments += 1
    elif action.action_type == "miss_payment":
        profile.total_late_payments += 1
    elif action.action_type == "hard_inquiry":
        profile.hard_inquiries += 1
    elif action.action_type == "collection_event":
        if action.action_id == "bankruptcy":
            profile.bankruptcies += 1
        else:
            profile.collections_accounts += 1
    
    return profile


def get_credit_improvement_tips(score: int) -> List[str]:
    """Get personalized tips to improve credit score."""
    
    tips = []
    
    if score < 300:
        tips = [
            "🚀 You have no credit history. Open a secured credit card ($200-$500 deposit) and make on-time payments for 6+ months.",
            "✅ Consider becoming an authorized user on a family member's credit card (if they have good credit).",
            "📋 Pull your free credit report at annualcreditreport.com and dispute any errors.",
        ]
    elif score < 580:
        tips = [
            "🔥 CRITICAL: Make all payments on time immediately. Even one late payment will tank your score.",
            "💳 Pay down credit card balances. Get utilization below 30%.",
            "📞 Contact creditors about payment plans or hardship programs if you're struggling.",
            "🚨 Avoid opening new credit accounts (hard inquiries hurt).",
        ]
    elif score < 670:
        tips = [
            "📈 Keep paying on time. Payment history is 35% of your score.",
            "💰 Target credit card utilization below 10%. Every payment helps.",
            "⏰ Time helps - accounts age and negative items fall off after 7 years.",
            "🛑 Don't close old credit cards (hurts your average age and utilization ratio).",
        ]
    elif score < 700:
        tips = [
            "✨ You're getting close to 'very good' credit! Keep payments on time.",
            "💳 Reduce credit card utilization below 10% for a quick score boost.",
            "📜 Consider diversifying credit mix (auto loan, installment loan, mortgage).",
            "🔍 Monitor for errors on your credit report.",
        ]
    elif score < 750:
        tips = [
            "🌟 Great credit! Focus on maintaining it with on-time payments.",
            "💳 Keep credit card utilization very low (under 10%).",
            "🏠 You qualify for excellent mortgage and auto loan rates.",
            "🎯 Avoid unnecessary hard inquiries and new accounts.",
        ]
    else:
        tips = [
            "🏆 Excellent credit! You're in the top tier.",
            "🔒 Protect it by continuing on-time payments and low utilization.",
            "🏦 You qualify for the best interest rates on all loans.",
            "👨‍👩‍👧 Consider helping family members build credit (authorized user).",
        ]
    
    return tips


def get_credit_score_breakdown(profile: CreditProfile) -> CreditScoreBreakdown:
    """Get detailed breakdown of what makes up the score."""
    
    score = calculate_credit_score(profile)
    
    # Calculate component scores
    if profile.on_time_payments + profile.total_late_payments == 0:
        payment_component = 0
    else:
        on_time_pct = profile.on_time_payments / (profile.on_time_payments + profile.total_late_payments)
        payment_component = int(300 + (on_time_pct * 550))
    
    if profile.utilization_ratio == 0:
        utilization_component = 750
    else:
        if profile.utilization_ratio <= 0.10:
            utilization_component = 850
        elif profile.utilization_ratio <= 0.30:
            utilization_component = 800
        elif profile.utilization_ratio <= 0.50:
            utilization_component = 700
        elif profile.utilization_ratio <= 1.0:
            utilization_component = 500
        else:
            utilization_component = 300
    
    age_months = profile.average_account_age
    if age_months >= 96:
        age_component = 850
    elif age_months >= 60:
        age_component = 750
    elif age_months >= 24:
        age_component = 650
    elif age_months >= 6:
        age_component = 500
    else:
        age_component = 300
    
    account_types = len(set(a.account_type for a in profile.accounts))
    mix_component = min(300 + (account_types * 100), 850)
    
    inquiry_component = max(300, 850 - (profile.hard_inquiries * 10))
    
    return CreditScoreBreakdown(
        total_score=score,
        payment_history=payment_component,
        credit_utilization=utilization_component,
        length_of_history=age_component,
        credit_mix=mix_component,
        hard_inquiries=inquiry_component,
        component_breakdown={
            "payment_history": {
                "score": payment_component,
                "weight": "35%",
                "on_time_count": profile.on_time_payments,
                "late_count": profile.total_late_payments
            },
            "credit_utilization": {
                "score": utilization_component,
                "weight": "30%",
                "ratio": f"{profile.utilization_ratio * 100:.1f}%",
                "ideal": "0-10%"
            },
            "length_of_history": {
                "score": age_component,
                "weight": "15%",
                "average_age_months": profile.average_account_age,
                "ideal": "8+ years (96 months)"
            },
            "credit_mix": {
                "score": mix_component,
                "weight": "10%",
                "account_types": account_types,
                "ideal": "4+ different types"
            },
            "hard_inquiries": {
                "score": inquiry_component,
                "weight": "10%",
                "count": profile.hard_inquiries,
                "impact": "Decreases after 12 months"
            }
        }
    )


def get_myth_fact(myth_id: str) -> Optional[CreditMythFact]:
    """Get a specific myth/fact."""
    return CREDIT_MYTHS.get(myth_id)


def get_all_myths() -> List[CreditMythFact]:
    """Get all myths/facts."""
    return list(CREDIT_MYTHS.values())


def get_myths_by_category(category: str) -> List[CreditMythFact]:
    """Get myths by category."""
    return [m for m in CREDIT_MYTHS.values() if m.category == category]
