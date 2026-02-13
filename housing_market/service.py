"""
Housing Market Service

Business logic for housing decisions, rent vs buy calculations,
roommate management, and commute trade-offs.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
import random
import math

from core_domain.player.player_model import Player
from core_domain.housing.housing_models import (
    HousingOption,
    Mortgage,
    OwnedProperty,
    RoommateArrangement,
    HousingDecision,
    HousingAchievement,
    HousingStory,
    BuyVsRentAnalysis,
)
from catalogs.housing_market import (
    ALL_HOUSING_OPTIONS,
    ROOMMATE_CONFIGS,
    MORTGAGE_PRODUCTS,
    OWNERSHIP_COSTS,
    RENT_INFLATION,
    COMMUTE_COSTS,
    HOUSING_ACHIEVEMENTS,
    HOUSING_STORIES,
)


# ==============================================================================
# RENT & MARKET OPERATIONS
# ==============================================================================

def apply_annual_rent_increase(player: Player) -> Dict[str, Any]:
    """
    Apply annual rent inflation (typically after graduation).
    Rent increases 5-8% per year in NYC area.
    """
    if not player.housing_market.current_housing:
        return {"error": "No current housing to increase rent"}
    
    # Calculate inflation rate
    base_rate = RENT_INFLATION["base_annual_rate"]
    market_modifier = RENT_INFLATION["market_modifiers"][player.housing_market.market.market_heat]
    
    # Check if in NYC (higher inflation)
    housing_option = ALL_HOUSING_OPTIONS.get(player.housing_market.current_housing)
    if housing_option and "nyc" in housing_option.location:
        base_rate += RENT_INFLATION["nyc_premium"]
    
    total_rate = base_rate + market_modifier
    
    old_rent = player.housing_market.current_rent
    new_rent = old_rent * (1 + total_rate)
    increase_amount = new_rent - old_rent
    
    player.housing_market.current_rent = new_rent
    player.housing_market.market.years_since_graduation += 1
    
    # Trigger story
    story = _create_story(
        player,
        "rent_increase",
        HOUSING_STORIES,
        percent=total_rate * 100,
        new_rent=new_rent,
    )
    
    # Check for rent regret achievement
    if player.housing_market.total_rent_paid_lifetime >= 100000:
        _unlock_achievement(player, "rent_regret", HOUSING_ACHIEVEMENTS)
    
    return {
        "old_rent": old_rent,
        "new_rent": new_rent,
        "increase_amount": increase_amount,
        "increase_percent": total_rate,
        "story": story,
    }


def choose_housing(player: Player, option_id: str, roommate_config: str = "alone") -> Dict[str, Any]:
    """
    Choose a new housing option (rent).
    """
    if option_id not in ALL_HOUSING_OPTIONS:
        return {"error": f"Housing option {option_id} not found"}
    
    housing_option = ALL_HOUSING_OPTIONS[option_id]
    
    # Validate roommate configuration
    if roommate_config not in ROOMMATE_CONFIGS:
        return {"error": f"Invalid roommate config: {roommate_config}"}
    
    roommate_cfg = ROOMMATE_CONFIGS[roommate_config]
    
    # Check if housing allows roommates
    if roommate_cfg["num_roommates"] > 0 and not housing_option.allows_roommates:
        return {"error": f"{housing_option.name} does not allow roommates (studio/1br)"}
    
    # Check if enough bedrooms for roommates
    required_bedrooms = roommate_cfg["num_roommates"] + 1
    if housing_option.bedrooms < required_bedrooms:
        return {"error": f"Not enough bedrooms for {roommate_cfg['num_roommates']} roommates"}
    
    # Calculate costs
    old_housing = player.housing_market.current_housing
    old_rent = player.housing_market.current_rent
    
    new_rent = housing_option.monthly_rent
    your_share = new_rent * roommate_cfg["rent_split_percent"]
    monthly_savings = old_rent - your_share if old_housing else 0
    
    # Update player housing
    player.housing_market.current_housing = option_id
    player.housing_market.current_rent = new_rent
    
    # Update roommate arrangement
    player.housing_market.roommate_arrangement = RoommateArrangement(
        num_roommates=roommate_cfg["num_roommates"],
        rent_split_percent=roommate_cfg["rent_split_percent"],
        privacy_level=roommate_cfg["privacy_level"],
        conflict_level=0,
        monthly_savings=monthly_savings if monthly_savings > 0 else 0,
    )
    
    # Record decision
    decision = HousingDecision(
        decision_id=f"housing_{len(player.housing_market.decisions)}",
        decision_type="move",
        timestamp=datetime.now().isoformat(),
        from_housing=old_housing or "",
        to_housing=option_id,
        financial_impact=0,  # No immediate cost for renting (security deposit abstracted)
        reason=f"Moved to {housing_option.name}",
    )
    player.housing_market.decisions.append(decision)
    
    # Trigger stories
    stories = []
    
    # First apartment story
    if not old_housing:
        story = _create_story(player, "first_apartment_shock", HOUSING_STORIES, rent=new_rent)
        stories.append(story)
        _unlock_achievement(player, "first_apartment", HOUSING_ACHIEVEMENTS)
    
    # Roommate story
    if roommate_cfg["num_roommates"] > 0:
        story = _create_story(
            player,
            "roommate_added",
            HOUSING_STORIES,
            old_rent=new_rent,
            new_rent=your_share,
            savings=monthly_savings,
        )
        stories.append(story)
    
    # Long commute story
    if housing_option.commute_time_minutes >= 60:
        commute_analysis = calculate_commute_impact(player, housing_option)
        story = _create_story(
            player,
            "long_commute_reality",
            HOUSING_STORIES,
            hours=commute_analysis["daily_commute_hours"],
            hours_per_week=commute_analysis["weekly_commute_hours"],
            days_per_year=commute_analysis["yearly_commute_days"],
            savings=monthly_savings if monthly_savings > 0 else 0,
        )
        stories.append(story)
    
    return {
        "housing_option": housing_option.model_dump(),
        "monthly_rent": new_rent,
        "your_monthly_cost": your_share,
        "roommates": roommate_cfg["num_roommates"],
        "privacy_level": roommate_cfg["privacy_level"],
        "commute_minutes": housing_option.commute_time_minutes,
        "monthly_savings": monthly_savings,
        "stories": stories,
        "decisions": [decision.model_dump()],
    }


# ==============================================================================
# ROOMMATE MANAGEMENT
# ==============================================================================

def add_roommate(player: Player) -> Dict[str, Any]:
    """
    Add a roommate to current housing (if space available).
    """
    if not player.housing_market.current_housing:
        return {"error": "No current housing"}
    
    housing_option = ALL_HOUSING_OPTIONS[player.housing_market.current_housing]
    
    if not housing_option.allows_roommates:
        return {"error": f"{housing_option.name} does not allow roommates"}
    
    current_roommates = player.housing_market.roommate_arrangement.num_roommates
    max_roommates = housing_option.bedrooms - 1
    
    if current_roommates >= max_roommates:
        return {"error": f"No more bedrooms available (max {max_roommates} roommates)"}
    
    # Update roommate arrangement
    old_share = player.housing_market.roommate_arrangement.rent_split_percent
    new_num_roommates = current_roommates + 1
    new_share = 1.0 / (new_num_roommates + 1)
    
    old_cost = player.housing_market.current_rent * old_share
    new_cost = player.housing_market.current_rent * new_share
    savings = old_cost - new_cost
    
    player.housing_market.roommate_arrangement.num_roommates = new_num_roommates
    player.housing_market.roommate_arrangement.rent_split_percent = new_share
    player.housing_market.roommate_arrangement.privacy_level = max(30, 100 - (new_num_roommates * 25))
    player.housing_market.roommate_arrangement.monthly_savings = savings
    
    # Record decision
    decision = HousingDecision(
        decision_id=f"roommate_{len(player.housing_market.decisions)}",
        decision_type="add_roommate",
        timestamp=datetime.now().isoformat(),
        to_housing=player.housing_market.current_housing,
        financial_impact=-savings,  # Negative = savings
        reason=f"Added roommate #{new_num_roommates}",
    )
    player.housing_market.decisions.append(decision)
    
    # Achievement for smart savings
    if savings >= 500 and new_num_roommates == 1:
        _unlock_achievement(player, "roommate_savings", HOUSING_ACHIEVEMENTS)
    
    # Story
    story = _create_story(
        player,
        "roommate_added",
        HOUSING_STORIES,
        old_rent=old_cost,
        new_rent=new_cost,
        savings=savings,
    )
    
    return {
        "roommates": new_num_roommates,
        "old_monthly_cost": old_cost,
        "new_monthly_cost": new_cost,
        "monthly_savings": savings,
        "privacy_level": player.housing_market.roommate_arrangement.privacy_level,
        "story": story,
    }


def trigger_roommate_conflict(player: Player) -> Dict[str, Any]:
    """
    Random roommate conflict event (simulation).
    """
    if player.housing_market.roommate_arrangement.num_roommates == 0:
        return {"error": "No roommates to have conflicts with"}
    
    # Increase conflict level
    conflict_increase = random.randint(10, 30)
    old_conflict = player.housing_market.roommate_arrangement.conflict_level
    new_conflict = min(100, old_conflict + conflict_increase)
    player.housing_market.roommate_arrangement.conflict_level = new_conflict
    
    # High conflict triggers story
    story = None
    if new_conflict >= 60:
        story = _create_story(player, "roommate_conflict", HOUSING_STORIES)
    
    return {
        "conflict_level": new_conflict,
        "conflict_increase": conflict_increase,
        "story": story,
    }


# ==============================================================================
# BUY VS RENT ANALYSIS
# ==============================================================================

def calculate_buy_vs_rent(
    player: Player,
    option_id: str,
    mortgage_product: str = "conventional_30",
    years: int = 5,
) -> BuyVsRentAnalysis:
    """
    Comprehensive buy vs rent analysis for a specific property.
    """
    if option_id not in ALL_HOUSING_OPTIONS:
        raise ValueError(f"Housing option {option_id} not found")
    
    housing_option = ALL_HOUSING_OPTIONS[option_id]
    mortgage_cfg = MORTGAGE_PRODUCTS[mortgage_product]
    
    # BUYING SCENARIO
    purchase_price = housing_option.purchase_price
    down_payment_percent = mortgage_cfg["min_down_payment_percent"]
    down_payment = purchase_price * down_payment_percent
    loan_amount = purchase_price - down_payment
    
    interest_rate = mortgage_cfg["interest_rate"]
    term_months = mortgage_cfg["term_years"] * 12
    
    # Calculate monthly mortgage payment (principal + interest only)
    monthly_rate = interest_rate / 12
    mortgage_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** term_months) / (
        ((1 + monthly_rate) ** term_months) - 1
    )
    
    # Closing costs
    closing_costs = purchase_price * mortgage_cfg["closing_costs_percent"]
    
    # Additional monthly costs
    property_tax_monthly = (purchase_price * OWNERSHIP_COSTS["property_tax_rate"]) / 12
    insurance_monthly = (purchase_price * OWNERSHIP_COSTS["home_insurance_rate"]) / 12
    maintenance_monthly = (purchase_price * OWNERSHIP_COSTS["maintenance_rate"]) / 12
    
    # HOA fees
    location = housing_option.location
    hoa_monthly = OWNERSHIP_COSTS["hoa_fees"].get(location, 0)
    
    total_monthly_buy = mortgage_payment + property_tax_monthly + insurance_monthly + maintenance_monthly + hoa_monthly
    
    # Total payments over time period
    total_mortgage_payments = mortgage_payment * (years * 12)
    total_other_costs = (property_tax_monthly + insurance_monthly + maintenance_monthly + hoa_monthly) * (years * 12)
    total_buy_payments = total_mortgage_payments + total_other_costs
    
    # Property appreciation
    appreciation_rate = 0.03  # 3% annual
    future_value = purchase_price * ((1 + appreciation_rate) ** years)
    
    # Calculate equity (simplified - actual equity calculation is complex)
    # Approximate: down payment + (portion of principal paid) + appreciation
    principal_paid_approx = total_mortgage_payments * 0.3  # Rough estimate (30% goes to principal in early years)
    equity = down_payment + principal_paid_approx + (future_value - purchase_price)
    
    # Net cost of buying = total spent - equity gained + closing costs
    net_cost_buy = total_buy_payments + closing_costs - equity
    
    # Opportunity cost (what down payment could earn if invested)
    investment_return = 0.07  # 7% annual return
    opportunity_cost = down_payment * ((1 + investment_return) ** years) - down_payment
    
    # RENTING SCENARIO
    monthly_rent = housing_option.monthly_rent
    
    # Rent with inflation
    total_rent_paid = 0
    current_rent = monthly_rent
    for year in range(years):
        total_rent_paid += current_rent * 12
        current_rent *= (1 + RENT_INFLATION["base_annual_rate"])  # Assume 5% annual increase
    
    avg_monthly_rent = total_rent_paid / (years * 12)
    net_cost_rent = total_rent_paid  # All money spent, $0 equity
    
    # COMPARISON
    # Breakeven: when does buying become cheaper than renting?
    breakeven_years = 0
    for test_years in range(1, 31):
        test_rent = sum(monthly_rent * ((1.05) ** y) * 12 for y in range(test_years))
        test_buy_payments = total_monthly_buy * test_years * 12 + closing_costs
        test_equity_approx = down_payment + (mortgage_payment * test_years * 12 * 0.3) + (purchase_price * 0.03 * test_years)
        test_net_buy = test_buy_payments - test_equity_approx
        
        if test_net_buy < test_rent:
            breakeven_years = test_years
            break
    
    if breakeven_years == 0:
        breakeven_years = 30  # Never breaks even in 30 years
    
    # Recommendation
    if years < breakeven_years:
        recommendation = "rent"
        reasoning = f"Renting is cheaper for {years} years. Breakeven at {breakeven_years} years."
    elif years > breakeven_years + 2:
        recommendation = "buy"
        reasoning = f"Buying builds ${equity:,.0f} equity. Breakeven at {breakeven_years} years."
    else:
        recommendation = "borderline"
        reasoning = f"Close call. Breakeven at {breakeven_years} years. Consider personal factors."
    
    # Trigger story
    story = _create_story(
        player,
        "buy_vs_rent_analysis",
        HOUSING_STORIES,
        buy_monthly=total_monthly_buy,
        rent_monthly=monthly_rent,
        equity=equity,
        years=years,
        down_payment=down_payment,
    )
    
    return BuyVsRentAnalysis(
        years_to_analyze=years,
        rent_total_cost=total_rent_paid,
        rent_monthly_avg=avg_monthly_rent,
        rent_inflation_adjusted=True,
        buy_purchase_price=purchase_price,
        buy_down_payment=down_payment,
        buy_loan_amount=loan_amount,
        buy_monthly_payment=total_monthly_buy,
        buy_total_payments=total_buy_payments,
        buy_property_value=future_value,
        buy_equity=equity,
        buy_closing_costs=closing_costs,
        buy_opportunity_cost=opportunity_cost,
        net_cost_rent=net_cost_rent,
        net_cost_buy=net_cost_buy,
        breakeven_years=breakeven_years,
        recommendation=recommendation,
        reasoning=reasoning,
    )


# ==============================================================================
# HOME PURCHASE
# ==============================================================================

def save_for_down_payment(player: Player, amount: float, goal_property_id: str) -> Dict[str, Any]:
    """
    Save money toward down payment for a specific property.
    """
    if goal_property_id not in ALL_HOUSING_OPTIONS:
        return {"error": f"Property {goal_property_id} not found"}
    
    housing_option = ALL_HOUSING_OPTIONS[goal_property_id]
    purchase_price = housing_option.purchase_price
    
    # Assume 20% down payment goal
    down_payment_goal = purchase_price * 0.20
    
    player.housing_market.down_payment_saved += amount
    player.housing_market.down_payment_goal = down_payment_goal
    
    percent_complete = (player.housing_market.down_payment_saved / down_payment_goal) * 100
    
    # Achievement at 50% and 100%
    if percent_complete >= 50 and percent_complete < 100:
        story = _create_story(
            player,
            "down_payment_progress",
            HOUSING_STORIES,
            saved=player.housing_market.down_payment_saved,
            goal=down_payment_goal,
            percent=percent_complete,
        )
    elif percent_complete >= 100:
        _unlock_achievement(player, "down_payment_saved", HOUSING_ACHIEVEMENTS)
        story = _create_story(
            player,
            "down_payment_progress",
            HOUSING_STORIES,
            saved=player.housing_market.down_payment_saved,
            goal=down_payment_goal,
            percent=100,
        )
    else:
        story = None
    
    # Deduct from player cash
    player.finance.balance -= amount
    
    return {
        "amount_saved": amount,
        "total_saved": player.housing_market.down_payment_saved,
        "goal": down_payment_goal,
        "percent_complete": percent_complete,
        "remaining": down_payment_goal - player.housing_market.down_payment_saved,
        "story": story,
    }


def purchase_home(
    player: Player,
    option_id: str,
    mortgage_product: str = "conventional_30",
) -> Dict[str, Any]:
    """
    Purchase a home with mortgage.
    """
    if option_id not in ALL_HOUSING_OPTIONS:
        return {"error": f"Property {option_id} not found"}
    
    housing_option = ALL_HOUSING_OPTIONS[option_id]
    mortgage_cfg = MORTGAGE_PRODUCTS[mortgage_product]
    
    purchase_price = housing_option.purchase_price
    min_down_payment = purchase_price * mortgage_cfg["min_down_payment_percent"]
    
    # Check if enough saved
    if player.housing_market.down_payment_saved < min_down_payment:
        return {
            "error": f"Insufficient down payment. Need ${min_down_payment:,.0f}, have ${player.housing_market.down_payment_saved:,.0f}"
        }
    
    # Use saved down payment
    down_payment = player.housing_market.down_payment_saved
    loan_amount = purchase_price - down_payment
    
    # Calculate mortgage
    interest_rate = mortgage_cfg["interest_rate"]
    term_years = mortgage_cfg["term_years"]
    term_months = term_years * 12
    
    monthly_rate = interest_rate / 12
    monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** term_months) / (
        ((1 + monthly_rate) ** term_months) - 1
    )
    
    # Closing costs
    closing_costs = purchase_price * mortgage_cfg["closing_costs_percent"]
    
    # Check if enough cash for closing costs
    if player.finance.balance < closing_costs:
        return {
            "error": f"Insufficient funds for closing costs. Need ${closing_costs:,.0f}, have ${player.finance.balance:,.0f}"
        }
    
    # Deduct closing costs
    player.finance.balance -= closing_costs
    
    # Calculate additional monthly costs
    property_tax_monthly = (purchase_price * OWNERSHIP_COSTS["property_tax_rate"]) / 12
    insurance_monthly = (purchase_price * OWNERSHIP_COSTS["home_insurance_rate"]) / 12
    maintenance_monthly = (purchase_price * OWNERSHIP_COSTS["maintenance_rate"]) / 12
    hoa_monthly = OWNERSHIP_COSTS["hoa_fees"].get(housing_option.location, 0)
    
    # Create mortgage
    mortgage = Mortgage(
        property_id=option_id,
        original_principal=loan_amount,
        current_balance=loan_amount,
        interest_rate=interest_rate,
        monthly_payment=monthly_payment,
        term_years=term_years,
        months_remaining=term_months,
        total_interest_paid=0.0,
        start_date=datetime.now().isoformat(),
    )
    
    # Create owned property
    owned_property = OwnedProperty(
        property_id=f"owned_{option_id}_{len(player.housing_market.owned_properties)}",
        option_id=option_id,
        purchase_price=purchase_price,
        purchase_date=datetime.now().isoformat(),
        current_value=purchase_price,
        down_payment=down_payment,
        has_mortgage=True,
        mortgage=mortgage,
        monthly_hoa_fees=hoa_monthly,
        monthly_property_tax=property_tax_monthly,
        monthly_insurance=insurance_monthly,
        monthly_maintenance=maintenance_monthly,
    )
    
    player.housing_market.owned_properties.append(owned_property)
    player.housing_market.down_payment_saved = 0  # Reset
    player.housing_market.current_housing = option_id
    
    # Record decision
    decision = HousingDecision(
        decision_id=f"purchase_{len(player.housing_market.decisions)}",
        decision_type="buy",
        timestamp=datetime.now().isoformat(),
        to_housing=option_id,
        financial_impact=down_payment + closing_costs,
        reason=f"Purchased {housing_option.name}",
    )
    player.housing_market.decisions.append(decision)
    
    # Achievement
    _unlock_achievement(player, "first_home_purchase", HOUSING_ACHIEVEMENTS)
    
    # Stories
    purchase_story = _create_story(
        player,
        "home_purchase",
        HOUSING_STORIES,
        price=purchase_price,
        down_payment=down_payment,
        monthly_payment=monthly_payment,
        years=term_years,
    )
    
    total_monthly = owned_property.get_total_monthly_cost()
    reality_story = _create_story(
        player,
        "mortgage_reality",
        HOUSING_STORIES,
        mortgage_payment=monthly_payment,
        principal=monthly_payment * 0.3,  # Approximate
        interest=monthly_payment * 0.7,
        tax=property_tax_monthly,
        insurance=insurance_monthly,
        hoa=hoa_monthly,
        total=total_monthly,
    )
    
    return {
        "purchase_price": purchase_price,
        "down_payment": down_payment,
        "loan_amount": loan_amount,
        "monthly_mortgage_payment": monthly_payment,
        "total_monthly_cost": total_monthly,
        "closing_costs": closing_costs,
        "property": owned_property.model_dump(),
        "stories": [purchase_story, reality_story],
    }


# ==============================================================================
# COMMUTE ANALYSIS
# ==============================================================================

def calculate_commute_impact(player: Player, housing_option: HousingOption) -> Dict[str, Any]:
    """
    Calculate time and financial impact of commuting.
    """
    one_way_minutes = housing_option.commute_time_minutes
    daily_minutes = one_way_minutes * 2
    daily_hours = daily_minutes / 60
    
    # Assume 5 workdays per week, 48 weeks per year
    weekly_minutes = daily_minutes * 5
    weekly_hours = weekly_minutes / 60
    
    yearly_hours = weekly_hours * 48
    yearly_days = yearly_hours / 24
    
    # Financial cost of time
    time_value_per_hour = COMMUTE_COSTS["time_cost_per_hour"]
    yearly_time_cost = yearly_hours * time_value_per_hour
    
    # Transit costs
    monthly_transit = one_way_minutes * COMMUTE_COSTS["transit_cost_per_minute"] * 2 * 22  # 22 workdays/month
    yearly_transit = monthly_transit * 12
    
    # Stress impact
    daily_stress_impact = (daily_hours * COMMUTE_COSTS["stress_per_hour_commute"])
    
    # Long commute achievement
    if one_way_minutes >= 60:
        # Track in player state (would need counter in model)
        pass
    
    return {
        "one_way_minutes": one_way_minutes,
        "daily_commute_hours": daily_hours,
        "weekly_commute_hours": weekly_hours,
        "yearly_commute_hours": yearly_hours,
        "yearly_commute_days": yearly_days,
        "yearly_time_cost": yearly_time_cost,
        "monthly_transit_cost": monthly_transit,
        "yearly_transit_cost": yearly_transit,
        "daily_stress_impact": daily_stress_impact,
    }


# ==============================================================================
# MONTHLY/ANNUAL UPDATES
# ==============================================================================

def process_monthly_housing_costs(player: Player) -> Dict[str, Any]:
    """
    Process monthly rent or mortgage payment.
    Called each month by the game loop.
    """
    monthly_cost = player.housing_market.get_current_monthly_housing_cost()
    
    # Deduct from balance
    player.finance.balance -= monthly_cost
    
    # Track spending
    if player.housing_market.owned_properties:
        # Mortgage payment
        player.housing_market.months_owning += 1
        for prop in player.housing_market.owned_properties:
            if prop.has_mortgage and prop.mortgage:
                player.housing_market.total_mortgage_paid += prop.mortgage.monthly_payment
                # Interest portion (approximate)
                interest_portion = prop.mortgage.monthly_payment * 0.7  # Rough early-year estimate
                player.housing_market.total_interest_paid += interest_portion
                prop.mortgage.total_interest_paid += interest_portion
                
                # Reduce balance (simplified - real amortization is complex)
                principal_portion = prop.mortgage.monthly_payment * 0.3
                prop.mortgage.current_balance -= principal_portion
                prop.mortgage.months_remaining -= 1
                
                # Check if paid off
                if prop.mortgage.months_remaining <= 0 or prop.mortgage.current_balance <= 0:
                    prop.has_mortgage = False
                    prop.mortgage = None
                    _unlock_achievement(player, "mortgage_paid_off", HOUSING_ACHIEVEMENTS)
    else:
        # Rent payment
        player.housing_market.months_renting += 1
        actual_cost = monthly_cost  # Already adjusted for roommates
        player.housing_market.total_rent_paid_lifetime += actual_cost
        
        # Check for rent regret milestones
        if player.housing_market.total_rent_paid_lifetime >= 50000:
            story = _create_story(
                player,
                "rent_regret",
                HOUSING_STORIES,
                total_rent=player.housing_market.total_rent_paid_lifetime,
                years=player.housing_market.months_renting / 12,
            )
        else:
            story = None
    
    return {
        "monthly_cost": monthly_cost,
        "months_renting": player.housing_market.months_renting,
        "months_owning": player.housing_market.months_owning,
        "total_rent_paid": player.housing_market.total_rent_paid_lifetime,
    }


def apply_property_appreciation(player: Player, years: int = 1) -> Dict[str, Any]:
    """
    Apply annual property appreciation to owned homes.
    """
    appreciation_rate = 0.03  # 3% annual
    
    results = []
    for prop in player.housing_market.owned_properties:
        old_value = prop.current_value
        new_value = old_value * ((1 + appreciation_rate) ** years)
        gain = new_value - old_value
        
        prop.current_value = new_value
        
        results.append({
            "property_id": prop.property_id,
            "old_value": old_value,
            "new_value": new_value,
            "gain": gain,
            "equity": prop.get_equity(),
        })
        
        # Story for significant appreciation
        if gain >= 20000:
            story = _create_story(
                player,
                "property_appreciation",
                HOUSING_STORIES,
                purchase=prop.purchase_price,
                current=new_value,
                gain=gain,
            )
    
    return {"properties": results}


# ==============================================================================
# SUMMARY & UTILITIES
# ==============================================================================

def get_housing_summary(player: Player) -> Dict[str, Any]:
    """
    Get complete housing state summary.
    """
    current_option = None
    if player.housing_market.current_housing:
        current_option = ALL_HOUSING_OPTIONS.get(player.housing_market.current_housing)
    
    return {
        "current_housing": current_option.model_dump() if current_option else None,
        "monthly_cost": player.housing_market.get_current_monthly_housing_cost(),
        "roommates": player.housing_market.roommate_arrangement.model_dump(),
        "owned_properties": [prop.model_dump() for prop in player.housing_market.owned_properties],
        "total_equity": player.housing_market.get_total_equity(),
        "down_payment_saved": player.housing_market.down_payment_saved,
        "down_payment_goal": player.housing_market.down_payment_goal,
        "lifetime_stats": {
            "total_rent_paid": player.housing_market.total_rent_paid_lifetime,
            "total_mortgage_paid": player.housing_market.total_mortgage_paid,
            "total_interest_paid": player.housing_market.total_interest_paid,
            "months_renting": player.housing_market.months_renting,
            "months_owning": player.housing_market.months_owning,
        },
        "decisions": [d.model_dump() for d in player.housing_market.decisions],
        "achievements": [a.model_dump() for a in player.housing_market.achievements],
        "stories": [s.model_dump() for s in player.housing_market.stories[-5:]],  # Last 5
    }


# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

def _create_story(player: Player, story_id: str, story_catalog: List, **kwargs) -> Optional[Dict]:
    """Create and record a story event"""
    story_template = next((s for s in story_catalog if s["story_id"] == story_id), None)
    if not story_template:
        return None
    
    message = story_template["message"].format(**kwargs)
    
    story = HousingStory(
        story_id=f"{story_id}_{len(player.housing_market.stories)}",
        title=story_template["title"],
        message=message,
        timestamp=datetime.now().isoformat(),
        tone=story_template["tone"],
    )
    player.housing_market.stories.append(story)
    
    return story.model_dump()


def _unlock_achievement(player: Player, achievement_id: str, achievement_catalog: List) -> Optional[Dict]:
    """Unlock an achievement"""
    # Check if already unlocked
    if any(a.achievement_id == achievement_id for a in player.housing_market.achievements):
        return None
    
    achievement_template = next((a for a in achievement_catalog if a["achievement_id"] == achievement_id), None)
    if not achievement_template:
        return None
    
    achievement = HousingAchievement(
        achievement_id=achievement_id,
        name=achievement_template["name"],
        description=achievement_template["description"],
        date_earned=datetime.now().isoformat(),
        tier=achievement_template["tier"],
    )
    player.housing_market.achievements.append(achievement)
    
    return achievement.model_dump()
