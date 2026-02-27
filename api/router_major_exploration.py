# api/router_major_exploration.py
# ================================================================
# Endpoints for the Major Discovery / Day-in-the-Life system.
# Called ONLY during onboarding before a player selects a major.
# No auth required — these are pre-game exploration endpoints.
# ================================================================

from __future__ import annotations
from fastapi import APIRouter, HTTPException
from catalogs.major_exploration import get_major_exploration, list_all_explorations
from catalogs.majors import MAJORS

router = APIRouter(prefix="/explore", tags=["major-exploration"])


@router.get("/majors")
def list_majors_with_exploration():
    """
    List all majors with basic info and whether a full
    day-in-the-life exploration is available.
    """
    return {
        "majors": list_all_explorations(),
        "total": len(MAJORS),
    }


@router.get("/majors/{major_id}")
def get_major_overview(major_id: str):
    """
    Get the full day-in-the-life exploration for a major.
    Includes scenarios, reality checks, and fit guidance.
    """
    if major_id not in MAJORS:
        available = sorted(MAJORS.keys())
        raise HTTPException(
            status_code=404,
            detail=f"Major '{major_id}' not found. Available: {available}"
        )

    return get_major_exploration(major_id)


@router.get("/majors/{major_id}/scenario/{scenario_index}")
def get_single_scenario(major_id: str, scenario_index: int):
    """
    Get a single scenario by index for step-by-step exploration.
    Frontend can show one scenario at a time for a better UX.
    """
    if major_id not in MAJORS:
        raise HTTPException(status_code=404, detail=f"Major '{major_id}' not found.")

    exploration = get_major_exploration(major_id)
    scenarios = exploration["exploration"].get("scenarios", [])

    if not scenarios:
        raise HTTPException(
            status_code=404,
            detail=f"No scenarios available for major '{major_id}' yet."
        )

    if scenario_index < 0 or scenario_index >= len(scenarios):
        raise HTTPException(
            status_code=400,
            detail=f"Scenario index {scenario_index} out of range. "
                   f"Available: 0 to {len(scenarios) - 1}"
        )

    scenario = scenarios[scenario_index]
    return {
        "major_id": major_id,
        "major_name": exploration["major_name"],
        "scenario_index": scenario_index,
        "total_scenarios": len(scenarios),
        "is_last": scenario_index == len(scenarios) - 1,
        "scenario": scenario,
    }


@router.get("/compare")
def compare_majors(major_a: str, major_b: str):
    """
    Compare two majors side by side.
    Useful when a player is deciding between two options.
    """
    if major_a not in MAJORS:
        raise HTTPException(status_code=404, detail=f"Major '{major_a}' not found.")
    if major_b not in MAJORS:
        raise HTTPException(status_code=404, detail=f"Major '{major_b}' not found.")

    info_a = MAJORS[major_a]
    info_b = MAJORS[major_b]

    exp_a = get_major_exploration(major_a)
    exp_b = get_major_exploration(major_b)

    return {
        "comparison": {
            major_a: {
                "name": info_a["name"],
                "difficulty": info_a["difficulty"],
                "job_outlook": info_a["job_outlook"],
                "typical_salaries": info_a["typical_salaries"],
                "mood": exp_a["exploration"].get("mood", ""),
                "best_fit_for": exp_a["exploration"].get("best_fit_for", ""),
                "not_great_if": exp_a["exploration"].get("not_great_if", ""),
                "reality_check": exp_a["exploration"].get("reality_check", []),
            },
            major_b: {
                "name": info_b["name"],
                "difficulty": info_b["difficulty"],
                "job_outlook": info_b["job_outlook"],
                "typical_salaries": info_b["typical_salaries"],
                "mood": exp_b["exploration"].get("mood", ""),
                "best_fit_for": exp_b["exploration"].get("best_fit_for", ""),
                "not_great_if": exp_b["exploration"].get("not_great_if", ""),
                "reality_check": exp_b["exploration"].get("reality_check", []),
            },
        }
    }


@router.get("/recommend")
def recommend_majors(
    enjoy_math: bool = False,
    enjoy_people: bool = False,
    enjoy_building: bool = False,
    enjoy_writing: bool = False,
    enjoy_helping: bool = False,
    want_high_salary: bool = False,
    want_job_security: bool = False,
    okay_with_grad_school: bool = False,
):
    """
    Simple preference-based major recommender.
    Returns up to 4 suggested majors based on player preferences.
    No quizzes — just honest matching.
    """
    scores: dict[str, int] = {mid: 0 for mid in MAJORS}

    if enjoy_math:
        for m in ["cs", "mathematics", "data_science", "electrical_engineering",
                  "mechanical_engineering", "finance", "economics"]:
            scores[m] = scores.get(m, 0) + 2

    if enjoy_people:
        for m in ["psychology", "nursing", "communications", "ba", "sociology"]:
            scores[m] = scores.get(m, 0) + 2

    if enjoy_building:
        for m in ["cs", "mechanical_engineering", "electrical_engineering",
                  "industrial_engineering", "data_science"]:
            scores[m] = scores.get(m, 0) + 2

    if enjoy_writing:
        for m in ["english", "communications", "history", "politics", "sociology"]:
            scores[m] = scores.get(m, 0) + 2

    if enjoy_helping:
        for m in ["nursing", "psychology", "sociology", "biology"]:
            scores[m] = scores.get(m, 0) + 2

    if want_high_salary:
        high_salary = ["cs", "data_science", "electrical_engineering",
                       "mechanical_engineering", "finance", "accounting", "nursing"]
        for m in high_salary:
            scores[m] = scores.get(m, 0) + 1

    if want_job_security:
        secure = ["nursing", "accounting", "cs", "data_science", "electrical_engineering"]
        for m in secure:
            scores[m] = scores.get(m, 0) + 1

    if okay_with_grad_school:
        for m in ["biology", "psychology", "mathematics", "economics"]:
            scores[m] = scores.get(m, 0) + 1

    # Sort by score, return top 4
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top = [mid for mid, score in ranked[:4] if score > 0]

    return {
        "recommended_majors": [
            {
                "major_id": mid,
                "major_name": MAJORS[mid]["name"],
                "difficulty": MAJORS[mid]["difficulty"],
                "job_outlook": MAJORS[mid]["job_outlook"],
                "typical_salaries": MAJORS[mid]["typical_salaries"],
                "has_exploration": True,
                "explore_url": f"/explore/majors/{mid}",
            }
            for mid in top
        ],
        "tip": "Click 'Explore' on any major to experience a day in that student's life before you decide.",
    }