# Health system service - handles all health-related logic
# Now with achievements, streaks, and narrative moments!
from datetime import datetime
import random
from typing import Optional, Dict, Any

from fastapi import HTTPException

from core_domain.player.player_model import Player
from core_domain.health.health_models import Health, HealthCondition, HealthHistory, Achievement
from catalogs.health import (
    MEDICAL_COSTS,
    FITNESS_OPTIONS,
    HEALTH_CONDITIONS,
    MENTAL_HEALTH_OPTIONS,
    PREVENTIVE_CARE,
    INSURANCE_COST_REDUCTION,
)
from catalogs.health_achievements import HEALTH_ACHIEVEMENTS
from catalogs.health_stories import HEALTH_STORIES


# =========================
# Health Initialization
# =========================

def initialize_player_health(player: Player) -> Health:
    """Initialize health for a new player"""
    return Health()


# =========================
# Achievement System
# =========================

def check_achievements(player: Player) -> list[Dict[str, Any]]:
    """
    Check if player has unlocked any new achievements.
    Returns list of newly unlocked achievements.
    """
    if not hasattr(player, 'health'):
        player.health = Health()
    
    newly_unlocked = []
    health = player.health
    
    for achievement_id, achievement_data in HEALTH_ACHIEVEMENTS.items():
        # Skip if already unlocked
        if any(a.achievement_id == achievement_id for a in health.unlocked_achievements):
            continue
        
        # Check trigger condition
        trigger_type = achievement_data.get("trigger_type")
        trigger_value = achievement_data.get("trigger_value")
        unlocked = False
        
        if trigger_type == "exercises_completed":
            unlocked = health.total_exercises_all_time >= trigger_value
        
        elif trigger_type == "gym_sessions":
            gym_visits = sum(1 for h in health.health_history if h.event_type == "exercise")
            unlocked = gym_visits >= trigger_value
        
        elif trigger_type == "therapy_sessions":
            unlocked = health.total_therapy_sessions_all_time >= trigger_value
        
        elif trigger_type == "mental_sessions":
            unlocked = health.total_therapy_sessions_all_time >= trigger_value
        
        elif trigger_type == "exercise_streak":
            unlocked = health.best_exercise_streak >= trigger_value
        
        elif trigger_type == "healthy_streak":
            unlocked = health.total_checkups_all_time >= trigger_value
        
        elif trigger_type == "checkups_completed":
            unlocked = health.total_checkups_all_time >= trigger_value
        
        elif trigger_type == "combined_health_action":
            required = trigger_value
            unlocked = (
                health.total_exercises_all_time >= required.get("exercises", 0) and
                health.total_therapy_sessions_all_time >= required.get("therapy", 0) and
                health.total_checkups_all_time >= required.get("checkups", 0)
            )
        
        # Unlock achievement if condition met
        if unlocked:
            achievement = Achievement(
                achievement_id=achievement_id,
                title=achievement_data["title"],
                tier=achievement_data["tier"],
                unlocked_semester=player.semester,
                reward_description=achievement_data["reward"]["message"],
            )
            health.unlocked_achievements.append(achievement)
            
            # Apply rewards
            _apply_achievement_rewards(player, achievement_data)
            
            newly_unlocked.append({
                "id": achievement_id,
                "title": achievement_data["title"],
                "tier": achievement_data["tier"],
                "message": achievement_data["reward"]["message"],
                "unlock_info": achievement_data["reward"].get("unlock_info", ""),
            })
    
    return newly_unlocked


