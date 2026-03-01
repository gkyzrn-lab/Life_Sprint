"""
Player Skill Rating System

Elo-like rating algorithm that tracks player skill across different domains
(finance, academics, time management, etc.) and adapts game difficulty.

Rating Ranges:
- 0-800: Beginner
- 800-1200: Intermediate  
- 1200-1600: Advanced
- 1600+: Expert

Starting rating: 1000 (intermediate baseline)
"""

from __future__ import annotations
from typing import Dict, Optional, Literal
from pydantic import BaseModel, Field
from enum import Enum
import math


class DifficultyTier(str, Enum):
    """Question difficulty tiers used for adaptive selection."""
    easy = "easy"
    medium = "medium"
    hard = "hard"
    expert = "expert"


class SkillDomain(str, Enum):
    """Skill domains tracked independently for each player."""
    finance = "finance"
    academics = "academics"
    time_management = "time_management"
    health = "health"
    career = "career"
    housing = "housing"
    general = "general"  # catch-all for tutorial/misc games


class DomainRating(BaseModel):
    """Rating for a specific skill domain."""
    domain: SkillDomain
    rating: float = 1000.0  # Elo rating (starting at intermediate)
    games_played: int = 0
    wins: int = 0  # games passed
    losses: int = 0  # games failed
    avg_score: float = 0.0  # rolling average of score_percent
    
    @property
    def win_rate(self) -> float:
        if self.games_played == 0:
            return 0.0
        return self.wins / self.games_played
    
    @property
    def difficulty_tier(self) -> DifficultyTier:
        """Determine appropriate difficulty tier based on rating."""
        if self.rating < 800:
            return DifficultyTier.easy
        elif self.rating < 1200:
            return DifficultyTier.medium
        elif self.rating < 1600:
            return DifficultyTier.hard
        else:
            return DifficultyTier.expert


class PlayerSkillRatings(BaseModel):
    """
    Container for all skill ratings across domains.
    Tracks player performance and determines adaptive difficulty.
    """
    ratings: Dict[SkillDomain, DomainRating] = Field(default_factory=dict)
    
    # Difficulty modifiers (player preferences)
    challenge_mode: bool = False  # +1 tier difficulty
    practice_mode: bool = False   # -1 tier difficulty (no rating changes)
    
    # Global stats
    total_games_played: int = 0
    total_points_earned: int = 0
    highest_streak: int = 0  # consecutive perfect scores (100%)
    current_streak: int = 0
    
    def get_or_create_rating(self, domain: SkillDomain) -> DomainRating:
        """Get rating for domain, creating with defaults if needed."""
        if domain not in self.ratings:
            self.ratings[domain] = DomainRating(domain=domain)
        return self.ratings[domain]
    
    def get_difficulty_tier(self, domain: SkillDomain) -> DifficultyTier:
        """
        Determine difficulty tier for a domain, accounting for player mode preferences.
        """
        rating = self.get_or_create_rating(domain)
        base_tier = rating.difficulty_tier
        
        # Apply modifiers
        tier_order = [DifficultyTier.easy, DifficultyTier.medium, DifficultyTier.hard, DifficultyTier.expert]
        tier_index = tier_order.index(base_tier)
        
        if self.challenge_mode:
            tier_index = min(tier_index + 1, len(tier_order) - 1)
        elif self.practice_mode:
            tier_index = max(tier_index - 1, 0)
        
        return tier_order[tier_index]
    
    def update_rating(
        self,
        domain: SkillDomain,
        score_percent: float,
        passed: bool,
        expected_difficulty: DifficultyTier,
    ) -> float:
        """
        Update Elo rating based on game performance.
        
        Args:
            domain: Skill domain being tested
            score_percent: Player's score (0-100)
            passed: Whether player met pass threshold
            expected_difficulty: Difficulty tier of the game
        
        Returns:
            Rating change (delta)
        """
        if self.practice_mode:
            # Practice mode: no rating changes, just tracking
            rating = self.get_or_create_rating(domain)
            rating.games_played += 1
            return 0.0
        
        rating = self.get_or_create_rating(domain)
        
        # Elo calculation
        # K-factor: how much ratings can change per game
        # Higher K for new players (more volatile), lower for experienced
        k_factor = 40.0 if rating.games_played < 10 else 20.0
        
        # Expected score based on difficulty tier
        # Easier games = higher expected score
        difficulty_factor = {
            DifficultyTier.easy: 0.75,     # expect 75% success
            DifficultyTier.medium: 0.60,   # expect 60% success
            DifficultyTier.hard: 0.45,     # expect 45% success
            DifficultyTier.expert: 0.30,   # expect 30% success
        }
        expected = difficulty_factor.get(expected_difficulty, 0.60)
        
        # Actual performance (normalized to 0-1)
        actual = score_percent / 100.0
        
        # Rating delta
        delta = k_factor * (actual - expected)
        
        # Apply change
        old_rating = rating.rating
        rating.rating += delta
        rating.rating = max(0.0, rating.rating)  # floor at 0
        
        # Update stats
        rating.games_played += 1
        if passed:
            rating.wins += 1
        else:
            rating.losses += 1
        
        # Update rolling average score
        if rating.games_played == 1:
            rating.avg_score = score_percent
        else:
            # exponential moving average (recent games weighted more)
            alpha = 0.3
            rating.avg_score = (alpha * score_percent) + ((1 - alpha) * rating.avg_score)
        
        # Update global stats
        self.total_games_played += 1
        if score_percent >= 100.0:
            self.current_streak += 1
            self.highest_streak = max(self.highest_streak, self.current_streak)
        else:
            self.current_streak = 0
        
        return delta
    
    def get_performance_summary(self, domain: Optional[SkillDomain] = None) -> Dict:
        """
        Get performance summary for a domain or overall.
        Useful for player dashboard / stats screen.
        """
        if domain:
            rating = self.get_or_create_rating(domain)
            return {
                "domain": domain.value,
                "rating": round(rating.rating, 1),
                "tier": rating.difficulty_tier.value,
                "games_played": rating.games_played,
                "win_rate": round(rating.win_rate * 100, 1),
                "avg_score": round(rating.avg_score, 1),
            }
        else:
            # Overall summary
            total_rating = sum(r.rating for r in self.ratings.values())
            avg_rating = total_rating / len(self.ratings) if self.ratings else 1000.0
            
            return {
                "overall_rating": round(avg_rating, 1),
                "total_games": self.total_games_played,
                "total_points": self.total_points_earned,
                "current_streak": self.current_streak,
                "highest_streak": self.highest_streak,
                "domains": {
                    domain.value: {
                        "rating": round(rating.rating, 1),
                        "tier": rating.difficulty_tier.value,
                    }
                    for domain, rating in self.ratings.items()
                },
            }


