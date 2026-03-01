"""
Analytics & Gamification System

Provides:
- Player progression tracking and leaderboards
- Career milestone achievements
- Achievement systems and badge unlocking
- Analytics dashboards for progress
- Impact tracking (decisions → outcomes correlation)
- Gamification mechanics (XP, leveling, streaks)
"""

from typing import Dict, List, Any, Optional
from uuid import uuid4
from datetime import datetime
from collections import defaultdict

from core_domain.player.player_model import Player


class PlayerAnalytics:
    """Tracks comprehensive player analytics."""
    
    def __init__(self, player_id: str):
        self.player_id = player_id
        self.started_date = datetime.now()
        self.total_playtime_hours = 0.0
        self.total_decisions_made = 0
        self.total_xp_earned = 0
        self.level = 1
        self.current_streak_days = 0
        self.achievements_unlocked = []
        self.career_milestones_reached = []
        self.decision_outcomes = []  # Track decision → outcome correlations


class GameProgress:
    """Tracks game progression metrics."""
    
    def __init__(self, player_id: str):
        self.player_id = player_id
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 1000
        self.total_xp = 0
        self.rank_percentile = 50.0
        self.badges_earned = []
        self.streaks = {
            "study_days": 0,
            "workout_days": 0,
            "planning_days": 0,
            "community_engagement_days": 0,
        }


# XP and Leveling System
XP_SYSTEM: Dict[str, Dict[str, Any]] = {
    "daily_login": {"xp": 10, "description": "Log in daily"},
    "complete_assignment": {"xp": 50, "description": "Complete course assignment"},
    "pass_exam": {"xp": 200, "description": "Pass exam"},
    "plan_semester": {"xp": 100, "description": "Plan semester"},
    "join_study_group": {"xp": 75, "description": "Join study group"},
    "attend_networking": {"xp": 150, "description": "Attend networking event"},
    "complete_project": {"xp": 300, "description": "Complete collaborative project"},
    "help_peer": {"xp": 80, "description": "Help peer with assignment"},
    "unlock_achievement": {"xp": 120, "description": "Unlock achievement"},
    "reach_milestone": {"xp": 500, "description": "Reach career milestone"},
}

# Achievement System
ACHIEVEMENT_CATALOG: Dict[str, Dict[str, Any]] = {
    "first_steps": {
        "name": "First Steps",
        "description": "Complete your first semester",
        "icon": "👣",
        "rarity": "Common",
        "xp_reward": 100,
        "condition": "Complete semester 1",
    },
    "honor_student": {
        "name": "Honor Student",
        "description": "Achieve 3.8+ GPA",
        "icon": "🎓",
        "rarity": "Rare",
        "xp_reward": 250,
        "condition": "GPA >= 3.8",
    },
    "financial_master": {
        "name": "Financial Master",
        "description": "Graduate debt-free",
        "icon": "💰",
        "rarity": "Rare",
        "xp_reward": 300,
        "condition": "Graduate with <= $0 debt",
    },
    "well_balanced": {
        "name": "Well-Balanced",
        "description": "Maintain 50+ happiness while studying",
        "icon": "⚖️",
        "rarity": "Rare",
        "xp_reward": 200,
        "condition": "Happiness >= 50 for 4 semesters",
    },
    "networking_pro": {
        "name": "Networking Pro",
        "description": "Attend 5+ networking events",
        "icon": "🤝",
        "rarity": "Uncommon",
        "xp_reward": 150,
        "condition": "Attend 5 networking events",
    },
    "study_buddy": {
        "name": "Study Buddy",
        "description": "Join 3+ study groups",
        "icon": "📚",
        "rarity": "Uncommon",
        "xp_reward": 120,
        "condition": "Join 3 study groups",
    },
    "career_changer": {
        "name": "Career Changer",
        "description": "Change career plans 3+ times",
        "icon": "🔄",
        "rarity": "Common",
        "xp_reward": 80,
        "condition": "Change career path 3 times",
    },
    "speedrunner": {
        "name": "Speedrunner",
        "description": "Graduate in 4 years with 3.5+ GPA",
        "icon": "⚡",
        "rarity": "Legendary",
        "xp_reward": 500,
        "condition": "Graduate with GPA 3.5+",
    },
    "renaissance_student": {
        "name": "Renaissance Student",
        "description": "Master 3+ different skill areas",
        "icon": "🎨",
        "rarity": "Rare",
        "xp_reward": 250,
        "condition": "Develop expertise in 3+ areas",
    },
    "mentor_legend": {
        "name": "Mentor Legend",
        "description": "Help 10+ students through mentoring",
        "icon": "👑",
        "rarity": "Legendary",
        "xp_reward": 400,
        "condition": "Mentor 10 students",
    },
}

