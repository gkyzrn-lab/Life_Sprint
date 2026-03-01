"""
Enhanced Biology Course Topics.
Provides detailed topic descriptions for biology (bio*) course IDs.
"""

from typing import Dict, Any

BIOLOGY_TOPICS: Dict[str, Dict[str, Any]] = {
    "bio101": {
        "title": "Intro to Biology",
        "description": "Cell biology, genetics, evolution, and ecology foundations.",
        "key_topics": [
            {
                "name": "Cell Structure",
                "description": "Prokaryotic and eukaryotic cells, organelles, and function.",
                "real_world": "How do plant and animal cells differ in structure and survival needs?"
            },
            {
                "name": "Genetics",
                "description": "DNA, genes, inheritance patterns, and molecular basis of heredity.",
                "real_world": "How do mutations create genetic variation for natural selection?"
            },
            {
                "name": "Evolution",
                "description": "Natural selection, adaptation, speciation, and evolutionary history.",
                "real_world": "How do fossils and DNA evidence trace the evolution of species?"
            },
            {
                "name": "Photosynthesis and Respiration",
                "description": "Energy transfer in cells, ATP, and metabolic pathways.",
                "real_world": "How do plants convert sunlight into chemical energy for growth?"
            },
            {
                "name": "Ecology",
                "description": "Populations, communities, biomes, and ecosystem dynamics.",
                "real_world": "How do predator-prey relationships maintain ecosystem balance?"
            },
        ],
    },
    "bio201": {
        "title": "Molecular Biology",
        "description": "Protein synthesis, gene expression, and cell signaling.",
        "key_topics": [
            {
                "name": "Central Dogma",
                "description": "DNA replication, transcription, and translation.",
                "real_world": "How does mRNA carry genetic instructions from DNA to ribosomes?"
            },
            {
                "name": "Gene Expression",
                "description": "Regulation, epigenetics, and environmental influences.",
                "real_world": "How do identical twins develop different traits despite same DNA?"
            },
            {
                "name": "Protein Structure",
                "description": "Amino acids, folding, domains, and functional relationships.",
                "real_world": "Why do misfolded proteins cause diseases like Alzheimer's?"
            },
            {
                "name": "Cell Signaling",
                "description": "Receptors, transduction, second messengers, and response.",
                "real_world": "How do hormones trigger specific cellular responses?"
            },
            {
                "name": "Biotechnology",
                "description": "Genetic engineering, cloning, and synthetic biology.",
                "real_world": "How do CRISPR techniques edit genes to cure genetic diseases?"
            },
        ],
    },
    "bio301": {
        "title": "Ecology and Conservation",
        "description": "Population dynamics, community interactions, and conservation biology.",
        "key_topics": [
            {
                "name": "Population Ecology",
                "description": "Growth models, carrying capacity, and limiting factors.",
                "real_world": "How do fisheries use population models to prevent overfishing?"
            },
            {
                "name": "Community Ecology",
                "description": "Competition, predation, symbiosis, and succession.",
                "real_world": "Why do invasive species disrupt native community balances?"
            },
            {
                "name": "Ecosystem Services",
                "description": "Energy flow, nutrient cycling, and biodiversity roles.",
                "real_world": "How do wetlands filter water and reduce flooding?"
            },
            {
                "name": "Conservation Strategies",
                "description": "Protected areas, breeding programs, and restoration.",
                "real_world": "How have species like California condors been brought back?"
            },
            {
                "name": "Climate Change",
                "description": "Anthropogenic impacts, adaptation, and mitigation.",
                "real_world": "How are organisms adapting migration and hibernation patterns?"
            },
        ],
    },
    "bio401": {
        "title": "Human Physiology",
        "description": "Organ systems, homeostasis, and integrated body function.",
        "key_topics": [
            {
                "name": "Nervous System",
                "description": "Neurons, synapses, action potentials, and signal integration.",
                "real_world": "How do neurotransmitters enable thoughts and emotions?"
            },
            {
                "name": "Cardiovascular System",
                "description": "Heart, blood vessels, circulation, and regulation.",
                "real_world": "Why does exercise strengthen the heart muscle?"
            },
            {
                "name": "Respiratory System",
                "description": "Gas exchange, ventilation, and oxygen transport.",
                "real_world": "How do high-altitude adaptations increase oxygen carrying?"
            },
            {
                "name": "Immune System",
                "description": "Innate and adaptive immunity, antibodies, and vaccines.",
                "real_world": "How do vaccines prepare immunity before exposure to pathogens?"
            },
            {
                "name": "Homeostasis",
                "description": "Temperature, pH, osmotic balance, and feedback mechanisms.",
                "real_world": "How does shivering maintain body temperature in cold?"
            },
        ],
    },
}


def get_biology_topics(course_id: str) -> Dict[str, Any]:
    """Get detailed topics for biology course."""
    return BIOLOGY_TOPICS.get(course_id, {})


def _topic_icon(topic_name: str) -> str:
    """Topic icon mapping for biology themes."""
    icon_map = {
        "cell": "🔬",
        "structure": "🏗️",
        "genetics": "🧬",
        "evolution": "🌳",
        "photosynthesis": "🌱",
        "respiration": "💨",
        "ecology": "🌍",
        "dogma": "📖",
        "expression": "⚙️",
        "protein": "🧪",
        "signaling": "📡",
        "biotechnology": "🔧",
        "population": "👥",
        "community": "🤝",
        "ecosystem": "🌲",
        "conservation": "♻️",
        "nervous": "🧠",
        "cardiovascular": "❤️",
        "respiratory": "💨",
        "immune": "🛡️",
        "homeostasis": "⚖️",
    }
    name = topic_name.lower()
    for key, icon in icon_map.items():
        if key in name:
            return icon
    return "🔬"


def format_biology_topics(course_id: str) -> Dict[str, Any]:
    """Format biology topics for frontend display."""
    course_data = get_biology_topics(course_id)
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
            f"Explain: {topic['name']}" if i % 2 == 0 else f"Evaluate: {topic['description']}"
            for i, topic in enumerate(course_data.get("key_topics", []))
        ][:5],
    }
