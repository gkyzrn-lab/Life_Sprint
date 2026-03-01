"""
Achievement Badge System - Reward player milestones with unlockable badges

Badges recognize player accomplishments across multiple dimensions:
- Domain mastery
- Consistency
- Volume
- Excellence
- Balanced development
"""

from __future__ import annotations
from typing import List, Dict, Any, Set
from pydantic import BaseModel

from analytics.readiness_score import (
    GAME_TYPE_TO_DOMAINS,
    LifeReadinessDomain,
    DomainReadiness,
)


class Badge(BaseModel):
    """A single achievement badge"""
    id: str
    name: str
    description: str
    icon: str  # emoji
    category: str  # e.g., "domain_mastery", "consistency", "volume"
    tier: int = 1  # 1=bronze, 2=silver, 3=gold


# ========================================
# Badge Catalog
# ========================================

ALL_BADGES: List[Badge] = [
    # Domain Mastery Badges (Tier 1: Bronze)
    Badge(
        id="finance_guru_bronze",
        name="Finance Guru (Bronze)",
        description="Complete 5+ finance games with 85%+ average score",
        icon="💰",
        category="domain_mastery",
        tier=1,
    ),
    Badge(
        id="tech_master_bronze",
        name="Tech Master (Bronze)",
        description="Complete 5+ technical games with 85%+ average score",
        icon="💻",
        category="domain_mastery",
        tier=1,
    ),
    Badge(
        id="leader_bronze",
        name="Leader (Bronze)",
        description="Complete 5+ leadership games with 85%+ average score",
        icon="👥",
        category="domain_mastery",
        tier=1,
    ),
    Badge(
        id="critical_thinker_bronze",
        name="Critical Thinker (Bronze)",
        description="Complete 5+ critical thinking games with 85%+ average score",
        icon="🧠",
        category="domain_mastery",
        tier=1,
    ),
    Badge(
        id="ethical_bronze",
        name="Ethical Champion (Bronze)",
        description="Complete 5+ ethics games with 85%+ average score",
        icon="⚖️",
        category="domain_mastery",
        tier=1,
    ),
    
    # Domain Mastery Badges (Tier 2: Silver - 10+ games, 90%+)
    Badge(
        id="finance_guru_silver",
        name="Finance Guru (Silver)",
        description="Complete 10+ finance games with 90%+ average score",
        icon="💎",
        category="domain_mastery",
        tier=2,
    ),
    Badge(
        id="tech_master_silver",
        name="Tech Master (Silver)",
        description="Complete 10+ technical games with 90%+ average score",
        icon="⚡",
        category="domain_mastery",
        tier=2,
    ),
    Badge(
        id="leader_silver",
        name="Leader (Silver)",
        description="Complete 10+ leadership games with 90%+ average score",
        icon="🌟",
        category="domain_mastery",
        tier=2,
    ),
    
    # Volume Badges
    Badge(
        id="game_explorer",
        name="Game Explorer",
        description="Complete 10+ games",
        icon="🎮",
        category="volume",
        tier=1,
    ),
    Badge(
        id="game_veteran",
        name="Game Veteran",
        description="Complete 30+ games",
        icon="🏆",
        category="volume",
        tier=2,
    ),
    Badge(
        id="game_legend",
        name="Game Legend",
        description="Complete 50+ games",
        icon="👑",
        category="volume",
        tier=3,
    ),
    
    # Consistency Badges
    Badge(
        id="consistent_performer",
        name="Consistent Performer",
        description="Complete 10 consecutive games at 70%+ score",
        icon="📈",
        category="consistency",
        tier=1,
    ),
    Badge(
        id="unstoppable",
        name="Unstoppable",
        description="Complete 20 consecutive games at 75%+ score",
        icon="🔥",
        category="consistency",
        tier=2,
    ),
    
    # Excellence Badges
    Badge(
        id="perfectionist",
        name="Perfectionist",
        description="Score 100% on 5 different games",
        icon="✨",
        category="excellence",
        tier=2,
    ),
    Badge(
        id="high_achiever",
        name="High Achiever",
        description="Achieve 90%+ average across all games (minimum 10 games)",
        icon="🎯",
        category="excellence",
        tier=3,
    ),
    
    # Domain Score Badges
    Badge(
        id="domain_expert",
        name="Domain Expert",
        description="Reach 90+ score in any domain",
        icon="🌟",
        category="domain_score",
        tier=2,
    ),
    Badge(
        id="domain_master",
        name="Domain Master",
        description="Reach 95+ score in any domain",
        icon="💫",
        category="domain_score",
        tier=3,
    ),
    
    # Career Readiness Badges
    Badge(
        id="career_ready",
        name="Career Ready",
        description="Achieve 70%+ overall readiness score",
        icon="🚀",
        category="career_readiness",
        tier=1,
    ),
    Badge(
        id="industry_ready",
        name="Industry Ready",
        description="Achieve 80%+ overall readiness with all domains at 60%+",
        icon="💼",
        category="career_readiness",
        tier=2,
    ),
    Badge(
        id="elite_candidate",
        name="Elite Candidate",
        description="Achieve 90%+ overall readiness with all domains at 75%+",
        icon="🏅",
        category="career_readiness",
        tier=3,
    ),
    
    # Balanced Development Badges
    Badge(
        id="well_rounded",
        name="Well-Rounded",
        description="All domains at 60%+ score",
        icon="🌈",
        category="balanced",
        tier=1,
    ),
    Badge(
        id="renaissance_student",
        name="Renaissance Student",
        description="All domains at 75%+ score",
        icon="🎨",
        category="balanced",
        tier=2,
    ),
]

