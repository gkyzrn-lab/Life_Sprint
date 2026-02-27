"""Credit score system for Life Sprint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class CreditAccount:
    """Represents a credit account (card, loan, etc.)."""

    account_id: str
    account_type: str
    credit_limit: float
    current_balance: float
    payment_status: str = "current"

    @property
    def utilization_ratio(self) -> float:
        if self.credit_limit <= 0:
            return 0.0
        return round(self.current_balance / self.credit_limit, 2)


@dataclass
class CreditProfile:
    """Represents a player's credit profile."""

    player_id: str
    credit_score: int
    accounts: List[CreditAccount] = field(default_factory=list)
    history: List[Dict[str, Any]] = field(default_factory=list)
    age_months: int = 0


@dataclass
class CreditScoreBreakdown:
    """Detailed breakdown of credit score."""

    total_score: int
    payment_history: int
    credit_utilization: int
    length_of_history: int
    credit_mix: int
    hard_inquiries: int
    component_breakdown: Dict[str, Any]


CREDIT_SCORE_RANGES = {
    "poor": {"min": 300, "max": 579, "mortgage_apr": "6.5%+"},
    "fair": {"min": 580, "max": 669, "mortgage_apr": "5.0-6.5%"},
    "good": {"min": 670, "max": 699, "mortgage_apr": "4.0-5.0%"},
    "very_good": {"min": 700, "max": 749, "mortgage_apr": "3.0-4.0%"},
    "excellent": {"min": 750, "max": 850, "mortgage_apr": "2.5-3.0%"},
}


CREDIT_MYTHS: Dict[str, Dict[str, str]] = {
    "myth_checking_hurts_score": {
        "myth": "Checking your own credit score hurts your credit.",
        "fact": "FALSE. Checking your own score is a soft inquiry and does not hurt.",
    },
    "myth_no_credit_best": {
        "myth": "Having no credit is better than having bad credit.",
        "fact": "FALSE. No credit history still makes approvals difficult.",
    },
    "myth_carry_balance": {
        "myth": "You should carry a balance to build credit.",
        "fact": "FALSE. Paying in full builds credit without interest.",
    },
    "myth_closed_accounts": {
        "myth": "Closing old cards always helps your score.",
        "fact": "FALSE. Closing cards can hurt utilization and account age.",
    },
    "myth_hard_inquiry_impact": {
        "myth": "Hard inquiries have a massive long-term impact.",
        "fact": "They cause a small short-term dip that fades over time.",
    },
    "myth_income_affects_credit": {
        "myth": "Your income affects your credit score.",
        "fact": "FALSE. Scores are based on credit behavior, not income.",
    },
    "myth_credit_repair": {
        "myth": "Credit repair companies can erase accurate negative info.",
        "fact": "FALSE. Accurate negative info stays for years.",
    },
    "myth_divorce_credit": {
        "myth": "Divorce removes shared credit responsibility.",
        "fact": "FALSE. You must refinance or remove names explicitly.",
    },
    "myth_debt_disappear": {
        "myth": "Negative items disappear after 3 years.",
        "fact": "FALSE. Most negatives stay for 7 years.",
    },
    "myth_paying_old_debt": {
        "myth": "Paying old debt always boosts your score immediately.",
        "fact": "It can help long-term but not always immediately.",
    },
}


CREDIT_ACTIONS_DATABASE: Dict[str, Dict[str, float]] = {
    "on_time_payment": {"score_impact": 5},
    "missed_payment_30": {"score_impact": -100},
    "missed_payment_60": {"score_impact": -150},
    "missed_payment_90": {"score_impact": -200},
    "hard_inquiry": {"score_impact": -7},
    "new_credit_account": {"score_impact": -10},
    "paid_collections": {"score_impact": 20},
    "dispute_removed": {"score_impact": 15},
    "charge_off": {"score_impact": -200},
}


def _clamp_score(score: int) -> int:
    return max(300, min(850, score))


def create_credit_profile(player_id: str, starting_score: Optional[int] = None) -> CreditProfile:
    if starting_score is None:
        starting_score = 680
    return CreditProfile(player_id=player_id, credit_score=_clamp_score(int(starting_score)))


def apply_credit_action(profile: CreditProfile, action_id: str) -> CreditProfile:
    action = CREDIT_ACTIONS_DATABASE.get(action_id)
    if not action:
        return profile

    delta = int(action["score_impact"])
    profile.credit_score = _clamp_score(profile.credit_score + delta)
    profile.history.append({"action": action_id, "score_change": delta})
    return profile


def calculate_credit_score(profile: CreditProfile) -> int:
    return _clamp_score(profile.credit_score)


def get_credit_score_breakdown(profile: CreditProfile) -> CreditScoreBreakdown:
    payment_history = 80
    payment_history -= 15 * sum(1 for h in profile.history if "missed_payment" in h["action"])
    payment_history = max(0, min(100, payment_history))

    utilization = 80
    if profile.accounts:
        avg_util = sum(a.utilization_ratio for a in profile.accounts) / len(profile.accounts)
        utilization = int(max(0, min(100, 100 - (avg_util * 100))))

    length = min(100, 20 + (profile.age_months // 6))

    mix_types = {a.account_type for a in profile.accounts}
    credit_mix = min(100, 40 + (len(mix_types) * 15))

    inquiries = 90 - 5 * sum(1 for h in profile.history if h["action"] == "hard_inquiry")
    inquiries = max(0, min(100, inquiries))

    component_breakdown = {
        "payment_history": payment_history,
        "credit_utilization": utilization,
        "age_of_credit": length,
        "credit_mix": credit_mix,
        "inquiries": inquiries,
    }

    return CreditScoreBreakdown(
        total_score=profile.credit_score,
        payment_history=payment_history,
        credit_utilization=utilization,
        length_of_history=length,
        credit_mix=credit_mix,
        hard_inquiries=inquiries,
        component_breakdown=component_breakdown,
    )


def get_credit_improvement_tips(profile: CreditProfile) -> List[str]:
    score = profile.credit_score
    tips: List[str] = []

    if score < 580:
        tips.extend(
            [
                "Pay all bills on time and set up autopay to avoid misses.",
                "Reduce utilization below 30% by paying down balances.",
                "Dispute any errors on your credit report promptly.",
            ]
        )
    elif score < 700:
        tips.extend(
            [
                "Keep utilization under 30% and aim for under 10% if possible.",
                "Pay more than the minimum to reduce balances faster.",
                "Limit new credit applications to avoid extra inquiries.",
            ]
        )
    else:
        tips.extend(
            [
                "Keep older accounts open to maintain credit history length.",
                "Monitor your credit for errors and review reports regularly.",
                "Use credit lightly and pay in full each month.",
            ]
        )

    return tips
