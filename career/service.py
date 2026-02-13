"""Career advancement service.

Handles:
- Job transitions and promotions
- Performance tracking (affected by health, education, burnout)
- Burnout accumulation and recovery
- Achievement unlocks
- Career story triggers
- Earnings calculations
"""

from core_domain.player.player_model import Player
from core_domain.career.career_models import Career, CareerAchievement, CareerHistory
from catalogs.career_paths import (
    CAREER_PATHS, BURNOUT_MECHANICS, PERFORMANCE_MODIFIERS, 
    CAREER_ACHIEVEMENTS, CAREER_STORIES, JOB_TIER_MODIFIERS
)
from catalogs.jobs import JOB_DEFS


def accept_job(player: Player, job_id: str) -> dict:
    """Player accepts a new job offer."""
    if job_id not in JOB_DEFS:
        raise ValueError(f"Job {job_id} not found")
    
    job = JOB_DEFS[job_id]
    
    # Initialize career if not exists
    if not hasattr(player, 'career'):
        player.career = Career()
    
    old_job = player.career.current_job_id
    player.job = job  # Keep for compatibility
    
    player.career.current_job_id = job_id
    player.career.current_job_title = job.title
    
    # Find career path tier to set salary
    base_salary = _get_base_salary_for_job(job_id)
    player.career.current_salary = base_salary
    
    player.career.total_jobs_held += 1
    player.career.semesters_at_current_job = 0
    player.career.next_promotion_eligible_semester = player.semester + 2  # Can promote in 2 semesters
    
    # Record in history
    history_entry = CareerHistory(
        event_type="hired",
        job_id=job_id,
        job_title=job.title,
        semester=player.semester,
        salary_before=player.career.current_salary if old_job else 0.0,
        salary_after=base_salary,
        reason="hired" if not old_job else "job_change",
    )
    player.career.history.append(history_entry)
    
    # Trigger "first job" story if applicable
    if not old_job:
        _trigger_story(player, "first_job")
    
    return {
        "job_id": job_id,
        "job_title": job.title,
        "salary": float(player.career.current_salary),
        "message": f"You accepted the position: {job.title}",
    }


def _get_base_salary_for_job(job_id: str) -> float:
    """Get base salary for a job based on career path."""
    # Check if it's a career path position
    if job_id in CAREER_PATHS:
        return float(CAREER_PATHS[job_id]["base_salary"])
    
    # Otherwise get from job definition
    if job_id in JOB_DEFS:
        job = JOB_DEFS[job_id]
        # Estimate salary from hourly wage and hours
        return float(job.hourly_wage * job.hours_per_week * 52)
    
    return 50000.0  # fallback


def update_performance_and_burnout(player: Player) -> dict:
    """
    Called once per semester to:
    - Calculate performance rating
    - Accumulate/recover burnout
    - Check for achievements
    - Trigger stories
    """
    if not hasattr(player, 'career'):
        player.career = Career()
    
    if not player.career.current_job_id:
        return {"career": "no_job"}
    
    # Calculate base performance
    performance = _calculate_performance(player)
    player.career.performance_rating = max(0, min(100, performance))
    
    # Update burnout
    job = JOB_DEFS.get(player.career.current_job_id)
    if job:
        # Stress accumulation from job
        stress_from_job = job.stress_per_semester * BURNOUT_MECHANICS["stress_to_burnout_rate"]
        
        # Burnout increases with stress, decreases with good health
        health_recovery = (player.health.health / 100.0) * BURNOUT_MECHANICS["burnout_recovery_base"]
        
        burnout_change = stress_from_job - health_recovery
        player.career.burnout_level = max(0, min(100, player.career.burnout_level + burnout_change))
    
    # Apply burnout health penalties
    if player.career.burnout_level > 0:
        health_penalty = player.career.burnout_level * BURNOUT_MECHANICS["health_penalty_per_burnout"] / 100
        player.health.health = max(0, player.health.health - health_penalty)
        
        mental_penalty = player.career.burnout_level * BURNOUT_MECHANICS["mental_health_penalty_per_burnout"] / 100
        player.health.mental_health = max(0, player.health.mental_health - mental_penalty)
    
    # Check for achievements
    achievements_unlocked = _check_career_achievements(player)
    
    # Trigger stories
    stories_triggered = []
    if player.career.burnout_level > 85:
        story = _trigger_story(player, "burnout_critical")
        if story:
            stories_triggered.append(story)
    elif player.career.burnout_level > 60:
        story = _trigger_story(player, "burnout_warning")
        if story:
            stories_triggered.append(story)
    
    if player.health.health < 40 and player.career.current_job_id:
        story = _trigger_story(player, "health_impact_on_job")
        if story:
            stories_triggered.append(story)
    
    # Increment semesters at job
    player.career.semesters_at_current_job += 1
    
    return {
        "performance": float(player.career.performance_rating),
        "burnout": float(player.career.burnout_level),
        "health_impact": float(health_penalty) if player.career.burnout_level > 0 else 0.0,
        "achievements_unlocked": achievements_unlocked,
        "stories_triggered": stories_triggered,
    }


