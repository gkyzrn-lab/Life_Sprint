# Life Purchases Service - Handle purchase transactions and effects
# This service manages player spending on real-life items

from typing import Dict, Optional, Tuple
from datetime import datetime

from core_domain.player.player_model import Player, HistoryEvent
from catalogs.life_purchases import get_purchase, LifePurchase, LIFE_PURCHASES


class PurchaseResult:
    """Result of a purchase attempt"""
    def __init__(
        self,
        success: bool,
        message: str,
        purchase: Optional[LifePurchase] = None,
        balance_before: float = 0.0,
        balance_after: float = 0.0,
        effects_applied: Dict[str, float] = None,
    ):
        self.success = success
        self.message = message
        self.purchase = purchase
        self.balance_before = balance_before
        self.balance_after = balance_after
        self.effects_applied = effects_applied or {}


class PurchaseLimitExceeded(Exception):
    """Raised when purchase limit for semester is exceeded"""
    pass


class InsufficientFunds(Exception):
    """Raised when player doesn't have enough money"""
    pass


class PurchaseNotFound(Exception):
    """Raised when purchase ID doesn't exist"""
    pass


def can_afford_purchase(player: Player, purchase: LifePurchase) -> bool:
    """Check if player has enough money for purchase"""
    return player.finance.balance >= purchase.cost


def get_purchase_count_this_semester(
    player: Player, purchase_id: str
) -> int:
    """Count how many times this purchase was made this semester"""
    count = 0
    for event in player.history:
        if event.semester == player.semester and event.label == f"purchase:{purchase_id}":
            count += 1
    return count


def check_purchase_limits(
    player: Player, purchase: LifePurchase
) -> Tuple[bool, Optional[str]]:
    """
    Check if purchase can be made (limits, availability, etc.)
    Returns (can_purchase, error_message)
    """
    # Check if player can afford it
    if player.finance.balance < purchase.cost:
        shortage = purchase.cost - player.finance.balance
        return False, f"Insufficient funds. Need ${shortage:.2f} more."

    # Check if purchase requires minimum semester
    if player.semester < purchase.requires_semester_min:
        return (
            False,
            f"This item is not available until semester {purchase.requires_semester_min}",
        )

    # Check one-time purchase (can only buy once total)
    if purchase.one_time:
        for event in player.history:
            if event.label == f"purchase:{purchase.purchase_id}":
                return False, f"You already own this. It's a one-time purchase."

    # Check max per semester
    if purchase.max_per_semester:
        count = get_purchase_count_this_semester(player, purchase.purchase_id)
        if count >= purchase.max_per_semester:
            return (
                False,
                f"You've reached the limit for this item ({purchase.max_per_semester} per semester).",
            )

    return True, None


def apply_purchase_effects(player: Player, purchase: LifePurchase) -> Dict[str, float]:
    """
    Apply the purchase effects to player stats.
    Returns dict of effects applied: {stat_name: change_amount}
    """
    effects_applied = {}

    for effect in purchase.effects:
        stat_name = effect.stat_name
        change = effect.change

        # Apply to different stat objects
        if stat_name == "stress":
            player.stats.stress = max(0, min(100, player.stats.stress + change))
            effects_applied["stress"] = change

        elif stat_name == "happiness":
            player.stats.happiness = max(0, min(100, player.stats.happiness + change))
            effects_applied["happiness"] = change

        elif stat_name == "eq":  # Emotional Quotient
            player.stats.eq = max(0, player.stats.eq + change)
            effects_applied["eq"] = change

        elif stat_name == "mental_health":
            player.health.mental_health = max(0, min(100, player.health.mental_health + change))
            effects_applied["mental_health"] = change

        elif stat_name == "fitness":
            player.health.fitness = max(0, min(100, player.health.fitness + change))
            effects_applied["fitness"] = change

        elif stat_name == "energy_level":
            player.stats.energy_level = max(0, min(100, player.stats.energy_level + change))
            effects_applied["energy_level"] = change

        elif stat_name == "sleep_quality":
            player.health.sleep_quality = max(0, min(100, player.health.sleep_quality + change))
            effects_applied["sleep_quality"] = change

        elif stat_name == "technical_skills":
            player.stats.technical_skills = max(0, min(100, player.stats.technical_skills + change))
            effects_applied["technical_skills"] = change

        elif stat_name == "communication_skills":
            player.stats.communication_skills = max(0, min(100, player.stats.communication_skills + change))
            effects_applied["communication_skills"] = change

        elif stat_name == "time_management":
            player.stats.time_management = max(0, min(100, player.stats.time_management + change))
            effects_applied["time_management"] = change

        elif stat_name == "business_acumen":
            player.stats.business_acumen = max(0, min(100, player.stats.business_acumen + change))
            effects_applied["business_acumen"] = change

    return effects_applied


