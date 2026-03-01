"""
Career Path Recommendation System.

Matches majors and academic performance to optimal career paths,
with job market data and salary projections.
"""

from typing import Dict, List, Any, Optional
from core_domain.player.player_model import Player


# Major-to-Career-Path mappings
MAJOR_CAREER_ALIGNMENTS: Dict[str, List[str]] = {
    "computer_science": [
        "tech_entry",      # Primary path
        "data_entry",
        "ai_entry",
    ],
    "data_science": [
        "data_entry",      # Primary
        "tech_entry",
        "research_entry",
    ],
    "business_admin": [
        "business_entry",  # Primary
        "finance_entry",
        "consulting_entry",
    ],
    "finance": [
        "finance_entry",   # Primary
        "trading_entry",
        "business_entry",
    ],
    "accounting": [
        "accounting_entry",  # Primary
        "finance_entry",
        "consulting_entry",
    ],
    "economics": [
        "research_entry",    # Primary
        "finance_entry",
        "policy_entry",
    ],
    "psychology": [
        "consulting_entry",  # Primary
        "research_entry",
        "hr_entry",
    ],
    "political_science": [
        "policy_entry",      # Primary
        "consulting_entry",
        "government_entry",
    ],
    "history": [
        "research_entry",    # Primary
        "consulting_entry",
        "government_entry",
    ],
    "engineering": [
        "tech_entry",        # Primary
        "engineering_entry",
    ],
    "physics": [
        "research_entry",    # Primary
        "tech_entry",
        "engineering_entry",
    ],
    "mathematics": [
        "research_entry",    # Primary
        "tech_entry",
        "finance_entry",
    ],
    "biology": [
        "research_entry",    # Primary
        "healthcare_entry",
    ],
    "chemistry": [
        "research_entry",    # Primary
        "engineering_entry",
    ],
    "liberal_arts": [
        "consulting_entry",  # Primary
        "policy_entry",
    ],
}

# Career tier salary ranges (annual, 2024 data)
CAREER_SALARY_RANGES: Dict[str, Dict[str, float]] = {
    "tech_entry": {"min": 65000, "mid": 75000, "max": 90000},
    "tech_mid": {"min": 85000, "mid": 105000, "max": 130000},
    "tech_senior": {"min": 110000, "mid": 135000, "max": 160000},
    "tech_lead": {"min": 140000, "mid": 170000, "max": 220000},
    
    "data_entry": {"min": 70000, "mid": 85000, "max": 105000},
    "data_mid": {"min": 95000, "mid": 120000, "max": 150000},
    "data_senior": {"min": 125000, "mid": 160000, "max": 200000},
    "data_lead": {"min": 160000, "mid": 200000, "max": 260000},
    
    "finance_entry": {"min": 60000, "mid": 75000, "max": 90000},
    "finance_mid": {"min": 78000, "mid": 105000, "max": 130000},
    "finance_senior": {"min": 105000, "mid": 135000, "max": 170000},
    "finance_lead": {"min": 135000, "mid": 175000, "max": 240000},
    
    "business_entry": {"min": 55000, "mid": 70000, "max": 85000},
    "business_mid": {"min": 75000, "mid": 95000, "max": 120000},
    "business_senior": {"min": 100000, "mid": 130000, "max": 160000},
    "business_lead": {"min": 130000, "mid": 165000, "max": 220000},
    
    "consulting_entry": {"min": 65000, "mid": 85000, "max": 110000},
    "consulting_mid": {"min": 95000, "mid": 125000, "max": 160000},
    "consulting_senior": {"min": 130000, "mid": 165000, "max": 210000},
    "consulting_lead": {"min": 165000, "mid": 215000, "max": 300000},
    
    "research_entry": {"min": 50000, "mid": 65000, "max": 80000},
    "research_mid": {"min": 70000, "mid": 95000, "max": 120000},
    "research_senior": {"min": 95000, "mid": 130000, "max": 160000},
    "research_lead": {"min": 130000, "mid": 170000, "max": 220000},
    
    "healthcare_entry": {"min": 55000, "mid": 70000, "max": 85000},
    "healthcare_mid": {"min": 75000, "mid": 100000, "max": 125000},
    "healthcare_senior": {"min": 105000, "mid": 140000, "max": 180000},
    
    "engineering_entry": {"min": 65000, "mid": 80000, "max": 100000},
    "engineering_mid": {"min": 85000, "mid": 110000, "max": 140000},
    "engineering_senior": {"min": 115000, "mid": 145000, "max": 180000},
    "engineering_lead": {"min": 145000, "mid": 185000, "max": 250000},
}

