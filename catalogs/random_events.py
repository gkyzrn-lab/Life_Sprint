"""
Random events, surprises, plot twists, and seasonal events.
Adds unpredictability and variety to each playthrough.
"""

from typing import Dict, List, Optional
import random
from enum import Enum

class EventCategory(str, Enum):
    FINANCIAL = "financial"
    ACADEMIC = "academic"
    SOCIAL = "social"
    HEALTH = "health"
    CAREER = "career"
    RANDOM = "random"

class EventTiming(str, Enum):
    SEMESTER_START = "semester_start"
    MID_SEMESTER = "mid_semester"
    SEMESTER_END = "semester_end"
    SEASONAL = "seasonal"
    RANDOM = "random"

# Financial Surprises
FINANCIAL_EVENTS = {
    "unexpected_scholarship": {
        "id": "unexpected_scholarship",
        "category": EventCategory.FINANCIAL,
        "title": "🎉 Surprise Scholarship!",
        "description": "You got an email: 'Congratulations! You've been selected for our emergency scholarship fund.'",
        "amount": lambda: random.randint(500, 2000),
        "probability": 0.15,
        "requirements": {"gpa": 3.0},
        "flavor_text": "Someone you helped last semester nominated you. Your kindness literally paid off.",
        "effects": {
            "money": "+random",  # Based on amount function
            "happiness": +20,
            "motivation": +15
        }
    },
    
    "car_breakdown": {
        "id": "car_breakdown",
        "category": EventCategory.FINANCIAL,
        "title": "🚗 Car Emergency",
        "description": "Your car broke down. Mechanic says $800 to fix it, or $300 for a temporary fix (might break again).",
        "probability": 0.12,
        "requirements": {"has_car": True},
        "choices": [
            {
                "id": "full_repair",
                "text": "Pay $800 for full repair",
                "requires_money": 800,
                "effects": {"money": -800, "car_reliability": 100, "stress": -10}
            },
            {
                "id": "cheap_repair",
                "text": "Pay $300 for temp fix",
                "requires_money": 300,
                "effects": {"money": -300, "car_reliability": 50, "future_breakdown_likely": True, "stress": +15}
            },
            {
                "id": "no_repair",
                "text": "Can't afford it - bus/bike instead",
                "effects": {"has_car": False, "commute_time": +30, "stress": +25, "saves_money": True}
            }
        ]
    },
    
    "tax_refund": {
        "id": "tax_refund",
        "category": EventCategory.FINANCIAL,
        "title": "💰 Tax Refund",
        "description": "Your tax refund came through!",
        "amount": lambda: random.randint(300, 800),
        "probability": 0.20,
        "timing": EventTiming.SEMESTER_START,
        "requirements": {"worked_last_year": True},
        "flavor_text": "That part-time job last year? You actually get money back. Feels like free money!",
        "effects": {
            "money": "+random",
            "happiness": +15
        }
    },
    
    "surprise_bill": {
        "id": "surprise_bill",
        "category": EventCategory.FINANCIAL,
        "title": "📄 Unexpected Bill",
        "description": "Medical bill / parking tickets / forgotten subscription. $250 due immediately.",
        "probability": 0.18,
        "amount": 250,
        "flavor_text": "How did you not see this coming? Doesn't matter now - it's due.",
        "effects": {
            "money": -250,
            "stress": +20
        }
    },
    
    "found_side_gig": {
        "id": "found_side_gig",
        "category": EventCategory.FINANCIAL,
        "title": "💼 Side Gig Opportunity",
        "description": "Friend needs help with their business. $500 for 2 weekends of work. Interested?",
        "probability": 0.15,
        "choices": [
            {
                "id": "take_gig",
                "text": "Take it - $500 for 20 hours work",
                "effects": {"money": +500, "time_lost_hours": 20, "stress": +10, "network": +5}
            },
            {
                "id": "decline",
                "text": "Decline - need to focus on studies",
                "effects": {"study_time_protected": True}
            }
        ]
    }
}

