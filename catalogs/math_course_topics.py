"""
Enhanced Mathematics Course Topics.
Provides detailed topic descriptions for mathematics (math*) course IDs.
"""

from typing import Dict, Any

MATH_TOPICS: Dict[str, Dict[str, Any]] = {
    "math101": {
        "title": "Calculus I",
        "description": "Limits, derivatives, and foundational change-rate modeling.",
        "key_topics": [
            {
                "name": "Limits and Continuity",
                "description": "Behavior of functions near points and continuity conditions.",
                "real_world": "How do engineers estimate behavior near structural stress thresholds?"
            },
            {
                "name": "Derivative Rules",
                "description": "Power, product, quotient, and chain rule techniques.",
                "real_world": "How do analysts measure instant growth rate in user adoption curves?"
            },
            {
                "name": "Applications of Derivatives",
                "description": "Optimization, related rates, and curve analysis.",
                "real_world": "How can a company optimize price to maximize revenue?"
            },
            {
                "name": "Implicit Differentiation",
                "description": "Differentiating relations not solved explicitly for one variable.",
                "real_world": "Why is implicit differentiation useful in physics constraint models?"
            },
            {
                "name": "Linear Approximation",
                "description": "Local linear models and differential-based estimation.",
                "real_world": "How do quick sensitivity estimates support risk decisions?"
            },
        ],
    },
    "math201": {
        "title": "Linear Algebra",
        "description": "Vectors, matrices, linear transformations, and system solving.",
        "key_topics": [
            {
                "name": "Systems of Linear Equations",
                "description": "Matrix methods and elimination for solving multivariable systems.",
                "real_world": "How do logistics teams solve large allocation problems efficiently?"
            },
            {
                "name": "Vector Spaces",
                "description": "Span, basis, dimension, and subspace structure.",
                "real_world": "How do recommendation systems represent users as vectors?"
            },
            {
                "name": "Eigenvalues and Eigenvectors",
                "description": "Spectral properties of matrices and dynamic behavior.",
                "real_world": "How does Google's PageRank rely on eigenvector concepts?"
            },
            {
                "name": "Linear Transformations",
                "description": "Mappings between spaces and their matrix representations.",
                "real_world": "How are 2D/3D graphics rotations modeled in game engines?"
            },
            {
                "name": "Orthogonality",
                "description": "Dot products, projections, and least-squares approximations.",
                "real_world": "How does regression use least squares to fit predictive models?"
            },
        ],
    },
    "math301": {
        "title": "Abstract Algebra I",
        "description": "Algebraic structures including groups, subgroups, and homomorphisms.",
        "key_topics": [
            {
                "name": "Group Axioms",
                "description": "Closure, associativity, identity, and inverses in algebraic systems.",
                "real_world": "How does symmetry in molecules map to group structures?"
            },
            {
                "name": "Subgroups and Cyclic Groups",
                "description": "Generators, subgroup tests, and finite-group properties.",
                "real_world": "How do repeating transformation patterns appear in cryptography?"
            },
            {
                "name": "Cosets and Lagrange's Theorem",
                "description": "Partitioning groups and divisibility constraints on order.",
                "real_world": "Why do structural constraints matter in secure key spaces?"
            },
            {
                "name": "Group Homomorphisms",
                "description": "Structure-preserving maps and kernels/images.",
                "real_world": "How do abstraction layers preserve core behavior across systems?"
            },
            {
                "name": "Isomorphisms",
                "description": "When two algebraic structures are essentially equivalent.",
                "real_world": "How can equivalent data models simplify software migrations?"
            },
        ],
    },
    "math401": {
        "title": "Abstract Algebra II",
        "description": "Ring and field theory with deeper structural algebra concepts.",
        "key_topics": [
            {
                "name": "Rings and Ideals",
                "description": "Ring operations, ideal structure, and quotient constructions.",
                "real_world": "How do modular arithmetic systems support cryptographic protocols?"
            },
            {
                "name": "Integral Domains and Fields",
                "description": "Properties that generalize arithmetic without zero divisors.",
                "real_world": "Why are finite fields essential in error-correcting codes?"
            },
            {
                "name": "Polynomial Rings",
                "description": "Factorization and irreducibility over different fields.",
                "real_world": "How do coding systems use polynomial factorization for reliability?"
            },
            {
                "name": "Field Extensions",
                "description": "Constructing larger fields and studying extension degree.",
                "real_world": "How does extension structure influence modern encryption methods?"
            },
            {
                "name": "Galois Concepts",
                "description": "Symmetry of roots and solvability insights.",
                "real_world": "Why does root symmetry matter for computational algebra systems?"
            },
        ],
    },
}


def get_math_topics(course_id: str) -> Dict[str, Any]:
    """Get detailed topics for math course."""
    return MATH_TOPICS.get(course_id, {})


def _topic_icon(topic_name: str) -> str:
    """Topic icon mapping for mathematics themes."""
    icon_map = {
        "limit": "📉",
        "derivative": "📈",
        "optimization": "🎯",
        "matrix": "🔢",
        "vector": "➡️",
        "eigen": "🧮",
        "orthogon": "📐",
        "group": "🔁",
        "isomorphism": "🪞",
        "ring": "💍",
        "field": "🌐",
        "polynomial": "✳️",
        "galois": "🔐",
    }
    name = topic_name.lower()
    for key, icon in icon_map.items():
        if key in name:
            return icon
    return "➗"


def format_math_topics(course_id: str) -> Dict[str, Any]:
    """Format mathematics topics for frontend display."""
    course_data = get_math_topics(course_id)
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
            f"Prove/Analyze: {topic['name']}" if i % 2 == 0 else f"Apply: {topic['description']}"
            for i, topic in enumerate(course_data.get("key_topics", []))
        ][:5],
    }
