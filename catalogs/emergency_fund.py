"""Emergency fund scenario system - teaches why emergency funds matter."""

from typing import Dict, List, Optional, Literal, Any
from pydantic import BaseModel, Field
import random


class EmergencyEvent(BaseModel):
    """An emergency event that requires money."""
    event_id: str
    event_type: Literal["medical", "car_repair", "job_loss", "home_repair", "dental", "travel", "pet"]
    
    # Event details
    name: str
    description: str
    typical_cost: float
    cost_range: tuple = (0, 0)  # (min, max)
    
    # Consequences
    urgency: Literal["immediate", "within_week", "within_month"]
    
    # Consequences without emergency fund
    consequence_if_no_fund: str
    debt_accrued: float  # Interest/fees if you can't pay
    
    # Learning
    educational_value: str
    prevention_tip: Optional[str] = None


class EmergencyScenario(BaseModel):
    """A scenario where player deals with emergencies."""
    scenario_id: str
    month: int  # Which month emergency occurs
    event: EmergencyEvent
    player_emergency_fund: float  # Player's emergency fund at time of event


class EmergencyFundChallenge(BaseModel):
    """A challenge to build emergency fund."""
    challenge_id: str
    
    # Parameters
    starting_balance: float
    starting_emergency_fund: float
    monthly_income: float
    monthly_expenses: float
    
    # Events that will occur
    events: List[EmergencyEvent] = Field(default_factory=list)
    event_schedule: List[int] = Field(default_factory=list)  # Months when events occur
    
    # Results
    final_balance: float = 0
    final_emergency_fund: float = 0
    total_debt_accrued: float = 0
    events_handled: int = 0
    events_caused_debt: int = 0


class EmergencyOutcome(BaseModel):
    """Outcome of handling an emergency."""
    event_name: str
    cost: float
    player_emergency_fund_before: float
    player_emergency_fund_after: float
    
    # What happened
    had_sufficient_funds: bool
    amount_short: float = 0  # If they couldn't cover
    
    # Consequences
    debt_created: float = 0  # If they had to borrow
    interest_paid: float = 0
    
    # Lesson
    lesson: str


