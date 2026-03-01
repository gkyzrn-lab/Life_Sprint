"""
Tournament System & Scheduling

Weekly and monthly tournaments with brackets, standings, and prizes.
"""

from __future__ import annotations
from typing import List, Dict, Optional, Set, Tuple
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime, timedelta
from uuid import uuid4
import random


# =========================
# Enums
# =========================

class TournamentType(str, Enum):
    """Tournament frequency and scope."""
    weekly = "weekly"
    monthly = "monthly"
    season = "season"


class TournamentStatus(str, Enum):
    """Tournament state."""
    signup = "signup"              # accepting registrations
    bracket_ready = "bracket_ready"  # bracket finalized
    in_progress = "in_progress"    # matches being played
    completed = "completed"        # all matches done


# =========================
# Models
# =========================

class TournamentParticipant(BaseModel):
    """Tournament participant details."""
    player_id: str
    player_name: str
    skill_rating: float = 1200.0
    wins: int = 0
    losses: int = 0
    current_rank: int = 0  # seed position
    eliminated: bool = False
    points: int = 0  # tournament points


class Match(BaseModel):
    """Single tournament match."""
    id: str = Field(default_factory=lambda: str(uuid4()))
    tournament_id: str
    round_num: int
    player1_id: str
    player2_id: str
    winner_id: Optional[str] = None
    player1_score: Optional[float] = None
    player2_score: Optional[float] = None
    completed: bool = False
    completed_at: Optional[datetime] = None
    points_awarded_winner: int = 0
    points_awarded_loser: int = 0


class TournamentStanding(BaseModel):
    """Participant standings in tournament."""
    player_id: str
    player_name: str
    wins: int
    losses: int
    points: int
    rank: int


class Tournament(BaseModel):
    """Tournament instance."""
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    tournament_type: TournamentType
    status: TournamentStatus = TournamentStatus.signup
    game_type: str  # e.g., "exam_micro"
    created_at: datetime = Field(default_factory=datetime.now)
    signup_deadline: datetime
    start_date: datetime
    end_date: datetime
    participants: Dict[str, TournamentParticipant] = Field(default_factory=dict)
    matches: Dict[str, Match] = Field(default_factory=dict)
    
    max_participants: int = 32
    min_participants: int = 2
    prize_pool: int = 100  # points distributed
    
    @property
    def is_full(self) -> bool:
        return len(self.participants) >= self.max_participants
    
    @property
    def can_register(self) -> bool:
        return (
            self.status == TournamentStatus.signup
            and datetime.now() < self.signup_deadline
            and not self.is_full
        )


# =========================
# Tournament Service
# =========================

