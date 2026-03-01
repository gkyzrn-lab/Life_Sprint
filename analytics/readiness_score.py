"""
Life Readiness Score Calculator

Analyzes player's mini-game performance across skill domains to compute
a comprehensive readiness score for post-graduation life challenges.

Domains:
- Finance: money management, budgeting, investing, debt
- Leadership: management, communication, team dynamics
- Technical: domain-specific hard skills (coding, accounting, engineering)
- Critical Thinking: problem solving, decision making, analysis
- Ethics: ethical reasoning, stakeholder awareness, social responsibility
"""

from __future__ import annotations
from typing import Dict, List, Optional
from pydantic import BaseModel
from enum import Enum
from time import time

from core_domain.player.player_model import Player
from academics.course_games import GameType, BA_COURSE_GAMES, get_game_by_id


# ========================================
# Domain Enumeration
# ========================================

class LifeReadinessDomain(str, Enum):
    """The 5 key skill domains for life readiness"""
    finance = "finance"
    leadership = "leadership"
    technical = "technical"
    critical_thinking = "critical_thinking"
    ethics = "ethics"


# Map game types to skill domains
GAME_TYPE_TO_DOMAINS: Dict[GameType, List[str]] = {
    # Finance domain
    GameType.BUDGET_CHALLENGE: ["finance"],
    GameType.CALCULATOR: ["finance", "technical"],
    GameType.CASH_FLOW: ["finance"],
    GameType.PROFIT_LOSS: ["finance", "technical"],
    
    # Leadership domain
    GameType.TEAM_BUILDER: ["leadership"],
    GameType.NEGOTIATION: ["leadership", "critical_thinking"],
    GameType.SCENARIO_DECISION: ["leadership", "critical_thinking"],
    
    # Technical domain
    GameType.ACCOUNTING_BALANCE: ["technical", "finance"],
    GameType.CODE_DEBUG: ["technical", "critical_thinking"],
    GameType.CODE_TRACE: ["technical"],
    GameType.CODE_BUILDER: ["technical"],
    GameType.CIRCUIT_SIM: ["technical"],
    GameType.PHYSICS_LAB: ["technical"],
    GameType.DATA_STRUCTURE_VIZ: ["technical"],
    GameType.ALGORITHM_RACE: ["technical", "critical_thinking"],
    GameType.SYSTEM_DESIGN: ["technical", "critical_thinking"],
    
    # Critical thinking
    GameType.CASE_STUDY: ["critical_thinking", "ethics"],
    GameType.DESIGN_CHALLENGE: ["critical_thinking", "technical"],
    
    # Specialized
    GameType.MARKET_SIM: ["finance", "critical_thinking"],
    GameType.MARKETING_CAMPAIGN: ["leadership", "critical_thinking"],
    GameType.INTERACTIVE_SIM: ["critical_thinking", "technical"],
    GameType.FORCE_DIAGRAM: ["technical"],
    GameType.CAD_BUILDER: ["technical"],
    
    # Boss battles and speed challenges
    GameType.BOSS_BATTLE: ["finance", "leadership", "technical", "critical_thinking", "ethics"],
    GameType.REAL_WORLD_PROJECT: ["finance", "leadership", "technical", "critical_thinking"],
    GameType.TIMED_CHALLENGE: ["technical"],
}


class DomainReadiness(BaseModel):
    """Readiness score for a single skill domain"""
    domain: str
    score: float  # 0-100
    games_completed: int
    recent_performance: float  # weighted average of recent scores
    trend: str  # "improving", "stable", "declining"


class LifeReadinessScore(BaseModel):
    """Comprehensive life readiness analytics"""
    overall_score: float  # 0-100 weighted average across domains
    domains: List[DomainReadiness]
    total_games_completed: int
    average_game_score: float
    readiness_level: str  # "beginner", "developing", "proficient", "expert"
    strengths: List[str]  # top 2 domains
    areas_for_growth: List[str]  # bottom 2 domains
    
    # Career readiness indicators
    career_ready: bool  # True if overall_score >= 70
    career_salary_impact: float  # Estimated salary multiplier based on readiness
    score_change_since_last_snapshot: float  # positive/negative delta vs previous snapshot
    momentum: str  # "up" | "flat" | "down"
    next_readiness_target: float  # next major readiness milestone (50/70/85/100)
    points_to_next_target: float  # points needed to reach next milestone
    coaching_tip: str  # personalized guidance message
    recommended_next_games: List[Dict[str, str]]  # Specific game recommendations with reasons
    achievement_badges: List[str]  # Badge IDs earned
    newly_earned_badges: List[str]  # NEW badges since last check


