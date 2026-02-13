"""Tests for scam detection mini-game."""

import pytest
from catalogs.scam_detection import (
    SCAM_SCENARIOS,
    SCAM_PREVENTION_TIPS,
    ScamDetectionResponse,
    get_random_scenario,
    get_scenarios_by_type,
    evaluate_scam_detection,
    get_random_prevention_tip_for_type,
    get_tip,
    get_all_tips,
    get_tips_by_category
)


def test_scam_scenarios_exist():
    """Test that scam scenarios are defined."""
    assert len(SCAM_SCENARIOS) > 0
    assert "phishing_easy_1" in SCAM_SCENARIOS
    assert "fake_job_easy" in SCAM_SCENARIOS


def test_scenario_structure():
    """Test that scenarios have required fields."""
    scenario = SCAM_SCENARIOS["phishing_easy_1"]
    
    assert scenario.scenario_id == "phishing_easy_1"
    assert scenario.scam_type in ["phishing_email", "fake_job", "romance_scam", "tech_support", 
                                   "investment_scam", "rental_scam", "scholarship_scam", "prize_notification"]
    assert scenario.difficulty in ["easy", "medium", "hard"]
    assert len(scenario.title) > 0
    assert len(scenario.sender) > 0
    assert len(scenario.content) > 50
    assert isinstance(scenario.is_scam, bool)
    assert len(scenario.why_scam_or_legit) > 0


def test_scam_has_red_flags():
    """Test that scam scenarios have red flags."""
    scenario = SCAM_SCENARIOS["phishing_easy_1"]
    
    assert scenario.is_scam is True
    assert len(scenario.red_flags) > 0
    # Should have multiple red flags
    assert len(scenario.red_flags) >= 3


def test_legitimate_scenario_structure():
    """Test that legitimate scenarios have proper signs."""
    scenario = SCAM_SCENARIOS["legitimate_email_1"]
    
    assert scenario.is_scam is False
    assert len(scenario.legitimate_signs) > 0
    assert len(scenario.red_flags) == 0  # Legitimate = no red flags


def test_get_random_scenario():
    """Test getting random scenarios."""
    scenario1 = get_random_scenario()
    assert scenario1 is not None
    assert scenario1.scenario_id in SCAM_SCENARIOS
    
    # Test difficulty filter
    easy_scenario = get_random_scenario(difficulty="easy")
    assert easy_scenario.difficulty == "easy"


def test_get_scenarios_by_type():
    """Test filtering scenarios by type."""
    phishing_scenarios = get_scenarios_by_type("phishing_email")
    assert len(phishing_scenarios) > 0
    assert all(s.scam_type == "phishing_email" for s in phishing_scenarios)
    
    job_scenarios = get_scenarios_by_type("fake_job")
    assert len(job_scenarios) > 0


def test_correct_scam_identification():
    """Test correctly identifying a scam."""
    scenario = SCAM_SCENARIOS["phishing_easy_1"]
    
    response = ScamDetectionResponse(
        player_verdict="scam",
        confidence="high",
        identified_red_flags=[
            "Multiple exclamation marks and ALL CAPS",
            "Creates artificial urgency (24 hours)",
            "Suspicious domain (chase-bank-security.net, not chase.com)"
        ]
    )
    
    result = evaluate_scam_detection(scenario, response, player_critical_thinking=70)
    
    assert result.correct is True
    assert result.actual_answer == "scam"
    assert result.score > 60
    assert result.scam_detection_skill_gained > 0
    assert len(result.explanation) > 0


def test_missing_red_flags_lowers_score():
    """Test that missing red flags reduces score."""
    scenario = SCAM_SCENARIOS["phishing_easy_1"]
    
    # Identify only 1 red flag out of many
    response_few = ScamDetectionResponse(
        player_verdict="scam",
        confidence="medium",
        identified_red_flags=["Multiple exclamation marks and ALL CAPS"]
    )
    
    # Identify multiple red flags
    response_many = ScamDetectionResponse(
        player_verdict="scam",
        confidence="high",
        identified_red_flags=[
            "Multiple exclamation marks and ALL CAPS",
            "Creates artificial urgency (24 hours)",
            "Suspicious domain (chase-bank-security.net, not chase.com)",
            "Generic greeting ('Dear Valued Customer')"
        ]
    )
    
    result_few = evaluate_scam_detection(scenario, response_few, player_critical_thinking=70)
    result_many = evaluate_scam_detection(scenario, response_many, player_critical_thinking=70)
    
    # More red flags = higher score
    assert result_many.score > result_few.score


