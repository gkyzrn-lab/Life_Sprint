"""
Credit card products from different bank tiers.
Teaches students about APR, credit limits, perks, and credit score building.
"""

from typing import Dict, List
from enum import Enum

class BankTier(str, Enum):
    PREMIUM = "premium"  # Top-tier banks
    STANDARD = "standard"  # Mid-tier banks
    STARTER = "starter"  # Student-focused banks

class CreditCardCategory(str, Enum):
    STUDENT = "student"
    CASHBACK = "cashback"
    REWARDS = "rewards"
    TRAVEL = "travel"
    SECURED = "secured"

# Credit Card Products
CREDIT_CARDS = {
    # PREMIUM TIER BANKS (High fees, high perks, but also high APR - can be a trap!)
    "premium_rewards_platinum": {
        "id": "premium_rewards_platinum",
        "bank_name": "Chase Sapphire",
        "card_name": "Student Rewards Platinum",
        "tier": BankTier.PREMIUM,
        "category": CreditCardCategory.REWARDS,
        "apr": 24.99,  # HIGH APR - expensive if you carry a balance!
        "annual_fee": 495,  # $495/year - VERY expensive! First year waived.
        "first_year_fee_waived": True,
        "credit_limit_range": (5000, 15000),
        "signup_bonus": 500,  # Big bonus to lure you in
        "spending_threshold": 1000,  # Spend $1,000 in 3 months for bonus
        
        "perks": {
            "cashback_rate": 0.02,  # 2% on all purchases
            "category_bonuses": {
                "dining": 0.03,  # 3% on dining
                "travel": 0.03  # 3% on travel
            },
            "gym_membership": True,
            "gym_monthly_value": 25,
            "streaming_credits": 10,  # $10/month streaming credit
            "travel_insurance": True,
            "purchase_protection": True,
            "no_foreign_transaction_fees": True
        },
        
        "requirements": {
            "min_credit_score": 700,
            "min_income": 12000,  # Annual income
            "must_be_student": True
        },
        
        "credit_building": {
            "reports_to_bureaus": True,
            "credit_score_impact": "high",
            "increases_credit_limit": True,
            "limit_increase_after_months": 6
        },
        
        "educational_info": {
            "best_for": "High spenders who use ALL perks AND pay in full every month",
            "warning": "$495 annual fee + 25% APR = DANGEROUS COMBO! If you carry even $1,000 balance, you pay $250 interest PLUS $495 fee = $745/year!",
            "tip": "This card is a TRAP unless you're wealthy. Most students should avoid. High fees + high APR = double whammy."
        },
        
        "application_difficulty": "hard"
    },
    
    "premium_cashback_elite": {
        "id": "premium_cashback_elite",
        "bank_name": "Citi Bank",
        "card_name": "Student Cashback Elite",
        "tier": BankTier.PREMIUM,
        "category": CreditCardCategory.CASHBACK,
        "apr": 23.99,  # HIGH APR - not as "elite" as it sounds!
        "annual_fee": 395,  # $395/year - expensive!
        "first_year_fee_waived": False,
        "credit_limit_range": (3000, 10000),
        "signup_bonus": 350,
        "spending_threshold": 750,
        
        "perks": {
            "cashback_rate": 0.015,  # 1.5% on all purchases
            "category_bonuses": {
                "groceries": 0.05,  # 5% on groceries
                "gas": 0.03  # 3% on gas
            },
            "price_protection": True,
            "extended_warranty": True,
            "fraud_protection": "zero_liability",
            "credit_score_monitoring": True
        },
        
        "requirements": {
            "min_credit_score": 680,
            "min_income": 10000,
            "must_be_student": True
        },
        
        "credit_building": {
            "reports_to_bureaus": True,
            "credit_score_impact": "high",
            "increases_credit_limit": True,
            "limit_increase_after_months": 6
        },
        
        "educational_info": {
            "best_for": "Heavy spenders who pay in full every month",
            "warning": "$395 annual fee + 24% APR! Need to spend $7,900/year on groceries just to break even. That's unrealistic for most students!",
            "tip": "$395 fee is VERY high for students. If you carry any balance, the 24% APR destroys any cashback benefits. Stick with free cards!"
        },
        
        "application_difficulty": "hard"
    },
    
    # STANDARD TIER BANKS (Reasonable rates, good perks, moderate requirements)
    "standard_student_visa": {
        "id": "standard_student_visa",
        "bank_name": "Bank of America",
        "card_name": "Student Visa Card",
        "tier": BankTier.STANDARD,
        "category": CreditCardCategory.STUDENT,
        "apr": 19.99,
        "annual_fee": 0,
        "credit_limit_range": (500, 2000),
        "signup_bonus": 50,
        "spending_threshold": 300,
        
        "perks": {
            "cashback_rate": 0.01,  # 1% on all purchases
            "category_bonuses": {
                "online_shopping": 0.025  # 2.5% online
            },
            "spotify_premium": True,
            "spotify_monthly_value": 10,
            "student_discounts": True,
            "discount_partners": ["Amazon", "Best Buy", "Apple"],
            "free_credit_score": True
        },
        
        "requirements": {
            "min_credit_score": 630,
            "min_income": 6000,
            "must_be_student": True
        },
        
        "credit_building": {
            "reports_to_bureaus": True,
            "credit_score_impact": "medium",
            "increases_credit_limit": True,
            "limit_increase_after_months": 12
        },
        
        "educational_info": {
            "best_for": "Students building credit for the first time",
            "warning": "20% APR is HIGH. But $0 annual fee means you're not losing money just for having the card.",
            "tip": "No annual fee = perfect starter card. Set up auto-pay for full balance. Build credit for free!"
        },
        
        "application_difficulty": "medium"
    },
    
    "standard_cashback_basic": {
        "id": "standard_cashback_basic",
        "bank_name": "Wells Fargo",
        "card_name": "Student Cashback Card",
        "tier": BankTier.STANDARD,
        "category": CreditCardCategory.CASHBACK,
        "apr": 20.49,
        "annual_fee": 0,
        "credit_limit_range": (500, 1500),
        "signup_bonus": 30,
        "spending_threshold": 200,
        
        "perks": {
            "cashback_rate": 0.01,  # 1% on all purchases
            "cell_phone_protection": True,
            "monthly_cell_protection_value": 15,
            "student_loan_payment_discount": 0.0025,  # 0.25% off if you have their student loan
            "financial_literacy_resources": True,
            "budgeting_tools": True
        },
        
        "requirements": {
            "min_credit_score": 620,
            "min_income": 5000,
            "must_be_student": True
        },
        
        "credit_building": {
            "reports_to_bureaus": True,
            "credit_score_impact": "medium",
            "increases_credit_limit": True,
            "limit_increase_after_months": 12
        },
        
        "educational_info": {
            "best_for": "Students who need basic cashback and cell phone protection",
            "warning": "20% APR is expensive. But $0 annual fee means no penalty for light use.",
            "tip": "No annual fee = no pressure to 'get your money's worth'. Use it, pay it off, build credit."
        },
        
        "application_difficulty": "medium"
    },
    
    # STARTER TIER BANKS (Higher rates, fewer perks, easiest to get)
    "starter_secured_card": {
        "id": "starter_secured_card",
        "bank_name": "Discover",
        "card_name": "Secured Student Card",
        "tier": BankTier.STARTER,
        "category": CreditCardCategory.SECURED,
        "apr": 22.99,
        "annual_fee": 0,
        "credit_limit_range": (200, 500),  # Based on security deposit
        "requires_security_deposit": True,
        "security_deposit_amount": 200,  # Minimum deposit
        "deposit_refund_after_months": 8,  # Get deposit back after 8 months of good payment
        "signup_bonus": 0,
        
        "perks": {
            "cashback_rate": 0.01,  # 1% on all purchases
            "category_bonuses": {
                "gas": 0.02,  # 2% on gas
                "restaurants": 0.02  # 2% on restaurants
            },
            "free_fico_score": True,
            "cashback_match_first_year": True,  # Doubles cashback first year
            "graduates_to_unsecured": True  # Can become regular card
        },
        
        "requirements": {
            "min_credit_score": 0,  # No minimum - secured card!
            "min_income": 0,
            "must_be_student": False,
            "requires_security_deposit": True
        },
        
        "credit_building": {
            "reports_to_bureaus": True,
            "credit_score_impact": "high",  # Great for building from scratch
            "increases_credit_limit": True,
            "limit_increase_after_months": 8,
            "can_graduate_to_unsecured": True
        },
        
        "educational_info": {
            "best_for": "Students with NO credit history or bad credit",
            "warning": "$200 deposit required, but $0 annual fee and you get deposit back after 8 months!",
            "tip": "Think of deposit as savings that builds your credit. No annual fee = no ongoing cost to build credit."
        },
        
        "application_difficulty": "easy"
    },
    
    "starter_basic_student": {
        "id": "starter_basic_student",
        "bank_name": "Capital One",
        "card_name": "Basic Student Card",
        "tier": BankTier.STARTER,
        "category": CreditCardCategory.STUDENT,
        "apr": 24.99,  # High APR but accepts almost everyone
        "annual_fee": 0,
        "credit_limit_range": (300, 1000),
        "signup_bonus": 0,
        
        "perks": {
            "cashback_rate": 0.0,  # No cashback
            "free_credit_monitoring": True,
            "fraud_alerts": True,
            "virtual_card_numbers": True,  # For online security
            "automatic_credit_line_reviews": True
        },
        
        "requirements": {
            "min_credit_score": 580,  # Very low requirement
            "min_income": 0,
            "must_be_student": True
        },
        
        "credit_building": {
            "reports_to_bureaus": True,
            "credit_score_impact": "medium",
            "increases_credit_limit": True,
            "limit_increase_after_months": 6
        },
        
        "educational_info": {
            "best_for": "Students who can't qualify for anything else",
            "warning": "25% APR is BRUTAL. But $0 annual fee means you can keep it forever while building credit.",
            "tip": "No annual fee = perfect for credit building. Use $20/month, pay off immediately, then upgrade later."
        },
        
        "application_difficulty": "easy"
    },
    
    "starter_prepaid_card": {
        "id": "starter_prepaid_card",
        "bank_name": "NetSpend",
        "card_name": "Student Prepaid Visa",
        "tier": BankTier.STARTER,
        "category": CreditCardCategory.SECURED,
        "apr": 0,  # No APR - it's prepaid!
        "annual_fee": 0,
        "monthly_fee": 5,  # Small monthly fee
        "credit_limit_range": (0, 0),  # No limit - you load money
        "is_prepaid": True,
        
        "perks": {
            "no_credit_check": True,
            "no_overdraft_fees": True,
            "mobile_app": True,
            "instant_notifications": True,
            "budget_tracking": True
        },
        
        "requirements": {
            "min_credit_score": 0,
            "min_income": 0,
            "must_be_student": False
        },
        
        "credit_building": {
            "reports_to_bureaus": False,  # Does NOT build credit
            "credit_score_impact": "none",
            "increases_credit_limit": False
        },
        
        "educational_info": {
            "best_for": "Students who want spending control without credit risk",
            "warning": "This does NOT build credit. It's training wheels for money management.",
            "tip": "Use this to learn budgeting, then move to a secured card to build credit."
        },
        
        "application_difficulty": "guaranteed"
    }
}

