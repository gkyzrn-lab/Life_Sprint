# api/router_progression.py  (IMPROVED)
# ================================================================
# KEY CHANGES vs original:
#   1. Burnout consequence: severe burnout forces a course drop
#   2. Health degradation: overloaded semesters damage health score
#   3. Sleep/stress feedback loop: overload reduces sleep quality
#   4. Scholarship auto-award: GPA-based scholarships applied each semester
#   5. Year tracking fixed: was wrong (3,5,7) → now correctly every 2 semesters
#   6. Monthly expense drain: deducted each month of the semester (4x)
#   7. Network score: grows from job/activity each semester
#   8. Graduation debt snapshot: captured when player finishes semester 8
#   9. Better error messages and response payload
# ================================================================

from __future__ import annotations

from fastapi import APIRouter, HTTPException
from api.deps import require_player
from catalogs.colleges import COLLEGES
from catalogs.majors import MAJORS
from academics.curriculum import CURRICULUM
from wellbeing.time_budget import compute_weekly_time_load
from wellbeing.stress_burnout import apply_time_pressure, update_burnout
from wellbeing.activity_effects import apply_activity_effects
from finance.service import accrue_interest_in_school, borrow_for_semester
from core_domain.player.player_model import HistoryEvent, BurnoutLevel
from core_domain.utils import safe_details
from core_domain.store import STORE

router = APIRouter(prefix="/progress", tags=["progression"])

# ── constants ────────────────────────────────────────────────────
MONTHS_PER_SEMESTER = 4
SCHOLARSHIP_THRESHOLDS = [
    (3.8, 2000.0, "Merit Excellence (GPA ≥ 3.8)"),
    (3.5, 1000.0, "Merit Award (GPA ≥ 3.5)"),
    (3.0,  500.0, "Dean's List (GPA ≥ 3.0)"),
]
NEED_BASED_INCOME_THRESHOLD = 50_000.0
NEED_BASED_AMOUNT = 1_500.0


# ── helpers ──────────────────────────────────────────────────────

def _semester_tuition(player) -> float:
    college = COLLEGES.get(player.college_id)
    if not college:
        return 0.0
    yearly = float(college.get("base_tuition_per_year", 0.0))
    major = MAJORS.get(player.major_id)
    if major and "tuition_multiplier" in major:
        yearly *= float(major["tuition_multiplier"])
    return yearly / 2.0


def _require_locked_plan(player):
    if not player.plan or not player.plan.locked:
        raise HTTPException(
            status_code=400,
            detail="You must lock a semester plan before progressing. Go to the Planning tab first."
        )


def _require_exam_passed(player):
    """Player must pass semester exam before advancing."""
    if player.semester not in player.semester_exams_passed:
        raise HTTPException(
            status_code=400,
            detail=f"You must pass the Semester {player.semester} exam before advancing. "
                   f"Score ≥ 70% to proceed."
        )


def _apply_health_effects(player, load: dict) -> dict:
    """
    Each semester, health and sleep are affected by overload and stress.
    Returns a dict of deltas for the response payload.
    """
    overload = float(load.get("overload", 0.0))
    stats = player.stats

    # Sleep degrades with overload (every 5 hrs overload = -2 sleep quality)
    sleep_delta = -(overload / 5.0) * 2.0
    # Health: stress drains it, happiness restores it slightly
    health_delta = -(stats.stress / 50.0) * 3.0 + (stats.happiness / 100.0) * 1.5
    # Network grows from job network_gain + activity social modifiers
    network_delta = 0.0
    if player.job:
        network_delta += float(player.job.network_gain)
    if player.housing:
        network_delta += float(player.housing.social_modifier) * 0.5

    # Clamp everything to [0, 100]
    stats.sleep_quality = max(0.0, min(100.0, stats.sleep_quality + sleep_delta))
    stats.health = max(0.0, min(100.0, stats.health + health_delta))
    stats.network_score = max(0.0, min(100.0, stats.network_score + network_delta))

    return {
        "sleep_delta": round(sleep_delta, 2),
        "health_delta": round(health_delta, 2),
        "network_delta": round(network_delta, 2),
    }


