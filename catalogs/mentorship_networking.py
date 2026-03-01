"""
Advanced Features: Mentorship & Networking System

Provides:
- Virtual mentorship connections (players can mentor/be mentored)
- Industry networking events
- Skill pairing (matching mentors with learners)
- Mentorship tracking and rewards
"""

from typing import Dict, List, Any, Optional
from uuid import uuid4
from datetime import datetime

from core_domain.player.player_model import Player


class MentorshipProfile:
    """Represents a mentorship relationship."""
    
    def __init__(
        self,
        mentor_id: str,
        mentee_id: str,
        focus_skills: List[str],
        monthly_sessions: int = 2,
    ):
        self.id = str(uuid4())
        self.mentor_id = mentor_id
        self.mentee_id = mentee_id
        self.focus_skills = focus_skills
        self.monthly_sessions = monthly_sessions
        self.created_date = datetime.now()
        self.sessions_completed = 0
        self.feedback_score = 0.0
        self.active = True


class NetworkingEvent:
    """Represents an industry networking event."""
    
    def __init__(
        self,
        name: str,
        industry: str,
        date: str,
        company_hosts: List[str],
        expected_attendees: int,
    ):
        self.id = str(uuid4())
        self.name = name
        self.industry = industry
        self.date = date
        self.company_hosts = company_hosts
        self.expected_attendees = expected_attendees
        self.attendees = []
        self.created_date = datetime.now()


# Mentorship Skill Matching Pairs
MENTORSHIP_SKILL_MATRIX: Dict[str, List[str]] = {
    "Python": ["Data Analysis", "Web Development", "Automation", "Machine Learning"],
    "Machine Learning": ["Data Science", "AI Engineering", "Data Analysis"],
    "System Design": ["Software Architecture", "Scalability", "Performance"],
    "Leadership": ["Management", "Team Building", "Communication"],
    "Product Management": ["Strategy", "Analytics", "Communication"],
    "Cloud Architecture": ["DevOps", "Infrastructure", "Security"],
    "Data Analysis": ["Python", "SQL", "Analytics", "Business Intelligence"],
}

# Networking events library
NETWORKING_EVENTS_CATALOG: List[Dict[str, Any]] = [
    {
        "name": "Tech Industry Mixer",
        "industry": "Technology",
        "frequency": "Monthly",
        "companies": ["Google", "Microsoft", "Apple", "Amazon", "Meta"],
        "expected_attendees": 200,
        "description": "Network with tech leaders and engineers from major companies",
        "skill_level": "All",
    },
    {
        "name": "Finance Careers Summit",
        "industry": "Finance",
        "frequency": "Quarterly",
        "companies": ["Goldman Sachs", "JPMorgan", "Morgan Stanley", "BlackRock"],
        "expected_attendees": 150,
        "description": "Connect with finance professionals and hiring managers",
        "skill_level": "All",
    },
    {
        "name": "Data Science Symposium",
        "industry": "Data Science",
        "frequency": "Quarterly",
        "companies": ["DataRobot", "Databricks", "Palantir", "Scale AI"],
        "expected_attendees": 300,
        "description": "Meet data scientists and ML engineers from cutting-edge companies",
        "skill_level": "Intermediate+",
    },
    {
        "name": "Consulting Case Competition",
        "industry": "Consulting",
        "frequency": "Annually",
        "companies": ["McKinsey", "BCG", "Bain", "Deloitte"],
        "expected_attendees": 500,
        "description": "Compete and network with consultants from top firms",
        "skill_level": "Advanced",
    },
    {
        "name": "Healthcare Tech Innovation Forum",
        "industry": "Healthcare",
        "frequency": "Semi-Annually",
        "companies": ["UnitedHealth", "CVS Health", "Optum", "Teladoc"],
        "expected_attendees": 250,
        "description": "Explore careers at intersection of healthcare and technology",
        "skill_level": "All",
    },
]

# Benefits of mentorship
MENTORSHIP_BENEFITS: Dict[str, Dict[str, Any]] = {
    "For Mentee": {
        "skill_growth": "+3-5% skill improvement per semester",
        "career_guidance": "Personalized advice from experienced professional",
        "network_expansion": "Access to mentor's professional network",
        "confidence_boost": "+10-15% improvement in career confidence",
        "faster_advancement": "+1 promotion opportunity earlier than average",
        "gpa_impact": "+0.2-0.3 GPA boost from focused learning",
    },
    "For Mentor": {
        "leadership_experience": "Practice and develop leadership skills",
        "network_growth": "Expand professional network",
        "satisfaction": "Help shape next generation of professionals",
        "career_prestige": "+5% salary premium for leaders and mentors",
        "industry_recognition": "Build reputation in field",
    },
}

# Networking event outcomes
NETWORKING_OUTCOMES: Dict[str, Dict[str, Any]] = {
    "job_opportunity": {
        "probability": 0.15,
        "description": "Receive job offer or interesting interview opportunity",
        "impact": "+30 career confidence, potential salary increase",
    },
    "mentor_connection": {
        "probability": 0.25,
        "description": "Meet someone willing to mentor you",
        "impact": "Start mentorship relationship, +20 career confidence",
    },
    "skill_insight": {
        "probability": 0.40,
        "description": "Learn about in-demand skills and career paths",
        "impact": "+15 knowledge, clarified career direction",
    },
    "project_collaboration": {
        "probability": 0.20,
        "description": "Find collaborators for industry projects",
        "impact": "Start collaborative project, +25 skill experience",
    },
}