def _apply_achievement_rewards(player: Player, achievement_data: Dict[str, Any]):
    """Apply reward modifiers from an achievement"""
    health = player.health
    rewards = achievement_data.get("reward", {})
    
    if "bonus_fitness_multiplier" in rewards:
        health.fitness_multiplier *= rewards["bonus_fitness_multiplier"]
    
    if "stress_reduction_bonus" in rewards:
        health.stress_reduction_bonus += rewards["stress_reduction_bonus"]
    
    if "mental_health_efficiency" in rewards:
        health.mental_health_efficiency = rewards["mental_health_efficiency"]
    
    if "illness_probability_reduction" in rewards:
        health.illness_probability_reduction += rewards["illness_probability_reduction"]
    
    if "gpa_bonus" in rewards:
        health.gpa_health_bonus += rewards["gpa_bonus"]

    if "checkup_cost_reduction" in rewards:
        health.checkup_cost_reduction += rewards["checkup_cost_reduction"]

    if "illness_severity_reduction" in rewards:
        health.illness_severity_reduction += rewards["illness_severity_reduction"]

    if "permanent_health_regen" in rewards:
        health.permanent_health_regen += rewards["permanent_health_regen"]

    if "all_health_multiplier" in rewards:
        health.all_health_multiplier *= rewards["all_health_multiplier"]

    if "permanent_health" in rewards:
        health.health = min(100, health.health + rewards["permanent_health"])
    
    if "gym_cost_reduction" in rewards:
        health.gym_membership_active = True
    
    if "therapy_cost_reduction" in rewards:
        health.therapy_enrolled = True


# =========================
# Streak System
# =========================

def update_exercise_streak(player: Player, exercised: bool) -> Dict[str, Any]:
    """
    Update exercise streak based on whether player exercised.
    """
    health = player.health
    
    if exercised:
        health.current_exercise_streak += 1
        health.best_exercise_streak = max(health.best_exercise_streak, health.current_exercise_streak)
        health.streak_power = 1.0 + (health.current_exercise_streak * 0.05)
        
        return {
            "streak_continuing": True,
            "current_streak": health.current_exercise_streak,
            "best_streak": health.best_exercise_streak,
            "streak_power": health.streak_power,
        }
    else:
        if health.current_exercise_streak > 0:
            broken_info = {
                "streak_broken": True,
                "streak_was": health.current_exercise_streak,
                "best_streak": health.best_exercise_streak,
            }
            health.current_exercise_streak = 0
            health.streak_power = 1.0
            return broken_info
        
        return {"streak_continuing": False, "current_streak": 0}


# =========================
# Story/Narrative System
# =========================

def trigger_health_stories(player: Player, event_type: str) -> Optional[Dict[str, Any]]:
    """Check if any health stories should trigger based on player state"""
    if not hasattr(player, 'health'):
        player.health = Health()
    
    health = player.health
    
    for story_id, story_data in HEALTH_STORIES.items():
        if story_id in health.stories_shown:
            continue
        
        if story_data.get("trigger") != event_type:
            continue
        
        condition = story_data.get("condition", "")
        triggered = _check_story_condition(player, condition)
        
        if triggered:
            health.stories_shown.append(story_id)
            
            effects = story_data.get("effects", {})
            if "happiness_bonus" in effects:
                player.stats.happiness = min(100, player.stats.happiness + effects["happiness_bonus"])
            if "mental_health_bonus" in effects:
                health.mental_health = min(100, health.mental_health + effects["mental_health_bonus"])
            if "stress_reduction" in effects:
                player.stats.stress = max(0, player.stats.stress - effects["stress_reduction"])
            
            return {
                "id": story_id,
                "title": story_data["title"],
                "message": story_data["message"],
                "tone": story_data["tone"],
                "effects": effects,
            }
    
    return None


def _check_story_condition(player: Player, condition: str) -> bool:
    """Simple condition checker for story triggers"""
    if not condition:
        return True
    
    health = player.health
    
    try:
        exercises_this_semester = health.exercises_this_semester
        stress = player.stats.stress
        health_val = health.health
        therapy_sessions = health.therapy_sessions_attended
        
        return eval(condition)
    except:
        return False


# =========================
# Exercise & Fitness
# =========================

