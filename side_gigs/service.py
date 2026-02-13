"""
Side Gigs & Freelancing Service

This service handles:
1. Starting and working gigs (DoorDash, freelancing, etc.)
2. Building passive income streams (blog, YouTube, etc.)
3. Starting and managing small businesses
4. Income tracking and time management
5. Skill growth and portfolio building
"""

import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

from core_domain.player.player_model import Player
from core_domain.side_gigs.side_gigs_models import (
    ActiveGig,
    PassiveIncomeStream,
    SmallBusiness,
    GigType,
    PassiveIncomeType,
    BusinessType,
)
from catalogs.side_gigs import (
    GIG_OPPORTUNITIES,
    PASSIVE_INCOME_OPTIONS,
    BUSINESS_OPTIONS,
    SIDE_GIG_ACHIEVEMENTS,
    SIDE_GIG_STORIES,
)


def can_start_gig(player: Player, gig_id: str) -> Tuple[bool, Optional[str]]:
    """
    Check if player meets requirements for a gig.
    Returns (can_start, reason_if_not)
    """
    if gig_id not in GIG_OPPORTUNITIES:
        return False, "Gig not found"
    
    gig = GIG_OPPORTUNITIES[gig_id]
    
    # Age requirement (most gigs require 18+, rideshare requires 21+)
    player_age = 18 + (player.plan.semester // 2) if player.plan else player.age  # Approximate age
    if player_age < gig.min_age:
        return False, f"Must be {gig.min_age}+ years old (rideshare apps require 21+)"
    
    # Car requirement
    if gig.requires_car:
        # Check if player can afford a car or has one
        # For now, assume if they have $5000+ they can have a car
        if player.finance.balance < 5000:
            return False, "This gig requires a car (need $5000+ for used car)"
    
    # Skill requirements
    for skill, required_level in gig.skill_requirements.items():
        if skill == "academic_performance":
            # Check GPA (75 = 3.0 GPA)
            if player.academics.gpa < 3.0:
                return False, "Need 3.0+ GPA for tutoring gigs"
        elif skill == "coding":
            # Check if player has coding skill (from CS major or projects)
            if player.stats.technical_skills < required_level:
                return False, f"Need {required_level}+ coding skills (take CS courses or build projects)"
        elif skill == "design":
            if player.stats.technical_skills < required_level:
                return False, f"Need {required_level}+ design skills (take design courses or build portfolio)"
        elif skill == "writing":
            # Assume all college students can write at 40+, higher levels need portfolio
            if required_level > 60 and player.side_gigs.portfolio_quality < 50:
                return False, f"Need stronger portfolio for high-paying writing gigs"
    
    # Startup cost
    if gig.startup_cost > player.finance.balance:
        return False, f"Need ${gig.startup_cost:.0f} to start (equipment, software, etc.)"
    
    return True, None


def start_gig(player: Player, gig_id: str) -> Tuple[ActiveGig, Optional[str]]:
    """
    Start a new gig. Deduct startup costs.
    Returns (ActiveGig, story_message)
    """
    can_start, reason = can_start_gig(player, gig_id)
    if not can_start:
        raise ValueError(f"Cannot start gig: {reason}")
    
    gig = GIG_OPPORTUNITIES[gig_id]
    
    # Deduct startup cost
    if gig.startup_cost > 0:
        player.finance.balance -= gig.startup_cost
    
    # Create ActiveGig
    active_gig = ActiveGig(
        gig_id=gig_id,
        started_date=datetime.now(),
        total_hours_worked=0.0,
        total_earned=0.0,
        hours_this_week=0.0,
        earnings_this_week=0.0,
        customer_rating=5.0,
        completion_rate=1.0,
        is_active=True,
        last_worked=None,
    )
    
    player.side_gigs.active_gigs.append(active_gig)
    
    # Check for first gig achievement
    if len(player.side_gigs.active_gigs) == 1:
        _unlock_achievement(player, "first_gig")
    
    # Trigger story
    story = f"You started {gig.name}. "
    if gig.startup_cost > 0:
        story += f"Startup cost: ${gig.startup_cost:.0f}. "
    story += "Let's see how it goes."
    
    return active_gig, story


def work_gig(
    player: Player,
    gig_id: str,
    hours: float
) -> Tuple[float, float, Optional[str]]:
    """
    Work a gig for X hours. Returns (earnings, expenses, story_message).
    
    Income varies based on:
    - Min/avg/max hourly rate (randomized)
    - Player's customer rating (higher rating = more orders/jobs)
    - Player's skills (better skills = higher effective rate)
    """
    # Find active gig
    active_gig = None
    for gig in player.side_gigs.active_gigs:
        if gig.gig_id == gig_id and gig.is_active:
            active_gig = gig
            break
    
    if not active_gig:
        raise ValueError(f"Gig {gig_id} not active")
    
    gig_config = GIG_OPPORTUNITIES[gig_id]
    
    # Calculate hourly rate (random within range, biased by rating)
    # Good rating (4.5+) = higher chance of max rate
    # Poor rating (< 4.0) = lower rates
    if active_gig.customer_rating >= 4.5:
        # Bias toward max rate
        rate = random.uniform(gig_config.avg_hourly_rate, gig_config.max_hourly_rate)
    elif active_gig.customer_rating >= 4.0:
        # Normal range
        rate = random.uniform(gig_config.min_hourly_rate, gig_config.max_hourly_rate)
    else:
        # Bias toward min rate (poor performance)
        rate = random.uniform(gig_config.min_hourly_rate, gig_config.avg_hourly_rate)
    
    # Skill bonus (if applicable)
    skill_multiplier = 1.0
    if gig_config.skill_improvement_per_hour:
        # If gig improves coding/design/writing, player's skill affects income
        if "coding" in gig_config.skill_improvement_per_hour:
            skill_multiplier = 1.0 + (player.stats.technical_skills / 100) * 0.3  # Up to +30%
        elif "design" in gig_config.skill_improvement_per_hour:
            skill_multiplier = 1.0 + (player.stats.technical_skills / 100) * 0.3
        elif "writing" in gig_config.skill_improvement_per_hour:
            skill_multiplier = 1.0 + (player.stats.communication_skills / 100) * 0.2  # Up to +20%
    
    rate *= skill_multiplier
    
    # Calculate earnings
    gross_earnings = hours * rate
    
    # Calculate expenses (ongoing costs)
    monthly_costs = gig_config.ongoing_costs_per_month
    hourly_costs = (monthly_costs / 160) * hours  # Assume 160 hours/month
    
    net_earnings = gross_earnings - hourly_costs
    
    # Update active gig
    active_gig.total_hours_worked += hours
    active_gig.total_earned += net_earnings
    active_gig.hours_this_week += hours
    active_gig.earnings_this_week += net_earnings
    active_gig.last_worked = datetime.now()
    
    # Update player state
    player.side_gigs.total_gig_income += net_earnings
    player.side_gigs.gig_hours_this_week += hours
    player.finance.balance += net_earnings
    
    # Impact on player (stress, energy)
    stress_increase = hours * gig_config.stress_per_hour
    energy_decrease = hours * gig_config.energy_per_hour
    player.stats.stress = min(100, player.stats.stress + stress_increase)
    player.stats.energy_level = max(0, player.stats.energy_level - energy_decrease)
    
    # Skill improvement
    for skill, improvement_per_hour in gig_config.skill_improvement_per_hour.items():
        improvement = hours * improvement_per_hour
        if skill == "coding" or skill == "design":
            player.stats.technical_skills = min(100, player.stats.technical_skills + improvement)
        elif skill == "communication" or skill == "teaching":
            player.stats.communication_skills = min(100, player.stats.communication_skills + improvement)
        elif skill == "time_management" or skill == "organization":
            player.stats.time_management = min(100, player.stats.time_management + improvement)
    
    # Portfolio boost
    if gig_config.portfolio_boost:
        portfolio_increase = hours * 0.5  # 0.5 points per hour
        player.side_gigs.portfolio_quality = min(
            100,
            player.side_gigs.portfolio_quality + portfolio_increase
        )
    
    # Check for achievements
    if active_gig.total_hours_worked >= 100:
        _unlock_achievement(player, "gig_grinder")
    
    if player.side_gigs.total_gig_income >= 1000:
        _unlock_achievement(player, "side_income_1k")
    
    if player.side_gigs.portfolio_quality >= 50:
        _unlock_achievement(player, "portfolio_builder")
    
    # Check for burnout warning
    if player.side_gigs.get_total_hours_per_week() >= 60:
        _unlock_achievement(player, "burnout_warning")
    
    # Story triggers
    story = None
    if active_gig.total_hours_worked == hours:  # First shift
        story = _get_story(player, "first_gig_day")
    
    return net_earnings, hourly_costs, story


def calculate_weekly_gig_income(player: Player) -> float:
    """Calculate average weekly gig income across all active gigs"""
    total = 0.0
    for gig in player.side_gigs.active_gigs:
        if gig.is_active:
            total += gig.earnings_this_week
    return total


def reset_weekly_gig_hours(player: Player):
    """Reset weekly hours for all gigs (call at start of new week)"""
    player.side_gigs.gig_hours_this_week = 0.0
    for gig in player.side_gigs.active_gigs:
        gig.hours_this_week = 0.0
        gig.earnings_this_week = 0.0


def start_passive_income_stream(
    player: Player,
    income_type: PassiveIncomeType,
    name: str
) -> Tuple[PassiveIncomeStream, Optional[str]]:
    """
    Start a passive income project (blog, YouTube, etc.).
    Returns (PassiveIncomeStream, story_message)
    
    IMPORTANT: Passive income starts at $0 and grows SLOWLY over months.
    """
    # Find config
    config = None
    for key, val in PASSIVE_INCOME_OPTIONS.items():
        if val["income_type"] == income_type:
            config = val
            break
    
    if not config:
        raise ValueError(f"Passive income type {income_type} not found")
    
    # Check startup cost
    if config["startup_cost"] > player.finance.balance:
        raise ValueError(
            f"Need ${config['startup_cost']:.0f} to start (domain, equipment, etc.)"
        )
    
    # Check skills
    for skill, required_level in config["skills_required"].items():
        if skill == "coding" or skill == "design" or skill == "video_editing":
            if player.stats.technical_skills < required_level:
                raise ValueError(f"Need {required_level}+ {skill} skills")
        elif skill == "writing" or skill == "seo":
            if player.stats.communication_skills < required_level:
                raise ValueError(f"Need {required_level}+ {skill} skills")
    
    # Deduct startup cost
    player.finance.balance -= config["startup_cost"]
    
    # Create stream
    stream = PassiveIncomeStream(
        stream_id=f"{income_type.value}_{len(player.side_gigs.passive_income_streams) + 1}",
        income_type=income_type,
        name=name,
        description=config["description"],
        started_date=datetime.now(),
        months_active=0,
        followers_subscribers=0,
        monthly_views_visits=0,
        current_monthly_income=0.0,
        total_earned=0.0,
        startup_cost=config["startup_cost"],
        time_invested_hours=config["initial_time_investment_hours"],
        hours_per_month_required=config["hours_per_month_required"],
        growth_rate=config["growth_rate"],
        is_active=True,
        monetized=False,
    )
    
    player.side_gigs.passive_income_streams.append(stream)
    
    # Achievement
    if len(player.side_gigs.passive_income_streams) == 1:
        _unlock_achievement(player, "passive_income_starter")
    
    # Story
    story = _get_story(player, "passive_income_reality")
    
    return stream, story


def update_passive_income_streams(player: Player, months_passed: int = 1) -> List[str]:
    """
    Update all passive income streams (call monthly).
    Returns list of story messages.
    
    Passive income grows based on:
    - Time (months_active)
    - Growth rate (exponential)
    - Player consistency (hours_per_month_required)
    """
    stories = []
    
    for stream in player.side_gigs.passive_income_streams:
        if not stream.is_active:
            continue
        
        # Find config
        config = None
        for key, val in PASSIVE_INCOME_OPTIONS.items():
            if val["income_type"] == stream.income_type:
                config = val
                break
        
        if not config:
            continue
        
        # Increment months
        stream.months_active += months_passed
        
        # Get expected income for this month (from timeline)
        income_timeline = config["income_timeline"]
        expected_income = 0.0
        
        # Find closest month in timeline
        for month in sorted(income_timeline.keys()):
            if stream.months_active >= month:
                expected_income = income_timeline[month]
        
        # Apply growth rate (if past initial timeline)
        if stream.months_active > max(income_timeline.keys()):
            # Exponential growth beyond timeline
            months_beyond = stream.months_active - max(income_timeline.keys())
            expected_income = income_timeline[max(income_timeline.keys())]
            expected_income *= (stream.growth_rate ** months_beyond)
        
        # Randomize slightly (90-110% of expected)
        actual_income = expected_income * random.uniform(0.9, 1.1)
        
        # Update stream
        stream.current_monthly_income = actual_income
        stream.total_earned += actual_income
        
        # Update followers/views (roughly proportional to income)
        if stream.income_type == PassiveIncomeType.BLOG:
            stream.monthly_views_visits = int(actual_income * 30)  # $1 = ~30 views
            stream.followers_subscribers = int(stream.monthly_views_visits * 0.1)
        elif stream.income_type == PassiveIncomeType.YOUTUBE:
            stream.followers_subscribers = int(actual_income * 10)  # $1 = ~10 subs
            stream.monthly_views_visits = int(actual_income * 500)  # $1 = ~500 views
        
        # Check monetization threshold
        if not stream.monetized and actual_income >= 25:
            stream.monetized = True
            stories.append(f"🎉 {stream.name} is now monetized! Earning ${actual_income:.0f}/month.")
        
        # Add income to player
        player.finance.balance += actual_income
        player.side_gigs.total_passive_income += actual_income
        player.side_gigs.monthly_passive_income = sum(
            s.current_monthly_income for s in player.side_gigs.passive_income_streams if s.is_active
        )
        
        # Check for achievements
        if actual_income > 0 and player.side_gigs.total_passive_income == actual_income:
            # First dollar
            _unlock_achievement(player, "first_dollar_passive")
            stories.append(_get_story(player, "first_passive_dollar"))
        
        if player.side_gigs.monthly_passive_income >= 100:
            _unlock_achievement(player, "passive_income_100")
        
        if player.side_gigs.monthly_passive_income >= 1000:
            _unlock_achievement(player, "passive_income_1k")
    
    return stories


def start_business(
    player: Player,
    business_type: BusinessType,
    name: str
) -> Tuple[SmallBusiness, Optional[str]]:
    """
    Start a small business. HIGH RISK, HIGH REWARD.
    
    Requires significant startup capital.
    Returns (SmallBusiness, story_message)
    """
    # Find config
    config = None
    for key, val in BUSINESS_OPTIONS.items():
        if val["business_type"] == business_type:
            config = val
            break
    
    if not config:
        raise ValueError(f"Business type {business_type} not found")
    
    # Check startup cost
    if config["startup_cost"] > player.finance.balance:
        raise ValueError(
            f"Need ${config['startup_cost']:.0f} to start (significantly more risk than gigs)"
        )
    
    # Check skills
    for skill, required_level in config["skills_required"].items():
        if skill == "coding" or skill == "product_design":
            if player.stats.technical_skills < required_level:
                raise ValueError(f"Need {required_level}+ {skill} skills to start this business")
        elif skill == "business" or skill == "marketing" or skill == "sales":
            if player.stats.business_acumen < required_level:
                raise ValueError(f"Need {required_level}+ {skill} knowledge")
    
    # Deduct startup cost
    player.finance.balance -= config["startup_cost"]
    
    # Create business
    business = SmallBusiness(
        business_id=f"{business_type.value}_{len(player.side_gigs.businesses) + 1}",
        business_type=business_type,
        name=name,
        description=config["description"],
        started_date=datetime.now(),
        months_in_operation=0,
        startup_cost=config["startup_cost"],
        total_invested=config["startup_cost"],
        total_revenue=0.0,
        total_expenses=config["startup_cost"],
        monthly_revenue=0.0,
        monthly_expenses=config["monthly_fixed_costs"],
        is_profitable=False,
        months_to_break_even=config["breakeven_months"],
        status="startup",
        is_active=True,
        customer_count=0,
        customer_satisfaction=4.0,
        hours_per_week=config["ongoing_hours_per_week"],
    )
    
    player.side_gigs.businesses.append(business)
    
    # Achievement
    if len(player.side_gigs.businesses) == 1:
        _unlock_achievement(player, "entrepreneur")
    
    # Story
    story = _get_story(player, "business_startup_costs")
    
    return business, story


def update_businesses(player: Player, months_passed: int = 1) -> List[str]:
    """
    Update all businesses (call monthly).
    Returns list of story messages.
    
    Business success depends on:
    - Time (revenue grows over months)
    - Player skills (better skills = higher success rate)
    - Luck (random events, competition)
    """
    stories = []
    
    for business in player.side_gigs.businesses:
        if not business.is_active:
            continue
        
        # Find config
        config = None
        for key, val in BUSINESS_OPTIONS.items():
            if val["business_type"] == business.business_type:
                config = val
                break
        
        if not config:
            continue
        
        # Increment months
        business.months_in_operation += months_passed
        
        # Get expected revenue for this month (from timeline)
        revenue_timeline = config["revenue_timeline"]
        expected_revenue = 0.0
        
        for month in sorted(revenue_timeline.keys()):
            if business.months_in_operation >= month:
                expected_revenue = revenue_timeline[month]
        
        # Success/failure check (random chance each month)
        failure_rate = config["failure_rate_per_month"]
        if random.random() < failure_rate:
            # Business struggling
            expected_revenue *= 0.5
            business.status = "struggling"
        
        # Skill multiplier (better skills = higher revenue)
        skill_multiplier = 1.0
        if business.business_type == BusinessType.MOBILE_APP or business.business_type == BusinessType.TECH_STARTUP:
            skill_multiplier = 0.8 + (player.stats.technical_skills / 100) * 0.4  # 0.8x to 1.2x
        elif business.business_type in [BusinessType.SERVICE_BUSINESS, BusinessType.FREELANCE_AGENCY]:
            skill_multiplier = 0.8 + (player.stats.business_acumen / 100) * 0.4
        
        expected_revenue *= skill_multiplier
        
        # Randomize (80-120% of expected)
        actual_revenue = expected_revenue * random.uniform(0.8, 1.2)
        
        # Calculate expenses
        fixed_costs = config["monthly_fixed_costs"]
        variable_costs = actual_revenue * config["monthly_variable_costs_percent"]
        total_expenses = fixed_costs + variable_costs
        
        # Calculate profit
        profit = actual_revenue - total_expenses
        
        # Update business
        business.monthly_revenue = actual_revenue
        business.monthly_expenses = total_expenses
        business.total_revenue += actual_revenue
        business.total_expenses += total_expenses
        
        # Check profitability
        if profit > 0 and not business.is_profitable:
            business.is_profitable = True
            business.status = "profitable"
            _unlock_achievement(player, "first_profit")
            stories.append(_get_story(player, "business_first_profit"))
        elif profit > 0:
            business.status = "growing"
        elif profit < -500:
            business.status = "struggling"
        
        # Update customer count (rough estimate)
        business.customer_count += int(actual_revenue / 50)  # $50 per customer average
        
        # Add profit/loss to player balance
        player.finance.balance += profit
        player.side_gigs.total_business_income += profit
        player.side_gigs.monthly_business_income = sum(
            b.monthly_revenue - b.monthly_expenses
            for b in player.side_gigs.businesses
            if b.is_active
        )
        
        # Check achievements
        if business.monthly_revenue >= 5000:
            _unlock_achievement(player, "business_5k")
    
    return stories


def check_diversified_income(player: Player):
    """Check if player has 3+ income streams (achievement)"""
    income_streams = 0
    
    # Count traditional job
    if player.career.current_job_id:
        income_streams += 1
    
    # Count active gigs
    if any(g.is_active for g in player.side_gigs.active_gigs):
        income_streams += 1
    
    # Count passive income (if earning $50+/month)
    if player.side_gigs.monthly_passive_income >= 50:
        income_streams += 1
    
    # Count businesses (if profitable)
    if any(b.is_profitable for b in player.side_gigs.businesses):
        income_streams += 1
    
    if income_streams >= 3:
        _unlock_achievement(player, "diversified_income")


def _unlock_achievement(player: Player, achievement_id: str):
    """Unlock a side gig achievement"""
    if achievement_id in player.side_gigs.side_gig_achievements_unlocked:
        return
    
    achievement = next(
        (a for a in SIDE_GIG_ACHIEVEMENTS if a["achievement_id"] == achievement_id),
        None
    )
    
    if achievement:
        player.side_gigs.side_gig_achievements_unlocked.append(achievement_id)


def _get_story(player: Player, story_id: str) -> Optional[str]:
    """Get a story message and record it"""
    story = next(
        (s for s in SIDE_GIG_STORIES if s["story_id"] == story_id),
        None
    )
    
    if story:
        player.side_gigs.side_gig_stories.append({
            "story_id": story_id,
            "title": story["title"],
            "message": story["message"],
            "triggered_at": datetime.now().isoformat(),
        })
        return story["message"]
    
    return None


def get_side_gigs_summary(player: Player) -> Dict:
    """Get complete summary of player's side hustle activities"""
    return {
        "active_gigs": [
            {
                "gig_id": g.gig_id,
                "name": GIG_OPPORTUNITIES[g.gig_id].name if g.gig_id in GIG_OPPORTUNITIES else g.gig_id,
                "total_hours": g.total_hours_worked,
                "total_earned": g.total_earned,
                "hours_this_week": g.hours_this_week,
                "earnings_this_week": g.earnings_this_week,
                "customer_rating": g.customer_rating,
                "avg_hourly_rate": g.total_earned / g.total_hours_worked if g.total_hours_worked > 0 else 0,
            }
            for g in player.side_gigs.active_gigs if g.is_active
        ],
        "passive_income_streams": [
            {
                "stream_id": s.stream_id,
                "name": s.name,
                "type": s.income_type.value,
                "months_active": s.months_active,
                "current_monthly_income": s.current_monthly_income,
                "total_earned": s.total_earned,
                "followers_subscribers": s.followers_subscribers,
                "monetized": s.monetized,
            }
            for s in player.side_gigs.passive_income_streams if s.is_active
        ],
        "businesses": [
            {
                "business_id": b.business_id,
                "name": b.name,
                "type": b.business_type.value,
                "months_in_operation": b.months_in_operation,
                "monthly_revenue": b.monthly_revenue,
                "monthly_expenses": b.monthly_expenses,
                "monthly_profit": b.monthly_revenue - b.monthly_expenses,
                "total_profit": b.total_revenue - b.total_expenses,
                "is_profitable": b.is_profitable,
                "status": b.status,
                "customer_count": b.customer_count,
            }
            for b in player.side_gigs.businesses if b.is_active
        ],
        "total_income": {
            "monthly_gig_income": player.side_gigs.monthly_gig_income,
            "monthly_passive_income": player.side_gigs.monthly_passive_income,
            "monthly_business_income": player.side_gigs.monthly_business_income,
            "total_monthly_side_income": player.side_gigs.get_total_side_income_monthly(),
        },
        "time_tracking": {
            "gig_hours_this_week": player.side_gigs.gig_hours_this_week,
            "passive_income_hours_this_week": player.side_gigs.passive_income_hours_this_week,
            "business_hours_this_week": player.side_gigs.business_hours_this_week,
            "total_hours_this_week": player.side_gigs.get_total_hours_per_week(),
            "over_committed": player.side_gigs.is_over_committed(),
        },
        "portfolio": {
            "portfolio_quality": player.side_gigs.portfolio_quality,
            "online_reputation": player.side_gigs.online_reputation,
        },
        "lifetime_earnings": {
            "total_gig_income": player.side_gigs.total_gig_income,
            "total_passive_income": player.side_gigs.total_passive_income,
            "total_business_income": player.side_gigs.total_business_income,
        },
    }
