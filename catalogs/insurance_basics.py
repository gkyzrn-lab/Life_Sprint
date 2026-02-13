"""Insurance education module - teaches insurance basics and decision-making."""

from typing import Dict, List, Optional, Literal
from pydantic import BaseModel, Field


class InsuranceType(BaseModel):
    """An insurance product type."""
    type_id: str
    type_name: str
    category: Literal["health", "property", "liability", "life", "other"]
    
    description: str
    why_needed: str
    what_it_covers: List[str]
    what_it_doesnt_cover: List[str]


class InsuranceScenario(BaseModel):
    """A real-world insurance scenario."""
    scenario_id: str
    scenario_name: str
    
    # The event
    event_description: str
    cost_without_insurance: float
    
    # Insurance options
    no_insurance_outcome: str
    with_insurance_outcome: str
    
    # Financial impact
    cost_with_insurance: float  # premiums + deductible
    savings_with_insurance: float  # cost_without_insurance - cost_with_insurance
    
    lesson: str


class InsuranceTermFact(BaseModel):
    """Insurance terminology with explanation."""
    term_id: str
    term: str
    definition: str
    example: str


class InsuranceMythFact(BaseModel):
    """Insurance myths vs facts."""
    myth_id: str
    myth: str
    fact: str
    financial_impact: float  # How much you might lose believing the myth


# Insurance types
INSURANCE_TYPES: Dict[str, InsuranceType] = {
    # HEALTH INSURANCE
    "health_insurance": InsuranceType(
        type_id="health_insurance",
        type_name="Health Insurance",
        category="health",
        description="Covers medical expenses including doctor visits, hospital, medications",
        why_needed="A single emergency room visit can cost $10,000+. One surgery can cost $50,000+. Without insurance, medical debt is the #1 cause of bankruptcy.",
        what_it_covers=[
            "Doctor office visits",
            "Preventive care (check-ups, vaccines)",
            "Hospital stays",
            "Emergency room",
            "Prescription medications",
            "Lab tests and imaging",
            "Mental health services",
        ],
        what_it_doesnt_cover=[
            "Everything below your deductible",
            "Cosmetic procedures",
            "Out-of-network care (usually)",
            "Experimental treatments",
        ]
    ),
    
    # AUTO INSURANCE
    "auto_liability": InsuranceType(
        type_id="auto_liability",
        type_name="Auto Liability Insurance",
        category="liability",
        description="Pays for damages you cause to others in a car accident",
        why_needed="If you cause an accident that injures someone, you're legally responsible. Without insurance, they can sue you for hundreds of thousands. It's required by law.",
        what_it_covers=[
            "Medical bills of the other person",
            "Property damage to other cars/property",
            "Legal defense costs",
            "Settlement/lawsuit costs",
        ],
        what_it_doesnt_cover=[
            "Damage to your own car",
            "Your own medical bills",
            "Intentional damage",
        ]
    ),
    
    "auto_collision": InsuranceType(
        type_id="auto_collision",
        type_name="Auto Collision Insurance",
        category="property",
        description="Covers damage to your car from accidents",
        why_needed="A car accident repair can cost $5,000-$20,000+. Without collision coverage, you pay 100% out of pocket. If you have a loan, your lender requires it.",
        what_it_covers=[
            "Damage from car accidents",
            "Repair or replacement of your car",
            "Minus deductible (usually $500-$1,000)",
        ],
        what_it_doesnt_cover=[
            "Damage not from accident (wear/tear, mechanical failure)",
        ]
    ),
    
    "auto_comprehensive": InsuranceType(
        type_id="auto_comprehensive",
        type_name="Auto Comprehensive Insurance",
        category="property",
        description="Covers damage to your car from non-accident events",
        why_needed="Theft, vandalism, weather, animals - these cause $2,000-$10,000+ in damage. Comprehensive covers these situations.",
        what_it_covers=[
            "Theft",
            "Vandalism",
            "Weather (hail, flood, tornado)",
            "Animal collisions",
            "Glass damage",
            "Fire",
        ],
        what_it_doesnt_cover=[
            "Accident damage (use collision)",
            "Mechanical breakdown",
            "Maintenance",
        ]
    ),
    
    # RENTERS INSURANCE
    "renters_insurance": InsuranceType(
        type_id="renters_insurance",
        type_name="Renters Insurance",
        category="property",
        description="Covers your belongings in an apartment/rental home",
        why_needed="Apartment fire, theft, or water damage can destroy everything you own ($5,000-$15,000+). Landlord's insurance only covers the building, not your stuff.",
        what_it_covers=[
            "Your furniture and belongings",
            "Laptop, clothes, phone",
            "Coverage away from home too",
            "Personal liability (someone injured in your apartment)",
            "Additional living expenses if you can't stay in apartment",
        ],
        what_it_doesnt_cover=[
            "The building itself (landlord's responsibility)",
            "Flood damage (separate flood insurance)",
            "Expensive jewelry/valuables (unless separately insured)",
        ]
    ),
    
    # LIFE INSURANCE
    "term_life": InsuranceType(
        type_id="term_life",
        type_name="Term Life Insurance",
        category="life",
        description="Pays a death benefit if you die during the term (10, 20, 30 years)",
        why_needed="If you have dependents, a mortgage, or debts, your death leaves them with financial burden. Term life is affordable ($20-50/month for young people) and covers the gap.",
        what_it_covers=[
            "Death benefit to beneficiary",
            "Coverage during active term",
            "Usually convertible to permanent at end of term",
        ],
        what_it_doesnt_cover=[
            "Pre-existing conditions (usually)",
            "Suicide (first 2 years)",
            "High-risk activities",
            "After the term ends",
        ]
    ),
    
    "whole_life": InsuranceType(
        type_id="whole_life",
        type_name="Whole Life Insurance",
        category="life",
        description="Lifetime coverage with cash value component",
        why_needed="More expensive ($200-400+/month) but lifetime coverage and builds cash value you can borrow against. For older people or permanent need.",
        what_it_covers=[
            "Lifetime death benefit",
            "Cash value growth (tax-deferred)",
            "Can borrow against cash value",
            "Level premiums for life",
        ],
        what_it_doesnt_cover=[
            "Usually not good for young people (too expensive)",
        ]
    ),
    
    # DISABILITY INSURANCE
    "short_term_disability": InsuranceType(
        type_id="short_term_disability",
        type_name="Short-Term Disability Insurance",
        category="other",
        description="Replaces 60-70% of income if you can't work (typically 3-6 months)",
        why_needed="If you get injured or sick, you stop earning money. One accident can cause 6+ months without income. Disability protects against this.",
        what_it_covers=[
            "60-70% of salary while out of work",
            "Usually covers 3-6 months",
            "Starts after 7-14 day waiting period",
        ],
        what_it_doesnt_cover=[
            "Longer than benefit period (use long-term disability)",
        ]
    ),
    
    "long_term_disability": InsuranceType(
        type_id="long_term_disability",
        type_name="Long-Term Disability Insurance",
        category="other",
        description="Replaces income if you can't work long-term (2+ years or until retirement)",
        why_needed="Serious injury/illness can take years to recover. Long-term disability protects against becoming a burden on family or running out of savings.",
        what_it_covers=[
            "60-70% of salary",
            "From end of short-term (usually month 6) until retirement",
            "Can last until age 65+",
        ],
        what_it_doesnt_cover=[
            "Own-occupation definition (varies by policy)",
        ]
    ),
}


