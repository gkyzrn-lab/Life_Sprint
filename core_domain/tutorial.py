"""
Tutorial and onboarding system for first-run players.

Defines tutorial steps, tooltips, and tracks which tutorials a player has seen.
"""

from __future__ import annotations
from typing import List, Dict, Optional
from enum import Enum
from pydantic import BaseModel, Field


class TutorialStep(BaseModel):
    """A single tutorial step with title, description, and context."""

    step_id: str  # e.g. "intro_welcome", "time_budget_explain"
    title: str
    description: str
    context: str  # where/when this step appears (e.g. "player_start", "semester_begin", "planning_page")
    priority: int = 0  # higher = shown earlier
    action_hint: Optional[str] = None  # UI hint for next action


class Tooltip(BaseModel):
    """A contextual tooltip for inline help."""

    tooltip_id: str
    label: str  # short label shown in UI (e.g. "What is GPA?")
    content: str  # longer explanation
    related_concept: str  # link to tutorial step, if any


class TutorialState(BaseModel):
    """Tracks which tutorials a player has seen."""

    completed_steps: List[str] = Field(default_factory=list)
    dismissed_tooltips: List[str] = Field(default_factory=list)
    tutorials_enabled: bool = True
    current_focus: Optional[str] = None  # e.g. "time_budget" or None


# ============================================================================
# Tutorial Library: Core Concepts
# ============================================================================

TUTORIAL_LIBRARY: Dict[str, TutorialStep] = {
    "intro_welcome": TutorialStep(
        step_id="intro_welcome",
        title="Welcome to Life Sprint!",
        description="You're about to embark on a journey through college and beyond. Your choices will shape your future—manage your time, finances, and health wisely.",
        context="player_start",
        priority=1000,
        action_hint="Click 'Next' to continue or 'Skip Tutorial' to start playing.",
    ),
    "time_budget_explain": TutorialStep(
        step_id="time_budget_explain",
        title="Understanding Your Time Budget",
        description=(
            "Each semester, you have a fixed number of hours. "
            "You must allocate time to: classes, studying, work, activities, and rest. "
            "Don't overcommit—burnout is real!"
        ),
        context="planning_page",
        priority=900,
        action_hint="You'll plan your semester time in the 'Plan' tab.",
    ),
    "loans_explained": TutorialStep(
        step_id="loans_explained",
        title="Student Loans & Financial Aid",
        description=(
            "Tuition costs money. You can pay out-of-pocket, get scholarships, or take loans. "
            "Loans have interest and must be repaid later. Choose wisely—debt compounds!"
        ),
        context="finance_page",
        priority=850,
        action_hint="Check your 'Finance' tab to see your balance and loan options.",
    ),
    "gpa_matters": TutorialStep(
        step_id="gpa_matters",
        title="GPA & Academic Progress",
        description=(
            "Your GPA affects scholarships, internships, and job prospects. "
            "High workload, stress, and poor sleep hurt your grades. Balance is key."
        ),
        context="academics_page",
        priority=800,
        action_hint="Study hard but don't sacrifice your health.",
    ),
    "stress_burnout": TutorialStep(
        step_id="stress_burnout",
        title="Stress & Burnout",
        description=(
            "Work too much without rest, and you'll burn out. Burned-out players lose focus, "
            "grades drop, and health suffers. Take breaks, maintain hobbies, and sleep well."
        ),
        context="planning_page",
        priority=750,
        action_hint="Monitor your stress level in the 'Stats' section.",
    ),
    "housing_tradeoffs": TutorialStep(
        step_id="housing_tradeoffs",
        title="Housing & Living Costs",
        description=(
            "Where you live affects your monthly expenses and well-being. "
            "Dorms are cheaper but crowded; off-campus housing is pricier but quieter. "
            "On-campus living can boost social life."
        ),
        context="player_start",
        priority=700,
        action_hint="Choose housing carefully—it's a major expense.",
    ),
    "work_study_balance": TutorialStep(
        step_id="work_study_balance",
        title="Work & Study Balance",
        description=(
            "A part-time job earns money but costs time. "
            "Too much work leaves no time for classes and studying. Too little means financial stress. "
            "Find your balance."
        ),
        context="job_selection",
        priority=650,
        action_hint="Consider a part-time job only if you can manage it.",
    ),
    "planning_ahead": TutorialStep(
        step_id="planning_ahead",
        title="Semester Planning",
        description=(
            "At the start of each semester, plan how you'll spend your time. "
            "Classes are mandatory, but decide how much time to study, work, and relax. "
            "Planning ahead prevents chaos."
        ),
        context="semester_begin",
        priority=600,
        action_hint="Fill out your semester plan before classes begin.",
    ),
}


