"""
Side Gigs & Freelancing API Router

Endpoints for managing gigs, passive income, and businesses.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

from core_domain.store import STORE
from core_domain.side_gigs.side_gigs_models import (
    GigType,
    PassiveIncomeType,
    BusinessType,
)
from side_gigs import service as side_gigs_service
from catalogs.side_gigs import (
    GIG_OPPORTUNITIES,
    PASSIVE_INCOME_OPTIONS,
    BUSINESS_OPTIONS,
    SIDE_GIG_ACHIEVEMENTS,
    SIDE_GIG_STORIES,
)

router = APIRouter(prefix="/side-gigs", tags=["side-gigs"])


# =============================================================================
# REQUEST MODELS
# =============================================================================

class StartGigRequest(BaseModel):
    player_id: str
    gig_id: str


class WorkGigRequest(BaseModel):
    player_id: str
    gig_id: str
    hours: float = Field(..., ge=0.5, le=12, description="Hours worked (0.5-12)")


class StartPassiveIncomeRequest(BaseModel):
    player_id: str
    income_type: PassiveIncomeType
    name: str = Field(..., min_length=1, max_length=100)


class UpdatePassiveIncomeRequest(BaseModel):
    player_id: str
    months_passed: int = Field(default=1, ge=1, le=12)


class StartBusinessRequest(BaseModel):
    player_id: str
    business_type: BusinessType
    name: str = Field(..., min_length=1, max_length=100)


class UpdateBusinessesRequest(BaseModel):
    player_id: str
    months_passed: int = Field(default=1, ge=1, le=12)


# =============================================================================
# GIG ECONOMY ENDPOINTS
# =============================================================================

@router.get("/gigs")
def get_all_gigs():
    """Get all available gig opportunities"""
    return {
        "gigs": [
            {
                "gig_id": gig_id,
                "name": gig.name,
                "gig_type": gig.gig_type.value,
                "description": gig.description,
                "min_age": gig.min_age,
                "requires_car": gig.requires_car,
                "hourly_rate_range": f"${gig.min_hourly_rate:.0f}-${gig.max_hourly_rate:.0f}",
                "avg_hourly_rate": gig.avg_hourly_rate,
                "flexible_hours": gig.flexible_hours,
                "startup_cost": gig.startup_cost,
                "ongoing_costs_per_month": gig.ongoing_costs_per_month,
                "skill_requirements": gig.skill_requirements,
                "portfolio_boost": gig.portfolio_boost,
            }
            for gig_id, gig in GIG_OPPORTUNITIES.items()
        ]
    }


@router.get("/gigs/{gig_id}")
def get_gig_details(gig_id: str):
    """Get detailed information about a specific gig"""
    if gig_id not in GIG_OPPORTUNITIES:
        raise HTTPException(status_code=404, detail="Gig not found")
    
    gig = GIG_OPPORTUNITIES[gig_id]
    
    return {
        "gig_id": gig_id,
        "name": gig.name,
        "gig_type": gig.gig_type.value,
        "description": gig.description,
        "requirements": {
            "min_age": gig.min_age,
            "requires_car": gig.requires_car,
            "requires_smartphone": gig.requires_smartphone,
            "skill_requirements": gig.skill_requirements,
            "startup_cost": gig.startup_cost,
        },
        "income": {
            "min_hourly_rate": gig.min_hourly_rate,
            "avg_hourly_rate": gig.avg_hourly_rate,
            "max_hourly_rate": gig.max_hourly_rate,
            "ongoing_costs_per_month": gig.ongoing_costs_per_month,
        },
        "time": {
            "flexible_hours": gig.flexible_hours,
            "min_hours_per_week": gig.min_hours_per_week,
            "max_hours_per_week": gig.max_hours_per_week,
        },
        "impact": {
            "stress_per_hour": gig.stress_per_hour,
            "energy_per_hour": gig.energy_per_hour,
            "skill_improvement_per_hour": gig.skill_improvement_per_hour,
            "portfolio_boost": gig.portfolio_boost,
        },
    }


@router.post("/gigs/check-eligibility")
def check_gig_eligibility(request: StartGigRequest):
    """Check if player can start a gig"""
    player = STORE.get_player(request.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    can_start, reason = side_gigs_service.can_start_gig(player, request.gig_id)
    
    return {
        "can_start": can_start,
        "reason": reason,
        "gig_id": request.gig_id,
    }


@router.post("/gigs/start")
def start_gig(request: StartGigRequest):
    """Start a new gig"""
    player = STORE.get_player(request.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    try:
        active_gig, story = side_gigs_service.start_gig(player, request.gig_id)
        STORE.put_player(player)
        
        return {
            "success": True,
            "active_gig": {
                "gig_id": active_gig.gig_id,
                "started_date": active_gig.started_date.isoformat(),
                "customer_rating": active_gig.customer_rating,
            },
            "story": story,
            "balance": player.finance.balance,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/gigs/work")
def work_gig(request: WorkGigRequest):
    """Work a gig for X hours"""
    player = STORE.get_player(request.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    try:
        earnings, expenses, story = side_gigs_service.work_gig(
            player,
            request.gig_id,
            request.hours
        )
        STORE.put_player(player)
        
        return {
            "success": True,
            "hours_worked": request.hours,
            "gross_earnings": earnings + expenses,
            "expenses": expenses,
            "net_earnings": earnings,
            "story": story,
            "player_state": {
                "balance": player.finance.balance,
                "stress_level": player.health.stress_level,
                "energy_level": player.stats.energy_level,
                "total_gig_income": player.side_gigs.total_gig_income,
                "hours_this_week": player.side_gigs.gig_hours_this_week,
            },
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{player_id}/gigs/active")
def get_active_gigs(player_id: str):
    """Get player's active gigs"""
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return {
        "active_gigs": [
            {
                "gig_id": gig.gig_id,
                "name": GIG_OPPORTUNITIES[gig.gig_id].name if gig.gig_id in GIG_OPPORTUNITIES else gig.gig_id,
                "total_hours_worked": gig.total_hours_worked,
                "total_earned": gig.total_earned,
                "hours_this_week": gig.hours_this_week,
                "earnings_this_week": gig.earnings_this_week,
                "customer_rating": gig.customer_rating,
                "avg_hourly_rate": gig.total_earned / gig.total_hours_worked if gig.total_hours_worked > 0 else 0,
            }
            for gig in player.side_gigs.active_gigs if gig.is_active
        ]
    }


