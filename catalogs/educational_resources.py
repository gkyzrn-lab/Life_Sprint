# Learning resources and external links for curriculum courses
# Provides students with additional materials to supplement their learning

from typing import Dict, List


# Resource types
RESOURCE_TYPES = {
    "video": "📺 Video Tutorial",
    "article": "📄 Article",
    "book": "📚 Book",
    "course": "🎓 Online Course",
    "tool": "🛠️ Tool/Software",
    "practice": "💪 Practice Platform",
    "documentation": "📖 Documentation",
    "community": "👥 Community",
    "podcast": "🎙️ Podcast"
}


# Course-specific resources
COURSE_RESOURCES = {
    "CS101": {
        "course_name": "Introduction to Programming",
        "resources": [
            {
                "type": "video",
                "title": "Python for Beginners - Full Course",
                "provider": "freeCodeCamp",
                "url": "https://www.youtube.com/watch?v=rfscVS0vtbw",
                "description": "Comprehensive Python tutorial for absolute beginners",
                "free": True
            },
            {
                "type": "course",
                "title": "CS50: Introduction to Computer Science",
                "provider": "Harvard (edX)",
                "url": "https://www.edx.org/course/cs50s-introduction-to-computer-science",
                "description": "Famous intro CS course from Harvard",
                "free": True
            },
            {
                "type": "practice",
                "title": "Codecademy Python",
                "provider": "Codecademy",
                "url": "https://www.codecademy.com/learn/learn-python-3",
                "description": "Interactive Python exercises and projects",
                "free": False
            },
            {
                "type": "book",
                "title": "Automate the Boring Stuff with Python",
                "provider": "Al Sweigart",
                "url": "https://automatetheboringstuff.com/",
                "description": "Practical Python programming for beginners",
                "free": True
            },
            {
                "type": "community",
                "title": "r/learnprogramming",
                "provider": "Reddit",
                "url": "https://www.reddit.com/r/learnprogramming/",
                "description": "Active community for programming learners",
                "free": True
            }
        ]
    },
    "CS102": {
        "course_name": "Data Structures",
        "resources": [
            {
                "type": "course",
                "title": "Data Structures and Algorithms",
                "provider": "Princeton (Coursera)",
                "url": "https://www.coursera.org/learn/algorithms-part1",
                "description": "Rigorous data structures course",
                "free": True
            },
            {
                "type": "practice",
                "title": "LeetCode",
                "provider": "LeetCode",
                "url": "https://leetcode.com/",
                "description": "Practice data structures through coding problems",
                "free": True
            },
            {
                "type": "video",
                "title": "Data Structures Easy to Advanced",
                "provider": "freeCodeCamp",
                "url": "https://www.youtube.com/watch?v=RBSGKlAvoiM",
                "description": "Complete data structures video course",
                "free": True
            },
            {
                "type": "book",
                "title": "Cracking the Coding Interview",
                "provider": "Gayle Laakmann McDowell",
                "url": "https://www.crackingthecodinginterview.com/",
                "description": "Essential for technical interviews",
                "free": False
            },
            {
                "type": "tool",
                "title": "VisuAlgo",
                "provider": "VisuAlgo",
                "url": "https://visualgo.net/",
                "description": "Visualize data structures and algorithms",
                "free": True
            }
        ]
    },
    "CS203": {
        "course_name": "Algorithms",
        "resources": [
            {
                "type": "book",
                "title": "Introduction to Algorithms (CLRS)",
                "provider": "MIT Press",
                "url": "https://mitpress.mit.edu/books/introduction-algorithms-third-edition",
                "description": "The definitive algorithms textbook",
                "free": False
            },
            {
                "type": "course",
                "title": "Algorithms Specialization",
                "provider": "Stanford (Coursera)",
                "url": "https://www.coursera.org/specializations/algorithms",
                "description": "Deep dive into algorithm design and analysis",
                "free": True
            },
            {
                "type": "practice",
                "title": "HackerRank",
                "provider": "HackerRank",
                "url": "https://www.hackerrank.com/",
                "description": "Algorithm challenges and competitions",
                "free": True
            }
        ]
    },
    "BUS101": {
        "course_name": "Introduction to Business",
        "resources": [
            {
                "type": "course",
                "title": "Introduction to Marketing",
                "provider": "Wharton (Coursera)",
                "url": "https://www.coursera.org/learn/wharton-marketing",
                "description": "Marketing fundamentals from top business school",
                "free": True
            },
            {
                "type": "podcast",
                "title": "How I Built This",
                "provider": "NPR",
                "url": "https://www.npr.org/podcasts/510313/how-i-built-this",
                "description": "Stories from founders and entrepreneurs",
                "free": True
            },
            {
                "type": "article",
                "title": "Harvard Business Review",
                "provider": "HBR",
                "url": "https://hbr.org/",
                "description": "Latest business insights and research",
                "free": False
            },
            {
                "type": "book",
                "title": "The Lean Startup",
                "provider": "Eric Ries",
                "url": "http://theleanstartup.com/",
                "description": "Modern entrepreneurship methodology",
                "free": False
            }
        ]
    },
    "MATH141": {
        "course_name": "Calculus I",
        "resources": [
            {
                "type": "video",
                "title": "Calculus",
                "provider": "Khan Academy",
                "url": "https://www.khanacademy.org/math/calculus-1",
                "description": "Comprehensive video lessons with practice",
                "free": True
            },
            {
                "type": "video",
                "title": "Essence of Calculus",
                "provider": "3Blue1Brown",
                "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr",
                "description": "Visual and intuitive calculus explanations",
                "free": True
            },
            {
                "type": "tool",
                "title": "Wolfram Alpha",
                "provider": "Wolfram",
                "url": "https://www.wolframalpha.com/",
                "description": "Computational engine for math problems",
                "free": True
            },
            {
                "type": "practice",
                "title": "Paul's Online Math Notes",
                "provider": "Paul Dawkins",
                "url": "https://tutorial.math.lamar.edu/",
                "description": "Calculus notes, examples, and practice problems",
                "free": True
            }
        ]
    },
    "ENG101": {
        "course_name": "English Composition",
        "resources": [
            {
                "type": "tool",
                "title": "Grammarly",
                "provider": "Grammarly",
                "url": "https://www.grammarly.com/",
                "description": "Writing assistant for grammar and style",
                "free": True
            },
            {
                "type": "tool",
                "title": "Hemingway Editor",
                "provider": "Hemingway",
                "url": "https://hemingwayapp.com/",
                "description": "Makes your writing clear and bold",
                "free": True
            },
            {
                "type": "book",
                "title": "On Writing Well",
                "provider": "William Zinsser",
                "url": "https://www.harpercollins.com/products/on-writing-well-william-zinsser",
                "description": "Classic guide to nonfiction writing",
                "free": False
            },
            {
                "type": "course",
                "title": "Writing in the Sciences",
                "provider": "Stanford (Coursera)",
                "url": "https://www.coursera.org/learn/sciwrite",
                "description": "Technical and scientific writing skills",
                "free": True
            }
        ]
    }
}


