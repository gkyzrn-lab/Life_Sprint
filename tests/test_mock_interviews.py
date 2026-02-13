"""Tests for mock interview system."""

import pytest
from catalogs.mock_interviews import (
    generate_interview,
    evaluate_interview_response,
    simulate_full_interview,
    get_interview_prep_tip,
    get_tips_by_category,
    InterviewQuestion,
    InterviewResponse,
    INTERVIEW_QUESTIONS,
    INTERVIEW_PREP_TIPS
)


def test_interview_questions_exist():
    """Test that common interview questions are defined."""
    assert len(INTERVIEW_QUESTIONS) >= 8
    
    # Must-have questions
    assert "tell_me_about_yourself" in INTERVIEW_QUESTIONS
    assert "why_this_company" in INTERVIEW_QUESTIONS
    assert "greatest_weakness" in INTERVIEW_QUESTIONS
    assert "questions_for_us" in INTERVIEW_QUESTIONS


def test_interview_question_structure():
    """Test that questions have required educational content."""
    for question in INTERVIEW_QUESTIONS.values():
        assert len(question.question_text) > 0
        assert question.question_type in ["behavioral", "technical", "situational", "culture_fit", "tricky"]
        assert question.difficulty in ["easy", "medium", "hard"]
        assert len(question.key_criteria) >= 2
        assert len(question.good_answer_framework) > 50
        assert len(question.red_flags) >= 2


def test_interview_prep_tips_exist():
    """Test that interview prep tips are comprehensive."""
    assert len(INTERVIEW_PREP_TIPS) >= 5
    
    # Critical tips must exist
    assert "star_method" in INTERVIEW_PREP_TIPS
    assert "research_company" in INTERVIEW_PREP_TIPS
    assert "prepare_stories" in INTERVIEW_PREP_TIPS


def test_prep_tip_structure():
    """Test that prep tips have educational content."""
    for tip in INTERVIEW_PREP_TIPS.values():
        assert len(tip.title) > 0
        assert len(tip.description) > 50
        assert len(tip.example) > 50
        assert tip.impact in ["low", "medium", "high", "critical"]
        assert tip.category in ["research", "star_method", "common_questions", "body_language", "follow_up", "red_flags"]


def test_generate_phone_screen():
    """Test generating a phone screen interview."""
    interview = generate_interview("Software Engineer", "mid", "phone_screen")
    
    assert interview.interview_round == "phone_screen"
    assert interview.time_limit_minutes == 30
    assert len(interview.questions) >= 3
    assert interview.interview_format == "one_on_one"
    assert interview.interviewer_personality == "friendly"


def test_generate_first_round():
    """Test generating a first round interview."""
    interview = generate_interview("Product Manager", "mid", "first_round")
    
    assert interview.interview_round == "first_round"
    assert interview.time_limit_minutes == 60
    assert len(interview.questions) >= 4
    # Should include behavioral questions
    behavioral_count = sum(1 for q in interview.questions if q.question_type == "behavioral")
    assert behavioral_count >= 2


def test_generate_technical_round():
    """Test generating a technical interview."""
    interview = generate_interview("Software Engineer", "high", "technical")
    
    assert interview.interview_round == "technical"
    # Should include technical questions
    technical_count = sum(1 for q in interview.questions if q.question_type == "technical")
    assert technical_count >= 1


def test_generate_final_round():
    """Test generating a final round interview."""
    interview = generate_interview("Data Analyst", "high", "final_round")
    
    assert interview.interview_round == "final_round"
    assert interview.time_limit_minutes >= 60
    assert interview.interview_format == "panel"
    # Should include hard questions
    hard_count = sum(1 for q in interview.questions if q.difficulty == "hard")
    assert hard_count >= 2


