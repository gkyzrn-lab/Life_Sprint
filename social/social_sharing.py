"""
Social Sharing & Achievement System

Achievements, badges, and social proof sharing.
"""

from __future__ import annotations
from typing import List, Dict, Optional, Set, Any
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
from uuid import uuid4


# =========================
# Enums
# =========================

class AchievementCategory(str, Enum):
    """Achievement categories."""
    academic = "academic"
    financial = "financial"
    health = "health"
    social = "social"
    milestone = "milestone"
    challenge = "challenge"


class AchievementRarity(str, Enum):
    """Achievement rarity/difficulty."""
    common = "common"       # 25%+ of players
    uncommon = "uncommon"   # 10-25% of players
    rare = "rare"           # 5-10% of players
    epic = "epic"           # 1-5% of players
    legendary = "legendary" # <1% of players


# =========================
# Models
# =========================

class Achievement(BaseModel):
    """Achievement definition."""
    id: str
    name: str
    description: str
    category: AchievementCategory
    rarity: AchievementRarity
    icon_url: str  # emoji or image URL
    points: int  # XP reward
    requirements: Dict[str, Any]  # conditions to unlock
    unlock_condition_text: str  # human-readable condition


class PlayerAchievement(BaseModel):
    """Player's earned achievement."""
    achievement_id: str
    player_id: str
    unlocked_at: datetime = Field(default_factory=datetime.now)
    progress: float = 0.0  # 0-100 for partial progress


class Badge(BaseModel):
    """Visual badge earned by player."""
    id: str
    name: str
    description: str
    icon_emoji: str
    color: str  # hex color
    rarity: AchievementRarity
    unlocked: bool = False
    unlocked_at: Optional[datetime] = None


class ShareableAchievement(BaseModel):
    """Achievement formatted for social sharing."""
    achievement_name: str
    achievement_description: str
    icon: str
    rarity: str
    player_name: str
    timestamp: datetime
    share_text: str
    
    @property
    def twitter_text(self) -> str:
        """Format for Twitter/X."""
        return f"🎮 I unlocked '{self.achievement_name}' in Life Sprint! {self.icon} #LifeSprint #Achievement"
    
    @property
    def facebook_text(self) -> str:
        """Format for Facebook."""
        return f"Just unlocked {self.icon} {self.achievement_name} - {self.achievement_description} in Life Sprint!"
    
    @property
    def linked_in_text(self) -> str:
        """Format for LinkedIn."""
        return f"Excited to share: I've earned the '{self.achievement_name}' achievement in Life Sprint, demonstrating {self.achievement_description}"


# =========================
# Achievement Definitions
# =========================

