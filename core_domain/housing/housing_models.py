"""
Housing Market & Life Decisions Models

Tracks housing market conditions, rent vs buy decisions, mortgages,
roommate arrangements, and commute trade-offs.
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime


class HousingMarket(BaseModel):
    """Current housing market conditions and trends"""
    rent_inflation_rate: float = 0.05  # 5% annual rent increase post-graduation
    market_heat: Literal["cold", "normal", "hot"] = "normal"
    years_since_graduation: int = 0
    total_rent_paid: float = 0.0
    
    
class Mortgage(BaseModel):
    """Mortgage loan details for owned property"""
    property_id: str
    original_principal: float  # Original loan amount
    current_balance: float  # Remaining principal
    interest_rate: float  # Annual interest rate (e.g., 0.065 for 6.5%)
    monthly_payment: float  # Principal + interest
    term_years: int  # Original loan term (30, 15, etc.)
    months_remaining: int
    total_interest_paid: float = 0.0
    start_date: str = ""
    
    
class RoommateArrangement(BaseModel):
    """Roommate cost-sharing and privacy impact"""
    num_roommates: int = 0  # 0 = living alone
    rent_split_percent: float = 1.0  # Your share (0.5 = 50% if 1 roommate)
    privacy_level: int = 100  # 100 = alone, decreases with roommates
    conflict_level: int = 0  # 0-100, random events increase this
    monthly_savings: float = 0.0  # How much you save vs living alone


class HousingOption(BaseModel):
    """A specific housing option (apartment, house, etc.)"""
    option_id: str
    name: str
    location: Literal["nyc_manhattan", "nyc_brooklyn", "nyc_queens", "nj_jersey_city", "nj_newark", "nj_hoboken"]
    housing_type: Literal["studio", "1br", "2br", "3br", "house"]
    monthly_rent: float  # Current market rent
    purchase_price: float  # If buying (0 if not for sale)
    bedrooms: int
    commute_time_minutes: int  # One-way commute to typical NYC job
    neighborhood_quality: int = 50  # 0-100 quality score
    allows_roommates: bool = True
    
    # Trade-off calculations
    annual_rent_cost: float = Field(default=0.0, init=False)
    weekly_commute_hours: float = Field(default=0.0, init=False)
    
    def __init__(self, **data):
        super().__init__(**data)
        self.annual_rent_cost = self.monthly_rent * 12
        self.weekly_commute_hours = (self.commute_time_minutes * 2 * 5) / 60  # 2 trips/day, 5 days/week


class OwnedProperty(BaseModel):
    """A property the player owns"""
    property_id: str
    option_id: str  # References HousingOption
    purchase_price: float
    purchase_date: str
    current_value: float
    down_payment: float
    has_mortgage: bool
    mortgage: Optional[Mortgage] = None
    appreciation_rate: float = 0.03  # 3% annual appreciation
    monthly_hoa_fees: float = 0.0
    monthly_property_tax: float = 0.0
    monthly_insurance: float = 0.0
    monthly_maintenance: float = 0.0
    
    def get_total_monthly_cost(self) -> float:
        """Calculate total monthly ownership cost"""
        cost = self.monthly_hoa_fees + self.monthly_property_tax + self.monthly_insurance + self.monthly_maintenance
        if self.has_mortgage and self.mortgage:
            cost += self.mortgage.monthly_payment
        return cost
    
    def get_equity(self) -> float:
        """Calculate current equity (value - remaining loan balance)"""
        mortgage_balance = self.mortgage.current_balance if self.has_mortgage and self.mortgage else 0.0
        return self.current_value - mortgage_balance


class HousingDecision(BaseModel):
    """Record of a major housing decision"""
    decision_id: str
    decision_type: Literal["rent", "buy", "move", "add_roommate", "remove_roommate"]
    timestamp: str
    from_housing: str = ""
    to_housing: str
    financial_impact: float  # Immediate cost (or savings if negative)
    reason: str
    

class HousingAchievement(BaseModel):
    """Achievement for housing milestones"""
    achievement_id: str
    name: str
    description: str
    date_earned: str
    tier: Literal["bronze", "silver", "gold", "platinum"]


class HousingStory(BaseModel):
    """Narrative moment from housing decisions"""
    story_id: str
    title: str
    message: str
    timestamp: str
    tone: Literal["cautionary", "triumphant", "informative", "shock"]


class BuyVsRentAnalysis(BaseModel):
    """Comparison analysis for buy vs rent decision"""
    years_to_analyze: int = 5
    
    # Renting scenario
    rent_total_cost: float
    rent_monthly_avg: float
    rent_inflation_adjusted: bool = True
    
    # Buying scenario
    buy_purchase_price: float
    buy_down_payment: float
    buy_loan_amount: float
    buy_monthly_payment: float
    buy_total_payments: float
    buy_property_value: float  # After appreciation
    buy_equity: float
    buy_closing_costs: float
    buy_opportunity_cost: float  # What down payment could earn in investments
    
    # Comparison
    net_cost_rent: float  # Total spent on rent
    net_cost_buy: float  # Total spent - equity gained
    breakeven_years: float  # When buying becomes cheaper than renting
    recommendation: Literal["rent", "buy", "borderline"]
    reasoning: str


class HousingMarketState(BaseModel):
    """Complete housing state for a player"""
    market: HousingMarket = Field(default_factory=HousingMarket)
    current_housing: Optional[str] = None  # option_id of current residence
    current_rent: float = 0.0
    roommate_arrangement: RoommateArrangement = Field(default_factory=RoommateArrangement)
    
    # Ownership
    owned_properties: List[OwnedProperty] = []
    down_payment_saved: float = 0.0
    down_payment_goal: float = 0.0  # Target for purchase
    
    # History
    decisions: List[HousingDecision] = []
    achievements: List[HousingAchievement] = []
    stories: List[HousingStory] = []
    
    # Cumulative stats
    total_rent_paid_lifetime: float = 0.0
    total_mortgage_paid: float = 0.0
    total_interest_paid: float = 0.0
    months_renting: int = 0
    months_owning: int = 0
    
    def get_current_monthly_housing_cost(self) -> float:
        """Calculate current monthly housing expense"""
        if self.owned_properties:
            # If owning, sum all property costs
            return sum(prop.get_total_monthly_cost() for prop in self.owned_properties)
        else:
            # If renting, apply roommate split
            return self.current_rent * self.roommate_arrangement.rent_split_percent
    
    def get_total_equity(self) -> float:
        """Total equity across all owned properties"""
        return sum(prop.get_equity() for prop in self.owned_properties)
