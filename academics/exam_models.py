from __future__ import annotations

from typing import List
from pydantic import BaseModel, Field


class ExamChoice(BaseModel):
    id: str
    text: str
    correct: bool = False


class ExamQuestion(BaseModel):
    id: str
    text: str
    choices: List[ExamChoice] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)


# DTOs you can use in API (optional, but helpful)
class FinalExamQuestionChoice(BaseModel):
    id: str
    text: str


class FinalExamQuestion(BaseModel):
    id: str
    text: str
    choices: List[FinalExamQuestionChoice]


class FinalExamResponse(BaseModel):
    major_id: str
    semester: int
    topic_tags: List[str] = Field(default_factory=list)
    questions: List[FinalExamQuestion]


class ExamAnswer(BaseModel):
    question_id: str
    chosen_choice_id: str


class ExamResult(BaseModel):
    correct_count: int
    total_questions: int
    score_percent: float
