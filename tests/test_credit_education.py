"""
Tests for credit card educational content in explanations and mini-lessons.
"""

import pytest
from catalogs.explanations import (
    get_explanation,
    get_contextual_explanation,
    FINANCIAL_EXPLANATIONS
)
from catalogs.mini_lessons import (
    get_lesson,
    MINI_LESSONS,
    LessonCategory
)

# Test Credit Card Explanations
def test_credit_card_explanations_exist():
    """Test that credit card explanations are in catalog."""
    credit_topics = [
        "credit_card_basics",
        "credit_score_building",
        "apr_explained",
        "credit_utilization"
    ]
    
    for topic in credit_topics:
        assert topic in FINANCIAL_EXPLANATIONS, f"Missing explanation: {topic}"

def test_credit_card_basics_explanation():
    """Test credit card basics explanation structure."""
    explanation = get_explanation("financial", "credit_card_basics")
    
    assert explanation is not None
    assert "title" in explanation
    assert "short" in explanation
    assert "long" in explanation
    assert "example" in explanation
    assert "tip" in explanation
    assert "real_impact" in explanation
    
    # Check content quality
    assert "$1,000" in explanation["example"]
    assert "interest" in explanation["example"].lower()
    
    # Check real impact has scenarios
    impact = explanation["real_impact"]
    assert "pay_full" in impact
    assert "minimum_only" in impact

def test_credit_score_explanation():
    """Test credit score explanation content."""
    explanation = get_explanation("financial", "credit_score_building")
    
    assert "300-850" in explanation["long"]
    assert "Payment history" in explanation["long"]
    
    # Should explain the score factors
    assert "35%" in explanation["long"]  # Payment history percentage
    
    # Real impact should have different score tiers
    impact = explanation["real_impact"]
    assert "excellent_740plus" in impact
    assert "poor_below_620" in impact
    
    # Check concrete financial impact
    assert "$" in str(impact.values())  # Should mention dollar amounts

def test_apr_explanation():
    """Test APR explanation."""
    explanation = get_explanation("financial", "apr_explained")
    
    assert "APR" in explanation["title"]
    assert "rate" in explanation["long"].lower() or "borrow" in explanation["long"].lower()
    assert "%" in explanation["example"]
    
    # Should show different APR scenarios
    assert "15%" in explanation["example"] or "15" in explanation["example"]
    assert "20%" in explanation["example"] or "20" in explanation["example"]
    
    # Should warn about compound effects
    impact = explanation["real_impact"]
    assert len(impact) >= 3  # Should have multiple APR tiers

def test_credit_utilization_explanation():
    """Test credit utilization explanation."""
    explanation = get_explanation("financial", "credit_utilization")
    
    assert "30%" in explanation["short"] or "30%" in explanation["long"]
    assert "credit limit" in explanation["long"].lower()
    
    # Should give concrete examples
    assert "$" in explanation["example"]
    assert "1,000" in explanation["example"] or "1000" in explanation["example"]
    
    # Impact should show different utilization levels
    impact = explanation["real_impact"]
    assert "under_10" in impact
    assert "over_50" in impact

# Test Credit Card Mini-Lessons
def test_credit_card_lessons_exist():
    """Test that credit card lessons are in catalog."""
    credit_lessons = [
        "credit_cards_101",
        "building_credit_score",
        "apr_and_interest",
        "credit_card_perks_lesson"
    ]
    
    for lesson_id in credit_lessons:
        assert lesson_id in MINI_LESSONS, f"Missing lesson: {lesson_id}"

def test_credit_cards_101_lesson():
    """Test credit cards 101 lesson structure and content."""
    lesson = get_lesson("credit_cards_101")
    
    assert lesson is not None
    assert lesson["category"] == LessonCategory.FINANCE
    assert lesson["title"] == "Credit Cards: Tool or Trap?"
    
    # Check content
    content = lesson["content"]
    assert "GOLDEN RULE" in content
    assert "Pay FULL balance" in content or "pay full balance" in content.lower()
    assert "$1,000" in content
    assert "interest" in content.lower()
    
    # Check duration is reasonable (30-60 seconds)
    assert 30 <= lesson["duration_seconds"] <= 90
    
    # Check educational elements
    assert "key_takeaway" in lesson
    assert len(lesson["key_takeaway"]) > 20