def get_card(card_id: str) -> Dict:
    """Get specific credit card details."""
    return CREDIT_CARDS.get(card_id)

def get_cards_by_tier(tier: BankTier) -> List[Dict]:
    """Get all cards in a specific tier."""
    return [card for card in CREDIT_CARDS.values() if card.get("tier") == tier]

def get_cards_player_qualifies_for(player_state: Dict) -> List[Dict]:
    """
    Get credit cards player qualifies for based on their financial state.
    
    Args:
        player_state: Player's current state including:
            - credit_score
            - annual_income
            - is_student
            - can_provide_deposit
    
    Returns:
        List of cards player qualifies for, sorted by tier (best first)
    """
    qualified = []
    
    credit_score = player_state.get("credit_score", 0)
    income = player_state.get("annual_income", 0)
    is_student = player_state.get("is_student", True)
    has_deposit_funds = player_state.get("balance", 0) >= 200
    
    for card_id, card in CREDIT_CARDS.items():
        requirements = card.get("requirements", {})
        
        # Check credit score
        min_score = requirements.get("min_credit_score", 0)
        if credit_score < min_score:
            continue
        
        # Check income
        min_income = requirements.get("min_income", 0)
        if income < min_income:
            continue
        
        # Check student status
        must_be_student = requirements.get("must_be_student", False)
        if must_be_student and not is_student:
            continue
        
        # Check security deposit
        needs_deposit = requirements.get("requires_security_deposit", False)
        if needs_deposit and not has_deposit_funds:
            continue
        
        qualified.append(card)
    
    # Sort by tier: premium first, then standard, then starter
    tier_order = {BankTier.PREMIUM: 0, BankTier.STANDARD: 1, BankTier.STARTER: 2}
    qualified.sort(key=lambda c: tier_order.get(c.get("tier"), 999))
    
    return qualified

