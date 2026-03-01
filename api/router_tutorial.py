"""
Tutorial Quest API Router

Endpoints for the new player tutorial quest chain.
"""

from __future__ import annotations
from typing import List, Dict, Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from core_domain.store import STORE
from academics.tutorial_service import start_tutorial_quest, submit_tutorial_game, get_quest_progress, skip_tutorial
from academics.tutorial_games import get_tutorial_game, get_new_player_quest

router = APIRouter(prefix="/tutorial", tags=["tutorial"])


# =============================================
# Request/Response Models
# =============================================

class TutorialGameAnswer(BaseModel):
    question_id: str
    choice_id: str


class SubmitTutorialGameRequest(BaseModel):
    player_id: str
    game_id: str
    answers: List[TutorialGameAnswer]


# =============================================
# Endpoints
# =============================================

@router.post("/{player_id}/start")
def start_tutorial_endpoint(player_id: str):
    """
    Start the new player tutorial quest chain.
    Returns quest details and first game.
    """
    player = STORE.require_player(player_id)
    result = start_tutorial_quest(player)
    STORE.put_player(player)
    return result


@router.post("/submit")
def submit_tutorial_game_endpoint(req: SubmitTutorialGameRequest):
    """
    Submit answers for a tutorial game.
    Grades answers and advances quest if passed.
    """
    player = STORE.require_player(req.player_id)
    
    answers = [{"question_id": a.question_id, "choice_id": a.choice_id} for a in req.answers]
    result = submit_tutorial_game(player, req.game_id, answers)
    
    STORE.put_player(player)
    return result


@router.get("/{player_id}/progress")
def get_tutorial_progress_endpoint(player_id: str):
    """Get current tutorial quest progress"""
    player = STORE.require_player(player_id)
    quest = get_new_player_quest()
    return get_quest_progress(player, quest.id)


@router.post("/{player_id}/skip")
def skip_tutorial_endpoint(player_id: str):
    """Allow player to skip tutorial (for testing or returning users)"""
    player = STORE.require_player(player_id)
    player = skip_tutorial(player)
    STORE.put_player(player)
    return {"message": "Tutorial skipped", "tutorial_complete": player.quest_state.tutorial_complete}


@router.get("/quest")
def get_tutorial_quest_info():
    """Get tutorial quest chain structure"""
    quest = get_new_player_quest()
    return quest.model_dump()


@router.get("/games")
def list_tutorial_games():
    """List all available tutorial games"""
    from academics.tutorial_games import TUTORIAL_GAMES
    return {
        "games": [g.model_dump() for g in TUTORIAL_GAMES.values()],
        "total_count": len(TUTORIAL_GAMES),
    }


@router.get("/games/{game_id}")
def get_tutorial_game_detail(game_id: str):
    """Get full tutorial game with questions"""
    game = get_tutorial_game(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Tutorial game not found")
    return game.model_dump()
