# Student progress tracking system
# Track courses completed, GPA, achievements, and overall progress

from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class CourseProgress(BaseModel):
    """Progress for a single course"""
    course_id: str
    course_name: str
    semester: int
    status: str  # "not_started", "in_progress", "completed", "failed"
    grade: Optional[str] = None  # "A", "B", "C", "D", "F"
    credits: int
    difficulty: str
    started_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None
    attempts: int = 1
    
    
class SemesterProgress(BaseModel):
    """Progress for an entire semester"""
    semester_number: int
    semester_name: str
    status: str  # "not_started", "in_progress", "completed"
    courses: List[CourseProgress]
    total_credits: int
    completed_credits: int
    gpa: Optional[float] = None
    started_date: Optional[datetime] = None
    completed_date: Optional[datetime] = None


class StudentProgress(BaseModel):
    """Overall student progress through their degree"""
    player_id: str
    major_id: str
    major_name: str
    current_semester: int
    total_semesters: int
    
    # Overall metrics
    overall_gpa: float = 0.0
    total_credits_earned: int = 0
    total_credits_required: int
    completion_percentage: float = 0.0
    
    # Semester-by-semester progress
    semesters: List[SemesterProgress] = []
    
    # Achievements and gamification
    achievements_earned: List[str] = []
    total_points: int = 0
    current_level: str = "freshman"
    
    # Learning path
    selected_learning_path: Optional[str] = None
    learning_path_progress: int = 0  # Percentage of path-specific courses completed
    
    # Statistics
    courses_completed: int = 0
    courses_in_progress: int = 0
    courses_remaining: int = 0
    best_semester_gpa: float = 0.0
    worst_semester_gpa: float = 0.0
    
    # Streaks and milestones
    current_streak: int = 0  # Consecutive semesters with 3.0+ GPA
    longest_streak: int = 0
    dean_list_semesters: int = 0  # Semesters with 3.5+ GPA
    
    # Career readiness
    internships_completed: int = 0
    projects_completed: int = 0
    networking_events_attended: int = 0
    

class ProgressUpdate(BaseModel):
    """Update to student progress"""
    course_id: str
    new_status: Optional[str] = None
    grade: Optional[str] = None
    notes: Optional[str] = None


# Helper functions for progress calculations

def calculate_gpa(grades: List[str], credits: List[int]) -> float:
    """Calculate GPA from grades and credits"""
    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    
    total_points = 0.0
    total_credits = 0
    
    for grade, credit in zip(grades, credits):
        if grade in grade_points:
            total_points += grade_points[grade] * credit
            total_credits += credit
    
    return total_points / total_credits if total_credits > 0 else 0.0


def calculate_completion_percentage(credits_earned: int, credits_required: int) -> float:
    """Calculate degree completion percentage"""
    return (credits_earned / credits_required * 100) if credits_required > 0 else 0.0


def check_achievement_unlocked(progress: StudentProgress) -> List[str]:
    """Check which achievements the student has unlocked"""
    newly_unlocked = []
    
    # First semester
    if progress.current_semester >= 2 and "first_semester" not in progress.achievements_earned:
        newly_unlocked.append("first_semester")
    
    # Dean's list
    if progress.best_semester_gpa >= 3.5 and "dean_list" not in progress.achievements_earned:
        newly_unlocked.append("dean_list")
    
    # Halfway there
    if progress.completion_percentage >= 50 and "halfway_there" not in progress.achievements_earned:
        newly_unlocked.append("halfway_there")
    
    # Graduation ready
    if progress.completion_percentage >= 100 and "graduation_ready" not in progress.achievements_earned:
        newly_unlocked.append("graduation_ready")
    
    # Comeback kid
    # This would require tracking GPA changes - implement in actual game logic
    
    return newly_unlocked