def exercise_session(player: Player, exercise_type: str) -> Dict[str, Any]:
    """Record exercise session with streaks, achievements, and stories"""
    if exercise_type not in FITNESS_OPTIONS:
        raise HTTPException(status_code=400, detail=f"Unknown exercise type: {exercise_type}")
    
    if not hasattr(player, 'health'):
        player.health = Health()
    
    exercise = FITNESS_OPTIONS[exercise_type]
    health = player.health
    
    fitness_gain = (
        exercise["fitness_gain_per_session"]
        * health.streak_power
        * health.fitness_multiplier
        * health.all_health_multiplier
    )
    health.fitness = min(100, health.fitness + fitness_gain)
    
    health_gain = fitness_gain * 0.8
    health.health = min(100, health.health + health_gain)
    
    stress_reduction = fitness_gain * 2 + health.stress_reduction_bonus
    player.stats.stress = max(0, player.stats.stress - stress_reduction)
    
    if "mental_health_gain" in exercise:
        health.mental_health = min(
            100,
            health.mental_health + (exercise["mental_health_gain"] * health.all_health_multiplier),
        )
    
    player.stats.happiness = min(100, player.stats.happiness + 5.0)
    
    health.exercises_this_semester += 1
    health.total_exercises_all_time += 1
    health.health_history.append(
        HealthHistory(
            event_id=f"exercise_{health.total_exercises_all_time}",
            event_type="exercise",
            health_impact=health_gain,
            stress_impact=-stress_reduction,
            semester=player.semester,
        )
    )
    
    streak_info = update_exercise_streak(player, True)
    
    cost = exercise.get("monthly_cost", 0.0) / exercise.get("sessions_per_month", 4)
    if cost > 0 and health.gym_membership_active:
        cost = cost * 0.8
    if cost > 0:
        player.finance.balance -= cost
    
    new_achievements = check_achievements(player)
    story = trigger_health_stories(player, "just_exercised")
    
    return {
        "exercise_type": exercise_type,
        "fitness_gain": fitness_gain,
        "health_gain": health_gain,
        "stress_reduction": stress_reduction,
        "cost": cost,
        "total_exercises_this_semester": health.exercises_this_semester,
        "exercise_streak": streak_info,
        "achievements_unlocked": new_achievements,
        "story": story,
    }


# =========================
# Mental Health & Therapy
# =========================

def attend_therapy(player: Player, therapy_type: str = "campus_counseling") -> Dict[str, Any]:
    """Attend therapy with achievements and stories"""
    if therapy_type not in MENTAL_HEALTH_OPTIONS:
        raise HTTPException(status_code=400, detail=f"Unknown therapy type: {therapy_type}")
    
    if not hasattr(player, 'health'):
        player.health = Health()
    
    health = player.health
    therapy = MENTAL_HEALTH_OPTIONS[therapy_type]
    
    mental_gain = (
        therapy["mental_health_gain"]
        * health.mental_health_efficiency
        * health.all_health_multiplier
    )
    health.mental_health = min(100, health.mental_health + mental_gain)
    
    stress_reduction = therapy["stress_reduction"] + health.stress_reduction_bonus
    player.stats.stress = max(0, player.stats.stress - stress_reduction)
    
    player.stats.happiness = min(100, player.stats.happiness + 4.0)
    
    health_gain = mental_gain * 0.6
    health.health = min(100, health.health + health_gain)
    
    cost = therapy["cost_per_session"]
    if health.therapy_enrolled:
        cost = cost * 0.85
    player.finance.balance -= cost
    
    health.therapy_sessions_attended += 1
    health.total_therapy_sessions_all_time += 1
    health.current_therapy_streak += 1
    health.best_therapy_streak = max(health.best_therapy_streak, health.current_therapy_streak)
    
    health.health_history.append(
        HealthHistory(
            event_id=f"therapy_{health.total_therapy_sessions_all_time}",
            event_type="therapy",
            health_impact=health_gain,
            stress_impact=-stress_reduction,
            cost=cost,
            semester=player.semester,
        )
    )
    
    for condition in health.current_conditions:
        if "depression" in condition.condition_id.lower():
            condition.duration_weeks = max(0, condition.duration_weeks - 1)
    
    new_achievements = check_achievements(player)
    story = trigger_health_stories(player, "attended_therapy")
    
    return {
        "therapy_type": therapy_type,
        "mental_health_gain": mental_gain,
        "stress_reduction": stress_reduction,
        "cost": cost,
        "total_sessions": health.total_therapy_sessions_all_time,
        "achievements_unlocked": new_achievements,
        "story": story,
    }


