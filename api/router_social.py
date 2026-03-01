"""
API Router: Social Features

Endpoints for friends, challenges, tournaments, and achievements.
"""

from __future__ import annotations
from typing import List, Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from core_domain.store import STORE
from social.leaderboard_service import leaderboard_service, LeaderboardEntry
from social.friends import friend_service, FriendRelationship, Challenge, ChallengeStatus
from social.tournament_scheduler import tournament_service, Tournament, TournamentStanding
from social.social_sharing import achievement_service, Badge, ShareableAchievement

router = APIRouter(prefix="/api/social", tags=["social"])


# =========================
# Request/Response Models
# =========================

class FriendRequestDto(BaseModel):
    target_player_id: str = Field(description="ID of player to befriend")


class FriendResponseDto(BaseModel):
    player_id: str
    friend_id: str
    status: str
    created_at: str


class ChallengeRequestDto(BaseModel):
    opponent_id: str = Field(description="ID of opponent")
    game_type: str = Field(description="Game type (e.g., 'exam_micro', 'tutorial')")


class ChallengeResponseDto(BaseModel):
    id: str
    challenger_id: str
    opponent_id: str
    game_type: str
    status: str
    challenger_score: Optional[float]
    opponent_score: Optional[float]


class ChallengeResultDto(BaseModel):
    challenge_id: str
    score: float = Field(ge=0, le=100, description="Score 0-100")


class TournamentRegisterDto(BaseModel):
    tournament_id: str = Field(description="Tournament ID to join")


class TournamentCreateDto(BaseModel):
    name: str = Field(min_length=1)
    tournament_type: str  # "weekly" or "monthly"
    game_type: str
    max_participants: int = 32


# =========================
# Leaderboard Endpoints
# =========================

@router.get("/leaderboard/global")
def get_global_leaderboard(
    period: str = "alltime",  # weekly, monthly, alltime
    limit: int = 50,
):
    """Get global player leaderboard."""
    leaderboard = leaderboard_service.get_leaderboard(
        leaderboard_type="global",
        period=period,
        limit=limit,
    )
    return {
        "leaderboard_type": "global",
        "period": period,
        "entries": [e.model_dump() for e in leaderboard.entries],
        "total_players": leaderboard.total_players,
    }


@router.get("/leaderboard/college/{college_id}")
def get_college_leaderboard(
    college_id: str,
    period: str = "alltime",
    limit: int = 50,
):
    """Get leaderboard for specific college."""
    leaderboard = leaderboard_service.get_leaderboard(
        leaderboard_type="college",
        filter_value=college_id,
        period=period,
        limit=limit,
    )
    return {
        "leaderboard_type": "college",
        "college_id": college_id,
        "period": period,
        "entries": [e.model_dump() for e in leaderboard.entries],
        "total_players": leaderboard.total_players,
    }


@router.get("/leaderboard/major/{major_id}")
def get_major_leaderboard(
    major_id: str,
    period: str = "alltime",
    limit: int = 50,
):
    """Get leaderboard for specific major."""
    leaderboard = leaderboard_service.get_leaderboard(
        leaderboard_type="major",
        filter_value=major_id,
        period=period,
        limit=limit,
    )
    return {
        "leaderboard_type": "major",
        "major_id": major_id,
        "period": period,
        "entries": [e.model_dump() for e in leaderboard.entries],
        "total_players": leaderboard.total_players,
    }


@router.get("/leaderboard/{player_id}/rank")
def get_player_rank(player_id: str):
    """Get player's rank in global leaderboard."""
    rank_info = leaderboard_service.get_player_rank(
        player_id=player_id,
        leaderboard_type="global",
    )
    
    if not rank_info:
        raise HTTPException(status_code=404, detail="Player not ranked yet")
    
    return {
        "player_id": player_id,
        "global_rank": rank_info.get("rank"),
        "global_score": rank_info.get("score"),
        "wins": rank_info.get("wins"),
    }


@router.get("/leaderboard/{player_id}/stats")
def get_player_stats(player_id: str):
    """Get player's leaderboard stats."""
    stats = leaderboard_service.get_player_stats(player_id)
    
    if not stats:
        raise HTTPException(status_code=404, detail="Player stats not found")
    
    return stats.model_dump()


