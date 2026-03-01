"""
Job Market Intelligence Router

Provides:
- Industry performance metrics
- Skills demand analysis  
- Salary benchmarks and trends
- Emerging job opportunities
- Market trend analysis
"""

from fastapi import APIRouter, HTTPException

from catalogs.job_market_data import (
    get_industry_overview,
    get_skills_market_analysis,
    get_emerging_opportunities,
    get_salary_benchmarks,
    get_market_trends_analysis,
    get_field_specific_outlook,
)

router = APIRouter(prefix="/api/market-intelligence", tags=["market-intelligence"])


@router.get("/industry-overview")
def industry_overview():
    """
    Get comprehensive overview of industry performance metrics.
    
    Includes:
    - Growth rates by sector
    - Hiring intensity
    - Salary trends
    - Top roles in each industry
    """
    return get_industry_overview()


@router.get("/skills-analysis")
def skills_analysis():
    """
    Get skills demand analysis and salary premiums.
    
    Shows:
    - Top 10 most demanded skills
    - Salary premium for each skill
    - Industries needing each skill
    - Growth trends
    """
    return get_skills_market_analysis()


@router.get("/emerging-opportunities")
def emerging_opportunities():
    """
    Get emerging roles with highest growth potential.
    
    Includes:
    - New roles (Prompt Engineer, MLOps Engineer, etc.)
    - Average salaries
    - Required skills
    - Educational paths
    """
    return get_emerging_opportunities()


@router.get("/salary-benchmarks")
def salary_benchmarks():
    """
    Get salary benchmarks across industries and experience levels.
    
    Shows:
    - Entry level salaries
    - 2-year, 5-year, and senior progression
    - Average growth rates
    - Industry comparisons
    """
    return get_salary_benchmarks()


@router.get("/market-trends")
def market_trends():
    """
    Get current job market trends and implications.
    
    Includes:
    - Top 6 market trends
    - Impact and growth potential
    - Recommended skills
    - Graduate advice
    """
    return get_market_trends_analysis()


@router.get("/field-outlook/{field_name}")
def field_outlook(field_name: str):
    """
    Get detailed market outlook for a specific industry field.
    
    Query examples:
    - /field-outlook/Technology
    - /field-outlook/Finance
    - /field-outlook/Healthcare
    """
    result = get_field_specific_outlook(field_name)
    
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    
    return result


@router.get("/comparison/{field1}/{field2}")
def compare_fields(field1: str, field2: str):
    """
    Compare job market characteristics between two fields.
    """
    field1_data = get_field_specific_outlook(field1)
    field2_data = get_field_specific_outlook(field2)
    
    if "error" in field1_data or "error" in field2_data:
        raise HTTPException(status_code=404, detail="One or both fields not found")
    
    return {
        "field1": field1_data,
        "field2": field2_data,
        "comparison": {
            "growth_advantage": field1_data["overview"]["growth_rate"] - field2_data["overview"]["growth_rate"],
            "hiring_intensity_1": field1_data["overview"]["hiring_intensity"],
            "hiring_intensity_2": field2_data["overview"]["hiring_intensity"],
            "demand_score_1": field1_data["overview"]["demand_score"],
            "demand_score_2": field2_data["overview"]["demand_score"],
        }
    }


@router.get("/skills-guide/{skill_name}")
def skill_market_guide(skill_name: str):
    """
    Get comprehensive guide for a specific in-demand skill.
    
    Shows:
    - Demand level
    - Industries using it
    - Salary premium
    - Learning resources
    """
    from catalogs.job_market_data import SKILLS_IN_DEMAND
    
    skill = SKILLS_IN_DEMAND.get(skill_name)
    if not skill:
        raise HTTPException(
            status_code=404,
            detail=f"Skill '{skill_name}' not found. Try one of: {list(SKILLS_IN_DEMAND.keys())}"
        )
    
    learning_paths = {
        "Python": [
            {"course": "CS101 (Intro to CS)", "difficulty": "Beginner"},
            {"course": "CS201 (Data Structures)", "difficulty": "Intermediate"},
            {"course": "DS101 (Data Science)", "difficulty": "Intermediate"},
        ],
        "SQL": [
            {"course": "CS201 (Databases)", "difficulty": "Intermediate"},
            {"course": "DS101 (Data Science)", "difficulty": "Intermediate"},
        ],
        "Machine Learning": [
            {"course": "Math201 (Linear Algebra)", "difficulty": "Intermediate"},
            {"course": "DS301 (Machine Learning)", "difficulty": "Advanced"},
            {"course": "DS401 (Deep Learning)", "difficulty": "Advanced"},
        ],
        "Cloud (AWS/Azure)": [
            {"course": "CS301 (Systems)", "difficulty": "Advanced"},
            {"course": "DevOps Courses", "difficulty": "Advanced"},
        ],
        "Data Analysis": [
            {"course": "Math101 (Statistics)", "difficulty": "Intermediate"},
            {"course": "CS101 (Intro)", "difficulty": "Beginner"},
            {"course": "DS101 (Data Science)", "difficulty": "Intermediate"},
        ],
    }
    
    return {
        "skill": skill_name,
        "demand_score": skill["demand_score"],
        "industries": skill["industries"],
        "salary_premium": f"+{skill['avg_salary_premium']*100:.0f}%",
        "growth_trend": skill["growth_trend"],
        "learning_path": learning_paths.get(skill_name, []),
        "career_impact": f"Having this skill increases earning potential and job opportunities significantly",
    }


@router.get("/entry-level-guide")
def entry_level_guide():
    """
    Guide for entry-level professionals entering the job market.
    
    Covers:
    - Best majors/fields for employment
    - Top skills to develop
    - Salary expectations
    - First job guidance
    """
    return {
        "title": "Entry-Level Professional Guide",
        "best_majors": [
            "Computer Science - Highest demand, highest entry salary",
            "Data Science - Rapidly growing, strong salary growth",
            "Engineering - Consistent demand, stable salaries",
            "Finance/Accounting - Good job prospects, competitive pay",
            "Business Admin - Flexible paths, many opportunities",
        ],
        "critical_first_5_years": [
            "Build 2-3 strong projects demonstrating your skills",
            "Develop both technical and soft skills",
            "Network actively in your target industry",
            "Seek mentorship from senior professionals",
            "Consider side projects or freelance work",
        ],
        "typical_entry_salaries": {
            "Software Engineer": "65,000 - 90,000",
            "Data Analyst": "70,000 - 105,000",
            "Financial Analyst": "60,000 - 90,000",
            "Business Analyst": "55,000 - 80,000",
            "Management Consultant": "85,000 - 110,000",
        },
        "salary_growth_expectations": {
            "2_years": "+25-30% typical",
            "5_years": "+50-70% typical",
            "10_years": "+150-200% typical",
        },
        "key_insights": [
            "First job matters - sets trajectory for years",
            "Continuous learning is mandatory in tech",
            "Build your professional brand",
            "Find a mentor early in career",
            "Diversity of experience valuable early on",
        ],
    }
