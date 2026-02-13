"""Salary negotiation system for Life Sprint.

Teaches students:
- How to research market rates
- When and how to negotiate
- Counteroffers and benefits negotiation
- Lifetime earnings impact of negotiation
- Common negotiation mistakes to avoid
"""

from typing import Dict, List, Optional, Literal
from pydantic import BaseModel, Field


class MarketData(BaseModel):
    """Market salary data for a position."""
    position: str
    location: str
    percentile_25: float
    percentile_50: float  # median
    percentile_75: float
    percentile_90: float
    typical_years_experience: int = 0


class NegotiationScenario(BaseModel):
    """A salary negotiation scenario."""
    scenario_id: str
    job_title: str
    company_name: str
    initial_offer: float
    market_median: float
    market_75th: float
    
    # Benefits that can be negotiated
    pto_days: int = 15
    signing_bonus: float = 0.0
    remote_days_per_week: int = 0
    professional_development_budget: float = 0.0
    
    # Context
    company_size: Literal["startup", "small", "medium", "large"]
    company_urgency: Literal["low", "medium", "high"]  # How badly they need you
    your_leverage: Literal["low", "medium", "high"]  # Based on skills, other offers
    
    # Risks
    risk_of_offer_withdrawal: float = 0.1  # 0-1 probability
    risk_of_lowball_counter: float = 0.05


class NegotiationStrategy(BaseModel):
    """Negotiation approach."""
    strategy_type: Literal["accept", "negotiate_salary", "negotiate_benefits", "negotiate_both", "decline"]
    
    # If negotiating salary
    requested_salary: Optional[float] = None
    justification: str = ""  # "market rate", "competing offer", "unique skills"
    
    # If negotiating benefits
    requested_pto: Optional[int] = None
    requested_signing_bonus: Optional[float] = None
    requested_remote_days: Optional[int] = None
    requested_dev_budget: Optional[float] = None
    
    # Communication style
    tone: Literal["aggressive", "assertive", "collaborative", "passive"] = "collaborative"


class NegotiationOutcome(BaseModel):
    """Result of negotiation."""
    success: bool
    final_salary: float
    final_pto: int
    final_signing_bonus: float
    final_remote_days: int
    final_dev_budget: float
    
    # Impact
    immediate_gain: float  # Salary increase vs initial offer
    lifetime_earnings_gain: float  # Over 40-year career with 3% annual raises
    
    # Feedback
    employer_response: str
    negotiation_score: int = 0  # 0-100
    lessons_learned: List[str] = Field(default_factory=list)


class NegotiationTip(BaseModel):
    """Educational tips for negotiation."""
    tip_id: str
    category: Literal["research", "timing", "communication", "strategy", "mistake"]
    title: str
    description: str
    example: str
    impact_level: Literal["low", "medium", "high", "critical"]


# Market data for common entry-level and mid-level positions
MARKET_DATA: Dict[str, MarketData] = {
    "software_engineer_entry": MarketData(
        position="Software Engineer (Entry-Level)",
        location="NYC Metro Area",
        percentile_25=85000,
        percentile_50=95000,
        percentile_75=110000,
        percentile_90=125000,
        typical_years_experience=0
    ),
    "software_engineer_mid": MarketData(
        position="Software Engineer (Mid-Level)",
        location="NYC Metro Area",
        percentile_25=110000,
        percentile_50=130000,
        percentile_75=155000,
        percentile_90=180000,
        typical_years_experience=3
    ),
    "data_analyst_entry": MarketData(
        position="Data Analyst (Entry-Level)",
        location="NYC Metro Area",
        percentile_25=70000,
        percentile_50=80000,
        percentile_75=92000,
        percentile_90=105000,
        typical_years_experience=0
    ),
    "marketing_coordinator": MarketData(
        position="Marketing Coordinator",
        location="NYC Metro Area",
        percentile_25=52000,
        percentile_50=62000,
        percentile_75=72000,
        percentile_90=82000,
        typical_years_experience=1
    ),
    "financial_analyst_entry": MarketData(
        position="Financial Analyst (Entry-Level)",
        location="NYC Metro Area",
        percentile_25=70000,
        percentile_50=82000,
        percentile_75=95000,
        percentile_90=108000,
        typical_years_experience=0
    ),
    "product_manager_entry": MarketData(
        position="Product Manager (Entry-Level)",
        location="NYC Metro Area",
        percentile_25=95000,
        percentile_50=115000,
        percentile_75=135000,
        percentile_90=155000,
        typical_years_experience=2
    ),
}