# Job market demand scores (0-100)
JOB_MARKET_DEMAND: Dict[str, Dict[str, Any]] = {
    "tech_entry": {"demand": 95, "growth": "Very High", "outlook": "Excellent"},
    "data_entry": {"demand": 92, "growth": "Extremely High", "outlook": "Excellent"},
    "ai_entry": {"demand": 88, "growth": "Extremely High", "outlook": "Excellent"},
    "finance_entry": {"demand": 75, "growth": "Moderate", "outlook": "Good"},
    "business_entry": {"demand": 70, "growth": "Moderate", "outlook": "Good"},
    "consulting_entry": {"demand": 80, "growth": "High", "outlook": "Good"},
    "research_entry": {"demand": 60, "growth": "Moderate", "outlook": "Stable"},
    "healthcare_entry": {"demand": 98, "growth": "Very High", "outlook": "Excellent"},
    "engineering_entry": {"demand": 90, "growth": "High", "outlook": "Excellent"},
    "policy_entry": {"demand": 65, "growth": "Low", "outlook": "Stable"},
    "government_entry": {"demand": 55, "growth": "Low", "outlook": "Stable"},
    "hr_entry": {"demand": 70, "growth": "Moderate", "outlook": "Good"},
}


def get_career_recommendations(player: Player) -> Dict[str, Any]:
    """
    Get career path recommendations based on major and academic performance.
    
    Returns:
    {
        "primary_recommendation": {
            "path_id": "tech_entry",
            "title": "Junior Developer",
            "reasoning": "...",
            "alignment_score": 95,
        },
        "alternative_recommendations": [...],
        "market_insights": {...},
        "skill_gaps": [...],
    }
    """
    major_id = getattr(player, 'major_id', 'liberal_arts').lower().replace(' ', '_')
    gpa = getattr(player, 'hs_gpa', 3.0)
    year_in_school = getattr(player, 'year_in_school', 1)
    
    # Get aligned career paths for major
    aligned_paths = MAJOR_CAREER_ALIGNMENTS.get(major_id, ["consulting_entry", "business_entry"])
    
    # Score and rank paths
    scored_paths = []
    for path_id in aligned_paths:
        score = _calculate_path_alignment_score(path_id, gpa, year_in_school)
        market_demand = JOB_MARKET_DEMAND.get(path_id, {})
        
        scored_paths.append({
            "path_id": path_id,
            "alignment_score": score,
            "market_demand": market_demand.get("demand", 50),
        })
    
    # Sort by alignment score (highest first)
    scored_paths.sort(key=lambda x: x["alignment_score"], reverse=True)
    
    # Build response
    primary = scored_paths[0] if scored_paths else None
    alternatives = scored_paths[1:3] if len(scored_paths) > 1 else []
    
    return {
        "primary_recommendation": _build_recommendation(primary, player),
        "alternative_recommendations": [_build_recommendation(r, player) for r in alternatives],
        "market_insights": _get_market_insights(scored_paths),
        "salary_projections": _get_salary_projections(scored_paths),
        "skill_development": _get_skill_gaps(primary, player) if primary else [],
    }


