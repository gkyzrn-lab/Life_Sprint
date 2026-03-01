"""
Leaderboard Service

Manages player rankings, scores, and statistics aggregation.
Supports multiple leaderboard types: global, by college, by major, class rankings.
"""

from __future__ import annotations
from typing import List, Dict, Any, Optional, Literal
from pydantic import BaseModel, Field
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import heapq


# =========================
# Models
# =========================

class LeaderboardEntry(BaseModel):
    """Single entry in a leaderboard."""
    rank: int
    player_id: str
    player_name: str
    score: int
    games_played: int
    win_rate: float
    college_id: Optional[str] = None
    major_id: Optional[str] = None
    average_rating: float = 1000.0  # from skill_ratings
    last_updated: datetime = Field(default_factory=datetime.now)


class Leaderboard(BaseModel):
    """Complete leaderboard data."""
    leaderboard_type: Literal["global", "college", "major", "class"]
    filter_value: Optional[str] = None  # college_id, major_id, or class_id
    entries: List[LeaderboardEntry] = Field(default_factory=list)
    updated_at: datetime = Field(default_factory=datetime.now)
    period: Literal["weekly", "monthly", "alltime"] = "alltime"


class PlayerStats(BaseModel):
    """Aggregated player statistics for rankings."""
    player_id: str
    player_name: str
    college_id: str
    major_id: str
    total_games_played: int = 0
    total_games_won: int = 0
    total_points: int = 0
    average_rating: float = 1000.0
    current_streak: int = 0
    highest_streak: int = 0
    last_game_at: Optional[datetime] = None
    
    @property
    def win_rate(self) -> float:
        if self.total_games_played == 0:
            return 0.0
        return (self.total_games_won / self.total_games_played) * 100


# =========================
# Leaderboard Service
# =========================