# =============================================================================
# PASSIVE INCOME ENDPOINTS
# =============================================================================

@router.get("/passive-income/options")
def get_passive_income_options():
    """Get all passive income options"""
    return {
        "options": [
            {
                "key": key,
                "income_type": config["income_type"].value,
                "name": config["name"],
                "description": config["description"],
                "startup_cost": config["startup_cost"],
                "initial_time_investment_hours": config["initial_time_investment_hours"],
                "hours_per_month_required": config["hours_per_month_required"],
                "months_to_monetization": config["months_to_monetization"],
                "success_rate": f"{config['success_rate'] * 100:.0f}%",
                "skills_required": config["skills_required"],
            }
            for key, config in PASSIVE_INCOME_OPTIONS.items()
        ]
    }


@router.post("/passive-income/start")
def start_passive_income(request: StartPassiveIncomeRequest):
    """Start a passive income stream"""
    player = STORE.get_player(request.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    try:
        stream, story = side_gigs_service.start_passive_income_stream(
            player,
            request.income_type,
            request.name
        )
        STORE.put_player(player)
        
        return {
            "success": True,
            "stream": {
                "stream_id": stream.stream_id,
                "name": stream.name,
                "income_type": stream.income_type.value,
                "startup_cost": stream.startup_cost,
                "current_monthly_income": stream.current_monthly_income,
            },
            "story": story,
            "balance": player.finance.balance,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/passive-income/update")
def update_passive_income(request: UpdatePassiveIncomeRequest):
    """Update all passive income streams (call monthly)"""
    player = STORE.get_player(request.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    stories = side_gigs_service.update_passive_income_streams(player, request.months_passed)
    STORE.put_player(player)
    
    return {
        "success": True,
        "months_passed": request.months_passed,
        "stories": stories,
        "monthly_passive_income": player.side_gigs.monthly_passive_income,
        "total_passive_income": player.side_gigs.total_passive_income,
        "balance": player.finance.balance,
    }


@router.get("/{player_id}/passive-income/streams")
def get_passive_income_streams(player_id: str):
    """Get player's passive income streams"""
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return {
        "streams": [
            {
                "stream_id": stream.stream_id,
                "name": stream.name,
                "income_type": stream.income_type.value,
                "months_active": stream.months_active,
                "current_monthly_income": stream.current_monthly_income,
                "total_earned": stream.total_earned,
                "followers_subscribers": stream.followers_subscribers,
                "monthly_views_visits": stream.monthly_views_visits,
                "monetized": stream.monetized,
            }
            for stream in player.side_gigs.passive_income_streams if stream.is_active
        ],
        "total_monthly_income": player.side_gigs.monthly_passive_income,
    }


# =============================================================================
# BUSINESS ENDPOINTS
# =============================================================================

@router.get("/businesses/options")
def get_business_options():
    """Get all business options"""
    return {
        "options": [
            {
                "key": key,
                "business_type": config["business_type"].value,
                "name": config["name"],
                "description": config["description"],
                "startup_cost": config["startup_cost"],
                "monthly_fixed_costs": config["monthly_fixed_costs"],
                "initial_time_investment_hours": config["initial_time_investment_hours"],
                "ongoing_hours_per_week": config["ongoing_hours_per_week"],
                "breakeven_months": config["breakeven_months"],
                "success_rate": f"{config['success_rate'] * 100:.0f}%",
                "skills_required": config["skills_required"],
            }
            for key, config in BUSINESS_OPTIONS.items()
        ]
    }


@router.post("/businesses/start")
def start_business(request: StartBusinessRequest):
    """Start a small business"""
    player = STORE.get_player(request.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    try:
        business, story = side_gigs_service.start_business(
            player,
            request.business_type,
            request.name
        )
        STORE.put_player(player)
        
        return {
            "success": True,
            "business": {
                "business_id": business.business_id,
                "name": business.name,
                "business_type": business.business_type.value,
                "startup_cost": business.startup_cost,
                "status": business.status,
            },
            "story": story,
            "balance": player.finance.balance,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/businesses/update")
def update_businesses(request: UpdateBusinessesRequest):
    """Update all businesses (call monthly)"""
    player = STORE.get_player(request.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    stories = side_gigs_service.update_businesses(player, request.months_passed)
    STORE.put_player(player)
    
    return {
        "success": True,
        "months_passed": request.months_passed,
        "stories": stories,
        "monthly_business_income": player.side_gigs.monthly_business_income,
        "total_business_income": player.side_gigs.total_business_income,
        "balance": player.finance.balance,
    }


@router.get("/{player_id}/businesses")
def get_businesses(player_id: str):
    """Get player's businesses"""
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return {
        "businesses": [
            {
                "business_id": business.business_id,
                "name": business.name,
                "business_type": business.business_type.value,
                "months_in_operation": business.months_in_operation,
                "monthly_revenue": business.monthly_revenue,
                "monthly_expenses": business.monthly_expenses,
                "monthly_profit": business.monthly_revenue - business.monthly_expenses,
                "total_revenue": business.total_revenue,
                "total_expenses": business.total_expenses,
                "total_profit": business.total_revenue - business.total_expenses,
                "is_profitable": business.is_profitable,
                "status": business.status,
                "customer_count": business.customer_count,
                "customer_satisfaction": business.customer_satisfaction,
            }
            for business in player.side_gigs.businesses if business.is_active
        ]
    }


# =============================================================================
# SUMMARY & TRACKING ENDPOINTS
# =============================================================================

@router.get("/{player_id}/summary")
def get_side_gigs_summary(player_id: str):
    """Get complete summary of side hustles"""
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return side_gigs_service.get_side_gigs_summary(player)


@router.get("/{player_id}/achievements")
def get_side_gig_achievements(player_id: str):
    """Get side gig achievements"""
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    unlocked = [
        {
            **achievement,
            "unlocked": achievement["achievement_id"] in player.side_gigs.side_gig_achievements_unlocked,
        }
        for achievement in SIDE_GIG_ACHIEVEMENTS
    ]
    
    return {"achievements": unlocked}


@router.get("/{player_id}/stories")
def get_side_gig_stories(player_id: str):
    """Get recent side gig stories"""
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    # Return last 10 stories
    return {
        "stories": player.side_gigs.side_gig_stories[-10:]
    }


@router.post("/{player_id}/check-diversification")
def check_income_diversification(player_id: str):
    """Check if player has diversified income (achievement)"""
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    side_gigs_service.check_diversified_income(player)
    STORE.put_player(player)
    
    return {
        "success": True,
        "diversified": "diversified_income" in player.side_gigs.side_gig_achievements_unlocked,
    }
