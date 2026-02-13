from pydantic import BaseModel, Field
from typing import List, Optional


class SemesterPlan(BaseModel):
    semester: int
    housing_option_id: str
    job_id: Optional[str] = None
    activities: List[str] = Field(default_factory=list)
    locked: bool = False
