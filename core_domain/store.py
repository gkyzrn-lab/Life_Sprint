# app/core/store.py

from __future__ import annotations

from typing import Dict
from core_domain.models import Player


class InMemoryStore:
    """
    Simple in-memory storage for development.
    Replace with DB later without touching business logic too much.
    """

    def __init__(self) -> None:
        self.players: Dict[str, Player] = {}

    def put_player(self, player: Player) -> None:
        self.players[player.id] = player

    def get_player(self, player_id: str) -> Player | None:
        return self.players.get(player_id)

    def require_player(self, player_id: str) -> Player:
        p = self.get_player(player_id)
        if not p:
            raise KeyError(f"Player not found: {player_id}")
        return p


STORE = InMemoryStore()
