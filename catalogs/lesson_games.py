# Lesson mini-games: interactive concept demonstrations for course lessons
# Each lesson can have a simple, engaging game to reinforce learning

from typing import Dict, List, Any

class LessonGame:
    """Defines an interactive mini-game for a lesson"""
    def __init__(
        self,
        game_id: str,
        lesson_id: str,
        title: str,
        game_type: str,  # "coding", "memory", "puzzle", "simulation", "matching", "interactive"
        description: str,
        objectives: List[str],
        difficulty: str,  # "beginner", "intermediate", "advanced"
        estimated_duration_minutes: int,
        content: Dict[str, Any],  # Game-specific content
    ):
        self.game_id = game_id
        self.lesson_id = lesson_id
        self.title = title
        self.game_type = game_type
        self.description = description
        self.objectives = objectives
        self.difficulty = difficulty
        self.estimated_duration_minutes = estimated_duration_minutes
        self.content = content


# Lesson games mapped by lesson ID
LESSON_GAMES = {
    # CS101 - Intro Programming
    "lesson_1": {  # Variables and Data Types
        "game_id": "game_cs101_01",
        "lesson_id": "lesson_1",
        "title": "Variable Type Guess",
        "game_type": "interactive",
        "description": "Identify the correct data type for different values. Click on values and categorize them as integers, strings, floats, or booleans.",
        "objectives": [
            "Understand different data types",
            "Recognize how to categorize values",
            "Learn type syntax in Python"
        ],
        "difficulty": "beginner",
        "estimated_duration_minutes": 5,
        "content": {
            "rounds": [
                {
                    "value": "42",
                    "correct_type": "integer",
                    "explanation": "42 is a whole number with no decimal point"
                },
                {
                    "value": "'Hello'",
                    "correct_type": "string",
                    "explanation": "Text in quotes is a string"
                },
                {
                    "value": "3.14",
                    "correct_type": "float",
                    "explanation": "Numbers with decimal points are floats"
                },
                {
                    "value": "True",
                    "correct_type": "boolean",
                    "explanation": "True and False are boolean values"
                },
                {
                    "value": "'2024'",
                    "correct_type": "string",
                    "explanation": "Even though it looks like a number, quotes make it a string"
                }
            ],
            "type_options": ["integer", "string", "float", "boolean"],
            "points_per_correct": 10
        }
    },
    "lesson_2": {  # Control Flow (if/else)
        "game_id": "game_cs101_02",
        "lesson_id": "lesson_2",
        "title": "Decision Tree Builder",
        "game_type": "puzzle",
        "description": "Build decision logic by arranging if/elif/else conditions. Complete scenarios by choosing the right conditions in the correct order.",
        "objectives": [
            "Understand conditional logic",
            "Practice if/elif/else syntax",
            "Learn to structure decision trees"
        ],
        "difficulty": "beginner",
        "estimated_duration_minutes": 7,
        "content": {
            "scenarios": [
                {
                    "scenario": "Check if someone can vote (age >= 18)",
                    "conditions": [
                        {"condition": "age >= 18", "result": "Can vote", "order": 1},
                        {"condition": "else", "result": "Too young to vote", "order": 2}
                    ],
                    "points": 20
                },
                {
                    "scenario": "Grade determination (90+: A, 80+: B, 70+: C, else: F)",
                    "conditions": [
                        {"condition": "score >= 90", "result": "Grade A", "order": 1},
                        {"condition": "score >= 80", "result": "Grade B", "order": 2},
                        {"condition": "score >= 70", "result": "Grade C", "order": 3},
                        {"condition": "else", "result": "Grade F", "order": 4}
                    ],
                    "points": 30
                },
                {
                    "scenario": "Even or odd number checker",
                    "conditions": [
                        {"condition": "number % 2 == 0", "result": "Even number", "order": 1},
                        {"condition": "else", "result": "Odd number", "order": 2}
                    ],
                    "points": 20
                }
            ]
        }
    },
    "lesson_3": {  # Loops (for/while)
        "game_id": "game_cs101_03",
        "lesson_id": "lesson_3",
        "title": "Loop Counter Challenge",
        "game_type": "coding",
        "description": "Write simple loop code to accomplish tasks. Predict loop output and complete missing loop code.",
        "objectives": [
            "Understand loop iteration",
            "Practice for and while loop syntax",
            "Learn loop control (break, continue)"
        ],
        "difficulty": "beginner",
        "estimated_duration_minutes": 8,
        "content": {
            "challenges": [
                {
                    "title": "Count to 10",
                    "task": "Write a loop that prints numbers 1 to 10",
                    "hint": "Use 'for i in range(1, 11):'",
                    "sample_code": "for i in range(?, ?):\n    print(i)",
                    "expected_output": "1\n2\n3\n4\n5\n6\n7\n8\n9\n10",
                    "points": 25
                },
                {
                    "title": "Sum of Numbers",
                    "task": "Write a loop to sum numbers 1 through 5",
                    "hint": "Use range and accumulate values",
                    "sample_code": "total = ?\nfor i in ?:\n    total += i\nprint(total)",
                    "expected_output": "15",
                    "points": 25
                },
                {
                    "title": "Print Even Numbers",
                    "task": "Loop through 1-20 and print only even numbers",
                    "hint": "Use if statement inside loop",
                    "sample_code": "for i in range(1, 21):\n    if ?:\n        print(i)",
                    "expected_output": "2\n4\n6\n8\n10\n12\n14\n16\n18\n20",
                    "points": 25
                }
            ]
        }
    },
    "lesson_4": {  # Functions
        "game_id": "game_cs101_04",
        "lesson_id": "lesson_4",
        "title": "Function Factory",
        "game_type": "interactive",
        "description": "Create and test functions. Match function definitions to their behavior and test function calls.",
        "objectives": [
            "Understand function definition",
            "Learn function parameters and return values",
            "Practice function calls"
        ],
        "difficulty": "intermediate",
        "estimated_duration_minutes": 8,
        "content": {
            "challenges": [
                {
                    "title": "Simple Greeting Function",
                    "definition": "def greet(name):\n    return f'Hello, {name}!'",
                    "test_cases": [
                        {"input": "greet('Alice')", "expected": "Hello, Alice!"},
                        {"input": "greet('Bob')", "expected": "Hello, Bob!"}
                    ],
                    "points": 20
                },
                {
                    "title": "Add Two Numbers",
                    "definition": "def add(a, b):\n    return a + b",
                    "test_cases": [
                        {"input": "add(3, 5)", "expected": "8"},
                        {"input": "add(10, 20)", "expected": "30"}
                    ],
                    "points": 20
                },
                {
                    "title": "Check if Number is Positive",
                    "definition": "def is_positive(num):\n    return num > 0",
                    "test_cases": [
                        {"input": "is_positive(5)", "expected": "True"},
                        {"input": "is_positive(-3)", "expected": "False"}
                    ],
                    "points": 20
                }
            ]
        }
    },
    "lesson_5": {  # Lists and Dictionaries
        "game_id": "game_cs101_05",
        "lesson_id": "lesson_5",
        "title": "Data Structure Organizer",
        "game_type": "puzzle",
        "description": "Organize data into lists and dictionaries. Choose the right data structure for different scenarios.",
        "objectives": [
            "Understand when to use lists vs dictionaries",
            "Practice indexing and access patterns",
            "Learn data organization principles"
        ],
        "difficulty": "intermediate",
        "estimated_duration_minutes": 7,
        "content": {
            "scenarios": [
                {
                    "scenario": "Store a to-do list",
                    "correct_structure": "list",
                    "explanation": "Use a list because order matters and you need to track multiple items in sequence",
                    "example": "todos = ['Buy milk', 'Write code', 'Call friend']"
                },
                {
                    "scenario": "Store student information (name, age, gpa)",
                    "correct_structure": "dictionary",
                    "explanation": "Use a dictionary because you need to associate values with meaningful keys",
                    "example": "student = {'name': 'Alice', 'age': 20, 'gpa': 3.8}"
                },
                {
                    "scenario": "Store list of temperatures for a week",
                    "correct_structure": "list",
                    "explanation": "Use a list because you have ordered sequential data",
                    "example": "temps = [72, 75, 68, 70, 76, 80, 78]"
                },
                {
                    "scenario": "Store contact information (phone, email, address)",
                    "correct_structure": "dictionary",
                    "explanation": "Use a dictionary to map labels to contact details",
                    "example": "contact = {'phone': '555-1234', 'email': 'user@example.com'}"
                }
            ],
            "structure_options": ["list", "dictionary"]
        }
    }
}


def get_lesson_game(lesson_id: str) -> Dict[str, Any]:
    """Get game for a specific lesson"""
    return LESSON_GAMES.get(lesson_id)


def get_lesson_games_by_course(course_id: str) -> List[Dict[str, Any]]:
    """Get all games for a course (based on course lessons)"""
    from catalogs.course_content import get_course_lessons
    
    lessons = get_course_lessons(course_id)
    games = []
    
    for lesson in lessons:
        game = get_lesson_game(lesson.get("id"))
        if game:
            games.append(game)
    
    return games