def calculate_monthly_perks_value(card: Dict) -> float:
    """Calculate monthly value of all perks."""
    perks = card.get("perks", {})
    total_value = 0.0
    
    if perks.get("gym_membership"):
        total_value += perks.get("gym_monthly_value", 0)
    
    if perks.get("spotify_premium"):
        total_value += perks.get("spotify_monthly_value", 0)
    
    if perks.get("cell_phone_protection"):
        total_value += perks.get("monthly_cell_protection_value", 0)
    
    if perks.get("streaming_credits"):
        total_value += perks.get("streaming_credits", 0)
    
    return total_value

def estimate_annual_cost_benefit(card: Dict, monthly_spending: float) -> Dict:
    """
    Calculate real cost/benefit of a credit card based on usage.
    
    Args:
        card: Credit card details
        monthly_spending: How much player spends per month
    
    Returns:
        Dict with annual fees, interest (if carrying balance), cashback earned, perks value
    """
    annual_spending = monthly_spending * 12
    
    # Costs
    annual_fee = card.get("annual_fee", 0)
    first_year_waived = card.get("first_year_fee_waived", False)
    first_year_fee = 0 if first_year_waived else annual_fee
    
    # Benefits
    cashback_rate = card.get("perks", {}).get("cashback_rate", 0)
    cashback_earned = annual_spending * cashback_rate
    
    perks_value = calculate_monthly_perks_value(card) * 12
    
    signup_bonus = card.get("signup_bonus", 0)
    
    # First year calculation
    first_year_benefit = cashback_earned + perks_value + signup_bonus - first_year_fee
    
    # Ongoing years calculation (no signup bonus, full annual fee)
    ongoing_benefit = cashback_earned + perks_value - annual_fee
    
    return {
        "annual_fee": annual_fee,
        "first_year_fee": first_year_fee,
        "cashback_earned": round(cashback_earned, 2),
        "perks_annual_value": round(perks_value, 2),
        "signup_bonus": signup_bonus,
        "first_year_total_benefit": round(cashback_earned + perks_value + signup_bonus, 2),
        "first_year_net_benefit": round(first_year_benefit, 2),
        "ongoing_annual_benefit": round(ongoing_benefit, 2),
        "break_even_spending": round(annual_fee / cashback_rate, 2) if cashback_rate > 0 else None
    }