def get_mentor_recommendations(player: Player) -> List[Dict[str, Any]]:
    """
    Get recommended mentors for a player based on skills and career path.
    
    Returns list of potential mentors with:
    - Expertise in skills player needs
    - Experience in player's target career
    - Availability for sessions
    """
    # Simulated mentor database - would be real in production
    MENTOR_DATABASE = [
        {
            "mentor_id": "mentor_001",
            "name": "Sarah Chen",
            "title": "Senior Software Engineer at Google",
            "expertise": ["Python", "System Design", "Cloud Architecture"],
            "target_career": ["Software Engineer", "Tech Lead"],
            "availability": "2 sessions/month",
            "experience_years": 8,
            "mentees_helped": 12,
            "rating": 4.8,
        },
        {
            "mentor_id": "mentor_002",
            "name": "Marcus Johnson",
            "title": "ML Engineer at OpenAI",
            "expertise": ["Machine Learning", "Python", "Data Analysis"],
            "target_career": ["Data Scientist", "ML Engineer"],
            "availability": "1-2 sessions/month",
            "experience_years": 6,
            "mentees_helped": 8,
            "rating": 4.9,
        },
        {
            "mentor_id": "mentor_003",
            "name": "Lisa Rodriguez",
            "title": "Senior Product Manager at Meta",
            "expertise": ["Product Management", "Leadership", "Strategy"],
            "target_career": ["Product Manager", "Strategy"],
            "availability": "2 sessions/month",
            "experience_years": 10,
            "mentees_helped": 15,
            "rating": 4.7,
        },
        {
            "mentor_id": "mentor_004",
            "name": "David Kim",
            "title": "Analyst at Goldman Sachs",
            "expertise": ["Finance", "Data Analysis", "Business"],
            "target_career": ["Financial Analyst", "Trader"],
            "availability": "3 sessions/month",
            "experience_years": 5,
            "mentees_helped": 10,
            "rating": 4.6,
        },
    ]
    
    # Filter and score mentors based on player fit
    recommendations = []
    for mentor in MENTOR_DATABASE:
        score = _calculate_mentor_fit(player, mentor)
        if score > 60:
            recommendations.append({
                **mentor,
                "fit_score": score,
                "why_match": _generate_mentor_match_reason(player, mentor),
            })
    
    # Sort by fit score
    recommendations.sort(key=lambda x: x["fit_score"], reverse=True)
    return recommendations[:3]  # Top 3


def _calculate_mentor_fit(player: Player, mentor: Dict) -> float:
    """Calculate how well a mentor matches a player's needs."""
    score = 50.0
    
    # Always give some score for availability and rating
    score += 10  # Base score for being available
    
    # Experience level match
    gpa = getattr(player, 'hs_gpa', 3.0)
    if gpa >= 3.7 and mentor["experience_years"] >= 5:
        score += 15
    elif gpa >= 3.5:
        score += 10
    
    # Rating bonus
    rating = mentor.get("rating", 4.0)
    score += (rating / 5) * 10
    
    return min(100, score)


def _generate_mentor_match_reason(player: Player, mentor: Dict) -> str:
    """Generate explanation for why this mentor matches player."""
    reasons = []
    
    major = getattr(player, 'major_id', 'unknown')
    gpa = getattr(player, 'hs_gpa', 3.0)
    
    # Match reason
    if any(major in role for role in mentor["target_career"]):
        reasons.append(f"Specializes in {major}-related careers")
    
    if gpa >= 3.5:
        reasons.append("Experienced with high-performing professionals")
    
    reasons.append(f"Rated {mentor['rating']}/5.0 by previous mentees")
    reasons.append(f"{mentor['mentees_helped']} mentees successfully guided")
    
    return " • ".join(reasons[:3])


def get_networking_events_for_player(player: Player) -> List[Dict[str, Any]]:
    """Get upcoming networking events relevant to player's major/interests."""
    major = getattr(player, 'major_id', 'unknown').lower()
    
    # Map majors to industries
    industry_map = {
        "computer_science": "Technology",
        "data_science": "Data Science",
        "finance": "Finance",
        "business": "Consulting",
        "healthcare": "Healthcare",
    }
    
    target_industry = industry_map.get(major, "Technology")
    
    relevant_events = []
    for event in NETWORKING_EVENTS_CATALOG:
        if target_industry.lower() in event["industry"].lower() or event["skill_level"] == "All":
            relevant_events.append({
                **event,
                "recommendation_score": 85,
                "why_recommended": f"Aligns with {major} career path",
                "attend_benefit": NETWORKING_OUTCOMES,
            })
    
    return relevant_events


def simulate_networking_event_outcome() -> str:
    """Simulate outcome of attending a networking event."""
    import random
    
    outcomes = list(NETWORKING_OUTCOMES.keys())
    weights = [NETWORKING_OUTCOMES[o]["probability"] for o in outcomes]
    
    return random.choices(outcomes, weights=weights)[0]


def calculate_mentorship_impact(sessions: int, player: Player) -> Dict[str, float]:
    """Calculate the impact of mentorship sessions on player stats."""
    impact = {
        "gpa_improvement": 0.0,
        "career_confidence": 0.0,
        "skill_growth": 0.0,
        "network_expansion": 0.0,
    }
    
    # Each session provides benefits
    impact["gpa_improvement"] = min(0.3, sessions * 0.05)
    impact["career_confidence"] = min(25, sessions * 3)
    impact["skill_growth"] = min(20, sessions * 2.5)
    impact["network_expansion"] = min(30, sessions * 4)
    
    return impact
