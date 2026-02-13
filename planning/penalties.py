from __future__ import annotations

from typing import Optional, Dict
from core_domain.player.player_model import Player
from core_domain.utils import clamp_player_wellbeing
from planning.emergency_causes import EmergencyCause


def apply_emergency_change_penalty(
    player: Player,
    *,
    changed_housing: bool,
    changed_job: bool,
    cause: Optional[EmergencyCause],
) -> Dict[str, float]:
    """
    Apply penalties for mid-semester changes.
    Returns a dict of applied deltas for logging/telemetry.

    Design goals:
      - changes feel expensive
      - burnout makes it worse
      - emergency causes tweak the pain
    """

    # Base penalties
    base_stress = 10.0
    base_happiness = -3.0
    base_admin_cost = 75.0

    # Specific penalties
    housing_one_time_cost = 150.0
    housing_extra_stress = 6.0

    job_extra_stress = 4.0

    # Cause modifiers
    housing_fee_multiplier = cause.housing_fee_multiplier if cause else 1.0
    job_stress_delta = cause.job_stress_delta if cause else 0.0
    happiness_delta_extra = cause.happiness_delta_extra if cause else 0.0
    money_delta_extra = cause.money_delta_extra if cause else 0.0

    # Apply base
    player.stats.stress += base_stress
    player.stats.happiness += (base_happiness + happiness_delta_extra)
    player.finance.balance -= base_admin_cost
    player.finance.balance += money_delta_extra

    # Apply change-specific
    if changed_housing:
        player.finance.balance -= (housing_one_time_cost * housing_fee_multiplier)
        player.stats.stress += housing_extra_stress

    if changed_job:
        # job_stress_delta can reduce the penalty, but we never want negative stress add from "changing jobs"
        player.stats.stress += max(0.0, job_extra_stress + job_stress_delta)

    # Burnout amplifies pain
    if player.stats.burnout >= 60.0:
        player.stats.stress += 6.0
        player.stats.happiness -= 2.0

    clamp_player_wellbeing(player)

    return {
        "base_stress": base_stress,
        "base_happiness": base_happiness,
        "base_admin_cost": base_admin_cost,
        "housing_one_time_cost": (housing_one_time_cost * housing_fee_multiplier) if changed_housing else 0.0,
        "housing_extra_stress": housing_extra_stress if changed_housing else 0.0,
        "job_extra_stress": max(0.0, job_extra_stress + job_stress_delta) if changed_job else 0.0,
        "cause_housing_fee_multiplier": housing_fee_multiplier,
        "cause_job_stress_delta": job_stress_delta,
        "cause_happiness_delta_extra": happiness_delta_extra,
        "cause_money_delta_extra": money_delta_extra,
        "burnout_amp": 1.0 if player.stats.burnout >= 60.0 else 0.0,
    }
