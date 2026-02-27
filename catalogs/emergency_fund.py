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
    difficulty: Literal["easy", "medium", "hard"] = "medium"
    months: int = 12
    monthly_savings_goal: float = 0
    starting_balance: float = 0
    potential_events: List[Dict[str, Any]] = Field(default_factory=list)


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


EMERGENCY_EVENTS: Dict[str, Dict[str, Any]] = {
    "car_transmission": {
        "event_name": "Transmission Failure",
        "description": "Your car's transmission fails and needs urgent repair.",
        "min_cost": 1000,
        "max_cost": 3000,
        "event_type": "car_repair"
    },
    "medical_emergency": {
        "event_name": "Emergency Room Visit",
        "description": "Unexpected ER visit and treatment required.",
        "min_cost": 3000,
        "max_cost": 10000,
        "event_type": "medical"
    },
    "apartment_flood": {
        "event_name": "Apartment Flood",
        "description": "Water damage to furniture and electronics.",
        "min_cost": 1500,
        "max_cost": 3000,
        "event_type": "home_repair"
    },
    "laptop_dies": {
        "event_name": "Laptop Dies",
        "description": "You need a replacement laptop for work/school.",
        "min_cost": 600,
        "max_cost": 1200,
        "event_type": "travel"
    },
    "job_loss": {
        "event_name": "Unexpected Job Loss",
        "description": "Income stops while you search for a new job.",
        "min_cost": 2000,
        "max_cost": 5000,
        "event_type": "job_loss"
    },
    "dental_emergency": {
        "event_name": "Emergency Dental Surgery",
        "description": "Urgent dental procedure required.",
        "min_cost": 800,
        "max_cost": 2000,
        "event_type": "dental"
    },
    "pet_emergency": {
        "event_name": "Pet Emergency",
        "description": "Emergency vet visit and surgery.",
        "min_cost": 2000,
        "max_cost": 5000,
        "event_type": "pet"
    },
    "home_repair": {
        "event_name": "Home Repair",
        "description": "Unexpected home repair expense.",
        "min_cost": 2000,
        "max_cost": 5000,
        "event_type": "home_repair"
    },
    "medical_deductible": {
        "event_name": "Medical Deductible",
        "description": "You hit your insurance deductible.",
        "min_cost": 1500,
        "max_cost": 3000,
        "event_type": "medical"
    },
    "travel_emergency": {
        "event_name": "Family Travel Emergency",
        "description": "Last-minute travel for a family emergency.",
        "min_cost": 400,
        "max_cost": 1000,
        "event_type": "travel"
    },
}


def create_emergency_fund_challenge(
    difficulty: Literal["easy", "medium", "hard"],
    monthly_savings_goal: float,
    months: int = 12,
    starting_balance: float = 0
) -> EmergencyFundChallenge:
    """Create an emergency fund building challenge."""
    if difficulty == "easy":
        event_ids = ["laptop_dies", "car_transmission"]
    elif difficulty == "medium":
        event_ids = ["laptop_dies", "car_transmission", "dental_emergency"]
    else:
        event_ids = list(EMERGENCY_EVENTS.keys())

    potential_events = [EMERGENCY_EVENTS[eid] for eid in event_ids]
    return EmergencyFundChallenge(
        challenge_id=f"challenge_{difficulty}_{months}",
        difficulty=difficulty,
        months=months,
        monthly_savings_goal=monthly_savings_goal,
        starting_balance=starting_balance,
        potential_events=potential_events,
    )


def simulate_emergency_fund_building(
    monthly_savings: float,
    starting_balance: float = 0,
    months: int = 12,
    difficulty: Literal["easy", "medium", "hard"] = "medium",
) -> Dict[str, Any]:
    """Simulate building emergency fund over time."""
    balance = starting_balance
    monthly_breakdown = []

    if difficulty == "easy":
        event_months = [6]
        event_ids = ["laptop_dies", "travel_emergency"]
    elif difficulty == "medium":
        event_months = [4, 9]
        event_ids = ["laptop_dies", "dental_emergency", "car_transmission"]
    else:
        event_months = [2, 4, 6, 8, 10]
        event_ids = list(EMERGENCY_EVENTS.keys())

    event_months = [m for m in event_months if m <= months]

    total_emergencies = 0
    for month in range(1, months + 1):
        balance += monthly_savings
        event_cost = 0

        if month in event_months:
            event = EMERGENCY_EVENTS[event_ids[total_emergencies % len(event_ids)]]
            event_cost = (event["min_cost"] + event["max_cost"]) / 2
            balance -= event_cost
            total_emergencies += 1

        monthly_breakdown.append({
            "month": month,
            "savings": monthly_savings,
            "balance": balance,
            "event_cost": event_cost,
        })

    return {
        "total_saved": monthly_savings * months,
        "final_balance": balance,
        "total_emergencies": total_emergencies,
        "monthly_breakdown": monthly_breakdown,
    }


def get_emergency_event(event_id: str) -> Optional[Dict[str, Any]]:
    """Get a specific emergency event."""
    return EMERGENCY_EVENTS.get(event_id)


def get_all_emergency_events() -> List[Dict[str, Any]]:
    """Get all emergency events."""
    return list(EMERGENCY_EVENTS.values())


def get_emergency_by_type(event_type: str) -> List[Dict[str, Any]]:
    """Get emergency events by type."""
    return [e for e in EMERGENCY_EVENTS.values() if e.get("event_type") == event_type]


def calculate_emergency_fund_target(monthly_expenses: float, months: int = 3) -> float:
    """Calculate recommended emergency fund target.
    
    Standard advice: 3-6 months of expenses.
    """
    return monthly_expenses * months


def get_emergency_fund_progress(
    current_savings: float,
    monthly_expenses: float,
    target_months: int = 3,
) -> Dict[str, Any]:
    """Get progress toward emergency fund goals."""
    target_amount = monthly_expenses * target_months
    progress_percent = (current_savings / target_amount) * 100 if target_amount else 0

    return {
        "current_savings": current_savings,
        "target_amount": target_amount,
        "progress_percent": progress_percent,
        "fully_funded": current_savings >= target_amount,
    }