def _calculate_performance(player: Player) -> float:
    """Calculate performance rating based on health, GPA, burnout, time in job."""
    base = 50.0
    
    # GPA factor (3.5 GPA = +35 points)
    gpa_bonus = player.stats.gpa * PERFORMANCE_MODIFIERS["gpa_factor"]
    base += gpa_bonus
    
    # Health factor
    health_bonus = (player.health.health / 100.0) * PERFORMANCE_MODIFIERS["health_factor"] * 100
    base += health_bonus
    
    # Mental health factor
    mental_bonus = (player.health.mental_health / 100.0) * PERFORMANCE_MODIFIERS["mental_health_factor"] * 100
    base += mental_bonus
    
    # Time in job bonus (increases loyalty/expertise)
    time_bonus = min(20, player.career.semesters_at_current_job * PERFORMANCE_MODIFIERS["time_in_job_bonus"])
    base += time_bonus
    
    # Burnout penalty
    burnout_penalty = player.career.burnout_level * PERFORMANCE_MODIFIERS["burnout_penalty"] / 100
    base -= burnout_penalty
    
    return max(0, min(100, base))


def _check_career_achievements(player: Player) -> list[dict]:
    """Check all career achievements and unlock new ones."""
    unlocked = []
    
    # Check first promotion
    if player.career.promotions_earned == 1 and "first_promotion" not in [a.achievement_id for a in player.career.unlocked_achievements]:
        achievement = _unlock_achievement(player, "first_promotion")
        if achievement:
            unlocked.append(achievement)
    
    # Check five promotions
    if player.career.promotions_earned >= 5 and "five_promotions" not in [a.achievement_id for a in player.career.unlocked_achievements]:
        achievement = _unlock_achievement(player, "five_promotions")
        if achievement:
            unlocked.append(achievement)
    
    # Check $100k salary
    if player.career.current_salary >= 100000 and "hundred_k_salary" not in [a.achievement_id for a in player.career.unlocked_achievements]:
        achievement = _unlock_achievement(player, "hundred_k_salary")
        if achievement:
            unlocked.append(achievement)
    
    # Check leadership role
    if _has_leadership_role(player) and "leadership_role" not in [a.achievement_id for a in player.career.unlocked_achievements]:
        achievement = _unlock_achievement(player, "leadership_role")
        if achievement:
            unlocked.append(achievement)
    
    # Check perfect performance
    if player.career.performance_rating >= 95 and "perfect_performance" not in [a.achievement_id for a in player.career.unlocked_achievements]:
        achievement = _unlock_achievement(player, "perfect_performance")
        if achievement:
            unlocked.append(achievement)
    
    # Check avoid burnout
    if player.career.burnout_level < 30 and player.career.total_jobs_held > 0 and "avoid_burnout" not in [a.achievement_id for a in player.career.unlocked_achievements]:
        achievement = _unlock_achievement(player, "avoid_burnout")
        if achievement:
            unlocked.append(achievement)
    
    # Check comeback after burnout
    if player.career.burnout_level < 20 and player.career.semesters_at_current_job > 2 and "comeback_after_burnout" not in [a.achievement_id for a in player.career.unlocked_achievements]:
        achievement = _unlock_achievement(player, "comeback_after_burnout")
        if achievement:
            unlocked.append(achievement)
    
    return unlocked