def get_credit_building_advice(current_score: int) -> Dict:
    """Get advice on building credit score."""
    if current_score == 0:
        return {
            "status": "No Credit History",
            "recommendation": "Start with a secured card (Discover Secured) or become authorized user on parent's card",
            "timeline": "6 months to establish score",
            "best_cards": ["starter_secured_card"],
            "tips": [
                "Use card for small purchases ($20-50/month)",
                "Pay FULL balance before due date",
                "Never miss a payment - set up auto-pay",
                "Keep utilization under 30% of limit"
            ]
        }
    elif current_score < 630:
        return {
            "status": "Poor Credit",
            "recommendation": "Focus on payment history and utilization",
            "timeline": "6-12 months to reach fair credit",
            "best_cards": ["starter_secured_card", "starter_basic_student"],
            "tips": [
                "Pay on time EVERY TIME (35% of score)",
                "Keep balance under 10% of limit (30% of score)",
                "Don't apply for multiple cards (hard inquiries hurt)",
                "Dispute any errors on credit report"
            ]
        }
    elif current_score < 680:
        return {
            "status": "Fair Credit",
            "recommendation": "Upgrade to standard tier cards for better terms",
            "timeline": "6-12 months to reach good credit",
            "best_cards": ["standard_student_visa", "standard_cashback_basic"],
            "tips": [
                "Continue perfect payment history",
                "Request credit limit increase (lowers utilization)",
                "Diversify with 2-3 cards for better credit mix",
                "Older accounts help - don't close old cards"
            ]
        }
    elif current_score < 740:
        return {
            "status": "Good Credit",
            "recommendation": "You qualify for premium cards with best rewards",
            "timeline": "6-12 months to reach excellent credit",
            "best_cards": ["premium_cashback_elite", "standard_student_visa"],
            "tips": [
                "Maintain low utilization (under 10%)",
                "Consider becoming authorized user on premium card",
                "Pay attention to credit mix (cards + loans + rent reporting)",
                "Monitor score monthly for errors"
            ]
        }
    else:  # 740+
        return {
            "status": "Excellent Credit",
            "recommendation": "Access to all premium cards and best rates",
            "timeline": "Maintain this level!",
            "best_cards": ["premium_rewards_platinum", "premium_cashback_elite"],
            "tips": [
                "You're in the top 25% - keep doing what you're doing",
                "Leverage your score: negotiate lower APR",
                "Use premium cards for maximum rewards",
                "Your score opens doors for great loan rates later"
            ]
        }

