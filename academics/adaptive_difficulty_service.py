"""
Adaptive Difficulty Service

Integrates skill rating system with game generation and grading.
Automatically adjusts difficulty based on player performance history.
"""

from __future__ import annotations
from typing import List, Dict, Any, Optional

from core_domain.player.player_model import Player, HistoryEvent
from core_domain.player.skill_ratings import (
    SkillDomain,
    DifficultyTier,
    select_questions_by_difficulty,
    calculate_dynamic_pass_threshold,
)


# =========================
# Domain Mapping
# =========================

def map_game_id_to_domain(game_id: str) -> SkillDomain:
    """Map game/course IDs to skill domains for rating tracking."""
    game_id_lower = game_id.lower()
    
    # Tutorial games
    if "tutorial" in game_id_lower:
        if "financial" in game_id_lower or "money" in game_id_lower:
            return SkillDomain.finance
        elif "time" in game_id_lower:
            return SkillDomain.time_management
        elif "gpa" in game_id_lower or "academic" in game_id_lower:
            return SkillDomain.academics
        elif "emergency" in game_id_lower:
            return SkillDomain.general
        else:
            return SkillDomain.general
    
    # Course games
    if "fin" in game_id_lower or "econ" in game_id_lower or "acct" in game_id_lower:
        return SkillDomain.finance
    elif "math" in game_id_lower or "calc" in game_id_lower or "stat" in game_id_lower:
        return SkillDomain.academics
    elif "health" in game_id_lower or "wellness" in game_id_lower:
        return SkillDomain.health
    elif "career" in game_id_lower or "interview" in game_id_lower or "resume" in game_id_lower:
        return SkillDomain.career
    elif "housing" in game_id_lower or "real_estate" in game_id_lower:
        return SkillDomain.housing
    else:
        return SkillDomain.academics  # default


def map_course_id_to_domain(course_id: str) -> SkillDomain:
    """Map course IDs to skill domains."""
    course_lower = course_id.lower()
    
    if any(x in course_lower for x in ["fin", "econ", "acct", "business"]):
        return SkillDomain.finance
    elif any(x in course_lower for x in ["health", "wellness", "nutrition"]):
        return SkillDomain.health
    elif any(x in course_lower for x in ["career", "professional", "internship"]):
        return SkillDomain.career
    else:
        return SkillDomain.academics


# =========================
# Adaptive Question Selection
# =========================

def select_adaptive_questions(
    player: Player,
    question_pool: List[Dict[str, Any]],
    domain: SkillDomain,
    count: int = 3,
) -> List[Dict[str, Any]]:
    """
    Select questions from pool based on player's skill rating in the domain.
    
    Args:
        player: Player with skill_ratings initialized
        question_pool: Questions with 'difficulty' field (easy/medium/hard/expert)
        domain: Skill domain being tested
        count: Number of questions to select
    
    Returns:
        List of questions matching player's skill level
    """
    if not player.skill_ratings:
        # Fallback: random selection if ratings not initialized
        import random
        return random.sample(question_pool, min(count, len(question_pool)))
    
    target_tier = player.skill_ratings.get_difficulty_tier(domain)
    return select_questions_by_difficulty(question_pool, target_tier, count, fallback=True)


# =========================
# Post-Game Rating Update
# =========================

