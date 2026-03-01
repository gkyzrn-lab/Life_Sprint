"""
Enhanced Physics Course Topics.
Provides detailed topic descriptions for physics (phys*) course IDs.
"""

from typing import Dict, Any

PHYSICS_TOPICS: Dict[str, Dict[str, Any]] = {
    "phys101": {
        "title": "Physics I",
        "description": "Classical mechanics foundations: motion, forces, energy, and momentum.",
        "key_topics": [
            {
                "name": "Kinematics",
                "description": "Describing motion using displacement, velocity, and acceleration.",
                "real_world": "How do self-driving systems predict vehicle trajectories at intersections?"
            },
            {
                "name": "Newton's Laws",
                "description": "Force-motion relationships and free-body diagram analysis.",
                "real_world": "Why does cargo shift dangerously if trucks brake too hard?"
            },
            {
                "name": "Work and Energy",
                "description": "Energy conservation and work-energy theorem applications.",
                "real_world": "How do roller coasters convert potential energy into speed?"
            },
            {
                "name": "Momentum and Collisions",
                "description": "Impulse, momentum conservation, and collision outcomes.",
                "real_world": "How do crash engineers design safer vehicles using momentum models?"
            },
            {
                "name": "Rotational Dynamics",
                "description": "Torque, angular motion, and moment of inertia.",
                "real_world": "Why do figure skaters spin faster when pulling arms inward?"
            },
        ],
    },
    "phys102": {
        "title": "Physics II",
        "description": "Electricity, magnetism, waves, and introductory modern physics.",
        "key_topics": [
            {
                "name": "Electric Fields and Potential",
                "description": "Charge interactions, field lines, and electric potential energy.",
                "real_world": "How do capacitive touchscreens detect finger input?"
            },
            {
                "name": "Circuits",
                "description": "Current, voltage, resistance, and circuit analysis principles.",
                "real_world": "Why does adding devices in parallel keep household voltage stable?"
            },
            {
                "name": "Magnetism and Induction",
                "description": "Magnetic fields, Lorentz force, and Faraday's law.",
                "real_world": "How do power generators convert rotation into electrical energy?"
            },
            {
                "name": "Waves and Interference",
                "description": "Wave propagation, superposition, and resonance behavior.",
                "real_world": "How do noise-canceling headphones use destructive interference?"
            },
            {
                "name": "Optics and Light",
                "description": "Reflection, refraction, and image formation in optical systems.",
                "real_world": "How do camera lenses focus light for sharp images?"
            },
        ],
    },
    "phys201": {
        "title": "Modern Physics",
        "description": "Relativity, quantum foundations, and atomic-scale physical behavior.",
        "key_topics": [
            {
                "name": "Special Relativity",
                "description": "Frames of reference, time dilation, and Lorentz transformations.",
                "real_world": "Why must GPS systems correct for relativistic timing effects?"
            },
            {
                "name": "Wave-Particle Duality",
                "description": "Matter and light exhibiting both wave and particle properties.",
                "real_world": "How does electron diffraction validate quantum behavior?"
            },
            {
                "name": "Quantum States",
                "description": "Quantization, probability amplitudes, and measurement basics.",
                "real_world": "How does quantum mechanics enable semiconductor design?"
            },
            {
                "name": "Atomic Structure",
                "description": "Energy levels, spectra, and atomic transition models.",
                "real_world": "How do emission spectra help identify unknown materials?"
            },
            {
                "name": "Nuclear Processes",
                "description": "Radioactivity, decay modes, and binding energy concepts.",
                "real_world": "How do medical imaging technologies use controlled nuclear physics?"
            },
        ],
    },
    "phys301": {
        "title": "Electromagnetic Theory",
        "description": "Advanced field theory and Maxwell-equation-based modeling.",
        "key_topics": [
            {
                "name": "Gauss's Law",
                "description": "Field-flux relationships in symmetric charge distributions.",
                "real_world": "How do engineers model shielding behavior in electronics?"
            },
            {
                "name": "Ampere-Maxwell Law",
                "description": "Magnetic fields from currents and changing electric fields.",
                "real_world": "How does displacement current explain wireless signal propagation?"
            },
            {
                "name": "Electromagnetic Waves",
                "description": "Propagation, polarization, and wave-medium interactions.",
                "real_world": "How do Wi-Fi routers transmit information through EM waves?"
            },
            {
                "name": "Boundary Conditions",
                "description": "Field behavior across interfaces and material transitions.",
                "real_world": "Why do antennas require careful material and geometry design?"
            },
            {
                "name": "Energy and Poynting Vector",
                "description": "Power flow and energy transport in fields.",
                "real_world": "How is power transfer quantified in microwave engineering?"
            },
        ],
    },
}


def get_physics_topics(course_id: str) -> Dict[str, Any]:
    """Get detailed topics for physics course."""
    return PHYSICS_TOPICS.get(course_id, {})


def _topic_icon(topic_name: str) -> str:
    """Topic icon mapping for physics themes."""
    icon_map = {
        "kinematics": "🏃",
        "newton": "🍎",
        "energy": "⚡",
        "momentum": "🎯",
        "rotational": "🌀",
        "electric": "🔌",
        "circuits": "🔋",
        "magnet": "🧲",
        "waves": "🌊",
        "optics": "🔭",
        "quantum": "🧬",
        "relativity": "🕒",
        "atomic": "⚛️",
        "nuclear": "☢️",
        "maxwell": "📡",
    }
    name = topic_name.lower()
    for key, icon in icon_map.items():
        if key in name:
            return icon
    return "🧪"


def format_physics_topics(course_id: str) -> Dict[str, Any]:
    """Format physics topics for frontend display."""
    course_data = get_physics_topics(course_id)
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
            f"Model: {topic['name']}" if i % 2 == 0 else f"Apply: {topic['description']}"
            for i, topic in enumerate(course_data.get("key_topics", []))
        ][:5],
    }