# Career Milestone Achievements
CAREER_MILESTONES: List[Dict[str, Any]] = [
    {
        "milestone": "Internship Secured",
        "description": "Land first internship",
        "gpa_requirement": 3.3,
        "semester_requirement": 2,
        "xp_reward": 300,
        "icon": "💼",
        "career_impact": "Increases job offer probability by 30%",
    },
    {
        "milestone": "Leadership Role",
        "description": "Become guild officer or project lead",
        "gpa_requirement": 3.2,
        "semester_requirement": 3,
        "xp_reward": 250,
        "icon": "👔",
        "career_impact": "Salary: +$5K",
    },
    {
        "milestone": "Published Work",
        "description": "Publish research or contribute to open source",
        "gpa_requirement": 3.5,
        "semester_requirement": 4,
        "xp_reward": 400,
        "icon": "📄",
        "career_impact": "+15% salary negotiation power",
    },
    {
        "milestone": "Industry Recognized",
        "description": "Gain industry certification or award",
        "gpa_requirement": 3.4,
        "semester_requirement": 5,
        "xp_reward": 350,
        "icon": "🏆",
        "career_impact": "+20% job competitiveness",
    },
    {
        "milestone": "Ready for Graduation",
        "description": "Complete all degree requirements",
        "gpa_requirement": 3.0,
        "semester_requirement": 8,
        "xp_reward": 1000,
        "icon": "🎓",
        "career_impact": "Unlocks senior roles and salaries",
    },
]

# Leaderboard Categories
LEADERBOARD_CATEGORIES: List[str] = [
    "overall_xp",
    "gpa",
    "career_readiness",
    "community_impact",
    "financial_health",
    "happiness",
    "graduation_readiness",
]

# Streak Bonuses
STREAK_BONUSES: Dict[int, Dict[str, Any]] = {
    7: {"name": "Week Warrior", "xp_multiplier": 1.1, "description": "7-day streak"},
    14: {"name": "Fortnight Fighter", "xp_multiplier": 1.2, "description": "14-day streak"},
    30: {"name": "Month Master", "xp_multiplier": 1.3, "description": "30-day streak"},
    100: {"name": "Century Champion", "xp_multiplier": 1.5, "description": "100-day streak"},
}

# Decision Impact Tracking
DECISION_CATEGORIES: Dict[str, List[str]] = {
    "academic": ["course_selection", "study_strategy", "exam_preparation"],
    "financial": ["borrowing", "spending", "earning"],
    "health": ["exercise", "sleep", "nutrition"],
    "social": ["networking", "mentoring", "community"],
    "career": ["internship", "job_search", "skill_building"],
}


# ==============================================================================
# Service Functions
# ==============================================================================

def calculate_player_rank(player: Player, all_players: List[Player] = None) -> Dict[str, Any]:
    """
    Calculate player's rank across multiple metrics.
    
    Metrics:
    - Overall XP/Level
    - GPA (academic success)
    - Career Readiness (skills, experience, network)
    - Community Impact (mentoring, guilds, projects)
    - Financial Health (debt/savings ratio)
    - Happiness/Wellbeing
    """
    if all_players is None:
        all_players = [player]  # Fallback for single-player ranking
    
    rank_data = {
        "player_id": player.id,
        "player_name": player.name,
        "metrics": {
            "gpa_percentile": 65.0 + (getattr(player, 'hs_gpa', 3.0) - 3.0) * 10,
            "happiness_percentile": 50.0,  # Would be calculated from actual stats
            "career_readiness": 45.0,  # Based on major, year, experience
            "financial_health": 60.0,  # Debt/savings ratio
            "community_engagement": 55.0,  # Guild/mentorship/projects
        },
        "overall_rank_percentile": 55.0,
    }
    
    return rank_data


def get_leaderboard(category: str, limit: int = 10) -> List[Dict[str, Any]]:
    """
    Get leaderboard for a specific category.
    
    Returns top players in:
    - Overall XP/Level
    - GPA
    - Career Readiness
    - Community Impact
    - Financial Health
    - Happiness
    - Graduation Readiness
    """
    if category not in LEADERBOARD_CATEGORIES:
        return []
    
    # Simulated leaderboard data
    leaderboard = [
        {
            "rank": 1,
            "name": "Alex Chen",
            "major": "Computer Science",
            "semester": 6,
            "value": 4.0 if category == "gpa" else 15750 if category == "overall_xp" else 92,
            "badge": "🏆",
        },
        {
            "rank": 2,
            "name": "Priya Patel",
            "major": "Finance",
            "semester": 5,
            "value": 3.95 if category == "gpa" else 14200 if category == "overall_xp" else 88,
            "badge": "🥈",
        },
        {
            "rank": 3,
            "name": "Jordan Smith",
            "major": "Data Science",
            "semester": 7,
            "value": 3.9 if category == "gpa" else 13500 if category == "overall_xp" else 85,
            "badge": "🥉",
        },
    ]
    
    return leaderboard[:limit]


