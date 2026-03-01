from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Dict, Any, List
from pydantic import BaseModel

from academics.curriculum import CURRICULUM
from api.deps import require_player
from core_domain.player.player_model import Player
from core_domain.store import STORE
from catalogs.curriculums import CURRICULUMS
from catalogs.course_content import get_course_content, get_course_lessons, get_course_quizzes
from catalogs.curriculum_achievements import (
    CURRICULUM_ACHIEVEMENTS,
    CURRICULUM_BADGES,
    SEMESTER_MILESTONES,
    PROGRESS_LEVELS,
    GAMIFICATION_POINTS,
    CURRICULUM_CHALLENGES
)
from catalogs.course_feedback import (
    SAMPLE_COURSE_FEEDBACK,
    COURSE_FEEDBACK_SUMMARIES,
    STUDENT_SUCCESS_STORIES,
    CourseFeedback
)
from catalogs.learning_paths import (
    LEARNING_PATHS,
    CAREER_INTERESTS,
    recommend_learning_path
)
from catalogs.student_progress import (
    SAMPLE_STUDENT_PROGRESS,
    get_progress_insights,
    check_achievement_unlocked,
    ProgressUpdate
)
from catalogs.educational_resources import (
    COURSE_RESOURCES,
    GENERAL_RESOURCES,
    STUDY_RESOURCES,
    get_resources_for_course,
    get_free_resources_for_course
)
from catalogs.real_world_scenarios import get_course_scenarios
from catalogs.lesson_games import get_lesson_game, get_lesson_games_by_course, LESSON_GAMES
from analytics.readiness_score import calculate_life_readiness_score

router = APIRouter(prefix="/curriculum", tags=["curriculum"])


# Request/Response Models
class AttendClassRequest(BaseModel):
    course_id: str


class ClassContent(BaseModel):
    course_id: str
    course_title: str
    topics: List[str]
    lessons: List[Dict]
    quizzes: List[Dict]
    resources: Dict[str, Any]
    learning_outcomes: List[str]


# ===== STATIC ROUTES FIRST (to avoid conflicts with parameterized routes) =====

@router.get("/available")
@router.get("/enhanced/list")
async def list_available_curricula():
    """Get a list of all available enhanced curricula (majors)."""
    available = [
        {
            "major_id": major_id,
            "major_name": curriculum["major_name"],
            "total_semesters": curriculum["total_semesters"],
            "career_paths": curriculum["career_paths"]
        }
        for major_id, curriculum in CURRICULUMS.items()
    ]
    return {
        "curricula": available,
        "available_majors": available,
        "total_majors": len(CURRICULUMS)
    }


@router.get("/achievements")
async def list_all_achievements():
    """Get all available curriculum achievements that students can earn."""
    total_points = sum(a.get("points", 0) for a in CURRICULUM_ACHIEVEMENTS.values())
    return {
        "achievements": list(CURRICULUM_ACHIEVEMENTS.values()),
        "total_achievements": len(CURRICULUM_ACHIEVEMENTS),
        "categories": ["completion", "performance", "engagement", "milestones"],
        "total_points_available": total_points
    }


@router.get("/badges")
async def list_all_badges():
    """Get all available curriculum badges that students can earn."""
    return {
        "badges": list(CURRICULUM_BADGES.values()),
        "total_badges": len(CURRICULUM_BADGES),
        "tiers": ["bronze", "silver", "gold", "platinum"]
    }


@router.get("/badges/{badge_id}")
async def get_badge_detail(badge_id: str):
    """Get detailed information about a specific badge."""
    badge = CURRICULUM_BADGES.get(badge_id)
    if not badge:
        raise HTTPException(status_code=404, detail="Badge not found")
    return badge


@router.get("/semester-milestones")
@router.get("/milestones")
async def get_semester_milestones():
    """Get milestone information for each semester including goals and tips."""
    return {
        "milestones": SEMESTER_MILESTONES,
        "total_semesters": len(SEMESTER_MILESTONES)
    }


@router.get("/challenges")
async def get_curriculum_challenges():
    """Get all available curriculum challenges that offer bonus points and achievements."""
    return {
        "challenges": CURRICULUM_CHALLENGES,
        "total_challenges": len(CURRICULUM_CHALLENGES)
    }


@router.get("/progress-levels")
async def get_progress_levels():
    """Get information about academic progress levels (Novice, Intermediate, Advanced, Expert)."""
    return {
        "levels": PROGRESS_LEVELS,
        "total_levels": len(PROGRESS_LEVELS)
    }


@router.get("/points-system")
@router.get("/points")
async def get_points_system():
    """Get details about the gamification points system (how points are earned)."""
    return {
        "point_rewards": GAMIFICATION_POINTS,
        "description": "Points are earned for completing courses, achieving high grades, and completing challenges."
    }


@router.get("/success-stories")
async def get_all_success_stories():
    """Get all student success stories across all majors."""
    all_stories = []
    for major_id, stories in STUDENT_SUCCESS_STORIES.items():
        for story in stories:
            all_stories.append({
                **story,
                "major_id": major_id
            })
    
    return {
        "stories": all_stories,
        "total_stories": len(all_stories)
    }


@router.get("/learning-paths")
async def list_learning_paths():
    """Get all available learning paths (specializations within majors)."""
    return {
        "learning_paths": list(LEARNING_PATHS.values()),
        "total_paths": len(LEARNING_PATHS)
    }


