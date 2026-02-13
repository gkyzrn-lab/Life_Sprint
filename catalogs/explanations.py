"""
Educational explanations for financial and life decisions.
Shows real-world consequences and teaches concepts.
"""

from typing import Dict, List

# Financial Decision Explanations
FINANCIAL_EXPLANATIONS = {
    "student_loan": {
        "title": "Understanding Student Loans",
        "short": "Borrowed money you must repay with interest after graduation.",
        "long": "A student loan is money borrowed to pay for education. You'll start repaying it after graduation, typically with interest rates between 4-8%. The total amount you pay back will be MORE than you borrowed due to compound interest.",
        "example": "If you borrow $10,000 at 6% interest over 10 years, you'll pay back $13,322 total. That's $3,322 in interest!",
        "tip": "Always compare interest rates. Even 1% difference can save thousands of dollars.",
        "real_impact": {
            "low_debt": "Graduating with under $20K debt gives you career flexibility and less stress.",
            "medium_debt": "$20K-$50K is manageable but will affect your budget for 5-10 years.",
            "high_debt": "Over $50K significantly limits your life choices and delays major purchases like homes."
        }
    },
    
    "part_time_job": {
        "title": "Balancing Work and Study",
        "short": "Earn money now but sacrifice study time and possibly grades.",
        "long": "Working part-time during college helps pay bills and builds experience, BUT every hour worked is an hour not studying. Research shows working over 15 hours/week can hurt GPA.",
        "example": "Working 20 hours/week at $15/hour = $300/week ($1,200/month). But if your GPA drops from 3.5 to 3.0, you might lose scholarships worth $5,000/year.",
        "tip": "Find the sweet spot: 10-15 hours/week is usually sustainable without hurting grades.",
        "real_impact": {
            "0_hours": "More study time and better grades, but financial stress increases.",
            "10_15_hours": "Balanced approach - manageable income without sacrificing academics.",
            "20_plus_hours": "Good income but high stress and GPA risk. Only if necessary."
        }
    },
    
    "expensive_college": {
        "title": "College Cost vs. Value",
        "short": "More expensive doesn't always mean better outcomes.",
        "long": "A $60,000/year private school might offer prestige, but you could get similar education at a $20,000/year state school. That $160,000 difference (4 years) could be a house down payment!",
        "example": "Two students: One graduates from Elite U with $100K debt, another from State U with $20K debt. Both get $50K starting jobs. Who's better off?",
        "tip": "Look at graduate outcomes (job placement, starting salaries) not just rankings. State schools often have identical outcomes at 1/3 the cost.",
        "real_impact": {
            "budget_school": "Low debt, high freedom. Can take risks, travel, save early.",
            "mid_tier": "Moderate debt. Manageable with good job, tight budget for 5-7 years.",
            "elite_school": "High debt. Better network, but needs high-paying job immediately. Limited flexibility."
        }
    },
    
    "internship": {
        "title": "Why Internships Matter",
        "short": "Real experience employers actually care about.",
        "long": "85% of jobs go to candidates with relevant experience. Internships are how you get that. They also help you discover what you DON'T want to do (equally valuable!).",
        "example": "Student A: 3.8 GPA, no internships. Student B: 3.3 GPA, 2 internships. Student B gets hired first 70% of the time.",
        "tip": "Even unpaid internships can be worth it if you can afford it. But paid internships are ideal - you learn AND earn.",
        "real_impact": {
            "no_internship": "Harder job search, lower starting salary, longer time to employment.",
            "one_internship": "Competitive candidate, solid starting point, faster hiring.",
            "multiple_internships": "Top candidate, higher salary offers, often hired where you interned."
        }
    },
    
    "credit_card": {
        "title": "The Credit Card Trap",
        "short": "Easy money now, but dangerous if you can't pay it back.",
        "long": "Credit cards charge 18-25% interest. If you only pay minimums, a $1,000 purchase could take 10 years to pay off and cost $2,000 total!",
        "example": "Buy a $500 laptop on credit. Pay only $25/month minimum. Final cost: $783 over 3 years. That's a 56% markup!",
        "tip": "GOLDEN RULE: Only use credit cards if you can pay the FULL balance each month. Otherwise, it's a trap.",
        "real_impact": {
            "responsible_use": "Builds credit score, earns rewards, safe emergency backup.",
            "occasional_balance": "Small interest charges, manageable but wasteful.",
            "revolving_debt": "Debt spiral. Interest piles up. Can take years to escape. Avoid at all costs!"
        }
    },
    
    "scholarship": {
        "title": "Free Money You Never Repay",
        "short": "The best financial aid - no payback required!",
        "long": "Scholarships are FREE money based on merit, need, or specific criteria. Unlike loans, you never pay them back. Many go unclaimed because students don't apply!",
        "example": "Spending 10 hours applying for scholarships could earn $5,000. That's $500/hour - better than any job!",
        "tip": "Apply to everything you're eligible for. Even small $500 scholarships add up. Use scholarship search engines.",
        "real_impact": {
            "full_ride": "Zero debt, pure freedom. Focus entirely on learning and growth.",
            "partial_scholarship": "Significantly reduces debt burden. Every $1,000 in scholarships saves $1,300+ in loan repayment.",
            "no_scholarship": "Maximum debt. Work harder on applications next semester!"
        }
    },
    
    "credit_card_basics": {
        "title": "Credit Cards: Powerful Tool or Debt Trap?",
        "short": "Pay in full = free rewards. Carry balance = expensive debt.",
        "long": "Credit cards let you borrow money up to a limit and pay it back over time. If you pay the FULL balance each month, you pay $0 interest. If you only pay the minimum, you can pay 2-3x the original cost due to compound interest at 20-25% APR.",
        "example": "Buy $1,000 laptop. Pay off in full = $1,000 total. Pay minimum ($25/month) at 24% APR = $1,680 total over 5 years. That's a $680 interest tax!",
        "tip": "Golden rule: Only charge what you can pay off in full this month. Treat it like a debit card that builds credit, not free money.",
        "real_impact": {
            "pay_full": "Build credit score, earn cashback rewards, $0 interest. Credit cards work FOR you.",
            "pay_most": "Some interest but manageable. Try to pay in full next month.",
            "minimum_only": "Debt trap. 20%+ interest compounds. Takes years to pay off. Avoid at all costs!"
        }
    },
    
    "credit_score_building": {
        "title": "Your Credit Score: The 300-850 Game",
        "short": "Good credit saves you $50,000+ in your lifetime.",
        "long": "Your credit score (300-850) determines if you can rent apartments, get loans, and what interest rates you pay. It's calculated from: Payment history (35%), Amount owed (30%), Credit history length (15%), New credit (10%), Credit mix (10%).",
        "example": "Student A: 760 score, gets auto loan at 4% = $400/month. Student B: 600 score, gets auto loan at 12% = $500/month. Same car, $100/month difference = $6,000 over 5 years!",
        "tip": "Build it: Get ONE card, charge $20-50/month, pay in FULL before due date. Never miss payments. Keep balance under 30% of limit. That's it.",
        "real_impact": {
            "excellent_740plus": "Access to best rates on everything. Save $50,000+ on mortgages, cars, loans over lifetime.",
            "good_680_739": "Decent rates. Some premium cards available. Keep building!",
            "fair_620_679": "Higher interest rates. Harder to rent apartments. Focus on payment history.",
            "poor_below_620": "Very high rates or rejection. Get secured card, rebuild slowly."
        }
    },
    
    "apr_explained": {
        "title": "APR: The Hidden Cost of Credit Cards",
        "short": "Lower APR = less expensive debt if you carry balances.",
        "long": "APR (Annual Percentage Rate) is how much it costs to borrow money for a year. 24% APR means you pay 24% extra if you carry a balance for a year. But it compounds monthly, so it's actually worse. Lower APR = less expensive debt.",
        "example": "$1,000 balance at different APRs paying $50/month:\n• 15% APR = paid off in 23 months, $127 interest\n• 20% APR = paid off in 24 months, $178 interest\n• 25% APR = paid off in 25 months, $237 interest",
        "tip": "Always compare APR when choosing cards. If you EVER carry a balance (emergencies), lower APR saves hundreds.",
        "real_impact": {
            "premium_15_17": "Excellent APR. Hard to qualify but worth it if you sometimes carry balances.",
            "good_18_20": "Decent APR. Most responsible students can get this.",
            "high_21_24": "Expensive. Only use if you pay in full or it's your only option.",
            "predatory_25plus": "Avoid if possible. Debt trap territory."
        }
    },
    
    "credit_utilization": {
        "title": "Credit Utilization: The 30% Rule",
        "short": "Use under 30% of your credit limit for best score.",
        "long": "Credit utilization is how much of your credit limit you're using. It's 30% of your credit score calculation. Using more than 30% hurts your score, even if you pay on time. Under 10% is ideal.",
        "example": "You have $1,000 credit limit:\n• Spend $100 = 10% utilization = GREAT for credit score\n• Spend $400 = 40% utilization = Hurts credit score\n• Spend $900 = 90% utilization = Seriously damages score",
        "tip": "Keep spending under 30% of limit. If you have $1,000 limit, never have more than $300 balance. Want to spend more? Get higher limit or pay off more frequently.",
        "real_impact": {
            "under_10": "Optimal for credit score. Shows you don't need credit = ironically makes lenders want to give you more.",
            "10_30": "Good range. Doesn't hurt your score.",
            "30_50": "Starts hurting score. Lenders see you as higher risk.",
            "over_50": "Major score damage. Pay down immediately!"
        }
    },
    
    "annual_fees": {
        "title": "Annual Fees: Are Premium Cards Worth It?",
        "short": "Premium cards charge annual fees. Worth it ONLY if perks exceed the fee.",
        "long": "Annual fees ($75-$195) are how premium cards pay for perks like gym memberships, high cashback, and travel benefits. Basic student cards have $0 annual fee because they offer fewer perks. The key question: Will you use enough perks to justify the fee?",
        "example": "Premium card: $95 annual fee, $25/month gym ($300 value), 2% cashback on $500/month spending ($120 value).\n• Total perks: $420/year\n• Cost: $95 fee\n• Net benefit: $325/year (worth it!)\n\nBut if you don't use the gym:\n• Perks: $120 cashback\n• Cost: $95 fee\n• Net: Only $25 benefit (not worth it, get free card instead)",
        "tip": "Students on tight budgets: Start with $0 annual fee cards. Premium cards are for when you're established and can maximize perks.",
        "real_impact": {
            "use_all_perks": "Premium cards pay for themselves. $95 fee for $300-500 in perks = great deal.",
            "use_some_perks": "Marginal benefit. Might break even. Calculate carefully before committing.",
            "use_no_perks": "Losing money! $95/year for nothing. Cancel and get a no-fee card.",
            "no_fee_cards": "Perfect for students. No risk, no pressure, just build credit and earn what you can."
        }
    }
}

