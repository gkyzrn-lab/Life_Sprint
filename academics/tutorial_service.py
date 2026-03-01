"""
Tutorial Quest Service

Manages player progression through the tutorial quest chain.
"""

from __future__ import annotations
from time import time
from typing import Dict, Any, List

from fastapi import HTTPException

from core_domain.player.player_model import Player, HistoryEvent
from core_domain.quests.quest_models import QuestProgress
from academics.tutorial_games import (
    get_tutorial_game,
    get_new_player_quest,
    calculate_quest_progress,
    get_mascot_dialogue,
    TutorialGame,
)


def start_tutorial_quest(player: Player) -> Dict[str, Any]:
    """
    Initialize the new player tutorial quest.
    Returns quest details and first step.
    """
    if player.quest_state.tutorial_complete:
        raise HTTPException(status_code=400, detail="Tutorial already completed")
    
    quest = get_new_player_quest()
    
    # Check if already started
    existing = next(
        (q for q in player.quest_state.active_quests if q.quest_id == quest.id),
        None
    )
    
    if existing:
        # Already started, return current progress
        return calculate_quest_progress(existing.completed_steps)
    
    # Start new quest
    quest_progress = QuestProgress(
        quest_id=quest.id,
        completed_steps=[],
        current_step_id=quest.steps[0].id,
        started_at=time(),
        completed_at=None,
        total_points_earned=0,
    )
    
    player.quest_state.active_quests.append(quest_progress)
    
    player.history.append(
        HistoryEvent(
            label=f"Tutorial Quest Started: {quest.id}",
            semester=player.semester,
            details={"step_index": 0.0},
        )
    )
    
    return {
        "quest": quest.model_dump(),
        "progress": calculate_quest_progress([]),
        "mascot_dialogue": get_mascot_dialogue("tutorial_start"),
        "first_game": get_tutorial_game(quest.steps[0].game_id).model_dump(),
    }