# Academic Surprises
ACADEMIC_EVENTS = {
    "surprise_exam": {
        "id": "surprise_exam",
        "category": EventCategory.ACADEMIC,
        "title": "😱 Pop Quiz Worth 10% of Grade",
        "description": "Professor walks in: 'I hope you did the readings... because here's a quiz.' You did NOT do the readings.",
        "probability": 0.20,
        "timing": EventTiming.MID_SEMESTER,
        "outcomes": {
            "prepared": {
                "chance": 0.3,  # Based on study habits
                "effects": {"grade_boost": +3, "confidence": +10}
            },
            "unprepared": {
                "chance": 0.7,
                "effects": {"grade_penalty": -5, "stress": +25, "wake_up_call": True}
            }
        }
    },
    
    "professor_recognizes_talent": {
        "id": "professor_recognizes_talent",
        "category": EventCategory.ACADEMIC,
        "title": "🌟 Professor Notices Your Potential",
        "description": "Professor asks you to be a TA (teaching assistant) next semester. Looks great on resume + pays $2,000.",
        "probability": 0.10,
        "requirements": {"gpa": 3.5, "subject_performance": "excellent"},
        "choices": [
            {
                "id": "accept_ta",
                "text": "Accept TA position",
                "effects": {
                    "is_ta": True,
                    "money_per_semester": +2000,
                    "resume_boost": +30,
                    "time_per_week": -10,
                    "teaching_experience": True
                }
            },
            {
                "id": "decline_ta",
                "text": "Decline - too busy",
                "effects": {"opportunity_missed": True}
            }
        ]
    },
    
    "group_project_disaster": {
        "id": "group_project_disaster",
        "category": EventCategory.ACADEMIC,
        "title": "🤦 Group Project Nightmare",
        "description": "It's due tomorrow. Two teammates ghosted. One submitted garbage. You have to carry the whole thing tonight.",
        "probability": 0.25,
        "timing": EventTiming.MID_SEMESTER,
        "choices": [
            {
                "id": "all_nighter",
                "text": "Pull an all-nighter and do it yourself",
                "effects": {"grade_saved": True, "stress": +35, "health": -20, "sleep_hours": 0, "resentment": +50}
            },
            {
                "id": "submit_incomplete",
                "text": "Submit what you have and explain to professor",
                "effects": {"grade_penalty": -15, "stress": +20, "integrity_maintained": True}
            },
            {
                "id": "confront_team",
                "text": "Emergency team meeting NOW - make them help",
                "success_chance": 0.6,
                "success_effects": {"project_completed": True, "stress": +10, "leadership": +15},
                "failure_effects": {"they_ghosted_anyway": True, "stress": +40}
            }
        ]
    },
    
    "research_opportunity": {
        "id": "research_opportunity",
        "category": EventCategory.ACADEMIC,
        "title": "🔬 Research Assistant Offer",
        "description": "Professor needs research assistant. Unpaid, but looks amazing for grad school applications.",
        "probability": 0.12,
        "requirements": {"gpa": 3.3, "semester": 4},
        "choices": [
            {
                "id": "accept_research",
                "text": "Accept (10 hours/week, unpaid)",
                "effects": {
                    "research_experience": True,
                    "grad_school_chance": 1.5,
                    "publication_possible": True,
                    "time_per_week": -10,
                    "resume_elite": True
                }
            },
            {
                "id": "decline_research",
                "text": "Can't afford unpaid work right now",
                "effects": {"financially_pragmatic": True}
            }
        ]
    }
}

