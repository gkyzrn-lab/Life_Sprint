"""
Industry Trends & Job Market Data System

Provides:
- Real-time-like job market data
- Industry trend analysis
- Salary trends by field and experience level
- Job growth projections
- Skills in demand
"""

from typing import Dict, List, Any
from datetime import datetime

# Industry sectors and their performance
INDUSTRY_PERFORMANCE: Dict[str, Dict[str, Any]] = {
    "Technology": {
        "growth_rate": 8.5,  # percentage YoY
        "hiring_intensity": "Very High",
        "salary_growth": 4.2,
        "top_roles": ["Software Engineer", "Data Scientist", "AI/ML Engineer", "DevOps Engineer"],
        "outlook": "Excellent",
        "demand_score": 98,
    },
    "Finance": {
        "growth_rate": 3.2,
        "hiring_intensity": "High",
        "salary_growth": 3.5,
        "top_roles": ["Financial Analyst", "Data Analyst", "Risk Manager", "Portfolio Manager"],
        "outlook": "Good",
        "demand_score": 85,
    },
    "Healthcare": {
        "growth_rate": 6.8,
        "hiring_intensity": "Very High",
        "salary_growth": 2.8,
        "top_roles": ["Healthcare IT", "Biomedical Engineer", "Data Analyst", "Project Manager"],
        "outlook": "Excellent",
        "demand_score": 95,
    },
    "Consulting": {
        "growth_rate": 4.5,
        "hiring_intensity": "High",
        "salary_growth": 4.8,
        "top_roles": ["Management Consultant", "Strategy Consultant", "Business Analyst"],
        "outlook": "Good",
        "demand_score": 82,
    },
    "Manufacturing": {
        "growth_rate": 2.1,
        "hiring_intensity": "Moderate",
        "salary_growth": 2.2,
        "top_roles": ["Engineer", "Operations Manager", "Quality Assurance"],
        "outlook": "Stable",
        "demand_score": 65,
    },
    "Real Estate": {
        "growth_rate": 2.8,
        "hiring_intensity": "Moderate",
        "salary_growth": 2.5,
        "top_roles": ["Analyst", "Property Manager", "Developer"],
        "outlook": "Stable",
        "demand_score": 60,
    },
    "Education": {
        "growth_rate": 1.5,
        "hiring_intensity": "Low",
        "salary_growth": 1.8,
        "top_roles": ["Teacher", "Administrator", "Instructional Designer"],
        "outlook": "Stable",
        "demand_score": 55,
    },
}

# Skills most in demand across industries
SKILLS_IN_DEMAND: Dict[str, Dict[str, Any]] = {
    "Python": {
        "demand_score": 98,
        "industries": ["Technology", "Finance", "Healthcare"],
        "avg_salary_premium": 0.12,  # 12% higher salary
        "growth_trend": "Very High",
    },
    "Java": {
        "demand_score": 90,
        "industries": ["Technology", "Finance"],
        "avg_salary_premium": 0.10,
        "growth_trend": "High",
    },
    "SQL": {
        "demand_score": 95,
        "industries": ["Technology", "Finance", "Healthcare"],
        "avg_salary_premium": 0.10,
        "growth_trend": "Very High",
    },
    "Cloud (AWS/Azure)": {
        "demand_score": 92,
        "industries": ["Technology", "Finance", "Healthcare"],
        "avg_salary_premium": 0.15,
        "growth_trend": "Extremely High",
    },
    "Machine Learning": {
        "demand_score": 88,
        "industries": ["Technology", "Finance", "Healthcare"],
        "avg_salary_premium": 0.20,
        "growth_trend": "Extremely High",
    },
    "Data Analysis": {
        "demand_score": 91,
        "industries": ["Technology", "Finance", "Consulting"],
        "avg_salary_premium": 0.13,
        "growth_trend": "Very High",
    },
    "Product Management": {
        "demand_score": 85,
        "industries": ["Technology", "Finance"],
        "avg_salary_premium": 0.18,
        "growth_trend": "High",
    },
    "Business Analysis": {
        "demand_score": 83,
        "industries": ["Technology", "Consulting", "Finance"],
        "avg_salary_premium": 0.11,
        "growth_trend": "High",
    },
    "Communication": {
        "demand_score": 89,
        "industries": ["All"],
        "avg_salary_premium": 0.08,
        "growth_trend": "Stable",
    },
    "Leadership": {
        "demand_score": 87,
        "industries": ["All"],
        "avg_salary_premium": 0.25,
        "growth_trend": "Stable",
    },
}