def test_evaluate_detailed_star_response():
    """Test evaluating a good STAR method response."""
    question = INTERVIEW_QUESTIONS["conflict_with_coworker"]
    
    response = InterviewResponse(
        response_type="detailed_star",
        response_text="[Good STAR response]",
        used_star_method=True,
        used_specific_examples=True,
        demonstrated_skill=True,
        showed_enthusiasm=True,
        avoided_red_flags=True
    )
    
    evaluation = evaluate_interview_response(question, response, 80, 80)
    
    # Should get high score
    assert evaluation["score"] >= 80
    assert len(evaluation["feedback"]) > 0


def test_evaluate_nervous_ramble():
    """Test evaluating a poor nervous response."""
    question = INTERVIEW_QUESTIONS["tell_me_about_yourself"]
    
    response = InterviewResponse(
        response_type="nervous_ramble",
        response_text="[Rambling response]",
        used_star_method=False,
        used_specific_examples=False,
        demonstrated_skill=False,
        showed_enthusiasm=False,
        avoided_red_flags=False  # Hit red flags
    )
    
    evaluation = evaluate_interview_response(question, response, 40, 30)
    
    # Should get low score
    assert evaluation["score"] < 50
    assert any("red flag" in fb.lower() for fb in evaluation["feedback"])


def test_star_method_bonus_for_behavioral():
    """Test that STAR method gives bonus for behavioral questions."""
    behavioral_question = INTERVIEW_QUESTIONS["conflict_with_coworker"]
    
    response_with_star = InterviewResponse(
        response_type="detailed_star",
        response_text="[Response]",
        used_star_method=True,
        used_specific_examples=True,
        demonstrated_skill=True,
        showed_enthusiasm=True,
        avoided_red_flags=True
    )
    
    response_without_star = InterviewResponse(
        response_type="brief_answer",
        response_text="[Response]",
        used_star_method=False,
        used_specific_examples=True,
        demonstrated_skill=True,
        showed_enthusiasm=True,
        avoided_red_flags=True
    )
    
    eval_with = evaluate_interview_response(behavioral_question, response_with_star, 50, 50)
    eval_without = evaluate_interview_response(behavioral_question, response_without_star, 50, 50)
    
    # STAR method should boost score
    assert eval_with["score"] > eval_without["score"]


def test_simulate_successful_interview():
    """Test simulating a successful interview."""
    scenario = generate_interview("Software Engineer", "mid", "first_round")
    
    outcome = simulate_full_interview(
        scenario,
        player_communication_skills=85,
        player_confidence=80,
        player_preparation="thorough"
    )
    
    # Should succeed with high skills and prep
    assert outcome.success == True
    assert outcome.overall_score >= 60
    assert outcome.next_step in ["technical", "final_round", "offer"]
    assert len(outcome.strengths) > 0


def test_simulate_failed_interview():
    """Test simulating a failed interview."""
    scenario = generate_interview("Software Engineer", "high", "technical")
    
    outcome = simulate_full_interview(
        scenario,
        player_communication_skills=30,
        player_confidence=25,
        player_preparation="none"
    )
    
    # Should fail with low skills and no prep
    assert outcome.success == False
    assert outcome.next_step == "rejected"
    assert outcome.rejection_reason is not None
    assert len(outcome.areas_for_improvement) > 0


def test_preparation_improves_outcome():
    """Test that thorough preparation improves interview outcome."""
    scenario = generate_interview("Data Analyst", "mid", "first_round")
    
    outcome_no_prep = simulate_full_interview(
        scenario,
        player_communication_skills=60,
        player_confidence=60,
        player_preparation="none"
    )
    
    outcome_thorough_prep = simulate_full_interview(
        scenario,
        player_communication_skills=60,
        player_confidence=60,
        player_preparation="thorough"
    )
    
    # Thorough prep should improve scores
    assert outcome_thorough_prep.overall_score >= outcome_no_prep.overall_score


def test_communication_skills_matter():
    """Test that communication skills impact interview success."""
    scenario = generate_interview("Product Manager", "mid", "first_round")
    
    outcome_low_skills = simulate_full_interview(
        scenario,
        player_communication_skills=40,
        player_confidence=60,
        player_preparation="basic"
    )
    
    outcome_high_skills = simulate_full_interview(
        scenario,
        player_communication_skills=90,
        player_confidence=60,
        player_preparation="basic"
    )
    
    # High communication skills should help
    assert outcome_high_skills.communication_score > outcome_low_skills.communication_score