# Social Surprises
SOCIAL_EVENTS = {
    "romantic_opportunity": {
        "id": "romantic_opportunity",
        "category": EventCategory.SOCIAL,
        "title": "❤️ Someone's Interested in You",
        "description": "That cute person from your class asked if you want to get coffee. Seems like more than friendship vibes.",
        "probability": 0.15,
        "timing": EventTiming.MID_SEMESTER,
        "choices": [
            {
                "id": "pursue_romance",
                "text": "Go for it - start dating",
                "effects": {
                    "in_relationship": True,
                    "happiness": +40,
                    "time_per_week": -8,
                    "study_distraction": +10,
                    "emotional_support": +30
                }
            },
            {
                "id": "just_friends",
                "text": "Keep it friendly - too busy for dating",
                "effects": {"friendship": +10, "focus_maintained": True}
            }
        ]
    },
    
    "friend_emergency": {
        "id": "friend_emergency",
        "category": EventCategory.SOCIAL,
        "title": "📞 Friend Crisis - They Need You",
        "description": "Your best friend is going through something serious. They need you tonight. But you have a major exam tomorrow.",
        "probability": 0.10,
        "timing": EventTiming.RANDOM,
        "choices": [
            {
                "id": "help_friend",
                "text": "Be there for them - exam can wait",
                "effects": {
                    "friendship": +50,
                    "exam_grade": -10,
                    "stress": +15,
                    "humanity_intact": True,
                    "friend_remembers_forever": True
                }
            },
            {
                "id": "prioritize_exam",
                "text": "Tell them you'll help after the exam",
                "effects": {
                    "exam_grade": +10,
                    "friendship": -20,
                    "guilt": +30,
                    "pragmatic_choice": True
                }
            },
            {
                "id": "compromise",
                "text": "Video call for 1 hour, then study",
                "effects": {
                    "friendship": +20,
                    "exam_grade": -3,
                    "stress": +20,
                    "balance_attempt": True
                }
            }
        ]
    },
    
    "party_invite_before_finals": {
        "id": "party_invite_before_finals",
        "category": EventCategory.SOCIAL,
        "title": "🎉 Epic Party vs. Finals Prep",
        "description": "The party of the semester. Everyone will be there. Your crush will be there. But finals start in 2 days.",
        "probability": 0.20,
        "timing": EventTiming.SEMESTER_END,
        "choices": [
            {
                "id": "go_party",
                "text": "YOLO - you're only in college once",
                "effects": {
                    "memories": +50,
                    "social_status": +20,
                    "finals_grade": -8,
                    "no_regrets": True,
                    "legendary_night": True
                }
            },
            {
                "id": "study_instead",
                "text": "Stay home and study",
                "effects": {
                    "finals_grade": +10,
                    "fomo": +35,
                    "responsible_choice": True
                }
            },
            {
                "id": "go_briefly",
                "text": "Show up for 1 hour then leave",
                "effects": {
                    "social_obligation_met": True,
                    "finals_grade": -2,
                    "stress": +10,
                    "balance_achieved": True
                }
            }
        ]
    },
    
    "falling_out": {
        "id": "falling_out",
        "category": EventCategory.SOCIAL,
        "title": "💔 Friend Group Drama",
        "description": "Two of your close friends had a massive fight. Both are asking you to take sides. Refusing to choose means losing both.",
        "probability": 0.12,
        "timing": EventTiming.RANDOM,
        "choices": [
            {
                "id": "side_with_a",
                "text": "Side with Friend A",
                "effects": {"friendship_a": +30, "friendship_b": -70, "social_circle_split": True, "stress": +25}
            },
            {
                "id": "side_with_b",
                "text": "Side with Friend B",
                "effects": {"friendship_b": +30, "friendship_a": -70, "social_circle_split": True, "stress": +25}
            },
            {
                "id": "mediate",
                "text": "Try to mediate and keep everyone together",
                "success_chance": 0.4,
                "success_effects": {"friendship_a": +20, "friendship_b": +20, "peacemaker_reputation": True, "stress": +15},
                "failure_effects": {"both_mad_at_you": True, "friendship_a": -30, "friendship_b": -30, "stress": +40}
            },
            {
                "id": "stay_out",
                "text": "Stay completely out of it",
                "effects": {"friendship_a": -15, "friendship_b": -15, "seen_as_distant": True, "stress": +10}
            }
        ]
    }
}