def submit_tutorial_game(
    player: Player,
    game_id: str,
    answers: List[Dict[str, str]],
) -> Dict[str, Any]:
    """
    Grade a tutorial game submission and advance quest if passed.
    
    Returns:
    - score_percent
    - passed (bool)
    - feedback per question
    - quest_progress
    - mascot_dialogue
    - next_step (if available)
    """
    game = get_tutorial_game(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Tutorial game not found")
    
    quest = get_new_player_quest()
    quest_progress = next(
        (q for q in player.quest_state.active_quests if q.quest_id == quest.id),
        None
    )
    
    if not quest_progress:
        raise HTTPException(status_code=400, detail="Tutorial quest not started")
    
    # Find the quest step for this game
    quest_step = next(
        (step for step in quest.steps if step.game_id == game_id),
        None
    )
    
    if not quest_step:
        raise HTTPException(status_code=400, detail="Game not part of tutorial quest")
    
    # Grade the game
    correct_count = 0
    total_questions = len(game.questions)
    feedback = []
    
    answer_map = {a["question_id"]: a["choice_id"] for a in answers}
    
    for question in game.questions:
        chosen_id = answer_map.get(question.id)
        chosen_choice = next(
            (c for c in question.choices if c["id"] == chosen_id),
            None
        )
        
        is_correct = chosen_choice and chosen_choice.get("correct", False)
        if is_correct:
            correct_count += 1
        
        feedback.append({
            "question_id": question.id,
            "question_text": question.text,
            "your_answer": chosen_choice["text"] if chosen_choice else "No answer",
            "is_correct": is_correct,
            "explanation": chosen_choice["explanation"] if chosen_choice else "Invalid choice",
        })
    
    score_percent = (correct_count / total_questions * 100) if total_questions > 0 else 0
    passed = score_percent >= quest_step.required_score
    
    # Determine mascot dialogue
    if correct_count == 0:
        mascot_msg = get_mascot_dialogue("struggling_multiple_wrong")
    elif correct_count == total_questions:
        mascot_msg = get_mascot_dialogue("first_correct_answer")
    elif passed:
        mascot_msg = get_mascot_dialogue("quest_step_complete")
    else:
        mascot_msg = get_mascot_dialogue("first_wrong_answer")
    
    result = {
        "game_id": game_id,
        "score_percent": score_percent,
        "correct_count": correct_count,
        "total_questions": total_questions,
        "passed": passed,
        "required_score": quest_step.required_score,
        "feedback": feedback,
        "mascot_dialogue": mascot_msg,
        "points_earned": 0,
        "next_step": None,
        "quest_complete": False,
    }
    
    if not passed:
        # Even on fail, update rating (negative feedback)
        # Import here to avoid circular imports at module load time
        from academics.adaptive_difficulty_service import update_player_rating_after_game
        from core_domain.player.skill_ratings import DifficultyTier
        
        update_player_rating_after_game(
            player,
            game_id,
            score_percent,
            passed,
            DifficultyTier.medium  # tutorial games start at medium
        )
        return result
    
    # Passed! Advance quest and update rating
    from academics.adaptive_difficulty_service import update_player_rating_after_game
    from core_domain.player.skill_ratings import DifficultyTier
    
    update_player_rating_after_game(
        player,
        game_id,
        score_percent,
        passed,
        DifficultyTier.medium  # tutorial games start at medium
    )
    
    if quest_step.id not in quest_progress.completed_steps:
        quest_progress.completed_steps.append(quest_step.id)
        
        # Award points
        points = quest_step.rewards.get("points", 0)
        player.game_points += points
        quest_progress.total_points_earned += points
        result["points_earned"] = points
        
        # Award badge if this step gives one
        badge_id = quest_step.rewards.get("badge")
        if badge_id and badge_id not in player.earned_badges:
            player.earned_badges.append(badge_id)
        
        # Find next step
        next_step_id = quest_step.next_step_id
        if next_step_id:
            quest_progress.current_step_id = next_step_id
            next_step = next(
                (s for s in quest.steps if s.id == next_step_id),
                None
            )
            if next_step:
                next_game = get_tutorial_game(next_step.game_id)
                result["next_step"] = {
                    "step": next_step.model_dump(),
                    "game": next_game.model_dump() if next_game else None,
                }
        else:
            # Quest complete!
            quest_progress.completed_at = time()
            quest_progress.current_step_id = None
            
            player.quest_state.completed_quests.append(quest.id)
            player.quest_state.tutorial_complete = True
            
            if quest_progress.started_at:
                duration = time() - quest_progress.started_at
                player.quest_state.tutorial_completion_time_seconds = duration
            
            result["quest_complete"] = True
            result["mascot_dialogue"] = get_mascot_dialogue("quest_chain_complete")
            
            player.history.append(
                HistoryEvent(
                    label="Tutorial Quest Complete! 🎊",
                    semester=player.semester,
                    details={
                        "total_points": float(quest_progress.total_points_earned),
                        "completion_time_seconds": player.quest_state.tutorial_completion_time_seconds or 0.0,
                    },
                )
            )
    
    return result


def get_quest_progress(player: Player, quest_id: str) -> Dict[str, Any]:
    """Get current progress for a specific quest"""
    quest_progress = next(
        (q for q in player.quest_state.active_quests if q.quest_id == quest_id),
        None
    )
    
    if not quest_progress:
        if quest_id in player.quest_state.completed_quests:
            return {
                "status": "completed",
                "quest_id": quest_id,
                "message": "Quest already completed",
            }
        return {
            "status": "not_started",
            "quest_id": quest_id,
            "message": "Quest not started",
        }
    
    progress = calculate_quest_progress(quest_progress.completed_steps)
    progress["started_at"] = quest_progress.started_at
    progress["total_points_earned"] = quest_progress.total_points_earned
    
    return progress


def skip_tutorial(player: Player) -> Player:
    """Allow player to skip tutorial (for returning users or testing)"""
    quest = get_new_player_quest()
    
    if player.quest_state.tutorial_complete:
        return player
    
    # Mark tutorial as complete without playing
    player.quest_state.tutorial_complete = True
    player.quest_state.completed_quests.append(quest.id)
    
    player.history.append(
        HistoryEvent(
            label="Tutorial Skipped",
            semester=player.semester,
            details={},
        )
    )
    
    return player