# Insurance scenarios
INSURANCE_SCENARIOS: Dict[str, InsuranceScenario] = {
    "scenario_car_accident": InsuranceScenario(
        scenario_id="scenario_car_accident",
        scenario_name="Car Accident with Injuries",
        event_description="You cause an accident that injures 3 people and damages 2 cars",
        cost_without_insurance=450000,  # Medical + lawsuits
        no_insurance_outcome="You're sued for $450,000+. Wages garnished for years. Credit ruined. Potentially jail time for driving uninsured.",
        with_insurance_outcome="Insurance pays up to your policy limits. You cover deductible ($500-1,000). Rest handled by insurer.",
        cost_with_insurance=1000,  # Deductible + annual premiums
        savings_with_insurance=449000,
        lesson="Auto liability is legally required and financially essential. One accident can bankrupt you without it."
    ),
    
    "scenario_apartment_fire": InsuranceScenario(
        scenario_id="scenario_apartment_fire",
        scenario_name="Apartment Fire",
        event_description="Fire in apartment building destroys all your belongings",
        cost_without_insurance=12000,  # Furniture, electronics, clothes, etc
        no_insurance_outcome="You lose everything. Have to replace all furniture, clothes, phone, laptop. Build back from nothing.",
        with_insurance_outcome="Insurance pays $12,000 (minus $250 deductible). You replace items and move on.",
        cost_with_insurance=250,  # Deductible (premiums ~$15/month already paid)
        savings_with_insurance=11750,
        lesson="Renters insurance is cheap (~$15/month) but saves thousands if disaster strikes. Most young people skip it and regret it."
    ),
    
    "scenario_heart_attack": InsuranceScenario(
        scenario_id="scenario_heart_attack",
        scenario_name="Heart Attack and Hospital Stay",
        event_description="You have a heart attack requiring 3-day hospital stay and surgery",
        cost_without_insurance=75000,  # Hospital, doctor, surgery
        no_insurance_outcome="Medical bill ruins you. Go into debt, default on payment plan, collections, bankruptcy.",
        with_insurance_outcome="Insurance negotiates the price. You pay copay + deductible (~$2,000). Insurance covers rest.",
        cost_with_insurance=2000,  # Deductible + coinsurance (premiums are ongoing but with insurance)
        savings_with_insurance=73000,
        lesson="Health insurance is the difference between financial stability and bankruptcy. One major health event without insurance is catastrophic."
    ),
    
    "scenario_job_loss": InsuranceScenario(
        scenario_id="scenario_job_loss",
        scenario_name="Job Loss (Disability due to injury)",
        event_description="You have a severe injury that prevents work for 8 months (recovery time)",
        cost_without_insurance=32000,  # 8 months of lost income at $4,000/month
        no_insurance_outcome="Can't work, can't pay rent/mortgage. Deplete savings, go into credit card debt, fall behind on bills, eviction risk.",
        with_insurance_outcome="Disability insurance pays 60% of income ($2,400/month). Cover most expenses and keep life stable.",
        cost_with_insurance=5000,  # 8 months at reduced income + $200/month premium
        savings_with_insurance=27000,
        lesson="Disability insurance is undervalued. Most young people think 'it won't happen to me' but injuries are more common than death before retirement."
    ),
    
    "scenario_life_insurance": InsuranceScenario(
        scenario_id="scenario_life_insurance",
        scenario_name="Death with Dependents",
        event_description="You die suddenly, leaving a spouse and two kids",
        cost_without_insurance=500000,  # 10 years of income replacement + college fund
        no_insurance_outcome="Family loses income earner. Spouse struggles to afford childcare, rent, and college. Kids may skip college due to cost.",
        with_insurance_outcome="$500,000 life insurance benefit provides financial security. Family can stay in home, kids go to college.",
        cost_with_insurance=6000,  # $50/month for 10 years
        savings_with_insurance=494000,
        lesson="Life insurance is cheap when young. $50/month for 30-year term. If you have dependents, it's essential."
    ),
}


