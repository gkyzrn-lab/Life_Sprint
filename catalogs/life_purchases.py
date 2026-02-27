# Life Purchases Store - Real-world spending items with life impact
# Players can spend money on items that affect their wellbeing, health, social life, and stress levels

from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class PurchaseEffect(BaseModel):
    """Effect of a purchase on player stats"""
    stat_name: str  # stress, happiness, mental_health, social_score, energy_level, fitness, etc.
    change: float  # positive or negative
    duration: Optional[int] = None  # None = permanent, number = weeks/duration


class LifePurchase(BaseModel):
    """A real-life purchase item the player can buy"""
    purchase_id: str
    name: str
    description: str
    category: str  # social, health, wellness, fun, practical, self-care
    cost: float
    effects: List[PurchaseEffect] = Field(default_factory=list)
    one_time: bool = True  # Can it be purchased repeatedly?
    max_per_semester: Optional[int] = None  # Limit purchases per semester
    emoji: str = "💰"
    requires_semester_min: int = 1  # Minimum semester to unlock


# ==================== LIFE PURCHASES CATALOG ====================

LIFE_PURCHASES: Dict[str, LifePurchase] = {
    # Social Activities
    "coffee_with_friends": LifePurchase(
        purchase_id="coffee_with_friends",
        name="Coffee with Friends",
        description="Grab coffee and catch up with friends. Reduce stress and build social connections.",
        category="social",
        cost=15.0,
        effects=[
            PurchaseEffect(stat_name="stress", change=-5),
            PurchaseEffect(stat_name="happiness", change=10),
            PurchaseEffect(stat_name="eq", change=2),
            PurchaseEffect(stat_name="mental_health", change=5),
        ],
        one_time=False,
        max_per_semester=4,
        emoji="☕",
    ),
    "dinner_with_friends": LifePurchase(
        purchase_id="dinner_with_friends",
        name="Dinner with Friends",
        description="Enjoy a nice dinner with friends. Great for stress relief and social bonding.",
        category="social",
        cost=40.0,
        effects=[
            PurchaseEffect(stat_name="stress", change=-8),
            PurchaseEffect(stat_name="happiness", change=15),
            PurchaseEffect(stat_name="eq", change=4),
            PurchaseEffect(stat_name="mental_health", change=8),
            PurchaseEffect(stat_name="energy_level", change=5),
        ],
        one_time=False,
        max_per_semester=3,
        emoji="🍽️",
    ),
    "concert_tickets": LifePurchase(
        purchase_id="concert_tickets",
        name="Concert Tickets",
        description="See your favorite band live. High happiness boost and great social time.",
        category="fun",
        cost=85.0,
        effects=[
            PurchaseEffect(stat_name="stress", change=-12),
            PurchaseEffect(stat_name="happiness", change=25),
            PurchaseEffect(stat_name="energy_level", change=10),
            PurchaseEffect(stat_name="mental_health", change=10),
        ],
        one_time=False,
        max_per_semester=2,
        emoji="🎵",
    ),
    "movie_night": LifePurchase(
        purchase_id="movie_night",
        name="Movie Night",
        description="Relax with a movie and snacks. Quick stress relief.",
        category="fun",
        cost=25.0,
        effects=[
            PurchaseEffect(stat_name="stress", change=-4),
            PurchaseEffect(stat_name="happiness", change=8),
            PurchaseEffect(stat_name="energy_level", change=3),
        ],
        one_time=False,
        max_per_semester=6,
        emoji="🍿",
    ),
    
    # Health & Wellness
    "gym_membership": LifePurchase(
        purchase_id="gym_membership",
        name="Gym Membership (Semester)",
        description="Join a gym for the semester. Improve fitness and reduce stress through exercise.",
        category="health",
        cost=120.0,
        effects=[
            PurchaseEffect(stat_name="fitness", change=20),
            PurchaseEffect(stat_name="stress", change=-10),
            PurchaseEffect(stat_name="energy_level", change=15),
            PurchaseEffect(stat_name="mental_health", change=12),
            PurchaseEffect(stat_name="happiness", change=8),
        ],
        one_time=False,
        max_per_semester=1,
        emoji="💪",
    ),
    "therapy_sessions": LifePurchase(
        purchase_id="therapy_sessions",
        name="Therapy Sessions (3 sessions)",
        description="Work with a therapist. Directly improve mental health and manage stress.",
        category="wellness",
        cost=300.0,
        effects=[
            PurchaseEffect(stat_name="mental_health", change=20),
            PurchaseEffect(stat_name="stress", change=-15),
            PurchaseEffect(stat_name="eq", change=8),
            PurchaseEffect(stat_name="happiness", change=12),
        ],
        one_time=False,
        max_per_semester=3,
        emoji="🧠",
        requires_semester_min=1,
    ),
    "spa_day": LifePurchase(
        purchase_id="spa_day",
        name="Spa Day",
        description="Treat yourself to massage, sauna, and relaxation. Maximum stress relief.",
        category="wellness",
        cost=150.0,
        effects=[
            PurchaseEffect(stat_name="stress", change=-20),
            PurchaseEffect(stat_name="mental_health", change=15),
            PurchaseEffect(stat_name="happiness", change=18),
            PurchaseEffect(stat_name="energy_level", change=8),
        ],
        one_time=False,
        max_per_semester=2,
        emoji="🧖",
    ),
    "meditation_app": LifePurchase(
        purchase_id="meditation_app",
        name="Meditation App (Annual)",
        description="Premium meditation subscription. Daily stress management and mental health.",
        category="wellness",
        cost=60.0,
        effects=[
            PurchaseEffect(stat_name="stress", change=-8),
            PurchaseEffect(stat_name="mental_health", change=15),
            PurchaseEffect(stat_name="eq", change=5),
        ],
        one_time=False,
        max_per_semester=1,
        emoji="🧘",
    ),
    
    # Practical Purchases
    "used_car": LifePurchase(
        purchase_id="used_car",
        name="Used Car",
        description="Buy a reliable used car. One-time cost but provides major convenience benefits.",
        category="practical",
        cost=8000.0,
        effects=[
            PurchaseEffect(stat_name="stress", change=-5),  # Less stress from commuting
            PurchaseEffect(stat_name="happiness", change=10),  # Freedom and convenience
            PurchaseEffect(stat_name="time_management", change=5),  # Better time management
        ],
        one_time=True,  # Buy once
        emoji="🚗",
        requires_semester_min=2,
    ),
    "laptop": LifePurchase(
        purchase_id="laptop",
        name="Quality Laptop",
        description="Invest in a good laptop for school and work. Improves productivity.",
        category="practical",
        cost=1200.0,
        effects=[
            PurchaseEffect(stat_name="time_management", change=8),
            PurchaseEffect(stat_name="stress", change=-3),
            PurchaseEffect(stat_name="technical_skills", change=2),
        ],
        one_time=True,
        emoji="💻",
        requires_semester_min=1,
    ),
    "apartment_upgrade": LifePurchase(
        purchase_id="apartment_upgrade",
        name="Better Apartment",
        description="Move to a nicer apartment with better amenities. Improves quality of life.",
        category="practical",
        cost=5000.0,  # One-time upgrade cost beyond normal rent
        effects=[
            PurchaseEffect(stat_name="mental_health", change=15),
            PurchaseEffect(stat_name="happiness", change=12),
            PurchaseEffect(stat_name="sleep_quality", change=10),
            PurchaseEffect(stat_name="stress", change=-8),
        ],
        one_time=True,
        emoji="🏠",
        requires_semester_min=2,
    ),
    
    # Self-Care & Personal Development
    "professional_wardrobe": LifePurchase(
        purchase_id="professional_wardrobe",
        name="Professional Wardrobe",
        description="Invest in quality professional clothes. Boost confidence for interviews.",
        category="self-care",
        cost=500.0,
        effects=[
            PurchaseEffect(stat_name="communication_skills", change=5),
            PurchaseEffect(stat_name="happiness", change=8),
            PurchaseEffect(stat_name="stress", change=-3),
        ],
        one_time=False,
        emoji="👔",
        requires_semester_min=3,
    ),
    "online_course": LifePurchase(
        purchase_id="online_course",
        name="Online Course/Certification",
        description="Invest in your future with an online course. Boost relevant skills.",
        category="self-care",
        cost=200.0,
        effects=[
            PurchaseEffect(stat_name="technical_skills", change=8),
            PurchaseEffect(stat_name="business_acumen", change=6),
            PurchaseEffect(stat_name="happiness", change=5),
        ],
        one_time=False,
        max_per_semester=3,
        emoji="🎓",
        requires_semester_min=2,
    ),
    "vacation": LifePurchase(
        purchase_id="vacation",
        name="Weekend Getaway",
        description="Take a break and travel. Major mental health and stress reset.",
        category="fun",
        cost=600.0,
        effects=[
            PurchaseEffect(stat_name="stress", change=-25),
            PurchaseEffect(stat_name="mental_health", change=25),
            PurchaseEffect(stat_name="happiness", change=20),
            PurchaseEffect(stat_name="energy_level", change=20),
            PurchaseEffect(stat_name="eq", change=5),
        ],
        one_time=False,
        max_per_semester=1,
        emoji="✈️",
        requires_semester_min=2,
    ),
    "gaming_console": LifePurchase(
        purchase_id="gaming_console",
        name="Gaming Console",
        description="Buy a gaming console for entertainment and stress relief.",
        category="fun",
        cost=400.0,
        effects=[
            PurchaseEffect(stat_name="stress", change=-8),
            PurchaseEffect(stat_name="happiness", change=15),
            PurchaseEffect(stat_name="energy_level", change=5),
        ],
        one_time=False,
        max_per_semester=2,
        emoji="🎮",
        requires_semester_min=2,
    ),
    "nutritionist_session": LifePurchase(
        purchase_id="nutritionist_session",
        name="Nutritionist Consultation",
        description="Meet with a nutritionist to optimize diet and health habits.",
        category="health",
        cost=200.0,
        effects=[
            PurchaseEffect(stat_name="fitness", change=8),
            PurchaseEffect(stat_name="energy_level", change=10),
            PurchaseEffect(stat_name="mental_health", change=8),
            PurchaseEffect(stat_name="stress", change=-5),
        ],
        one_time=False,
        max_per_semester=2,
        emoji="🥗",
        requires_semester_min=1,
    ),
    "weekend_camping_trip": LifePurchase(
        purchase_id="weekend_camping_trip",
        name="Weekend Camping Trip",
        description="Escape to nature for a weekend. Reduce stress and recharge.",
        category="fun",
        cost=200.0,
        effects=[
            PurchaseEffect(stat_name="stress", change=-15),
            PurchaseEffect(stat_name="mental_health", change=12),
            PurchaseEffect(stat_name="happiness", change=14),
            PurchaseEffect(stat_name="energy_level", change=10),
        ],
        one_time=False,
        max_per_semester=2,
        emoji="⛺",
        requires_semester_min=2,
    ),
    "music_lessons": LifePurchase(
        purchase_id="music_lessons",
        name="Music Lessons",
        description="Learn an instrument. Improve focus, creativity, and mental health.",
        category="self-care",
        cost=250.0,
        effects=[
            PurchaseEffect(stat_name="eq", change=8),
            PurchaseEffect(stat_name="stress", change=-8),
            PurchaseEffect(stat_name="mental_health", change=10),
            PurchaseEffect(stat_name="communication_skills", change=4),
        ],
        one_time=False,
        max_per_semester=2,
        emoji="🎸",
        requires_semester_min=3,
    ),
}


def get_purchase(purchase_id: str) -> Optional[LifePurchase]:
    """Get a specific purchase by ID"""
    return LIFE_PURCHASES.get(purchase_id)


def get_purchases_by_category(category: str) -> List[LifePurchase]:
    """Get all purchases in a category"""
    return [p for p in LIFE_PURCHASES.values() if p.category == category]


def get_available_purchases(current_semester: int) -> List[LifePurchase]:
    """Get all purchases available in current semester"""
    return [
        p for p in LIFE_PURCHASES.values()
        if p.requires_semester_min <= current_semester
    ]


def get_purchase_categories() -> List[str]:
    """Get all unique purchase categories"""
    return sorted(set(p.category for p in LIFE_PURCHASES.values()))
