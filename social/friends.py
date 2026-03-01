"""
Friend System & Challenges

Manages friend relationships and 1v1 game challenges between players.
"""

from __future__ import annotations
from typing import List, Dict, Optional, Literal
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
from uuid import uuid4


# =========================
# Enums
# =========================

class FriendStatus(str, Enum):
    """Friend relationship status."""
    pending = "pending"      # request sent, not accepted
    accepted = "accepted"    # mutual friends
    blocked = "blocked"      # player has blocked


class ChallengeStatus(str, Enum):
    """Challenge game status."""
    pending = "pending"      # awaiting opponent response
    accepted = "accepted"    # opponent accepted
    in_progress = "in_progress"  # both players playing
    completed = "completed"  # both players finished
    declined = "declined"    # opponent declined
    abandoned = "abandoned"  # one player didn't complete


class ChallengeOutcome(str, Enum):
    """Challenge result."""
    player1_won = "player1_won"
    player2_won = "player2_won"
    draw = "draw"
    no_contest = "no_contest"  # abandoned/declined


# =========================
# Models
# =========================

class FriendRelationship(BaseModel):
    """Friendship between two players."""
    player_id: str
    friend_id: str
    status: FriendStatus = FriendStatus.pending
    created_at: datetime = Field(default_factory=datetime.now)
    accepted_at: Optional[datetime] = None
    blocked_at: Optional[datetime] = None


class Challenge(BaseModel):
    """1v1 game challenge between two players."""
    id: str = Field(default_factory=lambda: str(uuid4()))
    challenger_id: str
    opponent_id: str
    game_type: str  # e.g., "exam_micro", "tutorial_welcome"
    status: ChallengeStatus = ChallengeStatus.pending
    challenger_score: Optional[float] = None  # 0-100
    opponent_score: Optional[float] = None    # 0-100
    outcome: Optional[ChallengeOutcome] = None
    created_at: datetime = Field(default_factory=datetime.now)
    accepted_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    
    @property
    def is_active(self) -> bool:
        """Challenge hasn't expired and isn't completed/declined."""
        if self.status in [ChallengeStatus.completed, ChallengeStatus.declined, ChallengeStatus.abandoned]:
            return False
        if self.expires_at and datetime.now() > self.expires_at:
            return False
        return True


class ChallengeResult(BaseModel):
    """Summary of a completed challenge."""
    challenge_id: str
    challenger_name: str
    opponent_name: str
    challenger_score: float
    opponent_score: float
    outcome: ChallengeOutcome
    points_awarded_challenger: int = 0
    points_awarded_opponent: int = 0
    completed_at: datetime = Field(default_factory=datetime.now)


# =========================
# Friend Service
# =========================

