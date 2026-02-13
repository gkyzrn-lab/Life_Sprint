from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel, Field


class CurriculumTopic(BaseModel):
    id: str
    label: str
    exam_tags: List[str] = Field(default_factory=list)


class Course(BaseModel):
    id: str
    title: str
    credits: int = 3
    difficulty: int = 5          # 1–10
    weekly_hours: int = 6        # total weekly time commitment
    skills: List[str] = Field(default_factory=list)
    topics: List[CurriculumTopic] = Field(default_factory=list)


class SemesterCurriculum(BaseModel):
    semester: int
    courses: List[Course] = Field(default_factory=list)
    notes: Optional[str] = None
