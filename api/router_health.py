# Health API Router - endpoints for health-related actions
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

from core_domain.store import STORE
from health.service import (
    exercise_session,
    attend_therapy,
    schedule_checkup,
    apply_health_condition,
    get_health_summary,
    get_achievement_progress,
    get_health_history,
    perform_batch_health_actions,
    progress_health_semester,
)

router = APIRouter(prefix="/health", tags=["health"])


# =========================
# Request Models
# =========================

class ExerciseRequest(BaseModel):
    player_id: str
    exercise_type: str = Field(
        ..., 
        description="Type of exercise: gym_membership, campus_gym, running, yoga"
    )


class TherapyRequest(BaseModel):
    player_id: str
    therapy_type: str = Field(
        default="campus_counseling",
        description="Type of therapy: campus_counseling, therapist, meditation"
    )


class CheckupRequest(BaseModel):
    player_id: str
    checkup_type: str = Field(
        default="annual_checkup",
        description="Type of checkup: annual_checkup, teeth_cleaning, eye_exam"
    )


class HealthConditionRequest(BaseModel):
    player_id: str
    condition_id: str = Field(
        ...,
        description="Condition type: cold, flu, broken_arm, depression, sleep_deprivation"
    )


class HealthSummaryRequest(BaseModel):
    player_id: str


class BatchHealthAction(BaseModel):
    type: str = Field(..., description="Action type: exercise, therapy, or checkup")
    exercise_type: Optional[str] = Field(None, description="For exercise: gym_membership, campus_gym, running, yoga")
    therapy_type: Optional[str] = Field(None, description="For therapy: campus_counseling, therapist, meditation")
    checkup_type: Optional[str] = Field(None, description="For checkup: annual_checkup, teeth_cleaning, eye_exam")


class BatchHealthRequest(BaseModel):
    player_id: str
    actions: list[BatchHealthAction] = Field(..., description="List of health actions to perform")



# =========================
# Exercise Endpoints
# =========================

