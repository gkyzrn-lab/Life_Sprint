from __future__ import annotations

from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from api.deps import require_player
from academics.exam_service import generate_final_exam, grade_exam, grade_exam_with_feedback
from academics.curriculum import CURRICULUM
from academics.course_service import (
    get_course_info,
    get_semester_courses,
    mark_course_completed,
    get_semester_exam_status,
    mark_semester_exam_passed,
    can_progress_to_next_semester,
    get_next_semester_info,
)
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
    from academics.exam_models import ExamAnswer
    parsed = [ExamAnswer(question_id=a["question_id"], chosen_choice_id=a["chosen_choice_id"]) for a in req.answers]

    # Get detailed feedback with correct answers if failed
    feedback_result = grade_exam_with_feedback(p, req.semester, parsed)
    result = feedback_result["exam_result"]
    passed = feedback_result["passed"]
    message = feedback_result["message"]
    feedback = feedback_result["feedback"]

    # GPA update
    sem_credits = _semester_credits(p, req.semester)
    if sem_credits <= 0:
        raise HTTPException(status_code=404, detail="Semester curriculum not found (credits missing)")

    grade_points = _score_to_grade_points(result["score_percent"])

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
                    "score_percent": float(result["score_percent"]),
                    "grade_points": float(grade_points),
                    "semester_credits": float(sem_credits),
                    "passed": passed
                }
            ),
        )
    )

    return {
        "exam_result": result,
        "passed": passed,
        "message": message,
        "feedback": feedback,  # Contains correct answers for failed questions
        "updated_player": p,
    }


# ==========================================
# NEW ENDPOINTS: Course Info & Semester Exam
# ==========================================

@router.get("/course-info/{course_id}")
def get_course_info_endpoint(course_id: str):
    """Get course information for displaying in a pop-up modal."""
    return get_course_info(course_id)


class MarkCourseCompleteRequest(BaseModel):
    player_id: str
    course_id: str


@router.post("/course-complete")
def mark_course_complete(req: MarkCourseCompleteRequest):
    """Mark a course as completed when player passes all its quizzes."""
    p = require_player(req.player_id)
    mark_course_completed(p, req.course_id)
    from core_domain.store import STORE
    STORE.put_player(p)
    
    return {
        "success": True,
        "course_id": req.course_id,
        "message": f"Course {req.course_id} marked as completed",
    }


@router.get("/semester-courses")
def get_semester_courses_endpoint(player_id: str):
    """Get all courses for the player's current semester with completion status."""
    p = require_player(player_id)
    courses = get_semester_courses(p)
    return {
        "semester": p.semester,
        "courses": courses,
    }


@router.get("/semester-exam-status")
def get_semester_exam_status_endpoint(player_id: str):
    """Get the status of the semester exam (can it be taken? how many courses completed?)."""
    p = require_player(player_id)
    status = get_semester_exam_status(p)
    return status


@router.post("/semester-exam/generate")
def generate_semester_exam(player_id: str, num_questions: int = 5):
    """
    Generate semester exam with 5 questions from all courses in the semester.
    Must complete all courses in the semester first.
    """
    p = require_player(player_id)
    
    # Check if player can take the exam
    status = get_semester_exam_status(p)
    if not status["can_take_exam"]:
        raise HTTPException(
            status_code=400,
            detail=f"Must complete all {status['total_courses']} courses before taking semester exam. "
                   f"Completed: {status['completed_courses']}/{status['total_courses']}"
        )
    
    exam = generate_final_exam(p, p.semester, num_questions=num_questions)
    return exam.model_dump()


class SubmitSemesterExamRequest(BaseModel):
    player_id: str
    answers: List[dict] = Field(default_factory=list)  # [{question_id, chosen_choice_id}]


@router.post("/semester-exam/submit")
def submit_semester_exam(req: SubmitSemesterExamRequest):
    """
    Submit semester exam answers. Must score 70% to pass.
    Passing allows progression to next semester.
    """
    p = require_player(req.player_id)

    # grade
    from academics.exam_models import ExamAnswer
    parsed = [ExamAnswer(question_id=a["question_id"], chosen_choice_id=a["chosen_choice_id"]) for a in req.answers]

    # Get detailed feedback with correct answers if failed
    feedback_result = grade_exam_with_feedback(p, p.semester, parsed)
    result = feedback_result["exam_result"]
    passed = feedback_result["passed"]
    message = feedback_result["message"]
    feedback = feedback_result["feedback"]

    # GPA update
    sem_credits = _semester_credits(p, p.semester)
    if sem_credits <= 0:
        raise HTTPException(status_code=404, detail="Semester curriculum not found (credits missing)")

    grade_points = _score_to_grade_points(result["score_percent"])

    # cumulative GPA (weighted)
    prev_credits = int(p.stats.total_credits)
    prev_gpa = float(p.stats.gpa)

    new_total_credits = prev_credits + sem_credits
    new_gpa = ((prev_gpa * prev_credits) + (grade_points * sem_credits)) / max(1, new_total_credits)

    p.stats.gpa = round(new_gpa, 3)
    p.stats.total_credits = new_total_credits

    # Mark exam as passed if score >= 70%
    if passed:
        mark_semester_exam_passed(p)

    p.history.append(
        HistoryEvent(
            label="Semester Exam Submitted",
            semester=p.semester,
            details=safe_details(
                {
                    "score_percent": float(result["score_percent"]),
                    "grade_points": float(grade_points),
                    "semester_credits": float(sem_credits),
                    "passed": passed
                }
            ),
        )
    )

    from core_domain.store import STORE
    STORE.put_player(p)

    return {
        "exam_result": result,
        "passed": passed,
        "message": message,
        "feedback": feedback,
        "can_progress": can_progress_to_next_semester(p),
        "updated_player": p,
    }


@router.get("/can-progress-semester")
def check_progression(player_id: str):
    """Check if player can progress to next semester (must have passed semester exam)."""
    p = require_player(player_id)
    can_progress = can_progress_to_next_semester(p)
    
    return {
        "can_progress": can_progress,
        "current_semester": p.semester,
        "semester": p.semester,
        "message": "You can progress to the next semester!" if can_progress else "You must pass the semester exam first.",
    }


@router.post("/progress-semester")
def progress_to_next_semester(player_id: str):
    """Move player to the next semester (only after passing semester exam)."""
    p = require_player(player_id)
    
    if not can_progress_to_next_semester(p):
        raise HTTPException(
            status_code=400,
            detail="You must pass the semester exam before progressing. Current semester: " + str(p.semester)
        )
    
    # Move to next semester
    current_semester = p.semester
    p.semester += 1
    p.year_in_school = (p.semester - 1) // 2 + 1
    
    # Clear completed courses for new semester
    p.completed_courses = []
    
    p.history.append(
        HistoryEvent(
            label="Semester Progression",
            semester=current_semester,
            details=safe_details({
                "from_semester": float(current_semester),
                "to_semester": float(p.semester),
            }),
        )
    )
    
    from core_domain.store import STORE
    STORE.put_player(p)
    
    next_info = get_next_semester_info(p) if p.semester <= 8 else {"message": "🎓 Degree completed!"}
    
    return {
        "success": True,
        "current_semester": p.semester,
        "year_in_school": p.year_in_school,
        "next_semester_info": next_info,
        "updated_player": p,
    }