BADGES_BY_ID = {badge.id: badge for badge in ALL_BADGES}


# ========================================
# Badge Check Functions
# ========================================

def _check_domain_mastery_badges(completed_games: List[Dict[str, Any]]) -> Set[str]:
    """Check domain-specific mastery badges based on game completion"""
    earned = set()
    
    # Group games by domain
    domain_games: Dict[LifeReadinessDomain, List[Dict]] = {
        LifeReadinessDomain.finance: [],
        LifeReadinessDomain.leadership: [],
        LifeReadinessDomain.technical: [],
        LifeReadinessDomain.critical_thinking: [],
        LifeReadinessDomain.ethics: [],
    }
    
    for game in completed_games:
        game_type_str = game.get("game_type", "")
        # GAME_TYPE_TO_DOMAINS uses GameType enum keys, need to convert string to enum
        try:
            from academics.course_games import GameType as GT
            game_type_enum = GT(game_type_str)
            domains = GAME_TYPE_TO_DOMAINS.get(game_type_enum, [])
        except (ValueError, KeyError):
            domains = []
        
        score = float(game.get("score_percent", 0))
        
        for domain_str in domains:
            # Convert string domain to enum
            try:
                domain = LifeReadinessDomain(domain_str)
                domain_games[domain].append({"score": score})
            except ValueError:
                continue
    
    # Check bronze badges (5+ games, 85%+)
    for domain, games in domain_games.items():
        if len(games) >= 5:
            avg_score = sum(g["score"] for g in games) / len(games)
            if avg_score >= 85:
                badge_id = f"{domain.value}_guru_bronze" if domain == LifeReadinessDomain.finance else f"{domain.value}_master_bronze"
                if domain == LifeReadinessDomain.leadership:
                    badge_id = "leader_bronze"
                elif domain == LifeReadinessDomain.critical_thinking:
                    badge_id = "critical_thinker_bronze"
                elif domain == LifeReadinessDomain.ethics:
                    badge_id = "ethical_bronze"
                
                if badge_id in BADGES_BY_ID:
                    earned.add(badge_id)
        
        # Check silver badges (10+ games, 90%+)
        if len(games) >= 10:
            avg_score = sum(g["score"] for g in games) / len(games)
            if avg_score >= 90:
                badge_id = f"{domain.value}_guru_silver" if domain == LifeReadinessDomain.finance else f"{domain.value}_master_silver"
                if domain == LifeReadinessDomain.leadership:
                    badge_id = "leader_silver"
                
                if badge_id in BADGES_BY_ID:
                    earned.add(badge_id)
    
    return earned


def _check_volume_badges(total_games: int) -> Set[str]:
    """Check badges based on total game count"""
    earned = set()
    
    if total_games >= 50:
        earned.add("game_legend")
    if total_games >= 30:
        earned.add("game_veteran")
    if total_games >= 10:
        earned.add("game_explorer")
    
    return earned


