"""
Enhanced CS Course Topics and Learning Materials.
Provides detailed, engaging topic descriptions for Computer Science courses.
"""

from typing import Dict, Any

CS_COURSE_TOPICS: Dict[str, Dict[str, Any]] = {
    "cs101": {
        "title": "Intro Programming",
        "description": "Programming foundations with variables, control flow, functions, and debugging.",
        "key_topics": [
            {
                "name": "Variables and Data Types",
                "description": "Representing data using integers, strings, booleans, and collections.",
                "real_world": "Why does a checkout system store prices as numeric types, not text?"
            },
            {
                "name": "Conditionals and Loops",
                "description": "Controlling program flow with if/else and repetitive logic with loops.",
                "real_world": "How does a recommendation engine loop through products to find matches?"
            },
            {
                "name": "Functions and Modularity",
                "description": "Breaking complex problems into reusable, testable functions.",
                "real_world": "Why do production apps split code into modules instead of one giant file?"
            },
            {
                "name": "Debugging Fundamentals",
                "description": "Identifying and fixing runtime, logic, and syntax errors.",
                "real_world": "How do developers trace a payment bug that only happens in edge cases?"
            },
            {
                "name": "Problem Decomposition",
                "description": "Translating real-world requirements into algorithmic steps.",
                "real_world": "How would you break down a to-do app into core features and data models?"
            },
        ],
    },
    "cs201": {
        "title": "Data Structures",
        "description": "Organizing data efficiently using arrays, linked lists, stacks, queues, trees, and hash maps.",
        "key_topics": [
            {
                "name": "Arrays and Lists",
                "description": "Sequential data storage and tradeoffs in insertion and access speed.",
                "real_world": "Why are product catalogs often cached as arrays while lookups use maps?"
            },
            {
                "name": "Stacks and Queues",
                "description": "LIFO and FIFO structures for ordered processing.",
                "real_world": "How does an undo button use a stack to reverse recent actions?"
            },
            {
                "name": "Hash Tables",
                "description": "Fast key-value lookup using hash functions and collision handling.",
                "real_world": "How can a login system check usernames quickly at scale?"
            },
            {
                "name": "Trees and Traversal",
                "description": "Hierarchical data modeling and DFS/BFS traversal techniques.",
                "real_world": "How do file systems and menu structures use trees?"
            },
            {
                "name": "Complexity Analysis",
                "description": "Comparing operations with Big-O to pick efficient structures.",
                "real_world": "Why does search feel instant in one app but slow in another?"
            },
        ],
    },
    "cs202": {
        "title": "Computer Architecture",
        "description": "Understanding how CPUs, memory, and machine instructions execute software.",
        "key_topics": [
            {
                "name": "CPU and Instruction Cycle",
                "description": "Fetch-decode-execute model and how instructions run at hardware level.",
                "real_world": "Why does optimized code run faster on the same machine?"
            },
            {
                "name": "Memory Hierarchy",
                "description": "Registers, cache, RAM, and storage with speed-capacity tradeoffs.",
                "real_world": "Why do cache misses hurt game and simulation performance?"
            },
            {
                "name": "Binary and Bitwise Operations",
                "description": "Binary representation and low-level data manipulation.",
                "real_world": "How do graphics engines pack color channels efficiently?"
            },
            {
                "name": "Assembly Basics",
                "description": "Low-level instructions, registers, and simple control flow.",
                "real_world": "How do reverse engineers inspect malware behavior?"
            },
            {
                "name": "Performance Bottlenecks",
                "description": "Identifying CPU-bound vs memory-bound workloads.",
                "real_world": "Why can an API be slow even when network latency is low?"
            },
        ],
    },
    "cs301": {
        "title": "Algorithms",
        "description": "Designing and analyzing efficient algorithms for complex computational problems.",
        "key_topics": [
            {
                "name": "Sorting and Searching",
                "description": "Core techniques like quicksort, mergesort, and binary search.",
                "real_world": "How do e-commerce sites sort millions of products quickly?"
            },
            {
                "name": "Greedy Algorithms",
                "description": "Locally optimal choices to approximate or solve optimization problems.",
                "real_world": "How can delivery routes be optimized with practical heuristics?"
            },
            {
                "name": "Dynamic Programming",
                "description": "Breaking overlapping subproblems into reusable memoized states.",
                "real_world": "How does autocomplete predict likely next words efficiently?"
            },
            {
                "name": "Graph Algorithms",
                "description": "Shortest path, traversal, and connectivity in networked data.",
                "real_world": "How does a maps app compute the fastest route in traffic?"
            },
            {
                "name": "Complexity Tradeoffs",
                "description": "Balancing time, space, and implementation complexity.",
                "real_world": "When is a simpler algorithm better for maintainability?"
            },
        ],
    },
}


def get_cs_course_topics(course_id: str) -> Dict[str, Any]:
    """Get detailed topics for a CS course."""
    return CS_COURSE_TOPICS.get(course_id, {})


def get_cs_topic_icon(topic_name: str) -> str:
    """Get an emoji icon for a CS topic."""
    icon_map = {
        "variables": "🔤",
        "data types": "🧱",
        "conditionals": "🔀",
        "loops": "🔁",
        "functions": "🧩",
        "debug": "🐛",
        "decomposition": "🗂️",
        "arrays": "📚",
        "lists": "🧾",
        "stack": "🥞",
        "queue": "🚶",
        "hash": "#️⃣",
        "tree": "🌳",
        "complexity": "⏱️",
        "cpu": "🖥️",
        "memory": "🧠",
        "binary": "0️⃣",
        "assembly": "⚙️",
        "performance": "🚀",
        "sorting": "📊",
        "searching": "🔎",
        "greedy": "💡",
        "dynamic": "🧮",
        "graph": "🕸️",
        "tradeoffs": "⚖️",
    }

    name = topic_name.lower()
    for key, icon in icon_map.items():
        if key in name:
            return icon
    return "💻"


def format_cs_topics_for_display(course_id: str) -> Dict[str, Any]:
    """Format CS course topics for frontend display."""
    course_data = get_cs_course_topics(course_id)
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
                "icon": get_cs_topic_icon(topic["name"]),
            }
            for topic in course_data.get("key_topics", [])
        ],
        "learning_outcomes": [
            f"Implement: {topic['name']}" if i % 2 == 0 else f"Apply: {topic['description']}"
            for i, topic in enumerate(course_data.get("key_topics", []))
        ][:5],
    }
