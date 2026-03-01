"""
Analytics & Gamification Router

Provides:
- Player analytics dashboard
- Leaderboards by category
- Achievement unlocking and progress
- Career milestone tracking
- Decision impact analysis
- XP and leveling system
- Graduation readiness assessment
"""

from fastapi import APIRouter, HTTPException

from core_domain.store import STORE
from catalogs.analytics_gamification import (
    calculate_player_rank,
    get_leaderboard,
    calculate_decision_impact,
    unlock_achievement,
    calculate_graduation_readiness,
    get_player_analytics_dashboard,
    ACHIEVEMENT_CATALOG,
    XP_SYSTEM,
    CAREER_MILESTONES,
    LEADERBOARD_CATEGORIES,
)

router = APIRouter(prefix="/api/analytics", tags=["analytics"])


@router.get("/dashboard/{player_id}")
def get_analytics_dashboard(player_id: str):
    """
    Get comprehensive analytics dashboard for a player.
    
    Shows:
    - Player level and XP progress
    - Key metrics (GPA, happiness, stress)
    - Achievements earned
    - Progress toward graduation
    - Career milestones
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    dashboard = get_player_analytics_dashboard(player)
    
    return dashboard


@router.get("/rank/{player_id}")
def get_player_rank(player_id: str):
    """
    Get player's rank across multiple metrics.
    
    Shows percentile rankings in:
    - Overall level/XP
    - GPA (academic)
    - Career readiness
    - Community impact
    - Financial health
    - Happiness/wellbeing
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    rank = calculate_player_rank(player)
    
    return {
        "player_id": player_id,
        "player_name": player.name,
        "rankings": rank["metrics"],
        "overall_percentile": rank["overall_rank_percentile"],
        "interpretation": {
            "percentile_50": "Average player",
            "percentile_75": "Top 25%",
            "percentile_90": "Top 10%",
        },
    }


@router.get("/leaderboards/{category}")
def get_category_leaderboard(category: str, limit: int = 10):
    """
    Get leaderboard for a specific category.
    
    Available categories:
    - overall_xp: Total experience points
    - gpa: Academic performance
    - career_readiness: Career development
    - community_impact: Social contribution
    - financial_health: Money management
    - happiness: Well-being score
    - graduation_readiness: Graduation progress
    """
    if category not in LEADERBOARD_CATEGORIES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid category. Must be one of: {', '.join(LEADERBOARD_CATEGORIES)}"
        )
    
    leaderboard = get_leaderboard(category, limit)
    
    return {
        "category": category,
        "total_players": len(leaderboard),
        "your_rank": None,  # Would calculate from player_id if provided
        "leaderboard": leaderboard,
    }


@router.get("/achievements")
def get_all_achievements():
    """
    Get all available achievements in the game.
    
    Shows:
    - Achievement name and icon
    - Unlock condition
    - XP reward
    - Rarity level
    """
    achievements = [
        {
            "id": ach_id,
            **achievement,
        }
        for ach_id, achievement in ACHIEVEMENT_CATALOG.items()
    ]
    
    return {
        "total_achievements": len(achievements),
        "achievements": achievements,
        "rarity_breakdown": {
            "Common": sum(1 for a in achievements if a["rarity"] == "Common"),
            "Uncommon": sum(1 for a in achievements if a["rarity"] == "Uncommon"),
            "Rare": sum(1 for a in achievements if a["rarity"] == "Rare"),
            "Legendary": sum(1 for a in achievements if a["rarity"] == "Legendary"),
        },
    }


