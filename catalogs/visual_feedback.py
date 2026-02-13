"""
Visual feedback, progress tracking, and analytics for player dashboard.
Provides clear indicators of player's status and progression.
"""

from typing import Dict, List
from datetime import datetime
from pydantic import BaseModel

class ProgressIndicator(BaseModel):
    """Visual progress bar/indicator."""
    current: float
    maximum: float
    percentage: float
    status: str  # "low", "medium", "good", "excellent", "critical"
    trend: str  # "improving", "stable", "declining"
    color: str  # For UI - "green", "yellow", "orange", "red"

class Milestone(BaseModel):
    """Achievement milestone."""
    id: str
    name: str
    completed: bool
    date_completed: str = None
    reward: str = None

def calculate_progress_indicator(current: float, maximum: float, thresholds: Dict = None) -> ProgressIndicator:
    """
    Calculate a progress indicator with status and color.
    
    Args:
        current: Current value
        maximum: Maximum value
        thresholds: Dict with "excellent", "good", "medium", "low" percentage thresholds
    
    Returns:
        ProgressIndicator object
    """
    if thresholds is None:
        thresholds = {
            "excellent": 0.8,
            "good": 0.6,
            "medium": 0.4,
            "low": 0.2,
            "critical": 0.0
        }
    
    percentage = (current / maximum) if maximum > 0 else 0.0
    percentage = max(0.0, min(1.0, percentage))
    
    # Determine status
    if percentage >= thresholds["excellent"]:
        status, color = "excellent", "green"
    elif percentage >= thresholds["good"]:
        status, color = "good", "lightgreen"
    elif percentage >= thresholds["medium"]:
        status, color = "medium", "yellow"
    elif percentage >= thresholds["low"]:
        status, color = "low", "orange"
    else:
        status, color = "critical", "red"
    
    return ProgressIndicator(
        current=current,
        maximum=maximum,
        percentage=percentage,
        status=status,
        trend="stable",  # Can be calculated from history
        color=color
    )