# Negotiation educational tips
NEGOTIATION_TIPS: Dict[str, NegotiationTip] = {
    "always_negotiate": NegotiationTip(
        tip_id="always_negotiate",
        category="strategy",
        title="Always Negotiate - Even Small Gains Matter",
        description="84% of employers expect candidates to negotiate, and 85% of candidates who negotiate get something. Even a small increase compounds over your career.",
        example="Getting $5,000 more on a $70,000 offer = $7,143 extra this year. Over 40 years with 3% raises: $336,000 more lifetime earnings!",
        impact_level="critical"
    ),
    "research_first": NegotiationTip(
        tip_id="research_first",
        category="research",
        title="Know Your Worth - Research Market Rates",
        description="Use sites like Glassdoor, Levels.fyi, Payscale. Know the 50th and 75th percentile for your role and location.",
        example="If market median is $75k and you're offered $65k, you have data to justify asking for $72-75k.",
        impact_level="critical"
    ),
    "wait_for_offer": NegotiationTip(
        tip_id="wait_for_offer",
        category="timing",
        title="Never Give Salary Expectations First",
        description="Whoever names a number first loses negotiating power. Let them make the first offer, then negotiate up.",
        example="If they ask 'What are your salary expectations?' say: 'I'd like to learn more about the role first. What's the range you have budgeted?'",
        impact_level="high"
    ),
    "competing_offers": NegotiationTip(
        tip_id="competing_offers",
        category="strategy",
        title="Competing Offers Are Powerful Leverage",
        description="Having another offer (or credibly interviewing elsewhere) gives you significant leverage. Employers don't want to lose you to a competitor.",
        example="'I'm excited about this role, but I have another offer at $80k. Can you match or exceed that?' This often works.",
        impact_level="high"
    ),
    "negotiate_benefits": NegotiationTip(
        tip_id="negotiate_benefits",
        category="strategy",
        title="If Salary Is Fixed, Negotiate Benefits",
        description="If they say salary is non-negotiable, ask for signing bonus, extra PTO, remote work, professional development budget, earlier review.",
        example="'I understand the salary is fixed. Would you consider a $5,000 signing bonus and an extra week of PTO?'",
        impact_level="medium"
    ),
    "collaborative_tone": NegotiationTip(
        tip_id="collaborative_tone",
        category="communication",
        title="Use Collaborative Language, Not Demands",
        description="Frame negotiation as problem-solving together, not adversarial. Say 'Can we find a way to...' not 'I demand...'",
        example="Good: 'I'm thrilled about joining. Can we explore whether $75k is feasible based on market rates?' Bad: 'I won't accept less than $75k.'",
        impact_level="high"
    ),
    "justify_with_data": NegotiationTip(
        tip_id="justify_with_data",
        category="communication",
        title="Justify Your Ask With Data, Not Feelings",
        description="Base your counteroffer on market research, your skills, or competing offers - not personal needs or feelings.",
        example="Good: 'Based on Glassdoor data for this role, the market rate is $75k.' Bad: 'I need $75k because I have student loans.'",
        impact_level="high"
    ),
    "dont_accept_immediately": NegotiationTip(
        tip_id="dont_accept_immediately",
        category="timing",
        title="Never Accept The First Offer Immediately",
        description="Even if it's great, ask for 24-48 hours to review. This shows you're thoughtful and opens the door to negotiate.",
        example="'Thank you! This is exciting. I'd like to review the full offer and get back to you tomorrow. Is that okay?'",
        impact_level="medium"
    ),
    "know_your_walkaway": NegotiationTip(
        tip_id="know_your_walkaway",
        category="strategy",
        title="Know Your Minimum Acceptable Offer",
        description="Before negotiating, decide your walkaway point. If they can't meet it, be prepared to decline respectfully.",
        example="If you need minimum $65k to cover expenses, don't accept $60k hoping it gets better. Know your number.",
        impact_level="medium"
    ),
    "practice_beforehand": NegotiationTip(
        tip_id="practice_beforehand",
        category="communication",
        title="Practice Your Negotiation Script",
        description="Role-play with a friend. Practice saying your counteroffer out loud so you're confident in the real conversation.",
        example="Script: 'I'm excited about this role. Based on my research and skills, I was hoping for $75k. Is there flexibility?'",
        impact_level="medium"
    ),
    "gender_gap_awareness": NegotiationTip(
        tip_id="gender_gap_awareness",
        category="mistake",
        title="Women Negotiate Less - Don't Fall Into This Trap",
        description="Studies show women negotiate less often than men, contributing to the wage gap. Always negotiate regardless of gender.",
        example="Women who negotiate their first salary increase lifetime earnings by over $1 million compared to those who don't.",
        impact_level="critical"
    ),
    "avoid_ultimatums": NegotiationTip(
        tip_id="avoid_ultimatums",
        category="mistake",
        title="Avoid Ultimatums Unless You're Willing to Walk",
        description="Don't say 'I need $X or I walk' unless you truly mean it. Ultimatums can backfire and burn bridges.",
        example="Bad: 'It's $80k or I'm out.' Better: 'I'm looking for something closer to $80k. Is there any flexibility?'",
        impact_level="high"
    ),
}