ACHIEVEMENT_CATALOG: Dict[str, Achievement] = {
    # Academic achievements
    "first_pass": Achievement(
        id="first_pass",
        name="First Pass",
        description="Pass your first exam",
        category=AchievementCategory.academic,
        rarity=AchievementRarity.common,
        icon_url="🎓",
        points=50,
        requirements={"exams_passed": 1},
        unlock_condition_text="Pass 1 exam",
    ),
    "perfect_score": Achievement(
        id="perfect_score",
        name="Perfect Score",
        description="Score 100% on an exam",
        category=AchievementCategory.academic,
        rarity=AchievementRarity.rare,
        icon_url="💯",
        points=200,
        requirements={"exam_score_100": True},
        unlock_condition_text="Score 100% on any exam",
    ),
    "honor_roll": Achievement(
        id="honor_roll",
        name="Honor Roll",
        description="Maintain GPA of 3.8+",
        category=AchievementCategory.academic,
        rarity=AchievementRarity.uncommon,
        icon_url="⭐",
        points=150,
        requirements={"gpa_threshold": 3.8},
        unlock_condition_text="Keep GPA at 3.8 or higher",
    ),
    "exam_streak_5": Achievement(
        id="exam_streak_5",
        name="On a Roll",
        description="Pass 5 exams in a row",
        category=AchievementCategory.academic,
        rarity=AchievementRarity.uncommon,
        icon_url="🔥",
        points=100,
        requirements={"exam_pass_streak": 5},
        unlock_condition_text="Pass 5 exams without failing",
    ),
    
    # Financial achievements
    "no_debt": Achievement(
        id="no_debt",
        name="Debt-Free",
        description="Graduate with zero debt",
        category=AchievementCategory.financial,
        rarity=AchievementRarity.epic,
        icon_url="💰",
        points=500,
        requirements={"graduation_debt": 0},
        unlock_condition_text="Graduate with $0 in loans",
    ),
    "scholarship": Achievement(
        id="scholarship",
        name="Scholarship Recipient",
        description="Earn a scholarship",
        category=AchievementCategory.financial,
        rarity=AchievementRarity.uncommon,
        icon_url="📚",
        points=100,
        requirements={"scholarship_earned": True},
        unlock_condition_text="Receive any scholarship",
    ),
    "side_hustle": Achievement(
        id="side_hustle",
        name="Entrepreneurial Spirit",
        description="Earn $1,000 from side gigs",
        category=AchievementCategory.financial,
        rarity=AchievementRarity.uncommon,
        icon_url="💼",
        points=100,
        requirements={"side_gig_earnings": 1000},
        unlock_condition_text="Earn $1,000 from side gigs",
    ),
    "savers": Achievement(
        id="savers",
        name="Penny Pincher",
        description="Save $5,000",
        category=AchievementCategory.financial,
        rarity=AchievementRarity.uncommon,
        icon_url="🏦",
        points=100,
        requirements={"savings_balance": 5000},
        unlock_condition_text="Accumulate $5,000 in savings",
    ),
    
    # Health achievements
    "balanced_life": Achievement(
        id="balanced_life",
        name="Work-Life Balance",
        description="Maintain stress below 40 for 2 semesters",
        category=AchievementCategory.health,
        rarity=AchievementRarity.uncommon,
        icon_url="🧘",
        points=100,
        requirements={"low_stress_semesters": 2},
        unlock_condition_text="Keep stress below 40 for 2 semesters",
    ),
    "fitness_goal": Achievement(
        id="fitness_goal",
        name="Fitness Goals",
        description="Maintain health above 75 for 4 semesters",
        category=AchievementCategory.health,
        rarity=AchievementRarity.rare,
        icon_url="💪",
        points=150,
        requirements={"high_health_semesters": 4},
        unlock_condition_text="Keep health above 75 for 4 semesters",
    ),
    "zen_master": Achievement(
        id="zen_master",
        name="Zen Master",
        description="Reach happiness of 90+",
        category=AchievementCategory.health,
        rarity=AchievementRarity.epic,
        icon_url="😄",
        points=300,
        requirements={"max_happiness": 90},
        unlock_condition_text="Achieve 90+ happiness",
    ),
    
    # Social achievements
    "first_friend": Achievement(
        id="first_friend",
        name="Making Connections",
        description="Add your first friend",
        category=AchievementCategory.social,
        rarity=AchievementRarity.common,
        icon_url="👥",
        points=50,
        requirements={"friends_count": 1},
        unlock_condition_text="Add 1 friend",
    ),
    "popular": Achievement(
        id="popular",
        name="Popular",
        description="Have 10+ friends",
        category=AchievementCategory.social,
        rarity=AchievementRarity.uncommon,
        icon_url="🌟",
        points=100,
        requirements={"friends_count": 10},
        unlock_condition_text="Make 10 friends",
    ),
    "challenge_winner": Achievement(
        id="challenge_winner",
        name="Challenge Champion",
        description="Win 5 friend challenges",
        category=AchievementCategory.social,
        rarity=AchievementRarity.uncommon,
        icon_url="🏆",
        points=100,
        requirements={"challenges_won": 5},
        unlock_condition_text="Win 5 1v1 challenges",
    ),
    "tournament_winner": Achievement(
        id="tournament_winner",
        name="Tournament Champion",
        description="Win a tournament",
        category=AchievementCategory.social,
        rarity=AchievementRarity.epic,
        icon_url="👑",
        points=300,
        requirements={"tournament_wins": 1},
        unlock_condition_text="Win any tournament",
    ),
    
    # Milestone achievements
    "graduation": Achievement(
        id="graduation",
        name="Graduated",
        description="Complete all years of college",
        category=AchievementCategory.milestone,
        rarity=AchievementRarity.epic,
        icon_url="🎓",
        points=500,
        requirements={"graduated": True},
        unlock_condition_text="Graduate from college",
    ),
    "semester_master": Achievement(
        id="semester_master",
        name="Semester Master",
        description="Complete 8 semesters without dropping below GPA 3.0",
        category=AchievementCategory.milestone,
        rarity=AchievementRarity.legendary,
        icon_url="🏅",
        points=1000,
        requirements={"semesters_above_3_0": 8},
        unlock_condition_text="Complete 8 semesters with 3.0+ GPA",
    ),
    "speedrunner": Achievement(
        id="speedrunner",
        name="Speedrunner",
        description="Graduate in 3 years",
        category=AchievementCategory.milestone,
        rarity=AchievementRarity.epic,
        icon_url="⚡",
        points=400,
        requirements={"graduated_in_semesters": 6},
        unlock_condition_text="Graduate in 6 semesters (3 years)",
    ),
}


# =========================
# Achievement Service
# =========================

