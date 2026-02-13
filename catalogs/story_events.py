"""
Story events, drama, and narrative content to make the game engaging.
Includes roommate drama, relationships, social media, rivalries, and mentors.
"""

from typing import Dict, List, Optional
from enum import Enum
import random

class EventType(str, Enum):
    ROOMMATE = "roommate"
    RELATIONSHIP = "relationship"
    SOCIAL_MEDIA = "social_media"
    RIVAL = "rival"
    MENTOR = "mentor"
    FRIEND_GROUP = "friend_group"
    CAMPUS_DRAMA = "campus_drama"
    OPPORTUNITY = "opportunity"

class EventImpact(str, Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    MIXED = "mixed"

# Roommate Drama Events
ROOMMATE_EVENTS = {
    "messy_roommate": {
        "id": "messy_roommate",
        "type": EventType.ROOMMATE,
        "title": "The Messy Roommate Situation",
        "description": "Your roommate hasn't done dishes in 2 weeks. The apartment smells. This is getting ridiculous.",
        "flavor_text": "You come home to find a pile of dishes in the sink... again. Fruit flies are starting to appear. Your roommate is playing video games, headphones on, oblivious.",
        "choices": [
            {
                "id": "confront",
                "text": "Confront them directly about it",
                "personality_match": ["assertive", "direct"],
                "outcomes": {
                    "success": {
                        "text": "They apologize and start cleaning immediately. You set up a chore schedule. Problem solved!",
                        "effects": {"stress": -10, "relationship_roommate": +20}
                    },
                    "failure": {
                        "text": "They get defensive: 'Stop being so uptight!' Now there's tension in the apartment.",
                        "effects": {"stress": +15, "relationship_roommate": -10}
                    }
                },
                "success_chance": 0.6
            },
            {
                "id": "passive_aggressive",
                "text": "Leave passive-aggressive notes",
                "personality_match": ["avoidant"],
                "outcomes": {
                    "success": {
                        "text": "They get the hint and start cleaning. But they're annoyed you didn't just talk to them.",
                        "effects": {"stress": -5, "relationship_roommate": -5}
                    },
                    "failure": {
                        "text": "They ignore the notes completely. The mess gets worse. You're now even more frustrated.",
                        "effects": {"stress": +20, "relationship_roommate": -15}
                    }
                },
                "success_chance": 0.3
            },
            {
                "id": "clean_yourself",
                "text": "Just clean it yourself to avoid conflict",
                "personality_match": ["people_pleaser"],
                "outcomes": {
                    "default": {
                        "text": "You spend an hour cleaning. They thank you but don't change. This will keep happening.",
                        "effects": {"stress": +10, "time_lost_hours": 1, "relationship_roommate": +5}
                    }
                },
                "success_chance": 1.0
            },
            {
                "id": "propose_solution",
                "text": "Suggest hiring a cleaning service (split cost)",
                "personality_match": ["pragmatic"],
                "outcomes": {
                    "success": {
                        "text": "They agree! $40/month each for bi-weekly cleaning. Problem solved, zero conflict.",
                        "effects": {"stress": -15, "monthly_expense": +40, "relationship_roommate": +10}
                    },
                    "failure": {
                        "text": "They say they can't afford it. You're back to square one.",
                        "effects": {"stress": +5}
                    }
                },
                "success_chance": 0.5
            }
        ],
        "unlocks_after_semester": 1,
        "can_repeat": True
    },
    
    "roommate_bestfriend": {
        "id": "roommate_bestfriend",
        "type": EventType.ROOMMATE,
        "title": "Roommate Becomes Best Friend",
        "description": "You and your roommate have been clicking lately. Late night talks, same sense of humor, genuine connection.",
        "flavor_text": "It's 2 AM. You're both studying, taking a break, and somehow you've been talking for an hour about everything and nothing. You realize... this person *gets* you.",
        "choices": [
            {
                "id": "embrace_friendship",
                "text": "Embrace the friendship, plan regular hangouts",
                "outcomes": {
                    "default": {
                        "text": "You gain a best friend for life. Study partner, emotional support, future wedding party member.",
                        "effects": {"stress": -20, "happiness": +30, "study_effectiveness": 1.2, "relationship_roommate": +50}
                    }
                },
                "success_chance": 1.0
            },
            {
                "id": "keep_distance",
                "text": "Keep things cordial but maintain distance",
                "outcomes": {
                    "default": {
                        "text": "You stay friendly but surface-level. Years later, you'll wonder 'what if?'",
                        "effects": {"relationship_roommate": +10}
                    }
                },
                "success_chance": 1.0
            }
        ],
        "requirements": {
            "relationship_roommate": 50,
            "semesters_lived_together": 2
        },
        "impact": EventImpact.POSITIVE,
        "unlocks_after_semester": 2,
        "can_repeat": False
    },
    
    "roommate_stealing": {
        "id": "roommate_stealing",
        "type": EventType.ROOMMATE,
        "title": "The Food Thief",
        "description": "Your groceries keep disappearing. You're pretty sure your roommate is eating your food without asking.",
        "flavor_text": "That leftover pizza you were looking forward to? Gone. Your fancy coffee creamer? Empty. The granola bars you just bought? Two left out of 12. What the hell?",
        "choices": [
            {
                "id": "confront_direct",
                "text": "Call them out directly",
                "outcomes": {
                    "success": {
                        "text": "They admit it sheepishly, Venmo you $40, and promise to stop. They follow through.",
                        "effects": {"money": +40, "relationship_roommate": -5, "stress": -10}
                    },
                    "failure": {
                        "text": "They deny everything and act offended. Now you have to label all your food like a psycho.",
                        "effects": {"stress": +15, "relationship_roommate": -20}
                    }
                },
                "success_chance": 0.7
            },
            {
                "id": "label_food",
                "text": "Label everything with your name",
                "outcomes": {
                    "default": {
                        "text": "It stops... but the apartment vibe is weird now. Roommate acts offended but guilty.",
                        "effects": {"stress": -5, "relationship_roommate": -10}
                    }
                },
                "success_chance": 1.0
            },
            {
                "id": "mini_fridge",
                "text": "Buy a mini fridge for your room ($80)",
                "outcomes": {
                    "default": {
                        "text": "Problem solved. Your food is safe. But you're out $80 and it's awkward.",
                        "effects": {"money": -80, "stress": -15, "relationship_roommate": -15}
                    }
                },
                "requirements": {"money": 80},
                "success_chance": 1.0
            },
            {
                "id": "let_it_slide",
                "text": "Buy cheaper food and let them have some",
                "outcomes": {
                    "default": {
                        "text": "You keep the peace but resent them every time you see them eating YOUR food.",
                        "effects": {"stress": +5, "monthly_food_cost": -20, "relationship_roommate": +5}
                    }
                },
                "success_chance": 1.0
            }
        ],
        "impact": EventImpact.NEGATIVE,
        "unlocks_after_semester": 1,
        "can_repeat": False
    }
}

# Social Media Events
SOCIAL_MEDIA_EVENTS = {
    "viral_moment": {
        "id": "viral_moment",
        "type": EventType.SOCIAL_MEDIA,
        "title": "Your Post Went Viral!",
        "description": "That funny video you posted? 500K views overnight. Your DMs are exploding.",
        "flavor_text": "You wake up to 1,000+ notifications. Your phone is buzzing constantly. Friends are texting 'Dude you're EVERYWHERE'. Is this what fame feels like?",
        "choices": [
            {
                "id": "capitalize",
                "text": "Try to capitalize on it (start a channel/account)",
                "outcomes": {
                    "success": {
                        "text": "You gain 10K followers and land a small sponsorship deal. $500/month extra income!",
                        "effects": {"monthly_income": +500, "stress": +10, "social_status": +30, "time_per_week": -5}
                    },
                    "failure": {
                        "text": "You try to recreate the magic but... nothing hits the same. Feels forced. You gave up.",
                        "effects": {"stress": +15, "time_wasted_hours": 20}
                    }
                },
                "success_chance": 0.4
            },
            {
                "id": "enjoy_moment",
                "text": "Enjoy your 15 minutes of fame and move on",
                "outcomes": {
                    "default": {
                        "text": "You have a funny story for parties. Life returns to normal. No regrets.",
                        "effects": {"happiness": +15, "social_status": +10}
                    }
                },
                "success_chance": 1.0
            },
            {
                "id": "delete_account",
                "text": "Delete the post - too much attention!",
                "personality_match": ["introverted", "private"],
                "outcomes": {
                    "default": {
                        "text": "Fame is NOT for you. You delete everything and ghost. Peace restored.",
                        "effects": {"stress": -10, "social_status": -5}
                    }
                },
                "success_chance": 1.0
            }
        ],
        "impact": EventImpact.MIXED,
        "unlocks_after_semester": 2,
        "rarity": "rare"
    },
    
    "online_drama": {
        "id": "online_drama",
        "type": EventType.SOCIAL_MEDIA,
        "title": "Dragged into Online Drama",
        "description": "Someone screenshot your casual comment and now you're in the middle of campus Twitter drama.",
        "flavor_text": "You made a joke. Someone took it out of context. Now 500 people are debating whether you're 'problematic'. Your mentions are a war zone.",
        "choices": [
            {
                "id": "apologize_publicly",
                "text": "Post a public apology to end it",
                "outcomes": {
                    "success": {
                        "text": "People accept your apology. Drama dies down in 48 hours. You learned to be more careful online.",
                        "effects": {"stress": -20, "social_status": -10, "lesson_learned": True}
                    },
                    "failure": {
                        "text": "The apology makes it worse. 'Not a real apology!' Drama continues for a week.",
                        "effects": {"stress": +30, "social_status": -20, "time_lost_hours": 15}
                    }
                },
                "success_chance": 0.6
            },
            {
                "id": "ignore_completely",
                "text": "Ignore it completely and wait for it to blow over",
                "outcomes": {
                    "default": {
                        "text": "It takes 3 days, but people move on to the next drama. You survive.",
                        "effects": {"stress": +15, "social_status": -5}
                    }
                },
                "success_chance": 1.0
            },
            {
                "id": "double_down",
                "text": "Double down - you said nothing wrong!",
                "personality_match": ["confrontational"],
                "outcomes": {
                    "success": {
                        "text": "Your friends back you up. The mob backs down. You look strong.",
                        "effects": {"stress": +10, "social_status": +15, "enemies_made": 20}
                    },
                    "failure": {
                        "text": "You become a pariah. People avoid you. This follows you for months.",
                        "effects": {"stress": +40, "social_status": -40, "relationship_friends": -20}
                    }
                },
                "success_chance": 0.3
            },
            {
                "id": "delete_everything",
                "text": "Delete all social media and disappear",
                "outcomes": {
                    "default": {
                        "text": "Problem solved but... you're now disconnected from campus social life.",
                        "effects": {"stress": -25, "social_status": -30, "networking_opportunities": -20}
                    }
                },
                "success_chance": 1.0
            }
        ],
        "impact": EventImpact.NEGATIVE,
        "unlocks_after_semester": 2,
        "can_repeat": True
    }
}

# Mentor System Events
MENTOR_EVENTS = {
    "find_mentor": {
        "id": "find_mentor",
        "type": EventType.MENTOR,
        "title": "Professor Offers to Mentor You",
        "description": "A professor notices your work and offers to mentor you. This could change everything.",
        "flavor_text": "After class, Dr. Martinez stops you: 'Your project was exceptional. I'd like to work with you more closely. Coffee next week to discuss your future?'",
        "choices": [
            {
                "id": "accept_mentorship",
                "text": "Accept the mentorship opportunity",
                "outcomes": {
                    "default": {
                        "text": "You gain a career mentor. Research opportunities, letters of recommendation, networking connections.",
                        "effects": {
                            "has_mentor": True,
                            "internship_chance": 1.3,
                            "grad_school_chance": 1.5,
                            "professional_network": +25,
                            "stress": +5  # More opportunities = more commitment
                        }
                    }
                },
                "success_chance": 1.0
            },
            {
                "id": "decline_too_busy",
                "text": "Decline - you're too busy already",
                "outcomes": {
                    "default": {
                        "text": "You maintain your current workload. Years later, you wonder what could have been.",
                        "effects": {"opportunity_missed": True}
                    }
                },
                "success_chance": 1.0
            }
        ],
        "requirements": {
            "gpa": 3.5,
            "semester": 3
        },
        "impact": EventImpact.POSITIVE,
        "unlocks_after_semester": 3,
        "can_repeat": False
    },
    
    "mentor_recommendation": {
        "id": "mentor_recommendation",
        "type": EventType.MENTOR,
        "title": "Mentor Connects You to Dream Internship",
        "description": "Your mentor emails: 'I know someone at [Dream Company]. Sent them your resume. They want to interview you!'",
        "flavor_text": "This is it. The internship everyone applies to and no one gets. And you're getting an interview because of your mentor's network. THIS is why relationships matter.",
        "choices": [
            {
                "id": "prepare_hard",
                "text": "Spend 2 weeks preparing intensively",
                "outcomes": {
                    "success": {
                        "text": "You NAIL the interview. Offer letter arrives within days. Dream internship secured!",
                        "effects": {
                            "internship_secured": True,
                            "internship_prestige": "elite",
                            "salary_boost": 1.5,
                            "career_trajectory": +50,
                            "stress": +20  # Worth it though
                        }
                    },
                    "failure": {
                        "text": "You did well but so did 10 other candidates. They went with someone else. Still a great experience.",
                        "effects": {"interview_experience": +1, "stress": +10}
                    }
                },
                "success_chance": 0.7
            },
            {
                "id": "wing_it",
                "text": "You got this - minimal prep, rely on your skills",
                "outcomes": {
                    "success": {
                        "text": "Your natural talent shines through. They're impressed. You got it!",
                        "effects": {"internship_secured": True, "confidence": +20}
                    },
                    "failure": {
                        "text": "You stumble on technical questions. They thank you for your time. You blew it.",
                        "effects": {"stress": +30, "regret": +50, "mentor_disappointed": True}
                    }
                },
                "success_chance": 0.3
            }
        ],
        "requirements": {
            "has_mentor": True,
            "semester": 5
        },
        "impact": EventImpact.POSITIVE,
        "unlocks_after_semester": 5,
        "can_repeat": False
    }
}

# Combine all events
ALL_STORY_EVENTS = {
    **ROOMMATE_EVENTS,
    **SOCIAL_MEDIA_EVENTS,
    **MENTOR_EVENTS
}

def get_event(event_id: str) -> Optional[Dict]:
    """Get a specific story event."""
    return ALL_STORY_EVENTS.get(event_id)

def get_available_events(semester: int, player_state: Dict) -> List[Dict]:
    """
    Get list of events that can trigger based on player state.
    
    Args:
        semester: Current semester
        player_state: Player's current state (stats, relationships, etc.)
    
    Returns:
        List of available events
    """
    available = []
    
    for event_id, event in ALL_STORY_EVENTS.items():
        # Check if unlocked
        if event.get("unlocks_after_semester", 0) > semester:
            continue
        
        # Check if can repeat
        if not event.get("can_repeat", False) and player_state.get(f"seen_{event_id}", False):
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
            elif player_value != req_value:
                meets_requirements = False
                break
        
        if meets_requirements:
            available.append(event)
    
    return available

def trigger_random_event(semester: int, player_state: Dict) -> Optional[Dict]:
    """
    Randomly trigger an event appropriate for the current state.
    Respects rarity ratings.
    """
    available = get_available_events(semester, player_state)
    
    if not available:
        return None
    
    # Weight by rarity
    common_events = [e for e in available if e.get("rarity") != "rare"]
    rare_events = [e for e in available if e.get("rarity") == "rare"]
    
    # 80% common, 20% rare
    if rare_events and random.random() < 0.2:
        return random.choice(rare_events)
    elif common_events:
        return random.choice(common_events)
    
    return None

def process_choice(event_id: str, choice_id: str, player_state: Dict) -> Dict:
    """
    Process a player's choice and return the outcome with effects.
    
    Returns:
        {
            "outcome_text": str,
            "effects": Dict,
            "success": bool
        }
    """
    event = get_event(event_id)
    if not event:
        return {"error": "Event not found"}
    
    # Find the choice
    choice = None
    for c in event.get("choices", []):
        if c["id"] == choice_id:
            choice = c
            break
    
    if not choice:
        return {"error": "Choice not found"}
    
    # Determine outcome
    success_chance = choice.get("success_chance", 1.0)
    success = random.random() < success_chance
    
    outcomes = choice.get("outcomes", {})
    
    if success and "success" in outcomes:
        outcome = outcomes["success"]
    elif not success and "failure" in outcomes:
        outcome = outcomes["failure"]
    else:
        outcome = outcomes.get("default", {})
    
    return {
        "outcome_text": outcome.get("text", ""),
        "effects": outcome.get("effects", {}),
        "success": success
    }