def calculate_lifetime_earnings_impact(
    base_salary: float,
    negotiated_salary: float,
    years: int = 40,
    annual_raise_percent: float = 3.0
) -> Dict[str, float]:
    """Calculate the lifetime earnings difference from negotiating.
    
    Args:
        base_salary: Initial offer without negotiation
        negotiated_salary: Salary after negotiation
        years: Career length (default 40 years)
        annual_raise_percent: Average annual raise (default 3%)
    
    Returns:
        Dictionary with immediate gain, lifetime gain, and details
    """
    immediate_gain = negotiated_salary - base_salary
    
    # Calculate total earnings over career with compound raises
    base_total = 0.0
    negotiated_total = 0.0
    current_base = base_salary
    current_negotiated = negotiated_salary
    
    for year in range(years):
        base_total += current_base
        negotiated_total += current_negotiated
        current_base *= (1 + annual_raise_percent / 100)
        current_negotiated *= (1 + annual_raise_percent / 100)
    
    lifetime_gain = negotiated_total - base_total
    
    return {
        "immediate_gain": immediate_gain,
        "lifetime_base_earnings": base_total,
        "lifetime_negotiated_earnings": negotiated_total,
        "lifetime_gain": lifetime_gain,
        "gain_multiplier": lifetime_gain / immediate_gain if immediate_gain > 0 else 0
    }


