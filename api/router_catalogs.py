from fastapi import APIRouter, HTTPException

from catalogs.majors import MAJORS
from catalogs.colleges import COLLEGES
from catalogs.housing import HOUSING_OPTIONS
from catalogs.jobs import JOB_DEFS
from catalogs.activities import ACTIVITIES
from catalogs.life_events import LIFE_EVENTS

router = APIRouter(prefix="/catalogs", tags=["catalogs"])


@router.get("/majors")
def majors():
    return MAJORS


@router.get("/colleges")
def colleges():
    return COLLEGES


@router.get("/colleges/{college_id}/majors")
def get_college_majors(college_id: str):
    """Get only the majors offered by a specific college."""
    college = COLLEGES.get(college_id)
    if not college:
        raise HTTPException(status_code=404, detail="College not found")
    
    offered = college.get("offered_majors", [])
    return {
        "college_id": college_id,
        "college_name": college["name"],
        "majors": {mid: MAJORS[mid] for mid in offered if mid in MAJORS}
    }


@router.get("/housing")
def housing():
    # Housing are Pydantic models; return dict
    return {k: v.model_dump() for k, v in HOUSING_OPTIONS.items()}


@router.get("/jobs")
def jobs():
    return {k: v.model_dump() for k, v in JOB_DEFS.items()}


@router.get("/activities")
def activities():
    return {k: v.model_dump() for k, v in ACTIVITIES.items()}


@router.get("/life-events")
def life_events():
    return LIFE_EVENTS