@router.post("/exercise")
def exercise(req: ExerciseRequest):
    """
    Record an exercise session for the player.
    Improves fitness, reduces stress, costs time/money.
    
    Exercise types:
    - gym_membership: $30/month, +5 fitness/session
    - campus_gym: Free, +3 fitness/session
    - running: Free, +4 fitness/session
    - yoga: $50/month, +3 fitness, +5 mental health/session
    """
    player = STORE.get_player(req.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    result = exercise_session(player, req.exercise_type)
    STORE.put_player(player)
    return result


# =========================
# Therapy & Mental Health
# =========================

@router.post("/therapy")
def therapy(req: TherapyRequest):
    """
    Attend a therapy or mental health session.
    Reduces stress, improves mental health, costs money/time.
    
    Therapy types:
    - campus_counseling: Free, +8 mental health/session
    - therapist: $100/session, +10 mental health/session
    - meditation: $10/month, +4 mental health/session
    """
    player = STORE.get_player(req.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    result = attend_therapy(player, req.therapy_type)
    STORE.put_player(player)
    return result


# =========================
# Preventive Care
# =========================

@router.post("/checkup")
def checkup(req: CheckupRequest):
    """
    Schedule a medical checkup or preventive care visit.
    Improves health, may prevent future illnesses.
    Insurance covers 40% of costs.
    
    Checkup types:
    - annual_checkup: $200, +10 health
    - teeth_cleaning: $100, +5 health
    - eye_exam: $150, +3 health
    """
    player = STORE.get_player(req.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    result = schedule_checkup(player, req.checkup_type)
    STORE.put_player(player)
    return result


# =========================
# Illness & Health Conditions
# =========================

@router.post("/condition")
def add_condition(req: HealthConditionRequest):
    """
    Apply a health condition (illness, injury) to player.
    For testing/game events. In normal play, conditions occur randomly.
    
    Conditions:
    - cold: Mild, 1 week, -0.2 GPA, -15 health
    - flu: Moderate, 2 weeks, -0.4 GPA, -25 health
    - broken_arm: Severe, 8 weeks, $5000 cost, -40 health
    - depression: Moderate, 12 weeks, -0.5 GPA, -30 health, -20 mental health
    - sleep_deprivation: Moderate, 4 weeks, -0.3 GPA, -20 health
    """
    player = STORE.get_player(req.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    result = apply_health_condition(player, req.condition_id)
    STORE.put_player(player)
    return result


# =========================
# Health Status
# =========================

@router.get("/{player_id}/summary")
def health_summary(player_id: str):
    """
    Get comprehensive health status for the player including achievements and streaks.
    
    Returns:
    - Overall health status (Excellent/Good/Fair/Poor)
    - Health metrics (health, fitness, mental health, sleep quality)
    - Active conditions count
    - Streaks: current and best exercise streak
    - Achievements: number unlocked and details
    - Streak power multiplier (increases with consecutive exercises)
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return get_health_summary(player)


@router.get("/{player_id}/achievements")
def get_achievements(player_id: str):
    """
    Get all unlocked achievements for the player.
    Shows progress toward future achievements.
    
    Returns:
    - List of unlocked achievements with tiers
    - Achievement progress (e.g., "3/5 exercises to next achievement")
    - Rewards from each achievement
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    if not hasattr(player, 'health') or not player.health.unlocked_achievements:
        return {"achievements": []}
    
    achievements = []
    for achievement in player.health.unlocked_achievements:
        achievements.append({
            "achievement_id": achievement.achievement_id,
            "title": achievement.title,
            "tier": achievement.tier,
            "unlocked_semester": achievement.unlocked_semester,
            "reward": achievement.reward_description,
        })
    
    return {"achievements": achievements}


@router.get("/{player_id}/achievement-progress")
def get_achievement_progress_endpoint(player_id: str):
    """
    Get detailed progress toward all health achievements.
    
    Shows three categories:
    - Unlocked: Already achieved
    - In Progress: 50%+ complete
    - Locked: Less than 50% complete
    
    For each achievement shows:
    - Title, description, tier, reward
    - Current progress (e.g., "3/5 exercises")
    - Percentage complete
    - What's needed to unlock
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return get_achievement_progress(player)


@router.get("/{player_id}/history")
def get_history(player_id: str, limit: int = 20):
    """
    Get player's health history timeline.
    
    Shows recent health events including:
    - Exercises and fitness activities
    - Therapy and mental health sessions
    - Medical checkups and preventive care
    - Illnesses and health conditions
    
    For each event shows impact on health, stress, and cost.
    Also shows current active conditions.
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    return get_health_history(player, limit)


# =========================
# Batch Actions
# =========================

@router.post("/batch-actions")
def batch_actions(req: BatchHealthRequest):
    """
    Perform multiple health actions in one request.
    
    Useful for doing a full health routine:
    - Morning run + therapy session
    - Gym workout + meditation + checkup
    - Any combination of exercise, therapy, and checkups
    
    Returns:
    - Results for each action (success/failure)
    - Total cost of all actions
    - All achievements unlocked
    - All stories triggered
    - Updated health summary
    
    Example request:
    {
        "player_id": "p1",
        "actions": [
            {"type": "exercise", "exercise_type": "running"},
            {"type": "therapy", "therapy_type": "meditation"},
            {"type": "checkup", "checkup_type": "annual_checkup"}
        ]
    }
    """
    player = STORE.get_player(req.player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    actions_list = [action.model_dump() for action in req.actions]
    result = perform_batch_health_actions(player, actions_list)
    STORE.put_player(player)
    return result



@router.get("/{player_id}/streaks")
def get_streaks(player_id: str):
    """
    Get detailed streak information for the player.
    Shows current and best streaks, and motivational messages.
    
    Returns:
    - Current exercise streak with fire emoji
    - Best exercise streak achieved
    - Streak power (multiplier for fitness gains)
    - Days/actions until next achievement unlock
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    health = player.health
    
    # Calculate streak fire emoji
    streak_emojis = min(5, health.current_exercise_streak // 2)  # 🔥 for every 2 days
    fire_display = "🔥" * streak_emojis if streak_emojis > 0 else "No streak"
    
    # Motivational message based on streak
    if health.current_exercise_streak == 0:
        streak_message = "Start your exercise streak today!"
    elif health.current_exercise_streak < 3:
        streak_message = "Keep going! Just a bit more to unlock 'On Fire' 🔥"
    elif health.current_exercise_streak < 7:
        streak_message = "You're on fire! 7 days unlocks 'Unstoppable' achievement!"
    else:
        streak_message = f"🏆 You're unstoppable! Best: {health.best_exercise_streak} days"
    
    return {
        "current_exercise_streak": health.current_exercise_streak,
        "best_exercise_streak": health.best_exercise_streak,
        "streak_fire_display": fire_display,
        "streak_power": health.streak_power,
        "streak_message": streak_message,
        "exercises_all_time": health.total_exercises_all_time,
    }


# =========================
# Semester Progression
# =========================

@router.post("/{player_id}/progress-semester")
def progress_semester(player_id: str):
    """
    Apply health changes at end of semester.
    
    Effects:
    - Health decay if no exercise
    - Mental health decay if no therapy and stress high
    - Progress active health conditions
    - Random illness events
    - Reset exercise/therapy counters
    """
    player = STORE.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    changes = progress_health_semester(player)
    STORE.put_player(player)
    return {
        "player_id": player_id,
        "semester": player.semester,
        "health_changes": changes,
        "health_summary": get_health_summary(player),
    }