def get_player_dashboard(player_state: Dict) -> Dict:
    """
    Generate comprehensive player dashboard with all visual indicators.
    
    Args:
        player_state: Current player state
    
    Returns:
        Dashboard dict with all progress indicators
    """
    dashboard = {
        "academic": {},
        "financial": {},
        "health": {},
        "social": {},
        "career": {},
        "overall": {}
    }
    
    # Academic Progress
    gpa = player_state.get("gpa", 0.0)
    dashboard["academic"]["gpa"] = calculate_progress_indicator(
        current=gpa,
        maximum=4.0,
        thresholds={"excellent": 0.9, "good": 0.8, "medium": 0.7, "low": 0.6, "critical": 0.0}
    ).model_dump()
    
    completed_credits = player_state.get("completed_credits", 0)
    required_credits = player_state.get("required_credits", 120)
    dashboard["academic"]["credits"] = calculate_progress_indicator(
        current=completed_credits,
        maximum=required_credits
    ).model_dump()
    
    # Financial Health
    balance = player_state.get("balance", 0)
    dashboard["financial"]["balance"] = {
        "current": balance,
        "status": "good" if balance > 1000 else "low" if balance > 0 else "critical",
        "color": "green" if balance > 1000 else "orange" if balance > 0 else "red"
    }
    
    debt = player_state.get("total_debt", 0)
    dashboard["financial"]["debt"] = {
        "current": debt,
        "status": "excellent" if debt == 0 else "good" if debt < 20000 else "medium" if debt < 40000 else "critical",
        "color": "green" if debt == 0 else "lightgreen" if debt < 20000 else "yellow" if debt < 40000 else "red",
        "monthly_payment": player_state.get("monthly_payment_estimate", 0)
    }
    
    # Emergency Fund
    emergency_fund = player_state.get("emergency_fund", 0)
    months_expenses_saved = emergency_fund / player_state.get("monthly_expenses", 1500)
    dashboard["financial"]["emergency_fund"] = {
        "current": emergency_fund,
        "months_covered": round(months_expenses_saved, 1),
        "status": "excellent" if months_expenses_saved >= 6 else "good" if months_expenses_saved >= 3 else "medium" if months_expenses_saved >= 1 else "critical",
        "color": "green" if months_expenses_saved >= 6 else "lightgreen" if months_expenses_saved >= 3 else "yellow" if months_expenses_saved >= 1 else "red"
    }
    
    # Health & Wellness
    stress = player_state.get("stress", 50)
    dashboard["health"]["stress"] = calculate_progress_indicator(
        current=100 - stress,  # Invert so higher is better
        maximum=100,
        thresholds={"excellent": 0.7, "good": 0.5, "medium": 0.3, "low": 0.2, "critical": 0.0}
    ).model_dump()
    
    # Physical health
    health = player_state.get("health", 80)
    dashboard["health"]["physical"] = calculate_progress_indicator(
        current=health,
        maximum=100
    ).model_dump()
    
    # Sleep
    sleep_hours = player_state.get("average_sleep_hours", 7)
    dashboard["health"]["sleep"] = {
        "current": sleep_hours,
        "status": "excellent" if 7 <= sleep_hours <= 9 else "good" if 6 <= sleep_hours <= 10 else "low",
        "color": "green" if 7 <= sleep_hours <= 9 else "yellow" if 6 <= sleep_hours <= 10 else "red"
    }
    
    # Social Life
    friendships = player_state.get("close_friends", 0)
    dashboard["social"]["friendships"] = {
        "count": friendships,
        "status": "excellent" if friendships >= 5 else "good" if friendships >= 3 else "medium" if friendships >= 1 else "low",
        "color": "green" if friendships >= 5 else "lightgreen" if friendships >= 3 else "yellow" if friendships >= 1 else "orange"
    }
    
    network = player_state.get("professional_network", 0)
    dashboard["social"]["network"] = {
        "count": network,
        "status": "excellent" if network >= 50 else "good" if network >= 20 else "medium" if network >= 5 else "low",
        "color": "green" if network >= 50 else "lightgreen" if network >= 20 else "yellow" if network >= 5 else "orange"
    }
    
    # Career Readiness
    internships = player_state.get("internships_completed", 0)
    dashboard["career"]["internships"] = {
        "count": internships,
        "status": "excellent" if internships >= 2 else "good" if internships >= 1 else "low",
        "color": "green" if internships >= 2 else "yellow" if internships >= 1 else "red"
    }
    
    resume_strength = player_state.get("resume_strength", 0)
    dashboard["career"]["resume"] = calculate_progress_indicator(
        current=resume_strength,
        maximum=100
    ).model_dump()
    
    # Overall Score
    overall_score = calculate_overall_score(player_state)
    dashboard["overall"]["score"] = overall_score
    dashboard["overall"]["rating"] = get_overall_rating(overall_score)
    dashboard["overall"]["color"] = get_rating_color(overall_score)
    
    return dashboard