def calculate_decision_impact(decision_type: str, outcome: str) -> Dict[str, float]:
    """
    Calculate the impact of a player decision on various stats.
    
    Decision Categories:
    - Academic (course selection, study strategy, exam prep)
    - Financial (borrowing, spending, earning)
    - Health (exercise, sleep, nutrition)
    - Social (networking, mentoring, community)
    - Career (internship, job search, skill building)
    """
    impact_map = {
        "academic": {
            "positive": {"gpa": 0.15, "confidence": 10, "stress": -5},
            "negative": {"gpa": -0.25, "happiness": -15, "stress": 20},
        },
        "financial": {
            "positive": {"balance": 5000, "confidence": 15, "stress": -10},
            "negative": {"balance": -5000, "stress": 25, "happiness": -20},
        },
        "health": {
            "positive": {"happiness": 20, "stress": -15, "confidence": 10},
            "negative": {"stress": 20, "happiness": -25, "burnout": 15},
        },
        "social": {
            "positive": {"happiness": 15, "network": 5, "confidence": 10},
            "negative": {"happiness": -10, "stress": 5},
        },
        "career": {
            "positive": {"confidence": 25, "xp": 200, "network": 8},
            "negative": {"confidence": -20, "stress": 15},
        },
    }
    
    category = decision_type.lower()
    outcome_key = "positive" if outcome.lower() == "success" else "negative"
    
    return impact_map.get(category, {}).get(outcome_key, {})


def unlock_achievement(player: Player, achievement_id: str) -> Dict[str, Any]:
    """
    Unlock an achievement for a player.
    """
    if achievement_id not in ACHIEVEMENT_CATALOG:
        return {"error": "Achievement not found"}
    
    achievement = ACHIEVEMENT_CATALOG[achievement_id]
    
    return {
        "status": "unlocked",
        "achievement_name": achievement["name"],
        "description": achievement["description"],
        "icon": achievement["icon"],
        "xp_earned": achievement["xp_reward"],
        "rarity": achievement["rarity"],
        "message": f"🎉 You unlocked: {achievement['name']}!",
    }


def calculate_graduation_readiness(player: Player) -> Dict[str, Any]:
    """
    Calculate player's readiness for graduation.
    
    Measures:
    - Academic completion (GPA, credits)
    - Career readiness (experience, network, skills)
    - Financial health (debt management)
    - Emotional wellness (happiness, burnout)
    """
    gpa = getattr(player, 'hs_gpa', 3.0)
    semester = getattr(player, 'semester', 1)
    
    academic_readiness = min(100, (semester / 8) * 100 + (gpa / 4.0) * 20)
    career_readiness = 45 + (semester - 1) * 8  # Increases each semester
    financial_readiness = 70  # Depends on debt, would need actual calculation
    wellness_readiness = 60  # Depends on happiness/burnout
    
    overall_readiness = (academic_readiness + career_readiness + financial_readiness + wellness_readiness) / 4
    
    return {
        "overall_readiness": min(100, overall_readiness),
        "academic_readiness": min(100, academic_readiness),
        "career_readiness": min(100, career_readiness),
        "financial_readiness": min(100, financial_readiness),
        "wellness_readiness": min(100, wellness_readiness),
        "estimated_graduation_confidence": "High" if overall_readiness >= 75 else "Medium" if overall_readiness >= 50 else "Low",
    }


def get_player_analytics_dashboard(player: Player) -> Dict[str, Any]:
    """
    Get comprehensive analytics dashboard for a player.
    """
    return {
        "player_id": player.id,
        "player_name": player.name,
        "joined_date": "Aug 15, 2024",  # Would be from player.created_date
        "playtime_hours": 120,
        "level": 5,
        "total_xp": 4250,
        "rank_percentile": 72,
        "key_metrics": {
            "gpa": getattr(player, 'hs_gpa', 3.0),
            "semester": getattr(player, 'semester', 1),
            "major": getattr(player, 'major_id', 'unknown'),
            "happiness": 65,
            "stress": 45,
            "burnout": 30,
        },
        "achievements_earned": 8,
        "career_milestones_reached": 2,
        "decision_success_rate": "72%",
        "next_goal": "Reach 5000 XP (89% progress)",
    }
