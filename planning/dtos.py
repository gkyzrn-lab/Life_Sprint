from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel, Field


class ForecastPlanRequest(BaseModel):
    player_id: str
    housing_option_id: str
    job_id: Optional[str] = None
    activities: List[str] = Field(default_factory=list)


class ForecastPlanResponse(BaseModel):
    player_id: str
    semester: int
    housing_option_id: str
    job_id: Optional[str]
    activities: List[str]

    weekly_load: dict
    warnings: List[str] = Field(default_factory=list)


class SavePlanRequest(BaseModel):
    player_id: str
    semester: int
    housing_option_id: str
    job_id: Optional[str] = None
    activities: List[str] = Field(default_factory=list)


class LockPlanRequest(BaseModel):
    player_id: str
    semester: int


class EmergencyChangeRequest(BaseModel):
    player_id: str
    semester: int

    # optional changes (any combination allowed)
    housing_option_id: Optional[str] = None
    job_id: Optional[str] = None  # pass "" to clear job

    activities: Optional[List[str]] = None  # if provided, replaces list

    # cause
    cause_id: Optional[str] = None
    random_cause: bool = False