def calculate_overall_score(player_state: Dict) -> float:
    """
    Calculate an overall "life score" from 0-100.
    Weighted combination of all life areas.
    """
    weights = {
        "academic": 0.25,
        "financial": 0.25,
        "health": 0.20,
        "social": 0.15,
        "career": 0.15
    }
    
    scores = {}
    
    # Academic (0-100)
    gpa = player_state.get("gpa", 0.0)
    scores["academic"] = (gpa / 4.0) * 100
    
    # Financial (0-100)
    debt = player_state.get("total_debt", 0)
    balance = player_state.get("balance", 0)
    emergency_fund = player_state.get("emergency_fund", 0)
    
    # Lower debt is better
    debt_score = max(0, 100 - (debt / 1000))  # Lose 1 point per $1K debt
    balance_score = min(100, (balance / 100))  # Gain 1 point per $100, cap at 100
    ef_score = min(100, (emergency_fund / 50))  # Gain 1 point per $50, cap at 100
    
    scores["financial"] = (debt_score + balance_score + ef_score) / 3
    
    # Health (0-100)
    stress = player_state.get("stress", 50)
    health = player_state.get("health", 80)
    sleep = player_state.get("average_sleep_hours", 7)
    
    stress_score = 100 - stress
    health_score = health
    sleep_score = 100 if 7 <= sleep <= 9 else 70 if 6 <= sleep <= 10 else 40
    
    scores["health"] = (stress_score + health_score + sleep_score) / 3
    
    # Social (0-100)
    friends = player_state.get("close_friends", 0)
    network = player_state.get("professional_network", 0)
    
    friend_score = min(100, friends * 20)  # 5 friends = 100
    network_score = min(100, network * 2)  # 50 connections = 100
    
    scores["social"] = (friend_score + network_score) / 2
    
    # Career (0-100)
    internships = player_state.get("internships_completed", 0)
    resume = player_state.get("resume_strength", 0)
    
    internship_score = min(100, internships * 50)  # 2 internships = 100
    resume_score = resume
    
    scores["career"] = (internship_score + resume_score) / 2
    
    # Weighted average
    overall = sum(scores[area] * weights[area] for area in weights)
    
    return round(overall, 1)

def get_overall_rating(score: float) -> str:
    """Convert overall score to rating."""
    if score >= 90:
        return "🌟 Exceptional - You're crushing it!"
    elif score >= 80:
        return "🎉 Excellent - Great balance and success"
    elif score >= 70:
        return "👍 Good - Solid progress, room to improve"
    elif score >= 60:
        return "😐 Fair - Some areas need attention"
    elif score >= 50:
        return "😟 Struggling - Multiple challenges"
    else:
        return "😰 Crisis Mode - Seek help immediately"

def get_rating_color(score: float) -> str:
    """Get color for overall rating."""
    if score >= 80:
        return "green"
    elif score >= 70:
        return "lightgreen"
    elif score >= 60:
        return "yellow"
    elif score >= 50:
        return "orange"
    else:
        return "red"

def get_semester_summary(player_state: Dict, semester: int) -> Dict:
    """
    Generate end-of-semester summary with highlights and lowlights.
    """
    return {
        "semester": semester,
        "highlights": [
            "Raised GPA to 3.6 (+0.3)" if player_state.get("gpa_improved") else None,
            "Landed amazing internship" if player_state.get("got_internship") else None,
            "Made 3 new close friends" if player_state.get("social_growth") else None,
            "Saved $2,000 this semester" if player_state.get("savings_growth") else None,
            "Joined fitness program, feeling great" if player_state.get("health_improvement") else None
        ],
        "challenges": [
            "Struggled with stress (avg 75)" if player_state.get("stress", 0) > 70 else None,
            "Ran into financial trouble" if player_state.get("balance", 0) < 0 else None,
            "GPA dropped to 2.8" if player_state.get("gpa_declined") else None,
            "Lost touch with friends" if player_state.get("social_decline") else None
        ],
        "achievements_unlocked": player_state.get("new_achievements", []),
        "lessons_learned": player_state.get("lessons_viewed", [])
    }

def get_graduation_report_card(player_state: Dict) -> Dict:
    """
    Generate final report card at graduation.
    Comprehensive summary of 4-year journey.
    """
    return {
        "final_stats": {
            "gpa": player_state.get("final_gpa", 0.0),
            "total_debt": player_state.get("total_debt", 0),
            "savings": player_state.get("balance", 0),
            "close_friends": player_state.get("close_friends", 0),
            "professional_network": player_state.get("professional_network", 0),
            "internships": player_state.get("internships_completed", 0)
        },
        "grades": {
            "academic": get_letter_grade(player_state.get("final_gpa", 0.0) / 4.0),
            "financial": get_financial_grade(player_state),
            "health": get_health_grade(player_state),
            "social": get_social_grade(player_state),
            "career": get_career_grade(player_state),
            "overall": get_letter_grade(calculate_overall_score(player_state) / 100)
        },
        "achievements": player_state.get("achievements_earned", []),
        "life_lessons_learned": player_state.get("total_lessons_viewed", 0),
        "memorable_moments": player_state.get("memorable_events", []),
        "regrets": player_state.get("missed_opportunities", []),
        "post_graduation_outlook": generate_outlook(player_state)
    }