# =========================
# Medical Visits & Preventive Care
# =========================

def schedule_checkup(player: Player, checkup_type: str = "annual_checkup") -> Dict[str, Any]:
    """Schedule checkup with achievements and stories"""
    if checkup_type not in PREVENTIVE_CARE:
        raise HTTPException(status_code=400, detail=f"Unknown checkup type: {checkup_type}")
    
    if not hasattr(player, 'health'):
        player.health = Health()
    
    health = player.health
    checkup = PREVENTIVE_CARE[checkup_type]
    
    cost = checkup["cost"]
    if health.medical_insurance:
        cost = cost * (1 - INSURANCE_COST_REDUCTION)
    if health.checkup_cost_reduction > 0:
        cost = cost * (1 - health.checkup_cost_reduction)
    
    player.finance.balance -= cost
    
    health_gain = checkup["health_gain"] * health.all_health_multiplier
    health.health = min(100, health.health + health_gain)
    
    health.last_checkup_semester = player.semester
    health.total_checkups_all_time += 1
    health.health_history.append(
        HealthHistory(
            event_id=f"checkup_{player.semester}",
            event_type="checkup",
            health_impact=health_gain,
            cost=cost,
            semester=player.semester,
        )
    )
    
    new_achievements = check_achievements(player)
    story = trigger_health_stories(player, "completed_checkup")
    
    return {
        "checkup_type": checkup_type,
        "health_gain": health_gain,
        "cost": cost,
        "cost_before_insurance": checkup["cost"],
        "insurance_savings": checkup["cost"] - cost,
        "last_checkup_semester": health.last_checkup_semester,
        "achievements_unlocked": new_achievements,
        "story": story,
    }


# =========================
# Illness & Injury Events
# =========================

def apply_health_condition(player: Player, condition_id: str, severity: Optional[str] = None) -> Dict[str, Any]:
    """Apply health condition with stories"""
    if condition_id not in HEALTH_CONDITIONS:
        raise HTTPException(status_code=400, detail=f"Unknown condition: {condition_id}")
    
    if not hasattr(player, 'health'):
        player.health = Health()
    
    health = player.health
    condition_data = HEALTH_CONDITIONS[condition_id]
    
    severity_reduction = min(0.8, health.illness_severity_reduction)
    adjusted_duration = max(1, int(condition_data["duration_weeks"] * (1 - severity_reduction)))
    adjusted_health_loss = condition_data.get("health_loss", 10.0) * (1 - severity_reduction)

    condition = HealthCondition(
        condition_id=condition_id,
        name=condition_data["name"],
        severity=condition_data["severity"],
        duration_weeks=adjusted_duration,
        gpa_impact=condition_data.get("gpa_impact", 0.0),
        stress_impact=condition_data.get("stress_impact", 0.0),
        cost=condition_data.get("medical_cost", 0.0),
    )
    
    health.current_conditions.append(condition)
    
    player.stats.stress += condition_data.get("stress_impact", 0.0)
    player.stats.happiness -= condition_data.get("stress_impact", 0.0) * 0.5
    health.health -= adjusted_health_loss
    
    if "mental_health_impact" in condition_data:
        health.mental_health += condition_data["mental_health_impact"]
    
    medical_cost = condition.cost
    if health.medical_insurance:
        medical_cost = medical_cost * (1 - INSURANCE_COST_REDUCTION)
    
    if medical_cost > 0:
        player.finance.balance -= medical_cost
    
    health.health_history.append(
        HealthHistory(
            event_id=f"illness_{len(health.current_conditions)}",
            event_type="illness",
            severity=condition_data["severity"],
            health_impact=-adjusted_health_loss,
            stress_impact=condition_data.get("stress_impact", 0.0),
            cost=medical_cost,
            semester=player.semester,
        )
    )
    
    story = trigger_health_stories(player, "got_sick")
    
    return {
        "condition_id": condition_id,
        "condition_name": condition_data["name"],
        "severity": condition_data["severity"],
        "duration_weeks": adjusted_duration,
        "gpa_impact": condition_data.get("gpa_impact", 0.0),
        "stress_impact": condition_data.get("stress_impact", 0.0),
        "medical_cost": medical_cost,
        "active_conditions": len(health.current_conditions),
        "story": story,
    }