@router.get("/career-interests")
async def list_career_interests():
    """Get all available career interest categories for learning path recommendations."""
    return {
        "interests": CAREER_INTERESTS,
        "total_categories": len(CAREER_INTERESTS)
    }


@router.get("/career-assessment")
async def get_career_assessment():
    """Get career assessment questions for personalized recommendations."""
    return CAREER_INTERESTS


@router.get("/resources/study-tips")
async def get_study_tips():
    """Get study techniques and productivity tools to help students succeed."""
    return STUDY_RESOURCES


@router.get("/resources/all-courses")
async def get_all_course_resources():
    """Get a list of all courses that have resources available."""
    return {
        "courses_with_resources": [
            {
                "course_id": course_id,
                "course_name": data["course_name"],
                "resource_count": len(data["resources"])
            }
            for course_id, data in COURSE_RESOURCES.items()
        ],
        "total_courses": len(COURSE_RESOURCES)
    }


# ===== PARAMETERIZED ROUTES (more specific patterns before generic ones) =====

@router.get("/achievements/{achievement_id}")
async def get_achievement_detail(achievement_id: str):
    """Get detailed information about a specific achievement."""
    if achievement_id not in CURRICULUM_ACHIEVEMENTS:
        raise HTTPException(status_code=404, detail="Achievement not found")
    
    return CURRICULUM_ACHIEVEMENTS[achievement_id]


@router.get("/semester-milestones/{semester_num}")
@router.get("/milestones/semester/{semester_num}")
async def get_semester_milestone(semester_num: int):
    """Get milestone details for a specific semester."""
    if semester_num not in SEMESTER_MILESTONES:
        raise HTTPException(status_code=404, detail="Semester milestone not found")
    
    milestone = SEMESTER_MILESTONES[semester_num]
    return {
        "semester": semester_num,
        "milestone": milestone.get("milestone"),
        "level": milestone.get("level"),
        "goals": milestone.get("goals", []),
        "academic_advice": milestone.get("academic_advice", [])
    }


@router.get("/challenges/{challenge_id}")
async def get_challenge_detail(challenge_id: str):
    """Get detailed information about a specific challenge."""
    challenge = next((c for c in CURRICULUM_CHALLENGES if c["id"] == challenge_id), None)
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")
    
    return challenge


# ===== LESSON GAMES ENDPOINTS =====

@router.get("/lessons/{lesson_id}/game")
async def get_lesson_game_endpoint(lesson_id: str):
    """Get the mini-game for a specific lesson to reinforce learning concepts."""
    game = get_lesson_game(lesson_id)
    if not game:
        raise HTTPException(status_code=404, detail=f"No game found for lesson {lesson_id}")
    
    return {
        "game_id": game["game_id"],
        "lesson_id": game["lesson_id"],
        "title": game["title"],
        "game_type": game["game_type"],
        "description": game["description"],
        "objectives": game["objectives"],
        "difficulty": game["difficulty"],
        "estimated_duration_minutes": game["estimated_duration_minutes"],
        "content": game["content"]
    }


@router.get("/courses/{course_id}/games")
async def get_course_games_endpoint(course_id: str):
    """Get games for a specific course (legacy endpoint)."""
    from academics.course_games import get_course_games as fetch_games
    
    games = fetch_games(course_id)
    return {
        "course_id": course_id,
        "games": [
            {
                "id": game.id,
                "title": game.title,
                "description": game.description,
                "topic": game.topic,
                "game_type": game.game_type,
                "estimated_duration_minutes": game.estimated_duration_minutes,
            }
            for game in games
        ]
    }


@router.get("/course/{course_id}")
async def get_course_details(course_id: str):
    """
    Get complete course details including content, topics, games, and resources.
    Perfect for course attendance/class view.
    """
    from academics.course_service import get_course_info
    
    course_info = get_course_info(course_id)
    
    return {
        **course_info,
        "attendance_url": f"/curriculum/attend-class",
        "topics_enriched": course_info.get("formatted_topics"),
        "games_available": len(course_info.get("mini_games", [])),
        "ready_to_play": len(course_info.get("mini_games", [])) > 0
    }

    """Get all mini-games available for lessons in a course."""
    games = get_lesson_games_by_course(course_id)
    
    if not games:
        raise HTTPException(status_code=404, detail=f"No games found for course {course_id}")
    
    return {
        "course_id": course_id,
        "total_games": len(games),
        "games": [
            {
                "game_id": game["game_id"],
                "lesson_id": game["lesson_id"],
                "title": game["title"],
                "game_type": game["game_type"],
                "description": game["description"],
                "difficulty": game["difficulty"],
                "estimated_duration_minutes": game["estimated_duration_minutes"]
            }
            for game in games
        ]
    }


@router.post("/lessons/{lesson_id}/game/submit")
async def submit_lesson_game(lesson_id: str, submission: Dict[str, Any]):
    """Submit game results for a lesson. Tracks which game objectives were mastered."""
    game = get_lesson_game(lesson_id)
    if not game:
        raise HTTPException(status_code=404, detail=f"No game found for lesson {lesson_id}")
    
    # Validate submission has score
    score = submission.get("score", 0)
    max_score = submission.get("max_score", 100)
    percentage = (score / max_score * 100) if max_score > 0 else 0
    
    return {
        "game_id": game["game_id"],
        "lesson_id": lesson_id,
        "score": score,
        "max_score": max_score,
        "percentage": round(percentage, 1),
        "passed": percentage >= 70,  # 70% pass threshold
        "message": "Game completed!" if percentage >= 70 else "Keep practicing!",
        "objectives_covered": game["objectives"],
        "next_lesson": None  # Frontend can determine next lesson
    }


