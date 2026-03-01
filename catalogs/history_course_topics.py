"""
Enhanced History Course Topics.
Provides detailed topic descriptions for history (hist*) course IDs.
"""

from typing import Dict, Any

HISTORY_TOPICS: Dict[str, Dict[str, Any]] = {
    "hist101": {
        "title": "World History to 1500",
        "description": "Ancient civilizations through medieval period globally.",
        "key_topics": [
            {
                "name": "Ancient Civilizations",
                "description": "Mesopotamia, Egypt, Indus, China, Mesoamerica.",
                "real_world": "How did early writing systems preserve knowledge for future generations?"
            },
            {
                "name": "Classical Antiquity",
                "description": "Greece, Rome, Persia, and classical philosophical traditions.",
                "real_world": "How did Greek democracy influence modern political systems?"
            },
            {
                "name": "Religious Transformations",
                "description": "Rise of Buddhism, Christianity, Islam, and their spread.",
                "real_world": "How did trade routes spread religions across continents?"
            },
            {
                "name": "Medieval Societies",
                "description": "Feudalism, kingdoms, empires, and cultural developments.",
                "real_world": "How did feudal systems organize medieval European life?"
            },
            {
                "name": "Global Contacts",
                "description": "Silk Road, Indian Ocean trade, and cross-cultural exchange.",
                "real_world": "How did trade networks connect distant civilizations?"
            },
        ],
    },
    "hist201": {
        "title": "World History 1500-Present",
        "description": "Early modern through contemporary global history.",
        "key_topics": [
            {
                "name": "Age of Exploration",
                "description": "European expansion, colonialism, and global encounters.",
                "real_world": "How did Columbus's voyage reshape global history?"
            },
            {
                "name": "Revolutions",
                "description": "Scientific, political, and industrial transformations.",
                "real_world": "Why did the Industrial Revolution begin in Britain?"
            },
            {
                "name": "Nationalism and Imperialism",
                "description": "Nation-states, empire building, and colonization.",
                "real_world": "How did imperial powers justify colonizing other territories?"
            },
            {
                "name": "World Wars and Ideologies",
                "description": "WWI, WWII, fascism, communism, and decolonization.",
                "real_world": "How did totalitarian ideologies mobilize millions?"
            },
            {
                "name": "Cold War and Globalization",
                "description": "Bipolar conflict, decolonization, and interconnected world.",
                "real_world": "How did the Cold War shape geopolitics for decades?"
            },
        ],
    },
    "hist301": {
        "title": "American History",
        "description": "Indigenous North America through contemporary United States.",
        "key_topics": [
            {
                "name": "Native America",
                "description": "Pre-Columbian societies, colonialism, and indigenous resilience.",
                "real_world": "How did Native Americans adapt to European colonization?"
            },
            {
                "name": "Colonial Period",
                "description": "European settlement, slavery, and tensions with Britain.",
                "real_world": "How did slavery shape colonial economies and society?"
            },
            {
                "name": "Revolution and Constitution",
                "description": "American independence, founding era, and constitutional framework.",
                "real_world": "Why did the Founders build in checks and balances?"
            },
            {
                "name": "Expansion and Slavery",
                "description": "Westward expansion, territorial disputes, and sectional conflict.",
                "real_world": "How did slavery expand with westward expansion?"
            },
            {
                "name": "Civil War to Present",
                "description": "Civil War, reconstruction, industrialization, and modern era.",
                "real_world": "How did Civil War and Reconstruction reshape the nation?"
            },
        ],
    },
    "hist401": {
        "title": "Historical Methods",
        "description": "Research, interpretation, evidence, and historical practice.",
        "key_topics": [
            {
                "name": "Primary Sources",
                "description": "Documents, artifacts, oral histories, and authentication.",
                "real_world": "How do historians verify the authenticity of ancient texts?"
            },
            {
                "name": "Interpretation",
                "description": "Bias, perspective, counterfactuals, and historical debate.",
                "real_world": "Can different historians legitimately disagree about the same events?"
            },
            {
                "name": "Causation",
                "description": "Cause and effect, contingency, and structural explanations.",
                "real_world": "Did individual leaders cause wars or did circumstances?"
            },
            {
                "name": "Historical Narratives",
                "description": "Story structure, periodization, and interpretive frameworks.",
                "real_world": "How do historians select which stories count as history?"
            },
            {
                "name": "Digital History",
                "description": "Archives, mapping, data analysis, and digital humanities.",
                "real_world": "How do digital tools reveal patterns in historical data?"
            },
        ],
    },
}


def get_history_topics(course_id: str) -> Dict[str, Any]:
    """Get detailed topics for history course."""
    return HISTORY_TOPICS.get(course_id, {})


def _topic_icon(topic_name: str) -> str:
    """Topic icon mapping for history themes."""
    icon_map = {
        "ancient": "🏺",
        "civilization": "🏛️",
        "classical": "🏛️",
        "religious": "🙏",
        "medieval": "🏰",
        "contact": "🤝",
        "exploration": "🧭",
        "revolution": "⚡",
        "nationalism": "🚩",
        "imperialism": "🌍",
        "war": "⚔️",
        "ideology": "💡",
        "cold": "❄️",
        "native": "🌲",
        "colonial": "🚢",
        "constitution": "📜",
        "expansion": "📈",
        "slavery": "⛓️",
        "civil": "🏛️",
        "primary": "📖",
        "interpretation": "🤔",
        "causation": "⛓️",
        "narrative": "📚",
        "digital": "💻",
    }
    name = topic_name.lower()
    for key, icon in icon_map.items():
        if key in name:
            return icon
    return "📚"


def format_history_topics(course_id: str) -> Dict[str, Any]:
    """Format history topics for frontend display."""
    course_data = get_history_topics(course_id)
    if not course_data:
        return {
            "course_id": course_id,
            "found": False,
            "message": f"Topics not yet available for {course_id}",
        }

    return {
        "course_id": course_id,
        "title": course_data.get("title", ""),
        "description": course_data.get("description", ""),
        "found": True,
        "topics": [
            {
                "name": topic["name"],
                "description": topic["description"],
                "real_world": topic["real_world"],
                "icon": _topic_icon(topic["name"]),
            }
            for topic in course_data.get("key_topics", [])
        ],
        "learning_outcomes": [
            f"Contextualize: {topic['name']}" if i % 2 == 0 else f"Evaluate: {topic['description']}"
            for i, topic in enumerate(course_data.get("key_topics", []))
        ][:5],
    }