def random_illness_event(player: Player) -> Optional[Dict[str, Any]]:
    """Randomly trigger illness event"""
    if not hasattr(player, 'health'):
        player.health = Health()
    
    health = player.health
    
    fitness_modifier = (100 - health.fitness) / 100
    health_modifier = (100 - health.health) / 100
    achievement_reduction = 1.0 - health.illness_probability_reduction
    
    for condition_id, condition_data in HEALTH_CONDITIONS.items():
        base_probability = condition_data.get("probability", 0.0)
        adjusted_probability = base_probability * fitness_modifier * health_modifier * achievement_reduction
        
        if random.random() < adjusted_probability:
            return apply_health_condition(player, condition_id)
    
    return None


# =========================
# Health Status
# =========================

def get_health_summary(player: Player) -> Dict[str, Any]:
    """Get comprehensive health status summary"""
    if not hasattr(player, 'health'):
        player.health = Health()
    
    health = player.health
    
    if health.health >= 80:
        overall_status = "Excellent"
    elif health.health >= 60:
        overall_status = "Good"
    elif health.health >= 40:
        overall_status = "Fair"
    else:
        overall_status = "Poor"
    
    active_conditions = len([c for c in health.current_conditions if c.duration_weeks > 0])
    
    return {
        "overall_status": overall_status,
        "health": round(health.health, 1),
        "fitness": round(health.fitness, 1),
        "mental_health": round(health.mental_health, 1),
        "sleep_quality": round(health.sleep_quality, 1),
        "active_conditions": active_conditions,
        "total_conditions_history": len(health.health_history),
        "exercises_this_semester": health.exercises_this_semester,
        "therapy_sessions": health.therapy_sessions_attended,
        "medical_insurance": health.medical_insurance,
        "gym_membership_active": health.gym_membership_active,
        "current_exercise_streak": health.current_exercise_streak,
        "best_exercise_streak": health.best_exercise_streak,
        "total_exercises_all_time": health.total_exercises_all_time,
        "total_therapy_sessions_all_time": health.total_therapy_sessions_all_time,
        "total_checkups_all_time": health.total_checkups_all_time,
        "achievements_unlocked": len(health.unlocked_achievements),
        "streak_power": round(health.streak_power, 2),
    }