@router.get("/games/all")
async def get_all_lesson_games():
    """Get all available lesson games in the system."""
    return {
        "total_games": len(LESSON_GAMES),
        "games_by_type": _group_games_by_type(),
        "games": [
            {
                "game_id": game["game_id"],
                "lesson_id": game["lesson_id"],
                "title": game["title"],
                "game_type": game["game_type"],
                "difficulty": game["difficulty"]
            }
            for game in LESSON_GAMES.values()
        ]
    }


def _group_games_by_type() -> Dict[str, int]:
    """Helper to count games by type"""
    from collections import Counter
    return dict(Counter(game.get("game_type") for game in LESSON_GAMES.values()))


@router.get("/success-stories/{major_id}")
async def get_success_stories(major_id: str):
    """Get inspirational success stories from students in this major."""
    if major_id not in STUDENT_SUCCESS_STORIES:
        raise HTTPException(status_code=404, detail="No success stories available for this major")
    
    return {
        "major_id": major_id,
        "stories": STUDENT_SUCCESS_STORIES[major_id],
        "total_stories": len(STUDENT_SUCCESS_STORIES[major_id])
    }


@router.get("/feedback/course/{course_id}")
async def get_course_feedback(course_id: str):
    """Get student feedback and reviews for a specific course."""
    if course_id not in SAMPLE_COURSE_FEEDBACK:
        raise HTTPException(status_code=404, detail="No feedback available for this course")
    
    return {
        "course_id": course_id,
        "reviews": SAMPLE_COURSE_FEEDBACK[course_id],
        "total_reviews": len(SAMPLE_COURSE_FEEDBACK[course_id])
    }


@router.get("/feedback/course/{course_id}/summary")
async def get_course_feedback_summary(course_id: str):
    """Get aggregated feedback summary for a course."""
    if course_id not in COURSE_FEEDBACK_SUMMARIES:
        raise HTTPException(status_code=404, detail="No feedback summary available for this course")
    
    return COURSE_FEEDBACK_SUMMARIES[course_id]


@router.post("/feedback/course/{course_id}")
async def submit_course_feedback(course_id: str, feedback: CourseFeedback):
    """Submit feedback for a course."""
    return {
        "message": "Feedback submitted successfully",
        "course_id": course_id,
        "feedback": feedback.model_dump()
    }


@router.get("/learning-paths/major/{major_id}")
async def get_learning_paths_by_major(major_id: str):
    """Get all learning paths available for a specific major."""
    paths = {k: v for k, v in LEARNING_PATHS.items() if v["major_id"] == major_id}
    
    if not paths:
        return {"message": f"No learning paths found for major: {major_id}"}
    
    return {
        "major_id": major_id,
        "learning_paths": list(paths.values()),
        "total_paths": len(paths)
    }


@router.get("/learning-paths/recommend/{major_id}")
async def recommend_learning_paths_by_major(
    major_id: str,
    interests: List[str] = Query(default=[]),
    skills: List[str] = Query(default=[]),
):
    """Get personalized learning path recommendations based on major, interests, and skills."""
    recommendations = recommend_learning_path(major_id, interests, skills)
    return {
        "major_id": major_id,
        "recommendations": recommendations,
        "total_recommendations": len(recommendations)
    }


@router.post("/learning-paths/recommend")
async def recommend_learning_path_endpoint(major_id: str, interests: List[str], skills: List[str]):
    """Get personalized learning path recommendations based on major, interests, and skills."""
    recommendations = recommend_learning_path(major_id, interests, skills)
    return {
        "major_id": major_id,
        "recommendations": recommendations,
        "total_recommendations": len(recommendations)
    }


@router.get("/learning-paths/{path_id}")
async def get_learning_path_detail(path_id: str):
    """Get detailed information about a specific learning path."""
    if path_id not in LEARNING_PATHS:
        raise HTTPException(status_code=404, detail="Learning path not found")
    
    return LEARNING_PATHS[path_id]


@router.get("/resources/subject/{subject}")
async def get_subject_resources(subject: str):
    """Get general resources for a subject area (computer_science, business, mathematics)."""
    if subject not in GENERAL_RESOURCES:
        raise HTTPException(status_code=404, detail="Subject not found")
    
    return GENERAL_RESOURCES[subject]


@router.get("/resources/course/{course_id}")
async def get_course_resources(course_id: str, free_only: bool = Query(default=False)):
    """Get learning resources for a specific course (videos, articles, tools, etc.)."""
    if free_only:
        resources = get_free_resources_for_course(course_id)
        return {
            "course_id": course_id,
            "resources": resources,
            "total_resources": len(resources),
            "filter": "free_only"
        }
    
    course_data = get_resources_for_course(course_id)
    return course_data


@router.get("/resources/recommendations/{major_id}")
async def get_recommended_resources(major_id: str):
    """Get recommended resources based on major."""
    major_to_subject = {
        "cs": "computer_science",
        "business": "business",
        "engineering": "computer_science",
        "mathematics": "mathematics"
    }
    
    subject = major_to_subject.get(major_id)
    if not subject:
        return {"message": "No specific recommendations for this major yet"}
    
    general = GENERAL_RESOURCES.get(subject, {})
    
    return {
        "major_id": major_id,
        "recommended_resources": general.get("resources", []),
        "study_tips": STUDY_RESOURCES
    }