def _apply_scholarships(player) -> float:
    """
    Award GPA-based and need-based scholarships.
    Returns total amount awarded this semester.
    """
    from core_domain.player.player_model import ScholarshipRecord
    awarded = 0.0
    gpa = player.stats.gpa

    # Merit scholarships (only award highest applicable tier)
    for min_gpa, amount, reason in SCHOLARSHIP_THRESHOLDS:
        if gpa >= min_gpa:
            record = ScholarshipRecord(
                name=reason,
                semester=player.semester,
                amount=amount,
                reason=f"GPA {gpa:.2f} ≥ {min_gpa}",
            )
            player.finance.scholarship_history.append(record)
            player.finance.balance += amount
            awarded += amount
            break  # only highest tier

    # Need-based scholarship
    if player.parent_income < NEED_BASED_INCOME_THRESHOLD:
        record = ScholarshipRecord(
            name="Need-Based Grant",
            semester=player.semester,
            amount=NEED_BASED_AMOUNT,
            reason=f"Parent income ${player.parent_income:,.0f} < threshold",
        )
        player.finance.scholarship_history.append(record)
        player.finance.balance += NEED_BASED_AMOUNT
        awarded += NEED_BASED_AMOUNT

    player.finance.scholarship_per_semester = awarded
    return awarded


def _apply_burnout_consequence(player) -> dict:
    """
    If severely burned out, drop the most recent incomplete course.
    Returns info about what happened.
    """
    if not player.stats.is_burned_out:
        return {"burnout_consequence": None}

    # Find courses for current semester that aren't completed
    sem_data = CURRICULUM.get(player.college_id, {}).get(player.major_id, {}).get(player.semester)
    if not sem_data:
        return {"burnout_consequence": None}

    incomplete = [
        c for c in sem_data.courses
        if c.course_id not in player.completed_courses
    ]

    if not incomplete:
        return {"burnout_consequence": None}

    # Drop the highest-credit incomplete course
    to_drop = max(incomplete, key=lambda c: c.credits)
    player.dropped_courses.append({
        "course_id": to_drop.course_id,
        "course_name": to_drop.name,
        "semester": player.semester,
        "reason": "severe_burnout",
    })

    # Partial stress relief from dropping
    player.stats.burnout = max(0.0, player.stats.burnout - 20.0)
    player.stats.stress = max(0.0, player.stats.stress - 10.0)

    return {
        "burnout_consequence": {
            "dropped_course": to_drop.course_id,
            "course_name": to_drop.name,
            "credits_lost": to_drop.credits,
            "message": f"⚠️ Severe burnout! You were forced to drop {to_drop.name}.",
        }
    }


def _deduct_monthly_expenses(player) -> float:
    """Deduct living expenses for each month of the semester. Borrow if broke."""
    total_expenses = 0.0
    for _ in range(MONTHS_PER_SEMESTER):
        monthly = float(player.finance.monthly_expenses)
        total_expenses += monthly
        if player.finance.balance >= monthly:
            player.finance.balance -= monthly
        else:
            gap = monthly - float(player.finance.balance)
            player.finance.balance = 0.0
            borrow_for_semester(player, gap)

    return total_expenses


# ── main endpoint ─────────────────────────────────────────────────