def update_player_rating_after_game(
    player: Player,
    game_id: str,
    score_percent: float,
    passed: bool,
    difficulty_tier: Optional[DifficultyTier] = None,
) -> Dict[str, Any]:
    """
    Update player's skill rating after completing a game.
    
    Args:
        player: Player to update
        game_id: ID of game completed
        score_percent: Player's score (0-100)
        passed: Whether player passed
        difficulty_tier: Difficulty of questions (auto-detected if None)
    
    Returns:
        Dict with rating changes and performance summary
    """
    if not player.skill_ratings:
        from core_domain.player.skill_ratings import PlayerSkillRatings
        object.__setattr__(player, 'skill_ratings', PlayerSkillRatings())
    
    domain = map_game_id_to_domain(game_id)
    
    # Auto-detect difficulty if not provided
    if difficulty_tier is None:
        difficulty_tier = player.skill_ratings.get_difficulty_tier(domain)
    
    # Update rating
    old_rating = player.skill_ratings.get_or_create_rating(domain).rating
    delta = player.skill_ratings.update_rating(domain, score_percent, passed, difficulty_tier)
    new_rating = player.skill_ratings.get_or_create_rating(domain).rating
    new_tier = player.skill_ratings.get_or_create_rating(domain).difficulty_tier
    
    # Log to history
    player.history.append(
        HistoryEvent(
            label=f"Skill Rating Updated: {domain.value}",
            semester=player.semester,
            details={
                "old_rating": float(old_rating),
                "new_rating": float(new_rating),
                "delta": float(delta),
                "score_percent": float(score_percent),
            },
        )
    )
    
    # Check for tier changes
    tier_changed = False
    old_tier = DifficultyTier.medium  # assume medium if first game
    if player.skill_ratings.get_or_create_rating(domain).games_played > 1:
        # Calculate what tier they were at before
        if old_rating < 800:
            old_tier = DifficultyTier.easy
        elif old_rating < 1200:
            old_tier = DifficultyTier.medium
        elif old_rating < 1600:
            old_tier = DifficultyTier.hard
        else:
            old_tier = DifficultyTier.expert
        tier_changed = old_tier != new_tier
    
    return {
        "domain": domain.value,
        "old_rating": round(old_rating, 1),
        "new_rating": round(new_rating, 1),
        "delta": round(delta, 1),
        "new_tier": new_tier.value,
        "tier_changed": tier_changed,
        "games_played": player.skill_ratings.get_or_create_rating(domain).games_played,
        "win_rate": round(player.skill_ratings.get_or_create_rating(domain).win_rate * 100, 1),
    }


# =========================
# Challenge/Practice Mode Helpers
# =========================

def set_challenge_mode(player: Player, enabled: bool) -> Dict[str, Any]:
    """
    Enable/disable challenge mode (increases difficulty by 1 tier).
    Useful for advanced players wanting harder questions.
    """
    if not player.skill_ratings:
        from core_domain.player.skill_ratings import PlayerSkillRatings
        object.__setattr__(player, 'skill_ratings', PlayerSkillRatings())
    
    player.skill_ratings.challenge_mode = enabled
    player.skill_ratings.practice_mode = False  # mutually exclusive
    
    player.history.append(
        HistoryEvent(
            label=f"Challenge Mode {'Enabled' if enabled else 'Disabled'}",
            semester=player.semester,
            details={"enabled": 1.0 if enabled else 0.0},
        )
    )
    
    return {
        "challenge_mode": enabled,
        "message": "Challenge mode ON: questions will be 1 tier harder" if enabled else "Challenge mode OFF"
    }


def set_practice_mode(player: Player, enabled: bool) -> Dict[str, Any]:
    """
    Enable/disable practice mode (decreases difficulty by 1 tier, no rating changes).
    Useful for learning without consequences.
    """
    if not player.skill_ratings:
        from core_domain.player.skill_ratings import PlayerSkillRatings
        object.__setattr__(player, 'skill_ratings', PlayerSkillRatings())
    
    player.skill_ratings.practice_mode = enabled
    player.skill_ratings.challenge_mode = False  # mutually exclusive
    
    player.history.append(
        HistoryEvent(
            label=f"Practice Mode {'Enabled' if enabled else 'Disabled'}",
            semester=player.semester,
            details={"enabled": 1.0 if enabled else 0.0},
        )
    )
    
    return {
        "practice_mode": enabled,
        "message": "Practice mode ON: easier questions, no rating changes" if enabled else "Practice mode OFF"
    }


def get_player_performance_dashboard(player: Player) -> Dict[str, Any]:
    """
    Generate comprehensive performance dashboard for player.
    Shows ratings, tiers, and stats across all domains.
    """
    if not player.skill_ratings:
        return {
            "initialized": False,
            "message": "No games played yet. Ratings will appear after completing tutorial.",
        }
    
    overall = player.skill_ratings.get_performance_summary()
    domain_details = []
    
    for domain in SkillDomain:
        if domain in player.skill_ratings.ratings:
            summary = player.skill_ratings.get_performance_summary(domain)
            domain_details.append(summary)
    
    return {
        "initialized": True,
        "overall": overall,
        "domains": domain_details,
        "challenge_mode": player.skill_ratings.challenge_mode,
        "practice_mode": player.skill_ratings.practice_mode,
    }