# =========================
# Difficulty Selection Helpers
# =========================

def select_questions_by_difficulty(
    question_pool: list,
    target_tier: DifficultyTier,
    count: int,
    fallback: bool = True,
) -> list:
    """
    Select questions matching target difficulty tier.
    
    Args:
        question_pool: List of questions with 'difficulty' field
        target_tier: Desired difficulty tier
        count: Number of questions to select
        fallback: If True and not enough questions found, select from adjacent tiers
    
    Returns:
        List of selected questions
    """
    import random
    
    # Filter by target difficulty
    matching = [q for q in question_pool if q.get("difficulty") == target_tier.value]
    
    if len(matching) >= count:
        return random.sample(matching, count)
    
    if not fallback:
        return random.sample(matching, min(count, len(matching)))
    
    # Fallback: include adjacent tiers
    tier_order = [DifficultyTier.easy, DifficultyTier.medium, DifficultyTier.hard, DifficultyTier.expert]
    tier_index = tier_order.index(target_tier)
    
    adjacent_tiers = []
    if tier_index > 0:
        adjacent_tiers.append(tier_order[tier_index - 1])
    if tier_index < len(tier_order) - 1:
        adjacent_tiers.append(tier_order[tier_index + 1])
    
    for adj_tier in adjacent_tiers:
        adj_matching = [q for q in question_pool if q.get("difficulty") == adj_tier.value]
        matching.extend(adj_matching)
    
    if len(matching) >= count:
        return random.sample(matching, count)
    else:
        # Still not enough: return all matching + random filler
        remaining = count - len(matching)
        others = [q for q in question_pool if q not in matching]
        if others and remaining > 0:
            matching.extend(random.sample(others, min(remaining, len(others))))
        return matching


def calculate_dynamic_pass_threshold(difficulty_tier: DifficultyTier, base_threshold: float = 70.0) -> float:
    """
    Calculate pass threshold based on difficulty.
    Harder games have lower pass requirements to account for increased challenge.
    
    Args:
        difficulty_tier: Question difficulty
        base_threshold: Standard pass percentage (default 70%)
    
    Returns:
        Adjusted pass threshold (50-80%)
    """
    adjustments = {
        DifficultyTier.easy: 5.0,      # 75% required
        DifficultyTier.medium: 0.0,    # 70% required
        DifficultyTier.hard: -10.0,    # 60% required
        DifficultyTier.expert: -20.0,  # 50% required
    }
    
    adjusted = base_threshold + adjustments.get(difficulty_tier, 0.0)
    return max(50.0, min(80.0, adjusted))  # clamp to reasonable range