def _check_consistency_badges(completed_games: List[Dict[str, Any]]) -> Set[str]:
    """Check consecutive performance badges"""
    earned = set()
    
    if len(completed_games) < 10:
        return earned
    
    # Check for streaks
    max_streak_70 = 0
    max_streak_75 = 0
    current_streak_70 = 0
    current_streak_75 = 0
    
    for game in completed_games:
        score = float(game.get("score_percent", 0))
        
        if score >= 70:
            current_streak_70 += 1
            max_streak_70 = max(max_streak_70, current_streak_70)
        else:
            current_streak_70 = 0
        
        if score >= 75:
            current_streak_75 += 1
            max_streak_75 = max(max_streak_75, current_streak_75)
        else:
            current_streak_75 = 0
    
    if max_streak_75 >= 20:
        earned.add("unstoppable")
    if max_streak_70 >= 10:
        earned.add("consistent_performer")
    
    return earned


def _check_excellence_badges(completed_games: List[Dict[str, Any]]) -> Set[str]:
    """Check badges for exceptional performance"""
    earned = set()
    
    if len(completed_games) < 5:
        return earned
    
    # Count perfect scores (100%)
    perfect_count = sum(1 for g in completed_games if float(g.get("score_percent", 0)) >= 100)
    if perfect_count >= 5:
        earned.add("perfectionist")
    
    # Check overall average (minimum 10 games)
    if len(completed_games) >= 10:
        avg_score = sum(float(g.get("score_percent", 0)) for g in completed_games) / len(completed_games)
        if avg_score >= 90:
            earned.add("high_achiever")
    
    return earned


def _check_domain_score_badges(domain_scores: List[DomainReadiness]) -> Set[str]:
    """Check badges based on computed domain readiness scores"""
    earned = set()
    
    for domain in domain_scores:
        if domain.score >= 95:
            earned.add("domain_master")
        if domain.score >= 90:
            earned.add("domain_expert")
    
    return earned


def _check_career_readiness_badges(overall_score: float, domain_scores: List[DomainReadiness]) -> Set[str]:
    """Check career readiness milestone badges"""
    earned = set()
    
    if overall_score >= 70:
        earned.add("career_ready")
    
    # Industry ready: 80%+ overall, all domains 60%+
    if overall_score >= 80:
        min_domain = min(d.score for d in domain_scores) if domain_scores else 0
        if min_domain >= 60:
            earned.add("industry_ready")
    
    # Elite candidate: 90%+ overall, all domains 75%+
    if overall_score >= 90:
        min_domain = min(d.score for d in domain_scores) if domain_scores else 0
        if min_domain >= 75:
            earned.add("elite_candidate")
    
    return earned


def _check_balanced_badges(domain_scores: List[DomainReadiness]) -> Set[str]:
    """Check badges for balanced skill development"""
    earned = set()
    
    if not domain_scores:
        return earned
    
    min_score = min(d.score for d in domain_scores)
    
    if min_score >= 75:
        earned.add("renaissance_student")
    if min_score >= 60:
        earned.add("well_rounded")
    
    return earned


def check_all_achievements(
    completed_games: List[Dict[str, Any]],
    overall_score: float,
    domain_scores: List[DomainReadiness],
) -> Dict[str, Any]:
    """
    Check all achievement criteria and return earned badges.
    
    Returns:
    {
        "earned_badge_ids": List[str],  # IDs of badges earned
        "badges": List[Badge],           # Full badge objects
        "newly_earned": List[str],       # NEW badges since last check (requires previous_badges param)
    }
    """
    earned_ids: Set[str] = set()
    
    # Run all badge checks
    earned_ids.update(_check_domain_mastery_badges(completed_games))
    earned_ids.update(_check_volume_badges(len(completed_games)))
    earned_ids.update(_check_consistency_badges(completed_games))
    earned_ids.update(_check_excellence_badges(completed_games))
    earned_ids.update(_check_domain_score_badges(domain_scores))
    earned_ids.update(_check_career_readiness_badges(overall_score, domain_scores))
    earned_ids.update(_check_balanced_badges(domain_scores))
    
    # Build badge objects
    badges = [BADGES_BY_ID[badge_id] for badge_id in earned_ids if badge_id in BADGES_BY_ID]
    
    # Sort by tier (highest first), then by category
    badges.sort(key=lambda b: (b.tier, b.category), reverse=True)
    
    return {
        "earned_badge_ids": list(earned_ids),
        "badges": badges,
        "total_badges_earned": len(badges),
    }


def get_newly_earned_badges(
    current_badges: List[str],
    previous_badges: List[str],
) -> List[Badge]:
    """
    Compare previous and current badge lists to find newly earned badges.
    Returns Badge objects for UI celebration.
    """
    prev_set = set(previous_badges)
    new_ids = [bid for bid in current_badges if bid not in prev_set]
    return [BADGES_BY_ID[bid] for bid in new_ids if bid in BADGES_BY_ID]