# Seasonal Events
SEASONAL_EVENTS = {
    "spring_break": {
        "id": "spring_break",
        "category": EventCategory.SOCIAL,
        "title": "🏖️ Spring Break Decision",
        "description": "Everyone's going somewhere for spring break. Beach trip ($800), staying on campus (free), or going home ($200).",
        "timing": EventTiming.SEASONAL,
        "semester": 4,  # Happens in semester 4
        "choices": [
            {
                "id": "beach_trip",
                "text": "Beach trip with friends ($800)",
                "requires_money": 800,
                "effects": {"money": -800, "memories": +50, "happiness": +40, "social_bonds": +30, "instagram_content": +100}
            },
            {
                "id": "stay_campus",
                "text": "Stay on campus and work/study",
                "effects": {"money": +600, "study_progress": +20, "fomo": +40, "productive_break": True}
            },
            {
                "id": "go_home",
                "text": "Go home and recharge ($200)",
                "effects": {"money": -200, "stress": -40, "family_connection": +30, "rest": +40}
            },
            {
                "id": "service_trip",
                "text": "Alternative spring break (service trip)",
                "effects": {"resume_boost": +20, "meaningful_experience": +50, "perspective_shift": True, "good_karma": +100}
            }
        ]
    },
    
    "summer_decision": {
        "id": "summer_decision",
        "category": EventCategory.CAREER,
        "title": "☀️ Summer Plans",
        "description": "Summer's coming. Internship? Work full-time? Take classes? Travel? Each has trade-offs.",
        "timing": EventTiming.SEASONAL,
        "occurs_every": "semester_end",
        "choices": [
            {
                "id": "internship",
                "text": "Pursue internship (best for career)",
                "effects": {"career_progress": +50, "money": +3000, "experience": +40, "summer_fun": -20}
            },
            {
                "id": "full_time_work",
                "text": "Work full-time (best for money)",
                "effects": {"money": +6000, "exhausted_by_fall": True, "career_progress": +10, "debt_reduction": +40}
            },
            {
                "id": "summer_classes",
                "text": "Take summer classes (graduate early)",
                "effects": {"credits": +9, "money": -2000, "academic_progress": +30, "no_break": True, "burnout_risk": +25}
            },
            {
                "id": "travel",
                "text": "Travel and recharge (best for mental health)",
                "effects": {"money": -2000, "happiness": +50, "stress": -60, "memories": +60, "refreshed": True}
            }
        ]
    },
    
    "thanksgiving_choice": {
        "id": "thanksgiving_choice",
        "category": EventCategory.SOCIAL,
        "title": "🦃 Thanksgiving Dilemma",
        "description": "Go home for Thanksgiving ($300 flight) or stay and have Friendsgiving on campus (free but family disappointed).",
        "timing": EventTiming.SEASONAL,
        "occurs_semester": [3, 5, 7],
        "choices": [
            {
                "id": "go_home",
                "text": "Fly home ($300)",
                "requires_money": 300,
                "effects": {"money": -300, "family_happiness": +50, "homesickness": -40, "guilt": -30}
            },
            {
                "id": "friendsgiving",
                "text": "Friendsgiving on campus",
                "effects": {"friend_bonds": +40, "family_disappointed": True, "guilt": +25, "independence": +20}
            }
        ]
    }
}