def get_progress_insights(progress: dict) -> Dict[str, any]:
    """Generate insights and recommendations based on progress"""
    insights = {
        "strengths": [],
        "areas_for_improvement": [],
        "recommendations": [],
        "motivational_message": ""
    }
    
    # Handle both dict and object
    if isinstance(progress, dict):
        overall_gpa = progress.get("overall_gpa", 0.0)
        completion_percentage = progress.get("completion_percentage", 0.0)
        current_semester = progress.get("current_semester", 1)
        total_semesters = progress.get("total_semesters", 8)
        dean_list_semesters = progress.get("dean_list_semesters", 0)
        current_streak = progress.get("current_streak", 0)
        internships_completed = progress.get("internships_completed", 0)
        projects_completed = progress.get("projects_completed", 0)
        networking_events_attended = progress.get("networking_events_attended", 0)
    else:
        overall_gpa = progress.overall_gpa
        completion_percentage = progress.completion_percentage
        current_semester = progress.current_semester
        total_semesters = progress.total_semesters
        dean_list_semesters = progress.dean_list_semesters
        current_streak = progress.current_streak
        internships_completed = progress.internships_completed
        projects_completed = progress.projects_completed
        networking_events_attended = progress.networking_events_attended
    
    # Analyze GPA
    if overall_gpa >= 3.5:
        insights["strengths"].append("Excellent academic performance - keep it up!")
        insights["motivational_message"] = "You're crushing it! 🌟"
    elif overall_gpa >= 3.0:
        insights["strengths"].append("Solid academic performance")
        insights["motivational_message"] = "Great work! Stay focused! 💪"
    elif overall_gpa >= 2.5:
        insights["areas_for_improvement"].append("GPA could be stronger")
        insights["recommendations"].append("Consider forming study groups")
        insights["recommendations"].append("Visit professors during office hours")
        insights["motivational_message"] = "You've got this! Small improvements make a big difference. 📈"
    else:
        insights["areas_for_improvement"].append("Academic performance needs attention")
        insights["recommendations"].append("Seek tutoring support immediately")
        insights["recommendations"].append("Meet with academic advisor")
        insights["recommendations"].append("Reduce course load if needed")
        insights["motivational_message"] = "Tough times don't last, tough people do. Ask for help! 🤝"
    
    # Analyze progress pace
    expected_progress = (current_semester / total_semesters) * 100
    if completion_percentage < expected_progress - 10:
        insights["areas_for_improvement"].append("Behind on credit requirements")
        insights["recommendations"].append("Consider summer courses to catch up")
    elif completion_percentage > expected_progress + 10:
        insights["strengths"].append("Ahead of schedule on credits!")
    
    # Check career readiness
    if current_semester >= 5:  # Junior year
        if internships_completed == 0:
            insights["recommendations"].append("Start applying for internships ASAP")
        if projects_completed < 2:
            insights["recommendations"].append("Build more portfolio projects")
        if networking_events_attended < 3:
            insights["recommendations"].append("Attend career fairs and networking events")
    
    # Dean's list recognition
    if dean_list_semesters > 0:
        insights["strengths"].append(f"Made Dean's List {dean_list_semesters} time(s)! 🏆")
    
    # Streak recognition
    if current_streak >= 3:
        insights["strengths"].append(f"Amazing {current_streak}-semester streak of 3.0+ GPA!")
    
    return insights


# Sample progress data for testing
SAMPLE_STUDENT_PROGRESS = {
    "player_001": {
        "player_id": "player_001",
        "major_id": "cs",
        "major_name": "Computer Science",
        "current_semester": 3,
        "total_semesters": 8,
        "overall_gpa": 3.6,
        "total_credits_earned": 32,
        "total_credits_required": 120,
        "completion_percentage": 26.7,
        "achievements_earned": ["first_semester", "dean_list"],
        "total_points": 850,
        "current_level": "sophomore",
        "selected_learning_path": "cs_fullstack",
        "learning_path_progress": 15,
        "courses_completed": 10,
        "courses_in_progress": 4,
        "courses_remaining": 26,
        "best_semester_gpa": 3.8,
        "worst_semester_gpa": 3.3,
        "current_streak": 2,
        "longest_streak": 2,
        "dean_list_semesters": 1,
        "internships_completed": 0,
        "projects_completed": 3,
        "networking_events_attended": 2
    }
}