# ============================================================================
# Tooltip Library: Inline Help
# ============================================================================

TOOLTIP_LIBRARY: Dict[str, Tooltip] = {
    "what_is_gpa": Tooltip(
        tooltip_id="what_is_gpa",
        label="What is GPA?",
        content=(
            "GPA (Grade Point Average) measures academic performance on a 0–4.0 scale. "
            "Higher GPA = better grades. It affects scholarships, internships, and job prospects."
        ),
        related_concept="gpa_matters",
    ),
    "what_is_stress": Tooltip(
        tooltip_id="what_is_stress",
        label="What is Stress?",
        content=(
            "Stress measures how overwhelmed you are. High stress from work, classes, or social pressure. "
            "If stress exceeds 100%, you burn out: health tanks, grades drop, and focus suffers."
        ),
        related_concept="stress_burnout",
    ),
    "what_is_balance": Tooltip(
        tooltip_id="what_is_balance",
        label="What is Cash Balance?",
        content=(
            "Your cash balance is how much money you have. "
            "Expenses reduce it, income (work) increases it. If it goes negative, you're in debt."
        ),
        related_concept="loans_explained",
    ),
    "interest_explained": Tooltip(
        tooltip_id="interest_explained",
        label="What is Loan Interest?",
        content=(
            "Interest is the cost of borrowing. If you take a $10k loan at 5% annual interest, "
            "you'll owe $10.5k after a year. The longer you carry the loan, the more interest accrues."
        ),
        related_concept="loans_explained",
    ),
    "what_is_network": Tooltip(
        tooltip_id="what_is_network",
        label="What is Network?",
        content=(
            "Network is your professional connections. Strong network opens doors for internships, jobs, and mentorship. "
            "You build network through work, activities, and socializing."
        ),
        related_concept="work_study_balance",
    ),
    "what_is_time_budget": Tooltip(
        tooltip_id="what_is_time_budget",
        label="What is Time Budget?",
        content=(
            "Time budget is the total hours available in a semester (usually ~730 hours). "
            "You must allocate it among classes, studying, work, activities, and sleep. "
            "Don't overcommit or you'll burn out."
        ),
        related_concept="time_budget_explain",
    ),
}


def get_tutorial_sequence() -> List[str]:
    """Return recommended tutorial steps in order (for first-time players)."""
    steps = [
        "intro_welcome",
        "time_budget_explain",
        "loans_explained",
        "housing_tradeoffs",
        "work_study_balance",
        "gpa_matters",
        "stress_burnout",
        "planning_ahead",
    ]
    return steps


def get_context_tutorials(context: str) -> List[TutorialStep]:
    """
    Get tutorials relevant to a specific context (e.g., "planning_page").
    Used to show contextual tips when player visits a page.
    """
    return [
        step for step in TUTORIAL_LIBRARY.values()
        if step.context == context
    ]


def get_tooltip(tooltip_id: str) -> Optional[Tooltip]:
    """Fetch a single tooltip by ID."""
    return TOOLTIP_LIBRARY.get(tooltip_id)


def get_all_tooltips() -> Dict[str, Tooltip]:
    """Get all available tooltips."""
    return TOOLTIP_LIBRARY.copy()
