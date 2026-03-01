"""
Community & Collaboration System

Provides:
- Student guilds/cohorts for group learning
- Study group matching by skill level and major
- Peer mentorship networks
- Achievement sharing and celebrations
- Collaborative projects
- Social bonding and community identity
"""

from typing import Dict, List, Any, Optional
from uuid import uuid4
from datetime import datetime

from core_domain.player.player_model import Player


class StudyGroup:
    """Represents a student study group."""
    
    def __init__(
        self,
        name: str,
        major: str,
        topic: str,
        meeting_frequency: str,
        max_members: int = 6,
    ):
        self.id = str(uuid4())
        self.name = name
        self.major = major
        self.topic = topic
        self.meeting_frequency = meeting_frequency
        self.max_members = max_members
        self.members = []
        self.created_date = datetime.now()
        self.meeting_notes = []
        self.performance_impact = 0.0


class Guild:
    """Represents a student guild/community."""
    
    def __init__(
        self,
        name: str,
        description: str,
        guild_type: str,
    ):
        self.id = str(uuid4())
        self.name = name
        self.description = description
        self.guild_type = guild_type  # academic, hobby, professional, social
        self.members = []
        self.created_date = datetime.now()
        self.events = []
        self.achievements = []
        self.level = 1
        self.prestige = 0.0


class CollaborativeProject:
    """Represents a collaborative project between students."""
    
    def __init__(
        self,
        name: str,
        description: str,
        project_type: str,
        required_roles: List[str],
    ):
        self.id = str(uuid4())
        self.name = name
        self.description = description
        self.project_type = project_type  # research, hackathon, startup, academic
        self.required_roles = required_roles
        self.team_members = []
        self.created_date = datetime.now()
        self.status = "active"
        self.completion_percentage = 0.0
        self.expected_outcomes = []


# Study Group Templates
STUDY_GROUP_TEMPLATES: List[Dict[str, Any]] = [
    {
        "name": "Data Structures Study Circle",
        "major": "Computer Science",
        "topic": "Advanced Data Structures",
        "frequency": "Weekly",
        "difficulty": "Intermediate",
        "ideal_size": 5,
        "benefits": [
            "Master complex data structures",
            "Prepare for technical interviews",
            "+15-20% algorithm speed improvement",
        ],
    },
    {
        "name": "Organic Chem Problem Setters",
        "major": "Chemistry",
        "topic": "Organic Chemistry Reactions",
        "frequency": "Bi-weekly",
        "difficulty": "Hard",
        "ideal_size": 4,
        "benefits": [
            "Solve complex reaction mechanisms",
            "Exam score improvement: +10-20%",
            "Deep conceptual understanding",
        ],
    },
    {
        "name": "Finance Case Study Group",
        "major": "Finance",
        "topic": "Portfolio Analysis & Valuation",
        "frequency": "Weekly",
        "difficulty": "Advanced",
        "ideal_size": 6,
        "benefits": [
            "Practice real trading scenarios",
            "Learn from peer strategies",
            "+25% faster case comprehension",
        ],
    },
    {
        "name": "Philosophy Seminar",
        "major": "Liberal Arts",
        "topic": "Ethics & Epistemology",
        "frequency": "Weekly",
        "difficulty": "Advanced",
        "ideal_size": 5,
        "benefits": [
            "Deep philosophical discussions",
            "Improve critical thinking",
            "Write better argumentative essays",
        ],
    },
    {
        "name": "ML Paper Reading Club",
        "major": "Data Science",
        "topic": "Latest ML Research Papers",
        "frequency": "Bi-weekly",
        "difficulty": "Advanced",
        "ideal_size": 6,
        "benefits": [
            "Stay current with research",
            "Understand cutting-edge techniques",
            "Build research discussion skills",
        ],
    },
]

# Guild Types and Templates
GUILD_TEMPLATES: List[Dict[str, Any]] = [
    {
        "name": "CS Competitive Programming Guild",
        "type": "academic",
        "description": "Master algorithmic problem solving through competitive programming",
        "total_members": 42,
        "level": 5,
        "achievements": [
            "Solved 1000+ Problems",
            "Won 5 Contests",
            "Training Complete",
        ],
        "benefits": [
            "+30% algorithm speed",
            "Interview preparation",
            "Contest prizes",
        ],
    },
    {
        "name": "Entrepreneurship Club",
        "type": "professional",
        "description": "Build startups and business ventures together",
        "total_members": 28,
        "level": 3,
        "achievements": [
            "2 Companies Launched",
            "Funded: $500K",
            "10 Members Employed",
        ],
        "benefits": [
            "Access to funding",
            "Mentorship from founders",
            "Co-founder connections",
        ],
    },
    {
        "name": "Data Science & Analytics Hub",
        "type": "professional",
        "description": "Collaborate on real-world data science projects",
        "total_members": 35,
        "level": 4,
        "achievements": [
            "Published 3 Papers",
            "Built 12 ML Models",
            "5 Job Placements",
        ],
        "benefits": [
            "Portfolio projects",
            "Publication opportunities",
            "Internship connections",
        ],
    },
    {
        "name": "Finance Trading Group",
        "type": "academic",
        "description": "Paper trading competition and market analysis",
        "total_members": 31,
        "level": 4,
        "achievements": [
            "+45% Returns Last Year",
            "100+ Case Studies",
            "3 Members Working on Wall St",
        ],
        "benefits": [
            "Real trading experience",
            "Market insights",
            "Wall Street connections",
        ],
    },
    {
        "name": "Global Citizenship Forum",
        "type": "social",
        "description": "Discuss global issues and cultural exchange",
        "total_members": 56,
        "level": 3,
        "achievements": [
            "Hosted 12 Events",
            "50+ Countries Represented",
            "5 Community Projects",
        ],
        "benefits": [
            "Cultural learning",
            "International network",
            "Community impact",
        ],
    },
]