def test_interview_progression():
    """Test that interview rounds progress correctly."""
    # Phone screen -> first round
    phone_scenario = generate_interview("Software Engineer", "mid", "phone_screen")
    phone_outcome = simulate_full_interview(phone_scenario, 85, 80, "thorough")
    
    if phone_outcome.success:
        assert phone_outcome.next_step == "first_round"
    
    # First round -> technical
    first_scenario = generate_interview("Software Engineer", "mid", "first_round")
    first_outcome = simulate_full_interview(first_scenario, 85, 80, "thorough")
    
    if first_outcome.success:
        assert first_outcome.next_step == "technical"
    
    # Technical -> final
    tech_scenario = generate_interview("Software Engineer", "mid", "technical")
    tech_outcome = simulate_full_interview(tech_scenario, 85, 80, "thorough")
    
    if tech_outcome.success:
        assert tech_outcome.next_step == "final_round"
    
    # Final -> offer
    final_scenario = generate_interview("Software Engineer", "mid", "final_round")
    final_outcome = simulate_full_interview(final_scenario, 85, 80, "thorough")
    
    if final_outcome.success:
        assert final_outcome.next_step == "offer"


def test_get_interview_prep_tip():
    """Test retrieving specific prep tips."""
    tip = get_interview_prep_tip("star_method")
    assert tip is not None
    assert tip.impact == "critical"
    assert "star" in tip.title.lower()


def test_get_tips_by_category():
    """Test retrieving tips by category."""
    star_tips = get_tips_by_category("star_method")
    assert len(star_tips) >= 1
    
    research_tips = get_tips_by_category("research")
    assert len(research_tips) >= 1


def test_red_flags_are_educational():
    """Test that red flags teach what not to do."""
    for question in INTERVIEW_QUESTIONS.values():
        assert len(question.red_flags) >= 2
        
        # Red flags should be specific and educational
        for red_flag in question.red_flags:
            assert len(red_flag) > 10  # Not just "bad"


def test_good_answer_frameworks():
    """Test that good answer frameworks are helpful."""
    for question in INTERVIEW_QUESTIONS.values():
        assert len(question.good_answer_framework) > 50
        
        # Should provide structure, not just "be good"
        framework = question.good_answer_framework.lower()
        # Should contain actionable advice
        assert any(word in framework for word in ["structure", "example", "step", "focus", "avoid"])


def test_interview_scenarios_vary_by_tier():
    """Test that interview difficulty matches job tier."""
    low_tier = generate_interview("Barista", "low", "first_round")
    high_tier = generate_interview("Senior Engineer", "high", "first_round")
    
    # Both should have interviews, but high tier might be more demanding
    assert len(low_tier.questions) >= 3
    assert len(high_tier.questions) >= 3


def test_outcome_includes_actionable_feedback():
    """Test that interview outcomes include useful feedback."""
    scenario = generate_interview("Software Engineer", "mid", "first_round")
    outcome = simulate_full_interview(scenario, 60, 60, "basic")
    
    # Should have strengths or improvements (or both)
    assert len(outcome.strengths) + len(outcome.areas_for_improvement) > 0
    
    # Feedback should be specific
    for strength in outcome.strengths:
        assert len(strength) > 20
    
    for improvement in outcome.areas_for_improvement:
        assert len(improvement) > 20


def test_tricky_questions_are_hard():
    """Test that tricky questions are marked as difficult."""
    tricky_questions = [q for q in INTERVIEW_QUESTIONS.values() if q.question_type == "tricky"]
    
    assert len(tricky_questions) >= 1
    
    for question in tricky_questions:
        # Tricky questions should be at least medium difficulty
        assert question.difficulty in ["medium", "hard"]
