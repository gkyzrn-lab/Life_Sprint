"""
Enhanced Psychology Course Topics.
Provides detailed topic descriptions for psychology (psych*) course IDs.
"""

from typing import Dict, Any

PSYCHOLOGY_TOPICS: Dict[str, Dict[str, Any]] = {
    "psych101": {
        "title": "Intro to Psychology",
        "description": "Psychological foundations covering brain, behavior, cognition, and development.",
        "key_topics": [
            {
                "name": "Neurobiology",
                "description": "Brain structure, neurotransmitters, and neural communication.",
                "real_world": "How do antidepressants work by affecting neurotransmitter levels?"
            },
            {
                "name": "Sensation and Perception",
                "description": "How sensory systems encode and brain interprets the world.",
                "real_world": "Why do optical illusions reveal how perception constructs reality?"
            },
            {
                "name": "Learning and Memory",
                "description": "Classical/operant conditioning, memory systems, and forgetting.",
                "real_world": "How do spacing effects in study schedules improve retention?"
            },
            {
                "name": "Motivation and Emotion",
                "description": "Drives, rewards, emotional regulation, and well-being.",
                "real_world": "Why do intrinsic motivations engage people more than external rewards?"
            },
            {
                "name": "Development Across Lifespan",
                "description": "Physical, cognitive, and social changes from infancy to aging.",
                "real_world": "How do developmental stages inform parenting and education strategies?"
            },
        ],
    },
    "psych201": {
        "title": "Research Methods",
        "description": "Experimental design, measurement, and statistical analysis for psychology.",
        "key_topics": [
            {
                "name": "Research Design",
                "description": "Experiments, quasi-experiments, correlational, and qualitative methods.",
                "real_world": "Why are randomized controlled trials the gold standard in psychology?"
            },
            {
                "name": "Measurement",
                "description": "Validity, reliability, and ethical testing considerations.",
                "real_world": "How do IQ tests balance standardization with cultural fairness?"
            },
            {
                "name": "Statistical Analysis",
                "description": "Inferential statistics, effect sizes, and power analysis.",
                "real_world": "Why do small-sample studies with large effects deserve publication?"
            },
            {
                "name": "Ethics in Research",
                "description": "Informed consent, confidentiality, and institutional review.",
                "real_world": "What protections guard vulnerable participants in psychological studies?"
            },
            {
                "name": "Data Visualization",
                "description": "Communicating research findings effectively to audiences.",
                "real_world": "How do researchers choose visualizations that convey findings honestly?"
            },
        ],
    },
    "psych301": {
        "title": "Cognitive Psychology",
        "description": "Mental processes including attention, language, problem-solving, and reasoning.",
        "key_topics": [
            {
                "name": "Attention",
                "description": "Selective attention, divided attention, and attentional blink.",
                "real_world": "Why are multitasking drivers so dangerous even when 'experienced'?"
            },
            {
                "name": "Memory Systems",
                "description": "Encoding, storage, retrieval, and forgetting mechanisms.",
                "real_world": "How do eyewitness memories become distorted over time?"
            },
            {
                "name": "Language",
                "description": "Linguistics, comprehension, production, and bilingualism.",
                "real_world": "How do deaf individuals without sign language develop language?"
            },
            {
                "name": "Problem-Solving",
                "description": "Algorithms, heuristics, insight, and overcoming mental sets.",
                "real_world": "Why do creative breaks help solve problems stuck in conventional thinking?"
            },
            {
                "name": "Reasoning and Judgment",
                "description": "Logic, biases, heuristics, and decision-making failures.",
                "real_world": "Why do anchoring effects manipulate prices in negotiations?"
            },
        ],
    },
    "psych401": {
        "title": "Social Psychology",
        "description": "Influence of society on individuals: attitudes, groups, and relationships.",
        "key_topics": [
            {
                "name": "Attitudes and Persuasion",
                "description": "Belief formation, attitude change, and resistance.",
                "real_world": "Why are central-route arguments more lasting than emotional appeals?"
            },
            {
                "name": "Conformity and Obedience",
                "description": "Social pressure, group influence, and authority compliance.",
                "real_world": "What made ordinary people obey harmful commands in Milgram's studies?"
            },
            {
                "name": "Group Dynamics",
                "description": "Cooperation, competition, leadership, and collective behavior.",
                "real_world": "How does social facilitation improve performance on easy tasks?"
            },
            {
                "name": "Interpersonal Attraction",
                "description": "Friendship, love, attachment, and relationship patterns.",
                "real_world": "Why do we prefer people similar to ourselves in background?"
            },
            {
                "name": "Prejudice and Stereotyping",
                "description": "Bias formation, discrimination, and intergroup relations.",
                "real_world": "How do contact and cooperation reduce prejudice across groups?"
            },
        ],
    },
}


def get_psychology_topics(course_id: str) -> Dict[str, Any]:
    """Get detailed topics for psychology course."""
    return PSYCHOLOGY_TOPICS.get(course_id, {})


def _topic_icon(topic_name: str) -> str:
    """Topic icon mapping for psychology themes."""
    icon_map = {
        "neuro": "🧠",
        "sensation": "👁️",
        "learning": "📚",
        "memory": "💭",
        "emotion": "😊",
        "development": "👶",
        "research": "🔬",
        "measurement": "📏",
        "ethics": "⚖️",
        "attention": "👀",
        "language": "🗣️",
        "problem": "🧩",
        "reasoning": "🤔",
        "attitude": "💭",
        "conformity": "👥",
        "attraction": "💖",
        "prejudice": "⚠️",
    }
    name = topic_name.lower()
    for key, icon in icon_map.items():
        if key in name:
            return icon
    return "🧠"


def format_psychology_topics(course_id: str) -> Dict[str, Any]:
    """Format psychology topics for frontend display."""
    course_data = get_psychology_topics(course_id)
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
            f"Analyze: {topic['name']}" if i % 2 == 0 else f"Apply: {topic['description']}"
            for i, topic in enumerate(course_data.get("key_topics", []))
        ][:5],
    }