class TournamentService:
    """Tournament creation, registration, and bracket management."""
    
    def __init__(self):
        self.tournaments: Dict[str, Tournament] = {}
        self.player_tournaments: Dict[str, List[str]] = {}  # {player_id → [tournament_ids]}
    
    def create_tournament(
        self,
        name: str,
        tournament_type: TournamentType,
        game_type: str,
        max_participants: int = 32,
        prize_pool: int = 100,
    ) -> Tournament:
        """Create a new tournament."""
        now = datetime.now()
        signup_days = 7 if tournament_type == TournamentType.weekly else 14
        
        tournament = Tournament(
            name=name,
            tournament_type=tournament_type,
            game_type=game_type,
            signup_deadline=now + timedelta(days=signup_days),
            start_date=now + timedelta(days=signup_days + 1),
            end_date=now + timedelta(days=signup_days + 14),
            max_participants=max_participants,
            prize_pool=prize_pool,
        )
        
        self.tournaments[tournament.id] = tournament
        return tournament
    
    def register_player(
        self,
        tournament_id: str,
        player_id: str,
        player_name: str,
        skill_rating: float,
    ) -> Tournament:
        """Register a player for tournament."""
        if tournament_id not in self.tournaments:
            raise ValueError("Tournament not found")
        
        tournament = self.tournaments[tournament_id]
        
        if not tournament.can_register:
            raise ValueError("Tournament registration closed")
        
        if player_id in tournament.participants:
            raise ValueError("Player already registered")
        
        participant = TournamentParticipant(
            player_id=player_id,
            player_name=player_name,
            skill_rating=skill_rating,
        )
        
        tournament.participants[player_id] = participant
        
        if player_id not in self.player_tournaments:
            self.player_tournaments[player_id] = []
        self.player_tournaments[player_id].append(tournament_id)
        
        return tournament
    
    def finalize_bracket(self, tournament_id: str) -> Tuple[Tournament, List[Match]]:
        """Generate bracket and return matches."""
        if tournament_id not in self.tournaments:
            raise ValueError("Tournament not found")
        
        tournament = self.tournaments[tournament_id]
        
        if len(tournament.participants) < tournament.min_participants:
            raise ValueError(f"Need at least {tournament.min_participants} participants")
        
        # Sort by skill rating to seed bracket
        participants_list = sorted(
            tournament.participants.values(),
            key=lambda p: p.skill_rating,
            reverse=True,
        )
        
        # Assign ranks
        for i, p in enumerate(participants_list):
            p.current_rank = i + 1
        
        # Generate round 1 matches (snake seed)
        matches = []
        for i in range(0, len(participants_list), 2):
            if i + 1 < len(participants_list):
                match = Match(
                    tournament_id=tournament_id,
                    round_num=1,
                    player1_id=participants_list[i].player_id,
                    player2_id=participants_list[i + 1].player_id,
                    points_awarded_winner=10,
                    points_awarded_loser=3,
                )
                matches.append(match)
                tournament.matches[match.id] = match
        
        tournament.status = TournamentStatus.bracket_ready
        return tournament, matches
    
    def submit_match_result(
        self,
        tournament_id: str,
        match_id: str,
        winner_id: str,
        player1_score: float,
        player2_score: float,
    ) -> Match:
        """Submit match result and advance winner."""
        if tournament_id not in self.tournaments:
            raise ValueError("Tournament not found")
        
        tournament = self.tournaments[tournament_id]
        
        if match_id not in tournament.matches:
            raise ValueError("Match not found")
        
        match = tournament.matches[match_id]
        
        if match.completed:
            raise ValueError("Match already completed")
        
        if winner_id not in [match.player1_id, match.player2_id]:
            raise ValueError("Winner must be one of the players")
        
        match.winner_id = winner_id
        match.player1_score = player1_score
        match.player2_score = player2_score
        match.completed = True
        match.completed_at = datetime.now()
        
        # Update participant stats
        winner = tournament.participants[winner_id]
        loser_id = match.player2_id if winner_id == match.player1_id else match.player1_id
        loser = tournament.participants[loser_id]
        
        winner.wins += 1
        winner.points += match.points_awarded_winner
        loser.losses += 1
        loser.points += match.points_awarded_loser
        
        # Generate next round matches if all current round done
        self._advance_tournament_bracket(tournament)
        
        return match
    
    def _advance_tournament_bracket(self, tournament: Tournament) -> None:
        """Generate next round bracket if all matches in current round are done."""
        completed_rounds = set()
        for match in tournament.matches.values():
            if match.completed:
                completed_rounds.add(match.round_num)
        
        # Check if current round is fully completed
        current_round_matches = [
            m for m in tournament.matches.values()
            if m.round_num == max(m.round_num for m in tournament.matches.values())
        ]
        
        if all(m.completed for m in current_round_matches) and len(current_round_matches) > 1:
            # Generate next round
            next_round_num = max(m.round_num for m in tournament.matches.values()) + 1
            winners = sorted(
                [m.winner_id for m in current_round_matches if m.winner_id],
                key=lambda pid: tournament.participants[pid].skill_rating,
                reverse=True,
            )
            
            for i in range(0, len(winners), 2):
                if i + 1 < len(winners):
                    match = Match(
                        tournament_id=tournament.id,
                        round_num=next_round_num,
                        player1_id=winners[i],
                        player2_id=winners[i + 1],
                        points_awarded_winner=20,
                        points_awarded_loser=5,
                    )
                    tournament.matches[match.id] = match
        
        # Check if tournament is complete (1 player left undefeated or finals done)
        active_count = sum(1 for p in tournament.participants.values() if not p.eliminated)
        if active_count <= 1 or (current_round_matches and len(current_round_matches) == 1 and current_round_matches[0].completed):
            tournament.status = TournamentStatus.completed
    
    def get_tournament_standings(self, tournament_id: str) -> List[TournamentStanding]:
        """Get tournament standings sorted by points and wins."""
        if tournament_id not in self.tournaments:
            raise ValueError("Tournament not found")
        
        tournament = self.tournaments[tournament_id]
        standings = [
            TournamentStanding(
                player_id=p.player_id,
                player_name=p.player_name,
                wins=p.wins,
                losses=p.losses,
                points=p.points,
                rank=0,
            )
            for p in tournament.participants.values()
        ]
        
        # Sort by points (desc), wins (desc)
        standings.sort(key=lambda s: (s.points, s.wins), reverse=True)
        
        # Assign ranks
        for i, standing in enumerate(standings):
            standing.rank = i + 1
        
        return standings
    
    def get_player_tournament_history(self, player_id: str) -> List[Tournament]:
        """Get all tournaments a player has joined."""
        tournament_ids = self.player_tournaments.get(player_id, [])
        return [self.tournaments[tid] for tid in tournament_ids if tid in self.tournaments]
    
    def get_active_tournaments(self) -> List[Tournament]:
        """Get all active tournaments (signup or in progress)."""
        now = datetime.now()
        return [
            t for t in self.tournaments.values()
            if t.status in [TournamentStatus.signup, TournamentStatus.bracket_ready, TournamentStatus.in_progress]
            and t.start_date > now
        ]


# Global instance
tournament_service = TournamentService()
