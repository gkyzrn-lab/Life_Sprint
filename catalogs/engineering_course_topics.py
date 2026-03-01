"""
Enhanced Engineering Course Topics.
Provides detailed topic descriptions for engineering (eng*) course IDs.
"""

from typing import Dict, Any

ENGINEERING_TOPICS: Dict[str, Dict[str, Any]] = {
    "eng101": {
        "title": "Engineering Design",
        "description": "Design process fundamentals from problem definition to prototyping.",
        "key_topics": [
            {
                "name": "Design Thinking",
                "description": "Empathize-define-ideate-prototype-test workflow for engineering solutions.",
                "real_world": "How do product teams reduce costly redesigns by testing early prototypes?"
            },
            {
                "name": "Requirements and Constraints",
                "description": "Translating stakeholder needs into measurable engineering specifications.",
                "real_world": "Why do safety constraints shape bridge and vehicle design from day one?"
            },
            {
                "name": "CAD Fundamentals",
                "description": "2D/3D modeling basics for communicating design intent.",
                "real_world": "How do mechanical teams use CAD to coordinate with manufacturing vendors?"
            },
            {
                "name": "Prototyping and Iteration",
                "description": "Building, testing, and improving designs through feedback cycles.",
                "real_world": "How does rapid prototyping shorten hardware development timelines?"
            },
            {
                "name": "Engineering Communication",
                "description": "Technical documentation, diagrams, and design presentations.",
                "real_world": "Why are clear design reports essential for regulatory approval?"
            },
        ],
    },
    "eng301": {
        "title": "Circuit Analysis",
        "description": "Core electrical circuit laws, methods, and dynamic response analysis.",
        "key_topics": [
            {
                "name": "Ohm and Kirchhoff Laws",
                "description": "Voltage/current relationships and conservation laws in circuits.",
                "real_world": "How do engineers diagnose power issues on embedded boards quickly?"
            },
            {
                "name": "Node and Mesh Analysis",
                "description": "Systematic methods to solve multi-loop circuit networks.",
                "real_world": "Why are matrix-based circuit solvers used in SPICE tools?"
            },
            {
                "name": "Thevenin and Norton Equivalents",
                "description": "Simplifying complex networks for load behavior analysis.",
                "real_world": "How do equivalents speed up battery/load design decisions?"
            },
            {
                "name": "Transient Response",
                "description": "Capacitor/inductor behavior during switching events.",
                "real_world": "Why do startup transients matter in power supply reliability?"
            },
            {
                "name": "AC Steady-State",
                "description": "Phasors, impedance, and sinusoidal circuit behavior.",
                "real_world": "How does impedance matching improve signal integrity?"
            },
        ],
    },
    "eng401": {
        "title": "Thermodynamics",
        "description": "Energy, heat, and work principles for engineering systems.",
        "key_topics": [
            {
                "name": "First Law of Thermodynamics",
                "description": "Energy conservation in closed and open systems.",
                "real_world": "How do engineers estimate efficiency losses in industrial plants?"
            },
            {
                "name": "Second Law and Entropy",
                "description": "Irreversibility, entropy generation, and process direction.",
                "real_world": "Why can no engine convert all heat into useful work?"
            },
            {
                "name": "Thermodynamic Cycles",
                "description": "Analysis of Rankine, Brayton, and refrigeration cycles.",
                "real_world": "How do HVAC systems optimize cooling cycle performance?"
            },
            {
                "name": "Properties of Pure Substances",
                "description": "Phase behavior, tables, and equations of state.",
                "real_world": "Why are steam tables critical for turbine design?"
            },
            {
                "name": "Heat Transfer Coupling",
                "description": "Conduction, convection, and radiation interactions.",
                "real_world": "How is battery thermal management designed for EV safety?"
            },
        ],
    },
    "eng601": {
        "title": "Advanced Controls",
        "description": "Model-based control design, stability, and optimization techniques.",
        "key_topics": [
            {
                "name": "State-Space Modeling",
                "description": "Representing dynamic systems with state variables and matrices.",
                "real_world": "How do robotics teams model multi-axis motion systems?"
            },
            {
                "name": "Stability Analysis",
                "description": "Lyapunov and eigenvalue-based stability criteria.",
                "real_world": "Why must autonomous drones guarantee stable feedback loops?"
            },
            {
                "name": "Observer Design",
                "description": "Estimating unmeasured states using system outputs.",
                "real_world": "How do EV controllers estimate battery states in real time?"
            },
            {
                "name": "Optimal Control",
                "description": "Cost-function minimization for control inputs and trajectories.",
                "real_world": "How does model predictive control reduce energy use in smart buildings?"
            },
            {
                "name": "Robust Control",
                "description": "Designing controllers resilient to uncertainty and disturbances.",
                "real_world": "How do industrial plants maintain performance under sensor noise?"
            },
        ],
    },
}


def get_engineering_topics(course_id: str) -> Dict[str, Any]:
    """Get detailed topics for engineering course."""
    return ENGINEERING_TOPICS.get(course_id, {})


def _topic_icon(topic_name: str) -> str:
    """Topic icon mapping for engineering themes."""
    icon_map = {
        "design": "🛠️",
        "cad": "📐",
        "prototype": "🧪",
        "circuit": "🔌",
        "kirchhoff": "🧮",
        "transient": "⚡",
        "thermo": "🌡️",
        "entropy": "♨️",
        "cycle": "🔄",
        "state-space": "📊",
        "stability": "🧷",
        "control": "🎛️",
        "observer": "👁️",
        "robust": "🛡️",
    }
    name = topic_name.lower()
    for key, icon in icon_map.items():
        if key in name:
            return icon
    return "⚙️"


def format_engineering_topics(course_id: str) -> Dict[str, Any]:
    """Format engineering topics for frontend display."""
    course_data = get_engineering_topics(course_id)
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
            f"Design/Model: {topic['name']}" if i % 2 == 0 else f"Apply: {topic['description']}"
            for i, topic in enumerate(course_data.get("key_topics", []))
        ][:5],
    }
