"""
Store catalog for in-game purchases.
Students can spend money on real-life items that affect their stats.
"""

from typing import Dict, List
from enum import Enum

class StoreCategory(str, Enum):
    ENTERTAINMENT = "entertainment"
    TECHNOLOGY = "technology"
    FOOD = "food"
    SOCIAL = "social"
    HEALTH = "health"
    EDUCATION = "education"
    CLOTHING = "clothing"
    TRANSPORTATION = "transportation"

# Store items available for purchase
STORE_ITEMS = {
    # ENTERTAINMENT
    "movie_ticket": {
        "id": "movie_ticket",
        "name": "Movie Theater Ticket",
        "category": StoreCategory.ENTERTAINMENT,
        "price": 15.00,
        "description": "2-hour escape from reality. Relax and recharge.",
        "effects": {
            "morale": 10,
            "social": 5,
            "stress": -8
        },
        "duration_hours": 2,
        "repeatable": True,
        "warning": "Don't go too often - that's $60/month if you go weekly!"
    },
    
    "concert_ticket": {
        "id": "concert_ticket",
        "name": "Concert / Music Event",
        "category": StoreCategory.ENTERTAINMENT,
        "price": 75.00,
        "description": "Live music experience. Great memories with friends.",
        "effects": {
            "morale": 25,
            "social": 20,
            "stress": -15,
            "energy": -10  # Exhausting but fun!
        },
        "duration_hours": 4,
        "repeatable": True,
        "warning": "Expensive but memorable. Once per semester is reasonable."
    },
    
    "video_game": {
        "id": "video_game",
        "name": "Video Game",
        "category": StoreCategory.ENTERTAINMENT,
        "price": 60.00,
        "description": "New release game. Hours of entertainment... or procrastination?",
        "effects": {
            "morale": 15,
            "stress": -10,
            "focus": -5,  # Can be distracting!
            "social": -5   # If you game alone too much
        },
        "duration_hours": 0,  # Ongoing
        "repeatable": True,
        "warning": "Gaming is fun but can become a time sink. Set limits!"
    },
    
    "streaming_subscription": {
        "id": "streaming_subscription",
        "name": "Streaming Service (Monthly)",
        "category": StoreCategory.ENTERTAINMENT,
        "price": 15.00,
        "description": "Netflix, Hulu, Disney+, etc. Entertainment on demand.",
        "effects": {
            "morale": 8,
            "stress": -5
        },
        "duration_hours": 0,  # Monthly subscription
        "repeatable": True,
        "warning": "Subscriptions add up! $15/month = $180/year."
    },
    
    "campus_event": {
        "id": "campus_event",
        "name": "Campus Event Ticket",
        "category": StoreCategory.ENTERTAINMENT,
        "price": 20.00,
        "description": "Comedy show, play, sports game, or campus festival.",
        "effects": {
            "morale": 12,
            "social": 15,
            "school_pride": 10,
            "stress": -8
        },
        "duration_hours": 3,
        "repeatable": True,
        "warning": "Great for building social connections on campus!"
    },
    
    # TECHNOLOGY
    "smartphone": {
        "id": "smartphone",
        "name": "New Smartphone",
        "category": StoreCategory.TECHNOLOGY,
        "price": 800.00,
        "description": "Latest phone. Necessary? Or just want the newest model?",
        "effects": {
            "social": 15,
            "anxiety": 10,  # FOMO, constant notifications
            "productivity": -5,  # Distracting
            "status": 10
        },
        "duration_hours": 0,
        "repeatable": False,  # One-time purchase (lasts years)
        "warning": "Do you NEED a new phone or just WANT one? Old phone still works?"
    },
    
    "laptop": {
        "id": "laptop",
        "name": "Student Laptop",
        "category": StoreCategory.TECHNOLOGY,
        "price": 1200.00,
        "description": "Powerful laptop for studying, projects, and assignments.",
        "effects": {
            "study_efficiency": 25,
            "productivity": 20,
            "focus": 10,
            "tech_skills": 5
        },
        "duration_hours": 0,
        "repeatable": False,
        "warning": "Essential tool! Good investment for college success."
    },
    
    "tablet": {
        "id": "tablet",
        "name": "Tablet / iPad",
        "category": StoreCategory.TECHNOLOGY,
        "price": 500.00,
        "description": "For note-taking, reading, and light work.",
        "effects": {
            "study_efficiency": 15,
            "organization": 10,
            "productivity": 10
        },
        "duration_hours": 0,
        "repeatable": False,
        "warning": "Nice to have but not essential. Laptop does the same things."
    },
    
    "noise_canceling_headphones": {
        "id": "noise_canceling_headphones",
        "name": "Noise-Canceling Headphones",
        "category": StoreCategory.TECHNOLOGY,
        "price": 300.00,
        "description": "Block out distractions. Study in peace.",
        "effects": {
            "focus": 20,
            "study_efficiency": 15,
            "stress": -10
        },
        "duration_hours": 0,
        "repeatable": False,
        "warning": "Great for noisy dorms! Helps you concentrate."
    },
    
    "gaming_console": {
        "id": "gaming_console",
        "name": "Gaming Console",
        "category": StoreCategory.TECHNOLOGY,
        "price": 500.00,
        "description": "PS5, Xbox, or Switch. Entertainment hub for your dorm.",
        "effects": {
            "morale": 20,
            "social": 10,  # Gaming with roommates
            "focus": -10,  # Very distracting
            "study_time": -15
        },
        "duration_hours": 0,
        "repeatable": False,
        "warning": "Fun but VERY distracting during finals. Set boundaries!"
    },
    
    # FOOD & DINING
    "restaurant_nice": {
        "id": "restaurant_nice",
        "name": "Nice Restaurant Dinner",
        "category": StoreCategory.FOOD,
        "price": 50.00,
        "description": "Treat yourself to a quality meal. Good food, good mood.",
        "effects": {
            "morale": 15,
            "social": 10,
            "health": 5,
            "stress": -8
        },
        "duration_hours": 2,
        "repeatable": True,
        "warning": "Delicious but pricey. Save for special occasions!"
    },
    
    "fast_food": {
        "id": "fast_food",
        "name": "Fast Food Meal",
        "category": StoreCategory.FOOD,
        "price": 12.00,
        "description": "Quick, cheap, convenient... but not healthy.",
        "effects": {
            "hunger": 0,  # Fills you up
            "health": -5,  # Not nutritious
            "energy": -3,  # Food coma
            "budget_consciousness": -2
        },
        "duration_hours": 0,
        "repeatable": True,
        "warning": "Eating out daily = $360/month. Cook at home when possible!"
    },
    
    "coffee_shop": {
        "id": "coffee_shop",
        "name": "Coffee Shop Visit",
        "category": StoreCategory.FOOD,
        "price": 6.00,
        "description": "Latte, study space, and caffeine boost.",
        "effects": {
            "energy": 10,
            "focus": 8,
            "social": 5,
            "morale": 5
        },
        "duration_hours": 2,
        "repeatable": True,
        "warning": "Daily coffee = $180/month. Make it at home for $20/month!"
    },
    
    "meal_prep_kit": {
        "id": "meal_prep_kit",
        "name": "Meal Prep Containers & Groceries",
        "category": StoreCategory.FOOD,
        "price": 80.00,
        "description": "Containers + groceries for a week of healthy meals.",
        "effects": {
            "health": 20,
            "energy": 10,
            "organization": 10,
            "budget_consciousness": 15,
            "life_skills": 10
        },
        "duration_hours": 0,
        "repeatable": True,
        "warning": "Smart investment! Saves $200+/month vs eating out."
    },
    
    # SOCIAL ACTIVITIES
    "dance_class": {
        "id": "dance_class",
        "name": "Dance / Salsa Class",
        "category": StoreCategory.SOCIAL,
        "price": 25.00,
        "description": "Learn to dance, meet new people, great workout!",
        "effects": {
            "social": 20,
            "confidence": 15,
            "health": 10,
            "morale": 18,
            "stress": -12
        },
        "duration_hours": 2,
        "repeatable": True,
        "warning": "Excellent for building confidence and meeting people!"
    },
    
    "bar_night": {
        "id": "bar_night",
        "name": "Night Out at Bars",
        "category": StoreCategory.SOCIAL,
        "price": 60.00,
        "description": "Drinks with friends. Social but expensive... and risky.",
        "effects": {
            "social": 15,
            "morale": 10,
            "health": -15,  # Alcohol effects
            "focus": -10,  # Hangover
            "study_time": -8,
            "safety_risk": 10
        },
        "duration_hours": 5,
        "repeatable": True,
        "warning": "Fun but expensive and unhealthy. Drink responsibly!"
    },
    
    "club_membership": {
        "id": "club_membership",
        "name": "Campus Club Membership",
        "category": StoreCategory.SOCIAL,
        "price": 30.00,
        "description": "Join a student organization. Build your resume and network.",
        "effects": {
            "social": 25,
            "networking": 20,
            "resume_strength": 15,
            "leadership": 10,
            "morale": 12
        },
        "duration_hours": 0,
        "repeatable": False,
        "warning": "Great ROI! Networking = future job opportunities."
    },
    
    "study_group_supplies": {
        "id": "study_group_supplies",
        "name": "Study Group Snacks & Supplies",
        "category": StoreCategory.SOCIAL,
        "price": 25.00,
        "description": "Host a study group. Pizza, snacks, good vibes.",
        "effects": {
            "social": 15,
            "study_efficiency": 10,
            "morale": 10,
            "networking": 8
        },
        "duration_hours": 3,
        "repeatable": True,
        "warning": "Studying together makes it less painful!"
    },
    
    # HEALTH & FITNESS
    "gym_membership": {
        "id": "gym_membership",
        "name": "Gym Membership (Monthly)",
        "category": StoreCategory.HEALTH,
        "price": 40.00,
        "description": "Access to fitness equipment and classes.",
        "effects": {
            "health": 25,
            "energy": 15,
            "stress": -20,
            "confidence": 10,
            "focus": 12
        },
        "duration_hours": 0,
        "repeatable": True,
        "warning": "Great investment IF you actually go. Don't just pay for guilt!"
    },
    
    "yoga_class": {
        "id": "yoga_class",
        "name": "Yoga Class Pass",
        "category": StoreCategory.HEALTH,
        "price": 20.00,
        "description": "Stress relief, flexibility, mindfulness.",
        "effects": {
            "stress": -20,
            "health": 10,
            "focus": 15,
            "morale": 12,
            "anxiety": -15
        },
        "duration_hours": 1,
        "repeatable": True,
        "warning": "Excellent for stress management during finals!"
    },
    
    "bike": {
        "id": "bike",
        "name": "Bicycle",
        "category": StoreCategory.TRANSPORTATION,
        "price": 300.00,
        "description": "Get around campus, exercise, save on gas.",
        "effects": {
            "health": 15,
            "energy": 10,
            "budget_consciousness": 20,
            "environmental": 10,
            "transportation_access": 20
        },
        "duration_hours": 0,
        "repeatable": False,
        "warning": "Pays for itself! No gas, no parking fees, good exercise."
    },
    
    "therapy_session": {
        "id": "therapy_session",
        "name": "Therapy / Counseling Session",
        "category": StoreCategory.HEALTH,
        "price": 80.00,
        "description": "Mental health support. Not a luxury, a necessity.",
        "effects": {
            "mental_health": 30,
            "stress": -25,
            "anxiety": -20,
            "coping_skills": 15,
            "self_awareness": 10
        },
        "duration_hours": 1,
        "repeatable": True,
        "warning": "Many campuses offer FREE counseling. Check first!"
    },
    
    # EDUCATION
    "textbooks_new": {
        "id": "textbooks_new",
        "name": "New Textbooks",
        "category": StoreCategory.EDUCATION,
        "price": 400.00,
        "description": "Brand new textbooks for the semester.",
        "effects": {
            "study_efficiency": 10,
            "grades": 5
        },
        "duration_hours": 0,
        "repeatable": True,
        "warning": "EXPENSIVE! Used books or rentals cost 70% less for same content!"
    },
    
    "textbooks_used": {
        "id": "textbooks_used",
        "name": "Used Textbooks",
        "category": StoreCategory.EDUCATION,
        "price": 150.00,
        "description": "Same content, much cheaper. Smart choice!",
        "effects": {
            "study_efficiency": 10,
            "grades": 5,
            "budget_consciousness": 20
        },
        "duration_hours": 0,
        "repeatable": True,
        "warning": "Smart students buy used. Save $250 per semester!"
    },
    
    "online_course": {
        "id": "online_course",
        "name": "Skill-Building Online Course",
        "category": StoreCategory.EDUCATION,
        "price": 100.00,
        "description": "Udemy, Coursera, LinkedIn Learning. Learn valuable skills.",
        "effects": {
            "tech_skills": 20,
            "resume_strength": 15,
            "career_readiness": 15,
            "marketability": 10
        },
        "duration_hours": 20,
        "repeatable": True,
        "warning": "Great ROI! Coding, design, and data skills are valuable."
    },
    
    "tutoring": {
        "id": "tutoring",
        "name": "Private Tutoring (5 sessions)",
        "category": StoreCategory.EDUCATION,
        "price": 200.00,
        "description": "One-on-one help in difficult subjects.",
        "effects": {
            "grades": 25,
            "study_efficiency": 20,
            "confidence": 15,
            "stress": -10
        },
        "duration_hours": 10,
        "repeatable": True,
        "warning": "Expensive but can save your GPA. Check for free campus tutoring first!"
    },
    
    # CLOTHING & APPEARANCE
    "interview_outfit": {
        "id": "interview_outfit",
        "name": "Professional Interview Outfit",
        "category": StoreCategory.CLOTHING,
        "price": 150.00,
        "description": "Suit or professional attire. Look the part to get the part.",
        "effects": {
            "confidence": 20,
            "interview_success": 25,
            "professionalism": 20,
            "first_impression": 15
        },
        "duration_hours": 0,
        "repeatable": False,
        "warning": "Investment in your future. Good outfit = better interviews!"
    },
    
    "designer_clothes": {
        "id": "designer_clothes",
        "name": "Designer Clothing",
        "category": StoreCategory.CLOTHING,
        "price": 300.00,
        "description": "Brand name fashion. Looks good... but expensive flex.",
        "effects": {
            "confidence": 10,
            "social": 8,
            "status": 15,
            "budget_consciousness": -20  # Bad financial habit
        },
        "duration_hours": 0,
        "repeatable": True,
        "warning": "Want vs need? $300 for clothes you could buy for $50 elsewhere."
    },
    
    # TRANSPORTATION
    "car_payment": {
        "id": "car_payment",
        "name": "Car (Monthly Payment)",
        "category": StoreCategory.TRANSPORTATION,
        "price": 350.00,
        "description": "Monthly car loan payment. Freedom... at a cost.",
        "effects": {
            "transportation_access": 30,
            "independence": 20,
            "job_access": 15,
            "budget_consciousness": -30,  # Expensive ongoing cost
            "stress": 10  # Maintenance, parking, insurance
        },
        "duration_hours": 0,
        "repeatable": True,
        "warning": "$350 + insurance + gas + parking = $600+/month! Can you afford it?"
    },
    
    "uber_rides": {
        "id": "uber_rides",
        "name": "Rideshare Credit ($50)",
        "category": StoreCategory.TRANSPORTATION,
        "price": 50.00,
        "description": "Uber/Lyft rides for the month. Convenient but adds up.",
        "effects": {
            "transportation_access": 15,
            "convenience": 10,
            "safety": 5  # Safer than walking alone at night
        },
        "duration_hours": 0,
        "repeatable": True,
        "warning": "Using daily? That's $50/week = $200/month. Consider alternatives!"
    }
}