@router.get("/player/{player_id}/semester/{semester}")
def get_player_semester_curriculum(player_id: str, semester: int):
    """Get curriculum for a specific semester for a player."""
    p = require_player(player_id)
    sem = CURRICULUM.get(p.college_id, {}).get(p.major_id, {}).get(int(semester))
    if not sem:
        raise HTTPException(status_code=404, detail="Curriculum not found for this selection")
    return sem.model_dump()


@router.get("/player/{player_id}/detailed-progress")
async def get_detailed_progress(player_id: str):
    """Get comprehensive progress tracking for a student."""
    if player_id in SAMPLE_STUDENT_PROGRESS:
        progress = SAMPLE_STUDENT_PROGRESS[player_id]
        insights = get_progress_insights(progress)
        
        return {
            "progress": progress,
            "insights": insights,
            "timestamp": "2026-02-13T00:00:00Z"
        }
    
    p = require_player(player_id)
    return {
        "player_id": player_id,
        "major_id": p.major_id,
        "message": "Progress tracking not yet initialized for this player"
    }


@router.get("/player/{player_id}/gpa-history")
async def get_gpa_history(player_id: str):
    """Get semester-by-semester GPA history for visualization."""
    return {
        "player_id": player_id,
        "gpa_history": [
            {"semester": 1, "gpa": 3.3, "credits": 15},
            {"semester": 2, "gpa": 3.8, "credits": 16},
            {"semester": 3, "gpa": 3.6, "credits": 17}
        ],
        "current_gpa": 3.6,
        "trend": "improving"
    }


@router.get("/player/{player_id}/achievements-progress")
async def get_achievements_progress(player_id: str):
    """Get achievements earned and progress toward locked achievements."""
    if player_id in SAMPLE_STUDENT_PROGRESS:
        progress = SAMPLE_STUDENT_PROGRESS[player_id]
        earned = progress["achievements_earned"]
        
        earned_details = [CURRICULUM_ACHIEVEMENTS[ach_id] for ach_id in earned if ach_id in CURRICULUM_ACHIEVEMENTS]
        locked = [ach for ach_id, ach in CURRICULUM_ACHIEVEMENTS.items() if ach_id not in earned]
        
        return {
            "player_id": player_id,
            "earned_achievements": earned_details,
            "locked_achievements": locked,
            "total_points": progress["total_points"],
            "completion_percentage": (len(earned) / len(CURRICULUM_ACHIEVEMENTS)) * 100
        }
    
    return {"player_id": player_id, "message": "No achievement data yet"}


@router.post("/player/{player_id}/update-progress")
async def update_progress(player_id: str, update: ProgressUpdate):
    """Update student progress (complete a course, assign grade, etc.)."""
    p = require_player(player_id)
    
    if player_id in SAMPLE_STUDENT_PROGRESS:
        progress_data = SAMPLE_STUDENT_PROGRESS[player_id]
        newly_unlocked = check_achievement_unlocked(progress_data)
        
        return {
            "player_id": player_id,
            "update_applied": update.model_dump(),
            "newly_unlocked_achievements": newly_unlocked,
            "message": "Progress updated successfully"
        }
    
    return {
        "player_id": player_id,
        "message": "Progress update recorded"
    }


@router.get("/player/{player_id}/next-steps")
async def get_next_steps(player_id: str):
    """Get personalized recommendations for what the student should do next."""
    if player_id in SAMPLE_STUDENT_PROGRESS:
        progress = SAMPLE_STUDENT_PROGRESS[player_id]
        insights = get_progress_insights(progress)
        
        next_steps = []
        next_steps.extend([
            {"priority": "high", "action": rec, "category": "academic"}
            for rec in insights["recommendations"]
        ])
        
        if progress["current_semester"] in SEMESTER_MILESTONES:
            milestone = SEMESTER_MILESTONES[progress["current_semester"]]
            next_steps.extend([
                {"priority": "medium", "action": tip, "category": "semester_tip"}
                for tip in milestone["tips"]
            ])
        
        if progress.get("selected_learning_path"):
            path = LEARNING_PATHS.get(progress["selected_learning_path"])
            if path:
                next_steps.append({
                    "priority": "medium",
                    "action": f"Explore {path['name']} electives",
                    "category": "learning_path"
                })
        
        return {
            "player_id": player_id,
            "next_steps": next_steps[:10],
            "current_semester": progress["current_semester"],
            "gpa": progress["overall_gpa"]
        }
    
    return {"player_id": player_id, "message": "No recommendations available yet"}


@router.get("/player/{player_id}/compare-peers")
async def compare_with_peers(player_id: str):
    """Compare student's progress with peers in the same major."""
    p = require_player(player_id)
    
    return {
        "player_id": player_id,
        "your_gpa": 3.6,
        "major_average_gpa": 3.2,
        "your_percentile": 75,
        "your_credits": 32,
        "average_credits_at_semester": 30,
        "comparison": {
            "gpa": "above_average",
            "pace": "on_track",
            "achievements": "above_average"
        },
        "message": "You're performing better than 75% of students in your major! 🎉"
    }