# Insurance terms
INSURANCE_TERMS: Dict[str, InsuranceTermFact] = {
    "deductible": InsuranceTermFact(
        term_id="deductible",
        term="Deductible",
        definition="Amount you pay out-of-pocket before insurance starts paying",
        example="$1,000 car collision deductible means you pay first $1,000 of damages, insurance pays the rest"
    ),
    
    "premium": InsuranceTermFact(
        term_id="premium",
        term="Premium",
        definition="Monthly or annual payment you pay to have insurance coverage",
        example="$100/month car insurance premium - if you don't pay, you lose coverage"
    ),
    
    "coverage_limit": InsuranceTermFact(
        term_id="coverage_limit",
        term="Coverage Limit (Policy Limit)",
        definition="Maximum amount insurance will pay for a claim",
        example="$100,000 auto liability limit means insurance pays maximum $100,000 for damages you cause"
    ),
    
    "copay": InsuranceTermFact(
        term_id="copay",
        term="Copay",
        definition="Fixed amount you pay for a specific service (health insurance)",
        example="$20 copay for doctor visit - you pay $20, insurance pays rest"
    ),
    
    "coinsurance": InsuranceTermFact(
        term_id="coinsurance",
        term="Coinsurance",
        definition="Percentage of costs you pay after meeting deductible",
        example="80/20 coinsurance means insurance pays 80%, you pay 20% after deductible"
    ),
    
    "out_of_pocket_max": InsuranceTermFact(
        term_id="out_of_pocket_max",
        term="Out-of-Pocket Maximum",
        definition="Maximum you'll pay in deductibles, copays, and coinsurance in a year",
        example="$5,000 out-of-pocket max means once you pay $5,000 total, insurance covers 100% rest of year"
    ),
    
    "exclusion": InsuranceTermFact(
        term_id="exclusion",
        term="Exclusion",
        definition="Specific situation or item that insurance won't cover",
        example="Flood exclusion in auto insurance means damage from flood isn't covered"
    ),
    
    "beneficiary": InsuranceTermFact(
        term_id="beneficiary",
        term="Beneficiary",
        definition="Person who receives the insurance payout when you die",
        example="Life insurance beneficiary gets the death benefit if you pass away"
    ),
    
    "grace_period": InsuranceTermFact(
        term_id="grace_period",
        term="Grace Period",
        definition="Time period after premium due date before coverage is canceled",
        example="30-day grace period means if premium is late, you still have coverage for 30 days"
    ),
}