# Emergency events database
EMERGENCY_EVENTS: Dict[str, EmergencyEvent] = {
    "car_transmission": EmergencyEvent(
        event_id="car_transmission",
        event_type="car_repair",
        name="Transmission Failure",
        description="Your car's transmission fails. It's dead on the highway. You need a new/rebuilt transmission.",
        typical_cost=1500,
        cost_range=(1000, 3000),
        urgency="immediate",
        consequence_if_no_fund="Take out car loan at 8% APR or put $1,500 on credit card at 22% APR. Can't use car until fixed.",
        debt_accrued=300,  # Interest per month until paid
        educational_value="$1,500 repair now vs. no emergency fund = $300+ in interest charges if you borrow.",
        prevention_tip="Keep car maintained. Regular oil changes ($30) prevent $1,500+ repairs."
    ),
    
    "medical_emergency": EmergencyEvent(
        event_id="medical_emergency",
        event_type="medical",
        name="Emergency Room Visit",
        description="You have sudden severe pain and need to go to the ER. Diagnosis: appendicitis. Surgery required.",
        typical_cost=5000,
        cost_range=(3000, 10000),
        urgency="immediate",
        consequence_if_no_fund="Medical debt sent to collections. Your credit score drops 100+ points. Bill collector calls start.",
        debt_accrued=200,  # Monthly interest and fees
        educational_value="Medical debt is the #1 cause of bankruptcy. If uninsured, ER + surgery = $5,000-$15,000.",
        prevention_tip="Get health insurance. Even basic plans cap out-of-pocket costs at $5,000-$7,000."
    ),
    
    "apartment_flood": EmergencyEvent(
        event_id="apartment_flood",
        event_type="home_repair",
        name="Apartment Flood (Neighbor's Leak)",
        description="Neighbor's apartment floods, water leaks into yours. Your furniture, electronics, and clothes are damaged.",
        typical_cost=2000,
        cost_range=(1500, 3000),
        urgency="immediate",
        consequence_if_no_fund="If you have renters insurance: $1,000-$2,000 (pay deductible). Without: YOU pay everything. Landlord won't help.",
        debt_accrued=100,  # If you have to replace furniture slowly
        educational_value="Renters insurance costs $15-30/month but covers $20,000-$30,000 in belongings. Worth it.",
        prevention_tip="Get renters insurance. Costs ~$20/month. Covers theft, fire, water damage, and liability."
    ),
    
    "laptop_dies": EmergencyEvent(
        event_id="laptop_dies",
        event_type="travel",
        name="Laptop Dies (For Work/School)",
        description="Your laptop stops working completely. You need it for work/school projects and remote work.",
        typical_cost=800,
        cost_range=(600, 1200),
        urgency="within_week",
        consequence_if_no_fund="Miss work deadlines. Miss school assignments. Credit card debt at 22% APR.",
        debt_accrued=15,  # Monthly interest
        educational_value="Technology emergencies happen. Budget laptops cost $600-800. Emergency fund prevents debt.",
        prevention_tip="Assume your devices will break. Allocate $50-100/month to tech replacement fund."
    ),
    
    "job_loss": EmergencyEvent(
        event_id="job_loss",
        event_type="job_loss",
        name="Unexpected Job Loss",
        description="You're laid off without warning. No severance. You need to cover living expenses while finding a new job.",
        typical_cost=3000,  # Monthly expenses
        cost_range=(2000, 5000),
        urgency="immediate",
        consequence_if_no_fund="Use credit cards. Rack up $5,000-10,000 in debt. Then scramble to pay it back with new job.",
        debt_accrued=400,  # Credit card interest
        educational_value="3-6 months emergency fund = months of security. Average job search: 3 months. Safety net is essential.",
        prevention_tip="Build 3-6 months of expenses. Saves you from $5,000+ in credit card debt during job transition."
    ),
    
    "dental_emergency": EmergencyEvent(
        event_id="dental_emergency",
        event_type="dental",
        name="Emergency Dental Surgery",
        description="Severe tooth infection. Needs root canal + crown. Extremely painful. Infection spreading.",
        typical_cost=1200,
        cost_range=(800, 2000),
        urgency="immediate",
        consequence_if_no_fund="Put on credit card. $1,200 at 22% APR = paying interest for 1+ year.",
        debt_accrued=22,  # Monthly interest
        educational_value="Dental work is expensive. If uninsured, budget $1,000-2,000/year for emergency dental.",
        prevention_tip="Dental insurance: ~$100-200/year. Covers emergencies up to 50%. ROI is huge if you have events."
    ),
    
    "pet_emergency": EmergencyEvent(
        event_id="pet_emergency",
        event_type="pet",
        name="Dog Emergency Surgery",
        description="Your dog gets hit by a car. Needs emergency surgery and hospitalization. Vet says $3,000-5,000.",
        typical_cost=3500,
        cost_range=(2000, 5000),
        urgency="immediate",
        consequence_if_no_fund="Can't afford surgery. Pet dies or suffers permanent disability. Massive guilt and regret.",
        debt_accrued=200,  # If you finance with credit card
        educational_value="Pet ownership has hidden costs. Vets don't negotiate like doctors. Pet insurance costs $30-50/month.",
        prevention_tip="Pet insurance or pet emergency fund. Saves you from devastating choice: debt or losing your pet."
    ),
    
    "home_repair_roof": EmergencyEvent(
        event_id="home_repair_roof",
        event_type="home_repair",
        name="Roof Leak (Water Damage)",
        description="Storm damages roof. Water leaks into attic and walls. Mold starting to grow. Needs immediate repair.",
        typical_cost=2500,
        cost_range=(2000, 5000),
        urgency="immediate",
        consequence_if_no_fund="Water damage worsens. Mold spreads. Repair costs escalate. Eventually $8,000+.",
        debt_accrued=150,  # Monthly interest if financed
        educational_value="Home repairs are expensive and unavoidable. ~1% of home value/year for maintenance.",
        prevention_tip="If you own a home: allocate 1% of home value annually for emergency repairs/maintenance."
    ),
    
    "medical_deductible": EmergencyEvent(
        event_id="medical_deductible",
        event_type="medical",
        name="Hospital Stay (Hit Deductible)",
        description="You get hospitalized for 3 days. Tests, medications, doctors. Insurance covers 80% after deductible.",
        typical_cost=2000,
        cost_range=(1500, 3000),
        urgency="immediate",
        consequence_if_no_fund="Medical debt. Collections agency. Credit score damage that lasts 7 years.",
        debt_accrued=100,
        educational_value="Insurance doesn't mean free care. Deductibles are typically $1,000-$5,000 per year.",
        prevention_tip="Budget your deductible as an emergency. If deductible is $3,000, treat it like mandatory emergency fund."
    ),
    
    "travel_emergency": EmergencyEvent(
        event_id="travel_emergency",
        event_type="travel",
        name="Flight Home for Family Emergency",
        description="Parent has heart attack. You need to fly home immediately. Last-minute flight is expensive.",
        typical_cost=600,
        cost_range=(400, 1000),
        urgency="immediate",
        consequence_if_no_fund="Can't afford flight. Miss seeing parent in hospital. Guilt lasts forever.",
        debt_accrued=0,  # Family usually helps, but emotional cost is high
        educational_value="Family emergencies happen. You can't predict them but can prepare financially.",
        prevention_tip="Everyone should have $500-1,000 accessible for family emergencies."
    ),
}


