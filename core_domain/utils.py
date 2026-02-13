# app/core/utils.py

from __future__ import annotations

from typing import Dict
from core_domain.models import Player, HistoryEvent
from core_domain.config import MAX_STRESS, MAX_HAPPINESS, MAX_BURNOUT


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


def clamp_stats(player: Player) -> None:
    player.stats.stress = clamp(player.stats.stress, 0.0, MAX_STRESS)
    player.stats.happiness = clamp(player.stats.happiness, 0.0, MAX_HAPPINESS)
    player.stats.burnout = clamp(player.stats.burnout, 0.0, MAX_BURNOUT)


def clamp_player_wellbeing(player: Player) -> None:
    """Backward-compatible helper used across wellbeing modules.
    Normalizes stress/happiness/burnout to allowed ranges.
    """
    clamp_stats(player)


def add_history(player: Player, label: str, semester: int, details: Dict[str, float] | None = None) -> None:
    player.history.append(
        HistoryEvent(label=label, semester=semester, details=details or {})
    )


def safe_details(details: Dict[str, object] | None) -> Dict[str, object]:
    """Convert numeric-like detail values to floats where possible so
    history details are stable and JSON-serializable.
    """
    out: Dict[str, object] = {}
    if not details:
        return out
    for k, v in details.items():
        try:
            out[k] = float(v)
        except Exception:
            out[k] = v
    return out
