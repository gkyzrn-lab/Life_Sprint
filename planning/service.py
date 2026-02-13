from __future__ import annotations

import random
from typing import List, Optional

from fastapi import HTTPException

from core_domain.player.player_model import Player, HistoryEvent
from core_domain.planning.planning_models import SemesterPlan
from core_domain.config import DEFAULT_BASE_MONTHLY_NONHOUSING_EXPENSES
from core_domain.utils import safe_details

from catalogs.housing import HOUSING_OPTIONS
from catalogs.jobs import JOB_DEFS
from catalogs.activities import ACTIVITIES

from wellbeing.time_budget import compute_weekly_time_load

from planning.emergency_causes import EMERGENCY_CAUSES, EmergencyCause
from planning.penalties import apply_emergency_change_penalty


def _validate_housing(housing_option_id: str) -> None:
    if housing_option_id not in HOUSING_OPTIONS:
        raise HTTPException(status_code=404, detail="Housing option not found")


def _validate_job(job_id: Optional[str]) -> None:
    if job_id is None:
        return
    if job_id == "":
        return
    if job_id not in JOB_DEFS:
        raise HTTPException(status_code=404, detail="Job not found")


def _validate_activities(activities: List[str]) -> None:
    for a in activities:
        if a not in ACTIVITIES:
            raise HTTPException(status_code=404, detail=f"Activity not found: {a}")


def _apply_plan_to_player_state(player: Player, housing_option_id: str, job_id: Optional[str], activities: List[str]) -> None:
    """
    Reflect the plan selections on the player's current state, so forecasts and progression work.
    """
    player.housing = HOUSING_OPTIONS[housing_option_id]

    if job_id is None or job_id == "":
        player.job = None
    else:
        player.job = JOB_DEFS[job_id]

    # monthly baseline expenses = housing + base non-housing expenses
    player.finance.monthly_expenses = float(player.housing.monthly_cost) + float(DEFAULT_BASE_MONTHLY_NONHOUSING_EXPENSES)

    # plan activities stored in plan itself (player.plan)


def forecast_plan(player: Player, housing_option_id: str, job_id: Optional[str], activities: List[str]) -> dict:
    """
    Preview weekly load + warnings without locking the plan.
    Note: This temporarily computes based on proposed choices; it does not permanently change anything.
    """
    _validate_housing(housing_option_id)
    _validate_job(job_id)
    _validate_activities(activities)

    # Create a shallow "preview" by temporarily swapping player fields
    original_housing = player.housing
    original_job = player.job
    original_plan = player.plan

    try:
        # temp apply
        temp_plan = SemesterPlan(
            semester=player.semester,
            housing_option_id=housing_option_id,
            job_id=None if (job_id is None or job_id == "") else job_id,
            activities=activities,
            locked=False,
        )
        player.plan = temp_plan
        _apply_plan_to_player_state(player, housing_option_id, job_id, activities)

        load = compute_weekly_time_load(player)

        warnings: List[str] = []
        if load["overload"] >= 15:
            warnings.append("Severe overload: expect burnout risk and GPA hit later.")
        elif load["overload"] >= 8:
            warnings.append("High overload: stress will rise fast unless you adjust.")
        elif load["overload"] > 0:
            warnings.append("Slight overload: manageable, but watch stress.")

        if player.stats.burnout >= 60:
            warnings.append("You’re already burned out. Overload will punish you more.")

        if player.job and player.job.hours_per_week >= 16 and load["course_hours"] >= 30:
            warnings.append("Heavy job + heavy course load: consider reducing one.")

        return {
            "weekly_load": load,
            "warnings": warnings,
        }
    finally:
        # restore
        player.housing = original_housing
        player.job = original_job
        player.plan = original_plan


