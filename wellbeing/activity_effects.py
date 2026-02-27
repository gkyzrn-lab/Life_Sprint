from __future__ import annotations

def apply_activity_effects(player) -> None:
    """
    Apply stress/happiness/cost effects from the player's chosen activities.
    """
    if not player.plan or not player.plan.activities:
        return

    try:
        from catalogs.activities import ACTIVITIES
        for activity_id in player.plan.activities:
            activity = ACTIVITIES.get(activity_id)
            if not activity:
                continue
            # Apply stress delta
            stress_delta = float(getattr(activity, 'stress_delta_per_semester', 0.0))
            player.stats.stress = max(0.0, min(100.0, player.stats.stress + stress_delta))
            # Apply happiness delta
            happiness_delta = float(getattr(activity, 'happiness_delta_per_semester', 0.0))
            player.stats.happiness = max(0.0, min(100.0, player.stats.happiness + happiness_delta))
            # Deduct cost
            cost = float(getattr(activity, 'cost_per_semester', 0.0))
            if cost > 0:
                player.finance.balance = max(0.0, player.finance.balance - cost)
    except Exception:
        # If activities catalog not available, apply generic small stress relief
        player.stats.stress = max(0.0, player.stats.stress - 2.0)
        player.stats.happiness = min(100.0, player.stats.happiness + 2.0)