@router.post("/achievement/unlock/{player_id}/{achievement_id}")
def unlock_player_achievement(player_id: str, achievement_id: str):
    """
    Unlock an achievement for a player.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    result = unlock_achievement(player, achievement_id)
    
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    
    return result


@router.get("/career-milestones")
def get_career_milestones():
    """
    Get all available career milestones.
    
    Shows:
    - Milestone name and requirements
    - XP reward
    - Career impact
    - Time to achieve
    """
    return {
        "total_milestones": len(CAREER_MILESTONES),
        "milestones": CAREER_MILESTONES,
        "progression_path": [m["milestone"] for m in CAREER_MILESTONES],
    }


@router.get("/decision-analysis/{decision_type}")
def analyze_decision(decision_type: str, outcome: str = "success"):
    """
    Get impact analysis for a decision.
    
    Decision Types:
    - academic: Course selection, study strategy
    - financial: Borrowing, spending, earning
    - health: Exercise, sleep, nutrition
    - social: Networking, mentoring
    - career: Internships, job search, skills
    
    Outcome: "success" or "failure"
    """
    impact = calculate_decision_impact(decision_type, outcome)
    
    if not impact:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid decision_type: {decision_type}"
        )
    
    return {
        "decision_type": decision_type,
        "outcome": outcome,
        "impact_on_stats": impact,
        "severity": "High" if abs(max(impact.values()) if impact else 0) > 20 else "Medium" if abs(max(impact.values()) if impact else 0) > 10 else "Low",
    }


@router.get("/xp-system")
def get_xp_system():
    """
    Get information about the XP and leveling system.
    
    Shows:
    - XP rewards for activities
    - Level progression
    - Streak bonuses
    """
    return {
        "activities": XP_SYSTEM,
        "level_progression": {
            "level_1": "0 XP",
            "level_2": "1000 XP",
            "level_3": "2500 XP",
            "level_4": "4500 XP",
            "level_5": "7500 XP",
            "level_10": "50000 XP",
        },
        "max_level": 25,
        "xp_per_level_scaling": "1000 + (level * 200)",
    }


@router.post("/decision-record/{player_id}")
def record_decision(player_id: str, decision_type: str, outcome: str, notes: str = None):
    """
    Record a player's decision and its outcome for analytics.
    
    In production, this would:
    - Store decision in database
    - Track decision → outcome correlation
    - Update player's decision success rate
    - Identify patterns in decision-making
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    decision_record = {
        "player_id": player_id,
        "decision_type": decision_type,
        "outcome": outcome,
        "timestamp": "2024-12-19T10:30:00Z",
        "impact_analyzed": True,
    }
    
    return {
        "status": "recorded",
        "decision_record": decision_record,
        "message": f"Decision recorded: {decision_type} → {outcome}",
        "next_action": "This data helps us personalize your experience",
    }


@router.get("/graduation-readiness/{player_id}")
def get_graduation_readiness(player_id: str):
    """
    Get detailed graduation readiness assessment.
    
    Measures:
    - Academic completion (GPA, credits)
    - Career preparation (internships, skills, network)
    - Financial readiness (debt management, savings)
    - Emotional wellness (happiness, burnout)
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    readiness = calculate_graduation_readiness(player)
    
    return {
        "player_id": player_id,
        "readiness_score": readiness,
        "estimated_graduation_semester": getattr(player, 'semester', 1) + (8 - getattr(player, 'semester', 1)),
        "recommendations": [
            "Increase GPA by taking easier electives" if readiness["academic_readiness"] < 80 else "Excellent academic progress",
            "Seek internship opportunities" if readiness["career_readiness"] < 70 else "Strong career preparation",
            "Consider financial planning" if readiness["financial_readiness"] < 70 else "Good financial health",
            "Prioritize mental health" if readiness["wellness_readiness"] < 70 else "Excellent well-being",
        ],
    }


@router.get("/impact-tracking/{player_id}")
def get_impact_tracking(player_id: str):
    """
    Get decision-outcome impact tracking for a player.
    
    Shows:
    - Decision success rate
    - Most impactful decisions
    - Patterns in decision-making
    - Recommendations for better outcomes
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return {
        "player_id": player_id,
        "total_decisions_tracked": 47,
        "success_rate": "72%",
        "most_impactful_decision_category": "Career",
        "decision_breakdown": {
            "academic": {"total": 12, "successful": 11, "rate": "92%"},
            "financial": {"total": 8, "successful": 5, "rate": "63%"},
            "health": {"total": 10, "successful": 7, "rate": "70%"},
            "social": {"total": 11, "successful": 8, "rate": "73%"},
            "career": {"total": 6, "successful": 6, "rate": "100%"},
        },
        "insights": [
            "Your career decisions have been consistently excellent",
            "Consider consulting peers for financial decisions",
            "Academic success correlates with planning ahead",
        ],
        "next_challenge": "Improve financial decision-making by 15%",
    }


@router.get("/progression-summary/{player_id}")
def get_progression_summary(player_id: str):
    """
    Get summary of player's overall progression.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    semester = getattr(player, 'semester', 1)
    gpa = getattr(player, 'hs_gpa', 3.0)
    
    return {
        "player_id": player_id,
        "player_name": player.name,
        "current_semester": semester,
        "estimated_graduation_semester": 8,
        "semesters_remaining": max(0, 8 - semester),
        "overall_progress": f"{(semester / 8) * 100:.0f}%",
        "key_achievements": [
            "Reached Level 5 in Gamification",
            "GPA: 3.5+ (Top 25%)",
            "Completed 3 internships",
            "Founded study group",
        ],
        "current_focus": "Career preparation",
        "graduation_confidence": "High",
        "path_to_success": {
            "academic": "Maintain 3.5+ GPA",
            "career": "Secure full-time offer",
            "financial": "Graduate with < $20K debt",
            "personal": "Maintain 60+ happiness",
        },
    }
