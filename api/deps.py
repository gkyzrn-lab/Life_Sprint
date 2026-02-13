from __future__ import annotations

from fastapi import HTTPException
from core_domain.store import STORE
from core_domain.player.player_model import Player


def require_player(player_id: str) -> Player:
    try:
        return STORE.require_player(player_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Player not found")
