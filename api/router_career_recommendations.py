"""
Career Recommendations Router

Provides:
- Personalized career path recommendations based on major & GPA
- Job market insights and salary projections
- Skill development recommendations
- Career progression information
"""

from fastapi import APIRouter, HTTPException

from core_domain.store import STORE
from catalogs.career_recommendations import get_career_recommendations, major_career_alignment_report

router = APIRouter(prefix="/api/career", tags=["career"])


@router.get("/recommendations/{player_id}")
def get_player_recommendations(player_id: str):
    """
    Get personalized career path recommendations for a player.
    
    Returns:
    - Primary career recommendation
    - Alternative recommendations
    - Market insights (demand, growth)
    - Salary projections
    - Skill development roadmap
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    recommendations = get_career_recommendations(player)
    
    return {
        "player_id": player_id,
        "major": getattr(player, 'major_id', 'unknown'),
        "gpa": getattr(player, 'current_gpa', 3.0),
        "recommendations": recommendations,
    }


@router.get("/market-overview")
def get_market_overview():
    """
    Get job market overview - demand, growth trends, emerging fields.
    
    Useful for career exploration and decision-making.
    """
    return {
        "summary": "Tech and data careers lead job market growth",
        "hottest_fields": [
            {
                "field": "Artificial Intelligence / Machine Learning",
                "demand": "Very High",
                "growth_rate": "25%+",
                "typical_salary": "$95,000 - $160,000 (entry-mid)",
            },
            {
                "field": "Data Science",
                "demand": "Very High",
                "growth_rate": "20%+",
                "typical_salary": "$85,000 - $150,000 (entry-mid)",
            },
            {
                "field": "Software Engineering",
                "demand": "High",
                "growth_rate": "15%+",
                "typical_salary": "$75,000 - $130,000 (entry-mid)",
            },
            {
                "field": "Healthcare Technology",
                "demand": "Very High",
                "growth_rate": "18%+",
                "typical_salary": "$80,000 - $120,000 (entry-mid)",
            },
            {
                "field": "Cloud Computing",
                "demand": "High",
                "growth_rate": "22%+",
                "typical_salary": "$85,000 - $140,000 (entry-mid)",
            },
        ],
        "emerging_trends": [
            "Hybrid AI/data roles combining machine learning with business",
            "Cybersecurity specialists with cloud infrastructure knowledge",
            "Full-stack data engineers",
            "AI ethics and responsible AI specialists",
        ],
        "salary_insights": {
            "median_entry": 70000,
            "median_mid": 105000,
            "median_senior": 140000,
            "highest_growth": "Tech sector (avg 8-10% annual growth)",
        },
    }


@router.get("/major-alignment/{major_id}")
def get_major_career_paths(major_id: str):
    """
    Get all career paths aligned with a specific major.
    Useful for onboarding/major selection.
    """
    report = major_career_alignment_report(major_id)
    
    if not report["recommended_paths"]:
        raise HTTPException(
            status_code=404,
            detail=f"Career paths not found for major '{major_id}'"
        )
    
    return report


@router.get("/salary-comparison")
def get_salary_comparison():
    """
    Compare entry-level salaries across career paths.
    """
    comparisons = [
        {
            "field": "Software Engineering",
            "entry_salary": 75000,
            "mid_salary": 105000,
            "senior_salary": 135000,
            "max_salary": 200000,
        },
        {
            "field": "Data Science",
            "entry_salary": 85000,
            "mid_salary": 120000,
            "senior_salary": 160000,
            "max_salary": 220000,
        },
        {
            "field": "Finance",
            "entry_salary": 75000,
            "mid_salary": 105000,
            "senior_salary": 135000,
            "max_salary": 240000,
        },
        {
            "field": "Consulting",
            "entry_salary": 85000,
            "mid_salary": 125000,
            "senior_salary": 165000,
            "max_salary": 300000,
        },
        {
            "field": "Healthcare Tech",
            "entry_salary": 70000,
            "mid_salary": 100000,
            "senior_salary": 140000,
            "max_salary": 180000,
        },
        {
            "field": "Research",
            "entry_salary": 65000,
            "mid_salary": 95000,
            "senior_salary": 130000,
            "max_salary": 180000,
        },
    ]
    
    return {
        "comparisons": comparisons,
        "note": "Salaries based on 2024 market data. Individual compensation varies.",
    }


@router.get("/skill-roadmap/{path_id}")
def get_skill_roadmap(path_id: str):
    """
    Get required skills and development roadmap for a career path.
    """
    roadmaps = {
        "tech_entry": {
            "path": "Software Engineering",
            "entry_title": "Junior Developer",
            "critical_skills": [
                {
                    "name": "Programming (Python/Java/Go)",
                    "timeframe": "2-3 semesters",
                    "resources": ["CS101/201", "Coding projects", "LeetCode"]
                },
                {
                    "name": "Data Structures & Algorithms",
                    "timeframe": "2-3 semesters",
                    "resources": ["CS201", "Algorithm courses", "Interview prep"]
                },
                {
                    "name": "System Design",
                    "timeframe": "3-4 semesters",
                    "resources": ["CS301", "Design patterns", "Senior engineer mentorship"]
                },
            ],
            "progression": [
                {"level": "Junior Dev", "timeline": "0-2 years", "focus": "Core coding skills"},
                {"level": "Mid Dev", "timeline": "2-5 years", "focus": "System thinking, mentoring"},
                {"level": "Senior Eng", "timeline": "5+ years", "focus": "Architecture, leadership"},
                {"level": "Tech Lead", "timeline": "7+ years", "focus": "Strategic decisions"},
            ],
        },
        "data_entry": {
            "path": "Data Science",
            "entry_title": "Data Analyst",
            "critical_skills": [
                {
                    "name": "Statistics & Math",
                    "timeframe": "2-3 semesters",
                    "resources": ["Math201/301", "Stats courses"]
                },
                {
                    "name": "Python/SQL",
                    "timeframe": "2-3 semesters",
                    "resources": ["CS courses", "DS101"]
                },
                {
                    "name": "Machine Learning",
                    "timeframe": "3-4 semesters",
                    "resources": ["DS301", "DS401", "Kaggle competitions"]
                },
            ],
            "progression": [
                {"level": "Junior Analyst", "timeline": "0-2 years", "focus": "SQL, basic ML"},
                {"level": "Data Scientist", "timeline": "2-5 years", "focus": "Advanced ML, insights"},
                {"level": "Senior DS", "timeline": "5+ years", "focus": "Strategy, leadership"},
                {"level": "ML Engineer", "timeline": "5+ years", "focus": "Deployment, scale"},
            ],
        },
        "finance_entry": {
            "path": "Finance",
            "entry_title": "Financial Analyst",
            "critical_skills": [
                {
                    "name": "Financial Accounting",
                    "timeframe": "2 semesters",
                    "resources": ["Fin101", "Acc101"]
                },
                {
                    "name": "Excel Mastery",
                    "timeframe": "1-2 semesters",
                    "resources": ["Finance bootcamp", "Daily practice"]
                },
                {
                    "name": "Valuation & Analysis",
                    "timeframe": "3-4 semesters",
                    "resources": ["Fin201", "CFA prep"]
                },
            ],
            "progression": [
                {"level": "Analyst", "timeline": "0-3 years", "focus": "Modeling, analysis"},
                {"level": "Senior Analyst", "timeline": "3-6 years", "focus": "Teams, strategy"},
                {"level": "Manager", "timeline": "6+ years", "focus": "Department leadership"},
            ],
        },
        "consulting_entry": {
            "path": "Management Consulting",
            "entry_title": "Consultant",
            "critical_skills": [
                {
                    "name": "Problem-Solving",
                    "timeframe": "Ongoing",
                    "resources": ["Case study practice", "McKinsey/BCG prep"]
                },
                {
                    "name": "Business Acumen",
                    "timeframe": "2-3 semesters",
                    "resources": ["BA courses", "Industry reading"]
                },
                {
                    "name": "Communication",
                    "timeframe": "Ongoing",
                    "resources": ["Presentations", "Public speaking clubs"]
                },
            ],
            "progression": [
                {"level": "Analyst", "timeline": "0-2 years", "focus": "Execution, client"},
                {"level": "Consultant", "timeline": "2-5 years", "focus": "Solving, leadership"},
                {"level": "Manager", "timeline": "5+ years", "focus": "Client relations"},
                {"level": "Partner", "timeline": "10+ years", "focus": "Firm strategy"},
            ],
        },
    }
    
    roadmap = roadmaps.get(path_id.lower())
    if not roadmap:
        raise HTTPException(
            status_code=404,
            detail=f"Skill roadmap not found for '{path_id}'"
        )
    
    return roadmap