def compare_cards(card_ids: List[str]) -> Dict:
    """Compare multiple credit cards side by side."""
    comparison = {
        "cards": [],
        "winner_categories": {}
    }
    
    for card_id in card_ids:
        card = get_card(card_id)
        if card:
            comparison["cards"].append({
                "id": card_id,
                "name": f"{card['bank_name']} {card['card_name']}",
                "tier": card["tier"],
                "apr": card["apr"],
                "credit_limit": card["credit_limit_range"][1],
                "cashback": card["perks"].get("cashback_rate", 0) * 100,
                "annual_fee": card["annual_fee"],
                "difficulty": card["application_difficulty"]
            })
    
    # Determine winners
    if comparison["cards"]:
        comparison["winner_categories"] = {
            "lowest_apr": min(comparison["cards"], key=lambda x: x["apr"])["name"],
            "highest_cashback": max(comparison["cards"], key=lambda x: x["cashback"])["name"],
            "highest_limit": max(comparison["cards"], key=lambda x: x["credit_limit"])["name"],
            "easiest_approval": min(comparison["cards"], key=lambda x: {"easy": 0, "medium": 1, "hard": 2, "guaranteed": -1}.get(x["difficulty"], 3))["name"]
        }
    
    return comparison

def get_all_cards() -> Dict[str, Dict]:
    """Get all credit cards."""
    return CREDIT_CARDS