def test_incorrect_scam_identification():
    """Test incorrectly identifying a scam as legitimate."""
    scenario = SCAM_SCENARIOS["phishing_easy_1"]
    
    response = ScamDetectionResponse(
        player_verdict="legitimate",
        confidence="high",
        identified_red_flags=[]
    )
    
    result = evaluate_scam_detection(scenario, response, player_critical_thinking=50)
    
    assert result.correct is False
    assert result.score < 30


def test_correctly_identifying_legitimate_email():
    """Test correctly identifying a legitimate email."""
    scenario = SCAM_SCENARIOS["legitimate_email_1"]
    
    response = ScamDetectionResponse(
        player_verdict="legitimate",
        confidence="high",
        identified_red_flags=[]
    )
    
    result = evaluate_scam_detection(scenario, response, player_critical_thinking=70)
    
    assert result.correct is True
    assert result.actual_answer == "legitimate"
    assert result.score > 60


def test_false_positive_on_legitimate():
    """Test incorrectly identifying legitimate as scam."""
    scenario = SCAM_SCENARIOS["legitimate_email_1"]
    
    response = ScamDetectionResponse(
        player_verdict="scam",
        confidence="medium",
        identified_red_flags=["Suspicious formatting"]
    )
    
    result = evaluate_scam_detection(scenario, response, player_critical_thinking=50)
    
    assert result.correct is False
    assert result.score < 30


def test_unsure_response():
    """Test that being unsure is better than being wrong."""
    scenario = SCAM_SCENARIOS["phishing_medium_1"]  # Harder to detect
    
    unsure_response = ScamDetectionResponse(
        player_verdict="unsure",
        confidence="low",
        identified_red_flags=[]
    )
    
    wrong_response = ScamDetectionResponse(
        player_verdict="legitimate",
        confidence="high",
        identified_red_flags=[]
    )
    
    result_unsure = evaluate_scam_detection(scenario, unsure_response, player_critical_thinking=50)
    result_wrong = evaluate_scam_detection(scenario, wrong_response, player_critical_thinking=50)
    
    # Being unsure should score higher than being confidently wrong
    assert result_unsure.score > result_wrong.score


def test_skill_affects_score():
    """Test that player's critical thinking skill affects score."""
    scenario = SCAM_SCENARIOS["phishing_easy_1"]
    
    response = ScamDetectionResponse(
        player_verdict="scam",
        confidence="high",
        identified_red_flags=["Multiple exclamation marks and ALL CAPS"]
    )
    
    result_low_skill = evaluate_scam_detection(scenario, response, player_critical_thinking=30)
    result_high_skill = evaluate_scam_detection(scenario, response, player_critical_thinking=90)
    
    # Higher skill = higher score for same response
    assert result_high_skill.score > result_low_skill.score


def test_phishing_easy_scenarios():
    """Test easy phishing scenarios are detectable."""
    easy_phishing = [s for s in SCAM_SCENARIOS.values() 
                     if s.scam_type == "phishing_email" and s.difficulty == "easy"]
    
    assert len(easy_phishing) > 0
    
    for scenario in easy_phishing:
        assert len(scenario.red_flags) >= 3  # Easy ones should have obvious flags
        assert "urgency" in str(scenario.red_flags).lower() or \
               "suspicious" in str(scenario.red_flags).lower() or \
               "domain" in str(scenario.red_flags).lower()


def test_sophisticated_phishing():
    """Test medium/hard phishing scenarios are more realistic."""
    scenario = SCAM_SCENARIOS["phishing_medium_1"]
    
    assert scenario.difficulty == "medium"
    assert len(scenario.legitimate_signs) > 0  # Has some realistic elements
    assert len(scenario.red_flags) > 0  # But still has red flags