# Collaborative Project Opportunities
PROJECT_OPPORTUNITIES: List[Dict[str, Any]] = [
    {
        "name": "AI-Powered Education Platform",
        "type": "startup",
        "description": "Build intelligent tutoring system using AI/ML",
        "required_roles": ["ML Engineer", "Backend Developer", "Product Designer"],
        "timeline": "4 months",
        "expected_impact": "10K+ student users",
        "funding_potential": "$100K seed round",
        "skills_developed": ["Full-stack AI", "Product management", "Startup basics"],
    },
    {
        "name": "Carbon Footprint Tracker",
        "type": "research",
        "description": "Environmental data science project on emissions tracking",
        "required_roles": ["Data Scientist", "Backend Dev", "Environmental Expert"],
        "timeline": "3 months",
        "expected_impact": "Research publication",
        "funding_potential": "Grant opportunity",
        "skills_developed": ["Climate analytics", "Data visualization", "Research methodology"],
    },
    {
        "name": "Community Financial Literacy App",
        "type": "academic",
        "description": "Gamified financial education app for underserved communities",
        "required_roles": ["Frontend Dev", "Game Designer", "Finance Expert"],
        "timeline": "5 months",
        "expected_impact": "10K+ users educated",
        "funding_potential": "Impact fund interest",
        "skills_developed": ["Social impact", "Full-stack web", "Financial education"],
    },
    {
        "name": "Hackathon Winning Team",
        "type": "hackathon",
        "description": "Form team for major hackathon competition",
        "required_roles": ["Full-stack Dev", "Designer", "Visionary Leader"],
        "timeline": "1 month",
        "expected_impact": "Prize money + visibility",
        "funding_potential": "Prize pool: $50K",
        "skills_developed": ["Rapid development", "Team coordination", "Innovation"],
    },
]

# Social Bonding Activities
SOCIAL_ACTIVITIES: List[Dict[str, Any]] = [
    {
        "name": "Weekly Coffee Chat",
        "format": "Small group casual meetup",
        "frequency": "Weekly",
        "capacity": 8,
        "bonding_score": 15,
        "fun_factor": "High",
    },
    {
        "name": "Study Session Celebration",
        "format": "Group reward after finishing major exams",
        "frequency": "Per semester",
        "capacity": 50,
        "bonding_score": 25,
        "fun_factor": "Very High",
    },
    {
        "name": "Skill-Sharing Potluck",
        "format": "Members teach each other quick skills while eating",
        "frequency": "Monthly",
        "capacity": 20,
        "bonding_score": 20,
        "fun_factor": "High",
    },
    {
        "name": "Virtual Global Hangout",
        "format": "Online chat with members worldwide",
        "frequency": "Bi-weekly",
        "capacity": 100,
        "bonding_score": 12,
        "fun_factor": "Medium",
    },
]

# Community Achievement Badges
COMMUNITY_ACHIEVEMENTS: Dict[str, Dict[str, Any]] = {
    "study_buddy_excellence": {
        "name": "Study Buddy Excellence",
        "description": "Completed 20 study group sessions",
        "icon": "📚",
        "rarity": "Common",
        "bonus": {"confidence": 10, "skill_growth": 5},
    },
    "guild_champion": {
        "name": "Guild Champion",
        "description": "Helped guild reach level 5",
        "icon": "👑",
        "rarity": "Legendary",
        "bonus": {"career_confidence": 25, "network": 20},
    },
    "collaboration_master": {
        "name": "Collaboration Master",
        "description": "Completed 3 collaborative projects",
        "icon": "🤝",
        "rarity": "Rare",
        "bonus": {"skill_growth": 20, "experience": 25},
    },
    "mentor_advocate": {
        "name": "Mentor Advocate",
        "description": "Mentored 5 students",
        "icon": "🎓",
        "rarity": "Rare",
        "bonus": {"career_confidence": 15, "salary_potential": 5000},
    },
    "community_builder": {
        "name": "Community Builder",
        "description": "Founded and grew a study group",
        "icon": "🏗️",
        "rarity": "Rare",
        "bonus": {"leadership": 20, "network": 15},
    },
    "innovation_leader": {
        "name": "Innovation Leader",
        "description": "Led successful collaborative startup/project",
        "icon": "⚡",
        "rarity": "Legendary",
        "bonus": {"career_confidence": 30, "network": 25, "salary_potential": 20000},
    },
}


