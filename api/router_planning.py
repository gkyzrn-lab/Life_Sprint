from __future__ import annotations

from fastapi import APIRouter, HTTPException

from api.deps import require_player
from planning.dtos import ForecastPlanRequest, SavePlanRequest, LockPlanRequest, EmergencyChangeRequest
from planning.service import forecast_plan, save_plan, lock_plan, emergency_change
from planning.emergency_causes import EMERGENCY_CAUSES

router = APIRouter(prefix="/planning", tags=["planning"])


@router.get("/emergency-causes")
def list_emergency_causes():
    return {k: v.__dict__ for k, v in EMERGENCY_CAUSES.items()}


@router.post("/forecast")
def plan_forecast(req: ForecastPlanRequest):
    p = require_player(req.player_id)
    result = forecast_plan(p, req.housing_option_id, req.job_id, req.activities)
    return {
        "player_id": req.player_id,
        "semester": p.semester,
        "housing_option_id": req.housing_option_id,
        "job_id": req.job_id,
        "activities": req.activities,
        "weekly_load": result["weekly_load"],
        "warnings": result["warnings"],
    }


@router.post("/save")
def plan_save(req: SavePlanRequest):
    p = require_player(req.player_id)
    plan = save_plan(p, req.semester, req.housing_option_id, req.job_id, req.activities)
    return plan.model_dump()


@router.post("/lock")
def plan_lock(req: LockPlanRequest):
    p = require_player(req.player_id)
    plan = lock_plan(p, req.semester)
    return plan.model_dump()


@router.post("/emergency-change")
def plan_emergency_change(req: EmergencyChangeRequest):
    p = require_player(req.player_id)
    updated = emergency_change(
        p,
        semester=req.semester,
        housing_option_id=req.housing_option_id,
        job_id=req.job_id,
        activities=req.activities,
        cause_id=req.cause_id,
        random_cause=req.random_cause,
    )
    return updated