# Insurance myths
INSURANCE_MYTHS: Dict[str, InsuranceMythFact] = {
    "myth_young_no_insurance": InsuranceMythFact(
        myth_id="myth_young_no_insurance",
        myth="I'm young and healthy, I don't need health insurance.",
        fact="One emergency room visit costs $3,000-10,000. One accident injury costs $30,000+. Medical debt is the #1 cause of bankruptcy. You need insurance.",
        financial_impact=50000
    ),
    
    "myth_car_accident_rare": InsuranceMythFact(
        myth_id="myth_car_accident_rare",
        myth="Car accidents are rare, I can skip collision insurance.",
        fact="1 in 366 drivers have a collision claim per year. Over 10 years, 3% chance. Uninsured claim means $8,000-15,000 out of pocket.",
        financial_impact=12000
    ),
    
    "myth_renters_landlord": InsuranceMythFact(
        myth_id="myth_renters_landlord",
        myth="My landlord's insurance covers my stuff.",
        fact="Landlord's insurance covers the building, not your belongings. Fire destroys your furniture, clothes, electronics ($10,000+). Landlord pays $0.",
        financial_impact=10000
    ),
    
    "myth_employer_life": InsuranceMythFact(
        myth_id="myth_employer_life",
        myth="My employer's life insurance is enough.",
        fact="Employer life insurance is usually 1-2x salary ($50,000-100,000). You need 10-15x salary if you have dependents or mortgage.",
        financial_impact=400000
    ),
    
    "myth_skipping_disability": InsuranceMythFact(
        myth_id="myth_skipping_disability",
        myth="Disability insurance is unnecessary, I won't get injured.",
        fact="1 in 4 workers will have a disability lasting 90+ days before retirement. If you can't work 6 months, you lose ~$24,000 in income.",
        financial_impact=24000
    ),
    
    "myth_insurance_waste": InsuranceMythFact(
        myth_id="myth_insurance_waste",
        myth="Insurance is a waste of money if you never use it.",
        fact="That's the point! Insurance protects against catastrophic loss. You don't 'use' car insurance to make money - you use it to avoid bankruptcy.",
        financial_impact=100000
    ),
}


# Insurance tips
INSURANCE_TIPS: Dict[str, str] = {
    "health_compare": "Compare health insurance plans on healthcare.gov. Cheap premium might mean high deductible. Calculate total cost (premium + deductible) for your situation.",
    
    "auto_bundling": "Bundle auto and renters/home insurance with same company. Usually saves 10-25% on both policies.",
    
    "health_preventive": "All health insurance covers preventive care 100% (no copay). Use it! Annual checkup, vaccines cost nothing, catch problems early.",
    
    "auto_discount": "Ask about auto insurance discounts: good driver (3+ years clean), bundling, good student (3.0+ GPA), defensive driving course, low mileage.",
    
    "life_term_young": "Buy term life insurance when young. $500,000 term for 30 years costs ~$50/month at 25, but $300/month at 45. Lock in rate now.",
    
    "renters_inventory": "Make list of your belongings with photos/videos for renters insurance claim. Easier to get full reimbursement if disaster strikes.",
    
    "disability_wait": "Longer waiting period = cheaper premium. If you have 6 months emergency fund, can do 90-day wait period and save on premiums.",
    
    "review_coverage": "Review insurance coverage annually. Income changes, family changes, assets change. Make sure coverage matches your life.",
}


def get_insurance_type(type_id: str) -> Optional[InsuranceType]:
    """Get insurance type details."""
    return INSURANCE_TYPES.get(type_id)


def get_all_insurance_types() -> List[InsuranceType]:
    """Get all insurance types."""
    return list(INSURANCE_TYPES.values())


def get_insurance_by_category(category: str) -> List[InsuranceType]:
    """Get insurance types by category."""
    return [i for i in INSURANCE_TYPES.values() if i.category == category]


def get_scenario(scenario_id: str) -> Optional[InsuranceScenario]:
    """Get insurance scenario."""
    return INSURANCE_SCENARIOS.get(scenario_id)


def get_all_scenarios() -> List[InsuranceScenario]:
    """Get all scenarios."""
    return list(INSURANCE_SCENARIOS.values())


def get_term(term_id: str) -> Optional[InsuranceTermFact]:
    """Get insurance term definition."""
    return INSURANCE_TERMS.get(term_id)


def get_all_terms() -> List[InsuranceTermFact]:
    """Get all insurance terms."""
    return list(INSURANCE_TERMS.values())


def get_myth(myth_id: str) -> Optional[InsuranceMythFact]:
    """Get insurance myth."""
    return INSURANCE_MYTHS.get(myth_id)


def get_all_myths() -> List[InsuranceMythFact]:
    """Get all insurance myths."""
    return list(INSURANCE_MYTHS.values())


def get_tip(tip_name: str) -> Optional[str]:
    """Get insurance tip."""
    return INSURANCE_TIPS.get(tip_name)


def get_all_tips() -> List[str]:
    """Get all insurance tips."""
    return list(INSURANCE_TIPS.values())