@router.get("/enhanced/{major_id}/visualization")
async def get_curriculum_visualization(major_id: str):
    """Get a visual-friendly structure of the curriculum for flowcharts or timeline displays."""
    if major_id not in CURRICULUMS:
        raise HTTPException(status_code=404, detail="Major not found")
    
    curriculum = CURRICULUMS[major_id]
    
    timeline = []
    for sem_num, semester in curriculum["semesters"].items():
        timeline.append({
            "semester": sem_num,
            "title": semester["title"],
            "description": semester["description"],
            "course_count": len(semester["courses"]),
            "total_credits": sum(course["credits"] for course in semester["courses"]),
            "difficulty_distribution": {
                "low": sum(1 for c in semester["courses"] if c["difficulty"] == "low"),
                "medium": sum(1 for c in semester["courses"] if c["difficulty"] == "medium"),
                "high": sum(1 for c in semester["courses"] if c["difficulty"] == "high"),
                "very_high": sum(1 for c in semester["courses"] if c["difficulty"] == "very_high")
            },
            "key_courses": [c["name"] for c in semester["courses"][:3]]
        })
    
    return {
        "major_id": major_id,
        "major_name": curriculum["major_name"],
        "total_semesters": curriculum["total_semesters"],
        "timeline": timeline,
        "career_paths": curriculum["career_paths"],
        "total_skills": len(curriculum["skills_gained"])
    }


@router.get("/enhanced/{major_id}/roadmap")
async def get_curriculum_roadmap(major_id: str):
    """Get a high-level roadmap showing progression through the major."""
    if major_id not in CURRICULUMS:
        raise HTTPException(status_code=404, detail="Major not found")
    
    curriculum = CURRICULUMS[major_id]
    
    years = []
    for year_num in range(1, 5):
        fall_sem = (year_num - 1) * 2 + 1
        spring_sem = (year_num - 1) * 2 + 2
        
        fall = curriculum["semesters"].get(fall_sem)
        spring = curriculum["semesters"].get(spring_sem)
        
        if fall or spring:
            years.append({
                "year": year_num,
                "label": f"Year {year_num}",
                "fall_semester": fall["title"] if fall else None,
                "spring_semester": spring["title"] if spring else None,
                "milestone": SEMESTER_MILESTONES.get(fall_sem, {}).get("milestone") if fall else None
            })
    
    return {
        "major_id": major_id,
        "major_name": curriculum["major_name"],
        "years": years,
        "roadmap": years
    }


@router.get("/enhanced/{major_id}/semester/{semester_num}")
async def get_semester_detail(major_id: str, semester_num: int):
    """Get detailed information about a specific semester in a major's curriculum."""
    if major_id not in CURRICULUMS:
        raise HTTPException(status_code=404, detail="Major not found")
    
    curriculum = CURRICULUMS[major_id]
    
    if semester_num not in curriculum["semesters"]:
        raise HTTPException(status_code=404, detail=f"Semester {semester_num} not found for this major")
    
    semester = curriculum["semesters"][semester_num]
    enriched_courses = [
        {
            **course,
            "real_world_scenarios": get_course_scenarios(course["id"], course.get("name", course["id"]))
        }
        for course in semester["courses"]
    ]
    semester = {**semester, "courses": enriched_courses}
    return {
        "major_id": major_id,
        "major_name": curriculum["major_name"],
        "semester_info": semester
    }


@router.get("/enhanced/{major_id}")
async def get_enhanced_curriculum(major_id: str):
    """Retrieve comprehensive curriculum information for a major with detailed semester breakdowns."""
    if major_id not in CURRICULUMS:
        raise HTTPException(status_code=404, detail="Major not found")

    curriculum = CURRICULUMS[major_id]
    enriched_semesters = {
        semester_num: {
            **semester,
            "courses": [
                {
                    **course,
                    "real_world_scenarios": get_course_scenarios(course["id"], course.get("name", course["id"]))
                }
                for course in semester["courses"]
            ]
        }
        for semester_num, semester in curriculum["semesters"].items()
    }
    return {
        "major_id": major_id,
        "major_name": curriculum["major_name"],
        "total_semesters": curriculum["total_semesters"],
        "semesters": enriched_semesters,
        "career_paths": curriculum["career_paths"],
        "skills_gained": curriculum["skills_gained"]
    }


@router.post("/attend-class")
async def attend_class(request: AttendClassRequest):
    """
    Attend a class and retrieve learning content for the course.
    Returns lessons, quizzes, topics, and resources for the course.
    """
    course_id = request.course_id.lower() if request and request.course_id else None
    
    if not course_id:
        raise HTTPException(status_code=400, detail="course_id is required")
    
    # Get course content
    content = get_course_content(course_id)
    
    if not content:
        raise HTTPException(status_code=404, detail=f"No learning content found for course {course_id}")
    
    # Get resources for this course (if available)
    resources_data = COURSE_RESOURCES.get(course_id.upper(), {})
    
    return {
        "course_id": course_id,
        "course_title": content.get("title", "Unknown Course"),
        "topics": content.get("topics", []),
        "lessons": content.get("lessons", []),
        "quizzes": content.get("quizzes", []),
        "learning_outcomes": content.get("learning_outcomes", []),
        "resources": resources_data,
        "message": f"You are now attending {content.get('title', 'Unknown Course')}. Complete lessons and quizzes to master the material!"
    }