# Job market trends
JOB_MARKET_TRENDS: List[Dict[str, Any]] = [
    {
        "trend": "AI/ML Integration Across All Sectors",
        "impact": "High",
        "growth_potential": "Extremely High",
        "description": "Companies across all industries are rapidly integrating AI/ML into products and operations.",
        "opportunity_level": "Excellent",
        "recommended_skills": ["Python", "Machine Learning", "Data Analysis"],
    },
    {
        "trend": "Cloud Computing Dominance",
        "impact": "High",
        "growth_potential": "Very High",
        "description": "Migration to cloud continues accelerating; cloud expertise becoming table stakes.",
        "opportunity_level": "Excellent",
        "recommended_skills": ["Cloud (AWS/Azure)", "DevOps", "Python"],
    },
    {
        "trend": "Cybersecurity Critical Priority",
        "impact": "High",
        "growth_potential": "Very High",
        "description": "Data breaches and regulations drive huge demand for security professionals.",
        "opportunity_level": "Excellent",
        "recommended_skills": ["Cybersecurity", "Network Administration", "Cloud"],
    },
    {
        "trend": "Remote Work Normalization",
        "impact": "Medium",
        "growth_potential": "High",
        "description": "Companies expanding remote hiring globally; flexibility becoming standard.",
        "opportunity_level": "Good",
        "recommended_skills": ["Communication", "Self-Management", "Collaboration Tools"],
    },
    {
        "trend": "Data as Competitive Asset",
        "impact": "High",
        "growth_potential": "Very High",
        "description": "Data-driven decision-making is now expected at all organizational levels.",
        "opportunity_level": "Excellent",
        "recommended_skills": ["SQL", "Data Analysis", "Python"],
    },
    {
        "trend": "Sustainability & ESG Roles Growing",
        "impact": "Medium",
        "growth_potential": "High",
        "description": "Environmental and social governance roles emerging across industries.",
        "opportunity_level": "Good",
        "recommended_skills": ["Analytics", "Strategy", "Domain Knowledge"],
    },
]

# Entry-level to mid-career salary progression by field
SALARY_PROGRESSION: Dict[str, Dict[str, Any]] = {
    "Software Engineering": {
        "entry": {"base": 75000, "range": (65000, 90000)},
        "2_years": {"base": 95000, "range": (80000, 115000)},
        "5_years": {"base": 130000, "range": (105000, 160000)},
        "senior": {"base": 160000, "range": (130000, 220000)},
    },
    "Data Science": {
        "entry": {"base": 85000, "range": (70000, 105000)},
        "2_years": {"base": 115000, "range": (95000, 140000)},
        "5_years": {"base": 155000, "range": (130000, 190000)},
        "senior": {"base": 190000, "range": (160000, 250000)},
    },
    "Finance": {
        "entry": {"base": 72000, "range": (60000, 90000)},
        "2_years": {"base": 95000, "range": (75000, 125000)},
        "5_years": {"base": 135000, "range": (105000, 175000)},
        "senior": {"base": 175000, "range": (140000, 250000)},
    },
    "Consulting": {
        "entry": {"base": 85000, "range": (70000, 110000)},
        "2_years": {"base": 120000, "range": (100000, 150000)},
        "5_years": {"base": 165000, "range": (140000, 210000)},
        "senior": {"base": 220000, "range": (180000, 300000)},
    },
    "Healthcare Tech": {
        "entry": {"base": 70000, "range": (60000, 85000)},
        "2_years": {"base": 92000, "range": (75000, 110000)},
        "5_years": {"base": 125000, "range": (105000, 155000)},
        "senior": {"base": 155000, "range": (130000, 190000)},
    },
}

# Emerging roles with highest growth potential
EMERGING_ROLES: List[Dict[str, Any]] = [
    {
        "role": "Prompt Engineer / AI Specialist",
        "growth": "Extremely High (New field, explosive growth)",
        "avg_salary": 95000,
        "required_skills": ["Python", "Large Language Models", "Communication"],
        "education_path": "CS/Data Science background recommended",
    },
    {
        "role": "Data Ops Engineer",
        "growth": "Very High",
        "avg_salary": 115000,
        "required_skills": ["Python", "SQL", "Cloud", "Data Engineering"],
        "education_path": "CS/Math/Data Science background",
    },
    {
        "role": "Cloud Security Engineer",
        "growth": "Very High",
        "avg_salary": 120000,
        "required_skills": ["Cloud", "Security", "Networking", "Python"],
        "education_path": "CS/Cybersecurity background",
    },
    {
        "role": "ML Ops Engineer",
        "growth": "Very High",
        "avg_salary": 125000,
        "required_skills": ["Python", "ML", "DevOps", "Cloud"],
        "education_path": "CS/Data Science background",
    },
    {
        "role": "Sustainability Analyst",
        "growth": "High",
        "avg_salary": 75000,
        "required_skills": ["Data Analysis", "Environmental Science", "Business"],
        "education_path": "Any major + sustainability focus",
    },
]


