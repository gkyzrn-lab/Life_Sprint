from __future__ import annotations

from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from api.deps import require_player
from academics.exam_service import generate_final_exam, grade_exam
from academics.curriculum import CURRICULUM
from core_domain.utils import safe_details
from core_domain.player.player_model import HistoryEvent

router = APIRouter(prefix="/exams", tags=["exams"])


class GenerateExamRequest(BaseModel):
    player_id: str
    semester: int
    num_questions: int = 3


class SubmitExamRequest(BaseModel):
    player_id: str
    semester: int
    answers: List[dict] = Field(default_factory=list)  # [{question_id, chosen_choice_id}]


def _score_to_grade_points(score_percent: float) -> float:
    s = float(score_percent)
    if s >= 90:
        return 4.0
    if s >= 80:
        return 3.3
    if s >= 70:
        return 2.7
    if s >= 60:
        return 2.0
    return 1.0


def _semester_credits(player, semester: int) -> int:
    sem = CURRICULUM.get(player.college_id, {}).get(player.major_id, {}).get(int(semester))
    if not sem:
        return 0
    return int(sum(c.credits for c in sem.courses))


@router.post("/generate")
def exams_generate(req: GenerateExamRequest):
    p = require_player(req.player_id)
    exam = generate_final_exam(p, req.semester, num_questions=req.num_questions)
    return exam.model_dump()


@router.post("/submit")
def exams_submit(req: SubmitExamRequest):
    p = require_player(req.player_id)

    # grade
    answers = []
    for a in req.answers:
        if "question_id" in a and "chosen_choice_id" in a:
            answers.append(type("A", (), a))  # tiny adapter
    # better: import ExamAnswer model, but we keep it lightweight here

    # Use proper grade function expecting ExamAnswer list.
    # We'll adapt to expected structure by building dict objects with attributes:
    from academics.exam_models import ExamAnswer
    parsed = [ExamAnswer(question_id=a["question_id"], chosen_choice_id=a["chosen_choice_id"]) for a in req.answers]

    result = grade_exam(p, req.semester, parsed)

    # GPA update
    sem_credits = _semester_credits(p, req.semester)
    if sem_credits <= 0:
        raise HTTPException(status_code=404, detail="Semester curriculum not found (credits missing)")

    grade_points = _score_to_grade_points(result.score_percent)

    # cumulative GPA (weighted)
    prev_credits = int(p.stats.total_credits)
    prev_gpa = float(p.stats.gpa)

    new_total_credits = prev_credits + sem_credits
    new_gpa = ((prev_gpa * prev_credits) + (grade_points * sem_credits)) / max(1, new_total_credits)

    p.stats.gpa = round(new_gpa, 3)
    p.stats.total_credits = new_total_credits

    p.history.append(
        HistoryEvent(
            label="Final Exam Submitted",
            semester=p.semester,
            details=safe_details(
                {
                    "score_percent": float(result.score_percent),
                    "grade_points": float(grade_points),
                    "semester_credits": float(sem_credits),
                }
            ),
        )
    )

    return {
        "exam_result": result.model_dump(),
        "updated_player": p,
    }