def _unlock_achievement(player: Player, achievement_id: str) -> dict | None:
    """Unlock a career achievement."""
    if achievement_id not in CAREER_ACHIEVEMENTS:
        return None
    
    # Check if already unlocked
    if any(a.achievement_id == achievement_id for a in player.career.unlocked_achievements):
        return None
    
    achievement_def = CAREER_ACHIEVEMENTS[achievement_id]
    
    achievement = CareerAchievement(
        achievement_id=achievement_id,
        title=achievement_def["title"],
        milestone_type=achievement_def["milestone_type"],
        achieved_semester=player.semester,
        description=achievement_def["description"],
    )
    
    player.career.unlocked_achievements.append(achievement)
    
    return {
        "achievement_id": achievement_id,
        "title": achievement_def["title"],
        "description": achievement_def["description"],
        "tier": achievement_def.get("tier", "bronze"),
    }


def _has_leadership_role(player: Player) -> bool:
    """Check if player has a leadership role."""
    if not player.career.current_job_id:
        return False
    
    career_path = CAREER_PATHS.get(player.career.current_job_id)
    if career_path and career_path.get("leadership"):
        return True
    
    return False


def attempt_promotion(player: Player) -> dict:
    """
    Attempt to promote player based on:
    - Time in current role (min 2 semesters)
    - Performance rating (min 70)
    - GPA requirement
    - Eligible for promotion (next_promotion_eligible_semester <= current semester)
    """
    if not player.career.current_job_id:
        return {"success": False, "reason": "no_current_job"}
    
    if player.semester < player.career.next_promotion_eligible_semester:
        semesters_left = player.career.next_promotion_eligible_semester - player.semester
        return {
            "success": False,
            "reason": "not_eligible_yet",
            "semesters_until_eligible": semesters_left,
        }
    
    # Get career path for current job
    career_path = CAREER_PATHS.get(player.career.current_job_id)
    if not career_path or not career_path.get("promotion_to"):
        return {"success": False, "reason": "no_promotion_available"}
    
    requirements = career_path.get("promotion_requirements", {})
    
    # Check requirements
    if player.career.performance_rating < requirements.get("min_performance", 70):
        return {
            "success": False,
            "reason": "low_performance",
            "current": float(player.career.performance_rating),
            "required": requirements.get("min_performance", 70),
        }
    
    if player.stats.gpa < requirements.get("min_gpa", 3.0):
        return {
            "success": False,
            "reason": "low_gpa",
            "current": float(player.stats.gpa),
            "required": requirements.get("min_gpa", 3.0),
        }
    
    if player.career.semesters_at_current_job < requirements.get("semesters_in_role", 2):
        return {
            "success": False,
            "reason": "not_enough_time_in_role",
            "current": player.career.semesters_at_current_job,
            "required": requirements.get("semesters_in_role", 2),
        }
    
    # PROMOTION GRANTED
    old_job = player.career.current_job_id
    old_title = player.career.current_job_title
    old_salary = player.career.current_salary
    
    new_job_id = career_path["promotion_to"]
    new_career_path = CAREER_PATHS.get(new_job_id)
    new_salary = new_career_path["base_salary"] if new_career_path else old_salary * 1.25
    
    player.career.current_job_id = new_job_id
    player.career.current_job_title = new_career_path["title"] if new_career_path else "Promoted"
    player.career.current_salary = float(new_salary)
    player.career.promotions_earned += 1
    player.career.semesters_at_current_job = 0
    player.career.next_promotion_eligible_semester = player.semester + 3  # Next promotion in 3 semesters
    
    if not player.career.first_promotion_semester:
        player.career.first_promotion_semester = player.semester
    
    # Record history
    history_entry = CareerHistory(
        event_type="promotion",
        job_id=new_job_id,
        job_title=player.career.current_job_title,
        semester=player.semester,
        salary_before=old_salary,
        salary_after=float(new_salary),
        reason="promotion",
    )
    player.career.history.append(history_entry)
    
    # Trigger story
    _trigger_story(player, "promotion_earned")
    
    # Check achievements
    achievements = _check_career_achievements(player)
    
    return {
        "success": True,
        "old_title": old_title,
        "new_title": player.career.current_job_title,
        "old_salary": float(old_salary),
        "new_salary": float(player.career.current_salary),
        "raise_amount": float(new_salary - old_salary),
        "promotions_total": player.career.promotions_earned,
        "achievements_unlocked": achievements,
    }


