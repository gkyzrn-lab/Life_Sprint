"""
Community & Collaboration Router

Provides:
- Study group discovery and matching
- Guild discovery and membership
- Collaborative project opportunities
- Community achievements
- Social bonding activities
"""

from fastapi import APIRouter, HTTPException

from core_domain.store import STORE
from catalogs.community_collaboration import (
    get_study_group_recommendations,
    get_available_guilds,
    get_collaborative_projects,
    calculate_community_impact,
    suggest_collaboration_partners,
    SOCIAL_ACTIVITIES,
    COMMUNITY_ACHIEVEMENTS,
    PROJECT_OPPORTUNITIES,
)

router = APIRouter(prefix="/api/community", tags=["community"])


@router.get("/study-groups/{player_id}")
def get_study_groups(player_id: str):
    """
    Get personalized study group recommendations.
    
    Shows:
    - Matching study groups by major/topic
    - Current members and available spaces
    - Expected impact on GPA and learning
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    groups = get_study_group_recommendations(player)
    
    return {
        "player_id": player_id,
        "major": getattr(player, 'major_id', 'unknown'),
        "recommended_study_groups": groups,
        "total_recommendations": len(groups),
        "why_join": [
            "Improve GPA through collaborative learning",
            "Build study habits with peers",
            "Prepare better for exams",
            "Network with classmates",
        ],
    }


@router.post("/study-groups/join/{player_id}/{group_name}")
def join_study_group(player_id: str, group_name: str):
    """
    Join a study group.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return {
        "status": "success",
        "message": f"Successfully joined {group_name}",
        "group_name": group_name,
        "first_meeting": "This Saturday, 2 PM",
        "location": "Library Study Room B",
        "group_members": 4,
        "meeting_frequency": "Weekly",
        "next_steps": [
            "Review group syllabus",
            "Introduce yourself to members",
            "Prepare materials for first meeting",
        ],
    }


@router.get("/guilds/{player_id}")
def get_guilds(player_id: str):
    """
    Get available guilds matching player's interests.
    
    Shows:
    - Academic, professional, and social guilds
    - Guild achievements and member count
    - Benefits of joining
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    guilds = get_available_guilds(player)
    
    return {
        "player_id": player_id,
        "major": getattr(player, 'major_id', 'unknown'),
        "available_guilds": guilds,
        "total_recommendations": len(guilds),
        "guild_benefits": {
            "community": "Sense of belonging and identity",
            "learning": "Collective knowledge sharing",
            "career": "Professional network and opportunities",
            "achievement": "Guild prestige and status",
        },
    }


@router.post("/guilds/join/{player_id}/{guild_name}")
def join_guild(player_id: str, guild_name: str):
    """
    Join a guild.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return {
        "status": "success",
        "message": f"Successfully joined {guild_name}",
        "guild_name": guild_name,
        "member_count": 42,
        "guild_level": 5,
        "your_role": "Apprentice",
        "next_event": "Guild Meetup - Next Friday",
        "welcome_bonus": {
            "credits": 100,
            "skill_boost": 5,
        },
        "next_steps": [
            "Attend orientation meeting",
            "Set learning goals with guild",
            "Participate in guild projects",
        ],
    }


@router.get("/projects/{player_id}")
def get_projects(player_id: str):
    """
    Get collaborative project opportunities.
    
    Shows:
    - Open projects seeking team members
    - Required roles and timeline
    - Expected outcomes and impact
    - Funding/prize potential
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    projects = get_collaborative_projects(player)
    
    return {
        "player_id": player_id,
        "major": getattr(player, 'major_id', 'unknown'),
        "available_projects": projects,
        "total_opportunities": len(projects),
        "project_benefits": [
            "Build portfolio with real projects",
            "Develop leadership and teamwork",
            "Create funding/prize opportunities",
            "Meet potential co-founders",
            "Gain industry recognition",
        ],
    }


@router.post("/projects/apply/{player_id}/{project_name}")
def apply_to_project(player_id: str, project_name: str, role: str = None):
    """
    Apply to join a collaborative project.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return {
        "status": "success",
        "message": f"Application submitted for {project_name}",
        "project_name": project_name,
        "application_role": role or "Flexible",
        "expected_response": "24-48 hours",
        "team_size": "5-7 people",
        "project_timeline": "4-5 months",
        "next_steps": [
            "Wait for team response",
            "Review detailed project brief",
            "Attend kickoff meeting",
            "Set personal goals for project",
        ],
    }