# Career Plot Twists
CAREER_EVENTS = {
    "startup_recruitment": {
        "id": "startup_recruitment",
        "category": EventCategory.CAREER,
        "title": "🚀 Startup Wants to Hire You NOW",
        "description": "A startup offered you a job. $70K, equity, skip graduation. Your parents will freak. But it's your dream company.",
        "probability": 0.05,
        "requirements": {"semester": 7, "gpa": 3.2, "internships_completed": 1},
        "rarity": "rare",
        "choices": [
            {
                "id": "take_job",
                "text": "Drop out and take the job (like Steve Jobs?)",
                "effects": {
                    "game_ending": "startup_path",
                    "no_degree": True,
                    "career_fast_track": True,
                    "family_devastated": True,
                    "risk_taken": True
                }
            },
            {
                "id": "defer",
                "text": "Ask to defer until after graduation",
                "success_chance": 0.7,
                "success_effects": {"job_deferred": True, "finish_degree": True, "best_of_both": True},
                "failure_effects": {"offer_rescinded": True, "regret": +50}
            },
            {
                "id": "decline",
                "text": "Decline - finish your degree",
                "effects": {"degree_completed": True, "opportunity_cost_unknown": True, "safe_choice": True}
            }
        ]
    },
    
    "viral_portfolio": {
        "id": "viral_portfolio",
        "category": EventCategory.CAREER,
        "title": "🌟 Your Work Went Viral",
        "description": "That project you posted online? Industry leaders are noticing. You're getting DMs from recruiters at top companies.",
        "probability": 0.08,
        "requirements": {"portfolio_quality": "high", "social_media_active": True},
        "effects": {
            "job_offers": 3,
            "salary_boost": 1.3,
            "industry_recognition": True,
            "confidence": +50,
            "imposter_syndrome": +20  # Paradox of success
        }
    }
}

# Combine all random events
ALL_RANDOM_EVENTS = {
    **FINANCIAL_EVENTS,
    **ACADEMIC_EVENTS,
    **SOCIAL_EVENTS,
    **SEASONAL_EVENTS,
    **CAREER_EVENTS
}

def get_event(event_id: str) -> Optional[Dict]:
    """Get a specific random event."""
    return ALL_RANDOM_EVENTS.get(event_id)

def trigger_random_event(semester: int, player_state: Dict, category: Optional[EventCategory] = None) -> Optional[Dict]:
    """
    Trigger a random event based on probability and player state.
    
    Args:
        semester: Current semester
        player_state: Player's current state
        category: Optional filter for event category
    
    Returns:
        Random event dict or None
    """
    eligible_events = []
    
    for event_id, event in ALL_RANDOM_EVENTS.items():
        # Filter by category if specified
        if category and event.get("category") != category:
            continue
        
        # Check if seasonal event is appropriate
        if event.get("timing") == EventTiming.SEASONAL:
            if "semester" in event and event["semester"] != semester:
                continue
            if "occurs_semester" in event and semester not in event["occurs_semester"]:
                continue
        
        # Check requirements
        requirements = event.get("requirements", {})
        meets_requirements = True
        
        for req_key, req_value in requirements.items():
            player_value = player_state.get(req_key, 0)
            if isinstance(req_value, (int, float)):
                if player_value < req_value:
                    meets_requirements = False
                    break
            elif isinstance(req_value, bool):
                if player_value != req_value:
                    meets_requirements = False
                    break
        
        if not meets_requirements:
            continue
        
        # Check probability
        probability = event.get("probability", 0.1)
        if random.random() < probability:
            eligible_events.append(event)
    
    return random.choice(eligible_events) if eligible_events else None

def get_seasonal_event(semester: int) -> Optional[Dict]:
    """Get the seasonal event for the current semester."""
    for event in SEASONAL_EVENTS.values():
        if event.get("semester") == semester:
            return event
        if "occurs_semester" in event and semester in event["occurs_semester"]:
            return event
    return None

def process_random_choice(event_id: str, choice_id: str, player_state: Dict) -> Dict:
    """
    Process player's choice for a random event.
    Similar to story events but for random occurrences.
    """
    event = get_event(event_id)
    if not event:
        return {"error": "Event not found"}
    
    choices = event.get("choices", [])
    choice = next((c for c in choices if c["id"] == choice_id), None)
    
    if not choice:
        return {"error": "Choice not found"}
    
    # Check if choice has success/failure outcomes
    if "success_chance" in choice:
        success = random.random() < choice["success_chance"]
        effects = choice.get("success_effects" if success else "failure_effects", {})
    else:
        effects = choice.get("effects", {})
        success = True
    
    return {
        "effects": effects,
        "success": success
    }

def get_events_by_category(category: EventCategory) -> List[Dict]:
    """Get all events in a specific category."""
    return [e for e in ALL_RANDOM_EVENTS.values() if e.get("category") == category]