def get_industry_overview() -> Dict[str, Any]:
    """Get comprehensive industry overview and market data."""
    return {
        "timestamp": datetime.now().isoformat(),
        "industries": INDUSTRY_PERFORMANCE,
        "summary": {
            "hottest_sector": "Technology",
            "best_hiring": ["Technology", "Healthcare", "Consulting"],
            "best_salaries": ["Consulting", "Technology", "Finance"],
            "most_stable": ["Healthcare", "Finance", "Education"],
        },
    }


def get_skills_market_analysis() -> Dict[str, Any]:
    """Get analysis of skills most in demand."""
    sorted_skills = sorted(
        SKILLS_IN_DEMAND.items(),
        key=lambda x: x[1]["demand_score"],
        reverse=True
    )
    
    return {
        "timestamp": datetime.now().isoformat(),
        "top_10_skills": [
            {
                "skill": skill_name,
                "demand_score": skill_data["demand_score"],
                "salary_premium": f"+{skill_data['avg_salary_premium']*100:.0f}%",
                "trend": skill_data["growth_trend"],
            }
            for skill_name, skill_data in sorted_skills[:10]
        ],
        "skills_matrix": SKILLS_IN_DEMAND,
    }


def get_emerging_opportunities() -> Dict[str, Any]:
    """Get emerging roles and opportunities."""
    return {
        "timestamp": datetime.now().isoformat(),
        "emerging_roles": EMERGING_ROLES,
        "opportunity_note": "These roles are in highest demand with strong salary growth potential.",
        "why_emerging": [
            "AI/ML revolution creating new specialties",
            "Cloud adoption requires new skill sets",
            "Security becomes more critical",
            "Data is core to all business decisions",
            "New regulations creating compliance roles",
        ],
    }


def get_salary_benchmarks() -> Dict[str, Any]:
    """Get salary benchmarks across fields and experience levels."""
    return {
        "timestamp": datetime.now().isoformat(),
        "progression": SALARY_PROGRESSION,
        "note": "Salaries based on 2024 market data. Actual compensation varies by location, company, and individual factors.",
        "salary_growth_rates": {
            "entry_to_2_years": 26,  # average % increase
            "2_to_5_years": 37,
            "5_to_senior": 23,
        },
    }


def get_market_trends_analysis() -> Dict[str, Any]:
    """Get current market trends and their implications."""
    return {
        "timestamp": datetime.now().isoformat(),
        "trends": JOB_MARKET_TRENDS,
        "key_insights": [
            "AI/ML skills now prerequisite for tech careers",
            "Data skills command premium across ALL industries",
            "Cloud expertise becoming table stakes",
            "Soft skills (communication, leadership) increasingly valued",
            "Remote work options expanding hiring pools globally",
        ],
        "advice_for_graduates": [
            "Prioritize learning Python and SQL early",
            "Build projects that demonstrate skills",
            "Stay informed about industry trends",
            "Develop both technical and communication skills",
            "Network and build relationships in target industries",
        ],
    }


def get_field_specific_outlook(field: str) -> Dict[str, Any]:
    """Get detailed outlook for a specific field."""
    field_clean = field.strip().title()
    industry = INDUSTRY_PERFORMANCE.get(field_clean)
    
    if not industry:
        return {
            "error": f"Field '{field}' not found",
            "available_fields": list(INDUSTRY_PERFORMANCE.keys()),
        }
    
    return {
        "field": field_clean,
        "overview": industry,
        "trends": [t for t in JOB_MARKET_TRENDS if any(
            field_clean.lower() in s.lower() or
            any(role.lower() in field_clean.lower() for role in industry["top_roles"])
            for s in [t["trend"]]
        )][:3],
        "top_emerging_roles": [
            r for r in EMERGING_ROLES
            if any(industry_role in r["role"] for industry_role in industry["top_roles"])
        ][:3],
    }