def make_purchase(
    player: Player, purchase_id: str
) -> PurchaseResult:
    """
    Execute a purchase for the player.
    
    Returns PurchaseResult with success/failure details.
    """
    # Get the purchase item
    purchase = get_purchase(purchase_id)
    if not purchase:
        raise PurchaseNotFound(f"Purchase '{purchase_id}' not found")

    # Check purchase limits and eligibility
    can_purchase, error_msg = check_purchase_limits(player, purchase)
    if not can_purchase:
        return PurchaseResult(
            success=False,
            message=error_msg or "Cannot make this purchase",
            purchase=purchase,
            balance_before=player.finance.balance,
            balance_after=player.finance.balance,
        )

    # Execute the purchase
    balance_before = player.finance.balance
    player.finance.balance -= purchase.cost
    balance_after = player.finance.balance

    # Apply effects
    effects_applied = apply_purchase_effects(player, purchase)

    # Record in history (HistoryEvent.details must have numeric values)
    history_event = HistoryEvent(
        label=f"purchase:{purchase_id}",
        semester=player.semester,
        details={
            "cost": purchase.cost,
            "balance_before": balance_before,
            "balance_after": balance_after,
            **effects_applied,
        },
    )
    player.history.append(history_event)

    # Create success message
    effects_str = ", ".join(
        [f"{stat}: {change:+.1f}" for stat, change in effects_applied.items()]
    )
    message = f"✅ Purchased '{purchase.name}' for ${purchase.cost:.2f}. Effects: {effects_str}"

    return PurchaseResult(
        success=True,
        message=message,
        purchase=purchase,
        balance_before=balance_before,
        balance_after=balance_after,
        effects_applied=effects_applied,
    )


def get_player_purchase_history(player: Player) -> list:
    """Get all purchases made by player"""
    purchases = []
    for event in player.history:
        if event.label.startswith("purchase:"):
            purchases.append(event)
    return purchases


def suggest_purchases_for_player(player: Player) -> list:
    """
    Suggest purchases based on player's current stats.
    Returns list of (purchase, reason) tuples
    """
    suggestions = []

    # Suggest stress relief if stressed
    if player.stats.stress > 70:
        stress_relief = [
            p for p in LIFE_PURCHASES.values()
            if p.category in ["social", "wellness", "fun"]
        ]
        for p in stress_relief[:3]:
            suggestions.append((p, f"High stress ({player.stats.stress:.0f}) - try stress relief"))

    # Suggest happiness boost if unhappy
    if player.stats.happiness < 50:
        happiness_boosters = [
            p for p in LIFE_PURCHASES.values()
            if p.category in ["social", "fun"]
        ]
        for p in happiness_boosters[:2]:
            suggestions.append((p, f"Low happiness ({player.stats.happiness:.0f}) - try a fun activity"))

    # Suggest health if fitness is low
    if player.health.fitness < 40:
        health_items = [
            p for p in LIFE_PURCHASES.values()
            if p.category in ["health", "wellness"]
        ]
        for p in health_items[:2]:
            suggestions.append((p, f"Low fitness ({player.health.fitness:.0f}) - improve your health"))

    # Suggest mental health if needed
    if player.health.mental_health < 50:
        mental_health_items = [
            p for p in LIFE_PURCHASES.values()
            if p.category == "wellness"
        ]
        for p in mental_health_items[:2]:
            suggestions.append((p, f"Mental health low ({player.health.mental_health:.0f}) - seek support"))

    return suggestions[:5]  # Top 5 suggestions
