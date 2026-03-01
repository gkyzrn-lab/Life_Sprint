"""
Enhanced Political Science Course Topics.
Provides detailed topic descriptions for political science (pol*) course IDs.
"""

from typing import Dict, Any

POLITICAL_SCIENCE_TOPICS: Dict[str, Dict[str, Any]] = {
    "pol101": {
        "title": "Intro to Political Science",
        "description": "Governments, institutions, and comparative political systems.",
        "key_topics": [
            {
                "name": "Government Systems",
                "description": "Democracy, autocracy, oligarchy, and hybrid systems.",
                "real_world": "How do democratic and authoritarian governments differ in accountability?"
            },
            {
                "name": "Political Institutions",
                "description": "Executive, legislative, judicial branches and separation of powers.",
                "real_world": "Why do checks and balances prevent concentration of government power?"
            },
            {
                "name": "Political Ideologies",
                "description": "Liberalism, conservatism, socialism, and emerging movements.",
                "real_world": "How do different ideologies approach healthcare and education policy?"
            },
            {
                "name": "Sovereignty and States",
                "description": "Nation-states, international law, and territorial control.",
                "real_world": "What gives governments legitimate authority over their territory?"
            },
            {
                "name": "Political Culture",
                "description": "Values, norms, identity, and citizen participation.",
                "real_world": "How do voting rates and civic engagement vary across democracies?"
            },
        ],
    },
    "pol201": {
        "title": "International Relations",
        "description": "States, conflict, cooperation, and global governance.",
        "key_topics": [
            {
                "name": "Power and Conflict",
                "description": "Realism, liberalism, constructivism, and conflict theories.",
                "real_world": "Why do nations accumulate military power despite mutual destruction risks?"
            },
            {
                "name": "Diplomacy and Negotiation",
                "description": "Treaties, alliances, bargaining, and diplomatic strategies.",
                "real_world": "How do diplomatic channels prevent escalation of international crises?"
            },
            {
                "name": "International Organizations",
                "description": "UN, NATO, EU, and multilateral cooperation structures.",
                "real_world": "Can international institutions enforce peace when national interests conflict?"
            },
            {
                "name": "Global Issues",
                "description": "Climate change, migration, trade, and transnational problems.",
                "real_world": "Why is climate change a commons problem requiring international cooperation?"
            },
            {
                "name": "Geopolitics",
                "description": "Regional powers, strategic interests, and global competition.",
                "real_world": "How do geographic factors shape regional power dynamics?"
            },
        ],
    },
    "pol301": {
        "title": "American Government",
        "description": "Constitutional structure, federalism, and U.S. institutions.",
        "key_topics": [
            {
                "name": "Constitution and Rights",
                "description": "Constitutional framework, amendments, and civil liberties.",
                "real_world": "How do courts balance security with privacy rights?"
            },
            {
                "name": "Federalism",
                "description": "Separation of powers, state/federal relations, and dual sovereignty.",
                "real_world": "Why do states sometimes resist federal mandates?"
            },
            {
                "name": "Congress",
                "description": "Legislative process, committees, parties, and representation.",
                "real_world": "How does gerrymandering influence election outcomes?"
            },
            {
                "name": "Presidency",
                "description": "Executive power, appointments, vetoes, and commander-in-chief role.",
                "real_world": "How constrained is presidential power by Congress and courts?"
            },
            {
                "name": "Courts and Justice",
                "description": "Judicial review, federalism in courts, and constitutional interpretation.",
                "real_world": "How do Supreme Court justices shape constitutional meaning?"
            },
        ],
    },
    "pol401": {
        "title": "Political Theory",
        "description": "Classic and contemporary theories of justice, power, and society.",
        "key_topics": [
            {
                "name": "Classical Theory",
                "description": "Hobbes, Locke, Rousseau, and social contract traditions.",
                "real_world": "Why do social contracts require citizens to surrender some freedoms?"
            },
            {
                "name": "Modern Ideologies",
                "description": "Marxism, feminism, postcolonialism, and critical theories.",
                "real_world": "How do power structures perpetuate inequality across generations?"
            },
            {
                "name": "Justice and Equality",
                "description": "Distributive justice, rights, desert, and fair opportunity.",
                "real_world": "What makes an economic system just or unfair?"
            },
            {
                "name": "Democracy Theory",
                "description": "Representation, participation, deliberation, and legitimacy.",
                "real_world": "Can democracies survive when citizens lose faith in institutions?"
            },
            {
                "name": "Political Identity",
                "description": "Nationalism, ethnicity, religion, and collective identity.",
                "real_world": "How do identity cleavages shape political conflict and alignment?"
            },
        ],
    },
}


def get_political_science_topics(course_id: str) -> Dict[str, Any]:
    """Get detailed topics for political science course."""
    return POLITICAL_SCIENCE_TOPICS.get(course_id, {})


def _topic_icon(topic_name: str) -> str:
    """Topic icon mapping for political science themes."""
    icon_map = {
        "government": "🏛️",
        "institution": "📋",
        "ideology": "💡",
        "sovereignty": "🌍",
        "culture": "🎭",
        "power": "⚔️",
        "conflict": "⚠️",
        "diplomacy": "🤝",
        "organization": "🔗",
        "global": "🌐",
        "geopolitics": "🗺️",
        "constitution": "📜",
        "rights": "✊",
        "federalism": "🏗️",
        "congress": "🏢",
        "presidency": "👑",
        "court": "⚖️",
        "justice": "🏛️",
        "theory": "📖",
        "democracy": "🗳️",
        "identity": "👥",
    }
    name = topic_name.lower()
    for key, icon in icon_map.items():
        if key in name:
            return icon
    return "🏛️"


def format_political_science_topics(course_id: str) -> Dict[str, Any]:
    """Format political science topics for frontend display."""
    course_data = get_political_science_topics(course_id)
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
            f"Analyze: {topic['name']}" if i % 2 == 0 else f"Evaluate: {topic['description']}"
            for i, topic in enumerate(course_data.get("key_topics", []))
        ][:5],
    }
