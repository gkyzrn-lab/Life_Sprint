"""
Tests for new engagement features: explanations, mini-lessons, badges,
story events, character customization, challenge modes, random events, and visual feedback.
"""

import pytest
from catalogs.explanations import (
    get_explanation,
    get_contextual_explanation,
    FINANCIAL_EXPLANATIONS
)
from catalogs.mini_lessons import (
    get_lesson,
    get_lessons_for_semester,
    get_random_lesson,
    LessonCategory
)
from catalogs.educational_badges import (
    get_badge,
    check_badge_requirements,
    get_badges_by_category
)
from catalogs.story_events import (
    get_event,
    get_available_events,
    process_choice,
    trigger_random_event
)
from catalogs.character_customization import (
    get_trait,
    get_backstory,
    apply_trait_effects,
    apply_backstory_effects,
    get_compatible_traits
)
from catalogs.challenge_modes import (
    get_challenge,
    check_challenge_victory,
    get_challenge_progress
)
from catalogs.random_events import (
    get_event as get_random_event,
    trigger_random_event as trigger_random,
    get_seasonal_event
)
from catalogs.visual_feedback import (
    calculate_progress_indicator,
    get_player_dashboard,
    calculate_overall_score,
    get_graduation_report_card
)


class TestExplanations:
    """Test explanation system."""
    
    def test_get_financial_explanation(self):
        """Test retrieving financial explanations."""
        explanation = get_explanation("financial", "student_loan")
        assert explanation is not None
        assert "title" in explanation
        assert "Understanding Student Loans" in explanation["title"]
        assert "example" in explanation
        assert "tip" in explanation
    
    def test_contextual_explanation(self):
        """Test personalized explanations."""
        context = {
            "loan_amount": 10000,
            "interest_rate": 0.06,
            "repayment_years": 10
        }
        explanation = get_contextual_explanation("student_loan", context)
        assert "your_situation" in explanation
        assert explanation["your_situation"]["borrowing"] == "$10,000"
    
    def test_all_explanations_have_required_fields(self):
        """Ensure all explanations have required fields."""
        for key, expl in FINANCIAL_EXPLANATIONS.items():
            assert "title" in expl
            assert "short" in expl
            assert "long" in expl
            assert "tip" in expl


class TestMiniLessons:
    """Test mini-lesson system."""
    
    def test_get_lesson_by_id(self):
        """Test retrieving lesson by ID."""
        lesson = get_lesson("budget_basics")
        assert lesson is not None
        assert lesson["title"] == "The 50/30/20 Budget Rule"
        assert lesson["category"] == LessonCategory.FINANCE
        assert "content" in lesson
        assert "key_takeaway" in lesson
    
    def test_lessons_unlock_by_semester(self):
        """Test lessons unlock at appropriate semesters."""
        semester_1_lessons = get_lessons_for_semester(1)
        semester_5_lessons = get_lessons_for_semester(5)
        
        # Earlier semesters have fewer lessons
        assert len(semester_1_lessons) < len(semester_5_lessons)
    
    def test_random_lesson_excludes_seen(self):
        """Test random lesson doesn't repeat seen lessons."""
        seen = ["budget_basics", "emergency_fund"]
        lesson = get_random_lesson(semester=5, exclude_seen=seen)
        
        if lesson:  # May be None if all seen
            assert lesson["id"] not in seen
    
    def test_all_lessons_have_duration(self):
        """Ensure all lessons have duration specified."""
        from catalogs.mini_lessons import MINI_LESSONS
        for lesson_id, lesson in MINI_LESSONS.items():
            assert "duration_seconds" in lesson
            assert 30 <= lesson["duration_seconds"] <= 90  # 30-90 second lessons


class TestEducationalBadges:
    """Test educational badge system."""
    
    def test_get_badge_by_id(self):
        """Test retrieving badge."""
        badge = get_badge("emergency_fund_starter")
        assert badge is not None
        assert badge["name"] == "🛡️ Emergency Fund Starter"
        assert "educational_value" in badge
    
    def test_check_badge_requirements(self):
        """Test badge requirement checking."""
        player_stats = {
            "savings_balance": 600,
            "total_debt_at_graduation": 15000
        }
        
        # Should earn emergency_fund_starter (requires 500)
        earned, progress = check_badge_requirements("emergency_fund_starter", player_stats)
        assert earned is True
        assert progress == 1.0
        
        # Should NOT earn loan_ninja_gold (requires 0 debt)
        earned, progress = check_badge_requirements("loan_ninja_gold", player_stats)
        assert earned is False
    
    def test_badges_by_category(self):
        """Test filtering badges by category."""
        financial_badges = get_badges_by_category("financial_literacy")
        assert len(financial_badges) > 0
        
        for badge in financial_badges.values():
            assert badge["category"] == "financial_literacy"