def evaluate_negotiation(
    scenario: NegotiationScenario,
    strategy: NegotiationStrategy,
    player_communication_skills: int = 50,
    player_confidence: int = 50
) -> NegotiationOutcome:
    """Simulate a salary negotiation based on scenario and strategy.
    
    Returns realistic outcome with feedback.
    """
    
    # Base success probability
    success_chance = 0.7  # 70% of negotiations succeed to some degree
    
    # Adjust based on strategy
    if strategy.strategy_type == "accept":
        # Accepting immediately - no negotiation
        lifetime_impact = calculate_lifetime_earnings_impact(
            scenario.initial_offer,
            scenario.initial_offer
        )
        return NegotiationOutcome(
            success=True,
            final_salary=scenario.initial_offer,
            final_pto=scenario.pto_days,
            final_signing_bonus=scenario.signing_bonus,
            final_remote_days=scenario.remote_days_per_week,
            final_dev_budget=scenario.professional_development_budget,
            immediate_gain=0.0,
            lifetime_earnings_gain=0.0,
            employer_response="Thank you for accepting! We're excited to have you join the team.",
            negotiation_score=0,
            lessons_learned=[
                "You accepted without negotiating. 84% of employers expect negotiation.",
                f"You could have potentially earned ${scenario.market_median - scenario.initial_offer:,.0f} more.",
                "Even a small increase compounds significantly over your career."
            ]
        )
    
    # Determine if request is reasonable
    if strategy.requested_salary:
        salary_request = strategy.requested_salary
        if salary_request > scenario.market_75th * 1.1:
            success_chance *= 0.3  # Very aggressive ask
        elif salary_request > scenario.market_median:
            success_chance *= 0.8  # Reasonable high ask
        elif salary_request < scenario.initial_offer:
            success_chance = 0.0  # Negotiating down? No.
    else:
        salary_request = scenario.initial_offer
    
    # Adjust for leverage
    leverage_multipliers = {
        "low": 0.6,
        "medium": 1.0,
        "high": 1.4
    }
    success_chance *= leverage_multipliers[scenario.your_leverage]
    
    # Adjust for company urgency
    urgency_multipliers = {
        "low": 0.7,
        "medium": 1.0,
        "high": 1.3
    }
    success_chance *= urgency_multipliers[scenario.company_urgency]
    
    # Adjust for player skills
    skill_modifier = (player_communication_skills + player_confidence) / 100
    success_chance *= skill_modifier
    
    # Adjust for tone
    tone_multipliers = {
        "aggressive": 0.5,  # Risky
        "assertive": 1.1,   # Good
        "collaborative": 1.2,  # Best
        "passive": 0.7      # Weak
    }
    success_chance *= tone_multipliers[strategy.tone]
    
    # Cap success chance
    success_chance = min(success_chance, 0.95)
    success_chance = max(success_chance, 0.05)
    
    # Simulate outcome (simplified - in game would use random)
    negotiation_succeeded = success_chance > 0.5
    
    if negotiation_succeeded:
        # Calculate final offer (meet them somewhere in between)
        gap = salary_request - scenario.initial_offer
        final_salary = scenario.initial_offer + (gap * success_chance)
        
        # Round to nearest $1000
        final_salary = round(final_salary / 1000) * 1000
        
        # Benefits negotiation
        final_pto = strategy.requested_pto if strategy.requested_pto else scenario.pto_days
        final_signing = strategy.requested_signing_bonus if strategy.requested_signing_bonus else scenario.signing_bonus
        final_remote = strategy.requested_remote_days if strategy.requested_remote_days else scenario.remote_days_per_week
        final_dev = strategy.requested_dev_budget if strategy.requested_dev_budget else scenario.professional_development_budget
        
        lifetime_impact = calculate_lifetime_earnings_impact(
            scenario.initial_offer,
            final_salary
        )
        
        # Determine response
        if final_salary >= scenario.market_median:
            response = f"We appreciate your research and professionalism. We can offer ${final_salary:,.0f}. Welcome to the team!"
        else:
            response = f"We can meet you at ${final_salary:,.0f}. This is our best offer, and we hope you'll accept."
        
        score = int(success_chance * 100)
        
        lessons = []
        if final_salary < scenario.market_median:
            lessons.append(f"You could have aimed higher. Market median is ${scenario.market_median:,.0f}.")
        if strategy.tone == "collaborative":
            lessons.append("Great job using collaborative language! This builds trust with your new employer.")
        if lifetime_impact["immediate_gain"] > 5000:
            lessons.append(f"Excellent! Negotiating gained you ${lifetime_impact['lifetime_gain']:,.0f} over your career!")
        
        return NegotiationOutcome(
            success=True,
            final_salary=final_salary,
            final_pto=final_pto,
            final_signing_bonus=final_signing,
            final_remote_days=final_remote,
            final_dev_budget=final_dev,
            immediate_gain=lifetime_impact["immediate_gain"],
            lifetime_earnings_gain=lifetime_impact["lifetime_gain"],
            employer_response=response,
            negotiation_score=score,
            lessons_learned=lessons
        )
    
    else:
        # Negotiation failed
        # Could result in: lowered offer, withdrawn offer, or just rejection of counteroffer
        
        import random
        random.seed(int(success_chance * 100))  # Deterministic for testing
        
        if random.random() < scenario.risk_of_offer_withdrawal:
            # Offer withdrawn (rare but happens)
            return NegotiationOutcome(
                success=False,
                final_salary=0.0,
                final_pto=0,
                final_signing_bonus=0.0,
                final_remote_days=0,
                final_dev_budget=0.0,
                immediate_gain=-scenario.initial_offer,
                lifetime_earnings_gain=-calculate_lifetime_earnings_impact(scenario.initial_offer, scenario.initial_offer)["lifetime_base_earnings"],
                employer_response="We've decided to move forward with another candidate. Best of luck in your search.",
                negotiation_score=0,
                lessons_learned=[
                    "Your negotiation approach was too aggressive and the offer was withdrawn.",
                    "Lesson: Know when to be assertive vs aggressive. Ultimatums can backfire.",
                    "Always be prepared to walk away, but don't make threats you don't mean."
                ]
            )
        else:
            # They hold firm at original offer
            return NegotiationOutcome(
                success=False,
                final_salary=scenario.initial_offer,
                final_pto=scenario.pto_days,
                final_signing_bonus=scenario.signing_bonus,
                final_remote_days=scenario.remote_days_per_week,
                final_dev_budget=scenario.professional_development_budget,
                immediate_gain=0.0,
                lifetime_earnings_gain=0.0,
                employer_response=f"We understand your position, but ${scenario.initial_offer:,.0f} is our best offer. We hope you'll still consider joining us.",
                negotiation_score=30,
                lessons_learned=[
                    "They held firm. This happens sometimes - not every negotiation succeeds.",
                    "You can still accept the original offer or decline respectfully.",
                    f"Consider: Is ${scenario.initial_offer:,.0f} fair? Market median is ${scenario.market_median:,.0f}."
                ]
            )


def get_negotiation_tip(tip_id: str) -> Optional[NegotiationTip]:
    """Get a specific negotiation tip."""
    return NEGOTIATION_TIPS.get(tip_id)


def get_tips_by_category(category: str) -> List[NegotiationTip]:
    """Get all tips for a category."""
    return [tip for tip in NEGOTIATION_TIPS.values() if tip.category == category]


def get_market_data(position_key: str) -> Optional[MarketData]:
    """Get market salary data for a position."""
    return MARKET_DATA.get(position_key)