def save_plan(player: Player, semester: int, housing_option_id: str, job_id: Optional[str], activities: List[str]) -> SemesterPlan:
    """
    Save a draft plan (not locked).
    If there is a locked plan for this semester, saving is blocked.
    """
    if semester != player.semester:
        raise HTTPException(status_code=400, detail="Plan can only be saved for the current semester.")

    _validate_housing(housing_option_id)
    _validate_job(job_id)
    _validate_activities(activities)

    if player.plan and player.plan.semester == semester and player.plan.locked:
        raise HTTPException(status_code=400, detail="Plan is locked for this semester.")

    plan = SemesterPlan(
        semester=semester,
        housing_option_id=housing_option_id,
        job_id=None if (job_id is None or job_id == "") else job_id,
        activities=activities,
        locked=False,
    )
    player.plan = plan
    _apply_plan_to_player_state(player, housing_option_id, job_id, activities)

    player.history.append(
        HistoryEvent(
            label="Plan Saved (Draft)",
            semester=player.semester,
            details=safe_details(
                {
                    "has_job": 1.0 if (job_id and job_id != "") else 0.0,
                    "activities_count": float(len(activities)),
                }
            ),
        )
    )
    return plan


def lock_plan(player: Player, semester: int) -> SemesterPlan:
    """
    Lock the plan. Required before progressing semester.
    """
    if semester != player.semester:
        raise HTTPException(status_code=400, detail="Plan can only be locked for the current semester.")
    if not player.plan or player.plan.semester != semester:
        raise HTTPException(status_code=400, detail="No plan found to lock for this semester.")

    if player.plan.locked:
        return player.plan

    player.plan.locked = True
    player.history.append(HistoryEvent(label="Plan Locked", semester=player.semester, details={}))
    return player.plan


def emergency_change(
    player: Player,
    *,
    semester: int,
    housing_option_id: Optional[str],
    job_id: Optional[str],
    activities: Optional[List[str]],
    cause_id: Optional[str],
    random_cause: bool,
) -> Player:
    """
    Mid-semester emergency modifications with penalties.
    Requirements:
      - current semester
      - plan exists and locked
      - emergency_tokens > 0
    """
    if semester != player.semester:
        raise HTTPException(status_code=400, detail="Emergency changes only allowed in the current semester.")
    if not player.plan or not player.plan.locked:
        raise HTTPException(status_code=400, detail="Emergency change requires a locked plan.")
    if player.stats.emergency_tokens <= 0:
        raise HTTPException(status_code=400, detail="No emergency tokens available.")

    # choose cause
    cause: Optional[EmergencyCause] = None
    if random_cause:
        cause = random.choice(list(EMERGENCY_CAUSES.values()))
    elif cause_id:
        cause = EMERGENCY_CAUSES.get(cause_id)
        if not cause:
            raise HTTPException(status_code=404, detail="Emergency cause not found.")

    changed_housing = False
    changed_job = False

    # housing change
    if housing_option_id is not None:
        _validate_housing(housing_option_id)
        if player.plan.housing_option_id != housing_option_id:
            player.plan.housing_option_id = housing_option_id
            changed_housing = True

    # job change (allow clearing with "")
    if job_id is not None:
        _validate_job(job_id)
        normalized_job = None if (job_id == "" or job_id is None) else job_id
        if player.plan.job_id != normalized_job:
            player.plan.job_id = normalized_job
            changed_job = True

    # activities update (replace list)
    if activities is not None:
        _validate_activities(activities)
        player.plan.activities = activities

    if not (changed_housing or changed_job or activities is not None):
        raise HTTPException(status_code=400, detail="No changes provided.")

    # apply plan -> player state
    _apply_plan_to_player_state(
        player,
        player.plan.housing_option_id,
        player.plan.job_id,
        player.plan.activities,
    )

    # consume token + penalties
    player.stats.emergency_tokens -= 1
    deltas = apply_emergency_change_penalty(
        player,
        changed_housing=changed_housing,
        changed_job=changed_job,
        cause=cause,
    )

    player.history.append(
        HistoryEvent(
            label="Emergency Change Used",
            semester=player.semester,
            details=deltas,
        )
    )
    if cause:
        player.history.append(HistoryEvent(label=f"Emergency Cause: {cause.name}", semester=player.semester, details={}))

    return player
