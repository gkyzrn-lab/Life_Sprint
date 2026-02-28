from __future__ import annotations

from uuid import uuid4
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, field_validator

from core_domain.store import STORE
from core_domain.config import DEFAULT_START_AGE, DEFAULT_START_BALANCE, DEFAULT_BASE_MONTHLY_NONHOUSING_EXPENSES
from core_domain.player.player_model import Player
from core_domain.stats.stats_model import Stats
from core_domain.finance.finance_models import Finance

from catalogs.colleges import COLLEGES
from catalogs.majors import MAJORS
from catalogs.housing import HOUSING_OPTIONS
from catalogs.jobs import JOB_DEFS

router = APIRouter(prefix="/player", tags=["player"])

# Backward compatibility for legacy college ids used by older clients/tests.
LEGACY_COLLEGE_ID_MAP = {
    "nyc_public": "cuny_baruch",
    "nyc_private": "nyu",
}


class StartPlayerRequest(BaseModel):
    name: str = Field(min_length=1, description="Player's name (required, non-empty)")
    college_id: str = Field(description="ID of the college (must exist in catalogs)")
    major_id: str = Field(description="ID of the major (must exist in catalogs)")

    # Optional player customizations
    age: Optional[int] = Field(None, description="Player's age (optional, default: 18)")
    hs_gpa: float = Field(3.0, ge=0.0, le=4.0, description="High school GPA (0-4.0)")
    parent_income: float = Field(60000.0, ge=0.0, description="Parent income (non-negative)")
    starting_balance: float = Field(5000.0, ge=500.0, description="Starting wallet balance (minimum $500)")

    # starting choices
    housing_option_id: str = Field("dorm", description="ID of housing option (must exist in catalogs)")
    job_id: Optional[str] = Field(None, description="ID of starting job (optional, must exist if provided)")

    @field_validator('age')
    @classmethod
    def validate_age(cls, v: Optional[int]) -> Optional[int]:
        if v is not None and (v < 5 or v > 25):
            raise ValueError('Age must be between 5 and 25')
        return v

    @field_validator('hs_gpa')
    @classmethod
    def validate_gpa(cls, v: float) -> float:
        if v < 0.0 or v > 4.0:
            raise ValueError('GPA must be between 0.0 and 4.0')
        return v

    @field_validator('parent_income')
    @classmethod
    def validate_income(cls, v: float) -> float:
        if v < 0.0:
            raise ValueError('Parent income must be non-negative')
        return v


@router.post("/start")
def start_player(req: StartPlayerRequest):
    """
    Create a new player and start the game.
    Validates all catalog references and returns clear error messages.
    """
    normalized_college_id = LEGACY_COLLEGE_ID_MAP.get(req.college_id, req.college_id)

    # Validate college
    if normalized_college_id not in COLLEGES:
        available = ', '.join(sorted(COLLEGES.keys()))
        raise HTTPException(
            status_code=422,
            detail=f"Invalid college_id '{req.college_id}'. Available colleges: {available}"
        )

    # Validate major
    if req.major_id not in MAJORS:
        available = ', '.join(sorted(MAJORS.keys()))
        raise HTTPException(
            status_code=422,
            detail=f"Invalid major_id '{req.major_id}'. Available majors: {available}"
        )

    # Validate housing
    if req.housing_option_id not in HOUSING_OPTIONS:
        available = ', '.join(sorted(HOUSING_OPTIONS.keys()))
        raise HTTPException(
            status_code=422,
            detail=f"Invalid housing_option_id '{req.housing_option_id}'. Available options: {available}"
        )

    # Validate job (if provided)
    if req.job_id and req.job_id not in JOB_DEFS:
        available = ', '.join(sorted(JOB_DEFS.keys()))
        raise HTTPException(
            status_code=422,
            detail=f"Invalid job_id '{req.job_id}'. Available jobs: {available}"
        )

    # All validations passed; proceed with player creation
    housing = HOUSING_OPTIONS[req.housing_option_id]
    job = JOB_DEFS[req.job_id] if req.job_id else None

    finance = Finance(
        balance=float(req.starting_balance),
        monthly_expenses=float(housing.monthly_cost) + float(DEFAULT_BASE_MONTHLY_NONHOUSING_EXPENSES),
        tuition_per_semester=0.0,       # will be set during progression (based on college)
        scholarship_per_semester=0.0,   # can be set later
    )

    player = Player(
        id=str(uuid4()),
        name=req.name.strip(),
        age=int(req.age) if req.age is not None else int(DEFAULT_START_AGE),
        hs_gpa=float(req.hs_gpa),
        parent_income=float(req.parent_income),
        major_id=req.major_id,
        college_id=normalized_college_id,
        semester=1,
        year_in_school=1,
        stats=Stats(),
        finance=finance,
        housing=housing,
        job=job,
        plan=None,
        history=[],
    )

    STORE.put_player(player)
    return player


@router.get("/{player_id}")
def get_player(player_id: str):
    p = STORE.get_player(player_id)
    if not p:
        raise HTTPException(status_code=404, detail="Player not found")
    return p
