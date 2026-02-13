# Health narrative moments and story events
# These provide emotional context and celebrate/warn players about their choices

HEALTH_STORIES = {
    # Positive moments
    "first_exercise_high": {
        "id": "first_exercise_high",
        "trigger": "just_exercised",
        "condition": "exercises_this_semester == 1",
        "title": "The Endorphin Rush",
        "message": "💪 You finish your workout and feel... different. Better. Your body feels lighter, your mind clearer. This is what people mean by 'runner's high.' You get it now.",
        "effects": {
            "happiness_bonus": 5.0,
            "mental_health_bonus": 3.0,
        },
        "tone": "triumphant",
    },
    "streak_milestone": {
        "id": "streak_milestone",
        "trigger": "streak_reached",
        "condition": "exercise_streak >= 3",
        "title": "You're On Fire! 🔥",
        "message": "Three days in a row. You've never stuck with something this long. Part of you wants to celebrate, another part realizes: 'I can actually do hard things.'",
        "effects": {
            "confidence_boost": 8.0,
            "happiness_bonus": 6.0,
        },
        "tone": "empowering",
    },
    "realization_health_gpa": {
        "id": "realization_health_gpa",
        "trigger": "gpa_boost_from_health",
        "condition": "health > 75 AND gpa_increased",
        "title": "The Connection",
        "message": "You notice your GPA went up. Your energy is better. You're sleeping better. Your grades improved. It clicks: Taking care of your body isn't separate from taking care of your future. It IS taking care of your future.",
        "effects": {
            "motivation_boost": 10.0,
            "stress_reduction": 5.0,
        },
        "tone": "revelatory",
    },
    "therapy_breakthrough": {
        "id": "therapy_breakthrough",
        "trigger": "attended_therapy",
        "condition": "stress > 60",
        "title": "Someone Gets It",
        "message": "You sit across from the counselor and just... talk. About stress. About college. About being scared. And instead of judgment, you hear: 'That's completely normal. You're not alone. And it's okay to struggle.' You feel lighter.",
        "effects": {
            "stress_reduction": 12.0,
            "mental_health_bonus": 8.0,
            "happiness_bonus": 7.0,
        },
        "tone": "supportive",
    },
    "checkup_relief": {
        "id": "checkup_relief",
        "trigger": "completed_checkup",
        "condition": "health_concern_present",
        "title": "Peace of Mind",
        "message": "The doctor says you're fine. Better than fine—you're actually quite healthy. The relief washes over you. Sometimes knowing you're okay is all you need.",
        "effects": {
            "stress_reduction": 8.0,
            "health_bonus": 5.0,
            "happiness_bonus": 5.0,
        },
        "tone": "reassuring",
    },
    
    # Warning moments
    "stress_warning": {
        "id": "stress_warning",
        "trigger": "high_stress_alert",
        "condition": "stress > 75",
        "title": "⚠️ You're Overwhelmed",
        "message": "Your shoulders are tense. You can't sleep. Everything feels urgent and impossible. You're spiraling. This is what anxiety feels like. You need help—not weakness, but wisdom. Consider talking to someone.",
        "effects": {
            "unlock_therapy_reminder": True,
            "health_warning": True,
        },
        "tone": "cautionary",
    },
    "burnout_spiral": {
        "id": "burnout_spiral",
        "trigger": "burnout_detected",
        "condition": "stress > 85 AND health < 40",
        "title": "🚨 BURNOUT ALERT",
        "message": "You're not fine. You haven't exercised in weeks. Your sleep is destroyed. Everything hurts. Your grades are dropping. You're caught in a spiral, and you can't see a way out. This is burnout. It's serious. Get help NOW.",
        "effects": {
            "force_intervention": True,
            "gpa_penalty": -0.3,
            "emergency_counselor_contact": True,
        },
        "tone": "urgent",
    },
    "illness_comedown": {
        "id": "illness_comedown",
        "trigger": "got_sick",
        "condition": "condition_applied",
        "title": "🤒 You're Not Feeling Well",
        "message": "A headache. A scratchy throat. That feeling in your chest. You're getting sick. Your body is telling you it needs a break. Listen to it. Rest matters.",
        "effects": {
            "health_penalty": -15.0,
            "gpa_penalty": -0.15,
            "reminder_to_rest": True,
        },
        "tone": "cautionary",
    },
    "recovery_progress": {
        "id": "recovery_progress",
        "trigger": "condition_improving",
        "condition": "condition_duration_reduced",
        "title": "Getting Better 💚",
        "message": "You're on the mend. Your body is healing. You're taking it easy, and that matters. Recovery isn't weakness—it's wisdom.",
        "effects": {
            "morale_boost": 4.0,
            "mental_health_bonus": 3.0,
        },
        "tone": "encouraging",
    },
    
    # Social awareness
    "friend_support": {
        "id": "friend_support",
        "trigger": "social_moment",
        "condition": "exercised_recently AND therapy_recent",
        "title": "Friends Notice",
        "message": "Your friend says: 'You seem different. Happier. What's going on?' You realize people can see when you're taking care of yourself. That matters.",
        "effects": {
            "social_bonus": 6.0,
            "happiness_bonus": 4.0,
            "confidence_bonus": 3.0,
        },
        "tone": "validating",
    },
    "family_concern": {
        "id": "family_concern",
        "trigger": "neglect_warning",
        "condition": "health < 30",
        "title": "Your Family's Worried",
        "message": "You see a text from home: 'Are you okay? You seem stressed.' They can see it even from far away. It reminds you that people care. You're not alone.",
        "effects": {
            "emotional_support": 5.0,
            "motivation_boost": 4.0,
        },
        "tone": "touching",
    },
}

# Story tones for UI
STORY_TONES = {
    "triumphant": {"emoji": "🌟", "color": "#FFD700"},
    "empowering": {"emoji": "⭐", "color": "#FFB6C1"},
    "revelatory": {"emoji": "💡", "color": "#87CEEB"},
    "supportive": {"emoji": "💚", "color": "#90EE90"},
    "reassuring": {"emoji": "✨", "color": "#DDA0DD"},
    "cautionary": {"emoji": "⚠️", "color": "#FFA500"},
    "urgent": {"emoji": "🚨", "color": "#FF6347"},
    "encouraging": {"emoji": "💪", "color": "#32CD32"},
    "validating": {"emoji": "👍", "color": "#4169E1"},
    "touching": {"emoji": "❤️", "color": "#FF69B4"},
}