def get_store_item(item_id: str) -> Dict:
    """Get a specific store item."""
    return STORE_ITEMS.get(item_id)

def get_items_by_category(category: StoreCategory) -> List[Dict]:
    """Get all items in a category."""
    return [item for item in STORE_ITEMS.values() if item["category"] == category]

def get_affordable_items(player_balance: float) -> List[Dict]:
    """Get items player can afford."""
    return [item for item in STORE_ITEMS.values() if item["price"] <= player_balance]

def purchase_item(player_balance: float, item_id: str) -> Dict:
    """
    Process a purchase.
    
    Returns:
        Dict with success status, new balance, and effects to apply
    """
    item = get_store_item(item_id)
    
    if not item:
        return {"success": False, "message": "Item not found"}
    
    if player_balance < item["price"]:
        return {
            "success": False,
            "message": f"Not enough money! Need ${item['price']}, have ${player_balance}"
        }
    
    new_balance = player_balance - item["price"]
    
    return {
        "success": True,
        "message": f"Purchased {item['name']} for ${item['price']}",
        "new_balance": new_balance,
        "effects": item["effects"],
        "warning": item.get("warning", "")
    }

def calculate_monthly_expenses(purchased_subscriptions: List[str]) -> float:
    """Calculate recurring monthly costs."""
    monthly_cost = 0.0
    
    monthly_items = [
        "streaming_subscription",
        "gym_membership",
        "car_payment"
    ]
    
    for item_id in purchased_subscriptions:
        if item_id in monthly_items:
            item = get_store_item(item_id)
            monthly_cost += item["price"]
    
    return monthly_cost

