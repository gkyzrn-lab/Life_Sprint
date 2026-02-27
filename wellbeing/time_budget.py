from __future__ import annotations

WEEKLY_HOURS_TOTAL = 168.0

def compute_weekly_time_load(player) -> dict:
    """
    Compute the player's weekly time load based on their current plan.
    Returns total hours used and overload amount.
    """
    # Base committed hours
    sleep_hours = 56.0  # 8 hrs/night

    # Class hours from curriculum
    class_hours = 0.0
    try:
        from academics.curriculum import CURRICULUM
        sem = CURRICULUM.get(player.college_id, {}).get(player.major_id, {}).get(player.semester)
        if sem:
            class_hours = float(sum(getattr(c, 'weekly_hours', 3) for c in sem.courses))
    except Exception:
        class_hours = 15.0  # default fallback

    # Work hours from job
    work_hours = 0.0
    if player.job:
        work_hours = float(player.job.hours_per_week)

    # Study hours from plan
    study_hours = 15.0
    if player.plan:
        study_hours = float(getattr(player.plan, 'intended_study_hours_per_week', 15.0))

    # Activity hours
    activity_hours = 0.0
    if player.plan and player.plan.activities:
        activity_hours = float(len(player.plan.activities) * 3)

    # Personal time (eating, hygiene, commute)
    personal_hours = 14.0

    total_hours = sleep_hours + class_hours + work_hours + study_hours + activity_hours + personal_hours
    overload = max(0.0, total_hours - WEEKLY_HOURS_TOTAL)

    return {
        "sleep_hours": sleep_hours,
        "class_hours": class_hours,
        "work_hours": work_hours,
        "study_hours": study_hours,
        "activity_hours": activity_hours,
        "personal_hours": personal_hours,
        "total_hours": round(total_hours, 1),
        "overload": round(overload, 1),
        "is_overloaded": overload > 0,
        "free_hours": round(max(0.0, WEEKLY_HOURS_TOTAL - total_hours), 1),
    }
