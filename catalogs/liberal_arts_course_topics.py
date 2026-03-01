"""
Enhanced Liberal Arts Course Topics.
Provides detailed topic descriptions for liberal arts (lib*) course IDs.
"""

from typing import Dict, Any

LIBERAL_ARTS_TOPICS: Dict[str, Dict[str, Any]] = {
    "lib101": {
        "title": "Critical Thinking",
        "description": "Build logic, argument analysis, and evidence-based reasoning skills.",
        "key_topics": [
            {
                "name": "Arguments and Claims",
                "description": "Distinguishing conclusions, premises, and supporting evidence.",
                "real_world": "How do you evaluate whether a viral social media claim is credible?"
            },
            {
                "name": "Logical Fallacies",
                "description": "Recognizing common reasoning errors in debates and media.",
                "real_world": "How can identifying strawman and ad hominem fallacies improve decisions?"
            },
            {
                "name": "Source Evaluation",
                "description": "Assessing reliability, bias, and context of information sources.",
                "real_world": "Why should policy decisions rely on peer-reviewed evidence over opinion blogs?"
            },
            {
                "name": "Structured Reasoning",
                "description": "Using deductive and inductive approaches to build sound conclusions.",
                "real_world": "How do product teams reason from user interviews to roadmap priorities?"
            },
            {
                "name": "Decision Frameworks",
                "description": "Applying criteria and tradeoff analysis to complex choices.",
                "real_world": "How do city planners weigh cost, equity, and sustainability in transit plans?"
            },
        ],
    },
    "lib201": {
        "title": "Philosophy",
        "description": "Explore ethics, knowledge, and major schools of philosophical thought.",
        "key_topics": [
            {
                "name": "Ethical Theories",
                "description": "Utilitarian, deontological, and virtue-ethics approaches.",
                "real_world": "How should autonomous vehicles prioritize outcomes in no-win scenarios?"
            },
            {
                "name": "Epistemology",
                "description": "How we justify beliefs and distinguish knowledge from opinion.",
                "real_world": "What standards should journalists use before publishing sensitive stories?"
            },
            {
                "name": "Free Will and Responsibility",
                "description": "Debates about agency, determinism, and accountability.",
                "real_world": "How do legal systems treat intent versus circumstance in sentencing?"
            },
            {
                "name": "Political Philosophy",
                "description": "Justice, rights, liberty, and social contract perspectives.",
                "real_world": "How should societies balance privacy with public safety?"
            },
            {
                "name": "Philosophy of Mind",
                "description": "Consciousness, identity, and mind-body questions.",
                "real_world": "Can advanced AI be considered morally significant?"
            },
        ],
    },
    "lib301": {
        "title": "Art History",
        "description": "Analyze artistic movements, cultural context, and visual interpretation.",
        "key_topics": [
            {
                "name": "Major Art Movements",
                "description": "Renaissance, Baroque, Modernism, and contemporary trends.",
                "real_world": "How do design teams borrow from historical styles in branding?"
            },
            {
                "name": "Visual Analysis",
                "description": "Reading composition, color, symbolism, and technique.",
                "real_world": "Why do museum labels highlight composition and symbolism for visitors?"
            },
            {
                "name": "Art and Power",
                "description": "How institutions and patrons shape artistic production.",
                "real_world": "How do sponsorships and galleries influence which artists gain visibility?"
            },
            {
                "name": "Global Perspectives",
                "description": "Comparing art traditions across regions and time periods.",
                "real_world": "How can global exhibitions challenge Western-centric narratives?"
            },
            {
                "name": "Cultural Memory",
                "description": "Art as archive of identity, conflict, and social change.",
                "real_world": "How do public monuments shape collective memory?"
            },
        ],
    },
    "lib401": {
        "title": "Ethics and Society",
        "description": "Apply ethical reasoning to modern social, policy, and technology issues.",
        "key_topics": [
            {
                "name": "Applied Ethics",
                "description": "Using ethical frameworks in medicine, business, and governance.",
                "real_world": "How should hospitals allocate scarce resources during emergencies?"
            },
            {
                "name": "Justice and Equity",
                "description": "Evaluating fairness in institutions and policy outcomes.",
                "real_world": "How do scholarship policies affect educational access?"
            },
            {
                "name": "Technology Ethics",
                "description": "Bias, transparency, and accountability in data-driven systems.",
                "real_world": "How should companies audit hiring algorithms for bias?"
            },
            {
                "name": "Civic Responsibility",
                "description": "Citizenship, participation, and ethical public discourse.",
                "real_world": "How can communities engage constructively in local planning debates?"
            },
            {
                "name": "Policy Tradeoffs",
                "description": "Balancing competing values in public decision-making.",
                "real_world": "How do lawmakers trade off climate goals with short-term economic pressure?"
            },
        ],
    },
}


def get_liberal_arts_topics(course_id: str) -> Dict[str, Any]:
    """Get detailed topics for liberal arts course."""
    return LIBERAL_ARTS_TOPICS.get(course_id, {})


def _topic_icon(topic_name: str) -> str:
    """Topic icon mapping for liberal arts themes."""
    icon_map = {
        "argument": "🧠",
        "logical": "🔎",
        "source": "📚",
        "reasoning": "🧩",
        "decision": "⚖️",
        "ethical": "🤝",
        "epistemology": "💭",
        "justice": "🏛️",
        "mind": "🧠",
        "art": "🎨",
        "visual": "🖼️",
        "culture": "🌍",
        "memory": "🗿",
        "technology": "💻",
        "civic": "🗳️",
        "policy": "📜",
    }
    name = topic_name.lower()
    for key, icon in icon_map.items():
        if key in name:
            return icon
    return "📖"


def format_liberal_arts_topics(course_id: str) -> Dict[str, Any]:
    """Format liberal arts topics for frontend display."""
    course_data = get_liberal_arts_topics(course_id)
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
            f"Evaluate: {topic['name']}" if i % 2 == 0 else f"Discuss: {topic['description']}"
            for i, topic in enumerate(course_data.get("key_topics", []))
        ][:5],
    }