def test_fake_job_scenarios():
    """Test fake job posting scenarios."""
    fake_jobs = get_scenarios_by_type("fake_job")
    
    assert len(fake_jobs) > 0
    
    for job in fake_jobs:
        if job.is_scam:
            # Should mention upfront fees as red flag
            red_flags_text = " ".join(job.red_flags).lower()
            assert "fee" in red_flags_text or "payment" in red_flags_text or "pay" in red_flags_text


def test_legitimate_job_posting():
    """Test legitimate job scenario."""
    scenario = SCAM_SCENARIOS["legitimate_job"]
    
    assert scenario.is_scam is False
    assert "No upfront fees" in str(scenario.legitimate_signs) or \
           "no fees" in str(scenario.legitimate_signs).lower()
    assert len(scenario.legitimate_signs) >= 5  # Should have many good signs


def test_romance_scam_red_flags():
    """Test romance scam scenarios."""
    scenario = SCAM_SCENARIOS["romance_scam_easy"]
    
    assert scenario.is_scam is True
    assert scenario.scam_type == "romance_scam"
    
    red_flags_text = " ".join(scenario.red_flags).lower()
    # Should mention money or video chat issues
    assert "money" in red_flags_text or "video" in red_flags_text or "remote" in red_flags_text


def test_tech_support_scam():
    """Test tech support scam scenario."""
    scenario = SCAM_SCENARIOS["tech_support_scam"]
    
    assert scenario.is_scam is True
    assert scenario.scam_type == "tech_support"
    
    # Should have urgency and fake phone number red flags
    red_flags_text = " ".join(scenario.red_flags).lower()
    assert "phone" in red_flags_text or "call" in red_flags_text
    assert "urgency" in red_flags_text or "urgent" in red_flags_text


def test_scholarship_scam():
    """Test scholarship scam scenario."""
    scenario = SCAM_SCENARIOS["scholarship_scam"]
    
    assert scenario.is_scam is True
    assert scenario.scam_type == "scholarship_scam"
    
    # Should mention application fee as red flag
    red_flags_text = " ".join(scenario.red_flags).lower()
    assert "fee" in red_flags_text


def test_investment_scam():
    """Test investment scam scenario."""
    scenario = SCAM_SCENARIOS["investment_scam_hard"]
    
    assert scenario.is_scam is True
    assert scenario.scam_type == "investment_scam"
    assert scenario.difficulty == "hard"
    
    # Should have legitimate-looking signs (sophisticated)
    assert len(scenario.legitimate_signs) > 0
    
    # But also clear red flags
    red_flags_text = " ".join(scenario.red_flags).lower()
    assert "return" in red_flags_text or "unrealistic" in red_flags_text


def test_prevention_tips_exist():
    """Test that prevention tips are defined."""
    assert len(SCAM_PREVENTION_TIPS) > 0
    assert "check_url" in SCAM_PREVENTION_TIPS
    assert "gift_cards_scam" in SCAM_PREVENTION_TIPS
    assert "never_pay_fees" in SCAM_PREVENTION_TIPS


def test_prevention_tip_structure():
    """Test prevention tip structure."""
    tip = SCAM_PREVENTION_TIPS["check_url"]
    
    assert tip.tip_id == "check_url"
    assert tip.category in ["email_safety", "job_hunting", "online_dating", "financial", "tech", "general"]
    assert len(tip.title) > 0
    assert len(tip.description) > 30
    assert len(tip.example) > 0
    assert tip.importance in ["low", "medium", "high", "critical"]


def test_critical_tips():
    """Test that critical tips are properly marked."""
    critical_tips = [t for t in SCAM_PREVENTION_TIPS.values() if t.importance == "critical"]
    
    assert len(critical_tips) >= 3
    
    # Gift cards should be critical
    gift_card_tip = SCAM_PREVENTION_TIPS["gift_cards_scam"]
    assert gift_card_tip.importance == "critical"