def receive_raise(player: Player, amount: float) -> dict:
    """Apply a salary raise (from performance review, market adjustment, etc)."""
    old_salary = player.career.current_salary
    player.career.current_salary += amount
    player.career.total_raises += amount
    
    # Record history
    history_entry = CareerHistory(
        event_type="raise",
        job_id=player.career.current_job_id or "unknown",
        job_title=player.career.current_job_title or "Unknown",
        semester=player.semester,
        salary_before=old_salary,
        salary_after=player.career.current_salary,
        reason="performance_review",
    )
    player.career.history.append(history_entry)
    
    return {
        "old_salary": float(old_salary),
        "new_salary": float(player.career.current_salary),
        "raise_amount": float(amount),
        "cumulative_raises": float(player.career.total_raises),
    }


def apply_therapy_burnout_reduction(player: Player, therapy_effectiveness: float = 1.0) -> dict:
    """Therapy session reduces burnout."""
    reduction = BURNOUT_MECHANICS["burnout_cooldown_per_therapy"] * therapy_effectiveness
    old_burnout = player.career.burnout_level
    player.career.burnout_level = max(0, player.career.burnout_level - reduction)
    
    return {
        "old_burnout": float(old_burnout),
        "new_burnout": float(player.career.burnout_level),
        "reduction": float(reduction),
    }


def _trigger_story(player: Player, story_id: str) -> dict | None:
    """Trigger a career story if conditions are met."""
    if story_id not in CAREER_STORIES:
        return None
    
    # Don't show same story twice
    if story_id in player.career.stories_shown:
        return None
    
    story_def = CAREER_STORIES[story_id]
    player.career.stories_shown.append(story_id)
    
    return {
        "story_id": story_id,
        "title": story_def["title"],
        "message": story_def["message"],
        "tone": story_def["tone"],
    }


def get_career_summary(player: Player) -> dict:
    """Get complete career summary for dashboard."""
    if not hasattr(player, 'career'):
        player.career = Career()
    
    return {
        "current_job": {
            "job_id": player.career.current_job_id,
            "title": player.career.current_job_title,
            "salary": float(player.career.current_salary),
            "semesters_in_role": player.career.semesters_at_current_job,
        },
        "performance": {
            "rating": float(player.career.performance_rating),
            "rating_tier": _performance_tier(player.career.performance_rating),
        },
        "burnout": {
            "level": float(player.career.burnout_level),
            "status": _burnout_status(player.career.burnout_level),
            "alert": player.career.burnout_level > 60,
        },
        "career_stats": {
            "total_jobs": player.career.total_jobs_held,
            "promotions": player.career.promotions_earned,
            "total_raises": float(player.career.total_raises),
            "highest_salary": float(player.career.highest_salary_achieved),
        },
        "achievements": [
            {
                "id": a.achievement_id,
                "title": a.title,
                "earned_semester": a.achieved_semester,
            }
            for a in player.career.unlocked_achievements
        ],
        "next_promotion_eligible": player.career.next_promotion_eligible_semester,
    }


def _performance_tier(rating: float) -> str:
    """Convert performance rating to tier."""
    if rating >= 90:
        return "Exceptional"
    elif rating >= 75:
        return "Strong"
    elif rating >= 60:
        return "Solid"
    elif rating >= 45:
        return "Average"
    else:
        return "Needs Improvement"


def _burnout_status(level: float) -> str:
    """Convert burnout level to status."""
    if level < 25:
        return "Thriving"
    elif level < 50:
        return "Healthy"
    elif level < 75:
        return "Stressed"
    elif level < 90:
        return "Burning Out"
    else:
        return "CRITICAL"