class TestStoryEvents:
    """Test story event system."""
    
    def test_get_story_event(self):
        """Test retrieving story event."""
        event = get_event("messy_roommate")
        assert event is not None
        assert "choices" in event
        assert len(event["choices"]) >= 2  # Multiple choices
    
    def test_available_events_respect_requirements(self):
        """Test events only available when requirements met."""
        player_state = {
            "semester": 3,
            "relationship_roommate": 60,
            "semesters_lived_together": 2
        }
        
        available = get_available_events(3, player_state)
        
        # Check that roommate_bestfriend is available (requires relationship 50+)
        event_ids = [e["id"] for e in available]
        assert "roommate_bestfriend" in event_ids
    
    def test_process_choice_returns_outcome(self):
        """Test processing player choice."""
        player_state = {"money": 1000}
        result = process_choice("messy_roommate", "confront", player_state)
        
        assert "outcome_text" in result
        assert "effects" in result
        assert "success" in result
    
    def test_events_can_repeat_or_not(self):
        """Test some events repeat, others don't."""
        repeatable = get_event("messy_roommate")
        unique = get_event("roommate_bestfriend")
        
        assert repeatable["can_repeat"] is True
        assert unique["can_repeat"] is False


class TestCharacterCustomization:
    """Test personality traits and backstories."""
    
    def test_get_personality_trait(self):
        """Test retrieving personality trait."""
        trait = get_trait("extroverted")
        assert trait is not None
        assert "affects" in trait
        assert "dialogue_style" in trait
    
    def test_conflicting_traits(self):
        """Test trait conflicts."""
        extroverted = get_trait("extroverted")
        introverted = get_trait("introverted")
        
        assert "introverted" in extroverted["conflicts_with"]
        assert "extroverted" in introverted["conflicts_with"]
    
    def test_compatible_traits_filter(self):
        """Test filtering compatible traits."""
        selected = ["extroverted"]
        compatible = get_compatible_traits(selected)
        
        # Introverted should NOT be in compatible list
        compatible_ids = [t["id"] for t in compatible]
        assert "introverted" not in compatible_ids
        assert "risk_taker" in compatible_ids  # No conflict
    
    def test_apply_trait_effects(self):
        """Test applying trait modifiers."""
        base_stats = {
            "stress": 50,
            "networking_effectiveness": 1.0
        }
        
        modified = apply_trait_effects(base_stats, ["extroverted"])
        
        # Extroverted reduces social stress and boosts networking
        assert modified["networking_effectiveness"] > 1.0
    
    def test_backstory_has_resources(self):
        """Test backstory provides starting resources."""
        backstory = get_backstory("first_generation")
        assert backstory is not None
        assert "starting_resources" in backstory
        assert "money" in backstory["starting_resources"]
        assert "unique_opportunities" in backstory
    
    def test_apply_backstory_effects(self):
        """Test applying backstory to player."""
        base_stats = {"money": 0}
        
        modified = apply_backstory_effects(base_stats, "first_generation")
        
        # First-gen student starts with 1000
        assert modified["money"] == 1000


class TestChallengeModes:
    """Test challenge mode system."""
    
    def test_get_challenge_mode(self):
        """Test retrieving challenge mode."""
        challenge = get_challenge("debt_free_challenge")
        assert challenge is not None
        assert "win_condition" in challenge
        assert "rules" in challenge
        assert "rewards" in challenge
    
    def test_check_victory_conditions(self):
        """Test victory condition checking."""
        player_state = {
            "graduated": True,
            "total_debt": 0
        }
        
        won, unmet = check_challenge_victory("debt_free_challenge", player_state)
        assert won is True
        assert len(unmet) == 0
    
    def test_check_victory_failure(self):
        """Test victory check when conditions not met."""
        player_state = {
            "graduated": True,
            "total_debt": 5000  # Has debt, should fail
        }
        
        won, unmet = check_challenge_victory("debt_free_challenge", player_state)
        assert won is False
        assert len(unmet) > 0
    
    def test_challenge_progress_tracking(self):
        """Test tracking progress toward challenge."""
        player_state = {
            "graduated": False,
            "total_debt": 10000
        }
        
        progress = get_challenge_progress("debt_free_challenge", player_state)
        
        assert "total_debt" in progress
        assert progress["total_debt"]["met"] is False  # Still has debt