# ===== MINI-GAMES ENDPOINTS =====

@router.get("/games/course/{course_id}")
async def get_course_games(course_id: str, player_id: str | None = Query(default=None)):
    """
    Get all available mini-games for a specific course.
    These interactive games help students learn course concepts.
    """
    from academics.course_games import get_course_games as fetch_games
    
    games = fetch_games(course_id)

    player = STORE.get_player(player_id) if player_id else None
    seen_ids = set(player.mini_game_seen_by_course.get(course_id, [])) if player else set()

    completed_entries = [g for g in (player.completed_games if player else []) if g.get("course_id") == course_id]
    completed_ids = {g.get("game_id") for g in completed_entries}
    best_score_by_game: Dict[str, float] = {}
    for entry in completed_entries:
        gid = str(entry.get("game_id"))
        score = float(entry.get("score_percent", 0.0))
        if gid not in best_score_by_game or score > best_score_by_game[gid]:
            best_score_by_game[gid] = score
    
    if not games:
        return {
            "course_id": course_id,
            "games": [],
            "message": f"No mini-games available yet for {course_id}. Check back soon!"
        }
    
    return {
        "course_id": course_id,
        "games": [
            {
                "id": game.id,
                "title": game.title,
                "description": game.description,
                "topic": game.topic,
                "game_type": game.game_type,
                "estimated_duration_minutes": game.estimated_duration_minutes,
                "question_count": len(game.questions),
                "points_per_correct": game.points_per_correct,
                "min_passing_score": game.min_passing_score,
                "average_question_difficulty": round(
                    (sum(float(q.difficulty) for q in game.questions) / max(1, len(game.questions))),
                    2,
                ),
                "seen": game.id in seen_ids or game.id in completed_ids,
                "completed": game.id in completed_ids,
                "best_score_percent": round(best_score_by_game.get(game.id, 0.0), 1) if game.id in best_score_by_game else None,
            }
            for game in games
        ],
        "total_games": len(games),
        "message": f"🎮 {len(games)} interactive game(s) available to master this topic!"
    }


@router.get("/games/{game_id}")
async def get_game_details(game_id: str):
    """
    Get full details of a specific mini-game including all questions.
    """
    from academics.course_games import get_game_by_id
    
    game = get_game_by_id(game_id)
    
    if not game:
        raise HTTPException(status_code=404, detail=f"Game {game_id} not found")
    
    return {
        "id": game.id,
        "course_id": game.course_id,
        "title": game.title,
        "description": game.description,
        "topic": game.topic,
        "game_type": game.game_type,
        "estimated_duration_minutes": game.estimated_duration_minutes,
        "points_per_correct": game.points_per_correct,
        "points_per_incorrect": game.points_per_incorrect,
        "min_passing_score": game.min_passing_score,
        "questions": [
            {
                "id": q.id,
                "prompt": q.prompt,
                "options": q.options,
                "difficulty": q.difficulty,
                # Note: correct_option_index NOT included here to prevent cheating
            }
            for q in game.questions
        ],
        "message": f"Ready to learn about {game.topic}? Complete this interactive game!"
    }


class GameSubmissionRequest(BaseModel):
    """Request to submit game answers"""
    game_id: str
    course_id: str
    answers: List[Dict[str, Any]]  # List of {question_id, selected_option_index}
    time_spent_minutes: int


class MarkGameSeenRequest(BaseModel):
    game_id: str
    course_id: str


@router.post("/games/seen")
async def mark_game_seen(request: MarkGameSeenRequest, player: Player = Depends(require_player)):
    from academics.course_games import get_game_by_id

    game = get_game_by_id(request.game_id)
    if not game:
        raise HTTPException(status_code=404, detail=f"Game {request.game_id} not found")
    if game.course_id != request.course_id:
        raise HTTPException(status_code=400, detail="Game does not belong to this course")

    seen_list = player.mini_game_seen_by_course.get(request.course_id, [])
    if request.game_id not in seen_list:
        seen_list.append(request.game_id)
        player.mini_game_seen_by_course[request.course_id] = seen_list
        STORE.put_player(player)

    return {
        "course_id": request.course_id,
        "game_id": request.game_id,
        "seen_count_for_course": len(player.mini_game_seen_by_course.get(request.course_id, [])),
        "message": "Mini-game marked as seen",
    }