def test_building_credit_score_lesson():
    """Test credit score building lesson."""
    lesson = get_lesson("building_credit_score")
    
    assert lesson is not None
    content = lesson["content"]
    
    # Should explain what affects credit score
    assert "Payment history" in content
    assert "35%" in content
    
    # Should provide actionable steps
    assert "payment" in content.lower()
    assert "score" in content.lower()
    
    # Should mention concrete benefits
    assert "$" in content  # Financial impact
    
    # Should unlock at reasonable time
    assert lesson["unlocks_after_semester"] <= 4

def test_apr_lesson():
    """Test APR lesson content."""
    lesson = get_lesson("apr_and_interest")
    
    content = lesson["content"]
    
    # Should define APR
    assert "APR" in content
    assert "Annual Percentage Rate" in content
    
    # Should show real comparison
    assert "$2,000" in content or "$2000" in content
    assert "15%" in content
    assert "25%" in content
    
    # Should show difference in total cost
    assert "$2,150" in content or "$2150" in content
    assert "$2,425" in content or "$2425" in content
    
    # Should provide strategy
    assert "strategy" in content.lower() or "tip" in lesson

def test_credit_card_perks_lesson():
    """Test credit card perks lesson."""
    lesson = get_lesson("credit_card_perks_lesson")
    
    content = lesson["content"]
    
    # Should discuss perks
    assert "perk" in content.lower()
    assert "cashback" in content.lower()
    
    # Should show math of perks vs interest
    assert "interest" in content.lower()
    assert "$" in content
    
    # Should warn about the catch
    assert "NET:" in content or "net" in content.lower()
    
    # Should provide decision framework
    assert "strategy" in content.lower() or "disciplined" in content.lower()

def test_lessons_progressive_unlock():
    """Test that credit card lessons unlock progressively."""
    credit_lessons = [
        "credit_cards_101",
        "building_credit_score",
        "apr_and_interest",
        "credit_card_perks_lesson"
    ]
    
    unlock_semesters = []
    for lesson_id in credit_lessons:
        lesson = get_lesson(lesson_id)
        unlock_semesters.append(lesson["unlocks_after_semester"])
    
    # Should unlock in reasonable progression
    assert min(unlock_semesters) >= 2  # Not too early
    assert max(unlock_semesters) <= 6  # Not too late
    
    # Should be somewhat ordered (basics before advanced)
    assert unlock_semesters[0] <= unlock_semesters[3]  # 101 before perks

def test_lessons_duration_appropriate():
    """Test that credit card lessons have appropriate duration."""
    credit_lessons = ["credit_cards_101", "building_credit_score", "apr_and_interest", "credit_card_perks_lesson"]
    
    for lesson_id in credit_lessons:
        lesson = get_lesson(lesson_id)
        # Should be short enough to be digestible (30-60 seconds target)
        assert 30 <= lesson["duration_seconds"] <= 90, f"Lesson {lesson_id} has inappropriate duration"

def test_educational_quality():
    """Test that credit card education is high quality."""
    credit_lessons = ["credit_cards_101", "building_credit_score", "apr_and_interest", "credit_card_perks_lesson"]
    
    for lesson_id in credit_lessons:
        lesson = get_lesson(lesson_id)
        content = lesson["content"]
        
        # Should have substantial content
        assert len(content) > 200, f"Lesson {lesson_id} has thin content"
        
        # Should include concrete numbers/examples
        assert "$" in content, f"Lesson {lesson_id} lacks concrete examples"
        
        # Should have actionable advice
        key_takeaway = lesson["key_takeaway"]
        assert len(key_takeaway) > 15, f"Lesson {lesson_id} has weak takeaway"