def _compute_domain_score(completed_games: List[Dict], domain: str) -> DomainReadiness:
    """
    Calculate readiness score for a single domain.
    
    Scoring:
    - Recent games weighted more heavily (exponential decay: latest game = 1.0x, 10 games ago = 0.5x)
    - Considers both accuracy and consistency
    - Minimum 3 games required for reliable score
    """
    # Filter games that contribute to this domain
    relevant_games = []
    for game in completed_games:
        game_type_str = game.get("game_type", "")
        try:
            game_type = GameType(game_type_str)
            domains = GAME_TYPE_TO_DOMAINS.get(game_type, [])
            if domain in domains:
                relevant_games.append(game)
        except (ValueError, KeyError):
            continue
    
    games_count = len(relevant_games)
    if games_count == 0:
        return DomainReadiness(
            domain=domain,
            score=0.0,
            games_completed=0,
            recent_performance=0.0,
            trend="unknown"
        )
    
    # Sort by completion order (oldest first)
    relevant_games = sorted(relevant_games, key=lambda g: g.get("completed_at", 0))
    
    # Calculate weighted score (recent games weighted more)
    weighted_sum = 0.0
    weight_sum = 0.0
    
    for idx, game in enumerate(relevant_games):
        score_pct = float(game.get("score_percent", 0.0))
        # Weight decays exponentially from oldest (0) to newest (games_count-1)
        # Latest game has weight 1.0, older games decay
        recency_factor = 0.5 + 0.5 * (idx / max(1, games_count - 1))
        
        weighted_sum += score_pct * recency_factor
        weight_sum += recency_factor
    
    recent_performance = weighted_sum / weight_sum if weight_sum > 0 else 0.0
    
    # Calculate trend (compare last 3 vs first 3 if enough data)
    trend = "stable"
    if games_count >= 6:
        first_three = sum(float(g.get("score_percent", 0)) for g in relevant_games[:3]) / 3
        last_three = sum(float(g.get("score_percent", 0)) for g in relevant_games[-3:]) / 3
        diff = last_three - first_three
        if diff >= 10:
            trend = "improving"
        elif diff <= -10:
            trend = "declining"
    elif games_count >= 3:
        first_avg = sum(float(g.get("score_percent", 0)) for g in relevant_games[:2]) / 2
        last_avg = sum(float(g.get("score_percent", 0)) for g in relevant_games[-2:]) / 2
        diff = last_avg - first_avg
        if diff >= 12:
            trend = "improving"
        elif diff <= -12:
            trend = "declining"
    
    # Adjust score based on consistency (penalty for high variance)
    scores = [float(g.get("score_percent", 0)) for g in relevant_games]
    if games_count >= 3:
        avg = sum(scores) / games_count
        variance = sum((s - avg) ** 2 for s in scores) / games_count
        std_dev = variance ** 0.5
        # High variance (inconsistent performance) reduces score slightly
        consistency_factor = max(0.9, 1.0 - (std_dev / 200.0))  # max 10% penalty
        recent_performance *= consistency_factor
    
    # Minimum games bonus (reward thorough practice)
    if games_count >= 10:
        recent_performance = min(100.0, recent_performance * 1.05)  # 5% bonus for 10+ games
    
    return DomainReadiness(
        domain=domain,
        score=round(recent_performance, 1),
        games_completed=games_count,
        recent_performance=round(recent_performance, 1),
        trend=trend
    )