def test_get_tip():
    """Test retrieving specific tips."""
    tip = get_tip("check_url")
    assert tip is not None
    assert tip.tip_id == "check_url"
    
    # Non-existent tip
    assert get_tip("fake_tip_id") is None


def test_get_all_tips():
    """Test getting all tips."""
    tips = get_all_tips()
    assert len(tips) > 0
    assert len(tips) == len(SCAM_PREVENTION_TIPS)


def test_get_tips_by_category():
    """Test filtering tips by category."""
    email_tips = get_tips_by_category("email_safety")
    assert len(email_tips) > 0
    assert all(t.category == "email_safety" for t in email_tips)
    
    job_tips = get_tips_by_category("job_hunting")
    assert len(job_tips) > 0


def test_get_random_prevention_tip_for_type():
    """Test getting relevant tips for scam types."""
    phishing_tip = get_random_prevention_tip_for_type("phishing_email")
    assert phishing_tip is not None
    assert phishing_tip.category in ["email_safety", "general"]
    
    job_tip = get_random_prevention_tip_for_type("fake_job")
    assert job_tip is not None
    assert job_tip.category in ["job_hunting", "general"]


def test_red_flags_are_educational():
    """Test that red flags teach valuable lessons."""
    for scenario in SCAM_SCENARIOS.values():
        if scenario.is_scam:
            # Each red flag should be descriptive (not just "bad email")
            for flag in scenario.red_flags:
                assert len(flag) > 10  # Should be descriptive
                assert not flag.isupper()  # Not all caps


def test_scenarios_have_real_world_examples():
    """Test that scenarios include real-world context."""
    for scenario in SCAM_SCENARIOS.values():
        assert len(scenario.real_world_example) > 30
        # Should mention statistics or real impact
        assert any(word in scenario.real_world_example.lower() 
                  for word in ["million", "billion", "$", "2023", "2024", "ftc", "victims"])


def test_difficulty_progression():
    """Test that scenarios have varied difficulty."""
    easy_count = len([s for s in SCAM_SCENARIOS.values() if s.difficulty == "easy"])
    medium_count = len([s for s in SCAM_SCENARIOS.values() if s.difficulty == "medium"])
    hard_count = len([s for s in SCAM_SCENARIOS.values() if s.difficulty == "hard"])
    
    # Should have mix of difficulties
    assert easy_count > 0
    assert medium_count > 0
    # Hard scenarios are optional but good to have
    assert hard_count >= 0


def test_scam_types_diversity():
    """Test that multiple scam types are covered."""
    types = set(s.scam_type for s in SCAM_SCENARIOS.values())
    
    # Should cover multiple scam types
    assert "phishing_email" in types
    assert "fake_job" in types
    assert len(types) >= 4  # At least 4 different scam types


def test_evaluation_provides_feedback():
    """Test that evaluation gives useful feedback."""
    scenario = SCAM_SCENARIOS["phishing_easy_1"]
    
    response = ScamDetectionResponse(
        player_verdict="scam",
        confidence="high",
        identified_red_flags=["Multiple exclamation marks and ALL CAPS"]
    )
    
    result = evaluate_scam_detection(scenario, response, player_critical_thinking=50)
    
    assert len(result.explanation) > 50
    assert len(result.prevention_tip) > 30
    assert len(result.red_flags_missed) > 0  # Didn't catch all flags


def test_skill_gain_varies_by_difficulty():
    """Test that harder scenarios give more skill."""
    easy_scenario = SCAM_SCENARIOS["phishing_easy_1"]
    hard_scenario = SCAM_SCENARIOS["investment_scam_hard"]
    
    response = ScamDetectionResponse(
        player_verdict="scam",
        confidence="high",
        identified_red_flags=[]
    )
    
    easy_result = evaluate_scam_detection(easy_scenario, response, player_critical_thinking=50)
    hard_result = evaluate_scam_detection(hard_scenario, response, player_critical_thinking=50)
    
    # Hard scenarios should give more skill (when correct)
    if easy_result.correct and hard_result.correct:
        assert hard_result.scam_detection_skill_gained >= easy_result.scam_detection_skill_gained
