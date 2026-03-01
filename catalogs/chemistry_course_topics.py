"""
Enhanced Chemistry Course Topics.
Provides detailed topic descriptions for chemistry (chem*) course IDs.
"""

from typing import Dict, Any

CHEMISTRY_TOPICS: Dict[str, Dict[str, Any]] = {
    "chem101": {
        "title": "Intro to Chemistry",
        "description": "Atomic structure, chemical bonding, and stoichiometry.",
        "key_topics": [
            {
                "name": "Atomic Structure",
                "description": "Electrons, orbitals, periodic trends, and quantum numbers.",
                "real_world": "How do electron configurations explain why metals conduct electricity?"
            },
            {
                "name": "Chemical Bonding",
                "description": "Ionic, covalent, and metallic bonds with molecular geometry.",
                "real_world": "Why is water bent and how does this shape affect its properties?"
            },
            {
                "name": "Stoichiometry",
                "description": "Mole concept, balancing equations, and limiting reagents.",
                "real_world": "How do chemists calculate exact amounts of reactants needed?"
            },
            {
                "name": "States of Matter",
                "description": "Gases, liquids, solids, and phase transitions.",
                "real_world": "Why does dry ice sublime instead of melting like ice?"
            },
            {
                "name": "Solutions and Reactions",
                "description": "Solubility, concentration, and types of chemical reactions.",
                "real_world": "How does dissolving salt in water affect freezing point?"
            },
        ],
    },
    "chem201": {
        "title": "Organic Chemistry",
        "description": "Carbon chemistry, reactions, and structure-function relationships.",
        "key_topics": [
            {
                "name": "Hydrocarbon Structures",
                "description": "Alkanes, alkenes, alkynes, and aromatic compounds.",
                "real_world": "Why is the six-membered ring in benzene exceptionally stable?"
            },
            {
                "name": "Functional Groups",
                "description": "Alcohols, aldehydes, carboxylic acids, and reactivity patterns.",
                "real_world": "How do functional groups predict chemical behavior?"
            },
            {
                "name": "Reaction Mechanisms",
                "description": "SN1, SN2, E1, E2, and addition/elimination pathways.",
                "real_world": "Why do different conditions favor substitution vs elimination?"
            },
            {
                "name": "Stereochemistry",
                "description": "Chirality, enantiomers, and 3D molecular representations.",
                "real_world": "Why do left and right versions of molecules taste different?"
            },
            {
                "name": "Synthetic Planning",
                "description": "Retrosynthesis, multi-step synthesis, and protection strategies.",
                "real_world": "How do chemists plan efficient routes to manufacture drugs?"
            },
        ],
    },
    "chem301": {
        "title": "Physical Chemistry",
        "description": "Thermodynamics, kinetics, and quantum chemistry.",
        "key_topics": [
            {
                "name": "Thermodynamics",
                "description": "Enthalpy, entropy, Gibbs free energy, and equilibrium.",
                "real_world": "Why do spontaneous reactions always increase total entropy?"
            },
            {
                "name": "Kinetics",
                "description": "Reaction rates, rate laws, activation energy, and catalysis.",
                "real_world": "How do catalysts speed reactions without being consumed?"
            },
            {
                "name": "Chemical Equilibrium",
                "description": "Equilibrium constants, Le Chatelier's principle, and ICE tables.",
                "real_world": "How do equilibrium shifts explain pressure effects on reactions?"
            },
            {
                "name": "Electrochemistry",
                "description": "Redox reactions, galvanic cells, and electrolysis.",
                "real_world": "How do batteries generate electricity from chemical reactions?"
            },
            {
                "name": "Spectroscopy",
                "description": "UV-Vis, IR, NMR, and mass spectrometry for structure determination.",
                "real_world": "How do spectroscopy techniques identify unknown compounds?"
            },
        ],
    },
    "chem401": {
        "title": "Analytical Chemistry",
        "description": "Quantitative analysis, separations, and instrumental techniques.",
        "key_topics": [
            {
                "name": "Acid-Base Chemistry",
                "description": "pH, titrations, buffer systems, and polyprotic acids.",
                "real_world": "How do antacids neutralize stomach acid despite continuous production?"
            },
            {
                "name": "Analytical Methods",
                "description": "Gravimetric, volumetric, and coulometric analysis.",
                "real_world": "How do water quality tests measure pollutant concentrations?"
            },
            {
                "name": "Separation Techniques",
                "description": "Chromatography, electrophoresis, and distillation.",
                "real_world": "How does gas chromatography detect drugs in blood samples?"
            },
            {
                "name": "Instrumental Analysis",
                "description": "Spectroscopy, electrochemistry, and chromatography instruments.",
                "real_world": "How do hospitals use analytical instruments for disease diagnosis?"
            },
            {
                "name": "Quality Assurance",
                "description": "Standards, calibration, error analysis, and validation.",
                "real_world": "Why do pharmaceutical labs run multiple tests on each batch?"
            },
        ],
    },
}


def get_chemistry_topics(course_id: str) -> Dict[str, Any]:
    """Get detailed topics for chemistry course."""
    return CHEMISTRY_TOPICS.get(course_id, {})


def _topic_icon(topic_name: str) -> str:
    """Topic icon mapping for chemistry themes."""
    icon_map = {
        "atomic": "⚛️",
        "structure": "🔗",
        "bonding": "🤝",
        "stoichiometry": "⚖️",
        "states": "❄️",
        "solution": "🧪",
        "hydrocarbon": "⛓️",
        "functional": "🎯",
        "mechanism": "🔄",
        "stereochemistry": "3️⃣",
        "synthetic": "🏗️",
        "thermodynamics": "🔥",
        "kinetics": "⚡",
        "equilibrium": "⚗️",
        "electrochemistry": "🔋",
        "spectroscopy": "📊",
        "acid": "🟣",
        "analytical": "🔬",
        "separation": "🌈",
        "instrumental": "⚙️",
        "quality": "✅",
    }
    name = topic_name.lower()
    for key, icon in icon_map.items():
        if key in name:
            return icon
    return "🧪"


def format_chemistry_topics(course_id: str) -> Dict[str, Any]:
    """Format chemistry topics for frontend display."""
    course_data = get_chemistry_topics(course_id)
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
            f"Predict: {topic['name']}" if i % 2 == 0 else f"Balance: {topic['description']}"
            for i, topic in enumerate(course_data.get("key_topics", []))
        ][:5],
    }