# General study resources by subject area
GENERAL_RESOURCES = {
    "computer_science": {
        "subject": "Computer Science",
        "resources": [
            {
                "type": "community",
                "title": "Stack Overflow",
                "provider": "Stack Exchange",
                "url": "https://stackoverflow.com/",
                "description": "Q&A for programming questions",
                "free": True
            },
            {
                "type": "practice",
                "title": "GitHub",
                "provider": "GitHub",
                "url": "https://github.com/",
                "description": "Code hosting and version control",
                "free": True
            },
            {
                "type": "documentation",
                "title": "MDN Web Docs",
                "provider": "Mozilla",
                "url": "https://developer.mozilla.org/",
                "description": "Web development documentation",
                "free": True
            },
            {
                "type": "podcast",
                "title": "Software Engineering Daily",
                "provider": "SE Daily",
                "url": "https://softwareengineeringdaily.com/",
                "description": "Daily interviews with software engineers",
                "free": True
            }
        ]
    },
    "business": {
        "subject": "Business",
        "resources": [
            {
                "type": "community",
                "title": "LinkedIn",
                "provider": "LinkedIn",
                "url": "https://www.linkedin.com/",
                "description": "Professional networking platform",
                "free": True
            },
            {
                "type": "article",
                "title": "The Wall Street Journal",
                "provider": "WSJ",
                "url": "https://www.wsj.com/",
                "description": "Business and financial news",
                "free": False
            },
            {
                "type": "podcast",
                "title": "Planet Money",
                "provider": "NPR",
                "url": "https://www.npr.org/podcasts/510289/planet-money",
                "description": "Economics explained through stories",
                "free": True
            },
            {
                "type": "tool",
                "title": "Excel",
                "provider": "Microsoft",
                "url": "https://www.microsoft.com/en-us/microsoft-365/excel",
                "description": "Essential tool for business analysis",
                "free": False
            }
        ]
    },
    "mathematics": {
        "subject": "Mathematics",
        "resources": [
            {
                "type": "video",
                "title": "Khan Academy",
                "provider": "Khan Academy",
                "url": "https://www.khanacademy.org/math",
                "description": "Free math education for all levels",
                "free": True
            },
            {
                "type": "video",
                "title": "3Blue1Brown",
                "provider": "3Blue1Brown",
                "url": "https://www.youtube.com/c/3blue1brown",
                "description": "Visual math explanations",
                "free": True
            },
            {
                "type": "community",
                "title": "Mathematics Stack Exchange",
                "provider": "Stack Exchange",
                "url": "https://math.stackexchange.com/",
                "description": "Q&A for math problems",
                "free": True
            }
        ]
    }
}


