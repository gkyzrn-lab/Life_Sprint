from __future__ import annotations

from fastapi import APIRouter, HTTPException

from api.deps import require_player
from catalogs.colleges import COLLEGES
from academics.curriculum import CURRICULUM

from wellbeing.time_budget import compute_weekly_time_load
from wellbeing.stress_burnout import apply_time_pressure, update_burnout
from wellbeing.activity_effects import apply_activity_effects

from finance.service import accrue_interest_in_school, borrow_for_semester
from core_domain.player.player_model import HistoryEvent
from core_domain.utils import safe_details

router = APIRouter(prefix="/progress", tags=["progression"])


def _semester_tuition(player) -> float:
    college = COLLEGES.get(player.college_id)
    if not college:
        return 0.0
    yearly = float(college.get("base_tuition_per_year", 0.0))
    return yearly / 2.0  # 2 semesters/year


def _require_locked_plan(player):
    if not player.plan or not player.plan.locked:
        raise HTTPException(status_code=400, detail="You must lock a semester plan before progressing.")


@router.post("/advance")
def advance_semester(player_id: str):
    p = require_player(player_id)
    _require_locked_plan(p)

    # sanity: must have curriculum for current semester
    sem = CURRICULUM.get(p.college_id, {}).get(p.major_id, {}).get(int(p.semester))
    if not sem:
        raise HTTPException(status_code=404, detail="Curriculum missing for current semester")

    # 1) Apply activity effects (cost + stress/happiness deltas)
    apply_activity_effects(p)

    # 2) Time load -> stress pressure, then burnout update
    load = compute_weekly_time_load(p)
    apply_time_pressure(p, load)
    update_burnout(p)

    # 3) Tuition payment (subtract scholarship), borrow if needed
    tuition = _semester_tuition(p)
    scholarship = float(p.finance.scholarship_per_semester or 0.0)
    due = max(0.0, tuition - scholarship)

    p.finance.tuition_per_semester = float(tuition)

    # Pay tuition from balance; if short, borrow to cover the gap
    if due > 0:
        if p.finance.balance >= due:
            p.finance.balance -= due
            borrowed = 0.0
        else:
            gap = due - float(p.finance.balance)
            # zero out balance, borrow gap, then pay
            p.finance.balance = 0.0
            borrowed = borrow_for_semester(p, gap)
            # borrowed goes into balance; immediately pay tuition
            pay_now = min(float(p.finance.balance), gap)
            p.finance.balance -= pay_now
    else:
        borrowed = 0.0

    # 4) In-school interest accrual for the semester duration (4 months)
    accrue_interest_in_school(p, months=4)

    # 5) Log
    p.history.append(
        HistoryEvent(
            label="Semester End Processed",
            semester=p.semester,
            details=safe_details(
                {
                    "weekly_total_hours": float(load["total_hours"]),
                    "weekly_overload": float(load["overload"]),
                    "tuition": float(tuition),
                    "scholarship": float(scholarship),
                    "tuition_due": float(due),
                    "borrowed_for_tuition_gap": float(borrowed),
                }
            ),
        )
    )

    # 6) Progress semester/year
    p.semester += 1
    if p.semester in (3, 5, 7):
        p.year_in_school += 1

    # refresh emergency tokens each semester (simple v1)
    p.stats.emergency_tokens = max(1, int(p.stats.emergency_tokens))

    # unlock plan for next semester (player must create/lock a new one)
    p.plan = None

    # graduation flag (simple)
    graduated = p.semester >= 9

    return {
        "player_id": p.id,
        "graduated": graduated,
        "new_semester": p.semester,
        "year_in_school": p.year_in_school,
        "player": p,
    }