def test_explanations_link_to_lessons():
    """Test that explanations and lessons cover similar topics."""
    # Topics covered in explanations
    explanation_topics = {
        "credit_card_basics": ["pay full", "interest", "minimum"],
        "credit_score_building": ["payment history", "score", "300-850"],
        "apr_explained": ["APR", "percentage", "interest rate"],
        "credit_utilization": ["30%", "credit limit", "utilization"]
    }
    
    # Topics covered in lessons
    lesson_topics = {
        "credit_cards_101": ["full balance", "interest", "golden rule"],
        "building_credit_score": ["payment history", "score", "credit"],
        "apr_and_interest": ["APR", "percentage", "rate"],
        "credit_card_perks_lesson": ["perks", "cashback", "interest"]
    }
    
    # Verify explanations cover their topics
    for exp_key, keywords in explanation_topics.items():
        explanation = get_explanation("financial", exp_key)
        combined_text = (explanation.get("short", "") + " " + explanation.get("long", "")).lower()
        
        matched = sum(1 for kw in keywords if kw.lower() in combined_text)
        assert matched >= 2, f"Explanation {exp_key} doesn't cover enough key topics"
    
    # Verify lessons cover their topics
    for lesson_id, keywords in lesson_topics.items():
        lesson = get_lesson(lesson_id)
        combined_text = (lesson.get("content", "") + " " + lesson.get("key_takeaway", "")).lower()
        
        matched = sum(1 for kw in keywords if kw.lower() in combined_text)
        assert matched >= 2, f"Lesson {lesson_id} doesn't cover enough key topics"

def test_real_world_examples():
    """Test that content includes real-world dollar examples."""
    # Check explanations
    credit_explanations = ["credit_card_basics", "credit_score_building", "apr_explained"]
    
    for exp_key in credit_explanations:
        explanation = get_explanation("financial", exp_key)
        example = explanation.get("example", "")
        
        # Should have concrete dollar amounts
        assert "$" in example, f"Explanation {exp_key} lacks dollar examples"
        assert any(char.isdigit() for char in example), f"Explanation {exp_key} lacks numbers"
    
    # Check lessons
    credit_lessons = ["credit_cards_101", "building_credit_score", "apr_and_interest"]
    
    for lesson_id in credit_lessons:
        lesson = get_lesson(lesson_id)
        content = lesson["content"]
        
        # Should have real numbers
        assert "$" in content, f"Lesson {lesson_id} lacks dollar examples"
        assert any(char.isdigit() for char in content), f"Lesson {lesson_id} lacks numbers"

def test_warnings_present():
    """Test that content includes appropriate warnings."""
    # All credit card explanations should have warnings
    credit_topics = ["credit_card_basics", "apr_explained"]
    
    for topic in credit_topics:
        explanation = get_explanation("financial", topic)
        combined = (explanation.get("short", "") + " " + 
                   explanation.get("long", "") + " " + 
                   explanation.get("tip", "")).lower()
        
        # Should warn about risks
        warning_words = ["avoid", "dangerous", "careful", "trap", "warning", "expensive"]
        has_warning = any(word in combined for word in warning_words)
        assert has_warning, f"Explanation {topic} lacks warnings"
    
    # Lessons should also include cautions
    for lesson_id in ["credit_cards_101", "apr_and_interest"]:
        lesson = get_lesson(lesson_id)
        content = lesson["content"].lower()
        
        warning_words = ["trap", "avoid", "never", "expensive", "careful"]
        has_warning = any(word in content for word in warning_words)
        assert has_warning, f"Lesson {lesson_id} lacks warnings"

def test_positive_actionable_advice():
    """Test that content includes positive, actionable advice."""
    # Check explanations give tips
    for topic in ["credit_card_basics", "credit_score_building", "apr_explained"]:
        explanation = get_explanation("financial", topic)
        tip = explanation.get("tip", "")
        
        assert len(tip) > 20, f"Explanation {topic} has weak tip"
        
        # Should be actionable (contains verbs)
        action_words = ["get", "pay", "set", "keep", "start", "use", "build", "apply", "compare"]
        has_action = any(word in tip.lower() for word in action_words)
        assert has_action, f"Explanation {topic} tip not actionable: {tip}"
    
    # Check lessons have takeaways
    for lesson_id in ["credit_cards_101", "building_credit_score", "apr_and_interest"]:
        lesson = get_lesson(lesson_id)
        takeaway = lesson["key_takeaway"]
        
        assert len(takeaway) > 15, f"Lesson {lesson_id} has weak takeaway"