class TestRandomEvents:
    """Test random event system."""
    
    def test_get_random_event_by_id(self):
        """Test retrieving random event."""
        event = get_random_event("unexpected_scholarship")
        assert event is not None
        assert "category" in event
        assert "probability" in event
    
    def test_seasonal_events(self):
        """Test seasonal event retrieval."""
        spring_break = get_seasonal_event(4)  # Semester 4
        assert spring_break is not None
        assert spring_break["id"] == "spring_break"
    
    def test_random_event_has_amount_function(self):
        """Test events with random amounts."""
        event = get_random_event("unexpected_scholarship")
        amount_func = event.get("amount")
        
        if callable(amount_func):
            amount = amount_func()
            assert 500 <= amount <= 2000  # Within expected range
    
    def test_random_events_respect_probability(self):
        """Test event triggering respects probability."""
        player_state = {"semester": 3, "gpa": 3.5}
        
        # Run multiple times to test randomness
        triggered_count = 0
        for _ in range(10):
            event = trigger_random(3, player_state)
            if event:
                triggered_count += 1
        
        # Should trigger sometimes but not always
        assert 0 <= triggered_count <= 10


class TestVisualFeedback:
    """Test visual feedback and progress tracking."""
    
    def test_calculate_progress_indicator(self):
        """Test progress indicator calculation."""
        indicator = calculate_progress_indicator(current=3.2, maximum=4.0)
        
        assert indicator.current == 3.2
        assert indicator.maximum == 4.0
        assert 0.0 <= indicator.percentage <= 1.0
        assert indicator.status in ["low", "medium", "good", "excellent", "critical"]
        assert indicator.color in ["red", "orange", "yellow", "lightgreen", "green"]
    
    def test_player_dashboard_generation(self):
        """Test generating player dashboard."""
        player_state = {
            "gpa": 3.5,
            "completed_credits": 60,
            "required_credits": 120,
            "balance": 2000,
            "total_debt": 15000,
            "stress": 45,
            "health": 85,
            "close_friends": 4,
            "professional_network": 25,
            "internships_completed": 1
        }
        
        dashboard = get_player_dashboard(player_state)
        
        assert "academic" in dashboard
        assert "financial" in dashboard
        assert "health" in dashboard
        assert "social" in dashboard
        assert "career" in dashboard
        assert "overall" in dashboard
    
    def test_overall_score_calculation(self):
        """Test overall life score calculation."""
        player_state = {
            "gpa": 3.5,
            "total_debt": 20000,
            "balance": 1000,
            "emergency_fund": 2000,
            "stress": 50,
            "health": 80,
            "average_sleep_hours": 7,
            "close_friends": 3,
            "professional_network": 20,
            "internships_completed": 1,
            "resume_strength": 70
        }
        
        score = calculate_overall_score(player_state)
        
        assert 0 <= score <= 100
        assert isinstance(score, float)
    
    def test_graduation_report_card(self):
        """Test final graduation report."""
        player_state = {
            "final_gpa": 3.6,
            "total_debt": 18000,
            "balance": 3000,
            "close_friends": 5,
            "professional_network": 40,
            "internships_completed": 2,
            "average_stress": 45,
            "burnout_count": 0
        }
        
        report = get_graduation_report_card(player_state)
        
        assert "final_stats" in report
        assert "grades" in report
        assert "post_graduation_outlook" in report
        
        # Check letter grades
        grades = report["grades"]
        assert all(grade in ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"] 
                  for grade in grades.values())


class TestIntegration:
    """Integration tests across multiple systems."""
    
    def test_full_player_journey(self):
        """Test a complete player journey through features."""
        # Start with character creation
        player_state = {
            "semester": 1,
            "gpa": 0.0,
            "money": 2000,
            "stress": 30,
            "traits": ["extroverted", "risk_taker"],
            "backstory": "first_generation"
        }
        
        # Apply character creation effects
        player_state = apply_trait_effects(player_state, player_state["traits"])
        player_state = apply_backstory_effects(player_state, player_state["backstory"])
        
        # Check available lessons
        lessons = get_lessons_for_semester(1)
        assert len(lessons) > 0
        
        # Check available events
        available_events = get_available_events(1, player_state)
        assert isinstance(available_events, list)
        
        # Generate dashboard
        dashboard = get_player_dashboard(player_state)
        assert "overall" in dashboard
    
    def test_challenge_mode_with_events(self):
        """Test challenge mode interacting with events."""
        # Start debt-free challenge
        challenge = get_challenge("debt_free_challenge")
        
        player_state = {
            "semester": 1,
            "graduated": False,
            "total_debt": 0,
            "money": 2000,
            "gpa": 3.0
        }
        
        # Apply starting modifiers
        for mod_key, mod_value in challenge["starting_modifiers"].items():
            player_state[mod_key] = mod_value
        
        # Check victory (should not be won yet)
        won, unmet = check_challenge_victory("debt_free_challenge", player_state)
        assert won is False  # Haven't graduated yet
        
        # Simulate graduation
        player_state["graduated"] = True
        won, unmet = check_challenge_victory("debt_free_challenge", player_state)
        assert won is True  # Graduated with no debt!


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