class LeaderboardService:
    """
    In-memory leaderboard management.
    Can be replaced with Redis for production.
    """
    
    def __init__(self):
        # Store player stats: {player_id → PlayerStats}
        self.player_stats: Dict[str, PlayerStats] = {}
        
        # Cache leaderboards: {(type, filter, period) → Leaderboard}
        self.leaderboard_cache: Dict[tuple, Leaderboard] = {}
        
        # Cache expiration: {key → datetime}
        self.cache_expiry: Dict[tuple, datetime] = {}
        
        self.cache_ttl_seconds = 300  # 5 minutes
    
    def update_player_stats(self, player_id: str, player_name: str, college_id: str, major_id: str, **kwargs) -> None:
        """
        Update or create player statistics.
        Typically called after game completion.
        """
        if player_id not in self.player_stats:
            self.player_stats[player_id] = PlayerStats(
                player_id=player_id,
                player_name=player_name,
                college_id=college_id,
                major_id=major_id,
            )
        
        stats = self.player_stats[player_id]
        
        if "games_played" in kwargs:
            stats.total_games_played = kwargs["games_played"]
        if "games_won" in kwargs:
            stats.total_games_won = kwargs["games_won"]
        if "points" in kwargs:
            stats.total_points = kwargs["points"]
        if "average_rating" in kwargs:
            stats.average_rating = kwargs["average_rating"]
        if "current_streak" in kwargs:
            stats.current_streak = kwargs["current_streak"]
        if "highest_streak" in kwargs:
            stats.highest_streak = kwargs["highest_streak"]
        
        stats.last_game_at = datetime.now()
        
        # Invalidate affected leaderboards
        self._invalidate_caches(player_id, college_id, major_id)
    
    def _invalidate_caches(self, player_id: str, college_id: str, major_id: str) -> None:
        """Invalidate leaderboard caches affected by this player update."""
        keys_to_invalidate = [
            ("global", None, "alltime"),
            ("global", None, "weekly"),
            ("global", None, "monthly"),
            ("college", college_id, "alltime"),
            ("college", college_id, "weekly"),
            ("college", college_id, "monthly"),
            ("major", major_id, "alltime"),
            ("major", major_id, "weekly"),
            ("major", major_id, "monthly"),
        ]
        
        for key in keys_to_invalidate:
            if key in self.leaderboard_cache:
                del self.leaderboard_cache[key]
            if key in self.cache_expiry:
                del self.cache_expiry[key]
    
    def get_leaderboard(
        self,
        leaderboard_type: Literal["global", "college", "major", "class"] = "global",
        filter_value: Optional[str] = None,
        period: Literal["weekly", "monthly", "alltime"] = "alltime",
        limit: int = 100,
    ) -> Leaderboard:
        """
        Get a leaderboard with optional filtering.
        
        Args:
            leaderboard_type: Type of leaderboard
            filter_value: College ID, major ID, or class ID
            period: Time period (weekly/monthly/alltime)
            limit: Max entries to return
        
        Returns:
            Leaderboard object
        """
        cache_key = (leaderboard_type, filter_value, period)
        
        # Check if cached and still valid
        if cache_key in self.leaderboard_cache:
            if self.cache_expiry.get(cache_key, datetime.now()) > datetime.now():
                return self.leaderboard_cache[cache_key]
        
        # Build leaderboard
        entries = []
        
        for player_id, stats in self.player_stats.items():
            # Filter by type and value
            if leaderboard_type == "college" and stats.college_id != filter_value:
                continue
            elif leaderboard_type == "major" and stats.major_id != filter_value:
                continue
            elif leaderboard_type == "class":
                # Class filtering would require separate class membership tracking
                # Skip for now, implement when class system exists
                continue
            
            # Filter by period (simple: check last_game_at)
            if period == "weekly":
                if not stats.last_game_at or (datetime.now() - stats.last_game_at).days > 7:
                    continue
            elif period == "monthly":
                if not stats.last_game_at or (datetime.now() - stats.last_game_at).days > 30:
                    continue
            
            entries.append(stats)
        
        # Sort by points (primary) then rating (secondary)
        entries.sort(key=lambda x: (-x.total_points, -x.average_rating))
        
        # Assign ranks and create entries
        leaderboard_entries = []
        for rank, stats in enumerate(entries[:limit], 1):
            entry = LeaderboardEntry(
                rank=rank,
                player_id=stats.player_id,
                player_name=stats.player_name,
                score=stats.total_points,
                games_played=stats.total_games_played,
                win_rate=stats.win_rate,
                college_id=stats.college_id,
                major_id=stats.major_id,
                average_rating=stats.average_rating,
            )
            leaderboard_entries.append(entry)
        
        # Create leaderboard
        leaderboard = Leaderboard(
            leaderboard_type=leaderboard_type,
            filter_value=filter_value,
            entries=leaderboard_entries,
            period=period,
        )
        
        # Cache it
        self.leaderboard_cache[cache_key] = leaderboard
        self.cache_expiry[cache_key] = datetime.now() + timedelta(seconds=self.cache_ttl_seconds)
        
        return leaderboard
    
    def get_player_rank(
        self,
        player_id: str,
        leaderboard_type: Literal["global", "college", "major"] = "global",
        filter_value: Optional[str] = None,
        period: Literal["weekly", "monthly", "alltime"] = "alltime",
    ) -> Optional[int]:
        """
        Get a player's rank on a specific leaderboard.
        Returns their position (1-indexed) or None if not ranked.
        """
        if player_id not in self.player_stats:
            return None
        
        leaderboard = self.get_leaderboard(leaderboard_type, filter_value, period, limit=10000)
        
        for entry in leaderboard.entries:
            if entry.player_id == player_id:
                return entry.rank
        
        return None
    
    def get_player_stats(self, player_id: str) -> Optional[PlayerStats]:
        """Get stats for a specific player."""
        return self.player_stats.get(player_id)


# =========================
# Global Service Instance
# =========================

leaderboard_service = LeaderboardService()
