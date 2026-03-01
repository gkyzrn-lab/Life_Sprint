"""
Service for course information, completion tracking, and semester exams.
Handles course pop-ups, completion status, and semester exam logic.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any
from fastapi import HTTPException

from core_domain.player.player_model import Player
from academics.curriculum import CURRICULUM
from catalogs.course_content import COURSE_CONTENT
from academics.course_games import get_course_games, get_game_by_id, calculate_game_score
from catalogs.course_topics import format_course_topics


def get_course_info(course_id: str) -> Dict[str, Any]:
    """
    Get course information for displaying in a pop-up modal.
    Returns course title, description, skills, topics, and other metadata.
    Includes mini-games for interactive learning.
    """
    # Search across all majors/semesters to find this course
    course_data = None
    for college_id, majors in CURRICULUM.items():
        for major_id, semesters in majors.items():
            for semester_num, sem_curriculum in semesters.items():
                for course in sem_curriculum.courses:
                    if course.id == course_id:
                        course_data = {
                            "id": course.id,
                            "title": course.title,
                            "credits": course.credits,
                            "difficulty": course.difficulty,
                            "weekly_hours": course.weekly_hours,
                            "skills": course.skills,
                            "topics": [t.label for t in course.topics] if course.topics else [],
                        }
                        break
                if course_data:
                    break
            if course_data:
                break
        if course_data:
            break

    if not course_data:
        raise HTTPException(status_code=404, detail=f"Course {course_id} not found in curriculum")

    # Merge with content data if available
    if course_id in COURSE_CONTENT:
        content = COURSE_CONTENT[course_id]
        course_data["description"] = content.get("brief_info", "")
        course_data["lessons_count"] = len(content.get("lessons", []))
        course_data["quizzes_count"] = len(content.get("quizzes", []))

    # Add mini-games for the course
    games = get_course_games(course_id)
    course_data["mini_games"] = [
        {
            "id": game.id,
            "title": game.title,
            "description": game.description,
            "topic": game.topic,
            "game_type": game.game_type,
            "estimated_duration_minutes": game.estimated_duration_minutes,
            "question_count": len(game.questions),
        }
        for game in games
    ]

    # Add formatted course topics (major-specific enrichment)
    topics_display = format_course_topics(course_id)
    if topics_display.get("found"):
        course_data["formatted_topics"] = topics_display

    return course_data


def get_semester_courses(player: Player) -> List[Dict[str, Any]]:
    """
    Get all courses for the player's current semester.
    Returns course list with completion status.
    """
    sem_curriculum = CURRICULUM.get(player.college_id, {}).get(player.major_id, {}).get(player.semester)
    
    if not sem_curriculum:
        raise HTTPException(status_code=404, detail="Semester curriculum not found")

    courses = []
    for course in sem_curriculum.courses:
        completed = is_course_completed(player, course.id)
        courses.append({
            "id": course.id,
            "title": course.title,
            "credits": course.credits,
            "difficulty": course.difficulty,
            "weekly_hours": course.weekly_hours,
            "skills": course.skills,
            "completed": completed,
        })

    return courses


def is_course_completed(player: Player, course_id: str) -> bool:
    """Check if player has completed a course (passed all its quizzes)."""
    # Check in player's completed_courses list
    return hasattr(player, 'completed_courses') and course_id in player.completed_courses


def mark_course_completed(player: Player, course_id: str) -> None:
    """Mark a course as completed when player passes its quizzes."""
    if not hasattr(player, 'completed_courses'):
        player.completed_courses = []
    
    if course_id not in player.completed_courses:
        player.completed_courses.append(course_id)


def get_semester_exam_status(player: Player) -> Dict[str, Any]:
    """
    Get the status of the semester exam for the player.
    Returns whether exam can be taken, how many courses completed, etc.
    """
    sem_curriculum = CURRICULUM.get(player.college_id, {}).get(player.major_id, {}).get(player.semester)
    
    if not sem_curriculum:
        raise HTTPException(status_code=404, detail="Semester curriculum not found")

    total_courses = len(sem_curriculum.courses)
    completed_courses = sum(1 for c in sem_curriculum.courses if is_course_completed(player, c.id))

    # Can take exam when all courses in semester are completed
    can_take_exam = completed_courses == total_courses
    
    return {
        "semester": player.semester,
        "total_courses": total_courses,
        "completed_courses": completed_courses,
        "can_take_exam": can_take_exam,
        "exam_taken": getattr(player, 'semester_exam_taken', {}).get(str(player.semester), False),
    }


def can_progress_to_next_semester(player: Player) -> bool:
    """
    Check if player can progress to the next semester.
    Must have passed the semester exam.
    """
    if not hasattr(player, 'semester_exam_taken'):
        player.semester_exam_taken = {}
    
    exam_taken = player.semester_exam_taken.get(str(player.semester), False)
    return exam_taken and player.semester < 8


def mark_semester_exam_passed(player: Player) -> None:
    """Mark that player has passed the current semester's exam."""
    if not hasattr(player, 'semester_exam_taken'):
        player.semester_exam_taken = {}
    
    player.semester_exam_taken[str(player.semester)] = True


def get_semester_exam_questions(player: Player, num_questions: int = 5) -> List[Dict[str, Any]]:
    """
    Generate semester exam with questions from all courses in the semester.
    Each course contributes ~1 question (5 questions total for 5 courses).
    """
    from academics.exam_service import generate_final_exam
    
    # Get standard exam with 5 questions
    exam = generate_final_exam(player, player.semester, num_questions=num_questions)
    
    return exam.model_dump()


def get_next_semester_info(player: Player) -> Dict[str, Any]:
    """Get info about the next semester to show when progressing."""
    next_sem = player.semester + 1
    if next_sem > 8:
        return {"message": "🎓 Congratulations! You've completed your degree!"}
    
    sem_curriculum = CURRICULUM.get(player.college_id, {}).get(player.major_id, {}).get(next_sem)
    
    if not sem_curriculum:
        raise HTTPException(status_code=404, detail="Next semester curriculum not found")

    return {
        "semester": next_sem,
        "notes": sem_curriculum.notes,
        "courses": [
            {
                "id": c.id,
                "title": c.title,
                "credits": c.credits,
                "difficulty": c.difficulty,
            }
            for c in sem_curriculum.courses
        ],
    }
