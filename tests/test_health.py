"""
Comprehensive tests for Health System
Tests achievements, streaks, stories, and all health operations.
"""
import pytest
from core_domain.player.player_model import Player, Housing
from core_domain.stats.stats_model import Stats
from core_domain.finance.finance_models import Finance
from core_domain.health.health_models import Health
from health.service import (
    initialize_player_health,
    exercise_session,
    attend_therapy,
    schedule_checkup,
    apply_health_condition,
    check_achievements,
    get_achievement_progress,
    get_health_history,
    get_health_summary,
    update_exercise_streak,
    perform_batch_health_actions,
    progress_health_semester,
)


@pytest.fixture
def test_player():
    """Create a fresh player for testing"""
    player = Player(
        id="test_health_player",
        player_id="test_health_player",
        name="Test Player",
        age=18,
        hs_gpa=3.5,
        parent_income=75000.0,
        major_id="computer_science",
        college_id="rutgers",
        housing=Housing(
            option_id="parents_house",
            name="Parents' House",
            monthly_cost=0.0,
        ),
        semester=1,
        stats=Stats(),
        finance=Finance(balance=10000.0),
    )
    player.health = initialize_player_health(player)
    return player


# =========================
# Exercise Tests
# =========================

def test_exercise_session_basic(test_player):
    """Test basic exercise session"""
    initial_fitness = test_player.health.fitness
    initial_stress = test_player.stats.stress
    
    result = exercise_session(test_player, "running")
    
    assert result["exercise_type"] == "running"
    assert test_player.health.fitness > initial_fitness
    assert test_player.stats.stress < initial_stress
    assert test_player.health.total_exercises_all_time == 1
    assert test_player.health.exercises_this_semester == 1
    assert result["cost"] == 0.0  # Running is free


def test_exercise_streak(test_player):
    """Test exercise streak tracking"""
    # First exercise starts streak
    result1 = exercise_session(test_player, "running")
    assert test_player.health.current_exercise_streak == 1
    assert test_player.health.best_exercise_streak == 1
    assert result1["exercise_streak"]["current_streak"] == 1
    
    # Second exercise continues streak
    result2 = exercise_session(test_player, "running")
    assert test_player.health.current_exercise_streak == 2
    assert test_player.health.best_exercise_streak == 2
    
    # Third exercise continues streak
    result3 = exercise_session(test_player, "running")
    assert test_player.health.current_exercise_streak == 3
    assert test_player.health.best_exercise_streak == 3


def test_exercise_streak_power(test_player):
    """Test that streak increases fitness gains"""
    # Do one exercise and record gain
    result1 = exercise_session(test_player, "running")
    first_gain = result1["fitness_gain"]
    
    # Do 4 more exercises to build streak
    for _ in range(4):
        exercise_session(test_player, "running")
    
    # Sixth exercise should have higher gain due to streak
    initial_fitness = test_player.health.fitness
    result6 = exercise_session(test_player, "running")
    
    assert test_player.health.current_exercise_streak == 6
    assert result6["fitness_gain"] > first_gain  # Streak power increases gains


def test_gym_membership_cost(test_player):
    """Test that gym membership costs money"""
    initial_balance = test_player.finance.balance
    
    result = exercise_session(test_player, "gym_membership")
    
    assert result["cost"] > 0.0
    assert test_player.finance.balance < initial_balance


def test_yoga_mental_health_bonus(test_player):
    """Test that yoga improves mental health"""
    initial_mental = test_player.health.mental_health
    
    exercise_session(test_player, "yoga")
    
    assert test_player.health.mental_health > initial_mental


# =========================
# Achievement Tests
# =========================

def test_first_workout_achievement(test_player):
    """Test unlocking 'First Workout' achievement"""
    result = exercise_session(test_player, "running")
    
    achievements = result["achievements_unlocked"]
    assert len(achievements) > 0
    assert any(a["id"] == "first_workout" for a in achievements)
    assert len(test_player.health.unlocked_achievements) > 0


def test_5k_runner_achievement(test_player):
    """Test unlocking '5K Runner' achievement (5 exercises)"""
    # Do 5 exercises
    for _ in range(5):
        exercise_session(test_player, "running")
    
    unlocked_ids = [a.achievement_id for a in test_player.health.unlocked_achievements]
    assert "5k_runner" in unlocked_ids


def test_on_fire_achievement(test_player):
    """Test unlocking 'On Fire' achievement (3 day streak)"""
    # Do 3 exercises to build streak
    for _ in range(3):
        exercise_session(test_player, "running")
    
    unlocked_ids = [a.achievement_id for a in test_player.health.unlocked_achievements]
    assert "on_fire" in unlocked_ids


def test_achievement_rewards_applied(test_player):
    """Test that achievement rewards are applied"""
    initial_multiplier = test_player.health.fitness_multiplier
    
    # Unlock first workout (gives fitness multiplier bonus)
    exercise_session(test_player, "running")
    
    # Multiplier should have increased
    assert test_player.health.fitness_multiplier > initial_multiplier


