"""
Tests for Social Features (Phase 1 Step 3)

Tests for leaderboards, friends, challenges, tournaments, and achievements.
"""

import pytest
from datetime import datetime, timedelta
from core_domain.store import STORE
from core_domain.player.player_model import Player
from core_domain.stats.stats_model import Stats
from core_domain.finance.finance_models import Finance
from catalogs.housing import HOUSING_OPTIONS

from social.leaderboard_service import leaderboard_service
from social.friends import friend_service, FriendStatus, ChallengeStatus
from social.tournament_scheduler import tournament_service, TournamentStatus, TournamentType
from social.social_sharing import achievement_service, AchievementCategory, ACHIEVEMENT_CATALOG


# =========================
# Fixtures
# =========================

@pytest.fixture(autouse=True)
def reset_services():
    """Reset all service instances before each test."""
    leaderboard_service.player_stats.clear()
    leaderboard_service.leaderboard_cache.clear()
    leaderboard_service.cache_expiry.clear()
    friend_service.friendships.clear()
    friend_service.challenges.clear()
    friend_service.player_friends.clear()
    friend_service.pending_challenges.clear()
    tournament_service.tournaments.clear()
    tournament_service.player_tournaments.clear()
    achievement_service.player_achievements.clear()
    achievement_service.achievement_unlock_dates.clear()
    achievement_service.achievement_progress.clear()
    STORE.players.clear()
    yield


def create_test_player(player_id: str, name: str, college_id: str = "cuny_baruch", major_id: str = "computer_science") -> Player:
    """Create a test player."""
    player = Player(
        id=player_id,
        name=name,
        age=20,
        hs_gpa=3.5,
        parent_income=60000.0,
        college_id=college_id,
        major_id=major_id,
        semester=1,
        year_in_school=1,
        stats=Stats(),
        finance=Finance(
            balance=5000.0,
            monthly_expenses=500.0,
            tuition_per_semester=5000.0,
        ),
        housing=HOUSING_OPTIONS["dorm"],
        job=None,
        plan=None,
        history=[],
    )
    STORE.put_player(player)
    return player


# =========================
# Leaderboard Tests
# =========================

class TestLeaderboard:
    def test_add_player_to_leaderboard(self):
        """Test adding player stats to leaderboard."""
        player = create_test_player("p1", "Alice")
        
        leaderboard_service.update_player_stats(
            "p1",
            "Alice",
            "cuny_baruch",
            "computer_science",
            games_played=7,
            games_won=5,
            points=850,
        )
        
        stats = leaderboard_service.get_player_stats("p1")
        assert stats is not None
        assert stats.total_games_played == 7
        assert stats.total_games_won == 5
        assert stats.total_points == 850
    
    def test_get_global_leaderboard(self):
        """Test retrieving global leaderboard."""
        players = [
            create_test_player("p1", "Alice"),
            create_test_player("p2", "Bob"),
            create_test_player("p3", "Charlie"),
        ]
        
        leaderboard_service.update_player_stats("p1", "Alice", "cuny_baruch", "cs", games_played=12, games_won=10, points=1000)
        leaderboard_service.update_player_stats("p2", "Bob", "cuny_baruch", "cs", games_played=10, games_won=5, points=750)
        leaderboard_service.update_player_stats("p3", "Charlie", "cuny_baruch", "cs", games_played=15, games_won=15, points=1200)
        
        leaderboard = leaderboard_service.get_leaderboard("global", limit=10)
        
        assert len(leaderboard.entries) == 3
        # Should be sorted by points descending
        assert leaderboard.entries[0].score == 1200
        assert leaderboard.entries[1].score == 1000
        assert leaderboard.entries[2].score == 750
    
    def test_leaderboard_caching(self):
        """Test that leaderboard uses caching."""
        players = [
            create_test_player("p1", "Alice"),
            create_test_player("p2", "Bob"),
        ]
        
        leaderboard_service.update_player_stats("p1", "Alice", "cuny_baruch", "cs", games_played=5, games_won=4, points=800)
        
        # Get leaderboard twice - second should use cache
        lb1 = leaderboard_service.get_leaderboard("global")
        lb2 = leaderboard_service.get_leaderboard("global")
        
        assert lb1 is lb2  # Same object from cache


# =========================
# Friend System Tests
# =========================

