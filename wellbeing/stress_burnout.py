from __future__ import annotations

def apply_time_pressure(player, load: dict) -> None:
    """
    Increase stress based on weekly overload hours.
    Every 5 hours of overload adds 5 stress points.
    """
    overload = float(load.get("overload", 0.0))
    stress_increase = (overload / 5.0) * 5.0
    player.stats.stress = min(100.0, player.stats.stress + stress_increase)

def update_burnout(player) -> None:
    """
    Update burnout based on current stress level.
    High stress accumulates burnout; low stress recovers it.
    """
    stress = float(player.stats.stress)
    if stress > 70:
        # High stress rapidly increases burnout
        player.stats.burnout = min(100.0, player.stats.burnout + (stress - 70) / 10.0)
    elif stress < 30:
        # Low stress slowly recovers burnout
        player.stats.burnout = max(0.0, player.stats.burnout - 5.0)
    else:
        # Moderate stress slightly increases burnout
        player.stats.burnout = min(100.0, player.stats.burnout + 1.0)