def test_achievement_progress(test_player):
    """Test achievement progress tracking"""
    # Do 2 exercises
    exercise_session(test_player, "running")
    exercise_session(test_player, "running")
    
    progress = get_achievement_progress(test_player)
    
    assert progress["total_achievements"] == 11
    assert progress["unlocked_count"] >= 1  # At least first_workout
    assert len(progress["in_progress"]) > 0  # Should have some in progress
    
    # Check that progress shows correctly
    for achievement in progress["in_progress"]:
        assert "progress" in achievement
        assert "percentage" in achievement


# =========================
# Therapy Tests
# =========================

def test_therapy_session(test_player):
    """Test basic therapy session"""
    # Set high stress
    test_player.stats.stress = 80.0
    initial_mental = test_player.health.mental_health
    
    result = attend_therapy(test_player, "campus_counseling")
    
    assert result["therapy_type"] == "campus_counseling"
    assert test_player.stats.stress < 80.0
    assert test_player.health.mental_health > initial_mental
    assert test_player.health.total_therapy_sessions_all_time == 1
    assert result["cost"] == 0.0  # Campus counseling is free


def test_therapy_achievement(test_player):
    """Test unlocking therapy achievement"""
    # Do 5 therapy sessions
    for _ in range(5):
        test_player.stats.stress = 60.0  # Reset stress
        attend_therapy(test_player, "campus_counseling")
    
    unlocked_ids = [a.achievement_id for a in test_player.health.unlocked_achievements]
    assert "mental_health_advocate" in unlocked_ids


def test_paid_therapy(test_player):
    """Test that paid therapy costs money but is more effective"""
    initial_balance = test_player.finance.balance
    test_player.stats.stress = 80.0
    
    result = attend_therapy(test_player, "therapist")
    
    assert result["cost"] > 0.0
    assert test_player.finance.balance < initial_balance
    assert result["mental_health_gain"] > 8.0  # Better than free counseling


# =========================
# Checkup Tests
# =========================

def test_annual_checkup(test_player):
    """Test annual checkup"""
    initial_health = test_player.health.health
    initial_balance = test_player.finance.balance
    
    result = schedule_checkup(test_player, "annual_checkup")
    
    assert result["checkup_type"] == "annual_checkup"
    assert test_player.health.health > initial_health
    assert result["cost"] > 0.0
    assert test_player.finance.balance < initial_balance
    assert test_player.health.total_checkups_all_time == 1


def test_insurance_cost_reduction(test_player):
    """Test that insurance reduces checkup costs"""
    test_player.health.medical_insurance = True
    
    result = schedule_checkup(test_player, "annual_checkup")
    
    assert result["cost"] < result["cost_before_insurance"]
    assert result["insurance_savings"] > 0.0


def test_checkup_achievement(test_player):
    """Test unlocking checkup achievement"""
    # Do 3 checkups
    schedule_checkup(test_player, "annual_checkup")
    schedule_checkup(test_player, "teeth_cleaning")
    schedule_checkup(test_player, "eye_exam")
    
    unlocked_ids = [a.achievement_id for a in test_player.health.unlocked_achievements]
    assert "preventive_pro" in unlocked_ids


# =========================
# Combined Achievement Tests
# =========================

def test_health_wisdom_combined_achievement(test_player):
    """Test unlocking 'Health Wisdom' platinum achievement (combined actions)"""
    # Do 10+ exercises
    for _ in range(10):
        exercise_session(test_player, "running")
    
    # Do 5+ therapy sessions
    for _ in range(5):
        test_player.stats.stress = 60.0
        attend_therapy(test_player, "campus_counseling")
    
    # Do 2+ checkups
    schedule_checkup(test_player, "annual_checkup")
    schedule_checkup(test_player, "teeth_cleaning")
    
    unlocked_ids = [a.achievement_id for a in test_player.health.unlocked_achievements]
    assert "health_wisdom" in unlocked_ids
    
    # Check that it's platinum tier
    health_wisdom = next(a for a in test_player.health.unlocked_achievements if a.achievement_id == "health_wisdom")
    assert health_wisdom.tier == "platinum"


# =========================
# Health Condition Tests
# =========================

def test_apply_health_condition(test_player):
    """Test applying health condition"""
    initial_health = test_player.health.health
    
    result = apply_health_condition(test_player, "cold")
    
    assert result["condition_id"] == "cold"
    assert result["severity"] == "mild"
    assert test_player.health.health < initial_health
    assert len(test_player.health.current_conditions) == 1


def test_severe_condition_cost(test_player):
    """Test that severe conditions are expensive"""
    initial_balance = test_player.finance.balance
    
    result = apply_health_condition(test_player, "broken_arm")
    
    assert result["severity"] == "severe"
    assert result["medical_cost"] > 1000.0
    assert test_player.finance.balance < initial_balance - 1000.0


# =========================
# Health History Tests
# =========================