class AchievementService:
    """Track and manage player achievements."""
    
    def __init__(self):
        self.player_achievements: Dict[str, Set[str]] = {}  # {player_id → {achievement_ids}}
        self.achievement_unlock_dates: Dict[str, Dict[str, datetime]] = {}  # {player_id → {achievement_id → datetime}}
        self.achievement_progress: Dict[str, Dict[str, float]] = {}  # {player_id → {achievement_id → progress_0_100}}
    
    def check_and_unlock_achievements(
        self,
        player_id: str,
        player_stats: Dict[str, Any],
    ) -> List[str]:
        """Check all achievements and unlock those that are now met."""
        unlocked = []
        
        if player_id not in self.player_achievements:
            self.player_achievements[player_id] = set()
            self.achievement_unlock_dates[player_id] = {}
            self.achievement_progress[player_id] = {}
        
        for ach_id, achievement in ACHIEVEMENT_CATALOG.items():
            # Already unlocked?
            if ach_id in self.player_achievements[player_id]:
                continue
            
            # Check if requirements met
            if self._check_achievement(achievement, player_stats):
                self.player_achievements[player_id].add(ach_id)
                self.achievement_unlock_dates[player_id][ach_id] = datetime.now()
                unlocked.append(ach_id)
            else:
                # Calculate progress
                progress = self._calculate_progress(achievement, player_stats)
                self.achievement_progress[player_id][ach_id] = progress
        
        return unlocked
    
    def _check_achievement(self, achievement: Achievement, player_stats: Dict[str, Any]) -> bool:
        """Check if achievement requirements are met."""
        for key, required_value in achievement.requirements.items():
            stat_value = player_stats.get(key)
            
            if isinstance(required_value, bool):
                if stat_value != required_value:
                    return False
            elif isinstance(required_value, (int, float)):
                if stat_value is None or stat_value < required_value:
                    return False
            elif isinstance(required_value, list):
                if stat_value not in required_value:
                    return False
        
        return True
    
    def _calculate_progress(self, achievement: Achievement, player_stats: Dict[str, Any]) -> float:
        """Calculate progress towards achievement (0-100)."""
        if not achievement.requirements:
            return 0.0
        
        # Simple progress: check one numeric requirement
        for key, required_value in achievement.requirements.items():
            if isinstance(required_value, (int, float)) and required_value > 0:
                current = player_stats.get(key, 0)
                progress = min(100.0, (current / required_value) * 100.0)
                return progress
        
        return 0.0
    
    def get_player_achievements(self, player_id: str) -> List[Achievement]:
        """Get all achievements a player has unlocked."""
        ach_ids = self.player_achievements.get(player_id, set())
        return [ACHIEVEMENT_CATALOG[ach_id] for ach_id in ach_ids if ach_id in ACHIEVEMENT_CATALOG]
    
    def get_achievement_progress(self, player_id: str) -> Dict[str, float]:
        """Get progress towards all locked achievements."""
        return self.achievement_progress.get(player_id, {})
    
    def get_unlocked_badges(self, player_id: str) -> List[Badge]:
        """Convert achievements to visual badges."""
        achievements = self.get_player_achievements(player_id)
        badges = []
        
        for achievement in achievements:
            badge = Badge(
                id=achievement.id,
                name=achievement.name,
                description=achievement.description,
                icon_emoji=achievement.icon_url,
                color=self._rarity_to_color(achievement.rarity),
                rarity=achievement.rarity,
                unlocked=True,
                unlocked_at=self.achievement_unlock_dates.get(player_id, {}).get(achievement.id),
            )
            badges.append(badge)
        
        return badges
    
    def _rarity_to_color(self, rarity: AchievementRarity) -> str:
        """Map rarity to hex color."""
        colors = {
            AchievementRarity.common: "#95a5a6",      # gray
            AchievementRarity.uncommon: "#2ecc71",    # green
            AchievementRarity.rare: "#3498db",        # blue
            AchievementRarity.epic: "#9b59b6",        # purple
            AchievementRarity.legendary: "#f39c12",   # gold
        }
        return colors.get(rarity, "#95a5a6")
    
    def create_shareable_achievement(self, player_id: str, achievement_id: str, player_name: str) -> ShareableAchievement:
        """Create shareable version of achievement."""
        if achievement_id not in ACHIEVEMENT_CATALOG:
            raise ValueError("Achievement not found")
        
        ach = ACHIEVEMENT_CATALOG[achievement_id]
        
        return ShareableAchievement(
            achievement_name=ach.name,
            achievement_description=ach.description,
            icon=ach.icon_url,
            rarity=ach.rarity.value,
            player_name=player_name,
            timestamp=self.achievement_unlock_dates.get(player_id, {}).get(achievement_id, datetime.now()),
            share_text=f"{player_name} unlocked {ach.icon_url} {ach.name}!",
        )


# Global instance
achievement_service = AchievementService()