def _calculate_path_alignment_score(path_id: str, gpa: float, year: int) -> float:
    """Calculate how well a player's profile aligns with a career path."""
    score = 50.0  # Base score
    
    # GPA premium: top students get higher scores
    if gpa >= 3.8:
        score += 25
    elif gpa >= 3.5:
        score += 20
    elif gpa >= 3.2:
        score += 15
    elif gpa >= 3.0:
        score += 10
    elif gpa >= 2.5:
        score += 5
    
    # Year in school adjustment
    if year >= 4:
        score += 10
    elif year >= 3:
        score += 5
    
    # Path-specific scoring
    if "tech" in path_id or "data" in path_id:
        if gpa >= 3.3:
            score += 10
    elif "consulting" in path_id:
        if gpa >= 3.5:
            score += 10
    elif "finance" in path_id:
        if gpa >= 3.4:
            score += 10
    
    # Market demand bonus
    demand = JOB_MARKET_DEMAND.get(path_id, {}).get("demand", 50)
    score += (demand / 100) * 15  # Max +15 for high demand
    
    return min(100, score)


def _build_recommendation(rec: Optional[Dict], player: Player) -> Dict[str, Any]:
    """Build a detailed recommendation object."""
    if not rec:
        return {}
    
    path_id = rec["path_id"]
    market = JOB_MARKET_DEMAND.get(path_id, {})
    salary = CAREER_SALARY_RANGES.get(path_id, {})
    
    # Infer title from path_id
    title_map = {
        "tech_entry": "Junior Developer",
        "data_entry": "Data Analyst",
        "ai_entry": "AI/ML Engineer (Entry)",
        "finance_entry": "Financial Analyst (Junior)",
        "business_entry": "Business Analyst",
        "consulting_entry": "Management Consultant (Entry)",
        "research_entry": "Research Scientist (Junior)",
        "healthcare_entry": "Healthcare Professional (Entry)",
        "engineering_entry": "Engineer (Entry)",
        "policy_entry": "Policy Analyst",
        "government_entry": "Government Analyst",
        "hr_entry": "HR Specialist (Entry)",
        "trading_entry": "Trading Analyst",
        "accounting_entry": "Accountant (Junior)",
    }
    
    return {
        "path_id": path_id,
        "title": title_map.get(path_id, "Professional"),
        "alignment_score": rec["alignment_score"],
        "market_demand": market.get("demand", 50),
        "market_outlook": market.get("outlook", "Stable"),
        "salary_range": {
            "min": int(salary.get("min", 50000)),
            "mid": int(salary.get("mid", 70000)),
            "max": int(salary.get("max", 100000)),
        },
        "reasoning": _get_recommendation_reasoning(path_id, rec["alignment_score"], player),
    }


def _get_recommendation_reasoning(path_id: str, score: float, player: Player) -> str:
    """Generate human-readable reasoning for recommendation."""
    reasoning_parts = []
    
    gpa = getattr(player, 'hs_gpa', 3.0)
    
    # GPA-based reasoning
    if gpa >= 3.7:
        reasoning_parts.append("Your strong academic performance positions you well for this career.")
    elif gpa >= 3.3:
        reasoning_parts.append("Your solid GPA qualifies you for this career path.")
    elif gpa >= 2.9:
        reasoning_parts.append("This career is a reasonable fit given your academics.")
    else:
        reasoning_parts.append("Consider improving your GPA to strengthen your candidacy.")
    
    # Major alignment
    major = getattr(player, 'major_id', 'liberal_arts')
    reasoning_parts.append(f"Your {major} major aligns well with this career's requirements.")
    
    # Market outlook
    market = JOB_MARKET_DEMAND.get(path_id, {})
    demand = market.get("demand", 50)
    if demand >= 90:
        reasoning_parts.append("This field has very strong job market demand.")
    elif demand >= 75:
        reasoning_parts.append("This field has good job market demand.")
    elif demand >= 60:
        reasoning_parts.append("This field has moderate job market demand.")
    else:
        reasoning_parts.append("This field has moderate job market demand.")
    
    return " ".join(reasoning_parts)


