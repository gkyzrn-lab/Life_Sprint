"""
Side Gigs & Freelancing Models

IMPORTANT DESIGN PHILOSOPHY:
This system teaches teens about MODERN INCOME OPPORTUNITIES beyond traditional jobs.

Key lessons:
1. GIG ECONOMY IS FLEXIBLE - Work on your own schedule, but income varies
2. PASSIVE INCOME TAKES TIME - Blogging/YouTube require months/years to pay off
3. ENTREPRENEURSHIP IS RISKY - High potential reward, but high failure rate
4. SKILLS = MONEY - Photography, coding, design can be monetized
5. DIVERSIFICATION MATTERS - Multiple income streams = financial security
6. TIME TRADE-OFFS - Every gig costs time that could be spent on school/health/social

This system is designed to be REALISTIC and EDUCATIONAL:
- Gig income is variable (some weeks good, some bad)
- Passive income starts at $0, grows slowly over months
- Business startup costs are real (many fail in first year)
- Freelance rates depend on skill level and portfolio quality
- Time management is critical (burnout is real)
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional, Dict
from enum import Enum


class GigType(str, Enum):
    """Types of gig economy work"""
    DELIVERY = "delivery"  # DoorDash, Uber Eats, Instacart
    RIDESHARE = "rideshare"  # Uber, Lyft
    TUTORING = "tutoring"  # Online tutoring, SAT prep
    FREELANCE_WRITING = "freelance_writing"  # Content writing, copywriting
    FREELANCE_DESIGN = "freelance_design"  # Graphic design, web design
    FREELANCE_CODING = "freelance_coding"  # Web development, app development
    PHOTOGRAPHY = "photography"  # Event photography, stock photos
    VIDEOGRAPHY = "videography"  # Event videos, YouTube editing
    SOCIAL_MEDIA_MANAGEMENT = "social_media_management"  # Manage accounts for small businesses
    VIRTUAL_ASSISTANT = "virtual_assistant"  # Admin tasks, scheduling
    PET_SITTING = "pet_sitting"  # Dog walking, pet sitting
    HANDYMAN = "handyman"  # Small repairs, furniture assembly


class PassiveIncomeType(str, Enum):
    """Types of passive income (long-term payoff)"""
    BLOG = "blog"  # Blogging with ads/affiliate links
    YOUTUBE = "youtube"  # YouTube channel with ads
    PODCAST = "podcast"  # Podcast with sponsorships
    STOCK_DIVIDENDS = "stock_dividends"  # Dividend-paying stocks
    ETSY_SHOP = "etsy_shop"  # Sell digital products/crafts
    ONLINE_COURSE = "online_course"  # Create and sell courses
    EBOOK = "ebook"  # Self-published books on Amazon
    STOCK_PHOTOGRAPHY = "stock_photography"  # Sell photos on stock sites
    AFFILIATE_MARKETING = "affiliate_marketing"  # Promote products for commission
    RENTAL_INCOME = "rental_income"  # Rent out room/parking spot


class BusinessType(str, Enum):
    """Types of small businesses (high risk, high reward)"""
    ONLINE_STORE = "online_store"  # E-commerce (Shopify, Amazon FBA)
    SERVICE_BUSINESS = "service_business"  # Consulting, coaching
    FOOD_BUSINESS = "food_business"  # Catering, food truck
    CREATIVE_STUDIO = "creative_studio"  # Photography, design studio
    TECH_STARTUP = "tech_startup"  # App, SaaS product
    DROPSHIPPING = "dropshipping"  # E-commerce without inventory
    CLOTHING_BRAND = "clothing_brand"  # Fashion/streetwear brand
    FREELANCE_AGENCY = "freelance_agency"  # Hire other freelancers
    SUBSCRIPTION_BOX = "subscription_box"  # Curated monthly boxes
    MOBILE_APP = "mobile_app"  # iOS/Android app


class GigOpportunity(BaseModel):
    """A single gig economy opportunity"""
    gig_id: str = Field(..., description="Unique identifier for this gig")
    gig_type: GigType = Field(..., description="Type of gig work")
    name: str = Field(..., description="Display name (e.g., 'DoorDash Delivery')")
    description: str = Field(..., description="What the gig involves")
    
    # Requirements
    min_age: int = Field(default=18, description="Minimum age (most require 18+)")
    requires_car: bool = Field(default=False, description="Need a car?")
    requires_smartphone: bool = Field(default=True, description="Need smartphone?")
    skill_requirements: Dict[str, int] = Field(
        default_factory=dict,
        description="Skills needed (e.g., {'coding': 60, 'design': 40})"
    )
    
    # Income potential (per hour)
    min_hourly_rate: float = Field(..., description="Minimum $/hour (bad weeks)")
    avg_hourly_rate: float = Field(..., description="Average $/hour")
    max_hourly_rate: float = Field(..., description="Maximum $/hour (good weeks)")
    
    # Time flexibility
    flexible_hours: bool = Field(default=True, description="Set your own schedule?")
    min_hours_per_week: int = Field(default=0, description="Minimum commitment")
    max_hours_per_week: int = Field(default=40, description="Practical maximum")
    
    # Costs
    startup_cost: float = Field(default=0.0, description="Initial cost to get started")
    ongoing_costs_per_month: float = Field(
        default=0.0,
        description="Gas, phone data, equipment maintenance"
    )
    
    # Impact on player
    stress_per_hour: float = Field(
        default=2.0,
        description="Stress increase per hour worked"
    )
    energy_per_hour: float = Field(
        default=5.0,
        description="Energy decrease per hour worked"
    )
    
    # Growth potential
    skill_improvement_per_hour: Dict[str, float] = Field(
        default_factory=dict,
        description="Skills improved while doing gig"
    )
    portfolio_boost: bool = Field(
        default=False,
        description="Does this build your portfolio?"
    )


class ActiveGig(BaseModel):
    """A gig the player is currently doing"""
    gig_id: str = Field(..., description="Reference to GigOpportunity")
    started_date: datetime = Field(default_factory=datetime.now)
    total_hours_worked: float = Field(default=0.0, description="Lifetime hours")
    total_earned: float = Field(default=0.0, description="Lifetime earnings")
    
    # Weekly tracking
    hours_this_week: float = Field(default=0.0)
    earnings_this_week: float = Field(default=0.0)
    
    # Performance (affects rates)
    customer_rating: float = Field(
        default=5.0,
        description="Average rating (3.0-5.0, affects gig access)"
    )
    completion_rate: float = Field(
        default=1.0,
        description="% of accepted gigs completed (0.0-1.0)"
    )
    
    # Tracking
    is_active: bool = Field(default=True, description="Still doing this gig?")
    last_worked: Optional[datetime] = None


class PassiveIncomeStream(BaseModel):
    """A passive income project (takes time to build)"""
    stream_id: str = Field(..., description="Unique identifier")
    income_type: PassiveIncomeType = Field(..., description="Type of passive income")
    name: str = Field(..., description="Project name (e.g., 'My Tech Blog')")
    description: str = Field(..., description="What it is")
    
    # Progress (passive income grows over time)
    started_date: datetime = Field(default_factory=datetime.now)
    months_active: int = Field(default=0, description="Months since start")
    
    # Growth metrics (platform-specific)
    followers_subscribers: int = Field(
        default=0,
        description="Blog readers, YouTube subscribers, etc."
    )
    monthly_views_visits: int = Field(
        default=0,
        description="Monthly traffic"
    )
    
    # Income (starts at $0, grows slowly)
    current_monthly_income: float = Field(
        default=0.0,
        description="Current $/month from this stream"
    )
    total_earned: float = Field(default=0.0, description="Lifetime earnings")
    
    # Investment required (time and money)
    startup_cost: float = Field(
        default=0.0,
        description="Domain, hosting, equipment, etc."
    )
    time_invested_hours: float = Field(
        default=0.0,
        description="Total hours spent building this"
    )
    
    # Monthly effort to maintain
    hours_per_month_required: float = Field(
        default=10.0,
        description="Time to maintain and grow"
    )
    
    # Growth rate (how fast it's growing)
    growth_rate: float = Field(
        default=1.1,
        description="Multiplier per month (1.1 = 10% growth)"
    )
    
    # Status
    is_active: bool = Field(default=True, description="Still working on this?")
    monetized: bool = Field(
        default=False,
        description="Has it reached monetization threshold?"
    )


class SmallBusiness(BaseModel):
    """A small business the player started (HIGH RISK, HIGH REWARD)"""
    business_id: str = Field(..., description="Unique identifier")
    business_type: BusinessType = Field(..., description="Type of business")
    name: str = Field(..., description="Business name")
    description: str = Field(..., description="What the business does")
    
    # Startup
    started_date: datetime = Field(default_factory=datetime.now)
    months_in_operation: int = Field(default=0)
    
    # Financial
    startup_cost: float = Field(..., description="Initial investment")
    total_invested: float = Field(
        default=0.0,
        description="Cumulative money invested"
    )
    total_revenue: float = Field(default=0.0, description="Lifetime sales")
    total_expenses: float = Field(default=0.0, description="Lifetime costs")
    monthly_revenue: float = Field(default=0.0, description="Current $/month sales")
    monthly_expenses: float = Field(
        default=0.0,
        description="Rent, inventory, ads, etc."
    )
    
    # Profitability
    is_profitable: bool = Field(
        default=False,
        description="Revenue > Expenses?"
    )
    months_to_break_even: Optional[int] = Field(
        default=None,
        description="How many months until profitable?"
    )
    
    # Status
    status: str = Field(
        default="startup",
        description="startup, growing, stable, struggling, failed"
    )
    is_active: bool = Field(default=True)
    
    # Success factors
    customer_count: int = Field(default=0, description="Total customers")
    customer_satisfaction: float = Field(
        default=4.0,
        description="Average rating (1.0-5.0)"
    )
    
    # Time investment
    hours_per_week: float = Field(
        default=20.0,
        description="Time spent on business"
    )


class SideGigsState(BaseModel):
    """Complete state of player's side gigs and entrepreneurship"""
    
    # Active gigs
    active_gigs: List[ActiveGig] = Field(
        default_factory=list,
        description="Gigs currently doing"
    )
    
    # Passive income streams
    passive_income_streams: List[PassiveIncomeStream] = Field(
        default_factory=list,
        description="Passive income projects"
    )
    
    # Businesses
    businesses: List[SmallBusiness] = Field(
        default_factory=list,
        description="Small businesses started"
    )
    
    # Overall stats
    total_gig_income: float = Field(
        default=0.0,
        description="Lifetime earnings from gigs"
    )
    total_passive_income: float = Field(
        default=0.0,
        description="Lifetime earnings from passive income"
    )
    total_business_income: float = Field(
        default=0.0,
        description="Lifetime earnings from businesses"
    )
    
    # Current monthly income (from all sources)
    monthly_gig_income: float = Field(
        default=0.0,
        description="Average monthly gig income"
    )
    monthly_passive_income: float = Field(
        default=0.0,
        description="Current monthly passive income"
    )
    monthly_business_income: float = Field(
        default=0.0,
        description="Current monthly business profit"
    )
    
    # Time spent this week
    gig_hours_this_week: float = Field(
        default=0.0,
        description="Hours spent on gigs this week"
    )
    passive_income_hours_this_week: float = Field(
        default=0.0,
        description="Hours spent on passive income this week"
    )
    business_hours_this_week: float = Field(
        default=0.0,
        description="Hours spent on business this week"
    )
    
    # Achievements unlocked
    side_gig_achievements_unlocked: List[str] = Field(
        default_factory=list,
        description="Achievement IDs"
    )
    
    # Stories experienced
    side_gig_stories: List[Dict] = Field(
        default_factory=list,
        description="Narrative moments"
    )
    
    # Skills developed through gigs
    skill_improvements: Dict[str, float] = Field(
        default_factory=dict,
        description="Skills improved through side work"
    )
    
    # Portfolio/reputation
    portfolio_quality: float = Field(
        default=0.0,
        description="Quality of work samples (0-100)"
    )
    online_reputation: float = Field(
        default=0.0,
        description="Reviews, ratings, social proof (0-100)"
    )
    
    def get_total_side_income_monthly(self) -> float:
        """Calculate total monthly income from all side hustles"""
        return (
            self.monthly_gig_income +
            self.monthly_passive_income +
            self.monthly_business_income
        )
    
    def get_total_hours_per_week(self) -> float:
        """Calculate total hours spent on side hustles per week"""
        return (
            self.gig_hours_this_week +
            self.passive_income_hours_this_week +
            self.business_hours_this_week
        )
    
    def is_over_committed(self) -> bool:
        """
        Check if player is spending too much time on side hustles.
        More than 20 hours/week on top of school/job is unsustainable.
        """
        return self.get_total_hours_per_week() > 20