@router.post("/advance")
def advance_semester(player_id: str):
    """
    Advance the player to the next semester.
    Requirements:
      - Must have a locked semester plan
      - Must have passed the semester exam (score ≥ 70%)
    """
    p = require_player(player_id)
    _require_locked_plan(p)
    _require_exam_passed(p)

    # Validate curriculum exists
    sem = CURRICULUM.get(p.college_id, {}).get(p.major_id, {}).get(int(p.semester))
    if not sem:
        raise HTTPException(
            status_code=404,
            detail=f"No curriculum found for college={p.college_id}, "
                   f"major={p.major_id}, semester={p.semester}"
        )

    effects = {}

    # 1) Burnout consequence BEFORE other effects
    burnout_info = _apply_burnout_consequence(p)
    effects.update(burnout_info)

    # 2) Activity effects (cost + stress/happiness)
    apply_activity_effects(p)

    # 3) Time load → stress pressure → burnout update
    load = compute_weekly_time_load(p)
    apply_time_pressure(p, load)
    update_burnout(p)

    # 4) Health/sleep/network effects from overload
    health_effects = _apply_health_effects(p, load)
    effects.update(health_effects)

    # 5) Scholarships (awarded before tuition so they can offset cost)
    scholarship_awarded = _apply_scholarships(p)

    # 6) Monthly living expenses (4 months)
    total_expenses = _deduct_monthly_expenses(p)

    # 7) Tuition payment
    tuition = _semester_tuition(p)
    scholarship = float(p.finance.scholarship_per_semester or 0.0)
    due = max(0.0, tuition - scholarship)
    p.finance.tuition_per_semester = float(tuition)

    if due > 0:
        if p.finance.balance >= due:
            p.finance.balance -= due
            borrowed = 0.0
        else:
            gap = due - float(p.finance.balance)
            p.finance.balance = 0.0
            borrowed = borrow_for_semester(p, gap)
            pay_now = min(float(p.finance.balance), gap)
            p.finance.balance -= pay_now
    else:
        borrowed = 0.0

    # 8) In-school interest accrual
    accrue_interest_in_school(p, months=MONTHS_PER_SEMESTER)

    # 9) Log history event
    p.history.append(
        HistoryEvent(
            label="Semester End Processed",
            semester=p.semester,
            details=safe_details({
                "weekly_total_hours": float(load["total_hours"]),
                "weekly_overload": float(load.get("overload", 0.0)),
                "tuition": float(tuition),
                "scholarship_awarded": float(scholarship_awarded),
                "tuition_due": float(due),
                "borrowed_for_tuition_gap": float(borrowed),
                "monthly_expenses_total": float(total_expenses),
                "health": float(p.stats.health),
                "sleep_quality": float(p.stats.sleep_quality),
                "burnout": float(p.stats.burnout),
                "network_score": float(p.stats.network_score),
            }),
        )
    )

    # 10) Advance semester and year
    old_semester = p.semester
    p.semester += 1
    # Correct year tracking: year advances every 2 semesters (1-2=Y1, 3-4=Y2, etc.)
    p.year_in_school = ((p.semester - 1) // 2) + 1

    # Reset emergency tokens
    p.stats.emergency_tokens = max(1, int(p.stats.emergency_tokens))

    # Clear plan for next semester
    p.plan = None

    # Clear completed courses for new semester (keep history via dropped_courses)
    completed_this_semester = list(p.completed_courses)
    p.completed_courses = []

    # 11) Graduation check & debt snapshot
    graduated = p.semester > 8
    if graduated and p.finance.total_debt_at_graduation is None:
        p.finance.total_debt_at_graduation = p.finance.loan_portfolio.total_balance

    STORE.put_player(p)

    return {
        "player_id": p.id,
        "graduated": graduated,
        "previous_semester": old_semester,
        "new_semester": p.semester,
        "year_in_school": p.year_in_school,
        "year_label": p.current_year_label,
        "semester_summary": {
            "courses_completed": completed_this_semester,
            "scholarship_awarded": scholarship_awarded,
            "tuition_paid": due,
            "borrowed": borrowed,
            "living_expenses": total_expenses,
            "gpa": p.stats.gpa,
            "burnout_level": p.stats.burnout_level,
            **effects,
        },
        "warnings": _build_warnings(p),
        "player": p,
    }


def _build_warnings(player) -> list[str]:
    """Surface actionable warnings for the frontend to display."""
    warnings = []
    if player.stats.burnout > 50:
        warnings.append(f"⚠️ Burnout at {player.stats.burnout:.0f}% — consider dropping an activity or working fewer hours.")
    if player.stats.health < 40:
        warnings.append("🏥 Your health is critically low — prioritize sleep and exercise next semester.")
    if player.stats.gpa < 2.0 and player.semester > 2:
        warnings.append("📉 GPA below 2.0 — you may be at risk of academic probation.")
    if player.finance.balance < 500:
        warnings.append("💸 Low cash balance — consider a part-time job or applying for aid.")
    if player.finance.loan_portfolio.total_balance > 40_000:
        warnings.append(f"💳 Loan balance ${player.finance.loan_portfolio.total_balance:,.0f} — "
                        f"consider a lower-cost housing option.")
    return warnings