class TestFriendsSystem:
    def test_send_friend_request(self):
        """Test sending friend request."""
        p1 = create_test_player("p1", "Alice")
        p2 = create_test_player("p2", "Bob")
        
        friendship = friend_service.send_friend_request("p1", "p2")
        
        assert friendship.player_id == "p1"
        assert friendship.friend_id == "p2"
        assert friendship.status == FriendStatus.pending
    
    def test_accept_friend_request(self):
        """Test accepting friend request."""
        p1 = create_test_player("p1", "Alice")
        p2 = create_test_player("p2", "Bob")
        
        friend_service.send_friend_request("p1", "p2")
        friendship = friend_service.accept_friend_request("p2", "p1")
        
        assert friendship.status == FriendStatus.accepted
        assert friendship.accepted_at is not None
        assert "p2" in friend_service.get_friends("p1")
        assert "p1" in friend_service.get_friends("p2")
    
    def test_decline_friend_request(self):
        """Test declining friend request."""
        p1 = create_test_player("p1", "Alice")
        p2 = create_test_player("p2", "Bob")
        
        friend_service.send_friend_request("p1", "p2")
        friend_service.decline_friend_request("p2", "p1")
        
        friends = friend_service.get_friends("p2")
        assert "p1" not in friends
    
    def test_block_player(self):
        """Test blocking a player."""
        p1 = create_test_player("p1", "Alice")
        p2 = create_test_player("p2", "Bob")
        
        friend_service.send_friend_request("p1", "p2")
        friend_service.accept_friend_request("p2", "p1")
        
        # Block player
        friend_service.block_player("p1", "p2")
        
        friends = friend_service.get_friends("p1")
        assert "p2" not in friends
    
    def test_cannot_challenge_non_friend(self):
        """Test that you can only challenge friends."""
        p1 = create_test_player("p1", "Alice")
        p2 = create_test_player("p2", "Bob")
        
        with pytest.raises(ValueError, match="Can only challenge friends"):
            friend_service.create_challenge("p1", "p2", "exam_micro")
    
    def test_create_and_accept_challenge(self):
        """Test creating and accepting a challenge."""
        p1 = create_test_player("p1", "Alice")
        p2 = create_test_player("p2", "Bob")
        
        # Make friends
        friend_service.send_friend_request("p1", "p2")
        friend_service.accept_friend_request("p2", "p1")
        
        # Create challenge
        challenge = friend_service.create_challenge("p1", "p2", "exam_micro")
        
        assert challenge.challenger_id == "p1"
        assert challenge.opponent_id == "p2"
        assert challenge.status == ChallengeStatus.pending
        
        # Accept challenge
        challenge = friend_service.accept_challenge(challenge.id, "p2")
        assert challenge.status == ChallengeStatus.accepted
    
    def test_submit_challenge_results(self):
        """Test submitting challenge game results."""
        p1 = create_test_player("p1", "Alice")
        p2 = create_test_player("p2", "Bob")
        
        friend_service.send_friend_request("p1", "p2")
        friend_service.accept_friend_request("p2", "p1")
        
        challenge = friend_service.create_challenge("p1", "p2", "exam_micro")
        friend_service.accept_challenge(challenge.id, "p2")
        
        # Submit results
        challenge = friend_service.submit_challenge_result(challenge.id, "p1", 85.0)
        assert challenge.challenger_score == 85.0
        assert challenge.status == ChallengeStatus.in_progress
        
        challenge = friend_service.submit_challenge_result(challenge.id, "p2", 92.0)
        assert challenge.opponent_score == 92.0
        assert challenge.status == ChallengeStatus.completed
        assert challenge.outcome.value == "player2_won"


# =========================
# Tournament Tests
# =========================

class TestTournamentSystem:
    def test_create_tournament(self):
        """Test creating a tournament."""
        tournament = tournament_service.create_tournament(
            name="Weekly Challenge",
            tournament_type=TournamentType.weekly,
            game_type="exam_micro",
            max_participants=16,
        )
        
        assert tournament.name == "Weekly Challenge"
        assert tournament.tournament_type == TournamentType.weekly
        assert tournament.status == TournamentStatus.signup
    
    def test_register_player(self):
        """Test registering player for tournament."""
        p1 = create_test_player("p1", "Alice")
        
        tournament = tournament_service.create_tournament(
            "Weekly", TournamentType.weekly, "exam_micro"
        )
        
        tournament = tournament_service.register_player(
            tournament.id, "p1", "Alice", 1250.0
        )
        
        assert "p1" in tournament.participants
        assert tournament.participants["p1"].wins == 0
    
    def test_finalize_bracket(self):
        """Test generating tournament bracket."""
        tournament = tournament_service.create_tournament(
            "Weekly", TournamentType.weekly, "exam_micro", max_participants=8
        )
        
        for i in range(4):
            p = create_test_player(f"p{i}", f"Player{i}")
            tournament_service.register_player(
                tournament.id, f"p{i}", f"Player{i}", 1200.0 + i * 50
            )
        
        tournament, matches = tournament_service.finalize_bracket(tournament.id)
        
        assert tournament.status == TournamentStatus.bracket_ready
        assert len(matches) > 0
        assert all(m.round_num == 1 for m in matches)
    
    def test_submit_match_result(self):
        """Test submitting tournament match result."""
        tournament = tournament_service.create_tournament(
            "Weekly", TournamentType.weekly, "exam_micro"
        )
        
        p1 = create_test_player("p1", "Alice")
        p2 = create_test_player("p2", "Bob")
        
        tournament_service.register_player(tournament.id, "p1", "Alice", 1200.0)
        tournament_service.register_player(tournament.id, "p2", "Bob", 1200.0)
        
        tournament, matches = tournament_service.finalize_bracket(tournament.id)
        match = matches[0]
        
        tournament_service.submit_match_result(
            tournament.id,
            match.id,
            "p1",  # winner
            85.0,  # p1 score
            78.0,  # p2 score
        )
        
        match = tournament.matches[match.id]
        assert match.winner_id == "p1"
        assert match.completed is True
        assert tournament.participants["p1"].wins == 1
        assert tournament.participants["p1"].points > 0
    
    def test_tournament_standings(self):
        """Test getting tournament standings."""
        tournament = tournament_service.create_tournament(
            "Weekly", TournamentType.weekly, "exam_micro"
        )
        
        for i in range(3):
            p = create_test_player(f"p{i}", f"Player{i}")
            tournament_service.register_player(
                tournament.id, f"p{i}", f"Player{i}", 1200.0
            )
        
        standings = tournament_service.get_tournament_standings(tournament.id)
        
        assert len(standings) == 3
        assert standings[0].rank == 1