def test_health_history_tracking(test_player):
    """Test that health history is tracked"""
    exercise_session(test_player, "running")
    attend_therapy(test_player, "campus_counseling")
    schedule_checkup(test_player, "annual_checkup")
    
    history = get_health_history(test_player, limit=10)
    
    assert len(history["recent_events"]) == 3
    assert history["total_events"] == 3
    assert "exercise" in history["event_counts"]
    assert "therapy" in history["event_counts"]
    assert "checkup" in history["event_counts"]


# =========================
# Batch Actions Tests
# =========================

def test_batch_health_actions(test_player):
    """Test performing multiple actions in one request"""
    actions = [
        {"type": "exercise", "exercise_type": "running"},
        {"type": "therapy", "therapy_type": "campus_counseling"},
        {"type": "checkup", "checkup_type": "teeth_cleaning"},
    ]
    
    result = perform_batch_health_actions(test_player, actions)
    
    assert result["actions_performed"] == 3
    assert result["actions_failed"] == 0
    assert len(result["results"]) == 3
    assert result["total_cost"] > 0.0  # Teeth cleaning costs money
    assert test_player.health.total_exercises_all_time == 1
    assert test_player.health.total_therapy_sessions_all_time == 1
    assert test_player.health.total_checkups_all_time == 1


def test_batch_actions_with_failure(test_player):
    """Test batch actions with invalid action"""
    actions = [
        {"type": "exercise", "exercise_type": "running"},
        {"type": "invalid_action"},  # This should fail
        {"type": "therapy", "therapy_type": "campus_counseling"},
    ]
    
    result = perform_batch_health_actions(test_player, actions)
    
    assert result["actions_performed"] == 2
    assert result["actions_failed"] == 1


# =========================
# Semester Progression Tests
# =========================

def test_semester_progression_health_decay(test_player):
    """Test that health decays if no exercise"""
    initial_health = test_player.health.health
    
    # Don't exercise this semester
    changes = progress_health_semester(test_player)
    
    assert "health_decay" in changes
    assert test_player.health.health < initial_health


def test_semester_progression_maintains_streak(test_player):
    """Test that exercising maintains streak across semester"""
    # Exercise this semester
    exercise_session(test_player, "running")
    current_streak = test_player.health.current_exercise_streak
    
    # Progress semester
    progress_health_semester(test_player)
    
    # Streak should be maintained
    assert test_player.health.current_exercise_streak == current_streak


def test_semester_progression_breaks_streak(test_player):
    """Test that no exercise breaks streak"""
    # Build a streak
    exercise_session(test_player, "running")
    exercise_session(test_player, "running")
    assert test_player.health.current_exercise_streak == 2
    
    # Don't exercise this semester, then progress
    test_player.health.exercises_this_semester = 0
    progress_health_semester(test_player)
    
    # Streak should be broken
    assert test_player.health.current_exercise_streak == 0


# =========================
# Health Summary Tests
# =========================

def test_health_summary(test_player):
    """Test health summary generation"""
    exercise_session(test_player, "running")
    attend_therapy(test_player, "campus_counseling")
    
    summary = get_health_summary(test_player)
    
    assert "overall_status" in summary
    assert summary["overall_status"] in ["Excellent", "Good", "Fair", "Poor"]
    assert "health" in summary
    assert "fitness" in summary
    assert "mental_health" in summary
    assert summary["total_exercises_all_time"] == 1
    assert summary["total_therapy_sessions_all_time"] == 1
    assert summary["achievements_unlocked"] > 0


# =========================
# Integration Tests
# =========================

def test_full_health_journey(test_player):
    """Test a full health journey with multiple actions"""
    # Week 1: Start exercising
    for _ in range(3):
        exercise_session(test_player, "running")
    
    # Week 2: Add therapy
    test_player.stats.stress = 70.0
    for _ in range(2):
        attend_therapy(test_player, "campus_counseling")
    
    # Week 3: Get checkup
    schedule_checkup(test_player, "annual_checkup")
    
    # Week 4: Continue routine
    for _ in range(4):
        exercise_session(test_player, "yoga")
    
    # Check overall progress
    summary = get_health_summary(test_player)
    progress = get_achievement_progress(test_player)
    history = get_health_history(test_player)
    
    # Should have good health stats
    assert summary["overall_status"] in ["Excellent", "Good"]
    assert summary["current_exercise_streak"] > 0
    assert summary["total_exercises_all_time"] == 7
    
    # Should have unlocked multiple achievements
    assert progress["unlocked_count"] >= 2
    
    # Should have comprehensive history
    assert history["total_events"] == 10


def test_achievement_multiplier_stacking(test_player):
    """Test that multiple achievements stack multipliers"""
    initial_multiplier = test_player.health.fitness_multiplier
    
    # Unlock multiple achievements by exercising
    for _ in range(10):
        exercise_session(test_player, "running")
    
    # Multiplier should have increased from multiple achievements
    assert test_player.health.fitness_multiplier > initial_multiplier
    
    # Higher multipliers should lead to bigger gains
    result = exercise_session(test_player, "running")
    assert result["fitness_gain"] > 4.0  # Base is 4, should be boosted


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