# ==============================================================================
# Service Functions
# ==============================================================================

def get_study_group_recommendations(player: Player) -> List[Dict[str, Any]]:
    """
    Get study group recommendations based on player's major and skill level.
    
    Returns:
    - Top matching study groups
    - Why they match
    - Expected impact on GPA and learning
    """
    major = getattr(player, 'major_id', 'unknown')
    gpa = getattr(player, 'hs_gpa', 3.0)
    
    recommendations = []
    for group_template in STUDY_GROUP_TEMPLATES:
        # Simple matching: exact major match
        if group_template["major"].lower() in major.lower() or major.lower() in group_template["major"].lower():
            score = 85 + (gpa - 3.0) * 10
            
            recommendations.append({
                **group_template,
                "match_score": min(100, score),
                "current_members": max(1, min(group_template["ideal_size"] - 1, 4)),
                "spaces_available": max(0, group_template["ideal_size"] - max(1, min(group_template["ideal_size"] - 1, 4))),
            })
    
    if not recommendations:
        # Fallback: recommend any group
        for group_template in STUDY_GROUP_TEMPLATES[:2]:
            score = 65 + (gpa - 3.0) * 5
            recommendations.append({
                **group_template,
                "match_score": min(100, score),
                "current_members": 3,
                "spaces_available": group_template["ideal_size"] - 3,
            })
    
    return sorted(recommendations, key=lambda x: x["match_score"], reverse=True)[:3]


def get_available_guilds(player: Player) -> List[Dict[str, Any]]:
    """
    Get guilds that match player's interests and career goals.
    """
    recommendations = []
    major = getattr(player, 'major_id', 'unknown').lower()
    
    # CS students get CS guild
    if 'computer' in major or 'science' in major or 'cs' in major:
        recommendations.append(GUILD_TEMPLATES[0])
    
    # Anyone can join entrepreneurship
    recommendations.append(GUILD_TEMPLATES[1])
    
    # Data/Finance students get relevant guilds
    if 'data' in major or 'finance' in major:
        recommendations.append(GUILD_TEMPLATES[2])
    
    if 'finance' in major:
        recommendations.append(GUILD_TEMPLATES[3])
    
    # Everyone should see social guilds
    if len(recommendations) < 3:
        recommendations.append(GUILD_TEMPLATES[4])
    
    return recommendations


def get_collaborative_projects(player: Player) -> List[Dict[str, Any]]:
    """
    Get collaborative project opportunities matching player's skills.
    """
    return [
        {
            **project,
            "open_positions": len(project["required_roles"]),
            "interested_members": 2,
            "difficulty": "Intermediate" if project["type"] == "hackathon" else "Advanced",
        }
        for project in PROJECT_OPPORTUNITIES
    ]


def calculate_community_impact(
    study_groups_joined: int,
    guild_level: int,
    projects_completed: int,
    member_count: int,
) -> Dict[str, float]:
    """
    Calculate impact of community involvement on player stats.
    """
    impact = {
        "gpa_boost": min(0.5, study_groups_joined * 0.08),
        "confidence_boost": min(40, (study_groups_joined * 5) + (guild_level * 3) + (projects_completed * 10)),
        "network_expansion": (study_groups_joined * 3) + (guild_level * 5) + (projects_completed * 8),
        "skill_development": min(30, (study_groups_joined * 2.5) + (projects_completed * 10)),
        "career_opportunity_probability": min(0.5, 0.1 + (guild_level * 0.08) + (projects_completed * 0.15)),
    }
    return impact


def suggest_collaboration_partners(player: Player, project_id: str) -> List[Dict[str, Any]]:
    """
    Suggest ideal collaboration partners for a specific project.
    
    In production, would match based on:
    - Complementary skills
    - Availability
    - Work style compatibility
    - Time zone proximity
    """
    suggestions = [
        {
            "name": "Alex Chen",
            "strength": "Full-stack development",
            "commitment": "20 hrs/week",
            "timezone": "PST",
            "compatibility_score": 92,
            "why_match": "Complementary backend skills",
        },
        {
            "name": "Jordan Smith",
            "strength": "Product design",
            "commitment": "15 hrs/week",
            "timezone": "EST",
            "compatibility_score": 88,
            "why_match": "UI/UX expertise fills gap",
        },
        {
            "name": "Priya Patel",
            "strength": "Data analytics",
            "commitment": "10 hrs/week",
            "timezone": "IST",
            "compatibility_score": 85,
            "why_match": "Strong analytics background",
        },
    ]
    return suggestions