def _clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _apply_game_outcome_effects(player: Player, course_id: str, score_percent: float, passed: bool, points_earned: float) -> Dict[str, float]:
    """
    Apply mini-game outcome impacts to life stats for realistic progression.
    Positive outcomes reduce stress / improve skills; poor outcomes add pressure.
    """
    score_ratio = _clamp(float(score_percent) / 100.0, 0.0, 1.0)
    points = max(0.0, float(points_earned))

    deltas: Dict[str, float] = {
        "balance": 0.0,
        "stress": 0.0,
        "happiness": 0.0,
        "burnout": 0.0,
        "gpa": 0.0,
        "technical_skills": 0.0,
        "business_acumen": 0.0,
        "communication_skills": 0.0,
        "time_management": 0.0,
        "energy_level": 0.0,
    }

    if passed:
        deltas["balance"] = round(20.0 + points * 0.4, 2)
        deltas["stress"] = round(-(1.5 + 3.5 * score_ratio), 2)
        deltas["happiness"] = round(1.0 + 3.0 * score_ratio, 2)
        deltas["burnout"] = round(-(0.8 + 2.0 * score_ratio), 2)
        deltas["gpa"] = round(0.01 + 0.03 * score_ratio, 3)
        deltas["energy_level"] = round(0.5 + 2.0 * score_ratio, 2)
        deltas["time_management"] = round(0.4 + 1.6 * score_ratio, 2)
    else:
        miss_ratio = 1.0 - score_ratio
        deltas["balance"] = round(-(8.0 + 12.0 * miss_ratio), 2)
        deltas["stress"] = round(2.5 + 4.0 * miss_ratio, 2)
        deltas["happiness"] = round(-(1.0 + 2.5 * miss_ratio), 2)
        deltas["burnout"] = round(1.2 + 2.8 * miss_ratio, 2)
        deltas["gpa"] = round(-(0.005 + 0.015 * miss_ratio), 3)
        deltas["energy_level"] = round(-(0.4 + 1.6 * miss_ratio), 2)
        deltas["time_management"] = round(0.2 + 0.8 * score_ratio, 2)

    cid = (course_id or "").lower()
    if cid.startswith("cs"):
        deltas["technical_skills"] = round(1.0 + 3.0 * score_ratio, 2)
    elif cid.startswith("ba") or cid.startswith("econ"):
        deltas["business_acumen"] = round(1.0 + 3.0 * score_ratio, 2)
        deltas["communication_skills"] = round(0.5 + 1.5 * score_ratio, 2)
    elif cid.startswith("eng") or cid.startswith("phys"):
        deltas["technical_skills"] = round(0.8 + 2.6 * score_ratio, 2)
        deltas["time_management"] += round(0.3 + 0.9 * score_ratio, 2)
    else:
        deltas["communication_skills"] = round(0.4 + 1.2 * score_ratio, 2)

    player.finance.balance = round(float(player.finance.balance) + deltas["balance"], 2)

    player.stats.stress = _clamp(float(player.stats.stress) + deltas["stress"], 0.0, 100.0)
    player.stats.happiness = _clamp(float(player.stats.happiness) + deltas["happiness"], 0.0, 100.0)
    player.stats.burnout = _clamp(float(player.stats.burnout) + deltas["burnout"], 0.0, 100.0)
    player.stats.gpa = _clamp(float(player.stats.gpa) + deltas["gpa"], 0.0, 4.0)
    player.stats.technical_skills = _clamp(float(player.stats.technical_skills) + deltas["technical_skills"], 0.0, 100.0)
    player.stats.business_acumen = _clamp(float(player.stats.business_acumen) + deltas["business_acumen"], 0.0, 100.0)
    player.stats.communication_skills = _clamp(float(player.stats.communication_skills) + deltas["communication_skills"], 0.0, 100.0)
    player.stats.time_management = _clamp(float(player.stats.time_management) + deltas["time_management"], 0.0, 100.0)
    player.stats.energy_level = _clamp(float(player.stats.energy_level) + deltas["energy_level"], 0.0, 100.0)

    return deltas


def _apply_career_consequences_from_game(player: Player, course_id: str, score_percent: float, passed: bool) -> Dict[str, Any]:
    """
    Career-facing consequences from mini-game outcomes:
    - unlock/block internship/interview opportunities
    - adjust long-term salary multiplier
    """
    cid = (course_id or "").lower()
    internship_key = f"internship_{cid}"
    interview_key = f"interview_{cid}"

    unlocked_now: List[str] = []
    blocked_now: List[str] = []

    # Ensure fields exist (backward compatibility for older players)
    if not hasattr(player, "career_unlocked_opportunities"):
        player.career_unlocked_opportunities = []
    if not hasattr(player, "career_blocked_opportunities"):
        player.career_blocked_opportunities = []
    if not hasattr(player, "career_salary_multiplier"):
        player.career_salary_multiplier = 1.0

    score = float(score_percent)

    if passed and score >= 85.0:
        for key in (internship_key, interview_key):
            if key not in player.career_unlocked_opportunities:
                player.career_unlocked_opportunities.append(key)
                unlocked_now.append(key)

            if key in player.career_blocked_opportunities:
                player.career_blocked_opportunities.remove(key)

        player.career_salary_multiplier = _clamp(float(player.career_salary_multiplier) + 0.02, 0.8, 1.5)

    elif passed:
        if internship_key not in player.career_unlocked_opportunities:
            player.career_unlocked_opportunities.append(internship_key)
            unlocked_now.append(internship_key)

        if internship_key in player.career_blocked_opportunities:
            player.career_blocked_opportunities.remove(internship_key)

        player.career_salary_multiplier = _clamp(float(player.career_salary_multiplier) + 0.01, 0.8, 1.5)

    else:
        if score < 60.0:
            if interview_key not in player.career_blocked_opportunities:
                player.career_blocked_opportunities.append(interview_key)
                blocked_now.append(interview_key)

            if interview_key in player.career_unlocked_opportunities:
                player.career_unlocked_opportunities.remove(interview_key)

            player.career_salary_multiplier = _clamp(float(player.career_salary_multiplier) - 0.02, 0.8, 1.5)
        else:
            player.career_salary_multiplier = _clamp(float(player.career_salary_multiplier) - 0.005, 0.8, 1.5)

    return {
        "unlocked_now": unlocked_now,
        "blocked_now": blocked_now,
        "salary_multiplier": round(float(player.career_salary_multiplier), 3),
        "total_unlocked": len(player.career_unlocked_opportunities),
        "total_blocked": len(player.career_blocked_opportunities),
    }