def get_smart_recommendations(player_balance: float, player_stats: Dict) -> List[Dict]:
    """
    Recommend items based on player's current situation.
    
    Args:
        player_balance: How much money player has
        player_stats: Player's current stats (stress, morale, grades, etc.)
    
    Returns:
        List of recommended items with reasoning
    """
    recommendations = []
    
    # High stress? Recommend stress relief
    if player_stats.get("stress", 0) > 70:
        recommendations.append({
            "item_id": "yoga_class",
            "reason": "Your stress is very high! Yoga can help you decompress.",
            "priority": "high"
        })
        recommendations.append({
            "item_id": "gym_membership",
            "reason": "Exercise is proven to reduce stress. Consider working out.",
            "priority": "medium"
        })
    
    # Low grades? Recommend education items
    if player_stats.get("gpa", 3.0) < 2.5:
        recommendations.append({
            "item_id": "tutoring",
            "reason": "Your GPA is struggling. Tutoring could make a big difference.",
            "priority": "high"
        })
        recommendations.append({
            "item_id": "textbooks_used",
            "reason": "Make sure you have the right materials to study effectively.",
            "priority": "medium"
        })
    
    # Low social? Recommend social activities
    if player_stats.get("social", 50) < 30:
        recommendations.append({
            "item_id": "club_membership",
            "reason": "You're isolated! Joining a club helps build friendships.",
            "priority": "high"
        })
        recommendations.append({
            "item_id": "dance_class",
            "reason": "Great way to meet people while having fun!",
            "priority": "medium"
        })
    
    # Good balance and can afford? Recommend investments
    if player_balance > 1000 and player_stats.get("stress", 50) < 40:
        recommendations.append({
            "item_id": "laptop",
            "reason": "You're in good shape. Invest in tools for success.",
            "priority": "medium"
        })
        recommendations.append({
            "item_id": "online_course",
            "reason": "Build skills for your future career.",
            "priority": "low"
        })
    
    return recommendations

def get_all_items() -> Dict[str, Dict]:
    """Get all store items."""
    return STORE_ITEMS

def get_item_count() -> int:
    """Get total number of items in store."""
    return len(STORE_ITEMS)