def _get_market_insights(scored_paths: List[Dict]) -> Dict[str, Any]:
    """Get aggregate market insights for recommended paths."""
    if not scored_paths:
        return {}
    
    demands = [p["market_demand"] for p in scored_paths[:3]]
    avg_demand = sum(demands) / len(demands)
    
    return {
        "average_market_demand": round(avg_demand),
        "top_growth_fields": ["AI/ML", "Data Science", "Healthcare Tech"],
        "emerging_opportunities": [
            "AI/ML roles in tech and finance",
            "Data science across all sectors",
            "Healthcare technology positions",
        ],
        "salary_trends": "Tech and data roles show strongest salary growth.",
    }


def _get_salary_projections(scored_paths: List[Dict]) -> Dict[str, Any]:
    """Generate salary projection over career progression."""
    if not scored_paths:
        return {}
    
    top_path = scored_paths[0]["path_id"]
    salaries = CAREER_SALARY_RANGES.get(top_path, {})
    
    # Estimate growth: entry → mid → senior progression
    entry_salary = salaries.get("min", 50000)
    
    return {
        "entry_level_salary": entry_salary,
        "mid_career_salary": entry_salary * 1.4,  # ~40% raise after 3 years
        "senior_level_salary": entry_salary * 1.8,  # ~80% raise after 6 years
        "years_to_senior": 6,
        "average_annual_growth": 0.08,  # 8% avg annual growth
    }


def _get_skill_gaps(rec: Optional[Dict], player: Player) -> List[Dict[str, str]]:
    """Identify skills needed for career path."""
    if not rec:
        return []
    
    path_id = rec["path_id"]
    
    skill_paths = {
        "tech_entry": [
            {"skill": "Python/Java", "importance": "Critical", "action": "Take CS201 (Data Structures)"},
            {"skill": "Problem Solving", "importance": "Critical", "action": "Practice coding challenges"},
            {"skill": "System Design", "importance": "Important", "action": "Study software architecture"},
        ],
        "data_entry": [
            {"skill": "Statistics", "importance": "Critical", "action": "Excel in math courses"},
            {"skill": "SQL/Python", "importance": "Critical", "action": "Learn data manipulation"},
            {"skill": "Data Viz", "importance": "Important", "action": "Study visualization tools"},
        ],
        "finance_entry": [
            {"skill": "Financial Analysis", "importance": "Critical", "action": "Take fin101"},
            {"skill": "Excel", "importance": "Critical", "action": "Master spreadsheets"},
            {"skill": "Economics", "importance": "Important", "action": "Take econ courses"},
        ],
        "consulting_entry": [
            {"skill": "Communication", "importance": "Critical", "action": "Join debate/presentation clubs"},
            {"skill": "Problem-Solving", "importance": "Critical", "action": "Work on case studies"},
            {"skill": "Business Acumen", "importance": "Important", "action": "Take BA courses"},
        ],
    }
    
    return skill_paths.get(path_id, [])


def major_career_alignment_report(major_id: str) -> Dict[str, Any]:
    """
    Generate a report showing all career paths suitable for a major.
    Useful for onboarding or career counseling.
    """
    aligned_paths = MAJOR_CAREER_ALIGNMENTS.get(major_id.lower().replace(' ', '_'), [])
    
    detailed_paths = []
    for path_id in aligned_paths:
        market = JOB_MARKET_DEMAND.get(path_id, {})
        salary = CAREER_SALARY_RANGES.get(path_id, {})
        
        detailed_paths.append({
            "path_id": path_id,
            "demand_score": market.get("demand", 50),
            "outlook": market.get("outlook", "Stable"),
            "salary_range": salary.get("min", 0),
        })
    
    return {
        "major": major_id,
        "recommended_paths": sorted(detailed_paths, key=lambda x: x["demand_score"], reverse=True),
        "total_paths": len(detailed_paths),
    }