# Life Decision Explanations
LIFE_EXPLANATIONS = {
    "stress_management": {
        "title": "Why Stress Management Matters",
        "short": "High stress tanks your performance and health.",
        "long": "Chronic stress leads to poor sleep, worse grades, illness, and bad decisions. Your brain literally performs worse under sustained stress.",
        "example": "Students with managed stress score 15-20% higher on exams and have 50% fewer sick days.",
        "tip": "Regular exercise, 7-8 hours sleep, and weekly 'fun time' aren't luxuries - they're performance enhancers.",
        "real_impact": "Managing stress = better grades, better health, better decisions. It's not optional."
    },
    
    "social_life": {
        "title": "Social Connection = Success",
        "short": "Your network becomes your net worth.",
        "long": "College friendships often become lifelong connections, business partners, and job referrals. 70% of jobs come through networking, not applications.",
        "example": "That person you helped in study group might hire you at their company 5 years later.",
        "tip": "Balance is key: All social and no study = bad grades. All study and no social = no network and burnout.",
        "real_impact": "Strong social connections lead to better mental health, job opportunities, and life satisfaction."
    },
    
    "health_choices": {
        "title": "Your Body, Your Performance",
        "short": "Exercise and good nutrition improve grades, not just health.",
        "long": "Regular exercise increases blood flow to the brain, improving memory and focus by 20-30%. Proper nutrition stabilizes energy and mood.",
        "example": "Students who exercise 3x/week have GPA averaging 0.4 points higher than sedentary students.",
        "tip": "Even 20 minutes of walking daily makes a huge difference. Meal prep on Sundays to avoid junk food all week.",
        "real_impact": "Good health = better grades, more energy, lower stress, fewer sick days."
    }
}