# =========================
# Achievement Tests
# =========================

class TestAchievementSystem:
    def test_unlock_achievement(self):
        """Test unlocking an achievement."""
        player_stats = {
            "friends_count": 1,
        }
        
        unlocked = achievement_service.check_and_unlock_achievements(
            "p1", player_stats
        )
        
        assert "first_friend" in unlocked
    
    def test_get_player_achievements(self):
        """Test retrieving player's achievements."""
        player_stats = {"friends_count": 1}
        achievement_service.check_and_unlock_achievements("p1", player_stats)
        
        achievements = achievement_service.get_player_achievements("p1")
        
        assert len(achievements) > 0
        assert any(a.id == "first_friend" for a in achievements)
    
    def test_achievement_progress(self):
        """Test tracking progress towards achievements."""
        player_stats = {"friends_count": 5}  # 50% towards "popular" (10 friends)
        
        achievement_service.check_and_unlock_achievements("p1", player_stats)
        progress = achievement_service.get_achievement_progress("p1")
        
        assert "popular" in progress
        assert progress["popular"] == 50.0
    
    def test_get_badges(self):
        """Test getting visual badges for achievements."""
        player_stats = {"friends_count": 1}
        achievement_service.check_and_unlock_achievements("p1", player_stats)
        
        badges = achievement_service.get_unlocked_badges("p1")
        
        assert len(badges) > 0
        assert all(b.unlocked for b in badges)
    
    def test_shareable_achievement(self):
        """Test creating shareable achievement."""
        player_stats = {"friends_count": 1}
        achievement_service.check_and_unlock_achievements("p1", player_stats)
        
        shareable = achievement_service.create_shareable_achievement(
            "p1", "first_friend", "TestPlayer"
        )
        
        assert shareable.achievement_name == "Making Connections"
        assert shareable.player_name == "TestPlayer"
        assert len(shareable.twitter_text) > 0
        assert len(shareable.facebook_text) > 0


# =========================
# Integration Tests
# =========================

class TestSocialIntegration:
    def test_friend_challenge_workflow(self):
        """Test complete friend challenge workflow."""
        p1 = create_test_player("p1", "Alice")
        p2 = create_test_player("p2", "Bob")
        
        # Make friends
        friend_service.send_friend_request("p1", "p2")
        friend_service.accept_friend_request("p2", "p1")
        
        # Create challenge
        challenge = friend_service.create_challenge("p1", "p2", "exam_micro")
        
        # Accept and play
        friend_service.accept_challenge(challenge.id, "p2")
        friend_service.submit_challenge_result(challenge.id, "p1", 95.0)
        friend_service.submit_challenge_result(challenge.id, "p2", 88.0)
        
        # Verify completion
        final_challenge = friend_service.challenges[challenge.id]
        assert final_challenge.status == ChallengeStatus.completed
        assert final_challenge.outcome.value == "player1_won"
    
    def test_tournament_full_cycle(self):
        """Test complete tournament from signup to completion."""
        tournament = tournament_service.create_tournament(
            "Mini Tournament",
            TournamentType.weekly,
            "exam_micro",
            max_participants=4,
        )
        
        # Register players
        for i in range(4):
            p = create_test_player(f"p{i}", f"Player{i}")
            tournament_service.register_player(
                tournament.id, f"p{i}", f"Player{i}", 1200.0 + i * 25
            )
        
        # Finalize bracket
        tournament, matches = tournament_service.finalize_bracket(tournament.id)
        assert tournament.status == TournamentStatus.bracket_ready
        
        # Play match
        match = matches[0]
        tournament_service.submit_match_result(
            tournament.id, match.id, match.player1_id, 90.0, 80.0
        )
        
        # Check standings
        standings = tournament_service.get_tournament_standings(tournament.id)
        assert standings[0].wins >= 1
    
    def test_achievement_unlock_from_friends(self):
        """Test unlocking achievement by making friends."""
        p1 = create_test_player("p1", "Alice")
        p2 = create_test_player("p2", "Bob")
        
        # Make friend
        friend_service.send_friend_request("p1", "p2")
        friend_service.accept_friend_request("p2", "p1")
        
        # Check achievements
        player_stats = {"friends_count": len(friend_service.get_friends("p1"))}
        unlocked = achievement_service.check_and_unlock_achievements("p1", player_stats)
        
        assert "first_friend" in unlocked


# =========================
# Run Tests
# =========================

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