def get_letter_grade(percentage: float) -> str:
    """Convert percentage to letter grade."""
    if percentage >= 0.93:
        return "A"
    elif percentage >= 0.90:
        return "A-"
    elif percentage >= 0.87:
        return "B+"
    elif percentage >= 0.83:
        return "B"
    elif percentage >= 0.80:
        return "B-"
    elif percentage >= 0.77:
        return "C+"
    elif percentage >= 0.73:
        return "C"
    elif percentage >= 0.70:
        return "C-"
    elif percentage >= 0.67:
        return "D+"
    elif percentage >= 0.60:
        return "D"
    else:
        return "F"

def get_financial_grade(player_state: Dict) -> str:
    """Calculate financial literacy grade."""
    debt = player_state.get("total_debt", 0)
    savings = player_state.get("balance", 0)
    
    if debt == 0 and savings > 10000:
        return "A+"
    elif debt < 15000 and savings > 5000:
        return "A"
    elif debt < 25000 and savings > 2000:
        return "B+"
    elif debt < 35000:
        return "B"
    elif debt < 50000:
        return "C"
    else:
        return "D"

def get_health_grade(player_state: Dict) -> str:
    """Calculate health/wellness grade."""
    avg_stress = player_state.get("average_stress", 50)
    burnout_episodes = player_state.get("burnout_count", 0)
    
    if avg_stress < 40 and burnout_episodes == 0:
        return "A"
    elif avg_stress < 55 and burnout_episodes <= 1:
        return "B"
    elif avg_stress < 70:
        return "C"
    else:
        return "D"

def get_social_grade(player_state: Dict) -> str:
    """Calculate social life grade."""
    friends = player_state.get("close_friends", 0)
    network = player_state.get("professional_network", 0)
    
    if friends >= 5 and network >= 30:
        return "A"
    elif friends >= 3 and network >= 15:
        return "B"
    elif friends >= 1 or network >= 5:
        return "C"
    else:
        return "D"

def get_career_grade(player_state: Dict) -> str:
    """Calculate career readiness grade."""
    internships = player_state.get("internships_completed", 0)
    resume_strength = player_state.get("resume_strength", 0)
    
    if internships >= 2 and resume_strength >= 80:
        return "A"
    elif internships >= 1 and resume_strength >= 60:
        return "B"
    elif resume_strength >= 40:
        return "C"
    else:
        return "D"

def generate_outlook(player_state: Dict) -> str:
    """Generate post-graduation outlook narrative."""
    debt = player_state.get("total_debt", 0)
    gpa = player_state.get("final_gpa", 0.0)
    internships = player_state.get("internships_completed", 0)
    network = player_state.get("professional_network", 0)
    
    outlook_points = []
    
    if debt == 0:
        outlook_points.append("You're debt-free! Massive advantage in life choices.")
    elif debt < 20000:
        outlook_points.append("Low debt gives you flexibility in career choices.")
    elif debt > 50000:
        outlook_points.append("High debt will impact decisions for years. Focus on high-paying jobs.")
    
    if gpa >= 3.7:
        outlook_points.append("Excellent GPA opens doors to grad school and competitive jobs.")
    elif gpa >= 3.0:
        outlook_points.append("Solid GPA shows competence.")
    
    if internships >= 2:
        outlook_points.append("Multiple internships = top candidate status.")
    elif internships == 0:
        outlook_points.append("No internships means harder job search ahead.")
    
    if network >= 50:
        outlook_points.append("Strong network will generate opportunities for years.")
    
    return " ".join(outlook_points) if outlook_points else "Your college experience was... interesting. Good luck out there!"