# Compound Interest Explanations
COMPOUND_INTEREST_EXAMPLES = {
    "save_early": {
        "title": "The Magic of Starting Early",
        "scenario": "Starting to save at age 22 vs age 32",
        "person_a": "Saves $200/month from age 22-32 (10 years) then stops. Total invested: $24,000",
        "person_b": "Saves $200/month from age 32-62 (30 years). Total invested: $72,000",
        "result": "At age 62, Person A has MORE money ($185,000 vs $140,000) despite investing 1/3 as much!",
        "lesson": "Time in the market beats timing the market. Start saving NOW, even small amounts."
    },
    
    "debt_cost": {
        "title": "The True Cost of Debt",
        "scenario": "Graduating with $40,000 in student loans at 6% interest",
        "payment_plan_10yr": "Pay $444/month for 10 years. Total paid: $53,280 (that's $13,280 in interest)",
        "payment_plan_20yr": "Pay $287/month for 20 years. Total paid: $68,880 (that's $28,880 in interest)",
        "opportunity_cost": "If you invested that interest instead at 7% returns, you'd have $50,000-$100,000 extra by retirement!",
        "lesson": "Every dollar in interest is a dollar you can't invest. Pay off high-interest debt FAST."
    }
}

def get_explanation(category: str, key: str) -> Dict:
    """Get explanation for a specific decision."""
    if category == "financial":
        return FINANCIAL_EXPLANATIONS.get(key, {})
    elif category == "life":
        return LIFE_EXPLANATIONS.get(key, {})
    elif category == "compound_interest":
        return COMPOUND_INTEREST_EXAMPLES.get(key, {})
    return {}

