"""
Quest System Models

Tracks player progress through tutorial quests and achievement chains.
"""

from __future__ import annotations
from typing import List, Dict, Any, Optional
from pydantic import BaseModel


class QuestProgress(BaseModel):
    """Player's progress through a specific quest chain"""
    quest_id: str
    completed_steps: List[str]  # Step IDs completed
    current_step_id: Optional[str]  # Current active step
    started_at: float  # Unix timestamp
    completed_at: Optional[float]  # Unix timestamp when finished
    total_points_earned: int
    
    
class PlayerQuestState(BaseModel):
    """All quest progress for a player"""
    active_quests: List[QuestProgress]  # Quests in progress
    completed_quests: List[str]  # Quest IDs fully completed
    tutorial_complete: bool  # Flag for tutorial completion
    tutorial_completion_time_seconds: Optional[float]  # How long tutorial took
