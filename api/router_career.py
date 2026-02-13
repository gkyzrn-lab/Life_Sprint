"""Career API routes."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from api.deps import require_player
from career.service import (
    accept_job,
    attempt_promotion,
    receive_raise,
    apply_therapy_burnout_reduction,
    get_career_summary,
    update_performance_and_burnout,
)

router = APIRouter(prefix="/career", tags=["career"])


class AcceptJobRequest(BaseModel):
    player_id: str
    job_id: str


class PromotionCheckRequest(BaseModel):
    player_id: str


class RaiseRequest(BaseModel):
    player_id: str
    amount: float


class BurnoutTherapyRequest(BaseModel):
    player_id: str
    therapy_effectiveness: float = 1.0


@router.post("/accept-job")
def career_accept_job(req: AcceptJobRequest):
    """Accept a job offer."""
    try:
        player = require_player(req.player_id)
        result = accept_job(player, req.job_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/check-promotion")
def career_attempt_promotion(req: PromotionCheckRequest):
    """Check if player is eligible for promotion and promote if so."""
    player = require_player(req.player_id)
    result = attempt_promotion(player)
    return result


@router.post("/raise")
def career_receive_raise(req: RaiseRequest):
    """Apply a salary raise."""
    player = require_player(req.player_id)
    result = receive_raise(player, req.amount)
    return result


@router.post("/update-semester")
def career_update_semester(player_id: str):
    """
    Called at end of semester to update performance/burnout.
    Should be called after all semester actions are complete.
    """
    player = require_player(player_id)
    result = update_performance_and_burnout(player)
    return result


@router.post("/burnout-therapy")
def career_therapy_reduce_burnout(req: BurnoutTherapyRequest):
    """Apply therapy to reduce burnout."""
    player = require_player(req.player_id)
    result = apply_therapy_burnout_reduction(player, req.therapy_effectiveness)
    return result


@router.get("/{player_id}/summary")
def career_get_summary(player_id: str):
    """Get complete career summary."""
    player = require_player(player_id)
    return get_career_summary(player)


@router.get("/{player_id}/earnings")
def career_get_earnings(player_id: str):
    """Get semester earnings based on current job."""
    player = require_player(player_id)
    
    if not player.career.current_job_id or not player.job:
        return {"earnings": 0.0, "reason": "no_job"}
    
    earnings = player.career.current_salary * player.job.hours_per_week * 16
    
    return {
        "job_title": player.career.current_job_title,
        "hourly_effective": float(player.career.current_salary / 2080),  # 2080 hours/year
        "hours_per_week": player.job.hours_per_week,
        "weeks_per_semester": 16,
        "gross_semester_earnings": float(earnings),
        "performance_multiplier": float(player.career.performance_rating / 50),  # perf affects earnings
    }


@router.get("/{player_id}/history")
def career_get_history(player_id: str):
    """Get career history (job changes, promotions, raises)."""
    player = require_player(player_id)
    
    return {
        "total_entries": len(player.career.history),
        "history": [
            {
                "event_type": h.event_type,
                "job_title": h.job_title,
                "semester": h.semester,
                "salary_before": float(h.salary_before),
                "salary_after": float(h.salary_after),
                "change": float(h.salary_after - h.salary_before),
                "reason": h.reason,
            }
            for h in player.career.history
        ],
    }
