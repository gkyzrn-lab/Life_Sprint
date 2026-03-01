"""
Enhanced Economics Course Topics.
Provides detailed topic descriptions for economics (econ*) course IDs.
"""

from typing import Dict, Any

ECONOMICS_TOPICS: Dict[str, Dict[str, Any]] = {
    "econ101": {
        "title": "Microeconomics",
        "description": "Individual decision-making, market behavior, and pricing dynamics.",
        "key_topics": [
            {
                "name": "Supply and Demand",
                "description": "Price formation through shifts in supply and demand curves.",
                "real_world": "Why do concert ticket prices jump after a major artist announces a tour?"
            },
            {
                "name": "Elasticity",
                "description": "Sensitivity of quantity demanded/supplied to price and income changes.",
                "real_world": "Why does fuel demand fall slowly even when gas prices rise sharply?"
            },
            {
                "name": "Consumer Choice",
                "description": "Utility, budget constraints, and optimal bundles.",
                "real_world": "How do households trade off rent, food, and transportation costs?"
            },
            {
                "name": "Production and Costs",
                "description": "Short-run/long-run production functions and cost structures.",
                "real_world": "Why can large manufacturers produce cheaper per unit than small shops?"
            },
            {
                "name": "Market Structures",
                "description": "Competition, monopoly, and oligopoly outcomes.",
                "real_world": "How does pricing in the smartphone market differ from local produce markets?"
            },
        ],
    },
    "econ201": {
        "title": "Intermediate Microeconomics",
        "description": "Formal models of consumer and firm behavior with optimization techniques.",
        "key_topics": [
            {
                "name": "Constrained Optimization",
                "description": "Lagrangian methods for utility and cost minimization problems.",
                "real_world": "How do firms optimize ad spend under fixed campaign budgets?"
            },
            {
                "name": "Duality Theory",
                "description": "Linking expenditure and utility functions for demand analysis.",
                "real_world": "How do analysts infer preferences from observed purchasing data?"
            },
            {
                "name": "Producer Theory",
                "description": "Profit maximization under technology and input constraints.",
                "real_world": "How do restaurants choose labor vs automation to manage costs?"
            },
            {
                "name": "General Equilibrium Basics",
                "description": "Interdependent markets and welfare implications.",
                "real_world": "How can a housing shortage raise wages and inflation simultaneously?"
            },
            {
                "name": "Welfare and Efficiency",
                "description": "Pareto efficiency, deadweight loss, and policy tradeoffs.",
                "real_world": "How do taxes create efficiency costs while funding public goods?"
            },
        ],
    },
    "econ301": {
        "title": "Econometrics I",
        "description": "Statistical tools for estimating economic relationships from data.",
        "key_topics": [
            {
                "name": "Linear Regression",
                "description": "OLS estimation, interpretation, and assumptions.",
                "real_world": "How do economists estimate wage effects of education levels?"
            },
            {
                "name": "Inference and Hypothesis Testing",
                "description": "Confidence intervals, p-values, and model significance.",
                "real_world": "How do policy teams test whether a subsidy program worked?"
            },
            {
                "name": "Omitted Variable Bias",
                "description": "Sources of biased estimates and model misspecification.",
                "real_world": "Why can naive correlations overstate the impact of training programs?"
            },
            {
                "name": "Heteroskedasticity",
                "description": "Non-constant error variance and robust standard errors.",
                "real_world": "Why do income datasets often require robust inference methods?"
            },
            {
                "name": "Model Diagnostics",
                "description": "Residual checks, fit quality, and specification testing.",
                "real_world": "How do analysts detect when a forecasting model breaks during shocks?"
            },
        ],
    },
    "econ401": {
        "title": "Labor Economics",
        "description": "Workforce dynamics, wages, incentives, and labor-market policy.",
        "key_topics": [
            {
                "name": "Labor Supply and Demand",
                "description": "How wages and participation respond to market conditions.",
                "real_world": "Why do some industries face worker shortages despite wage growth?"
            },
            {
                "name": "Human Capital",
                "description": "Education and training effects on productivity and earnings.",
                "real_world": "How does upskilling change long-term wage trajectories?"
            },
            {
                "name": "Unemployment Dynamics",
                "description": "Frictional, structural, and cyclical unemployment mechanisms.",
                "real_world": "Why does unemployment persist after recessions end?"
            },
            {
                "name": "Wage Inequality",
                "description": "Drivers of dispersion across sectors, skills, and demographics.",
                "real_world": "How do technology and globalization influence wage gaps?"
            },
            {
                "name": "Labor Policy",
                "description": "Minimum wage, unions, and employment regulation impacts.",
                "real_world": "How can policy improve worker protections without reducing hiring?"
            },
        ],
    },
}


def get_economics_topics(course_id: str) -> Dict[str, Any]:
    """Get detailed topics for economics course."""
    return ECONOMICS_TOPICS.get(course_id, {})


def _topic_icon(topic_name: str) -> str:
    """Topic icon mapping for economics themes."""
    icon_map = {
        "supply": "📈",
        "demand": "📉",
        "elasticity": "🧲",
        "consumer": "🛒",
        "market": "🏪",
        "optimization": "🎯",
        "welfare": "⚖️",
        "regression": "📊",
        "inference": "🔬",
        "bias": "⚠️",
        "diagnostics": "🩺",
        "labor": "👷",
        "wage": "💵",
        "policy": "🏛️",
        "unemployment": "📋",
    }
    name = topic_name.lower()
    for key, icon in icon_map.items():
        if key in name:
            return icon
    return "📘"


def format_economics_topics(course_id: str) -> Dict[str, Any]:
    """Format economics topics for frontend display."""
    course_data = get_economics_topics(course_id)
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