def get_achievement_progress(player: Player) -> Dict[str, Any]:
    """
    Get detailed achievement progress for all health achievements.
    Shows what's unlocked and progress toward locked achievements.
    """
    if not hasattr(player, 'health'):
        player.health = Health()
    
    health = player.health
    unlocked_ids = set(a.achievement_id for a in health.unlocked_achievements)
    
    progress = {
        "unlocked": [],
        "in_progress": [],
        "locked": [],
        "total_achievements": len(HEALTH_ACHIEVEMENTS),
        "unlocked_count": len(unlocked_ids),
    }
    
    for achievement_id, achievement_data in HEALTH_ACHIEVEMENTS.items():
        achievement_info = {
            "id": achievement_id,
            "title": achievement_data["title"],
            "description": achievement_data["description"],
            "tier": achievement_data["tier"],
            "reward": achievement_data["reward"]["message"],
        }
        
        if achievement_id in unlocked_ids:
            unlocked = next(a for a in health.unlocked_achievements if a.achievement_id == achievement_id)
            achievement_info["unlocked_semester"] = unlocked.unlocked_semester
            progress["unlocked"].append(achievement_info)
            continue
        
        trigger_type = achievement_data.get("trigger_type")
        trigger_value = achievement_data.get("trigger_value")
        
        current_value = 0
        progress_text = ""
        
        if trigger_type == "exercises_completed":
            current_value = health.total_exercises_all_time
            progress_text = f"{current_value}/{trigger_value} exercises"
        elif trigger_type == "gym_sessions":
            current_value = len([h for h in health.health_history if h.event_type == "exercise"])
            progress_text = f"{current_value}/{trigger_value} gym sessions"
        elif trigger_type == "therapy_sessions" or trigger_type == "mental_sessions":
            current_value = health.total_therapy_sessions_all_time
            progress_text = f"{current_value}/{trigger_value} therapy sessions"
        elif trigger_type == "exercise_streak":
            current_value = health.best_exercise_streak
            progress_text = f"{current_value}/{trigger_value} day streak"
        elif trigger_type == "checkups_completed":
            current_value = health.total_checkups_all_time
            progress_text = f"{current_value}/{trigger_value} checkups"
        elif trigger_type == "combined_health_action":
            exercises = health.total_exercises_all_time
            therapy = health.total_therapy_sessions_all_time
            checkups = health.total_checkups_all_time
            target_exercises = trigger_value.get("exercises", 10) if isinstance(trigger_value, dict) else 10
            target_therapy = trigger_value.get("therapy", 5) if isinstance(trigger_value, dict) else 5
            target_checkups = trigger_value.get("checkups", 2) if isinstance(trigger_value, dict) else 2
            progress_text = (
                f"Exercises: {exercises}/{target_exercises}, "
                f"Therapy: {therapy}/{target_therapy}, "
                f"Checkups: {checkups}/{target_checkups}"
            )
            current_value = min(
                exercises / max(target_exercises, 1),
                therapy / max(target_therapy, 1),
                checkups / max(target_checkups, 1),
            ) * 100
        
        achievement_info["progress"] = progress_text
        achievement_info["current_value"] = current_value
        achievement_info["target_value"] = trigger_value if isinstance(trigger_value, (int, float)) else 100
        
        # Use target_value or 1 to avoid division by zero
        target = trigger_value if isinstance(trigger_value, (int, float)) and trigger_value else 1
        if current_value >= target * 0.5:
            achievement_info["percentage"] = round((current_value / target) * 100, 1)
            progress["in_progress"].append(achievement_info)
        else:
            achievement_info["percentage"] = round((current_value / target) * 100, 1)
            progress["locked"].append(achievement_info)
    
    progress["in_progress"].sort(key=lambda x: x["percentage"], reverse=True)
    progress["locked"].sort(key=lambda x: x["percentage"], reverse=True)
    
    return progress


def get_health_history(player: Player, limit: int = 20) -> Dict[str, Any]:
    """
    Get player's health history with timeline of events.
    Shows exercises, therapy, checkups, and illnesses.
    """
    if not hasattr(player, 'health'):
        player.health = Health()
    
    health = player.health
    
    history_list = []
    for event in health.health_history[-limit:]:
        history_list.append({
            "event_id": event.event_id,
            "event_type": event.event_type,
            "semester": event.semester,
            "severity": event.severity if event.severity else None,
            "health_impact": event.health_impact,
            "stress_impact": event.stress_impact,
            "cost": event.cost,
        })
    
    history_list.reverse()
    
    event_type_counts = {}
    for event in health.health_history:
        event_type = event.event_type
        event_type_counts[event_type] = event_type_counts.get(event_type, 0) + 1
    
    return {
        "recent_events": history_list,
        "total_events": len(health.health_history),
        "event_counts": event_type_counts,
        "current_conditions": [
            {
                "condition_id": c.condition_id,
                "name": c.name,
                "severity": c.severity,
                "duration_weeks": c.duration_weeks,
                "gpa_impact": c.gpa_impact,
                "stress_impact": c.stress_impact,
            }
            for c in health.current_conditions if c.duration_weeks > 0
        ],
    }