@router.get("/collaboration-partners/{player_id}/{project_name}")
def get_collaboration_partners(player_id: str, project_name: str):
    """
    Get suggested collaboration partners for a project.
    
    Shows:
    - Ideal team members by skill
    - Work style compatibility
    - Timezone and availability
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    partners = suggest_collaboration_partners(player, project_name)
    
    return {
        "project_name": project_name,
        "suggested_partners": partners,
        "selection_tip": "Choose team members with complementary skills for best results",
        "team_dynamics": "Cross-functional teams perform 40% better",
    }


@router.get("/achievements")
def get_community_achievements():
    """
    Get all available community achievement badges.
    """
    return {
        "total_achievements": len(COMMUNITY_ACHIEVEMENTS),
        "achievements": [
            {
                **achievement,
                "id": ach_id,
            }
            for ach_id, achievement in COMMUNITY_ACHIEVEMENTS.items()
        ],
        "rarity_distribution": {
            "Common": 1,
            "Rare": 3,
            "Legendary": 2,
        },
    }


@router.get("/social-activities")
def get_social_activities():
    """
    Get community social bonding activities.
    """
    return {
        "total_activities": len(SOCIAL_ACTIVITIES),
        "activities": SOCIAL_ACTIVITIES,
        "bonding_score_range": "12-25 per activity",
        "frequency": "Multiple events per month",
        "impact": {
            "community_spirit": "Increases sense of belonging",
            "mental_health": "Stress relief and social connection",
            "peer_network": "Build lasting friendships",
        },
    }


@router.post("/attend-activity/{player_id}/{activity_name}")
def attend_social_activity(player_id: str, activity_name: str):
    """
    Attend a social bonding activity.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return {
        "status": "success",
        "message": f"Registered for {activity_name}",
        "activity_name": activity_name,
        "attendance_confirmed": True,
        "date": "This Saturday, 3 PM",
        "location": "Student Center Room 201",
        "expected_attendees": 25,
        "benefits": {
            "bonding_score": 20,
            "happiness": 15,
            "stress_relief": 10,
        },
        "bring": ["Yourself", "Curiosity", "Open mind"],
    }


@router.get("/community-impact/{player_id}")
def get_community_impact(player_id: str, groups: int = 2, guild_level: int = 2, projects: int = 1):
    """
    Calculate the impact of community involvement.
    
    Shows:
    - GPA improvement from study groups
    - Confidence and network growth
    - Career opportunity probability
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    impact = calculate_community_impact(groups, guild_level, projects, guild_level * 10)
    
    return {
        "player_id": player_id,
        "scenario": {
            "study_groups_joined": groups,
            "guild_level_achieved": guild_level,
            "projects_completed": projects,
        },
        "impact_on_stats": {
            "gpa_boost": f"+{impact['gpa_boost']:.2f}",
            "confidence_boost": f"+{impact['confidence_boost']:.0f}",
            "network_expansion": f"+{impact['network_expansion']:.0f} connections",
            "skill_development": f"+{impact['skill_development']:.0f}",
        },
        "career_impact": {
            "opportunity_probability": f"{impact['career_opportunity_probability']*100:.0f}%",
            "salary_improvement": "15-25% potential increase",
            "advancement": "1-2 additional opportunities",
        },
        "interpretation": {
            "participation_level": "High" if (groups + guild_level + projects) >= 4 else "Moderate" if (groups + guild_level + projects) >= 2 else "Low",
            "recommendation": "Increase community involvement for maximum career impact",
        },
    }