def create_emergency_fund_challenge(
    starting_balance: float,
    monthly_income: float,
    monthly_expenses: float,
    months: int = 12,
    difficulty: Literal["easy", "medium", "hard"] = "medium"
) -> EmergencyFundChallenge:
    """Create an emergency fund building challenge."""
    
    challenge = EmergencyFundChallenge(
        challenge_id=f"challenge_{starting_balance}_{difficulty}",
        starting_balance=starting_balance,
        starting_emergency_fund=0,
        monthly_income=monthly_income,
        monthly_expenses=monthly_expenses,
        events=[],
        event_schedule=[]
    )
    
    # Generate random events based on difficulty
    if difficulty == "easy":
        event_chances = {"month_3": 0.5, "month_6": 0.4, "month_12": 0.3}
        event_pool = ["laptop_dies", "car_transmission"]
    elif difficulty == "medium":
        event_chances = {"month_3": 0.6, "month_6": 0.6, "month_9": 0.5, "month_12": 0.6}
        event_pool = ["laptop_dies", "car_transmission", "dental_emergency", "apartment_flood"]
    else:  # hard
        event_chances = {"month_2": 0.8, "month_5": 0.7, "month_8": 0.7, "month_12": 0.8}
        event_pool = list(EMERGENCY_EVENTS.keys())
    
    for month_check, probability in event_chances.items():
        if random.random() < probability:
            month = int(month_check.split("_")[1])
            event_id = random.choice(event_pool)
            challenge.events.append(EMERGENCY_EVENTS[event_id])
            challenge.event_schedule.append(month)
    
    return challenge


def simulate_emergency_fund_building(
    starting_balance: float,
    monthly_income: float,
    monthly_expenses: float,
    emergency_fund_target: float,
    monthly_savings_rate: float = 0.20,  # 20% of income
    events: List[tuple] = None  # (month, cost)
) -> Dict:
    """Simulate building emergency fund over time.
    
    Returns month-by-month breakdown.
    """
    
    balance = starting_balance
    emergency_fund = 0
    total_debt = 0
    month_breakdown = []
    events_by_month = {month: cost for month, cost in (events or [])}
    
    for month in range(1, 13):
        # Income
        available = monthly_income - monthly_expenses
        
        # Allocate to emergency fund
        emergency_savings = available * monthly_savings_rate
        emergency_fund += emergency_savings
        balance += emergency_savings
        
        # Check for emergency event
        event_occurred = False
        event_name = None
        event_cost = 0
        
        if month in events_by_month:
            event_occurred = True
            event_cost = events_by_month[month]
            event_name = "Emergency Event"
            
            # Handle the emergency
            if emergency_fund >= event_cost:
                # Had enough saved
                emergency_fund -= event_cost
                balance -= event_cost
            else:
                # Had to go into debt
                amount_short = event_cost - emergency_fund
                total_debt += amount_short * 1.22  # Credit card interest
                emergency_fund = 0
                balance -= emergency_fund  # Use what was saved
        
        # Track month
        month_breakdown.append({
            "month": month,
            "income": monthly_income,
            "expenses": monthly_expenses,
            "savings": emergency_savings,
            "emergency_fund": emergency_fund,
            "total_balance": balance,
            "event_occurred": event_occurred,
            "event_cost": event_cost,
            "total_debt_accumulated": total_debt
        })
    
    return {
        "final_balance": balance,
        "final_emergency_fund": emergency_fund,
        "total_debt": total_debt,
        "met_target": emergency_fund >= emergency_fund_target,
        "months_breakdown": month_breakdown
    }


def get_emergency_event(event_id: str) -> Optional[EmergencyEvent]:
    """Get a specific emergency event."""
    return EMERGENCY_EVENTS.get(event_id)


def get_all_emergency_events() -> List[EmergencyEvent]:
    """Get all emergency events."""
    return list(EMERGENCY_EVENTS.values())


def get_emergency_by_type(event_type: str) -> List[EmergencyEvent]:
    """Get emergency events by type."""
    return [e for e in EMERGENCY_EVENTS.values() if e.event_type == event_type]


def calculate_emergency_fund_target(monthly_expenses: float, months: int = 3) -> float:
    """Calculate recommended emergency fund target.
    
    Standard advice: 3-6 months of expenses.
    """
    return monthly_expenses * months


def get_emergency_fund_progress(
    current_fund: float,
    monthly_expenses: float
) -> Dict[str, Any]:
    """Get progress toward emergency fund goals."""
    
    target_3m = monthly_expenses * 3
    target_6m = monthly_expenses * 6
    
    return {
        "current_fund": current_fund,
        "months_of_expenses_covered": round(current_fund / monthly_expenses, 1),
        "target_3_months": target_3m,
        "target_6_months": target_6m,
        "progress_to_3m_percent": round((current_fund / target_3m) * 100, 1),
        "progress_to_6m_percent": round((current_fund / target_6m) * 100, 1),
        "still_needed_for_3m": max(0, target_3m - current_fund),
        "still_needed_for_6m": max(0, target_6m - current_fund),
        "at_3_month_minimum": current_fund >= target_3m,
        "at_6_month_recommended": current_fund >= target_6m,
    }
