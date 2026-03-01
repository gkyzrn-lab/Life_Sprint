"""
Enhanced Data Science Course Topics.
Provides detailed topic descriptions for data science (ds*) course IDs.
"""

from typing import Dict, Any

DATA_SCIENCE_TOPICS: Dict[str, Dict[str, Any]] = {
    "ds101": {
        "title": "Intro to Data Science",
        "description": "Data science fundamentals, tools, and workflow for decision-making.",
        "key_topics": [
            {
                "name": "Data Collection",
                "description": "Identifying data sources, APIs, databases, and acquisition methods.",
                "real_world": "How do companies ethically collect user data while respecting privacy?"
            },
            {
                "name": "Data Cleaning",
                "description": "Handling missing values, duplicates, outliers, and data quality.",
                "real_world": "Why does 80% of data science work involve cleaning messy data?"
            },
            {
                "name": "Exploratory Data Analysis",
                "description": "Visualization and statistical summarization to understand patterns.",
                "real_world": "How do analysts discover hidden correlations before building models?"
            },
            {
                "name": "Data Storytelling",
                "description": "Communicating insights clearly to non-technical stakeholders.",
                "real_world": "Why do CEOs dismiss data findings if analysts can't explain them clearly?"
            },
            {
                "name": "Ethics and Privacy",
                "description": "Privacy regulations, bias, fairness, and responsible data handling.",
                "real_world": "How can predictive models avoid perpetuating discrimination?"
            },
        ],
    },
    "ds201": {
        "title": "Probability & Statistics",
        "description": "Foundational statistics for inference, hypothesis testing, and estimation.",
        "key_topics": [
            {
                "name": "Distributions",
                "description": "Normal, binomial, Poisson, and other probability distributions.",
                "real_world": "How do quality-control teams use distribution knowledge to spot defects?"
            },
            {
                "name": "Hypothesis Testing",
                "description": "p-values, significance levels, and Type I/II errors.",
                "real_world": "How do drug trials ensure new medications truly work better?"
            },
            {
                "name": "Confidence Intervals",
                "description": "Estimating population parameters with uncertainty quantification.",
                "real_world": "Why do election polls report margins of error?"
            },
            {
                "name": "Bayesian Inference",
                "description": "Prior beliefs, likelihood, and posterior updating.",
                "real_world": "How do spam filters learn from user feedback?"
            },
            {
                "name": "Design of Experiments",
                "description": "Planning studies to isolate causal effects.",
                "real_world": "How do A/B tests ensure fair comparisons in product features?"
            },
        ],
    },
    "ds301": {
        "title": "Machine Learning",
        "description": "Supervised and unsupervised learning algorithms for predictions.",
        "key_topics": [
            {
                "name": "Supervised Learning",
                "description": "Regression and classification with labeled training data.",
                "real_world": "How do credit-scoring models predict loan default risk?"
            },
            {
                "name": "Unsupervised Learning",
                "description": "Clustering and dimensionality reduction without labels.",
                "real_world": "How do e-commerce platforms discover customer segments?"
            },
            {
                "name": "Feature Engineering",
                "description": "Creating and selecting informative predictors.",
                "real_world": "Why do custom features often outperform raw data in competitions?"
            },
            {
                "name": "Model Validation",
                "description": "Cross-validation, overfitting detection, and generalization.",
                "real_world": "How do teams avoid building models that work on training data only?"
            },
            {
                "name": "Ensemble Methods",
                "description": "Boosting, bagging, and combining weak learners.",
                "real_world": "Why do random forests often beat individual decision trees?"
            },
        ],
    },
    "ds401": {
        "title": "Deep Learning",
        "description": "Neural networks and representation learning for complex patterns.",
        "key_topics": [
            {
                "name": "Neural Network Basics",
                "description": "Perceptrons, activation functions, and backpropagation.",
                "real_world": "How do neural networks approximate arbitrary functions?"
            },
            {
                "name": "Convolutional Networks",
                "description": "Local feature detection for image and spatial data.",
                "real_world": "How do face-recognition systems learn to detect facial features?"
            },
            {
                "name": "Recurrent Networks",
                "description": "Sequential modeling and temporal dependencies.",
                "real_world": "How do language models predict the next word in autocomplete?"
            },
            {
                "name": "Training Techniques",
                "description": "Optimization, regularization, and hyperparameter tuning.",
                "real_world": "Why do batching and learning-rate schedules speed training?"
            },
            {
                "name": "Transfer Learning",
                "description": "Reusing pre-trained models for new tasks with limited data.",
                "real_world": "How can startups build vision systems without massive datasets?"
            },
        ],
    },
}


def get_data_science_topics(course_id: str) -> Dict[str, Any]:
    """Get detailed topics for data science course."""
    return DATA_SCIENCE_TOPICS.get(course_id, {})


def _topic_icon(topic_name: str) -> str:
    """Topic icon mapping for data science themes."""
    icon_map = {
        "collection": "🔍",
        "cleaning": "🧹",
        "analysis": "📊",
        "storytelling": "📖",
        "ethics": "⚖️",
        "distribution": "📈",
        "hypothesis": "🧪",
        "confidence": "✅",
        "bayesian": "🎲",
        "experiment": "🔬",
        "supervised": "👨‍🏫",
        "unsupervised": "🔓",
        "feature": "🎯",
        "validation": "✔️",
        "ensemble": "🎭",
        "neural": "🧠",
        "transfer": "🔄",
    }
    name = topic_name.lower()
    for key, icon in icon_map.items():
        if key in name:
            return icon
    return "📉"


def format_data_science_topics(course_id: str) -> Dict[str, Any]:
    """Format data science topics for frontend display."""
    course_data = get_data_science_topics(course_id)
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
            f"Implement: {topic['name']}" if i % 2 == 0 else f"Apply: {topic['description']}"
            for i, topic in enumerate(course_data.get("key_topics", []))
        ][:5],
    }