def get_contextual_explanation(decision_type: str, context: Dict) -> Dict:
    """
    Generate a contextual explanation based on player's specific situation.
    
    Args:
        decision_type: Type of decision being made
        context: Player's current state (debt, GPA, stress, etc.)
    
    Returns:
        Personalized explanation with specific numbers
    """
    base_explanation = FINANCIAL_EXPLANATIONS.get(decision_type) or LIFE_EXPLANATIONS.get(decision_type)
    
    if not base_explanation:
        return {}
    
    # Personalize based on context
    personalized = base_explanation.copy()
    
    # Add specific numbers from player's situation
    if decision_type == "student_loan" and "loan_amount" in context:
        amount = context["loan_amount"]
        rate = context.get("interest_rate", 0.06)
        years = context.get("repayment_years", 10)
        
        total_paid = amount * (1 + rate) ** years
        interest_paid = total_paid - amount
        
        personalized["your_situation"] = {
            "borrowing": f"${amount:,.0f}",
            "will_pay_back": f"${total_paid:,.0f}",
            "interest_cost": f"${interest_paid:,.0f}",
            "monthly_payment": f"${(total_paid / (years * 12)):,.0f}"
        }
    
    return personalized

def get_all_explanations() -> Dict:
    """Get all available explanations."""
    return {
        "financial": FINANCIAL_EXPLANATIONS,
        "life": LIFE_EXPLANATIONS,
        "compound_interest": COMPOUND_INTEREST_EXAMPLES
    }
