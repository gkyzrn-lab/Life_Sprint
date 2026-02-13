"""
Housing Market API Router

Endpoints for housing decisions, rent vs buy analysis, and property management.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Literal

from core_domain.store import STORE
from housing_market.service import (
    apply_annual_rent_increase,
    choose_housing,
    add_roommate,
    trigger_roommate_conflict,
    calculate_buy_vs_rent,
    save_for_down_payment,
    purchase_home,
    calculate_commute_impact,
    process_monthly_housing_costs,
    apply_property_appreciation,
    get_housing_summary,
)
from catalogs.housing_market import ALL_HOUSING_OPTIONS

router = APIRouter(prefix="/housing-market", tags=["housing_market"])


# ==============================================================================
# REQUEST MODELS
# ==============================================================================

class ChooseHousingRequest(BaseModel):
    player_id: str
    option_id: str
    roommate_config: Literal["alone", "one_roommate", "two_roommates"] = "alone"


class AddRoommateRequest(BaseModel):
    player_id: str


class BuyVsRentRequest(BaseModel):
    player_id: str
    option_id: str
    mortgage_product: Literal["conventional_30", "conventional_15", "fha_loan"] = "conventional_30"
    years: int = 5


class SaveDownPaymentRequest(BaseModel):
    player_id: str
    amount: float
    goal_property_id: str


class PurchaseHomeRequest(BaseModel):
    player_id: str
    option_id: str
    mortgage_product: Literal["conventional_30", "conventional_15", "fha_loan"] = "conventional_30"


class CommuteAnalysisRequest(BaseModel):
    option_id: str


# ==============================================================================
# HOUSING BROWSING & SELECTION
# ==============================================================================

@router.get("/options")
def get_housing_options():
    """
    List all available housing options (NYC + NJ).
    """
    return {
        "options": [opt.model_dump() for opt in ALL_HOUSING_OPTIONS.values()],
        "count": len(ALL_HOUSING_OPTIONS),
        "locations": ["nyc_manhattan", "nyc_brooklyn", "nyc_queens", "nj_jersey_city", "nj_hoboken", "nj_newark"],
    }


@router.get("/options/{option_id}")
def get_housing_option(option_id: str):
    """
    Get details for a specific housing option.
    """
    if option_id not in ALL_HOUSING_OPTIONS:
        raise HTTPException(status_code=404, detail=f"Housing option {option_id} not found")
    
    option = ALL_HOUSING_OPTIONS[option_id]
    return {"option": option.model_dump()}


@router.post("/choose")
def choose_housing_endpoint(request: ChooseHousingRequest):
    """
    Choose a housing option (rent).
    """
    player = STORE.get_player(request.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    result = choose_housing(player, request.option_id, request.roommate_config)
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    STORE.put_player(player)
    return result


# ==============================================================================
# RENT & MARKET OPERATIONS
# ==============================================================================

@router.post("/rent-increase")
def apply_rent_increase(player_id: str):
    """
    Apply annual rent increase (5-8% inflation).
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    result = apply_annual_rent_increase(player)
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    STORE.put_player(player)
    return result


@router.post("/monthly-payment")
def process_monthly_payment(player_id: str):
    """
    Process monthly rent or mortgage payment.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    result = process_monthly_housing_costs(player)
    STORE.put_player(player)
    return result


# ==============================================================================
# ROOMMATE MANAGEMENT
# ==============================================================================

@router.post("/roommate/add")
def add_roommate_endpoint(request: AddRoommateRequest):
    """
    Add a roommate to current housing.
    """
    player = STORE.get_player(request.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    result = add_roommate(player)
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    STORE.put_player(player)
    return result


@router.post("/roommate/conflict")
def trigger_conflict(player_id: str):
    """
    Trigger a roommate conflict event (simulation).
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    result = trigger_roommate_conflict(player)
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    STORE.put_player(player)
    return result


# ==============================================================================
# BUY VS RENT ANALYSIS
# ==============================================================================

@router.post("/buy-vs-rent")
def buy_vs_rent_analysis(request: BuyVsRentRequest):
    """
    Compare buying vs renting for a specific property.
    """
    player = STORE.get_player(request.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    try:
        analysis = calculate_buy_vs_rent(
            player,
            request.option_id,
            request.mortgage_product,
            request.years,
        )
        STORE.put_player(player)  # Save story
        return {"analysis": analysis.model_dump()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# ==============================================================================
# HOME PURCHASE
# ==============================================================================

@router.post("/down-payment/save")
def save_down_payment(request: SaveDownPaymentRequest):
    """
    Save money toward down payment.
    """
    player = STORE.get_player(request.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    result = save_for_down_payment(player, request.amount, request.goal_property_id)
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    STORE.put_player(player)
    return result


@router.post("/purchase")
def purchase_home_endpoint(request: PurchaseHomeRequest):
    """
    Purchase a home with mortgage.
    """
    player = STORE.get_player(request.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    result = purchase_home(player, request.option_id, request.mortgage_product)
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    STORE.put_player(player)
    return result


@router.get("/{player_id}/down-payment")
def get_down_payment_status(player_id: str):
    """
    Get down payment savings progress.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    saved = player.housing_market.down_payment_saved
    goal = player.housing_market.down_payment_goal
    percent = (saved / goal * 100) if goal > 0 else 0
    
    return {
        "saved": saved,
        "goal": goal,
        "percent_complete": percent,
        "remaining": goal - saved if goal > 0 else 0,
    }


# ==============================================================================
# PROPERTY MANAGEMENT
# ==============================================================================

@router.post("/property/appreciation")
def apply_appreciation(player_id: str, years: int = 1):
    """
    Apply property appreciation to owned homes.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    result = apply_property_appreciation(player, years)
    STORE.put_player(player)
    return result


@router.get("/{player_id}/properties")
def get_owned_properties(player_id: str):
    """
    Get all properties owned by player.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return {
        "properties": [prop.model_dump() for prop in player.housing_market.owned_properties],
        "total_equity": player.housing_market.get_total_equity(),
        "count": len(player.housing_market.owned_properties),
    }


# ==============================================================================
# COMMUTE ANALYSIS
# ==============================================================================

@router.post("/commute-analysis")
def commute_analysis(request: CommuteAnalysisRequest):
    """
    Calculate commute time and cost impact for a housing option.
    """
    if request.option_id not in ALL_HOUSING_OPTIONS:
        raise HTTPException(status_code=404, detail="Housing option not found")
    
    housing_option = ALL_HOUSING_OPTIONS[request.option_id]
    
    # Dummy player for calculation (doesn't need to be real)
    from core_domain.player.player_model import Player
    dummy_player = Player(player_id="dummy", name="Dummy")
    
    result = calculate_commute_impact(dummy_player, housing_option)
    return result


# ==============================================================================
# SUMMARY & DASHBOARD
# ==============================================================================

@router.get("/{player_id}/summary")
def get_summary(player_id: str):
    """
    Get complete housing state summary.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return get_housing_summary(player)


@router.get("/{player_id}/achievements")
def get_achievements(player_id: str):
    """
    Get housing achievements.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return {
        "achievements": [a.model_dump() for a in player.housing_market.achievements],
        "count": len(player.housing_market.achievements),
    }


@router.get("/{player_id}/stories")
def get_stories(player_id: str, limit: int = 10):
    """
    Get recent housing stories.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    stories = player.housing_market.stories[-limit:]
    return {
        "stories": [s.model_dump() for s in stories],
        "count": len(stories),
    }
