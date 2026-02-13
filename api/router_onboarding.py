"""
Onboarding and tutorial API endpoints.

Provides endpoints for:
- Fetching tutorial steps and tooltips
- Tracking tutorial progress
- Retrieving context-specific tutorials
"""

from __future__ import annotations

from typing import List, Dict, Optional, Any
from fastapi import APIRouter, HTTPException

from core_domain.store import STORE
from core_domain.tutorial import (
    TUTORIAL_LIBRARY,
    TOOLTIP_LIBRARY,
    TutorialStep,
    Tooltip,
    get_tutorial_sequence,
    get_context_tutorials,
    get_tooltip,
    get_all_tooltips,
)
from pydantic import BaseModel, Field


router = APIRouter(prefix="/onboarding", tags=["onboarding"])


# ============================================================================
# Request/Response Models
# ============================================================================

class CompleteTutorialRequest(BaseModel):
    player_id: str
    step_id: str


class DismissTooltipRequest(BaseModel):
    player_id: str
    tooltip_id: str


class TutorialProgressResponse(BaseModel):
    player_id: str
    completed_steps: List[str]
    dismissed_tooltips: List[str]
    tutorials_enabled: bool
    completion_percentage: float  # 0-100


# ============================================================================
# Endpoints
# ============================================================================

@router.get("/tutorial-sequence")
def get_recommended_sequence() -> Dict[str, Any]:
    """
    Get the recommended tutorial sequence for first-time players.
    Returns an ordered list of tutorial step IDs.
    """
    sequence = get_tutorial_sequence()
    steps = [TUTORIAL_LIBRARY.get(sid) for sid in sequence]
    steps = [s for s in steps if s]  # filter None
    return {
        "sequence": steps,
        "total_steps": len(steps),
    }


@router.get("/tutorial/{step_id}")
def get_tutorial(step_id: str) -> TutorialStep:
    """
    Fetch a single tutorial step by ID.
    Returns the full tutorial details.
    """
    step = TUTORIAL_LIBRARY.get(step_id)
    if not step:
        raise HTTPException(status_code=404, detail="Tutorial step not found")
    return step


@router.get("/tutorials/context/{context}")
def get_tutorials_by_context(context: str) -> Dict[str, Any]:
    """
    Fetch all tutorials relevant to a specific context.
    Contexts: "player_start", "planning_page", "finance_page", "academics_page", etc.
    """
    tutorials = get_context_tutorials(context)
    if not tutorials:
        return {"context": context, "tutorials": []}
    return {
        "context": context,
        "tutorials": tutorials,
        "count": len(tutorials),
    }


@router.get("/tooltips")
def get_all_tooltips_endpoint() -> Dict[str, Tooltip]:
    """
    Fetch all available tooltips.
    """
    return get_all_tooltips()


@router.get("/tooltip/{tooltip_id}")
def get_tooltip_endpoint(tooltip_id: str) -> Tooltip:
    """
    Fetch a single tooltip by ID.
    """
    tooltip = get_tooltip(tooltip_id)
    if not tooltip:
        raise HTTPException(status_code=404, detail="Tooltip not found")
    return tooltip


@router.post("/tutorial/complete")
def complete_tutorial(req: CompleteTutorialRequest) -> TutorialProgressResponse:
    """
    Mark a tutorial step as completed for a player.
    Useful for tracking onboarding progress.
    """
    player = STORE.get_player(req.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    # Add to completed steps if not already there
    if req.step_id not in player.tutorial_state.completed_steps:
        player.tutorial_state.completed_steps.append(req.step_id)
        STORE.put_player(player)

    # Calculate completion percentage
    sequence = get_tutorial_sequence()
    total_tutorials = len(sequence)
    completed = len(player.tutorial_state.completed_steps)
    completion_pct = (completed / total_tutorials * 100) if total_tutorials > 0 else 0.0

    return TutorialProgressResponse(
        player_id=player.id,
        completed_steps=player.tutorial_state.completed_steps,
        dismissed_tooltips=player.tutorial_state.dismissed_tooltips,
        tutorials_enabled=player.tutorial_state.tutorials_enabled,
        completion_percentage=completion_pct,
    )


@router.post("/tooltip/dismiss")
def dismiss_tooltip(req: DismissTooltipRequest) -> TutorialProgressResponse:
    """
    Mark a tooltip as dismissed (so it won't be shown again).
    """
    player = STORE.get_player(req.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    # Add to dismissed tooltips if not already there
    if req.tooltip_id not in player.tutorial_state.dismissed_tooltips:
        player.tutorial_state.dismissed_tooltips.append(req.tooltip_id)
        STORE.put_player(player)

    # Calculate completion percentage
    sequence = get_tutorial_sequence()
    total_tutorials = len(sequence)
    completed = len(player.tutorial_state.completed_steps)
    completion_pct = (completed / total_tutorials * 100) if total_tutorials > 0 else 0.0

    return TutorialProgressResponse(
        player_id=player.id,
        completed_steps=player.tutorial_state.completed_steps,
        dismissed_tooltips=player.tutorial_state.dismissed_tooltips,
        tutorials_enabled=player.tutorial_state.tutorials_enabled,
        completion_percentage=completion_pct,
    )


@router.get("/{player_id}/progress")
def get_tutorial_progress(player_id: str) -> TutorialProgressResponse:
    """
    Get a player's tutorial progress.
    Returns completed steps, dismissed tooltips, and overall completion percentage.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    sequence = get_tutorial_sequence()
    total_tutorials = len(sequence)
    completed = len(player.tutorial_state.completed_steps)
    completion_pct = (completed / total_tutorials * 100) if total_tutorials > 0 else 0.0

    return TutorialProgressResponse(
        player_id=player.id,
        completed_steps=player.tutorial_state.completed_steps,
        dismissed_tooltips=player.tutorial_state.dismissed_tooltips,
        tutorials_enabled=player.tutorial_state.tutorials_enabled,
        completion_percentage=completion_pct,
    )


@router.post("/{player_id}/enable-tutorials")
def enable_tutorials(player_id: str) -> TutorialProgressResponse:
    """
    Re-enable tutorials for a player (in case they disabled them).
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    player.tutorial_state.tutorials_enabled = True
    STORE.put_player(player)

    sequence = get_tutorial_sequence()
    total_tutorials = len(sequence)
    completed = len(player.tutorial_state.completed_steps)
    completion_pct = (completed / total_tutorials * 100) if total_tutorials > 0 else 0.0

    return TutorialProgressResponse(
        player_id=player.id,
        completed_steps=player.tutorial_state.completed_steps,
        dismissed_tooltips=player.tutorial_state.dismissed_tooltips,
        tutorials_enabled=player.tutorial_state.tutorials_enabled,
        completion_percentage=completion_pct,
    )


@router.post("/{player_id}/disable-tutorials")
def disable_tutorials(player_id: str) -> TutorialProgressResponse:
    """
    Disable tutorials for a player (skip onboarding).
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    player.tutorial_state.tutorials_enabled = False
    STORE.put_player(player)

    sequence = get_tutorial_sequence()
    total_tutorials = len(sequence)
    completed = len(player.tutorial_state.completed_steps)
    completion_pct = (completed / total_tutorials * 100) if total_tutorials > 0 else 0.0

    return TutorialProgressResponse(
        player_id=player.id,
        completed_steps=player.tutorial_state.completed_steps,
        dismissed_tooltips=player.tutorial_state.dismissed_tooltips,
        tutorials_enabled=player.tutorial_state.tutorials_enabled,
        completion_percentage=completion_pct,
    )