# =========================
# Friend Endpoints
# =========================

@router.post("/friends/request")
def send_friend_request(player_id: str, request: FriendRequestDto):
    """Send friend request to another player."""
    try:
        friendship = friend_service.send_friend_request(
            player_id=player_id,
            target_id=request.target_player_id,
        )
        return friendship.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/friends/accept")
def accept_friend_request(player_id: str, requester_id: str):
    """Accept friend request."""
    try:
        friendship = friend_service.accept_friend_request(
            player_id=player_id,
            requester_id=requester_id,
        )
        return friendship.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/friends/decline")
def decline_friend_request(player_id: str, requester_id: str):
    """Decline friend request."""
    try:
        friend_service.decline_friend_request(
            player_id=player_id,
            requester_id=requester_id,
        )
        return {"status": "declined"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/friends/block")
def block_player(player_id: str, target_id: str):
    """Block a player."""
    try:
        friendship = friend_service.block_player(
            player_id=player_id,
            target_id=target_id,
        )
        return friendship.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/friends/{player_id}")
def get_friends(player_id: str):
    """Get list of player's friends."""
    friends = friend_service.get_friends(player_id)
    return {"player_id": player_id, "friends": friends}


# =========================
# Challenge Endpoints
# =========================

@router.post("/challenges/create")
def create_challenge(player_id: str, request: ChallengeRequestDto):
    """Create a 1v1 challenge."""
    try:
        challenge = friend_service.create_challenge(
            challenger_id=player_id,
            opponent_id=request.opponent_id,
            game_type=request.game_type,
        )
        return challenge.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/challenges/{challenge_id}/accept")
def accept_challenge(player_id: str, challenge_id: str):
    """Accept a challenge."""
    try:
        challenge = friend_service.accept_challenge(
            challenge_id=challenge_id,
            player_id=player_id,
        )
        return challenge.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/challenges/{challenge_id}/decline")
def decline_challenge(player_id: str, challenge_id: str):
    """Decline a challenge."""
    try:
        challenge = friend_service.decline_challenge(
            challenge_id=challenge_id,
            player_id=player_id,
        )
        return challenge.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/challenges/{challenge_id}/submit-result")
def submit_challenge_result(player_id: str, challenge_id: str, request: ChallengeResultDto):
    """Submit game result for challenge."""
    try:
        challenge = friend_service.submit_challenge_result(
            challenge_id=challenge_id,
            player_id=player_id,
            score=request.score,
        )
        return challenge.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/challenges/{player_id}")
def get_player_challenges(player_id: str, status: Optional[str] = None):
    """Get challenges for player."""
    challenges = friend_service.get_player_challenges(
        player_id=player_id,
        status=ChallengeStatus(status) if status else None,
    )
    return {
        "player_id": player_id,
        "challenges": [c.model_dump() for c in challenges],
    }


@router.get("/challenges/{player_id}/pending")
def get_pending_challenges(player_id: str):
    """Get pending challenges awaiting this player's response."""
    challenges = friend_service.get_pending_challenges(player_id)
    return {
        "player_id": player_id,
        "pending_challenges": [c.model_dump() for c in challenges],
    }


# =========================
# Tournament Endpoints
# =========================

@router.post("/tournaments/create")
def create_tournament(request: TournamentCreateDto):
    """Create a new tournament."""
    try:
        tournament = tournament_service.create_tournament(
            name=request.name,
            tournament_type=request.tournament_type,
            game_type=request.game_type,
            max_participants=request.max_participants,
        )
        return tournament.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/tournaments/{tournament_id}/register")
def register_tournament(player_id: str, tournament_id: str):
    """Register player for tournament."""
    try:
        # Get player for name and skill rating
        player = STORE.require_player(player_id)
        
        tournament = tournament_service.register_player(
            tournament_id=tournament_id,
            player_id=player_id,
            player_name=player.name,
            skill_rating=float(player.stats.skill_rating) if hasattr(player.stats, 'skill_rating') else 1200.0,
        )
        return tournament.model_dump()
    except (ValueError, KeyError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/tournaments/{tournament_id}/finalize-bracket")
def finalize_tournament_bracket(tournament_id: str):
    """Generate tournament bracket and matches."""
    try:
        tournament, matches = tournament_service.finalize_bracket(tournament_id)
        return {
            "tournament": tournament.model_dump(),
            "matches": [m.model_dump() for m in matches],
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/tournaments/{tournament_id}/matches/{match_id}/result")
def submit_tournament_match_result(tournament_id: str, match_id: str, winner_id: str, player1_score: float, player2_score: float):
    """Submit tournament match result."""
    try:
        match = tournament_service.submit_match_result(
            tournament_id=tournament_id,
            match_id=match_id,
            winner_id=winner_id,
            player1_score=player1_score,
            player2_score=player2_score,
        )
        return match.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/tournaments/{tournament_id}/standings")
def get_tournament_standings(tournament_id: str):
    """Get tournament standings."""
    try:
        standings = tournament_service.get_tournament_standings(tournament_id)
        return {
            "tournament_id": tournament_id,
            "standings": [s.model_dump() for s in standings],
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/tournaments/active")
def get_active_tournaments():
    """Get all active tournaments."""
    tournaments = tournament_service.get_active_tournaments()
    return {
        "total_tournaments": len(tournaments),
        "tournaments": [t.model_dump() for t in tournaments],
    }


@router.get("/tournaments/{player_id}/history")
def get_player_tournament_history(player_id: str):
    """Get player's tournament participation history."""
    tournaments = tournament_service.get_player_tournament_history(player_id)
    return {
        "player_id": player_id,
        "tournaments": [t.model_dump() for t in tournaments],
    }


# =========================
# Achievement Endpoints
# =========================

@router.get("/achievements/{player_id}")
def get_player_achievements(player_id: str):
    """Get player's unlocked achievements."""
    achievements = achievement_service.get_player_achievements(player_id)
    return {
        "player_id": player_id,
        "total_unlocked": len(achievements),
        "achievements": [
            {
                "id": a.id,
                "name": a.name,
                "description": a.description,
                "icon": a.icon_url,
                "points": a.points,
                "rarity": a.rarity.value,
            }
            for a in achievements
        ],
    }


@router.get("/achievements/{player_id}/progress")
def get_achievement_progress(player_id: str):
    """Get progress towards locked achievements."""
    progress = achievement_service.get_achievement_progress(player_id)
    return {
        "player_id": player_id,
        "progress": progress,
    }


@router.get("/badges/{player_id}")
def get_player_badges(player_id: str):
    """Get player's visual badges."""
    badges = achievement_service.get_unlocked_badges(player_id)
    return {
        "player_id": player_id,
        "total_badges": len(badges),
        "badges": [b.model_dump() for b in badges],
    }


@router.get("/achievements/{player_id}/{achievement_id}/share")
def get_shareable_achievement(player_id: str, achievement_id: str):
    """Get shareable version of achievement."""
    try:
        player = STORE.require_player(player_id)
        
        shareable = achievement_service.create_shareable_achievement(
            player_id=player_id,
            achievement_id=achievement_id,
            player_name=player.name,
        )
        
        return {
            "achievement": shareable.model_dump(),
            "share_links": {
                "twitter": shareable.twitter_text,
                "facebook": shareable.facebook_text,
                "linkedin": shareable.linked_in_text,
            },
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/achievements/{player_id}/check")
def check_achievements(player_id: str):
    """Check for newly unlocked achievements."""
    try:
        player = STORE.require_player(player_id)
        
        # Compile player stats for achievement checking
        player_stats = {
            "exams_passed": player.stats.exams_passed if hasattr(player.stats, 'exams_passed') else 0,
            "gpa_threshold": float(player.stats.gpa) if hasattr(player.stats, 'gpa') else 0.0,
            "graduation_debt": 0.0,  # would come from finance module
            "friends_count": len(friend_service.get_friends(player_id)),
        }
        
        unlocked = achievement_service.check_and_unlock_achievements(
            player_id=player_id,
            player_stats=player_stats,
        )
        
        return {
            "player_id": player_id,
            "newly_unlocked": unlocked,
            "count": len(unlocked),
        }
    except KeyError:
        raise HTTPException(status_code=404, detail="Player not found")