class FriendService:
    """In-memory friend and challenge management."""
    
    def __init__(self):
        # Store friendships: {(min(p1, p2), max(p1, p2)) → FriendRelationship}
        self.friendships: Dict[tuple, FriendRelationship] = {}
        
        # Store challenges: {challenge_id → Challenge}
        self.challenges: Dict[str, Challenge] = {}
        
        # Quick lookup: {player_id → [friend_ids]}
        self.player_friends: Dict[str, List[str]] = {}
        
        # Quick lookup: {player_id → [pending_challenges]}
        self.pending_challenges: Dict[str, List[str]] = {}
    
    def _get_friendship_key(self, player_id: str, friend_id: str) -> tuple:
        """Get canonical key for friendship (ordered pair)."""
        return tuple(sorted([player_id, friend_id]))
    
    def send_friend_request(self, player_id: str, target_id: str) -> FriendRelationship:
        """Send friend request from player to target."""
        if player_id == target_id:
            raise ValueError("Cannot send friend request to yourself")
        
        key = self._get_friendship_key(player_id, target_id)
        
        if key in self.friendships:
            existing = self.friendships[key]
            if existing.status == FriendStatus.accepted:
                raise ValueError("Already friends")
            if existing.status == FriendStatus.pending:
                raise ValueError("Friend request already pending")
        
        friendship = FriendRelationship(
            player_id=player_id,
            friend_id=target_id,
        )
        
        self.friendships[key] = friendship
        if player_id not in self.player_friends:
            self.player_friends[player_id] = []
        
        return friendship
    
    def accept_friend_request(self, player_id: str, requester_id: str) -> FriendRelationship:
        """Accept friend request."""
        key = self._get_friendship_key(player_id, requester_id)
        
        if key not in self.friendships:
            raise ValueError("No friend request found")
        
        friendship = self.friendships[key]
        if friendship.status != FriendStatus.pending:
            raise ValueError(f"Cannot accept: status is {friendship.status}")
        
        friendship.status = FriendStatus.accepted
        friendship.accepted_at = datetime.now()
        
        # Add to both players' friend lists
        if player_id not in self.player_friends:
            self.player_friends[player_id] = []
        if requester_id not in self.player_friends:
            self.player_friends[requester_id] = []
        
        if requester_id not in self.player_friends[player_id]:
            self.player_friends[player_id].append(requester_id)
        if player_id not in self.player_friends[requester_id]:
            self.player_friends[requester_id].append(player_id)
        
        return friendship
    
    def decline_friend_request(self, player_id: str, requester_id: str) -> None:
        """Decline friend request."""
        key = self._get_friendship_key(player_id, requester_id)
        
        if key in self.friendships:
            del self.friendships[key]
    
    def block_player(self, player_id: str, target_id: str) -> FriendRelationship:
        """Block a player (prevents challenges & friend requests)."""
        key = self._get_friendship_key(player_id, target_id)
        
        if key in self.friendships:
            friendship = self.friendships[key]
        else:
            friendship = FriendRelationship(player_id=player_id, friend_id=target_id)
            self.friendships[key] = friendship
        
        friendship.status = FriendStatus.blocked
        friendship.blocked_at = datetime.now()
        
        # Remove from friend lists
        if target_id in self.player_friends.get(player_id, []):
            self.player_friends[player_id].remove(target_id)
        
        return friendship
    
    def get_friends(self, player_id: str) -> List[str]:
        """Get list of player's friends (accepted relationships)."""
        return self.player_friends.get(player_id, [])
    
    def create_challenge(self, challenger_id: str, opponent_id: str, game_type: str) -> Challenge:
        """Create a 1v1 challenge."""
        if challenger_id == opponent_id:
            raise ValueError("Cannot challenge yourself")
        
        # Check if already friends (optional - could allow non-friends)
        if opponent_id not in self.get_friends(challenger_id):
            raise ValueError("Can only challenge friends")
        
        # Check if blocked
        key = self._get_friendship_key(challenger_id, opponent_id)
        if key in self.friendships and self.friendships[key].status == FriendStatus.blocked:
            raise ValueError("Cannot challenge blocked player")
        
        challenge = Challenge(
            challenger_id=challenger_id,
            opponent_id=opponent_id,
            game_type=game_type,
            expires_at=datetime.now() + timedelta(days=7),  # 7 day expiration
        )
        
        self.challenges[challenge.id] = challenge
        
        # Add to opponent's pending challenges
        if opponent_id not in self.pending_challenges:
            self.pending_challenges[opponent_id] = []
        self.pending_challenges[opponent_id].append(challenge.id)
        
        return challenge
    
    def accept_challenge(self, challenge_id: str, player_id: str) -> Challenge:
        """Accept a challenge invitation."""
        if challenge_id not in self.challenges:
            raise ValueError("Challenge not found")
        
        challenge = self.challenges[challenge_id]
        if challenge.opponent_id != player_id:
            raise ValueError("Only the opponent can accept")
        
        if challenge.status != ChallengeStatus.pending:
            raise ValueError(f"Cannot accept: challenge is {challenge.status}")
        
        challenge.status = ChallengeStatus.accepted
        challenge.accepted_at = datetime.now()
        
        # Remove from pending
        if challenge_id in self.pending_challenges.get(player_id, []):
            self.pending_challenges[player_id].remove(challenge_id)
        
        return challenge
    
    def decline_challenge(self, challenge_id: str, player_id: str) -> Challenge:
        """Decline a challenge."""
        if challenge_id not in self.challenges:
            raise ValueError("Challenge not found")
        
        challenge = self.challenges[challenge_id]
        if challenge.opponent_id != player_id:
            raise ValueError("Only the opponent can decline")
        
        challenge.status = ChallengeStatus.declined
        
        # Remove from pending
        if challenge_id in self.pending_challenges.get(player_id, []):
            self.pending_challenges[player_id].remove(challenge_id)
        
        return challenge
    
    def submit_challenge_result(
        self,
        challenge_id: str,
        player_id: str,
        score: float,
    ) -> Challenge:
        """
        Submit a challenge game result for a player.
        Accepts scores from both players, finalizes when both submitted.
        """
        if challenge_id not in self.challenges:
            raise ValueError("Challenge not found")
        
        challenge = self.challenges[challenge_id]
        
        if player_id == challenge.challenger_id:
            if challenge.challenger_score is not None:
                raise ValueError("Challenger already submitted score")
            challenge.challenger_score = score
        elif player_id == challenge.opponent_id:
            if challenge.opponent_score is not None:
                raise ValueError("Opponent already submitted score")
            challenge.opponent_score = score
        else:
            raise ValueError("Player not in this challenge")
        
        # Check if both have submitted
        if challenge.challenger_score is not None and challenge.opponent_score is not None:
            challenge.status = ChallengeStatus.completed
            challenge.completed_at = datetime.now()
            
            # Determine outcome
            if challenge.challenger_score > challenge.opponent_score:
                challenge.outcome = ChallengeOutcome.player1_won
            elif challenge.opponent_score > challenge.challenger_score:
                challenge.outcome = ChallengeOutcome.player2_won
            else:
                challenge.outcome = ChallengeOutcome.draw
        else:
            challenge.status = ChallengeStatus.in_progress
        
        return challenge
    
    def get_player_challenges(self, player_id: str, status: Optional[ChallengeStatus] = None) -> List[Challenge]:
        """Get challenges for a player, optionally filtered by status."""
        challenges = []
        
        for challenge in self.challenges.values():
            if player_id not in [challenge.challenger_id, challenge.opponent_id]:
                continue
            if status and challenge.status != status:
                continue
            challenges.append(challenge)
        
        # Sort by created_at, newest first
        challenges.sort(key=lambda x: x.created_at, reverse=True)
        return challenges
    
    def get_pending_challenges(self, player_id: str) -> List[Challenge]:
        """Get pending challenges awaiting this player's response."""
        return [
            self.challenges[cid]
            for cid in self.pending_challenges.get(player_id, [])
            if cid in self.challenges
        ]


# Global instance
from datetime import timedelta
friend_service = FriendService()
