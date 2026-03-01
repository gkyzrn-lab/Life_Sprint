"""
Adaptive Difficulty API Router

Endpoints for managing player skill ratings and difficulty preferences.
"""

from __future__ import annotations
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from core_domain.store import STORE
from academics.adaptive_difficulty_service import (
    set_challenge_mode,
    set_practice_mode,
    get_player_performance_dashboard,
)

router = APIRouter(prefix="/difficulty", tags=["difficulty"])


# =============================================
# Request/Response Models
# =============================================

class SetModeRequest(BaseModel):
    enabled: bool


# =============================================
# Endpoints
# =============================================

@router.post("/{player_id}/challenge-mode")
def set_challenge_mode_endpoint(player_id: str, req: SetModeRequest):
    """
    Enable/disable challenge mode for player.
    Challenge mode increases question difficulty by 1 tier.
    """
    player = STORE.require_player(player_id)
    result = set_challenge_mode(player, req.enabled)
    STORE.put_player(player)
    return result


@router.post("/{player_id}/practice-mode")
def set_practice_mode_endpoint(player_id: str, req: SetModeRequest):
    """
    Enable/disable practice mode for player.
    Practice mode decreases difficulty by 1 tier and disables rating changes.
    """
    player = STORE.require_player(player_id)
    result = set_practice_mode(player, req.enabled)
    STORE.put_player(player)
    return result


@router.get("/{player_id}/dashboard")
def get_performance_dashboard(player_id: str):
    """
    Get comprehensive performance dashboard showing:
    - Overall rating and tier
    - Per-domain ratings and stats
    - Win rates and average scores
    - Current streak information
    - Mode preferences (challenge/practice)
    """
    player = STORE.require_player(player_id)
    return get_player_performance_dashboard(player)


@router.get("/{player_id}/stats")
def get_skill_stats(player_id: str):
    """
    Get condensed skill statistics for UI display.
    Lighter-weight version of /dashboard for frequent polling.
    """
    player = STORE.require_player(player_id)
    
    if not player.skill_ratings:
        return {
            "initialized": False,
            "total_games": 0,
            "current_streak": 0,
        }
    
    ratings_data = {}
    for domain, rating in player.skill_ratings.ratings.items():
        ratings_data[domain.value] = {
            "rating": round(rating.rating, 0),
            "tier": rating.difficulty_tier.value,
        }
    
    return {
        "initialized": True,
        "total_games": player.skill_ratings.total_games_played,
        "total_points": player.skill_ratings.total_points_earned,
        "current_streak": player.skill_ratings.current_streak,
        "highest_streak": player.skill_ratings.highest_streak,
        "ratings": ratings_data,
        "challenge_mode": player.skill_ratings.challenge_mode,
        "practice_mode": player.skill_ratings.practice_mode,
    }