@router.post("/games/submit")
async def submit_game(request: GameSubmissionRequest, player: Player = Depends(require_player)):
    """
    Submit game answers and receive score, feedback, and learning points.
    """
    from academics.course_games import get_game_by_id, calculate_game_score
    
    game = get_game_by_id(request.game_id)
    if not game:
        raise HTTPException(status_code=404, detail=f"Game {request.game_id} not found")
    
    if game.course_id != request.course_id:
        raise HTTPException(status_code=400, detail="Game does not belong to this course")
    
    # Grade the game
    correct_count = 0
    feedback_details = []
    key_learnings = []
    
    question_map = {q.id: q for q in game.questions}
    
    for answer in request.answers:
        question_id = answer.get("question_id")
        selected_index = answer.get("selected_option_index")
        
        if question_id not in question_map:
            continue
        
        question = question_map[question_id]
        is_correct = selected_index == question.correct_option_index
        
        if is_correct:
            correct_count += 1
            feedback_details.append({
                "question_id": question_id,
                "is_correct": True,
                "learning_point": question.learning_point
            })
        else:
            feedback_details.append({
                "question_id": question_id,
                "is_correct": False,
                "correct_answer": question.options[question.correct_option_index],
                "explanation": question.explanation,
                "learning_point": question.learning_point
            })
        
        key_learnings.append(question.learning_point)
    
    # Calculate score
    score_data = calculate_game_score(correct_count, len(request.answers), game)
    
    # Award points to player based on performance
    player.game_points += score_data["points_earned"]

    # Track completed games
    player.completed_games.append({
        "game_id": request.game_id,
        "course_id": request.course_id,
        "score_percent": score_data["score_percent"],
        "points_earned": score_data["points_earned"],
        "passed": score_data["passed"],
        "timestamp": "now"  # Replace with actual timestamp in future
    })

    seen_list = player.mini_game_seen_by_course.get(request.course_id, [])
    if request.game_id not in seen_list:
        seen_list.append(request.game_id)
        player.mini_game_seen_by_course[request.course_id] = seen_list

    life_impact = _apply_game_outcome_effects(
        player,
        course_id=request.course_id,
        score_percent=score_data["score_percent"],
        passed=score_data["passed"],
        points_earned=score_data["points_earned"],
    )

    career_consequences = _apply_career_consequences_from_game(
        player,
        course_id=request.course_id,
        score_percent=score_data["score_percent"],
        passed=score_data["passed"],
    )

    player.history.append(
        {
            "label": "Mini-Game Completed",
            "semester": player.semester,
            "details": {
                "score_percent": float(score_data["score_percent"]),
                "points_earned": float(score_data["points_earned"]),
                "passed": 1.0 if score_data["passed"] else 0.0,
                "delta_stress": float(life_impact["stress"]),
                "delta_happiness": float(life_impact["happiness"]),
                "delta_burnout": float(life_impact["burnout"]),
                "delta_balance": float(life_impact["balance"]),
                "delta_gpa": float(life_impact["gpa"]),
                "career_salary_multiplier": float(player.career_salary_multiplier),
            },
        }
    )

    STORE.put_player(player)
    
    return {
        "game_id": request.game_id,
        "course_id": request.course_id,
        "score_percent": score_data["score_percent"],
        "points_earned": score_data["points_earned"],
        "correct_answers": score_data["correct_answers"],
        "total_questions": score_data["total_questions"],
        "passed": score_data["passed"],
        "time_spent_minutes": request.time_spent_minutes,
        "feedback": feedback_details,
        "key_learnings": list(set(key_learnings)),  # Unique learnings
        "total_game_points": player.game_points,
        "life_impact": life_impact,
        "updated_stats": {
            "stress": float(player.stats.stress),
            "happiness": float(player.stats.happiness),
            "burnout": float(player.stats.burnout),
            "gpa": float(player.stats.gpa),
            "technical_skills": float(player.stats.technical_skills),
            "business_acumen": float(player.stats.business_acumen),
            "communication_skills": float(player.stats.communication_skills),
            "time_management": float(player.stats.time_management),
            "energy_level": float(player.stats.energy_level),
            "balance": float(player.finance.balance),
        },
        "career_consequences": career_consequences,
        "message": (
            f"🎉 Great job! You scored {score_data['score_percent']:.1f}% and earned {score_data['points_earned']} points!"
            if score_data["passed"]
            else f"💡 You scored {score_data['score_percent']:.1f}%. Review the correct answers and try again!"
        )
    }


@router.get("/analytics/{player_id}")
def get_life_readiness_analytics(player_id: str):
    """
    Get comprehensive Life Readiness Score analytics.
    Shows player's readiness across skill domains based on mini-game performance.
    
    Returns:
    - Overall readiness score (0-100)
    - Domain breakdowns (finance, leadership, technical, critical thinking, ethics)
    - Strengths and areas for growth
    - Career readiness indicators
    - Recommended next challenges
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    analytics = calculate_life_readiness_score(player)
    
    # Save updated player with badges and history
    STORE.put_player(player)
    
    return {
        "player_id": player_id,
        "player_name": player.name,
        "semester": player.semester,
        "analytics": analytics.model_dump(),
        "readiness_history": player.readiness_history,
    }