# =========================
# Semester Progression
# =========================

def progress_health_semester(player: Player) -> Dict[str, Any]:
    """Apply health changes at end of semester"""
    if not hasattr(player, 'health'):
        player.health = Health()
    
    health = player.health
    changes = {}
    
    if health.exercises_this_semester == 0:
        health_decay = 10.0
        health.health = max(0, health.health - health_decay)
        changes["health_decay"] = -health_decay
        update_exercise_streak(player, False)
    else:
        changes["streak_maintained"] = True
        if health.permanent_health_regen > 0:
            regen = health.permanent_health_regen
            health.health = min(100, health.health + regen)
            changes["health_regen"] = regen
    
    if health.therapy_sessions_attended == 0 and player.stats.stress > 50:
        mental_decay = 5.0
        health.mental_health = max(0, health.mental_health - mental_decay)
        changes["mental_health_decay"] = -mental_decay
    
    remaining_conditions = []
    for condition in health.current_conditions:
        condition.duration_weeks -= 1
        if condition.duration_weeks > 0:
            remaining_conditions.append(condition)
    health.current_conditions = remaining_conditions
    
    if random.random() < 0.25:
        illness = random_illness_event(player)
        if illness:
            changes["random_illness"] = illness["condition_name"]
    
    if player.stats.stress > 75:
        story = trigger_health_stories(player, "high_stress_alert")
        if story:
            changes["stress_story"] = story
    
    health.exercises_this_semester = 0
    health.therapy_sessions_attended = 0
    health.current_therapy_streak = 0
    health.stories_shown = []
    
    return changes


def perform_batch_health_actions(player: Player, actions: list[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Perform multiple health actions in one request.
    Useful for players doing multiple activities in one day/week.
    
    Actions format:
    [
        {"type": "exercise", "exercise_type": "running"},
        {"type": "therapy", "therapy_type": "campus_counseling"},
        {"type": "checkup", "checkup_type": "annual_checkup"},
    ]
    """
    results = []
    total_cost = 0.0
    all_achievements = []
    all_stories = []
    
    for action in actions:
        action_type = action.get("type")
        
        try:
            if action_type == "exercise":
                result = exercise_session(player, action.get("exercise_type", "running"))
                results.append({"action": "exercise", "success": True, "result": result})
                total_cost += result.get("cost", 0.0)
                
            elif action_type == "therapy":
                result = attend_therapy(player, action.get("therapy_type", "campus_counseling"))
                results.append({"action": "therapy", "success": True, "result": result})
                total_cost += result.get("cost", 0.0)
                
            elif action_type == "checkup":
                result = schedule_checkup(player, action.get("checkup_type", "annual_checkup"))
                results.append({"action": "checkup", "success": True, "result": result})
                total_cost += result.get("cost", 0.0)
                
            else:
                results.append({"action": action_type, "success": False, "error": f"Unknown action type: {action_type}"})
                continue
            
            if result.get("achievements_unlocked"):
                all_achievements.extend(result["achievements_unlocked"])
            
            if result.get("story"):
                all_stories.append(result["story"])
                
        except Exception as e:
            results.append({"action": action_type, "success": False, "error": str(e)})
    
    return {
        "actions_performed": len([r for r in results if r["success"]]),
        "actions_failed": len([r for r in results if not r["success"]]),
        "results": results,
        "total_cost": total_cost,
        "achievements_unlocked": all_achievements,
        "stories_triggered": all_stories,
        "health_summary": get_health_summary(player),
    }