# Study tips and productivity resources
STUDY_RESOURCES = {
    "study_techniques": [
        {
            "technique": "Pomodoro Technique",
            "description": "Study for 25 minutes, break for 5. Repeat.",
            "tools": ["Forest App", "Pomofocus"],
            "best_for": "Maintaining focus during long study sessions"
        },
        {
            "technique": "Active Recall",
            "description": "Test yourself instead of re-reading notes",
            "tools": ["Anki", "Quizlet"],
            "best_for": "Memorization and long-term retention"
        },
        {
            "technique": "Spaced Repetition",
            "description": "Review material at increasing intervals",
            "tools": ["Anki", "RemNote"],
            "best_for": "Retaining large amounts of information"
        },
        {
            "technique": "Feynman Technique",
            "description": "Explain concepts in simple terms to test understanding",
            "tools": ["Teaching others", "Writing explanations"],
            "best_for": "Deep understanding of complex topics"
        }
    ],
    "productivity_tools": [
        {
            "name": "Notion",
            "category": "Note-taking",
            "url": "https://www.notion.so/",
            "description": "All-in-one workspace for notes and organization",
            "free": True
        },
        {
            "name": "Todoist",
            "category": "Task Management",
            "url": "https://todoist.com/",
            "description": "Simple and powerful to-do list",
            "free": True
        },
        {
            "name": "Forest",
            "category": "Focus",
            "url": "https://www.forestapp.cc/",
            "description": "Stay focused and plant virtual trees",
            "free": False
        },
        {
            "name": "Anki",
            "category": "Flashcards",
            "url": "https://apps.ankiweb.net/",
            "description": "Spaced repetition flashcard system",
            "free": True
        }
    ]
}


def get_resources_for_course(course_id: str) -> Dict:
    """Get all resources for a specific course"""
    return COURSE_RESOURCES.get(course_id, {
        "course_name": course_id,
        "resources": [],
        "message": "No specific resources available for this course yet"
    })


def get_free_resources_for_course(course_id: str) -> List[Dict]:
    """Get only free resources for a course"""
    course_data = COURSE_RESOURCES.get(course_id, {})
    resources = course_data.get("resources", [])
    return [r for r in resources if r.get("free", False)]