def calculate_life_readiness_score(player: Player) -> LifeReadinessScore:
    """
    Calculate comprehensive life readiness score from player's mini-game history.
    
    Returns analytics dashboard data with overall score and domain breakdown.
    """
    completed = player.completed_games
    total_games = len(completed)
    
    # Calculate domain scores
    domains_to_check = ["finance", "leadership", "technical", "critical_thinking", "ethics"]
    domain_scores: List[DomainReadiness] = []
    
    for domain in domains_to_check:
        domain_score = _compute_domain_score(completed, domain)
        if domain_score.games_completed > 0:  # Only include domains with games
            domain_scores.append(domain_score)
    
    # Calculate overall score (weighted by domain importance)
    # Weight critical life skills higher
    domain_weights = {
        "finance": 0.30,        # 30% weight - critical for life
        "leadership": 0.25,     # 25% weight - interpersonal skills
        "technical": 0.20,      # 20% weight - career-specific
        "critical_thinking": 0.20,  # 20% weight - problem solving
        "ethics": 0.05,         # 5% weight - moral reasoning
    }
    
    overall_weighted_sum = 0.0
    overall_weight_sum = 0.0
    
    for domain_result in domain_scores:
        weight = domain_weights.get(domain_result.domain, 0.1)
        overall_weighted_sum += domain_result.score * weight
        overall_weight_sum += weight
    
    overall_score = overall_weighted_sum / overall_weight_sum if overall_weight_sum > 0 else 0.0
    
    # Calculate average game score across all games
    if total_games > 0:
        avg_game_score = sum(float(g.get("score_percent", 0)) for g in completed) / total_games
    else:
        avg_game_score = 0.0
    
    # Determine readiness level
    if overall_score >= 85:
        readiness_level = "expert"
    elif overall_score >= 70:
        readiness_level = "proficient"
    elif overall_score >= 50:
        readiness_level = "developing"
    else:
        readiness_level = "beginner"
    
    # Identify strengths and areas for growth
    sorted_domains = sorted(domain_scores, key=lambda d: d.score, reverse=True)
    strengths = [d.domain for d in sorted_domains[:2]] if len(sorted_domains) >= 2 else [d.domain for d in sorted_domains]
    areas_for_growth = [d.domain for d in sorted_domains[-2:]] if len(sorted_domains) >= 2 else []
    
    # Career readiness check
    career_ready = overall_score >= 70.0
    
    # Career salary impact (readiness translates to earning potential)
    # Scale: 50 score = 0.85x salary, 70 score = 1.0x, 90+ score = 1.2x
    if overall_score < 50:
        career_salary_impact = 0.85 + (overall_score / 50) * 0.15  # 0.85-1.0 range
    elif overall_score < 70:
        career_salary_impact = 1.0 + ((overall_score - 50) / 20) * 0.0  # stay at 1.0
    else:
        career_salary_impact = 1.0 + ((overall_score - 70) / 20) * 0.2  # 1.0-1.2 range
    
    career_salary_impact = round(career_salary_impact, 2)

    # ========================================
    # NEW: Momentum + Coaching Insights
    # ========================================
    existing_history = player.readiness_history if hasattr(player, "readiness_history") and player.readiness_history else []
    previous_score = None
    if existing_history:
        previous_score = float(existing_history[-1].get("overall_score", overall_score))

    score_change_since_last_snapshot = 0.0 if previous_score is None else round(overall_score - previous_score, 1)

    if score_change_since_last_snapshot >= 3.0:
        momentum = "up"
    elif score_change_since_last_snapshot <= -3.0:
        momentum = "down"
    else:
        momentum = "flat"

    # Next milestone target for motivation
    if overall_score < 50:
        next_readiness_target = 50.0
    elif overall_score < 70:
        next_readiness_target = 70.0
    elif overall_score < 85:
        next_readiness_target = 85.0
    else:
        next_readiness_target = 100.0

    points_to_next_target = round(max(0.0, next_readiness_target - overall_score), 1)
    
    # ========================================
    # IMPROVEMENT #1: Specific Game Recommendations
    # ========================================
    recommended_next_games: List[Dict[str, str]] = []
    weak_domain = areas_for_growth[0] if areas_for_growth else None
    
    if weak_domain:
        
        # Find games that train the weak domain
        candidate_games = []
        for course_games in BA_COURSE_GAMES.values():
            for mini_game in course_games:
                domains = GAME_TYPE_TO_DOMAINS.get(mini_game.game_type, [])
                if weak_domain in domains:
                    # Score game by difficulty match
                    # Get player's level in this domain
                    domain_obj = next((d for d in domain_scores if d.domain == weak_domain), None)
                    player_level = domain_obj.score if domain_obj else 50
                    
                    # Estimate game difficulty from questions
                    avg_difficulty = sum(q.difficulty for q in mini_game.questions) / len(mini_game.questions) if mini_game.questions else 3
                    # Map difficulty (1-5) to score range (20-100)
                    game_difficulty_score = 20 + (avg_difficulty - 1) * 20
                    
                    # Score match: prefer games slightly harder than current level
                    # Perfect match: game is 5-15 points harder
                    difficulty_diff = game_difficulty_score - player_level
                    if -10 <= difficulty_diff <= 20:
                        match_quality = 100 - abs(difficulty_diff - 10)  # peak at +10 difficulty
                    else:
                        match_quality = max(0, 100 - abs(difficulty_diff) * 2)
                    
                    candidate_games.append({
                        "game_id": mini_game.id,
                        "title": mini_game.title,
                        "course_id": mini_game.course_id,
                        "difficulty": avg_difficulty,
                        "match_score": match_quality,
                        "reason": f"Improves {weak_domain} - {'Easy' if difficulty_diff < -10 else 'Good match' if difficulty_diff <= 10 else 'Challenge'}"
                    })
        
        # Sort by match quality and take top 5
        candidate_games.sort(key=lambda g: g["match_score"], reverse=True)
        for game in candidate_games[:5]:
            recommended_next_games.append({
                "game_id": game["game_id"],
                "title": game["title"],
                "course_id": game["course_id"],
                "reason": game["reason"],
            })

    # Personalized coaching tip
    if total_games < 3:
        coaching_tip = "Complete at least 3 mini-games to unlock reliable coaching insights."
    elif momentum == "down" and weak_domain:
        coaching_tip = f"Your momentum dipped. Focus on {weak_domain.replace('_', ' ')} practice this week to recover quickly."
    elif momentum == "up" and points_to_next_target > 0:
        coaching_tip = f"Great momentum. You're only {points_to_next_target:.1f} points from your next readiness milestone ({next_readiness_target:.0f})."
    elif weak_domain:
        coaching_tip = f"Steady progress. Prioritize {weak_domain.replace('_', ' ')} games for the fastest score gains."
    else:
        coaching_tip = "Keep your streak alive with one focused practice session this week."
    
    # ========================================
    # IMPROVEMENT #2: Achievement Badge System
    # ========================================
    from analytics.achievement_badges import check_all_achievements, get_newly_earned_badges
    
    achievement_result = check_all_achievements(completed, overall_score, domain_scores)
    current_badge_ids = achievement_result["earned_badge_ids"]
    
    # Compare with player's previous badges to find newly earned
    previous_badge_ids = player.earned_badges if hasattr(player, 'earned_badges') else []
    newly_earned = get_newly_earned_badges(current_badge_ids, previous_badge_ids)
    newly_earned_ids = [b.id for b in newly_earned]
    
    # Update player's badge collection
    player.earned_badges = current_badge_ids
    
    # ========================================
    # IMPROVEMENT #3: Historical Trend Tracking
    # ========================================
    # Record snapshot for this calculation
    snapshot = {
        "semester": player.semester,
        "overall_score": round(overall_score, 1),
        "domains": {d.domain: round(d.score, 1) for d in domain_scores},
        "total_games": total_games,
        "timestamp": int(time()),
    }
    
    # Append to history (limit to last 16 semesters for performance)
    if not hasattr(player, 'readiness_history') or player.readiness_history is None:
        player.readiness_history = []
    
    # Only add snapshot if semester changed or significant time passed
    should_snapshot = True
    if player.readiness_history:
        last_snapshot = player.readiness_history[-1]
        if last_snapshot.get("semester") == player.semester and last_snapshot.get("total_games") == total_games:
            should_snapshot = False  # Same semester, no new games
    
    if should_snapshot:
        player.readiness_history.append(snapshot)
        # Keep only last 16 snapshots
        if len(player.readiness_history) > 16:
            player.readiness_history = player.readiness_history[-16:]
    
    return LifeReadinessScore(
        overall_score=round(overall_score, 1),
        domains=domain_scores,
        total_games_completed=total_games,
        average_game_score=round(avg_game_score, 1),
        readiness_level=readiness_level,
        strengths=strengths,
        areas_for_growth=areas_for_growth,
        career_ready=career_ready,
        career_salary_impact=career_salary_impact,
        score_change_since_last_snapshot=score_change_since_last_snapshot,
        momentum=momentum,
        next_readiness_target=next_readiness_target,
        points_to_next_target=points_to_next_target,
        coaching_tip=coaching_tip,
        recommended_next_games=recommended_next_games,
        achievement_badges=current_badge_ids,
        newly_earned_badges=newly_earned_ids,
    )
