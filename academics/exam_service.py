from __future__ import annotations

from typing import List, Dict
from fastapi import HTTPException

from core_domain.player.player_model import Player
from academics.exam_models import (
    FinalExamResponse,
    FinalExamQuestion,
    FinalExamQuestionChoice,
    ExamAnswer,
    ExamResult,
)
from academics.exam_pools import EXAM_POOLS
from academics.selectors import (
    get_semester_courses_and_tags,
    get_semester_exam_tags,
    select_exam_questions_with_course_coverage,
)


def generate_final_exam(player: Player, semester: int, num_questions: int = 3) -> FinalExamResponse:
    if semester != player.semester:
        # In v1 we enforce "current semester exam" to keep state consistent
        raise HTTPException(status_code=400, detail="Exam can only be generated for the current semester.")

    major_id = player.major_id
    pool = EXAM_POOLS.get(major_id, {}).get(semester)
    if not pool:
        raise HTTPException(status_code=404, detail="No exam pool found for this major/semester.")

    courses_and_tags = get_semester_courses_and_tags(player.college_id, major_id, semester)
    topic_tags = get_semester_exam_tags(player.college_id, major_id, semester)

    # select questions with coverage
    chosen = select_exam_questions_with_course_coverage(pool, courses_and_tags, n=min(num_questions, len(pool)))

    questions: List[FinalExamQuestion] = []
    for q in chosen:
        questions.append(
            FinalExamQuestion(
                id=q.id,
                text=q.text,
                choices=[FinalExamQuestionChoice(id=c.id, text=c.text) for c in q.choices],
            )
        )

    return FinalExamResponse(
        major_id=major_id,
        semester=semester,
        topic_tags=topic_tags,
        questions=questions,
    )


def grade_exam(player: Player, semester: int, answers: List[ExamAnswer]) -> ExamResult:
    major_id = player.major_id
    pool = EXAM_POOLS.get(major_id, {}).get(semester)
    if not pool:
        raise HTTPException(status_code=404, detail="No exam pool found for this major/semester.")

    q_map = {q.id: q for q in pool}

    correct = 0
    total = 0

    for a in answers:
        q = q_map.get(a.question_id)
        if not q:
            continue
        total += 1
        chosen = next((c for c in q.choices if c.id == a.chosen_choice_id), None)
        if chosen and chosen.correct:
            correct += 1

    score_percent = 0.0 if total == 0 else (correct / total) * 100.0
    return ExamResult(correct_count=correct, total_questions=total, score_percent=score_percent)
