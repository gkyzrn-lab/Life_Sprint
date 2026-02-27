# Course learning content - quizzes, lessons, and learning objectives
# Provides structured learning materials for each course

from typing import Dict, List


class CourseContent:
    """Defines learning content for a course"""
    def __init__(self, course_id: str, course_title: str, topics: List[str], lessons: List[Dict], quizzes: List[Dict]):
        self.course_id = course_id
        self.course_title = course_title
        self.topics = topics
        self.lessons = lessons
        self.quizzes = quizzes


# Learning content by course
COURSE_CONTENT = {
    "cs101": {
        "title": "Intro Programming",
        "topics": [
            "Variables and Data Types",
            "Control Flow (if/else)",
            "Loops (for/while)",
            "Functions",
            "Lists and Dictionaries"
        ],
        "lessons": [
            {
                "id": "lesson_1",
                "topic": "Variables and Data Types",
                "title": "Understanding Variables",
                "content": "A variable is a named container for storing data. Learn about integers, strings, floats, and booleans.",
                "duration_minutes": 15,
                "difficulty": "beginner"
            },
            {
                "id": "lesson_2",
                "topic": "Control Flow (if/else)",
                "title": "Making Decisions with If Statements",
                "content": "Control flow allows your program to make decisions. Use if, elif, and else to create branching logic.",
                "duration_minutes": 20,
                "difficulty": "beginner"
            },
            {
                "id": "lesson_3",
                "topic": "Loops (for/while)",
                "title": "Repeating Code with Loops",
                "content": "Loops let you repeat code multiple times. Learn about for loops and while loops to automate repetitive tasks.",
                "duration_minutes": 25,
                "difficulty": "beginner"
            },
            {
                "id": "lesson_4",
                "topic": "Functions",
                "title": "Creating Reusable Code with Functions",
                "content": "Functions allow you to package code into reusable blocks. Learn how to define, call, and return values from functions.",
                "duration_minutes": 30,
                "difficulty": "intermediate"
            },
            {
                "id": "lesson_5",
                "topic": "Lists and Dictionaries",
                "title": "Organizing Data with Collections",
                "content": "Lists and dictionaries store multiple values. Understand indexing, slicing, and iteration over collections.",
                "duration_minutes": 35,
                "difficulty": "intermediate"
            }
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Variables and Data Types",
                "title": "Variables Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What is a variable?",
                        "options": [
                            "A named container for storing data",
                            "A function that performs calculations",
                            "A type of loop",
                            "A way to comment code"
                        ],
                        "correct_answer": "A named container for storing data",
                        "explanation": "A variable is a named location in memory that stores a value."
                    },
                    {
                        "id": "q2",
                        "question": "Which of these is a valid variable name in Python?",
                        "options": [
                            "my-variable",
                            "2myvar",
                            "my_variable",
                            "my variable"
                        ],
                        "correct_answer": "my_variable",
                        "explanation": "Python variable names can contain letters, numbers, and underscores, but cannot start with a number or contain spaces."
                    },
                    {
                        "id": "q3",
                        "question": "What is the data type of 'Hello World'?",
                        "options": [
                            "Integer",
                            "Float",
                            "String",
                            "Boolean"
                        ],
                        "correct_answer": "String",
                        "explanation": "Text enclosed in quotes is a string data type."
                    }
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Control Flow (if/else)",
                "title": "If/Else Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What does the 'elif' keyword mean?",
                        "options": [
                            "End if",
                            "Else if",
                            "Else in for loop",
                            "Else if left"
                        ],
                        "correct_answer": "Else if",
                        "explanation": "'elif' is short for 'else if' and provides an additional condition to check."
                    },
                    {
                        "id": "q2",
                        "question": "How many 'else' statements can you have in one if/elif/else block?",
                        "options": [
                            "None",
                            "One",
                            "Multiple",
                            "As many as you want"
                        ],
                        "correct_answer": "One",
                        "explanation": "You can have at most one 'else' statement at the end of an if/elif/else block."
                    },
                    {
                        "id": "q3",
                        "question": "What is the correct syntax for an if statement in Python?",
                        "options": [
                            "if (condition) { }",
                            "if condition:",
                            "if: condition",
                            "if condition then:"
                        ],
                        "correct_answer": "if condition:",
                        "explanation": "Python uses 'if condition:' followed by an indented block to define conditional logic."
                    }
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_3",
                "topic": "Functions",
                "title": "Functions Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What keyword is used to define a function?",
                        "options": [
                            "function",
                            "def",
                            "define",
                            "func"
                        ],
                        "correct_answer": "def",
                        "explanation": "The 'def' keyword is used to define a function in Python."
                    },
                    {
                        "id": "q2",
                        "question": "What does the 'return' statement do?",
                        "options": [
                            "Goes back to the beginning of the function",
                            "Sends a value back to the caller",
                            "Stops the program",
                            "Repeats the function"
                        ],
                        "correct_answer": "Sends a value back to the caller",
                        "explanation": "'return' sends a value back to wherever the function was called."
                    },
                    {
                        "id": "q3",
                        "question": "What are the inputs to a function called?",
                        "options": [
                            "Returns",
                            "Arguments or Parameters",
                            "Variables",
                            "Functions"
                        ],
                        "correct_answer": "Arguments or Parameters",
                        "explanation": "Inputs to a function are called arguments (when passed in) or parameters (in the function definition)."
                    }
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_4",
                "topic": "Loops (for/while)",
                "title": "Loops Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "Which loop type is best for iterating a fixed number of times?",
                        "options": [
                            "while loop",
                            "for loop",
                            "do-while loop",
                            "repeat loop"
                        ],
                        "correct_answer": "for loop",
                        "explanation": "A for loop is ideal when you know exactly how many times you need to iterate."
                    },
                    {
                        "id": "q2",
                        "question": "What is the difference between 'for' and 'while' loops?",
                        "options": [
                            "There is no difference",
                            "for loops are faster",
                            "for loops iterate a set number of times, while loops run until a condition is false",
                            "while loops are used only in Python"
                        ],
                        "correct_answer": "for loops iterate a set number of times, while loops run until a condition is false",
                        "explanation": "For loops are typically used with known iteration counts (like lists), while while loops continue until a condition becomes false."
                    },
                    {
                        "id": "q3",
                        "question": "What will 'range(5)' produce in Python?",
                        "options": [
                            "1, 2, 3, 4, 5",
                            "0, 1, 2, 3, 4",
                            "1, 2, 3, 4",
                            "5, 4, 3, 2, 1"
                        ],
                        "correct_answer": "0, 1, 2, 3, 4",
                        "explanation": "range(5) generates numbers from 0 to 4 (5 numbers total), starting at 0."
                    }
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_5",
                "topic": "Lists and Dictionaries",
                "title": "Data Collections Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "How do you access the first element of a list?",
                        "options": [
                            "list[1]",
                            "list[0]",
                            "list.first()",
                            "list{0}"
                        ],
                        "correct_answer": "list[0]",
                        "explanation": "Python uses zero-based indexing, so the first element is at index 0."
                    },
                    {
                        "id": "q2",
                        "question": "What is the correct syntax to create a dictionary?",
                        "options": [
                            "dict = [key: value]",
                            "dict = {key: value}",
                            "dict = (key, value)",
                            "dict = key, value"
                        ],
                        "correct_answer": "dict = {key: value}",
                        "explanation": "Dictionaries in Python are created using curly braces {} with key-value pairs."
                    },
                    {
                        "id": "q3",
                        "question": "How do you add an element to a list?",
                        "options": [
                            "list.add(item)",
                            "list.push(item)",
                            "list.append(item)",
                            "list[+1] = item"
                        ],
                        "correct_answer": "list.append(item)",
                        "explanation": "The append() method adds an element to the end of a list."
                    }
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": [
            "Write and execute Python code",
            "Use variables and data types",
            "Apply control flow logic",
            "Create reusable functions",
            "Work with data collections"
        ]
    },
    "ba101": {
        "title": "Intro Business",
        "topics": [
            "Business Fundamentals",
            "Economics 101",
            "Marketing Basics",
            "Finance Essentials",
            "Entrepreneurship"
        ],
        "lessons": [
            {
                "id": "lesson_1",
                "topic": "Business Fundamentals",
                "title": "What is Business?",
                "content": "Explore the core concepts of business including production, consumption, and value creation.",
                "duration_minutes": 20,
                "difficulty": "beginner"
            },
            {
                "id": "lesson_2",
                "topic": "Economics 101",
                "title": "Supply and Demand",
                "content": "Understand how supply and demand affect pricing and market dynamics.",
                "duration_minutes": 25,
                "difficulty": "beginner"
            },
            {
                "id": "lesson_3",
                "topic": "Marketing Basics",
                "title": "Marketing Fundamentals",
                "content": "Learn the 4 Ps of marketing: Product, Price, Place, and Promotion.",
                "duration_minutes": 25,
                "difficulty": "intermediate"
            },
            {
                "id": "lesson_4",
                "topic": "Finance Essentials",
                "title": "Financial Statements",
                "content": "Understand income statements, balance sheets, and cash flow statements.",
                "duration_minutes": 30,
                "difficulty": "intermediate"
            },
            {
                "id": "lesson_5",
                "topic": "Entrepreneurship",
                "title": "Starting Your Own Business",
                "content": "Learn the key steps to start and grow your own business venture.",
                "duration_minutes": 35,
                "difficulty": "intermediate"
            }
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Business Fundamentals",
                "title": "Business Basics Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What is the primary goal of a business?",
                        "options": [
                            "To create value and generate profit",
                            "To employ people",
                            "To pay taxes",
                            "To compete with competitors"
                        ],
                        "correct_answer": "To create value and generate profit",
                        "explanation": "The primary goal of a business is to create value for customers and generate profit."
                    },
                    {
                        "id": "q2",
                        "question": "What are the three main sectors of an economy?",
                        "options": [
                            "Public, Private, Government",
                            "Primary, Secondary, Tertiary",
                            "Profit, Non-profit, Government",
                            "Small, Medium, Large"
                        ],
                        "correct_answer": "Primary, Secondary, Tertiary",
                        "explanation": "The three main sectors are primary (raw materials), secondary (manufacturing), and tertiary (services)."
                    },
                    {
                        "id": "q3",
                        "question": "What is an entrepreneur?",
                        "options": [
                            "A person who works for a large corporation",
                            "Someone who takes financial risks to create a business",
                            "A government official",
                            "A person who invests in stocks"
                        ],
                        "correct_answer": "Someone who takes financial risks to create a business",
                        "explanation": "An entrepreneur is someone who identifies opportunities and takes risks to start and grow a new business."
                    }
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Economics 101",
                "title": "Economics Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What happens to price when demand increases and supply stays the same?",
                        "options": [
                            "Price decreases",
                            "Price stays the same",
                            "Price increases",
                            "Supply increases"
                        ],
                        "correct_answer": "Price increases",
                        "explanation": "When demand increases and supply remains constant, prices rise due to increased competition for limited goods."
                    },
                    {
                        "id": "q2",
                        "question": "What is inflation?",
                        "options": [
                            "A decrease in prices over time",
                            "A general increase in prices over time, reducing purchasing power",
                            "An increase in the stock market",
                            "A decrease in unemployment"
                        ],
                        "correct_answer": "A general increase in prices over time, reducing purchasing power",
                        "explanation": "Inflation is when the general level of prices increases, meaning your money buys less."
                    },
                    {
                        "id": "q3",
                        "question": "What is a market economy?",
                        "options": [
                            "An economy run entirely by the government",
                            "An economy where prices are determined by supply and demand",
                            "An economy where there is no trade",
                            "An economy that has no money"
                        ],
                        "correct_answer": "An economy where prices are determined by supply and demand",
                        "explanation": "A market economy relies on supply and demand to determine prices and allocate resources."
                    }
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_3",
                "topic": "Marketing Basics",
                "title": "Marketing Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What are the 4 Ps of marketing?",
                        "options": [
                            "Price, Profit, Publicity, Planning",
                            "Product, Price, Place, Promotion",
                            "People, Process, Product, Place",
                            "Pricing, Place, Planning, Performance"
                        ],
                        "correct_answer": "Product, Price, Place, Promotion",
                        "explanation": "The 4 Ps are the core elements of a marketing mix: Product, Price, Place (distribution), and Promotion."
                    },
                    {
                        "id": "q2",
                        "question": "What is a target market?",
                        "options": [
                            "The total number of customers in the world",
                            "The specific group of customers a company aims to reach",
                            "The market value of a company",
                            "The competitors of a business"
                        ],
                        "correct_answer": "The specific group of customers a company aims to reach",
                        "explanation": "A target market is the specific group of people that a company identifies as most likely to buy their products or services."
                    },
                    {
                        "id": "q3",
                        "question": "What is brand loyalty?",
                        "options": [
                            "The amount of money spent on advertising",
                            "How often a customer returns to buy from the same company",
                            "The number of competitors a company has",
                            "The size of the company's workforce"
                        ],
                        "correct_answer": "How often a customer returns to buy from the same company",
                        "explanation": "Brand loyalty is when customers consistently choose to buy from the same company because of satisfaction and trust."
                    }
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_4",
                "topic": "Finance Essentials",
                "title": "Finance Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What is an income statement?",
                        "options": [
                            "A list of all assets a company owns",
                            "A financial statement showing revenue and expenses over a period",
                            "A statement of cash flow",
                            "A list of company employees"
                        ],
                        "correct_answer": "A financial statement showing revenue and expenses over a period",
                        "explanation": "An income statement (also called a P&L statement) shows a company's revenues, expenses, and profit or loss over a period."
                    },
                    {
                        "id": "q2",
                        "question": "What is a balance sheet?",
                        "options": [
                            "A record of daily transactions",
                            "A statement showing assets, liabilities, and equity at a point in time",
                            "A budget for future expenses",
                            "A record of employee salaries"
                        ],
                        "correct_answer": "A statement showing assets, liabilities, and equity at a point in time",
                        "explanation": "A balance sheet shows what a company owns (assets), owes (liabilities), and the owner's stake (equity) at a specific moment."
                    },
                    {
                        "id": "q3",
                        "question": "What is ROI (Return on Investment)?",
                        "options": [
                            "The total amount of money invested",
                            "The profit made relative to the amount invested",
                            "The interest rate on a loan",
                            "The total revenue of a company"
                        ],
                        "correct_answer": "The profit made relative to the amount invested",
                        "explanation": "ROI measures how much profit you make from an investment compared to the amount you invested, usually shown as a percentage."
                    }
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_5",
                "topic": "Entrepreneurship",
                "title": "Entrepreneurship Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What is a business plan?",
                        "options": [
                            "A daily schedule for employees",
                            "A document outlining how a business will operate and succeed",
                            "A list of competitor prices",
                            "A marketing advertisement"
                        ],
                        "correct_answer": "A document outlining how a business will operate and succeed",
                        "explanation": "A business plan is a comprehensive document that describes the business model, strategy, financial projections, and operational details."
                    },
                    {
                        "id": "q2",
                        "question": "What does 'startup' mean?",
                        "options": [
                            "A large established company",
                            "A new business venture, typically in early stages",
                            "The act of turning on equipment",
                            "A government agency"
                        ],
                        "correct_answer": "A new business venture, typically in early stages",
                        "explanation": "A startup is a newly created business venture, often focusing on innovation and growth in the early stages."
                    },
                    {
                        "id": "q3",
                        "question": "What is a business model?",
                        "options": [
                            "A person who models business fashion",
                            "The way a company creates and delivers value to customers",
                            "A list of business expenses",
                            "A legal document for businesses"
                        ],
                        "correct_answer": "The way a company creates and delivers value to customers",
                        "explanation": "A business model describes how a company makes money and delivers value to its customers (e.g., subscription, direct sales, advertising)."
                    }
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": [
            "Understand core business concepts",
            "Apply economic principles",
            "Develop marketing strategies",
            "Read financial statements",
            "Launch a business idea"
        ]
    },
    "cs102": {
        "title": "Data Structures",
        "topics": [
            "Arrays and Lists",
            "Stacks and Queues",
            "Trees and Graphs",
            "Hash Tables",
            "Sorting and Searching"
        ],
        "lessons": [
            {
                "id": "lesson_1",
                "topic": "Arrays and Lists",
                "title": "Understanding Arrays and Linked Lists",
                "content": "Learn how arrays store data sequentially and linked lists connect data through pointers. Understand time complexity for access, insert, and delete operations.",
                "duration_minutes": 25,
                "difficulty": "beginner"
            },
            {
                "id": "lesson_2",
                "topic": "Stacks and Queues",
                "title": "LIFO and FIFO Data Structures",
                "content": "Explore stacks (Last In, First Out) and queues (First In, First Out). See real-world applications like browser history and job scheduling.",
                "duration_minutes": 20,
                "difficulty": "beginner"
            },
            {
                "id": "lesson_3",
                "topic": "Trees and Graphs",
                "title": "Hierarchical and Network Data Structures",
                "content": "Understand tree structures including binary trees, binary search trees, and general graphs. Learn traversal algorithms like BFS and DFS.",
                "duration_minutes": 40,
                "difficulty": "intermediate"
            },
            {
                "id": "lesson_4",
                "topic": "Hash Tables",
                "title": "Fast Lookup with Hash Functions",
                "content": "Learn how hash tables provide O(1) average case lookup time. Understand collision handling and hash function design.",
                "duration_minutes": 30,
                "difficulty": "intermediate"
            },
            {
                "id": "lesson_5",
                "topic": "Sorting and Searching",
                "title": "Efficient Algorithms for Organization",
                "content": "Explore sorting algorithms (QuickSort, MergeSort, HeapSort) and searching techniques (Binary Search). Analyze time complexity of each.",
                "duration_minutes": 35,
                "difficulty": "intermediate"
            }
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Arrays and Lists",
                "title": "Arrays and Lists Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What is the time complexity of accessing an element in an array by index?",
                        "options": [
                            "O(n)",
                            "O(log n)",
                            "O(1)",
                            "O(n²)"
                        ],
                        "correct_answer": "O(1)",
                        "explanation": "Array access by index is constant time because the memory address can be calculated directly."
                    },
                    {
                        "id": "q2",
                        "question": "What is the main disadvantage of a linked list compared to an array?",
                        "options": [
                            "Uses more memory",
                            "No random access - must traverse from the beginning",
                            "Can't store different data types",
                            "Fixed size"
                        ],
                        "correct_answer": "No random access - must traverse from the beginning",
                        "explanation": "Linked lists require traversal from the beginning to access elements, making access O(n), while arrays support O(1) direct access."
                    },
                    {
                        "id": "q3",
                        "question": "What is the time complexity of inserting an element at the beginning of a linked list?",
                        "options": [
                            "O(n)",
                            "O(log n)",
                            "O(1)",
                            "O(n²)"
                        ],
                        "correct_answer": "O(1)",
                        "explanation": "Inserting at the beginning of a linked list only requires changing a few pointers, making it O(1)."
                    }
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Stacks and Queues",
                "title": "Stacks and Queues Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What does LIFO stand for?",
                        "options": [
                            "Last In, First Out",
                            "List In, File Out",
                            "Linear Input, File Output",
                            "Load In, Format Out"
                        ],
                        "correct_answer": "Last In, First Out",
                        "explanation": "LIFO (Last In, First Out) is the principle that the last item added is the first item removed, which is how stacks work."
                    },
                    {
                        "id": "q2",
                        "question": "Which data structure would you use to implement browser back button functionality?",
                        "options": [
                            "Queue",
                            "Stack",
                            "Array",
                            "Tree"
                        ],
                        "correct_answer": "Stack",
                        "explanation": "A stack is perfect for browser history because the last page visited (most recent) is the first one you go back to."
                    },
                    {
                        "id": "q3",
                        "question": "What is the time complexity of pushing and popping from a stack?",
                        "options": [
                            "O(n)",
                            "O(log n)",
                            "O(1)",
                            "O(n²)"
                        ],
                        "correct_answer": "O(1)",
                        "explanation": "Both push and pop operations on a stack are O(1) because they only affect the top element."
                    }
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_3",
                "topic": "Trees and Graphs",
                "title": "Trees and Graphs Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What is a binary tree?",
                        "options": [
                            "A tree where each node has exactly 2 children",
                            "A tree where each node has at most 2 children",
                            "A tree with 2 levels",
                            "A tree with 2 root nodes"
                        ],
                        "correct_answer": "A tree where each node has at most 2 children",
                        "explanation": "A binary tree is a tree where each node has at most 2 children (left and right), but may have 0, 1, or 2."
                    },
                    {
                        "id": "q2",
                        "question": "What is the time complexity of searching in a balanced binary search tree?",
                        "options": [
                            "O(n)",
                            "O(log n)",
                            "O(1)",
                            "O(n²)"
                        ],
                        "correct_answer": "O(log n)",
                        "explanation": "A balanced BST offers O(log n) search time because you eliminate half the remaining nodes with each comparison."
                    },
                    {
                        "id": "q3",
                        "question": "What is DFS (Depth-First Search)?",
                        "options": [
                            "A search that explores breadth first from a node",
                            "A search that explores as far as possible along each branch",
                            "A search that only works on sorted data",
                            "A search that requires a hash table"
                        ],
                        "correct_answer": "A search that explores as far as possible along each branch",
                        "explanation": "DFS explores as deeply as possible along each branch before backtracking, often implemented with recursion or a stack."
                    }
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_4",
                "topic": "Hash Tables",
                "title": "Hash Tables Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What is the average time complexity of a hash table lookup?",
                        "options": [
                            "O(n)",
                            "O(log n)",
                            "O(1)",
                            "O(n²)"
                        ],
                        "correct_answer": "O(1)",
                        "explanation": "Hash tables provide average case O(1) lookup time by using a hash function to calculate the index directly."
                    },
                    {
                        "id": "q2",
                        "question": "What is a hash collision?",
                        "options": [
                            "When two keys hash to the same index",
                            "When the hash table is full",
                            "When the hash function is too slow",
                            "When the table needs to be resized"
                        ],
                        "correct_answer": "When two keys hash to the same index",
                        "explanation": "A collision occurs when two different keys hash to the same array index, requiring a collision resolution strategy."
                    },
                    {
                        "id": "q3",
                        "question": "Which approach handles collisions by searching for the next available slot?",
                        "options": [
                            "Chaining",
                            "Open addressing",
                            "Rehashing",
                            "Bucketing"
                        ],
                        "correct_answer": "Open addressing",
                        "explanation": "Open addressing handles collisions by finding another empty slot in the table, using techniques like linear probing."
                    }
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_5",
                "topic": "Sorting and Searching",
                "title": "Sorting and Searching Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What is the time complexity of binary search?",
                        "options": [
                            "O(n)",
                            "O(log n)",
                            "O(1)",
                            "O(n²)"
                        ],
                        "correct_answer": "O(log n)",
                        "explanation": "Binary search achieves O(log n) time by eliminating half of the remaining elements with each comparison on sorted data."
                    },
                    {
                        "id": "q2",
                        "question": "Which sorting algorithm has O(n log n) time complexity in all cases (best, average, and worst)?",
                        "options": [
                            "QuickSort",
                            "BubbleSort",
                            "MergeSort",
                            "InsertionSort"
                        ],
                        "correct_answer": "MergeSort",
                        "explanation": "MergeSort guarantees O(n log n) in best, average, and worst cases due to its divide-and-conquer approach."
                    },
                    {
                        "id": "q3",
                        "question": "What is the space complexity of QuickSort?",
                        "options": [
                            "O(n)",
                            "O(log n)",
                            "O(1)",
                            "O(n²)"
                        ],
                        "correct_answer": "O(log n)",
                        "explanation": "QuickSort uses O(log n) space due to the recursion call stack, making it more space-efficient than MergeSort which needs O(n)."
                    }
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": [
            "Understand fundamental data structures",
            "Analyze time and space complexity",
            "Choose appropriate data structures for problems",
            "Implement basic data structures",
            "Optimize algorithm performance"
        ]
    },
    "bus101": {
        "title": "Introduction to Business",
        "topics": [
            "Business Fundamentals",
            "Types of Business Organizations",
            "Global Economy",
            "Business Ethics",
            "Entrepreneurship Basics"
        ],
        "lessons": [
            {
                "id": "lesson_1",
                "topic": "Business Fundamentals",
                "title": "What is Business?",
                "content": "Learn the core principles of business including value creation, stakeholders, and profit generation.",
                "duration_minutes": 20,
                "difficulty": "beginner"
            },
            {
                "id": "lesson_2",
                "topic": "Types of Business Organizations",
                "title": "Sole Proprietorships to Corporations",
                "content": "Understand different business structures including partnerships, LLCs, and corporations.",
                "duration_minutes": 25,
                "difficulty": "beginner"
            },
            {
                "id": "lesson_3",
                "topic": "Global Economy",
                "title": "Understanding Global Markets",
                "content": "Explore international trade, globalization, and multinational corporations.",
                "duration_minutes": 30,
                "difficulty": "intermediate"
            }
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Business Fundamentals",
                "title": "Business Basics",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What is the primary purpose of a for-profit business?",
                        "options": [
                            "To employ as many people as possible",
                            "To generate profit for owners/shareholders",
                            "To pay taxes to the government",
                            "To eliminate competition"
                        ],
                        "correct_answer": "To generate profit for owners/shareholders",
                        "explanation": "While businesses have multiple stakeholders, the primary purpose of a for-profit business is to generate profit for its owners or shareholders."
                    },
                    {
                        "id": "q2",
                        "question": "Which factor of production includes buildings and machinery?",
                        "options": [
                            "Land",
                            "Labor",
                            "Capital",
                            "Entrepreneurship"
                        ],
                        "correct_answer": "Capital",
                        "explanation": "Capital includes physical assets like buildings, machinery, and equipment used in production."
                    },
                    {
                        "id": "q3",
                        "question": "What is a stakeholder?",
                        "options": [
                            "Only the shareholders of a company",
                            "Anyone affected by a business's operations",
                            "Only the employees",
                            "The board of directors only"
                        ],
                        "correct_answer": "Anyone affected by a business's operations",
                        "explanation": "Stakeholders include anyone with an interest in the business: shareholders, employees, customers, suppliers, and the community."
                    }
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Business Organizations",
                "title": "Business Structures",
                "questions": [
                    {
                        "id": "q1",
                        "question": "What is the main advantage of a corporation?",
                        "options": [
                            "Easiest to set up",
                            "No taxes required",
                            "Limited liability for owners",
                            "Only one owner allowed"
                        ],
                        "correct_answer": "Limited liability for owners",
                        "explanation": "Corporations provide limited liability, meaning owners are not personally responsible for business debts."
                    },
                    {
                        "id": "q2",
                        "question": "What is double taxation in a C-corporation?",
                        "options": [
                            "Paying taxes twice a year",
                            "Corporation pays tax on profits, then shareholders pay tax on dividends",
                            "Paying both state and federal taxes",
                            "Two different tax rates"
                        ],
                        "correct_answer": "Corporation pays tax on profits, then shareholders pay tax on dividends",
                        "explanation": "Double taxation occurs when corporate profits are taxed at the corporate level, and then dividends to shareholders are taxed again as personal income."
                    },
                    {
                        "id": "q3",
                        "question": "In a sole proprietorship, who is liable for business debts?",
                        "options": [
                            "No one",
                            "The government",
                            "Only the business",
                            "The owner personally"
                        ],
                        "correct_answer": "The owner personally",
                        "explanation": "In a sole proprietorship, there is no legal separation between the owner and the business, so the owner has unlimited personal liability."
                    }
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": [
            "Understand business fundamentals",
            "Identify different business structures",
            "Recognize stakeholder interests",
            "Understand basic business operations"
        ]
    },
    "econ101": {
        "title": "Microeconomics",
        "topics": [
            "Supply and Demand",
            "Market Equilibrium",
            "Elasticity",
            "Consumer Theory",
            "Market Structures"
        ],
        "lessons": [
            {
                "id": "lesson_1",
                "topic": "Supply and Demand",
                "title": "The Foundation of Economics",
                "content": "Master the laws of supply and demand and how they determine prices in markets.",
                "duration_minutes": 30,
                "difficulty": "intermediate"
            },
            {
                "id": "lesson_2",
                "topic": "Market Equilibrium",
                "title": "Where Supply Meets Demand",
                "content": "Understand how markets reach equilibrium and what causes shifts.",
                "duration_minutes": 25,
                "difficulty": "intermediate"
            },
            {
                "id": "lesson_3",
                "topic": "Elasticity",
                "title": "Price Sensitivity",
                "content": "Learn how elasticity measures responsiveness to price changes.",
                "duration_minutes": 30,
                "difficulty": "intermediate"
            }
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Supply and Demand",
                "title": "Supply and Demand Quiz",
                "questions": [
                    {
                        "id": "q1",
                        "question": "According to the law of demand, what happens when price increases?",
                        "options": [
                            "Quantity demanded increases",
                            "Quantity demanded decreases",
                            "Supply increases",
                            "Nothing changes"
                        ],
                        "correct_answer": "Quantity demanded decreases",
                        "explanation": "The law of demand states that as price increases, quantity demanded decreases, assuming all else equal."
                    },
                    {
                        "id": "q2",
                        "question": "What causes a rightward shift in the supply curve?",
                        "options": [
                            "Increase in production costs",
                            "Decrease in number of sellers",
                            "Improvement in technology",
                            "Increase in taxes"
                        ],
                        "correct_answer": "Improvement in technology",
                        "explanation": "Technology improvements reduce costs and increase supply, shifting the supply curve to the right."
                    },
                    {
                        "id": "q3",
                        "question": "What is a substitute good?",
                        "options": [
                            "A good used together with another",
                            "A good that can replace another",
                            "A cheaper version of the same good",
                            "A luxury good"
                        ],
                        "correct_answer": "A good that can replace another",
                        "explanation": "Substitute goods can replace each other in consumption, like Coke and Pepsi."
                    },
                    {
                        "id": "q4",
                        "question": "If demand increases and supply stays constant, what happens to equilibrium price?",
                        "options": [
                            "Price decreases",
                            "Price increases",
                            "Price stays the same",
                            "Quantity decreases"
                        ],
                        "correct_answer": "Price increases",
                        "explanation": "When demand increases with constant supply, competition for limited goods drives prices higher."
                    }
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_2",
                "topic": "Elasticity",
                "title": "Price Elasticity",
                "questions": [
                    {
                        "id": "q1",
                        "question": "When is demand considered elastic?",
                        "options": [
                            "When elasticity < 1",
                            "When elasticity > 1",
                            "When elasticity = 1",
                            "When elasticity = 0"
                        ],
                        "correct_answer": "When elasticity > 1",
                        "explanation": "Elastic demand means quantity changes by a larger percentage than price (elasticity > 1)."
                    },
                    {
                        "id": "q2",
                        "question": "Which product typically has inelastic demand?",
                        "options": [
                            "Luxury cars",
                            "Designer clothing",
                            "Insulin for diabetics",
                            "Vacation packages"
                        ],
                        "correct_answer": "Insulin for diabetics",
                        "explanation": "Necessities like insulin have inelastic demand because people need them regardless of price."
                    },
                    {
                        "id": "q3",
                        "question": "What happens to total revenue when price increases for an elastic good?",
                        "options": [
                            "Revenue increases",
                            "Revenue decreases",
                            "Revenue stays the same",
                            "Quantity increases"
                        ],
                        "correct_answer": "Revenue decreases",
                        "explanation": "For elastic goods, the percentage decrease in quantity is larger than the price increase, so total revenue falls."
                    }
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": [
            "Understand supply and demand mechanics",
            "Analyze market equilibrium",
            "Calculate and interpret elasticity",
            "Evaluate consumer behavior"
        ]
    },
    "math141": {
        "title": "Calculus I",
        "topics": ["Limits", "Derivatives", "Applications of Derivatives", "Integration Basics"],
        "lessons": [
            {"id": "lesson_1", "topic": "Limits", "title": "Understanding Limits", "content": "Master the concept of limits and continuity.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Derivatives", "title": "The Derivative", "content": "Learn differentiation rules and techniques.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Applications", "title": "Real-World Applications", "content": "Apply derivatives to optimization and related rates problems.", "duration_minutes": 40, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Limits and Derivatives",
                "title": "Calculus Fundamentals",
                "questions": [
                    {"id": "q1", "question": "What is the limit as x approaches 0 of sin(x)/x?", "options": ["0", "1", "Infinity", "Does not exist"], "correct_answer": "1", "explanation": "This is a famous limit that equals 1, proved using the squeeze theorem."},
                    {"id": "q2", "question": "What does the derivative represent?", "options": ["The area under a curve", "The instantaneous rate of change", "The total distance", "The average value"], "correct_answer": "The instantaneous rate of change", "explanation": "The derivative measures how a function changes at a specific point."},
                    {"id": "q3", "question": "What is the derivative of x²?", "options": ["x", "2x", "x²", "2"], "correct_answer": "2x", "explanation": "Using the power rule: d/dx(x^n) = n*x^(n-1), so d/dx(x²) = 2x."},
                    {"id": "q4", "question": "At a critical point, what is true about the derivative?", "options": ["It equals zero or is undefined", "It is positive", "It is negative", "It equals one"], "correct_answer": "It equals zero or is undefined", "explanation": "Critical points occur where f'(x) = 0 or f'(x) does not exist."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Calculate limits", "Differentiate functions", "Solve optimization problems", "Analyze function behavior"]
    },
    "eng101": {
        "title": "English Composition",
        "topics": ["Academic Writing", "Research Methods", "Citation Styles", "Persuasive Writing"],
        "lessons": [
            {"id": "lesson_1", "topic": "Academic Writing", "title": "Writing Clear Prose", "content": "Develop clear, concise academic writing skills.", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Research", "title": "Finding Credible Sources", "content": "Learn to evaluate and cite academic sources.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Writing Fundamentals",
                "title": "Composition Basics",
                "questions": [
                    {"id": "q1", "question": "What is a thesis statement?", "options": ["The conclusion of an essay", "The main argument or claim of an essay", "A quotation from a source", "The introduction paragraph"], "correct_answer": "The main argument or claim of an essay", "explanation": "A thesis statement presents the main argument or central claim of your essay."},
                    {"id": "q2", "question": "What does MLA stand for?", "options": ["Modern Literature Association", "Modern Language Association", "Multiple Language Analysis", "Major Literary Archive"], "correct_answer": "Modern Language Association", "explanation": "MLA (Modern Language Association) is a common citation style for humanities papers."},
                    {"id": "q3", "question": "What is plagiarism?", "options": ["Using too many sources", "Presenting someone else's work as your own", "Writing a long essay", "Citing sources incorrectly"], "correct_answer": "Presenting someone else's work as your own", "explanation": "Plagiarism is using someone else's words or ideas without proper attribution."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Write clear academic prose", "Conduct research", "Cite sources properly", "Construct persuasive arguments"]
    },
    "cs201": {
        "title": "Discrete Mathematics",
        "topics": ["Logic", "Proofs", "Sets", "Functions", "Graph Theory"],
        "lessons": [
            {"id": "lesson_1", "topic": "Logic", "title": "Propositional Logic", "content": "Master logic statements, truth tables, and logical operators.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Proofs", "title": "Proof Techniques", "content": "Learn direct proofs, contradiction, and induction.", "duration_minutes": 35, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Logic and Proofs",
                "title": "Discrete Math Fundamentals",
                "questions": [
                    {"id": "q1", "question": "What is the negation of 'All birds can fly'?", "options": ["All birds cannot fly", "Some birds cannot fly", "No birds can fly", "Some birds can fly"], "correct_answer": "Some birds cannot fly", "explanation": "The negation of 'for all x, P(x)' is 'there exists an x such that not P(x)'."},
                    {"id": "q2", "question": "What proof technique assumes the opposite and derives a contradiction?", "options": ["Direct proof", "Proof by contradiction", "Proof by induction", "Constructive proof"], "correct_answer": "Proof by contradiction", "explanation": "Proof by contradiction assumes the negation of what you want to prove and shows this leads to an impossibility."},
                    {"id": "q3", "question": "In graph theory, what is a tree?", "options": ["A graph with cycles", "A connected graph with no cycles", "A disconnected graph", "A graph with all vertices connected to all others"], "correct_answer": "A connected graph with no cycles", "explanation": "A tree is a connected, acyclic graph."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Apply logical reasoning", "Construct mathematical proofs", "Understand set theory", "Analyze graph structures"]
    },
    "math142": {
        "title": "Calculus II",
        "topics": ["Integration", "Series", "Applications"],
        "lessons": [{"id": "lesson_1", "topic": "Integration", "title": "Integration Methods", "content": "Master integration techniques.", "duration_minutes": 35, "difficulty": "high"}],
        "quizzes": [{
            "id": "quiz_1",
            "topic": "Integration",
            "title": "Integration Techniques",
            "questions": [
                {"id": "q1", "question": "What is the integral of 1/x?", "options": ["x²/2", "ln|x| + C", "1/x² + C", "e^x + C"], "correct_answer": "ln|x| + C", "explanation": "The antiderivative of 1/x is ln|x| + C."},
                {"id": "q2", "question": "Which technique for ∫x·e^x dx?", "options": ["Substitution", "Integration by parts", "Partial fractions", "Direct"], "correct_answer": "Integration by parts", "explanation": "Use integration by parts for products."},
                {"id": "q3", "question": "Definite integral represents?", "options": ["Derivative", "Area under curve", "Slope", "Limit"], "correct_answer": "Area under curve", "explanation": "Definite integrals calculate area."}
            ],
            "passing_score": 70,
            "difficulty": "high"
        }],
        "learning_outcomes": ["Master integration", "Apply integrals", "Analyze series"]
    },
    "cs203": {
        "title": "Algorithms",
        "topics": ["Algorithm Analysis", "Sorting", "Graph Algorithms", "Dynamic Programming"],
        "lessons": [{"id": "lesson_1", "topic": "Analysis", "title": "Big O", "content": "Analyze complexity.", "duration_minutes": 30, "difficulty": "high"}],
        "quizzes": [{
            "id": "quiz_1",
            "topic": "Algorithms",
            "title": "Algorithm Fundamentals",
            "questions": [
                {"id": "q1", "question": "Best case time complexity of QuickSort?", "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"], "correct_answer": "O(n log n)", "explanation": "QuickSort is O(n log n) best/average case."},
                {"id": "q2", "question": "Key principle of dynamic programming?", "options": ["Divide and conquer", "Storing results to avoid recomputation", "Random pivots", "Sorting first"], "correct_answer": "Storing results to avoid recomputation", "explanation": "DP memoizes subproblem solutions."},
                {"id": "q3", "question": "Dijkstra's algorithm finds?", "options": ["Sorting", "Shortest paths in weighted graphs", "Binary search", "Matrix multiplication"], "correct_answer": "Shortest paths in weighted graphs", "explanation": "Dijkstra finds shortest paths."}
            ],
            "passing_score": 70,
            "difficulty": "very_high"
        }],
        "learning_outcomes": ["Analyze complexity", "Implement algorithms", "Solve optimization problems"]
    },
    "cs210": {
        "title": "Computer Organization",
        "topics": ["Architecture", "Assembly", "Memory", "CPU"],
        "lessons": [{"id": "lesson_1", "topic": "Architecture", "title": "Computer Architecture", "content": "Hardware organization.", "duration_minutes": 30, "difficulty": "intermediate"}],
        "quizzes": [{
            "id": "quiz_1",
            "topic": "Architecture",
            "title": "Architecture Basics",
            "questions": [
                {"id": "q1", "question": "CPU stands for?", "options": ["Central Processing Unit", "Computer Processing Unit", "Central Program Unit", "Core Processing Unit"], "correct_answer": "Central Processing Unit", "explanation": "CPU = Central Processing Unit."},
                {"id": "q2", "question": "What is cache memory?", "options": ["Main memory", "Fast memory close to CPU", "Disk storage", "Virtual memory"], "correct_answer": "Fast memory close to CPU", "explanation": "Cache is fast memory near CPU."},
                {"id": "q3", "question": "ALU purpose?", "options": ["Store data", "Perform arithmetic and logical operations", "Manage I/O", "Control flow"], "correct_answer": "Perform arithmetic and logical operations", "explanation": "ALU does math and logic operations."}
            ],
            "passing_score": 70,
            "difficulty": "intermediate"
        }],
        "learning_outcomes": ["Understand architecture", "Program assembly", "Analyze performance"]
    },
    "stat200": {
        "title": "Probability & Statistics",
        "topics": ["Probability", "Distributions", "Statistical Inference", "Hypothesis Testing"],
        "lessons": [{"id": "lesson_1", "topic": "Probability", "title": "Probability Fundamentals", "content": "Master probability.", "duration_minutes": 30, "difficulty": "intermediate"}],
        "quizzes": [{
            "id": "quiz_1",
            "topic": "Probability",
            "title": "Probability Quiz",
            "questions": [
                {"id": "q1", "question": "Probability of heads on fair coin?", "options": ["0.25", "0.5", "0.75", "1.0"], "correct_answer": "0.5", "explanation": "Fair coin P(heads) = 0.5."},
                {"id": "q2", "question": "Central Limit Theorem states?", "options": ["All normal", "Sample means approach normal as n increases", "Always 0.5", "Mean equals SD"], "correct_answer": "Sample means approach normal as n increases", "explanation": "CLT: sample means become normal."},
                {"id": "q3", "question": "P-value is?", "options": ["Null is true", "Probability of data if null true", "Error probability", "Population mean"], "correct_answer": "Probability of data if null true", "explanation": "P-value measures data likelihood given null."}
            ],
            "passing_score": 70,
            "difficulty": "intermediate"
        }],
        "learning_outcomes": ["Calculate probabilities", "Work with distributions", "Test hypotheses"]
    },
    "cs220": {
        "title": "Operating Systems",
        "topics": ["Processes", "Memory Management", "File Systems", "Synchronization"],
        "lessons": [{"id": "lesson_1", "topic": "Processes", "title": "Process Management", "content": "Process scheduling.", "duration_minutes": 35, "difficulty": "high"}],
        "quizzes": [{
            "id": "quiz_1",
            "topic": "OS",
            "title": "OS Fundamentals",
            "questions": [
                {"id": "q1", "question": "What is a process?", "options": ["Program on disk", "Program in execution", "CPU instruction", "Memory address"], "correct_answer": "Program in execution", "explanation": "Process is executing program."},
                {"id": "q2", "question": "Context switch is?", "options": ["Changing programs", "Saving and restoring CPU state when switching", "Moving to disk", "Updating memory"], "correct_answer": "Saving and restoring CPU state when switching", "explanation": "Context switch saves/restores process state."},
                {"id": "q3", "question": "Semaphores solve?", "options": ["Scheduling", "Synchronization between processes/threads", "Memory allocation", "File I/O"], "correct_answer": "Synchronization between processes/threads", "explanation": "Semaphores control shared resource access."}
            ],
            "passing_score": 70,
            "difficulty": "high"
        }],
        "learning_outcomes": ["Understand OS concepts", "Implement synchronization", "Analyze scheduling"]
    },
    "cs225": {
        "title": "Database Systems",
        "topics": ["Relational Model", "SQL", "Database Design", "Normalization"],
        "lessons": [{"id": "lesson_1", "topic": "SQL", "title": "SQL Fundamentals", "content": "Master SQL queries.", "duration_minutes": 30, "difficulty": "intermediate"}],
        "quizzes": [{
            "id": "quiz_1",
            "topic": "Databases",
            "title": "Database Quiz",
            "questions": [
                {"id": "q1", "question": "SQL stands for?", "options": ["Structured Query Language", "Simple Query Language", "Standard Query Language", "System Query Language"], "correct_answer": "Structured Query Language", "explanation": "SQL = Structured Query Language."},
                {"id": "q2", "question": "Primary key is?", "options": ["First column", "Unique identifier for each row", "Foreign key", "Index"], "correct_answer": "Unique identifier for each row", "explanation": "Primary key uniquely identifies rows."},
                {"id": "q3", "question": "Normalization achieves?", "options": ["Faster queries", "Reducing redundancy and improving integrity", "Larger database", "Simpler queries"], "correct_answer": "Reducing redundancy and improving integrity", "explanation": "Normalization reduces redundancy."}
            ],
            "passing_score": 70,
            "difficulty": "intermediate"
        }],
        "learning_outcomes": ["Write SQL", "Design databases", "Understand transactions"]
    },
    "cs230": {
        "title": "Software Engineering",
        "topics": ["SDLC", "Design Patterns", "Testing", "Version Control"],
        "lessons": [{"id": "lesson_1", "topic": "SDLC", "title": "Development Process", "content": "Software lifecycle.", "duration_minutes": 30, "difficulty": "intermediate"}],
        "quizzes": [{
            "id": "quiz_1",
            "topic": "SE",
            "title": "SE Principles",
            "questions": [
                {"id": "q1", "question": "Version control purpose?", "options": ["Speed up code", "Track changes and collaborate", "Compile programs", "Test software"], "correct_answer": "Track changes and collaborate", "explanation": "Version control tracks code changes."},
                {"id": "q2", "question": "Test-Driven Development is?", "options": ["Testing after", "Writing tests before code", "Testing at end", "Automated deployment"], "correct_answer": "Writing tests before code", "explanation": "TDD writes tests first."},
                {"id": "q3", "question": "Design pattern is?", "options": ["UI design", "Reusable solution to common problem", "Testing framework", "Database schema"], "correct_answer": "Reusable solution to common problem", "explanation": "Design patterns solve recurring problems."}
            ],
            "passing_score": 70,
            "difficulty": "intermediate"
        }],
        "learning_outcomes": ["Apply SDLC", "Use patterns", "Write tests", "Use version control"]
    },
    "acc201": {
        "title": "Financial Accounting",
        "topics": ["Accounting Equation", "Debits and Credits", "Financial Statements", "Adjusting Entries", "Closing Process"],
        "lessons": [
            {"id": "lesson_1", "topic": "Accounting Equation", "title": "Understanding the Accounting Equation", "content": "Learn the fundamental equation: Assets = Liabilities + Owner's Equity", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Debits and Credits", "title": "The Double-Entry System", "content": "Master debits and credits for each account type", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Financial Statements", "title": "Creating Financial Statements", "content": "Learn to prepare income statements, balance sheets, and cash flow statements", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_4", "topic": "Adjusting Entries", "title": "Period-End Adjustments", "content": "Understand accruals, deferrals, and other adjusting entries", "duration_minutes": 30, "difficulty": "advanced"},
            {"id": "lesson_5", "topic": "Closing Process", "title": "The Accounting Cycle", "content": "Complete the accounting cycle with closing entries", "duration_minutes": 25, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Accounting Equation",
                "title": "Accounting Equation Quiz",
                "questions": [
                    {"id": "q1", "question": "What is the accounting equation?", "options": ["Assets = Liabilities + Equity", "Revenue - Expenses = Profit", "Debits = Credits", "Cash In - Cash Out = Balance"], "correct_answer": "Assets = Liabilities + Equity", "explanation": "The fundamental accounting equation states that Assets = Liabilities + Owner's Equity."},
                    {"id": "q2", "question": "If a company has $50,000 in assets and $20,000 in liabilities, what is the owner's equity?", "options": ["$70,000", "$30,000", "$50,000", "$20,000"], "correct_answer": "$30,000", "explanation": "Owner's Equity = Assets - Liabilities = $50,000 - $20,000 = $30,000."},
                    {"id": "q3", "question": "When a company purchases equipment with cash, what happens to the accounting equation?", "options": ["Assets increase", "Assets decrease", "Assets stay the same, one asset increases while another decreases", "Liabilities increase"], "correct_answer": "Assets stay the same, one asset increases while another decreases", "explanation": "Cash (asset) decreases, Equipment (asset) increases by the same amount."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Debits and Credits",
                "title": "Debits and Credits Quiz",
                "questions": [
                    {"id": "q1", "question": "Which accounts increase with a debit?", "options": ["Assets and Expenses", "Liabilities and Revenue", "Equity and Revenue", "Only Assets"], "correct_answer": "Assets and Expenses", "explanation": "Assets and Expenses have debit balances and increase with debits."},
                    {"id": "q2", "question": "When recording a sale on account, what entry is made?", "options": ["Debit Cash, Credit Revenue", "Debit Accounts Receivable, Credit Revenue", "Debit Revenue, Credit Cash", "Debit Accounts Payable, Credit Revenue"], "correct_answer": "Debit Accounts Receivable, Credit Revenue", "explanation": "A sale on account increases Accounts Receivable (asset, debit) and Revenue (credit)."},
                    {"id": "q3", "question": "What is the normal balance of the Revenue account?", "options": ["Debit", "Credit", "Zero", "Either debit or credit"], "correct_answer": "Credit", "explanation": "Revenue accounts have a normal credit balance."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Financial Statements",
                "title": "Financial Statements Quiz",
                "questions": [
                    {"id": "q1", "question": "Which financial statement shows a company's financial position at a specific point in time?", "options": ["Income Statement", "Balance Sheet", "Cash Flow Statement", "Statement of Retained Earnings"], "correct_answer": "Balance Sheet", "explanation": "The Balance Sheet shows the financial position (assets, liabilities, equity) at a specific date."},
                    {"id": "q2", "question": "Net Income is calculated as:", "options": ["Assets - Liabilities", "Revenue - Expenses", "Cash In - Cash Out", "Debits - Credits"], "correct_answer": "Revenue - Expenses", "explanation": "Net Income = Revenue - Expenses for a period."},
                    {"id": "q3", "question": "Which statement shows where cash came from and how it was used?", "options": ["Income Statement", "Balance Sheet", "Cash Flow Statement", "Trial Balance"], "correct_answer": "Cash Flow Statement", "explanation": "The Cash Flow Statement tracks cash inflows and outflows."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand the accounting equation", "Apply debits and credits correctly", "Prepare basic financial statements", "Complete the accounting cycle"]
    },
    "acc202": {
        "title": "Managerial Accounting",
        "topics": ["Cost Behavior", "Cost-Volume-Profit Analysis", "Budgeting", "Variance Analysis", "Capital Budgeting"],
        "lessons": [
            {"id": "lesson_1", "topic": "Cost Behavior", "title": "Understanding Cost Behavior", "content": "Learn about fixed, variable, and mixed costs", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "CVP Analysis", "title": "Break-Even Analysis", "content": "Master cost-volume-profit relationships", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Budgeting", "title": "Master Budgeting", "content": "Create comprehensive operational budgets", "duration_minutes": 35, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Cost Behavior",
                "title": "Cost Behavior Quiz",
                "questions": [
                    {"id": "q1", "question": "What are fixed costs?", "options": ["Costs that stay constant in total regardless of activity level", "Costs that vary with production", "Costs that are always the same per unit", "Costs that change monthly"], "correct_answer": "Costs that stay constant in total regardless of activity level", "explanation": "Fixed costs remain constant in total even when production volume changes."},
                    {"id": "q2", "question": "Variable costs per unit are:", "options": ["Constant", "Increasing", "Decreasing", "Unpredictable"], "correct_answer": "Constant", "explanation": "Variable costs per unit remain constant, while total variable costs change with volume."},
                    {"id": "q3", "question": "Which is an example of a mixed cost?", "options": ["Rent", "Direct materials", "Utilities with base charge plus usage", "Sales commissions"], "correct_answer": "Utilities with base charge plus usage", "explanation": "Mixed costs have both fixed and variable components."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "CVP Analysis",
                "title": "Break-Even Quiz",
                "questions": [
                    {"id": "q1", "question": "Break-even point is where:", "options": ["Profit is maximized", "Total Revenue = Total Costs", "Variable costs equal fixed costs", "Sales are highest"], "correct_answer": "Total Revenue = Total Costs", "explanation": "Break-even occurs when total revenue equals total costs (no profit or loss)."},
                    {"id": "q2", "question": "Contribution margin is:", "options": ["Sales - Variable Costs", "Sales - Fixed Costs", "Sales - All Costs", "Profit margin"], "correct_answer": "Sales - Variable Costs", "explanation": "Contribution margin = Sales - Variable Costs."},
                    {"id": "q3", "question": "If fixed costs are $10,000 and contribution margin per unit is $5, break-even units are:", "options": ["500", "1,000", "2,000", "5,000"], "correct_answer": "2,000", "explanation": "Break-even units = Fixed Costs / Contribution Margin per Unit = $10,000 / $5 = 2,000 units."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Classify costs by behavior", "Calculate break-even point", "Perform CVP analysis", "Create master budgets"]
    },
    "econ102": {
        "title": "Macroeconomics",
        "topics": ["GDP and Economic Growth", "Unemployment and Inflation", "Monetary Policy", "Fiscal Policy", "International Trade"],
        "lessons": [
            {"id": "lesson_1", "topic": "GDP", "title": "Measuring Economic Activity", "content": "Learn how GDP is calculated and what it measures", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Unemployment", "title": "Labor Markets", "content": "Understand types of unemployment and the natural rate", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_3", "topic": "Inflation", "title": "Price Level Changes", "content": "Study causes and effects of inflation", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_4", "topic": "Monetary Policy", "title": "Central Banking", "content": "Explore how central banks influence the economy", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_5", "topic": "International Trade", "title": "Global Economics", "content": "Understand comparative advantage and trade policy", "duration_minutes": 25, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "GDP and Economic Growth",
                "title": "GDP Quiz",
                "questions": [
                    {"id": "q1", "question": "What does GDP measure?", "options": ["Total value of all final goods and services produced in an economy", "Total income of all workers", "Total government spending", "Total exports minus imports"], "correct_answer": "Total value of all final goods and services produced in an economy", "explanation": "GDP measures the total market value of all final goods and services produced within a country."},
                    {"id": "q2", "question": "Which is NOT a component of GDP?", "options": ["Consumption", "Investment", "Intermediate goods", "Government purchases"], "correct_answer": "Intermediate goods", "explanation": "GDP counts only final goods to avoid double-counting. The components are C + I + G + NX."},
                    {"id": "q3", "question": "Real GDP adjusts nominal GDP for:", "options": ["Population", "Inflation", "Unemployment", "Exchange rates"], "correct_answer": "Inflation", "explanation": "Real GDP adjusts nominal GDP for changes in the price level (inflation)."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Unemployment and Inflation",
                "title": "Unemployment & Inflation Quiz",
                "questions": [
                    {"id": "q1", "question": "Frictional unemployment is:", "options": ["Long-term structural unemployment", "Temporary unemployment during job transitions", "Unemployment due to recession", "Unemployment due to automation"], "correct_answer": "Temporary unemployment during job transitions", "explanation": "Frictional unemployment occurs when workers are between jobs."},
                    {"id": "q2", "question": "The Consumer Price Index (CPI) measures:", "options": ["Stock market performance", "Changes in the price level of consumer goods", "Employment rate", "Economic growth"], "correct_answer": "Changes in the price level of consumer goods", "explanation": "CPI tracks the average change in prices paid by consumers for a basket of goods."},
                    {"id": "q3", "question": "What is the Phillips Curve relationship?", "options": ["GDP and inflation", "Unemployment and inflation", "Interest rates and GDP", "Taxes and spending"], "correct_answer": "Unemployment and inflation", "explanation": "The Phillips Curve shows an inverse relationship between unemployment and inflation."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Monetary Policy",
                "title": "Monetary Policy Quiz",
                "questions": [
                    {"id": "q1", "question": "The Federal Reserve's main tool for monetary policy is:", "options": ["Government spending", "Tax rates", "Open market operations", "Trade policy"], "correct_answer": "Open market operations", "explanation": "The Fed primarily uses open market operations (buying/selling bonds) to influence the money supply."},
                    {"id": "q2", "question": "When the Fed wants to stimulate the economy, it:", "options": ["Raises interest rates", "Lowers interest rates", "Increases taxes", "Reduces government spending"], "correct_answer": "Lowers interest rates", "explanation": "Lowering interest rates makes borrowing cheaper, stimulating investment and consumption."},
                    {"id": "q3", "question": "What is quantitative easing?", "options": ["Raising reserve requirements", "Large-scale asset purchases to inject money", "Increasing interest rates", "Reducing government debt"], "correct_answer": "Large-scale asset purchases to inject money", "explanation": "Quantitative easing involves central banks buying assets to increase money supply."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand macroeconomic indicators", "Analyze monetary policy", "Evaluate fiscal policy", "Understand international trade"]
    },
    "mkt201": {
        "title": "Marketing Fundamentals",
        "topics": ["Marketing Mix (4Ps)", "Market Segmentation", "Consumer Behavior", "Marketing Research", "Brand Management"],
        "lessons": [
            {"id": "lesson_1", "topic": "Marketing Mix", "title": "The 4Ps of Marketing", "content": "Learn Product, Price, Place, and Promotion strategies", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Segmentation", "title": "Market Segmentation and Targeting", "content": "Identify and target specific customer segments", "duration_minutes": 30, "difficulty": "beginner"},
            {"id": "lesson_3", "topic": "Consumer Behavior", "title": "Understanding Consumer Decision-Making", "content": "Study how consumers make purchase decisions", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_4", "topic": "Research", "title": "Marketing Research Methods", "content": "Learn qualitative and quantitative research techniques", "duration_minutes": 25, "difficulty": "intermediate"},
            {"id": "lesson_5", "topic": "Branding", "title": "Building Strong Brands", "content": "Understand brand equity and positioning", "duration_minutes": 30, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Marketing Mix",
                "title": "4Ps Quiz",
                "questions": [
                    {"id": "q1", "question": "The four Ps of marketing are:", "options": ["Product, Price, Place, Promotion", "Plan, People, Process, Performance", "Positioning, Pricing, Publicity, Profit", "Product, People, Place, Profit"], "correct_answer": "Product, Price, Place, Promotion", "explanation": "The traditional marketing mix consists of Product, Price, Place (distribution), and Promotion."},
                    {"id": "q2", "question": "Which P relates to distribution channels?", "options": ["Product", "Price", "Place", "Promotion"], "correct_answer": "Place", "explanation": "Place refers to distribution channels and how products reach customers."},
                    {"id": "q3", "question": "Premium pricing is appropriate when:", "options": ["Competing on cost", "Product has unique value or prestige", "Market is saturated", "Customers are price-sensitive"], "correct_answer": "Product has unique value or prestige", "explanation": "Premium pricing works when products offer unique value, quality, or brand prestige."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Market Segmentation",
                "title": "Segmentation Quiz",
                "questions": [
                    {"id": "q1", "question": "Market segmentation is:", "options": ["Selling to everyone", "Dividing the market into distinct groups", "Setting prices", "Advertising strategy"], "correct_answer": "Dividing the market into distinct groups", "explanation": "Market segmentation divides a broad market into distinct subgroups with similar needs."},
                    {"id": "q2", "question": "Demographic segmentation uses:", "options": ["Age, gender, income", "Lifestyle and values", "Usage rate", "Geographic location"], "correct_answer": "Age, gender, income", "explanation": "Demographic segmentation divides markets by observable characteristics like age, gender, and income."},
                    {"id": "q3", "question": "What is a target market?", "options": ["Everyone who might buy", "Specific segment(s) a company focuses on", "The entire industry", "Competitors' customers"], "correct_answer": "Specific segment(s) a company focuses on", "explanation": "A target market is the specific segment(s) a company chooses to serve."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Consumer Behavior",
                "title": "Consumer Behavior Quiz",
                "questions": [
                    {"id": "q1", "question": "The stages of the consumer decision process are:", "options": ["Awareness, Interest, Desire, Action", "Need recognition, Search, Evaluation, Purchase, Post-purchase", "See, Think, Do", "Attention, Interest, Purchase"], "correct_answer": "Need recognition, Search, Evaluation, Purchase, Post-purchase", "explanation": "The consumer decision process includes: need recognition, information search, evaluation of alternatives, purchase decision, and post-purchase behavior."},
                    {"id": "q2", "question": "Maslow's hierarchy suggests people first satisfy:", "options": ["Self-actualization needs", "Esteem needs", "Physiological needs", "Social needs"], "correct_answer": "Physiological needs", "explanation": "Maslow's hierarchy shows physiological needs (food, water, shelter) must be met first."},
                    {"id": "q3", "question": "Cognitive dissonance occurs:", "options": ["Before purchase", "During purchase", "After purchase when doubts arise", "During information search"], "correct_answer": "After purchase when doubts arise", "explanation": "Cognitive dissonance is post-purchase doubt about whether the right decision was made."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Apply the marketing mix", "Segment and target markets", "Understand consumer behavior", "Conduct marketing research"]
    },
    "fin301": {
        "title": "Corporate Finance",
        "topics": ["Time Value of Money", "Capital Budgeting", "Risk and Return", "Cost of Capital", "Capital Structure"],
        "lessons": [
            {"id": "lesson_1", "topic": "Time Value of Money", "title": "Present and Future Value", "content": "Learn to calculate PV and FV of cash flows", "duration_minutes": 30, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Capital Budgeting", "title": "Investment Decision Making", "content": "Master NPV, IRR, and payback methods", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Risk and Return", "title": "Investment Risk Analysis", "content": "Understand the risk-return tradeoff", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_4", "topic": "Cost of Capital", "title": "WACC Calculation", "content": "Calculate weighted average cost of capital", "duration_minutes": 30, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Time Value of Money",
                "title": "TVM Quiz",
                "questions": [
                    {"id": "q1", "question": "The time value of money principle states:", "options": ["Money today is worth more than money in the future", "Money loses value over time only due to inflation", "All money has equal value", "Future money is worth more"], "correct_answer": "Money today is worth more than money in the future", "explanation": "Due to opportunity cost and inflation, money available today is worth more than the same amount in the future."},
                    {"id": "q2", "question": "If you invest $1,000 at 10% annual interest, what will it be worth in 1 year?", "options": ["$1,010", "$1,100", "$1,200", "$1,000"], "correct_answer": "$1,100", "explanation": "FV = PV × (1 + r) = $1,000 × 1.10 = $1,100."},
                    {"id": "q3", "question": "Present value of $1,100 one year from now at 10% discount rate is:", "options": ["$1,100", "$1,000", "$990", "$1,210"], "correct_answer": "$1,000", "explanation": "PV = FV / (1 + r) = $1,100 / 1.10 = $1,000."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Capital Budgeting",
                "title": "NPV and IRR Quiz",
                "questions": [
                    {"id": "q1", "question": "Net Present Value (NPV) is:", "options": ["Sum of all future cash flows", "Present value of future cash flows minus initial investment", "Total profit", "Internal rate of return"], "correct_answer": "Present value of future cash flows minus initial investment", "explanation": "NPV = PV of future cash flows - Initial investment. Positive NPV projects add value."},
                    {"id": "q2", "question": "A project should be accepted if:", "options": ["IRR < Cost of Capital", "NPV < 0", "NPV > 0", "Payback period is long"], "correct_answer": "NPV > 0", "explanation": "Projects with positive NPV add value and should be accepted."},
                    {"id": "q3", "question": "Internal Rate of Return (IRR) is the discount rate where:", "options": ["NPV is maximized", "NPV equals zero", "Cash flows are highest", "Cost of capital is minimized"], "correct_answer": "NPV equals zero", "explanation": "IRR is the discount rate that makes NPV = 0."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Risk and Return",
                "title": "Risk & Return Quiz",
                "questions": [
                    {"id": "q1", "question": "The relationship between risk and return is:", "options": ["Inverse", "No relationship", "Direct - higher risk requires higher expected return", "Random"], "correct_answer": "Direct - higher risk requires higher expected return", "explanation": "Investors require higher expected returns to compensate for taking higher risks."},
                    {"id": "q2", "question": "Systematic risk is:", "options": ["Risk affecting only one company", "Market-wide risk that cannot be diversified away", "Risk from poor management", "Company-specific risk"], "correct_answer": "Market-wide risk that cannot be diversified away", "explanation": "Systematic risk affects the entire market and cannot be eliminated through diversification."},
                    {"id": "q3", "question": "Diversification reduces:", "options": ["Systematic risk", "Unsystematic (company-specific) risk", "All risk", "Market risk"], "correct_answer": "Unsystematic (company-specific) risk", "explanation": "Diversification reduces unsystematic risk by spreading investments across different assets."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Apply time value of money concepts", "Evaluate capital budgeting projects", "Analyze risk and return", "Calculate cost of capital"]
    },
    "mgt301": {
        "title": "Organizational Behavior and Management",
        "topics": ["Leadership Theories", "Motivation", "Team Dynamics", "Organizational Culture", "Change Management"],
        "lessons": [
            {"id": "lesson_1", "topic": "Leadership", "title": "Leadership Styles and Theories", "content": "Explore different leadership approaches", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Motivation", "title": "Motivating Employees", "content": "Study motivation theories and applications", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Teams", "title": "Building Effective Teams", "content": "Learn team development and dynamics", "duration_minutes": 25, "difficulty": "intermediate"},
            {"id": "lesson_4", "topic": "Culture", "title": "Organizational Culture", "content": "Understand and shape company culture", "duration_minutes": 30, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Leadership",
                "title": "Leadership Quiz",
                "questions": [
                    {"id": "q1", "question": "Transformational leadership focuses on:", "options": ["Transactions and rewards", "Inspiring and developing followers", "Maintaining status quo", "Strict rules"], "correct_answer": "Inspiring and developing followers", "explanation": "Transformational leaders inspire, motivate, and develop their followers to achieve extraordinary outcomes."},
                    {"id": "q2", "question": "Situational leadership theory suggests leaders should:", "options": ["Use one consistent style", "Adapt style based on follower readiness", "Always be democratic", "Focus only on tasks"], "correct_answer": "Adapt style based on follower readiness", "explanation": "Situational leadership requires adapting leadership style based on followers' competence and commitment."},
                    {"id": "q3", "question": "Emotional intelligence in leadership involves:", "options": ["IQ and technical skills", "Understanding and managing emotions", "Financial acumen", "Industry knowledge"], "correct_answer": "Understanding and managing emotions", "explanation": "Emotional intelligence includes self-awareness, self-regulation, empathy, and social skills."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Motivation",
                "title": "Motivation Quiz",
                "questions": [
                    {"id": "q1", "question": "Maslow's hierarchy of needs includes (from bottom to top):", "options": ["Physiological, Safety, Social, Esteem, Self-actualization", "Money, Recognition, Power, Achievement", "Hygiene, Motivators", "Existence, Relatedness, Growth"], "correct_answer": "Physiological, Safety, Social, Esteem, Self-actualization", "explanation": "Maslow's hierarchy progresses from basic physiological needs to self-actualization."},
                    {"id": "q2", "question": "Herzberg's two-factor theory identifies:", "options": ["Motivators and hygiene factors", "Intrinsic and extrinsic rewards", "Theory X and Theory Y", "Positive and negative reinforcement"], "correct_answer": "Motivators and hygiene factors", "explanation": "Herzberg distinguished between hygiene factors (prevent dissatisfaction) and motivators (create satisfaction)."},
                    {"id": "q3", "question": "Intrinsic motivation comes from:", "options": ["External rewards like money", "Internal satisfaction from the work itself", "Fear of punishment", "Competition with others"], "correct_answer": "Internal satisfaction from the work itself", "explanation": "Intrinsic motivation comes from internal satisfaction, enjoyment, and meaning in the work itself."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Team Dynamics",
                "title": "Teams Quiz",
                "questions": [
                    {"id": "q1", "question": "Tuckman's stages of team development are:", "options": ["Forming, Storming, Norming, Performing, Adjourning", "Plan, Do, Check, Act", "Start, Build, Optimize, Close", "Create, Develop, Execute, Finish"], "correct_answer": "Forming, Storming, Norming, Performing, Adjourning", "explanation": "Tuckman identified five stages: Forming, Storming, Norming, Performing, and Adjourning."},
                    {"id": "q2", "question": "Group cohesion refers to:", "options": ["Team size", "Degree of attraction members feel toward the team", "Leadership style", "Team productivity"], "correct_answer": "Degree of attraction members feel toward the team", "explanation": "Cohesion is the strength of bonds and commitment among team members."},
                    {"id": "q3", "question": "Social loafing occurs when:", "options": ["Teams work too hard", "Individual effort decreases in group settings", "Leaders are absent", "Teams are too small"], "correct_answer": "Individual effort decreases in group settings", "explanation": "Social loafing is the tendency for individuals to put in less effort when working in a group."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Apply leadership theories", "Motivate team members", "Build effective teams", "Manage organizational change"]
    },
    "ops301": {
        "title": "Operations Management",
        "topics": ["Process Design", "Quality Management", "Supply Chain Management", "Inventory Control", "Lean Operations"],
        "lessons": [
            {"id": "lesson_1", "topic": "Process Design", "title": "Designing Operations Processes", "content": "Learn how to design efficient operational processes", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Quality", "title": "Total Quality Management", "content": "Implement quality management systems", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Supply Chain", "title": "Supply Chain Strategy", "content": "Optimize supply chain operations", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Process Design",
                "title": "Process Design Quiz",
                "questions": [
                    {"id": "q1", "question": "Process capacity is:", "options": ["Maximum output per time period", "Minimum output required", "Average production rate", "Total inventory"], "correct_answer": "Maximum output per time period", "explanation": "Capacity is the maximum rate of output an operation can achieve."},
                    {"id": "q2", "question": "The bottleneck in a process is:", "options": ["The fastest step", "The step with lowest capacity", "First step", "Last step"], "correct_answer": "The step with lowest capacity", "explanation": "The bottleneck is the step with the lowest capacity that limits overall process throughput."},
                    {"id": "q3", "question": "Process utilization is:", "options": ["Actual output / Maximum capacity", "Cost / Revenue", "Inventory / Sales", "Time / Distance"], "correct_answer": "Actual output / Maximum capacity", "explanation": "Utilization = Actual Output / Maximum Capacity."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Quality Management",
                "title": "Quality Quiz",
                "questions": [
                    {"id": "q1", "question": "Six Sigma aims for:", "options": ["Zero defects", "3.4 defects per million opportunities", "50% reduction in defects", "100% inspection"], "correct_answer": "3.4 defects per million opportunities", "explanation": "Six Sigma targets 3.4 defects per million opportunities, nearly zero defects."},
                    {"id": "q2", "question": "The PDCA cycle stands for:", "options": ["Plan, Do, Check, Act", "Prepare, Develop, Control, Assess", "Process, Design, Create, Analyze", "Plan, Design, Complete, Audit"], "correct_answer": "Plan, Do, Check, Act", "explanation": "PDCA (Plan-Do-Check-Act) is a continuous improvement cycle."},
                    {"id": "q3", "question": "ISO 9000 is a standard for:", "options": ["Environmental management", "Quality management systems", "Safety management", "Financial reporting"], "correct_answer": "Quality management systems", "explanation": "ISO 9000 provides standards for quality management systems."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Supply Chain",
                "title": "Supply Chain Quiz",
                "questions": [
                    {"id": "q1", "question": "Just-In-Time (JIT) inventory aims to:", "options": ["Maximize inventory levels", "Receive materials exactly when needed", "Store materials for long periods", "Buy in bulk"], "correct_answer": "Receive materials exactly when needed", "explanation": "JIT minimizes inventory by receiving materials exactly when needed for production."},
                    {"id": "q2", "question": "The bullwhip effect in supply chains refers to:", "options": ["Increasing demand variability upstream", "Stable demand", "Decreasing costs", "Improved quality"], "correct_answer": "Increasing demand variability upstream", "explanation": "The bullwhip effect describes how small demand variations amplify upstream in the supply chain."},
                    {"id": "q3", "question": "Economic Order Quantity (EOQ) minimizes:", "options": ["Revenue", "Total inventory costs (holding + ordering)", "Production time", "Quality defects"], "correct_answer": "Total inventory costs (holding + ordering)", "explanation": "EOQ is the order size that minimizes total inventory costs."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Design efficient processes", "Implement quality systems", "Manage supply chains", "Control inventory effectively"]
    },
    "law201": {
        "title": "Business Law",
        "topics": ["Contract Law", "Business Torts", "Employment Law", "Intellectual Property", "Business Ethics"],
        "lessons": [
            {"id": "lesson_1", "topic": "Contracts", "title": "Contract Formation", "content": "Learn essential elements of valid contracts", "duration_minutes": 30, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Torts", "title": "Business Torts and Liability", "content": "Understand tort liability in business", "duration_minutes": 25, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Employment", "title": "Employment Law Basics", "content": "Study employment relationships and regulations", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Contract Law",
                "title": "Contracts Quiz",
                "questions": [
                    {"id": "q1", "question": "The essential elements of a contract are:", "options": ["Offer, Acceptance, Consideration", "Offer and Price", "Handshake and Trust", "Written agreement only"], "correct_answer": "Offer, Acceptance, Consideration", "explanation": "A valid contract requires offer, acceptance, and consideration (something of value exchanged)."},
                    {"id": "q2", "question": "Consideration in contract law means:", "options": ["Being thoughtful", "Something of value exchanged by parties", "Time to think about the deal", "Legal advice"], "correct_answer": "Something of value exchanged by parties", "explanation": "Consideration is something of legal value given by each party (money, services, goods, promises)."},
                    {"id": "q3", "question": "A breach of contract occurs when:", "options": ["Contract terms are unclear", "One party fails to perform obligations", "Both parties agree to end contract", "Contract is verbal"], "correct_answer": "One party fails to perform obligations", "explanation": "Breach occurs when a party fails to fulfill contractual obligations without legal excuse."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Business Torts",
                "title": "Torts Quiz",
                "questions": [
                    {"id": "q1", "question": "A tort is:", "options": ["A type of contract", "A civil wrong causing harm or loss", "A criminal act", "A business agreement"], "correct_answer": "A civil wrong causing harm or loss", "explanation": "A tort is a civil (not criminal) wrong that causes someone to suffer harm or loss."},
                    {"id": "q2", "question": "Negligence requires proof of:", "options": ["Intent to harm", "Duty, Breach, Causation, Damages", "Criminal behavior", "Contract violation"], "correct_answer": "Duty, Breach, Causation, Damages", "explanation": "Negligence requires: duty of care, breach of duty, causation, and damages."},
                    {"id": "q3", "question": "Product liability can arise from:", "options": ["Defective products causing harm", "Poor customer service", "High prices", "Slow delivery"], "correct_answer": "Defective products causing harm", "explanation": "Product liability holds manufacturers/sellers responsible for defective products that cause injury."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand contract law", "Identify business torts", "Apply employment law", "Protect intellectual property"]
    },
    "mis301": {
        "title": "Management Information Systems",
        "topics": ["Information Systems in Business", "Database Management", "Systems Development", "E-Commerce", "IT Security"],
        "lessons": [
            {"id": "lesson_1", "topic": "IS Basics", "title": "Information Systems Overview", "content": "Understand how IS supports business operations", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Databases", "title": "Database Systems", "content": "Learn database design and management", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Development", "title": "Systems Development Lifecycle", "content": "Study SDLC phases and methodologies", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Information Systems",
                "title": "IS Fundamentals Quiz",
                "questions": [
                    {"id": "q1", "question": "Management Information Systems support:", "options": ["Only technical tasks", "Strategic, tactical, and operational decisions", "Only executive decisions", "Only data storage"], "correct_answer": "Strategic, tactical, and operational decisions", "explanation": "MIS provide information to support decision-making at all organizational levels."},
                    {"id": "q2", "question": "Transaction Processing Systems (TPS) primarily:", "options": ["Support executive decisions", "Process routine business transactions", "Analyze trends", "Create reports"], "correct_answer": "Process routine business transactions", "explanation": "TPS handle daily routine transactions like sales, purchases, and payments."},
                    {"id": "q3", "question": "Business Intelligence systems help organizations:", "options": ["Process transactions faster", "Analyze data for insights and decision-making", "Store more data", "Reduce costs only"], "correct_answer": "Analyze data for insights and decision-making", "explanation": "BI systems analyze data to provide insights that support strategic decisions."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Database Management",
                "title": "Database Quiz",
                "questions": [
                    {"id": "q1", "question": "Normalization in databases aims to:", "options": ["Increase data redundancy", "Eliminate data redundancy and anomalies", "Speed up queries", "Add more tables"], "correct_answer": "Eliminate data redundancy and anomalies", "explanation": "Normalization organizes data to reduce redundancy and prevent update anomalies."},
                    {"id": "q2", "question": "A primary key is:", "options": ["Most important field", "Unique identifier for each record", "First field in table", "Largest field"], "correct_answer": "Unique identifier for each record", "explanation": "A primary key uniquely identifies each record in a database table."},
                    {"id": "q3", "question": "SQL is used for:", "options": ["Programming applications", "Querying and managing relational databases", "Creating websites", "Network configuration"], "correct_answer": "Querying and managing relational databases", "explanation": "SQL (Structured Query Language) is the standard language for relational database management."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand role of IS in business", "Design databases", "Develop information systems", "Implement IT security"]
    },
    "math110": {
        "title": "Business Mathematics",
        "topics": ["Linear Equations", "Financial Mathematics", "Systems of Equations", "Functions and Graphs", "Applied Optimization"],
        "lessons": [
            {"id": "lesson_1", "topic": "Linear Equations", "title": "Solving Linear Equations", "content": "Master linear equations for business applications", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Financial Math", "title": "Interest and Annuities", "content": "Calculate interest, loans, and annuities", "duration_minutes": 30, "difficulty": "beginner"},
            {"id": "lesson_3", "topic": "Systems", "title": "Systems of Equations", "content": "Solve systems for break-even analysis", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Linear Equations",
                "title": "Linear Equations Quiz",
                "questions": [
                    {"id": "q1", "question": "Solve for x: 3x + 5 = 20", "options": ["x = 5", "x = 15", "x = 25", "x = 7"], "correct_answer": "x = 5", "explanation": "3x = 15, so x = 5."},
                    {"id": "q2", "question": "The slope of the line y = 2x + 3 is:", "options": ["2", "3", "2x", "5"], "correct_answer": "2", "explanation": "In slope-intercept form y = mx + b, m is the slope. Here m = 2."},
                    {"id": "q3", "question": "If total cost C = 1000 + 5x where x is units, the fixed cost is:", "options": ["5", "1000", "1005", "5x"], "correct_answer": "1000", "explanation": "Fixed cost is the constant term: $1,000."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Financial Mathematics",
                "title": "Financial Math Quiz",
                "questions": [
                    {"id": "q1", "question": "Simple interest on $1,000 at 5% for 2 years is:", "options": ["$50", "$100", "$150", "$1,100"], "correct_answer": "$100", "explanation": "Simple Interest = Principal × Rate × Time = $1,000 × 0.05 × 2 = $100."},
                    {"id": "q2", "question": "Compound interest differs from simple interest because:", "options": ["Interest rate is higher", "Interest earns interest", "Principal is larger", "Time period is longer"], "correct_answer": "Interest earns interest", "explanation": "Compound interest calculates interest on both principal and accumulated interest."},
                    {"id": "q3", "question": "An annuity is:", "options": ["One-time payment", "Series of equal periodic payments", "Variable payments", "Loan principal"], "correct_answer": "Series of equal periodic payments", "explanation": "An annuity is a series of equal payments made at regular intervals."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_3",
                "topic": "Break-Even Analysis",
                "title": "Break-Even Quiz",
                "questions": [
                    {"id": "q1", "question": "Break-even point occurs when:", "options": ["Revenue = Total Costs", "Profit is maximized", "Variable costs = 0", "Fixed costs = 0"], "correct_answer": "Revenue = Total Costs", "explanation": "Break-even is where Total Revenue = Total Costs (profit = 0)."},
                    {"id": "q2", "question": "If fixed costs are $5,000, price per unit is $20, and variable cost per unit is $12, break-even units are:", "options": ["250", "417", "625", "1,000"], "correct_answer": "625", "explanation": "Break-even = Fixed Costs / (Price - Variable Cost) = $5,000 / ($20 - $12) = 625 units."},
                    {"id": "q3", "question": "Contribution margin per unit equals:", "options": ["Price - Variable Cost per unit", "Price - Fixed Cost per unit", "Revenue - Total Costs", "Total Revenue / Units"], "correct_answer": "Price - Variable Cost per unit", "explanation": "Contribution margin per unit = Selling Price - Variable Cost per unit."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Solve business math problems", "Apply financial mathematics", "Use break-even analysis", "Optimize business decisions"]
    },
    "chem101": {
        "title": "General Chemistry I",
        "topics": ["Atomic Structure", "Chemical Bonding", "Stoichiometry", "States of Matter", "Solutions"],
        "lessons": [
            {"id": "lesson_1", "topic": "Atomic Structure", "title": "Atoms and the Periodic Table", "content": "Understand atomic structure, isotopes, and periodic trends.", "duration_minutes": 30, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Chemical Bonding", "title": "Ionic and Covalent Bonds", "content": "Learn how atoms bond and how to predict molecular shape.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Stoichiometry", "title": "Mole Calculations", "content": "Practice balancing equations and calculating reactants and products.", "duration_minutes": 35, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Atomic Structure",
                "title": "Atomic Structure Quiz",
                "questions": [
                    {"id": "q1", "question": "The atomic number represents:", "options": ["Number of protons", "Number of neutrons", "Mass number", "Number of electrons in the nucleus"], "correct_answer": "Number of protons", "explanation": "Atomic number equals the number of protons in the nucleus."},
                    {"id": "q2", "question": "Isotopes of an element differ in:", "options": ["Number of protons", "Number of neutrons", "Atomic number", "Chemical properties"], "correct_answer": "Number of neutrons", "explanation": "Isotopes have the same protons but different neutrons."},
                    {"id": "q3", "question": "An electron occupies a region of space called:", "options": ["Orbit", "Shell", "Orbital", "Nucleus"], "correct_answer": "Orbital", "explanation": "An orbital is the probability region where an electron is likely found."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Chemical Bonding",
                "title": "Bonding Quiz",
                "questions": [
                    {"id": "q1", "question": "Ionic bonds form when:", "options": ["Electrons are shared equally", "Electrons are transferred", "Protons are shared", "Neutrons are transferred"], "correct_answer": "Electrons are transferred", "explanation": "Ionic bonds form from electron transfer between metals and nonmetals."},
                    {"id": "q2", "question": "A covalent bond involves:", "options": ["Electron transfer", "Electron sharing", "Proton sharing", "Ionic attraction"], "correct_answer": "Electron sharing", "explanation": "Covalent bonds result from shared electron pairs."},
                    {"id": "q3", "question": "VSEPR theory predicts:", "options": ["Atomic mass", "Molecular shape", "Bond energy", "Reaction rate"], "correct_answer": "Molecular shape", "explanation": "VSEPR predicts geometry based on electron pair repulsion."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Stoichiometry",
                "title": "Stoichiometry Quiz",
                "questions": [
                    {"id": "q1", "question": "A balanced chemical equation obeys:", "options": ["Conservation of mass", "Conservation of energy only", "Conservation of volume", "Conservation of charge only"], "correct_answer": "Conservation of mass", "explanation": "Balanced equations conserve atoms (mass)."},
                    {"id": "q2", "question": "The mole is defined as:", "options": ["6.022×10^23 particles", "1 gram of any substance", "1 liter of gas", "Atomic number"], "correct_answer": "6.022×10^23 particles", "explanation": "One mole equals Avogadro’s number of particles."},
                    {"id": "q3", "question": "Limiting reagent is:", "options": ["Reagent in excess", "Reagent that runs out first", "Catalyst", "Product"], "correct_answer": "Reagent that runs out first", "explanation": "The limiting reagent determines the maximum product formed."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Explain atomic structure", "Predict bonding and shapes", "Apply stoichiometry", "Interpret chemical equations"]
    },
    "chem102": {
        "title": "General Chemistry II",
        "topics": ["Thermochemistry", "Chemical Kinetics", "Chemical Equilibrium", "Acids and Bases", "Electrochemistry"],
        "lessons": [
            {"id": "lesson_1", "topic": "Thermochemistry", "title": "Energy in Reactions", "content": "Study enthalpy, heat flow, and calorimetry.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Kinetics", "title": "Reaction Rates", "content": "Understand rate laws, mechanisms, and catalysts.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Equilibrium", "title": "Chemical Equilibrium", "content": "Learn equilibrium constants and Le Châtelier’s principle.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Thermochemistry",
                "title": "Thermochemistry Quiz",
                "questions": [
                    {"id": "q1", "question": "An exothermic reaction:", "options": ["Absorbs heat", "Releases heat", "Has ΔH > 0", "Always slows down"], "correct_answer": "Releases heat", "explanation": "Exothermic reactions release heat and have ΔH < 0."},
                    {"id": "q2", "question": "Heat at constant pressure is measured by:", "options": ["ΔH", "ΔG", "ΔS", "ΔU"], "correct_answer": "ΔH", "explanation": "Enthalpy change (ΔH) equals heat at constant pressure."},
                    {"id": "q3", "question": "A calorimeter measures:", "options": ["Mass", "Heat transfer", "Volume", "Concentration"], "correct_answer": "Heat transfer", "explanation": "Calorimeters measure heat flow in reactions."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_2",
                "topic": "Chemical Kinetics",
                "title": "Kinetics Quiz",
                "questions": [
                    {"id": "q1", "question": "Reaction rate generally increases with:", "options": ["Lower temperature", "Lower concentration", "Higher temperature", "Larger particle size"], "correct_answer": "Higher temperature", "explanation": "Higher temperature increases kinetic energy and collision frequency."},
                    {"id": "q2", "question": "A catalyst:", "options": ["Increases activation energy", "Decreases activation energy", "Is consumed", "Changes ΔH"], "correct_answer": "Decreases activation energy", "explanation": "Catalysts lower activation energy and speed up reactions without being consumed."},
                    {"id": "q3", "question": "Rate law for a reaction is determined by:", "options": ["Overall stoichiometry", "Experimental data", "Balanced equation", "Equilibrium constant"], "correct_answer": "Experimental data", "explanation": "Rate laws are determined experimentally."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Chemical Equilibrium",
                "title": "Equilibrium Quiz",
                "questions": [
                    {"id": "q1", "question": "At equilibrium:", "options": ["Forward and reverse rates are equal", "Reactants equal products", "Reaction stops", "All reactants are consumed"], "correct_answer": "Forward and reverse rates are equal", "explanation": "Equilibrium is dynamic with equal forward and reverse rates."},
                    {"id": "q2", "question": "Le Châtelier’s principle predicts:", "options": ["Equilibrium shifts to oppose a change", "Equilibrium constant changes with concentration", "Reactions stop", "Temperature has no effect"], "correct_answer": "Equilibrium shifts to oppose a change", "explanation": "The system shifts to reduce the applied stress."},
                    {"id": "q3", "question": "For a reaction aA + bB ⇌ cC + dD, the equilibrium constant expression is:", "options": ["[C]^c[D]^d/[A]^a[B]^b", "[A]^a[B]^b/[C]^c[D]^d", "[A][B][C][D]", "a+b=c+d"], "correct_answer": "[C]^c[D]^d/[A]^a[B]^b", "explanation": "Products over reactants, each raised to their coefficients."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Analyze thermochemical processes", "Apply rate laws", "Predict equilibrium shifts", "Solve equilibrium problems"]
    },
    "phys141": {
        "title": "Physics I: Mechanics",
        "topics": ["Kinematics", "Newton's Laws", "Work and Energy", "Momentum", "Rotational Motion"],
        "lessons": [
            {"id": "lesson_1", "topic": "Kinematics", "title": "Motion in One Dimension", "content": "Describe motion using displacement, velocity, and acceleration.", "duration_minutes": 30, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Newton's Laws", "title": "Forces and Motion", "content": "Apply Newton’s laws to analyze forces.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Energy", "title": "Work and Energy", "content": "Use energy methods to solve mechanics problems.", "duration_minutes": 35, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Kinematics",
                "title": "Kinematics Quiz",
                "questions": [
                    {"id": "q1", "question": "Velocity is:", "options": ["Rate of change of position", "Rate of change of acceleration", "Distance only", "Mass times acceleration"], "correct_answer": "Rate of change of position", "explanation": "Velocity is the time derivative of position."},
                    {"id": "q2", "question": "Acceleration is:", "options": ["Change in position", "Change in velocity per unit time", "Force per unit mass", "Energy per unit time"], "correct_answer": "Change in velocity per unit time", "explanation": "Acceleration is the rate of change of velocity."},
                    {"id": "q3", "question": "For constant acceleration, displacement is:", "options": ["s = ut + 1/2 at^2", "s = at", "s = vt", "s = u/t"], "correct_answer": "s = ut + 1/2 at^2", "explanation": "Kinematic equation for constant acceleration: s = ut + 1/2 at^2."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Newton's Laws",
                "title": "Newton’s Laws Quiz",
                "questions": [
                    {"id": "q1", "question": "Newton’s second law states:", "options": ["F = ma", "Action = reaction", "Inertia is constant", "Energy is conserved"], "correct_answer": "F = ma", "explanation": "Net force equals mass times acceleration."},
                    {"id": "q2", "question": "A net force of 10 N on a 2 kg object produces acceleration of:", "options": ["5 m/s^2", "10 m/s^2", "20 m/s^2", "2 m/s^2"], "correct_answer": "5 m/s^2", "explanation": "a = F/m = 10/2 = 5 m/s^2."},
                    {"id": "q3", "question": "Newton’s third law pairs are:", "options": ["Equal and opposite forces on different objects", "Equal forces on same object", "Unrelated forces", "Balanced forces"], "correct_answer": "Equal and opposite forces on different objects", "explanation": "Third law: every action has equal and opposite reaction on another object."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Work and Energy",
                "title": "Energy Quiz",
                "questions": [
                    {"id": "q1", "question": "Work done by a constant force is:", "options": ["W = Fd cosθ", "W = Fd", "W = F/d", "W = mgh"], "correct_answer": "W = Fd cosθ", "explanation": "Work is the dot product of force and displacement."},
                    {"id": "q2", "question": "Kinetic energy is:", "options": ["1/2 mv^2", "mgh", "ma", "p/v"], "correct_answer": "1/2 mv^2", "explanation": "Kinetic energy depends on mass and velocity: KE = 1/2 mv^2."},
                    {"id": "q3", "question": "The work-energy theorem states:", "options": ["Net work equals change in kinetic energy", "Energy is always conserved", "Momentum equals impulse", "Power equals force"], "correct_answer": "Net work equals change in kinetic energy", "explanation": "Net work done on an object equals its change in kinetic energy."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Analyze motion with kinematics", "Apply Newton’s laws", "Use energy methods", "Solve mechanics problems"]
    },
    "cs301": {
        "title": "Computer Networks",
        "topics": ["Network Models", "IP Addressing", "Routing and Switching", "Transport Protocols", "Application Protocols"],
        "lessons": [
            {"id": "lesson_1", "topic": "Network Models", "title": "OSI and TCP/IP Models", "content": "Compare the OSI and TCP/IP layers and their responsibilities.", "duration_minutes": 30, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "IP Addressing", "title": "IPv4 Addressing and Subnets", "content": "Learn IP addressing, subnet masks, and CIDR notation.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Transport", "title": "TCP and UDP", "content": "Understand reliable vs. unreliable transport and common ports.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Network Models",
                "title": "Network Models Quiz",
                "questions": [
                    {"id": "q1", "question": "Which OSI layer is responsible for end-to-end communication?", "options": ["Network", "Transport", "Data Link", "Physical"], "correct_answer": "Transport", "explanation": "The Transport layer provides end-to-end delivery and reliability."},
                    {"id": "q2", "question": "In the TCP/IP model, IP operates at the:", "options": ["Application layer", "Transport layer", "Internet layer", "Link layer"], "correct_answer": "Internet layer", "explanation": "IP is an Internet layer protocol in the TCP/IP model."},
                    {"id": "q3", "question": "Which protocol is used for reliable, connection-oriented transport?", "options": ["UDP", "TCP", "IP", "ICMP"], "correct_answer": "TCP", "explanation": "TCP provides reliable, ordered, connection-oriented delivery."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "IP Addressing",
                "title": "IP Addressing Quiz",
                "questions": [
                    {"id": "q1", "question": "A /24 subnet mask corresponds to:", "options": ["255.255.255.0", "255.255.0.0", "255.0.0.0", "255.255.255.255"], "correct_answer": "255.255.255.0", "explanation": "A /24 mask has 24 network bits, which is 255.255.255.0."},
                    {"id": "q2", "question": "How many usable host addresses are in a /24 network?", "options": ["256", "254", "128", "255"], "correct_answer": "254", "explanation": "A /24 has 256 total addresses; 2 are reserved (network and broadcast)."},
                    {"id": "q3", "question": "Which IP range is private (RFC 1918)?", "options": ["10.0.0.0/8", "8.8.8.0/24", "1.1.1.0/24", "172.0.0.0/8"], "correct_answer": "10.0.0.0/8", "explanation": "Private ranges include 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Routing and Application Protocols",
                "title": "Routing & Protocols Quiz",
                "questions": [
                    {"id": "q1", "question": "Routers primarily operate at which OSI layer?", "options": ["Data Link", "Network", "Transport", "Application"], "correct_answer": "Network", "explanation": "Routers forward packets based on network-layer (IP) addresses."},
                    {"id": "q2", "question": "DNS is used to:", "options": ["Encrypt traffic", "Resolve domain names to IP addresses", "Assign IP addresses", "Route packets"], "correct_answer": "Resolve domain names to IP addresses", "explanation": "DNS translates domain names into IP addresses."},
                    {"id": "q3", "question": "The default port for HTTPS is:", "options": ["80", "443", "22", "53"], "correct_answer": "443", "explanation": "HTTPS uses TCP port 443 by default."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Explain network models", "Apply IP addressing concepts", "Differentiate TCP and UDP", "Understand routing and common protocols"]
    },
    "cs310": {
        "title": "Machine Learning",
        "topics": ["Supervised Learning", "Unsupervised Learning", "Model Evaluation", "Overfitting and Regularization", "Neural Networks"],
        "lessons": [
            {"id": "lesson_1", "topic": "Supervised Learning", "title": "Regression and Classification", "content": "Learn how labeled data is used to train models.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Unsupervised Learning", "title": "Clustering and Dimensionality Reduction", "content": "Explore patterns in unlabeled data.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Model Evaluation", "title": "Metrics and Validation", "content": "Evaluate models using accuracy, precision, recall, and cross-validation.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Supervised Learning",
                "title": "Supervised Learning Quiz",
                "questions": [
                    {"id": "q1", "question": "Which task is supervised learning?", "options": ["Clustering customers", "Predicting house prices", "Dimensionality reduction", "Association rules"], "correct_answer": "Predicting house prices", "explanation": "Predicting prices uses labeled data and is supervised learning (regression)."},
                    {"id": "q2", "question": "Classification models predict:", "options": ["Continuous values", "Discrete class labels", "Only probabilities", "Clusters"], "correct_answer": "Discrete class labels", "explanation": "Classification predicts discrete categories (labels)."},
                    {"id": "q3", "question": "A training set is used to:", "options": ["Evaluate final performance only", "Train model parameters", "Select test labels", "Deploy the model"], "correct_answer": "Train model parameters", "explanation": "Training data is used to fit model parameters."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_2",
                "topic": "Unsupervised Learning",
                "title": "Unsupervised Learning Quiz",
                "questions": [
                    {"id": "q1", "question": "K-means is primarily used for:", "options": ["Classification", "Regression", "Clustering", "Forecasting"], "correct_answer": "Clustering", "explanation": "K-means groups data into clusters based on similarity."},
                    {"id": "q2", "question": "PCA is used to:", "options": ["Increase model variance", "Reduce dimensionality", "Label data", "Increase overfitting"], "correct_answer": "Reduce dimensionality", "explanation": "Principal Component Analysis reduces dimensionality while preserving variance."},
                    {"id": "q3", "question": "Unsupervised learning typically uses:", "options": ["Labeled data", "Unlabeled data", "Only test data", "Balanced classes"], "correct_answer": "Unlabeled data", "explanation": "Unsupervised methods learn patterns without labels."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Evaluation & Overfitting",
                "title": "Model Evaluation Quiz",
                "questions": [
                    {"id": "q1", "question": "Overfitting occurs when a model:", "options": ["Performs well on training but poorly on new data", "Underperforms on training data", "Is too simple", "Has no parameters"], "correct_answer": "Performs well on training but poorly on new data", "explanation": "Overfitting is poor generalization despite high training performance."},
                    {"id": "q2", "question": "Which technique helps reduce overfitting?", "options": ["Regularization", "Adding more noise", "Reducing training data", "Increasing model complexity"], "correct_answer": "Regularization", "explanation": "Regularization penalizes complexity to improve generalization."},
                    {"id": "q3", "question": "Cross-validation is used to:", "options": ["Train on all data", "Estimate model performance on unseen data", "Increase bias", "Eliminate variance"], "correct_answer": "Estimate model performance on unseen data", "explanation": "Cross-validation provides a robust estimate of out-of-sample performance."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Differentiate ML paradigms", "Train supervised models", "Apply clustering and PCA", "Evaluate and tune models"]
    },
    "cs320": {
        "title": "Computer Security",
        "topics": ["CIA Triad", "Cryptography", "Authentication and Authorization", "Web Vulnerabilities", "Network Security"],
        "lessons": [
            {"id": "lesson_1", "topic": "CIA Triad", "title": "Security Fundamentals", "content": "Understand confidentiality, integrity, and availability.", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Cryptography", "title": "Encryption Basics", "content": "Learn symmetric vs. asymmetric encryption and hashing.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Web Security", "title": "Common Vulnerabilities", "content": "Identify SQL injection, XSS, and CSRF risks.", "duration_minutes": 35, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "CIA Triad",
                "title": "Security Fundamentals Quiz",
                "questions": [
                    {"id": "q1", "question": "Confidentiality primarily means:", "options": ["Data is accurate", "Only authorized users can access data", "Systems are always available", "Data is encrypted"], "correct_answer": "Only authorized users can access data", "explanation": "Confidentiality restricts access to authorized users."},
                    {"id": "q2", "question": "Integrity refers to:", "options": ["Keeping systems running", "Ensuring data is accurate and unaltered", "Encrypting all traffic", "Backing up data only"], "correct_answer": "Ensuring data is accurate and unaltered", "explanation": "Integrity ensures data is trustworthy and not modified improperly."},
                    {"id": "q3", "question": "Availability means:", "options": ["Data is secret", "Systems and data are accessible when needed", "All traffic is encrypted", "Only admins can log in"], "correct_answer": "Systems and data are accessible when needed", "explanation": "Availability ensures systems and data are accessible to authorized users."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Cryptography",
                "title": "Cryptography Quiz",
                "questions": [
                    {"id": "q1", "question": "Which is an example of symmetric encryption?", "options": ["RSA", "AES", "ECC", "Diffie-Hellman"], "correct_answer": "AES", "explanation": "AES uses the same key for encryption and decryption (symmetric)."},
                    {"id": "q2", "question": "Public-key encryption uses:", "options": ["One shared secret key", "A public and a private key", "Only a private key", "Only a public key"], "correct_answer": "A public and a private key", "explanation": "Asymmetric encryption uses a key pair: public and private."},
                    {"id": "q3", "question": "A hash function is used to:", "options": ["Encrypt data reversibly", "Create a fixed-size digest", "Compress data", "Generate random keys"], "correct_answer": "Create a fixed-size digest", "explanation": "Hashing produces a one-way fixed-size digest for integrity checks."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Web Vulnerabilities",
                "title": "Web Security Quiz",
                "questions": [
                    {"id": "q1", "question": "SQL injection occurs when:", "options": ["Input is not sanitized and alters database queries", "Passwords are encrypted", "HTTPS is disabled", "Cookies are secure"], "correct_answer": "Input is not sanitized and alters database queries", "explanation": "SQL injection exploits unsanitized input to manipulate SQL queries."},
                    {"id": "q2", "question": "Cross-site scripting (XSS) allows attackers to:", "options": ["Steal user sessions by running scripts in browsers", "Access the database directly", "Change server OS", "Encrypt files"], "correct_answer": "Steal user sessions by running scripts in browsers", "explanation": "XSS injects scripts executed in the victim’s browser."},
                    {"id": "q3", "question": "CSRF attacks rely on:", "options": ["Tricking a logged-in user to submit unwanted requests", "Brute-force passwords", "Breaking TLS", "Buffer overflows"], "correct_answer": "Tricking a logged-in user to submit unwanted requests", "explanation": "CSRF exploits authenticated users to perform actions without consent."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Explain the CIA triad", "Apply basic cryptography concepts", "Identify common web vulnerabilities", "Understand authentication and authorization"]
    },
    "stat201": {
        "title": "Business Statistics",
        "topics": ["Descriptive Statistics", "Probability", "Distributions", "Hypothesis Testing", "Regression"],
        "lessons": [
            {"id": "lesson_1", "topic": "Descriptive Statistics", "title": "Summarizing Data", "content": "Compute mean, median, variance, and standard deviation.", "duration_minutes": 30, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Probability", "title": "Basics of Probability", "content": "Calculate probabilities and interpret outcomes.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Hypothesis Testing", "title": "Testing Claims", "content": "Understand null and alternative hypotheses and p-values.", "duration_minutes": 35, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Descriptive Statistics",
                "title": "Descriptive Statistics Quiz",
                "questions": [
                    {"id": "q1", "question": "The mean is:", "options": ["The middle value", "The average of all values", "The most frequent value", "The range"], "correct_answer": "The average of all values", "explanation": "Mean is the sum divided by the number of values."},
                    {"id": "q2", "question": "The median is:", "options": ["The average", "The middle value when ordered", "The largest value", "The most frequent value"], "correct_answer": "The middle value when ordered", "explanation": "Median is the middle value after sorting the data."},
                    {"id": "q3", "question": "Standard deviation measures:", "options": ["Central tendency", "Spread of data", "Total count", "Maximum value"], "correct_answer": "Spread of data", "explanation": "Standard deviation quantifies dispersion around the mean."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Probability",
                "title": "Probability Quiz",
                "questions": [
                    {"id": "q1", "question": "A probability value must be between:", "options": ["-1 and 1", "0 and 1", "0 and 100", "-100 and 100"], "correct_answer": "0 and 1", "explanation": "Probabilities range from 0 (impossible) to 1 (certain)."},
                    {"id": "q2", "question": "If two events are independent, then P(A and B) equals:", "options": ["P(A) + P(B)", "P(A) × P(B)", "P(A) / P(B)", "P(A) - P(B)"], "correct_answer": "P(A) × P(B)", "explanation": "For independent events, the joint probability is the product."},
                    {"id": "q3", "question": "The complement of event A is:", "options": ["P(A)", "1 - P(A)", "P(A) + 1", "P(A)/2"], "correct_answer": "1 - P(A)", "explanation": "The complement is the probability that A does not occur."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Hypothesis Testing",
                "title": "Hypothesis Testing Quiz",
                "questions": [
                    {"id": "q1", "question": "The null hypothesis typically states:", "options": ["There is an effect", "There is no effect", "The alternative is true", "The sample is biased"], "correct_answer": "There is no effect", "explanation": "The null hypothesis assumes no effect or no difference."},
                    {"id": "q2", "question": "A p-value represents:", "options": ["Probability the null is true", "Probability of observing data as extreme under the null", "Sample size", "Confidence level"], "correct_answer": "Probability of observing data as extreme under the null", "explanation": "The p-value measures evidence against the null hypothesis."},
                    {"id": "q3", "question": "If p-value < alpha, we:", "options": ["Fail to reject the null", "Reject the null", "Accept the null", "Increase sample size"], "correct_answer": "Reject the null", "explanation": "A p-value below alpha indicates statistically significant evidence."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Summarize data", "Apply probability rules", "Conduct hypothesis tests", "Interpret statistical results"]
    },
    "bus301": {
        "title": "Business Ethics",
        "topics": ["Ethical Frameworks", "Corporate Social Responsibility", "Compliance", "Stakeholder Analysis", "Ethical Decision Making"],
        "lessons": [
            {"id": "lesson_1", "topic": "Ethical Frameworks", "title": "Ethics in Business", "content": "Explore utilitarianism, rights, and justice approaches.", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "CSR", "title": "Corporate Social Responsibility", "content": "Understand how companies balance profit, people, and planet.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Compliance", "title": "Regulation and Governance", "content": "Learn why compliance systems prevent legal and reputational risks.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Ethical Frameworks",
                "title": "Ethics Frameworks Quiz",
                "questions": [
                    {"id": "q1", "question": "Utilitarianism focuses on:", "options": ["Maximizing overall good", "Following rules regardless of outcomes", "Individual rights only", "Short-term profits"], "correct_answer": "Maximizing overall good", "explanation": "Utilitarianism aims for the greatest good for the greatest number."},
                    {"id": "q2", "question": "A rights-based approach emphasizes:", "options": ["Cost reduction", "Individual rights and dignity", "Market share", "Speed"], "correct_answer": "Individual rights and dignity", "explanation": "Rights-based ethics protect fundamental human rights."},
                    {"id": "q3", "question": "Justice ethics focuses on:", "options": ["Fairness and equity", "Profit maximization", "Only legal compliance", "Public relations"], "correct_answer": "Fairness and equity", "explanation": "Justice ethics centers on fairness in distribution and process."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "CSR",
                "title": "CSR Quiz",
                "questions": [
                    {"id": "q1", "question": "CSR refers to:", "options": ["Only charity donations", "Business responsibility to society", "Marketing campaigns", "Tax minimization"], "correct_answer": "Business responsibility to society", "explanation": "CSR includes ethical, social, and environmental responsibilities."},
                    {"id": "q2", "question": "The triple bottom line includes:", "options": ["People, Planet, Profit", "Revenue, Costs, Profit", "Quality, Speed, Cost", "Risk, Return, Growth"], "correct_answer": "People, Planet, Profit", "explanation": "The triple bottom line expands performance beyond financial results."},
                    {"id": "q3", "question": "Stakeholder theory suggests companies should:", "options": ["Focus only on shareholders", "Consider all stakeholder interests", "Ignore community impacts", "Maximize short-term profit"], "correct_answer": "Consider all stakeholder interests", "explanation": "Stakeholder theory considers customers, employees, suppliers, and communities."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Ethical Decision Making",
                "title": "Ethical Decisions Quiz",
                "questions": [
                    {"id": "q1", "question": "A conflict of interest occurs when:", "options": ["Personal interests affect professional judgment", "A project is delayed", "Costs are high", "Competition is intense"], "correct_answer": "Personal interests affect professional judgment", "explanation": "Conflicts arise when personal interests can influence decisions."},
                    {"id": "q2", "question": "Whistleblowing is:", "options": ["Reporting illegal or unethical behavior", "Leaking trade secrets", "Firing employees", "Marketing a product"], "correct_answer": "Reporting illegal or unethical behavior", "explanation": "Whistleblowing reports wrongdoing inside an organization."},
                    {"id": "q3", "question": "An ethical culture is strengthened by:", "options": ["Clear values and leadership example", "No policies", "Ignoring complaints", "Only profit targets"], "correct_answer": "Clear values and leadership example", "explanation": "Ethical culture relies on clear values and leadership behavior."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Apply ethical frameworks", "Understand CSR", "Analyze stakeholder impacts", "Make ethical decisions"]
    },
    "comm101": {
        "title": "Technical Communication",
        "topics": ["Audience and Purpose", "Report Structure", "Data Visualization", "Presentations", "Editing and Style"],
        "lessons": [
            {"id": "lesson_1", "topic": "Audience and Purpose", "title": "Know Your Audience", "content": "Tailor technical messages to different audiences.", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Report Structure", "title": "Technical Reports", "content": "Organize reports with clear sections and evidence.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Presentations", "title": "Technical Presentations", "content": "Deliver clear, concise presentations with visuals.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Audience and Purpose",
                "title": "Audience Quiz",
                "questions": [
                    {"id": "q1", "question": "The primary goal of technical communication is:", "options": ["Impressing with jargon", "Clear and accurate information", "Longer documents", "Avoiding visuals"], "correct_answer": "Clear and accurate information", "explanation": "Technical communication prioritizes clarity and accuracy."},
                    {"id": "q2", "question": "When writing for nontechnical audiences, you should:", "options": ["Use more acronyms", "Define terms and simplify", "Skip explanations", "Add equations"], "correct_answer": "Define terms and simplify", "explanation": "Adapt language and define terms for accessibility."},
                    {"id": "q3", "question": "Purpose statements help by:", "options": ["Hiding the main point", "Clarifying document goals", "Adding length", "Removing structure"], "correct_answer": "Clarifying document goals", "explanation": "A clear purpose guides content selection and organization."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Report Structure",
                "title": "Reports Quiz",
                "questions": [
                    {"id": "q1", "question": "A typical technical report includes:", "options": ["Abstract, Methods, Results, Conclusion", "Only results", "Only introduction", "Images only"], "correct_answer": "Abstract, Methods, Results, Conclusion", "explanation": "Standard report structure includes purpose, methods, results, and conclusions."},
                    {"id": "q2", "question": "Headings are important because they:", "options": ["Increase word count", "Improve readability and navigation", "Replace content", "Hide key points"], "correct_answer": "Improve readability and navigation", "explanation": "Headings organize content and help readers scan."},
                    {"id": "q3", "question": "Evidence in reports should be:", "options": ["Unverified", "Credible and cited", "Only opinions", "Hidden"], "correct_answer": "Credible and cited", "explanation": "Technical claims require credible sources and citations."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Presentations",
                "title": "Presentations Quiz",
                "questions": [
                    {"id": "q1", "question": "Effective slides should:", "options": ["Be text-heavy", "Highlight key points", "Use tiny fonts", "Include every detail"], "correct_answer": "Highlight key points", "explanation": "Slides support the speaker by emphasizing key points."},
                    {"id": "q2", "question": "Good visuals should:", "options": ["Confuse the audience", "Match the message", "Be decorative only", "Replace speaking"], "correct_answer": "Match the message", "explanation": "Visuals should directly support the message."},
                    {"id": "q3", "question": "A strong conclusion should:", "options": ["Introduce new data", "Summarize and call to action", "Ignore questions", "End abruptly"], "correct_answer": "Summarize and call to action", "explanation": "Conclusions reinforce the main message and next steps."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Tailor messages to audiences", "Write clear technical reports", "Use visuals effectively", "Deliver strong presentations"]
    },
    "math241": {
        "title": "Calculus III",
        "topics": ["Vectors", "Partial Derivatives", "Multiple Integrals", "Vector Fields", "Line and Surface Integrals"],
        "lessons": [
            {"id": "lesson_1", "topic": "Vectors", "title": "Vector Basics", "content": "Work with vectors in 2D and 3D and compute dot and cross products.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Partial Derivatives", "title": "Multivariable Differentiation", "content": "Compute partials and gradients of multivariable functions.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Multiple Integrals", "title": "Double and Triple Integrals", "content": "Evaluate integrals over regions and volumes.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Vectors",
                "title": "Vectors Quiz",
                "questions": [
                    {"id": "q1", "question": "The dot product of two perpendicular vectors is:", "options": ["0", "1", "-1", "Depends on magnitude"], "correct_answer": "0", "explanation": "Perpendicular vectors have zero dot product."},
                    {"id": "q2", "question": "The cross product of two vectors is:", "options": ["A scalar", "A vector perpendicular to both", "Always zero", "Always parallel"], "correct_answer": "A vector perpendicular to both", "explanation": "The cross product produces a vector orthogonal to both inputs."},
                    {"id": "q3", "question": "The magnitude of vector (3,4,0) is:", "options": ["5", "7", "4", "3"], "correct_answer": "5", "explanation": "Magnitude is sqrt(3^2 + 4^2 + 0^2) = 5."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_2",
                "topic": "Partial Derivatives",
                "title": "Partial Derivatives Quiz",
                "questions": [
                    {"id": "q1", "question": "A partial derivative measures:", "options": ["Rate of change holding other variables constant", "Total change in all variables", "Area under a curve", "Vector length"], "correct_answer": "Rate of change holding other variables constant", "explanation": "Partial derivatives treat other variables as constants."},
                    {"id": "q2", "question": "The gradient of a function points in the direction of:", "options": ["Greatest increase", "Greatest decrease", "Zero slope", "Constant value"], "correct_answer": "Greatest increase", "explanation": "The gradient points toward steepest ascent."},
                    {"id": "q3", "question": "If f(x,y)=x^2+y^2, then ∂f/∂x =", "options": ["2x", "2y", "x+y", "x^2"], "correct_answer": "2x", "explanation": "Differentiate with respect to x, treating y as constant."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            },
            {
                "id": "quiz_3",
                "topic": "Multiple Integrals",
                "title": "Multiple Integrals Quiz",
                "questions": [
                    {"id": "q1", "question": "Double integrals are used to compute:", "options": ["Area and volume", "Only derivatives", "Only slopes", "Only vectors"], "correct_answer": "Area and volume", "explanation": "Double integrals can compute area, volume, and mass."},
                    {"id": "q2", "question": "Changing the order of integration can:", "options": ["Simplify evaluation", "Change the value", "Make it undefined", "Always increase it"], "correct_answer": "Simplify evaluation", "explanation": "Order changes can make regions easier to integrate."},
                    {"id": "q3", "question": "Triple integrals integrate over:", "options": ["A line", "A surface", "A volume", "A point"], "correct_answer": "A volume", "explanation": "Triple integrals compute volume integrals in 3D."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Use vectors and vector operations", "Compute partial derivatives and gradients", "Evaluate multiple integrals", "Apply multivariable calculus"]
    },
    "phys142": {
        "title": "Physics II: Electricity & Magnetism",
        "topics": ["Electric Fields", "Electric Circuits", "Magnetism", "Electromagnetic Induction", "Waves"],
        "lessons": [
            {"id": "lesson_1", "topic": "Electric Fields", "title": "Charges and Fields", "content": "Understand Coulomb's law and electric field concepts.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Circuits", "title": "DC Circuits", "content": "Apply Ohm's law and Kirchhoff's rules to circuits.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Magnetism", "title": "Magnetic Forces and Fields", "content": "Analyze forces on moving charges and currents.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Electric Fields",
                "title": "Electric Fields Quiz",
                "questions": [
                    {"id": "q1", "question": "Coulomb's law describes:", "options": ["Force between charges", "Magnetic induction", "Energy conservation", "Wave speed"], "correct_answer": "Force between charges", "explanation": "Coulomb's law gives the electric force between charges."},
                    {"id": "q2", "question": "Electric field units are:", "options": ["N/C", "J", "W", "T"], "correct_answer": "N/C", "explanation": "Electric field is force per unit charge (N/C)."},
                    {"id": "q3", "question": "Electric potential is:", "options": ["Energy per unit charge", "Force per unit charge", "Charge per unit area", "Current per unit time"], "correct_answer": "Energy per unit charge", "explanation": "Electric potential is potential energy per unit charge."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_2",
                "topic": "Circuits",
                "title": "Circuits Quiz",
                "questions": [
                    {"id": "q1", "question": "Ohm's law is:", "options": ["V = IR", "F = ma", "P = IV", "E = mc^2"], "correct_answer": "V = IR", "explanation": "Ohm's law relates voltage, current, and resistance."},
                    {"id": "q2", "question": "Kirchhoff's current law states:", "options": ["Sum of currents into a node equals sum out", "Voltages add to zero in a loop", "Current is constant in parallel", "Resistance adds in parallel"], "correct_answer": "Sum of currents into a node equals sum out", "explanation": "KCL is conservation of charge at a node."},
                    {"id": "q3", "question": "Equivalent resistance in series is:", "options": ["Sum of resistances", "Product of resistances", "Inverse sum", "Difference of resistances"], "correct_answer": "Sum of resistances", "explanation": "Series resistances add directly."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Magnetism",
                "title": "Magnetism Quiz",
                "questions": [
                    {"id": "q1", "question": "Magnetic force on a moving charge is given by:", "options": ["F = qvB sinθ", "F = qE", "F = ma", "F = kq1q2/r^2"], "correct_answer": "F = qvB sinθ", "explanation": "The magnetic force is qvB sinθ."},
                    {"id": "q2", "question": "The right-hand rule is used to determine:", "options": ["Direction of magnetic force", "Magnitude of charge", "Resistance", "Electric potential"], "correct_answer": "Direction of magnetic force", "explanation": "Right-hand rule gives direction of magnetic force or field."},
                    {"id": "q3", "question": "Faraday's law relates to:", "options": ["Induced emf from changing magnetic flux", "Electric force between charges", "Ohm's law", "Newton's second law"], "correct_answer": "Induced emf from changing magnetic flux", "explanation": "Faraday's law states induced emf equals the rate of change of magnetic flux."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Analyze electric fields and potential", "Solve circuit problems", "Apply magnetic force laws", "Understand induction"]
    },
    "engr201": {
        "title": "Statics",
        "topics": ["Forces and Moments", "Equilibrium", "Trusses", "Friction", "Distributed Loads"],
        "lessons": [
            {"id": "lesson_1", "topic": "Forces and Moments", "title": "Force Systems", "content": "Resolve forces and compute moments about points.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Equilibrium", "title": "Static Equilibrium", "content": "Apply equilibrium equations in 2D systems.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Trusses", "title": "Truss Analysis", "content": "Analyze truss members using method of joints.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Forces and Moments",
                "title": "Forces & Moments Quiz",
                "questions": [
                    {"id": "q1", "question": "Moment of a force is:", "options": ["Force × perpendicular distance", "Mass × acceleration", "Force / distance", "Work / time"], "correct_answer": "Force × perpendicular distance", "explanation": "Moment equals force times perpendicular lever arm."},
                    {"id": "q2", "question": "A force couple produces:", "options": ["Pure moment", "Pure force", "No effect", "Only translation"], "correct_answer": "Pure moment", "explanation": "A couple creates rotation without net force."},
                    {"id": "q3", "question": "The sign of a moment depends on:", "options": ["Rotation direction", "Force magnitude only", "Distance only", "Units"], "correct_answer": "Rotation direction", "explanation": "Clockwise or counterclockwise determines sign convention."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_2",
                "topic": "Equilibrium",
                "title": "Equilibrium Quiz",
                "questions": [
                    {"id": "q1", "question": "For a body in 2D equilibrium, the equations are:", "options": ["ΣFx=0, ΣFy=0, ΣM=0", "F=ma only", "ΣF=0 only", "ΣM=0 only"], "correct_answer": "ΣFx=0, ΣFy=0, ΣM=0", "explanation": "Static equilibrium requires zero net force and moment."},
                    {"id": "q2", "question": "If ΣFx ≠ 0, the body:", "options": ["Is in equilibrium", "Accelerates in x", "Has zero moment", "Has no forces"], "correct_answer": "Accelerates in x", "explanation": "Nonzero net force causes acceleration."},
                    {"id": "q3", "question": "A free-body diagram shows:", "options": ["All external forces and moments", "Internal stresses", "Material properties", "Only weights"], "correct_answer": "All external forces and moments", "explanation": "FBDs include all external loads and reactions."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Trusses",
                "title": "Trusses Quiz",
                "questions": [
                    {"id": "q1", "question": "A truss member is in tension when:", "options": ["It is being pulled", "It is being pushed", "It is bending", "It is twisting"], "correct_answer": "It is being pulled", "explanation": "Tension means the member is being stretched."},
                    {"id": "q2", "question": "Method of joints uses:", "options": ["ΣFx=0 and ΣFy=0 at each joint", "ΣM=0 only", "Energy methods", "Stress-strain curves"], "correct_answer": "ΣFx=0 and ΣFy=0 at each joint", "explanation": "Joints are in equilibrium with zero net force."},
                    {"id": "q3", "question": "Zero-force members occur when:", "options": ["Two non-collinear members meet at a joint with no external load", "All joints are loaded", "Members are symmetric", "Loads are uniform"], "correct_answer": "Two non-collinear members meet at a joint with no external load", "explanation": "Certain joint conditions imply zero-force members."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Resolve forces and moments", "Apply equilibrium equations", "Analyze trusses", "Interpret free-body diagrams"]
    },
    "engr205": {
        "title": "Materials Science",
        "topics": ["Atomic Structure", "Mechanical Properties", "Phase Diagrams", "Polymers", "Composites"],
        "lessons": [
            {"id": "lesson_1", "topic": "Atomic Structure", "title": "Materials at the Atomic Level", "content": "Relate bonding and structure to material properties.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Mechanical Properties", "title": "Stress and Strain", "content": "Understand elasticity, yield, and failure.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Phase Diagrams", "title": "Alloys and Phases", "content": "Use phase diagrams to predict microstructures.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Atomic Structure",
                "title": "Materials Basics Quiz",
                "questions": [
                    {"id": "q1", "question": "Metallic bonding is characterized by:", "options": ["Delocalized electrons", "Electron transfer only", "Electron sharing only", "No electrons"], "correct_answer": "Delocalized electrons", "explanation": "Metals have a sea of delocalized electrons."},
                    {"id": "q2", "question": "Crystalline materials have:", "options": ["Regular atomic arrangement", "Random arrangement", "No structure", "Only molecules"], "correct_answer": "Regular atomic arrangement", "explanation": "Crystals have periodic, ordered atomic structures."},
                    {"id": "q3", "question": "Amorphous materials are:", "options": ["Non-crystalline", "Always metals", "Perfect crystals", "Only gases"], "correct_answer": "Non-crystalline", "explanation": "Amorphous materials lack long-range order."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_2",
                "topic": "Mechanical Properties",
                "title": "Mechanical Properties Quiz",
                "questions": [
                    {"id": "q1", "question": "Stress is defined as:", "options": ["Force per unit area", "Force times length", "Energy per unit time", "Strain per unit area"], "correct_answer": "Force per unit area", "explanation": "Stress equals force divided by cross-sectional area."},
                    {"id": "q2", "question": "Strain is:", "options": ["Change in length / original length", "Force / area", "Area / length", "Energy / volume"], "correct_answer": "Change in length / original length", "explanation": "Strain is a dimensionless measure of deformation."},
                    {"id": "q3", "question": "The slope of the elastic region of a stress-strain curve is:", "options": ["Yield strength", "Elastic modulus", "Ultimate strength", "Toughness"], "correct_answer": "Elastic modulus", "explanation": "The slope in the elastic region is Young's modulus."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Phase Diagrams",
                "title": "Phase Diagrams Quiz",
                "questions": [
                    {"id": "q1", "question": "A eutectic point indicates:", "options": ["Lowest melting temperature", "Highest melting temperature", "Pure metal", "Elastic limit"], "correct_answer": "Lowest melting temperature", "explanation": "The eutectic point is the lowest temperature where liquid can exist."},
                    {"id": "q2", "question": "Solidus line represents:", "options": ["All solid region", "All liquid region", "Start of melting", "Gas phase"], "correct_answer": "All solid region", "explanation": "Below the solidus, the alloy is fully solid."},
                    {"id": "q3", "question": "The lever rule is used to:", "options": ["Find phase fractions", "Calculate stress", "Determine voltage", "Compute strain"], "correct_answer": "Find phase fractions", "explanation": "The lever rule determines phase proportions in a two-phase region."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Relate structure to properties", "Interpret stress-strain behavior", "Use phase diagrams", "Select materials for applications"]
    },
    "math246": {
        "title": "Differential Equations",
        "topics": ["First-Order ODEs", "Second-Order ODEs", "Systems of ODEs", "Laplace Transforms", "Modeling"],
        "lessons": [
            {"id": "lesson_1", "topic": "First-Order ODEs", "title": "Separable and Linear Equations", "content": "Solve basic first-order differential equations.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Second-Order ODEs", "title": "Homogeneous and Particular Solutions", "content": "Solve second-order equations with constant coefficients.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Systems", "title": "Systems of Differential Equations", "content": "Model coupled systems and use eigenvalues.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "First-Order ODEs",
                "title": "First-Order ODE Quiz",
                "questions": [
                    {"id": "q1", "question": "A separable equation can be:", "options": ["Rewritten as f(y)dy = g(x)dx", "Solved by matrix methods", "Always linear", "Only numerical"], "correct_answer": "Rewritten as f(y)dy = g(x)dx", "explanation": "Separable equations isolate x and y terms."},
                    {"id": "q2", "question": "An integrating factor is used to solve:", "options": ["Linear first-order ODEs", "Second-order ODEs", "Systems of ODEs", "Nonlinear PDEs"], "correct_answer": "Linear first-order ODEs", "explanation": "Integrating factors solve linear first-order equations."},
                    {"id": "q3", "question": "The solution to dy/dx = ky is:", "options": ["y = Ce^{kx}", "y = kx + C", "y = Cx^k", "y = C"], "correct_answer": "y = Ce^{kx}", "explanation": "Exponential growth/decay equation."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_2",
                "topic": "Second-Order ODEs",
                "title": "Second-Order ODE Quiz",
                "questions": [
                    {"id": "q1", "question": "A homogeneous linear second-order ODE with constant coefficients has solution form:", "options": ["y = e^{rx}", "y = ax + b", "y = sin(x) only", "y = ln(x)"], "correct_answer": "y = e^{rx}", "explanation": "Characteristic equation solutions give exponential forms."},
                    {"id": "q2", "question": "If the characteristic equation has complex roots, the solution is:", "options": ["Exponentials only", "Sines and cosines", "Polynomials only", "No solution"], "correct_answer": "Sines and cosines", "explanation": "Complex roots lead to sinusoidal solutions."},
                    {"id": "q3", "question": "A particular solution is used to:", "options": ["Solve nonhomogeneous equations", "Solve homogeneous equations", "Find eigenvalues", "Find initial conditions"], "correct_answer": "Solve nonhomogeneous equations", "explanation": "Nonhomogeneous ODEs require a particular solution."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            },
            {
                "id": "quiz_3",
                "topic": "Systems of ODEs",
                "title": "Systems Quiz",
                "questions": [
                    {"id": "q1", "question": "A system of linear ODEs can be written as:", "options": ["x' = Ax", "x' = b", "x = Ax", "x' = A + x"], "correct_answer": "x' = Ax", "explanation": "Linear systems are commonly expressed as x' = Ax."},
                    {"id": "q2", "question": "Eigenvalues determine:", "options": ["Solution behavior", "Initial conditions", "Integration limits", "Units"], "correct_answer": "Solution behavior", "explanation": "Eigenvalues determine stability and growth/decay."},
                    {"id": "q3", "question": "Phase plane analysis uses:", "options": ["Plots of variables against each other", "Time series only", "Fourier transforms", "Only constants"], "correct_answer": "Plots of variables against each other", "explanation": "Phase plane plots show trajectories of systems."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Solve first-order ODEs", "Solve second-order ODEs", "Analyze systems", "Model engineering systems"]
    },
    "engr202": {
        "title": "Dynamics",
        "topics": ["Kinematics", "Kinetics", "Work and Energy", "Impulse and Momentum", "Rigid Body Motion"],
        "lessons": [
            {"id": "lesson_1", "topic": "Kinematics", "title": "Motion Analysis", "content": "Describe motion of particles and rigid bodies.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Kinetics", "title": "Forces and Acceleration", "content": "Apply Newton's laws to moving bodies.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Energy", "title": "Work-Energy Methods", "content": "Solve dynamics using energy approaches.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Kinematics",
                "title": "Dynamics Kinematics Quiz",
                "questions": [
                    {"id": "q1", "question": "Acceleration is the time derivative of:", "options": ["Velocity", "Position", "Momentum", "Force"], "correct_answer": "Velocity", "explanation": "Acceleration is the rate of change of velocity."},
                    {"id": "q2", "question": "Angular velocity relates to:", "options": ["Rotation rate", "Linear speed only", "Force", "Mass"], "correct_answer": "Rotation rate", "explanation": "Angular velocity measures rate of rotation."},
                    {"id": "q3", "question": "Tangential acceleration depends on:", "options": ["Change in speed", "Change in direction only", "Mass", "Radius only"], "correct_answer": "Change in speed", "explanation": "Tangential acceleration is due to change in speed along the path."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_2",
                "topic": "Kinetics",
                "title": "Dynamics Kinetics Quiz",
                "questions": [
                    {"id": "q1", "question": "Newton's second law for a particle is:", "options": ["ΣF = ma", "ΣM = Iα", "p = mv", "E = mc^2"], "correct_answer": "ΣF = ma", "explanation": "The net force equals mass times acceleration."},
                    {"id": "q2", "question": "Impulse equals:", "options": ["Change in momentum", "Change in energy", "Force divided by time", "Mass times distance"], "correct_answer": "Change in momentum", "explanation": "Impulse is the integral of force over time and equals Δp."},
                    {"id": "q3", "question": "For planar rigid bodies, rotational equation is:", "options": ["ΣM = Iα", "ΣF = ma", "p = mv", "V = IR"], "correct_answer": "ΣM = Iα", "explanation": "Rigid body rotation follows ΣM = Iα."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "Work and Energy",
                "title": "Work-Energy Quiz",
                "questions": [
                    {"id": "q1", "question": "Work done by a force is:", "options": ["W = Fd cosθ", "W = Fd", "W = F/d", "W = mgh"], "correct_answer": "W = Fd cosθ", "explanation": "Work is the dot product of force and displacement."},
                    {"id": "q2", "question": "Power is:", "options": ["Work per unit time", "Force per unit area", "Energy per unit mass", "Momentum per unit time"], "correct_answer": "Work per unit time", "explanation": "Power measures the rate of doing work."},
                    {"id": "q3", "question": "Conservation of energy applies when:", "options": ["Only conservative forces do work", "Only nonconservative forces do work", "All forces are zero", "Mass is zero"], "correct_answer": "Only conservative forces do work", "explanation": "Energy is conserved when nonconservative work is zero."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Analyze motion with kinematics", "Apply Newton's laws to motion", "Use impulse-momentum", "Solve energy problems"]
    },
    "engr210": {
        "title": "Thermodynamics",
        "topics": ["First Law", "Second Law", "Properties of Pure Substances", "Power Cycles", "Heat Transfer"],
        "lessons": [
            {"id": "lesson_1", "topic": "First Law", "title": "Energy Conservation", "content": "Apply energy balances to closed and open systems.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Second Law", "title": "Entropy and Efficiency", "content": "Understand entropy and limits on energy conversion.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Power Cycles", "title": "Heat Engines", "content": "Analyze Rankine and Brayton cycles.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "First Law",
                "title": "First Law Quiz",
                "questions": [
                    {"id": "q1", "question": "The first law of thermodynamics states:", "options": ["Energy is conserved", "Entropy always decreases", "Heat flows cold to hot", "Work is zero"], "correct_answer": "Energy is conserved", "explanation": "The first law is conservation of energy."},
                    {"id": "q2", "question": "For a closed system, ΔE equals:", "options": ["Q - W", "Q + W", "W - Q", "0"], "correct_answer": "Q - W", "explanation": "Energy change equals heat in minus work out."},
                    {"id": "q3", "question": "Specific internal energy is:", "options": ["Energy per unit mass", "Energy per unit volume", "Energy per unit time", "Force per unit area"], "correct_answer": "Energy per unit mass", "explanation": "Specific internal energy is u = U/m."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_2",
                "topic": "Second Law",
                "title": "Second Law Quiz",
                "questions": [
                    {"id": "q1", "question": "The second law implies:", "options": ["Entropy of an isolated system increases", "Energy is created", "Heat flows hot to cold only if work is added", "Perfect efficiency is possible"], "correct_answer": "Entropy of an isolated system increases", "explanation": "Entropy increases for isolated systems."},
                    {"id": "q2", "question": "A reversible process is:", "options": ["Idealized with no entropy generation", "Always fast", "Always irreversible", "Impossible"], "correct_answer": "Idealized with no entropy generation", "explanation": "Reversible processes generate no entropy."},
                    {"id": "q3", "question": "Thermal efficiency of a heat engine is:", "options": ["W_net/Q_in", "Q_out/Q_in", "Q_in/W_net", "1 + Q_out/Q_in"], "correct_answer": "W_net/Q_in", "explanation": "Efficiency is net work output divided by heat input."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            },
            {
                "id": "quiz_3",
                "topic": "Power Cycles",
                "title": "Power Cycles Quiz",
                "questions": [
                    {"id": "q1", "question": "The Rankine cycle is commonly used in:", "options": ["Steam power plants", "Refrigerators", "Gas turbines only", "Batteries"], "correct_answer": "Steam power plants", "explanation": "Rankine cycle models steam power plants."},
                    {"id": "q2", "question": "The Brayton cycle is used for:", "options": ["Gas turbines", "Hydroelectric dams", "Solar panels", "Batteries"], "correct_answer": "Gas turbines", "explanation": "Brayton cycle models gas turbine engines."},
                    {"id": "q3", "question": "Carnot efficiency depends on:", "options": ["Hot and cold reservoir temperatures", "Working fluid only", "Pressure only", "Volume only"], "correct_answer": "Hot and cold reservoir temperatures", "explanation": "Carnot efficiency is a function of reservoir temperatures."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Apply energy balances", "Interpret entropy", "Analyze power cycles", "Evaluate thermal efficiency"]
    },
    "engr215": {
        "title": "Circuits & Electronics",
        "topics": ["Ohm's Law", "Kirchhoff's Laws", "Circuit Analysis", "AC Circuits", "Semiconductor Basics"],
        "lessons": [
            {"id": "lesson_1", "topic": "Ohm's Law", "title": "Voltage, Current, Resistance", "content": "Apply Ohm's law to simple circuits.", "duration_minutes": 30, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Kirchhoff's Laws", "title": "Circuit Laws", "content": "Use KCL and KVL to analyze networks.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "AC Circuits", "title": "AC Analysis", "content": "Understand impedance and phase in AC circuits.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Ohm's Law",
                "title": "Ohm's Law Quiz",
                "questions": [
                    {"id": "q1", "question": "Ohm's law states:", "options": ["V = IR", "P = IV", "F = ma", "E = mc^2"], "correct_answer": "V = IR", "explanation": "Voltage equals current times resistance."},
                    {"id": "q2", "question": "If R = 10Ω and I = 2A, V =", "options": ["20V", "5V", "12V", "10V"], "correct_answer": "20V", "explanation": "V = IR = 10 × 2 = 20V."},
                    {"id": "q3", "question": "Resistance in series is:", "options": ["Sum of resistances", "Inverse sum", "Product of resistances", "Average"], "correct_answer": "Sum of resistances", "explanation": "Series resistances add directly."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            },
            {
                "id": "quiz_2",
                "topic": "Kirchhoff's Laws",
                "title": "Kirchhoff Quiz",
                "questions": [
                    {"id": "q1", "question": "KCL states:", "options": ["Sum of currents at a node is zero", "Sum of voltages in a loop is zero", "Power is conserved", "Resistance is constant"], "correct_answer": "Sum of currents at a node is zero", "explanation": "Kirchhoff's current law conserves charge at a node."},
                    {"id": "q2", "question": "KVL states:", "options": ["Sum of voltages in a loop is zero", "Sum of currents in a loop is zero", "Voltage is constant", "Current is constant"], "correct_answer": "Sum of voltages in a loop is zero", "explanation": "Kirchhoff's voltage law conserves energy in a loop."},
                    {"id": "q3", "question": "A supernode occurs when:", "options": ["A voltage source connects two non-reference nodes", "A resistor is open", "A current source is shorted", "A node has no elements"], "correct_answer": "A voltage source connects two non-reference nodes", "explanation": "Supernodes form around voltage sources between nodes."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_3",
                "topic": "AC Circuits",
                "title": "AC Circuits Quiz",
                "questions": [
                    {"id": "q1", "question": "Impedance in AC circuits combines:", "options": ["Resistance and reactance", "Voltage and current", "Power and energy", "Charge and field"], "correct_answer": "Resistance and reactance", "explanation": "Impedance is the total opposition to AC, combining resistance and reactance."},
                    {"id": "q2", "question": "A capacitor in AC has reactance that:", "options": ["Decreases with frequency", "Increases with frequency", "Is constant", "Is zero"], "correct_answer": "Decreases with frequency", "explanation": "Capacitive reactance Xc = 1/(ωC), decreases with frequency."},
                    {"id": "q3", "question": "In a purely resistive AC circuit, current and voltage are:", "options": ["In phase", "90° out of phase", "180° out of phase", "Random"], "correct_answer": "In phase", "explanation": "Resistive circuits have zero phase difference."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Apply Ohm's law", "Use Kirchhoff's laws", "Analyze AC circuits", "Understand basic electronics"]
    },
    "cs350": {
        "title": "Senior Capstone Project I",
        "topics": ["Project Planning", "Requirements Analysis", "System Design", "Implementation", "Team Collaboration"],
        "lessons": [
            {"id": "lesson_1", "topic": "Planning", "title": "Project Planning and Scope", "content": "Define project goals, scope, and deliverables for your capstone.", "duration_minutes": 30, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Design", "title": "System Architecture Design", "content": "Design the architecture and components of your system.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Implementation", "title": "Agile Development", "content": "Implement features iteratively using agile methodologies.", "duration_minutes": 45, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Project Management",
                "title": "Capstone Planning Quiz",
                "questions": [
                    {"id": "q1", "question": "A well-defined project scope includes:", "options": ["Clear objectives and deliverables", "Only deadlines", "No constraints", "Just ideas"], "correct_answer": "Clear objectives and deliverables", "explanation": "Scope defines what will and won't be delivered."},
                    {"id": "q2", "question": "Agile development emphasizes:", "options": ["Detailed upfront planning", "Iterative development and feedback", "No documentation", "Waterfall phases"], "correct_answer": "Iterative development and feedback", "explanation": "Agile values working software and responsiveness to change."},
                    {"id": "q3", "question": "Version control for team projects is important for:", "options": ["Collaboration and tracking changes", "Faster coding", "Fewer meetings", "Graphics design"], "correct_answer": "Collaboration and tracking changes", "explanation": "Version control enables collaboration and maintains code history."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Plan software projects", "Design system architecture", "Work in teams", "Deliver working software"]
    },
    "cs351": {
        "title": "Senior Capstone Project II",
        "topics": ["Testing and QA", "Deployment", "Documentation", "Presentations", "Portfolio Development"],
        "lessons": [
            {"id": "lesson_1", "topic": "Testing", "title": "Comprehensive Testing", "content": "Test your system thoroughly and fix bugs.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Deployment", "title": "Production Deployment", "content": "Deploy your application to production environments.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Documentation", "title": "Technical Documentation", "content": "Write user guides and technical documentation.", "duration_minutes": 30, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Software Quality",
                "title": "Testing & Deployment Quiz",
                "questions": [
                    {"id": "q1", "question": "Integration testing focuses on:", "options": ["Individual functions", "Interaction between components", "User interface only", "Database only"], "correct_answer": "Interaction between components", "explanation": "Integration testing verifies components work together."},
                    {"id": "q2", "question": "Continuous Integration (CI) means:", "options": ["Code is integrated and tested frequently", "Deploy once at end", "No testing", "Manual deployment"], "correct_answer": "Code is integrated and tested frequently", "explanation": "CI automates builds and tests with each commit."},
                    {"id": "q3", "question": "Good documentation should be:", "options": ["Clear, accurate, and maintained", "Written once and never updated", "Only for developers", "Optional"], "correct_answer": "Clear, accurate, and maintained", "explanation": "Documentation must be clear and kept current."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Test software thoroughly", "Deploy applications", "Write documentation", "Present projects professionally"]
    },
    "cs3xx": {
        "title": "Technical Elective",
        "topics": ["Specialized CS Topic", "Advanced Concepts", "Practical Applications", "Industry Trends", "Case Studies"],
        "lessons": [
            {"id": "lesson_1", "topic": "Introduction", "title": "Course Overview", "content": "Explore this specialized CS area in depth.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Core Concepts", "title": "Fundamental Principles", "content": "Master the key concepts and techniques.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Applications", "title": "Real-World Projects", "content": "Apply knowledge to practical scenarios.", "duration_minutes": 40, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Core Concepts",
                "title": "Elective Concepts Quiz",
                "questions": [
                    {"id": "q1", "question": "Why specialize in a CS subdomain?", "options": ["Required by law", "Develop deep expertise for career differentiation", "Easier classes", "No reason"], "correct_answer": "Develop deep expertise for career differentiation", "explanation": "Specialization builds valuable expertise in high-demand areas."},
                    {"id": "q2", "question": "Technical electives help you:", "options": ["Graduate faster", "Align skills with career interests", "Avoid core courses", "Reduce workload"], "correct_answer": "Align skills with career interests", "explanation": "Electives let you pursue interests and career goals."},
                    {"id": "q3", "question": "Industry trends in specialized areas:", "options": ["Never change", "Evolve rapidly requiring continuous learning", "Only matter for research", "Are irrelevant"], "correct_answer": "Evolve rapidly requiring continuous learning", "explanation": "Tech specializations require staying current with trends."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Master specialized CS topic", "Apply advanced techniques", "Build relevant projects", "Prepare for specialized careers"]
    },
    "cs4xx": {
        "title": "Advanced Technical Elective",
        "topics": ["Advanced Specialization", "Cutting-Edge Topics", "Research Methods", "Innovation", "Professional Practice"],
        "lessons": [
            {"id": "lesson_1", "topic": "Advanced Topics", "title": "Deep Dive", "content": "Explore advanced research and industry applications.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Innovation", "title": "Emerging Technologies", "content": "Study cutting-edge developments in the field.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Practice", "title": "Professional Application", "content": "Apply skills to complex real-world problems.", "duration_minutes": 40, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Advanced Concepts",
                "title": "Advanced Topics Quiz",
                "questions": [
                    {"id": "q1", "question": "Advanced electives prepare you for:", "options": ["Entry-level positions only", "Specialized roles and graduate study", "Teaching only", "Management only"], "correct_answer": "Specialized roles and graduate study", "explanation": "Advanced courses build expertise for specialized careers or research."},
                    {"id": "q2", "question": "Research skills developed include:", "options": ["Memorization only", "Critical analysis and problem solving", "Following instructions", "Avoiding complexity"], "correct_answer": "Critical analysis and problem solving", "explanation": "Research develops analytical and independent problem-solving skills."},
                    {"id": "q3", "question": "Innovation in technology requires:", "options": ["Following old patterns only", "Combining knowledge with creativity", "Avoiding risks", "Working alone"], "correct_answer": "Combining knowledge with creativity", "explanation": "Innovation blends technical knowledge with creative thinking."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Master advanced specialized topics", "Apply cutting-edge techniques", "Develop research skills", "Innovate solutions"]
    },
    "cs400": {
        "title": "Theory of Computation",
        "topics": ["Automata Theory", "Formal Languages", "Computability", "Complexity Classes", "Decidability"],
        "lessons": [
            {"id": "lesson_1", "topic": "Automata", "title": "Finite Automata and Regular Languages", "content": "Study DFAs, NFAs, and regular expressions.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Context-Free", "title": "Context-Free Languages", "content": "Explore pushdown automata and CFGs.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Computability", "title": "Turing Machines and Decidability", "content": "Understand the limits of computation.", "duration_minutes": 40, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Automata",
                "title": "Automata Quiz",
                "questions": [
                    {"id": "q1", "question": "A DFA has:", "options": ["One start state and deterministic transitions", "Multiple start states", "Non-deterministic transitions", "No accept states"], "correct_answer": "One start state and deterministic transitions", "explanation": "DFAs have exactly one transition per symbol from each state."},
                    {"id": "q2", "question": "Regular expressions describe:", "options": ["Regular languages", "Context-free languages", "Undecidable languages", "All languages"], "correct_answer": "Regular languages", "explanation": "Regex and finite automata describe regular languages."},
                    {"id": "q3", "question": "The pumping lemma is used to:", "options": ["Prove a language is regular", "Prove a language is not regular", "Design automata", "Optimize algorithms"], "correct_answer": "Prove a language is not regular", "explanation": "The pumping lemma shows certain languages aren't regular."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            },
            {
                "id": "quiz_2",
                "topic": "Context-Free Languages",
                "title": "CFG Quiz",
                "questions": [
                    {"id": "q1", "question": "A context-free grammar consists of:", "options": ["Variables, terminals, rules, start symbol", "Only terminals", "Only variables", "Turing machines"], "correct_answer": "Variables, terminals, rules, start symbol", "explanation": "CFGs have variables, terminals, production rules, and a start symbol."},
                    {"id": "q2", "question": "Pushdown automata have:", "options": ["A stack for memory", "Multiple stacks", "No memory", "Only registers"], "correct_answer": "A stack for memory", "explanation": "PDAs use a stack, making them more powerful than finite automata."},
                    {"id": "q3", "question": "The language {a^n b^n | n ≥ 0} is:", "options": ["Regular", "Context-free but not regular", "Context-sensitive", "Undecidable"], "correct_answer": "Context-free but not regular", "explanation": "This language requires counting, which needs a stack (CFG)."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            },
            {
                "id": "quiz_3",
                "topic": "Computability",
                "title": "Computability Quiz",
                "questions": [
                    {"id": "q1", "question": "A Turing machine can:", "options": ["Compute any computable function", "Only add numbers", "Only check regular languages", "Solve the halting problem"], "correct_answer": "Compute any computable function", "explanation": "Turing machines define the limits of computation."},
                    {"id": "q2", "question": "The halting problem is:", "options": ["Decidable", "Undecidable", "Solvable in polynomial time", "Trivial"], "correct_answer": "Undecidable", "explanation": "No algorithm can determine if arbitrary programs halt."},
                    {"id": "q3", "question": "P vs NP asks whether:", "options": ["Problems verifiable in polynomial time are solvable in polynomial time", "All problems are easy", "Turing machines are powerful", "Algorithms exist for everything"], "correct_answer": "Problems verifiable in polynomial time are solvable in polynomial time", "explanation": "P vs NP is one of the biggest unsolved problems in computer science."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Understand automata and formal languages", "Analyze computability", "Study complexity classes", "Recognize fundamental limits"]
    },
    "cs410": {
        "title": "Professional Development",
        "topics": ["Resume and Portfolio", "Technical Interviews", "Networking", "Career Planning", "Workplace Skills"],
        "lessons": [
            {"id": "lesson_1", "topic": "Resume", "title": "Building Your Resume", "content": "Craft a compelling technical resume and portfolio.", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Interviews", "title": "Technical Interview Prep", "content": "Practice coding interviews and problem-solving.", "duration_minutes": 40, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Networking", "title": "Professional Networking", "content": "Build your professional network and personal brand.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Career Preparation",
                "title": "Career Prep Quiz",
                "questions": [
                    {"id": "q1", "question": "A technical resume should emphasize:", "options": ["Personal hobbies", "Relevant projects and technical skills", "Unrelated work history", "High school activities"], "correct_answer": "Relevant projects and technical skills", "explanation": "Technical resumes highlight programming skills and relevant projects."},
                    {"id": "q2", "question": "Behavioral interview questions assess:", "options": ["Coding speed", "How you handle situations and work with others", "Only algorithms knowledge", "GPA"], "correct_answer": "How you handle situations and work with others", "explanation": "Behavioral questions reveal soft skills and problem-solving approaches."},
                    {"id": "q3", "question": "A professional portfolio should include:", "options": ["Every assignment", "Best projects with descriptions and code", "Only theoretical work", "Nothing"], "correct_answer": "Best projects with descriptions and code", "explanation": "Portfolios showcase your best work with context."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Create professional resume", "Prepare for technical interviews", "Build professional network", "Plan career path"]
    },
    "gen400": {
        "title": "Senior Seminar",
        "topics": ["Current CS Topics", "Ethics in Technology", "Career Paths", "Graduate School", "Industry Trends"],
        "lessons": [
            {"id": "lesson_1", "topic": "Ethics", "title": "Ethics in Computing", "content": "Explore ethical issues in AI, privacy, and technology.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Career Paths", "title": "CS Career Options", "content": "Understand different career paths in computer science.", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_3", "topic": "Trends", "title": "Emerging Technologies", "content": "Discuss current trends like AI, blockchain, quantum computing.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Ethics and Society",
                "title": "Tech Ethics Quiz",
                "questions": [
                    {"id": "q1", "question": "Algorithmic bias can occur when:", "options": ["Training data reflects societal biases", "Code is well-written", "Models are simple", "Testing is thorough"], "correct_answer": "Training data reflects societal biases", "explanation": "Biased training data leads to biased models."},
                    {"id": "q2", "question": "Privacy concerns in tech include:", "options": ["Too few ads", "Unauthorized collection and use of personal data", "Open source software", "Code documentation"], "correct_answer": "Unauthorized collection and use of personal data", "explanation": "Privacy protection requires informed consent and data minimization."},
                    {"id": "q3", "question": "Responsible AI development requires:", "options": ["Maximum profit", "Fairness, transparency, and accountability", "No regulation", "Speed only"], "correct_answer": "Fairness, transparency, and accountability", "explanation": "Ethical AI considers societal impact and accountability."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand tech ethics", "Explore career options", "Discuss emerging trends", "Reflect on CS impact"]
    },
    "str401": {
        "title": "Strategic Management",
        "topics": ["Competitive Strategy", "Business Models", "Strategic Analysis", "Corporate Strategy", "Strategy Implementation"],
        "lessons": [
            {"id": "lesson_1", "topic": "Competitive Strategy", "title": "Porter's Five Forces", "content": "Analyze industry competition and position your business.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Business Models", "title": "Value Creation", "content": "Design and evaluate business models.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Implementation", "title": "Strategy Execution", "content": "Turn strategy into action with balanced scorecards.", "duration_minutes": 30, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Competitive Strategy",
                "title": "Strategy Analysis Quiz",
                "questions": [
                    {"id": "q1", "question": "Porter's Five Forces analyzes:", "options": ["Internal operations", "Industry competitive structure", "Employee motivation", "Product features"], "correct_answer": "Industry competitive structure", "explanation": "Five forces assess industry attractiveness and competitive intensity."},
                    {"id": "q2", "question": "Competitive advantage comes from:", "options": ["Being cheapest or offering unique value", "Copying competitors", "Avoiding innovation", "Reducing quality"], "correct_answer": "Being cheapest or offering unique value", "explanation": "Advantage requires either cost leadership or differentiation."},
                    {"id": "q3", "question": "A value chain analyzes:", "options": ["Supply costs only", "Activities that create value", "Only marketing", "Employee salaries"], "correct_answer": "Activities that create value", "explanation": "Value chain breaks down activities to identify competitive advantage sources."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            },
            {
                "id": "quiz_2",
                "topic": "Business Models",
                "title": "Business Models Quiz",
                "questions": [
                    {"id": "q1", "question": "A business model describes:", "options": ["Only revenue", "How a company creates and captures value", "Marketing plans", "Organization charts"], "correct_answer": "How a company creates and captures value", "explanation": "Business models define value proposition, customers, and revenue."},
                    {"id": "q2", "question": "Platform business models rely on:", "options": ["Manufacturing products", "Connecting users and facilitating exchanges", "Retail stores", "Single customers"], "correct_answer": "Connecting users and facilitating exchanges", "explanation": "Platforms create value by connecting participants."},
                    {"id": "q3", "question": "A sustainable competitive advantage must be:", "options": ["Valuable, rare, inimitable, and organized to exploit", "Cheap", "Easy to copy", "Short-term"], "correct_answer": "Valuable, rare, inimitable, and organized to exploit", "explanation": "VRIO framework identifies sustainable advantages."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Analyze competitive dynamics", "Design business models", "Develop corporate strategy", "Implement strategy effectively"]
    },
    "bus410": {
        "title": "Business Analytics",
        "topics": ["Data Analysis", "Predictive Analytics", "Business Intelligence", "Data Visualization", "Analytics Tools"],
        "lessons": [
            {"id": "lesson_1", "topic": "Data Analysis", "title": "Exploratory Data Analysis", "content": "Clean and explore business data for insights.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Predictive", "title": "Predictive Modeling", "content": "Build models to forecast business outcomes.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "BI Tools", "title": "Business Intelligence Platforms", "content": "Use Tableau, Power BI for dashboards and reporting.", "duration_minutes": 35, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Data Analysis",
                "title": "Data Analysis Quiz",
                "questions": [
                    {"id": "q1", "question": "Exploratory data analysis involves:", "options": ["Summarizing and visualizing data to understand patterns", "Only hypothesis testing", "Deploying models", "Writing code"], "correct_answer": "Summarizing and visualizing data to understand patterns", "explanation": "EDA discovers patterns before formal modeling."},
                    {"id": "q2", "question": "Data cleaning is important because:", "options": ["Raw data often has errors and inconsistencies", "It's optional", "Models work better with bad data", "It wastes time"], "correct_answer": "Raw data often has errors and inconsistencies", "explanation": "Clean data is essential for accurate analysis."},
                    {"id": "q3", "question": "A correlation of 0.9 indicates:", "options": ["No relationship", "Strong positive relationship", "Causation", "Weak relationship"], "correct_answer": "Strong positive relationship", "explanation": "High positive correlation shows variables move together."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_2",
                "topic": "Predictive Analytics",
                "title": "Predictive Analytics Quiz",
                "questions": [
                    {"id": "q1", "question": "Predictive analytics aims to:", "options": ["Describe past data", "Forecast future outcomes", "Only visualize", "Replace decisions"], "correct_answer": "Forecast future outcomes", "explanation": "Predictive analytics uses data to forecast future events."},
                    {"id": "q2", "question": "Feature engineering involves:", "options": ["Creating relevant variables for models", "Buying data", "Ignoring variables", "Using all variables"], "correct_answer": "Creating relevant variables for models", "explanation": "Feature engineering creates predictive variables from raw data."},
                    {"id": "q3", "question": "Model validation prevents:", "options": ["Overfitting and ensures generalization", "Accurate predictions", "Data collection", "Visualization"], "correct_answer": "Overfitting and ensures generalization", "explanation": "Validation tests model performance on new data."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Analyze business data", "Build predictive models", "Create dashboards", "Drive data-informed decisions"]
    },
    "mkt410": {
        "title": "Digital Marketing",
        "topics": ["SEO and SEM", "Social Media Marketing", "Content Marketing", "Email Marketing", "Analytics and Metrics"],
        "lessons": [
            {"id": "lesson_1", "topic": "SEO", "title": "Search Engine Optimization", "content": "Optimize websites for search engine visibility.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Social Media", "title": "Social Media Strategy", "content": "Build brand presence on social platforms.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Content", "title": "Content Marketing", "content": "Create valuable content that attracts and engages customers.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "SEO and SEM",
                "title": "SEO Quiz",
                "questions": [
                    {"id": "q1", "question": "SEO focuses on:", "options": ["Paid advertising", "Organic search rankings", "Email campaigns", "TV ads"], "correct_answer": "Organic search rankings", "explanation": "SEO improves unpaid search engine visibility."},
                    {"id": "q2", "question": "Keywords are important because:", "options": ["They match search queries", "They increase costs", "They reduce traffic", "They're decorative"], "correct_answer": "They match search queries", "explanation": "Keywords align content with user searches."},
                    {"id": "q3", "question": "SEM includes:", "options": ["Only organic search", "Paid search advertising like Google Ads", "Social media only", "Email only"], "correct_answer": "Paid search advertising like Google Ads", "explanation": "SEM includes paid search marketing."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            },
            {
                "id": "quiz_2",
                "topic": "Social Media",
                "title": "Social Media Quiz",
                "questions": [
                    {"id": "q1", "question": "Social media marketing goals include:", "options": ["Brand awareness and engagement", "Avoiding customers", "Reducing communication", "Limiting reach"], "correct_answer": "Brand awareness and engagement", "explanation": "Social media builds awareness and engagement with audiences."},
                    {"id": "q2", "question": "Engagement rate measures:", "options": ["How users interact with content", "Only follower count", "Only impressions", "Sales only"], "correct_answer": "How users interact with content", "explanation": "Engagement tracks likes, comments, shares relative to reach."},
                    {"id": "q3", "question": "Influencer marketing leverages:", "options": ["Traditional ads", "Trusted individuals with engaged audiences", "Billboards", "Cold calling"], "correct_answer": "Trusted individuals with engaged audiences", "explanation": "Influencers provide authentic endorsements to their followers."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Implement SEO strategies", "Manage social media campaigns", "Create content marketing", "Measure digital marketing ROI"]
    },
    "ent401": {
        "title": "Entrepreneurship",
        "topics": ["Opportunity Recognition", "Business Planning", "Funding and Valuation", "Lean Startup", "Growth Strategies"],
        "lessons": [
            {"id": "lesson_1", "topic": "Opportunity", "title": "Identifying Opportunities", "content": "Spot market gaps and validate business ideas.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Planning", "title": "Business Plan Development", "content": "Create a comprehensive business plan.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Funding", "title": "Raising Capital", "content": "Understand funding sources from bootstrapping to venture capital.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Entrepreneurship Basics",
                "title": "Entrepreneurship Quiz",
                "questions": [
                    {"id": "q1", "question": "A viable business opportunity requires:", "options": ["Just an idea", "Market need, feasibility, and profit potential", "Only capital", "No competition"], "correct_answer": "Market need, feasibility, and profit potential", "explanation": "Opportunities must meet a need, be feasible, and offer returns."},
                    {"id": "q2", "question": "The lean startup method emphasizes:", "options": ["Detailed 5-year plans", "Build-measure-learn cycles with MVPs", "No customer feedback", "Large initial investment"], "correct_answer": "Build-measure-learn cycles with MVPs", "explanation": "Lean startup validates assumptions quickly with minimum viable products."},
                    {"id": "q3", "question": "Venture capital is most appropriate for:", "options": ["Low-growth businesses", "High-growth potential startups", "Established companies", "Non-profits"], "correct_answer": "High-growth potential startups", "explanation": "VCs invest in scalable, high-growth opportunities."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Identify business opportunities", "Develop business plans", "Understand startup funding", "Apply lean startup principles"]
    },
    "glb401": {
        "title": "Global Business Strategy",
        "topics": ["International Trade", "Market Entry Strategies", "Cultural Differences", "Global Supply Chains", "International Finance"],
        "lessons": [
            {"id": "lesson_1", "topic": "Globalization", "title": "Global Business Environment", "content": "Understand forces driving international business.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Entry Strategies", "title": "International Market Entry", "content": "Compare exporting, licensing, joint ventures, and FDI.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Culture", "title": "Cross-Cultural Management", "content": "Navigate cultural differences in global business.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "International Business",
                "title": "Global Business Quiz",
                "questions": [
                    {"id": "q1", "question": "Comparative advantage suggests countries should:", "options": ["Produce everything domestically", "Specialize in what they do relatively better", "Avoid trade", "Only import"], "correct_answer": "Specialize in what they do relatively better", "explanation": "Comparative advantage drives beneficial specialization and trade."},
                    {"id": "q2", "question": "Tariffs are:", "options": ["Subsidies for exports", "Taxes on imports", "Quotas", "Trade agreements"], "correct_answer": "Taxes on imports", "explanation": "Tariffs are import taxes that protect domestic industries."},
                    {"id": "q3", "question": "Cultural dimensions like power distance affect:", "options": ["Currency rates", "Management styles and communication", "Product quality", "Technology only"], "correct_answer": "Management styles and communication", "explanation": "Cultural dimensions shape organizational behavior and communication."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand global trade", "Select market entry strategies", "Manage across cultures", "Analyze international markets"]
    },
    "bus490": {
        "title": "Business Capstone Project",
        "topics": ["Strategic Analysis", "Business Consulting", "Problem Solving", "Client Management", "Professional Presentation"],
        "lessons": [
            {"id": "lesson_1", "topic": "Analysis", "title": "Strategic Business Analysis", "content": "Analyze a real company's strategic position.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Solutions", "title": "Developing Recommendations", "content": "Create actionable solutions for business problems.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Presentation", "title": "Executive Presentations", "content": "Present findings and recommendations professionally.", "duration_minutes": 30, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Capstone Projects",
                "title": "Business Capstone Quiz",
                "questions": [
                    {"id": "q1", "question": "A capstone project demonstrates:", "options": ["Memorization", "Integration of business knowledge", "One skill only", "Theory without application"], "correct_answer": "Integration of business knowledge", "explanation": "Capstones synthesize learning across business disciplines."},
                    {"id": "q2", "question": "Client management requires:", "options": ["Ignoring feedback", "Clear communication and managing expectations", "Avoiding meetings", "No updates"], "correct_answer": "Clear communication and managing expectations", "explanation": "Successful consulting requires managing client relationships."},
                    {"id": "q3", "question": "Strategic recommendations should be:", "options": ["Vague and theoretical", "Specific, actionable, and justified", "Copied from competitors", "Generic"], "correct_answer": "Specific, actionable, and justified", "explanation": "Recommendations must be practical and evidence-based."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Conduct strategic analysis", "Develop business solutions", "Work with clients", "Present professionally"]
    },
    "bus495": {
        "title": "Professional Development",
        "topics": ["Resume and Cover Letters", "Interviewing", "Networking", "Career Planning", "Professionalism"],
        "lessons": [
            {"id": "lesson_1", "topic": "Job Search", "title": "Job Search Strategies", "content": "Develop effective job search and application strategies.", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Interviewing", "title": "Interview Skills", "content": "Master behavioral and case interview techniques.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Networking", "title": "Professional Networking", "content": "Build and leverage your professional network.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Career Development",
                "title": "Professional Development Quiz",
                "questions": [
                    {"id": "q1", "question": "A strong cover letter should:", "options": ["Repeat your resume", "Connect your experience to the specific role", "Be generic", "Focus on what you want"], "correct_answer": "Connect your experience to the specific role", "explanation": "Cover letters should show fit for the specific position."},
                    {"id": "q2", "question": "The STAR method for interviews involves:", "options": ["Situation, Task, Action, Result", "Skills, Training, Attitude, Results", "Salary, Title, Activities, Responsibilities", "Start, Try, Analyze, Repeat"], "correct_answer": "Situation, Task, Action, Result", "explanation": "STAR structures behavioral interview responses."},
                    {"id": "q3", "question": "Networking is valuable because:", "options": ["Many jobs are filled through connections", "It's required", "It's only for extroverts", "It replaces skills"], "correct_answer": "Many jobs are filled through connections", "explanation": "Most opportunities come through professional networks."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Create effective resumes", "Interview successfully", "Build professional network", "Plan career trajectory"]
    },
    "sem401": {
        "title": "Senior Seminar",
        "topics": ["Current Business Trends", "Leadership", "Ethics", "Global Issues", "Career Transitions"],
        "lessons": [
            {"id": "lesson_1", "topic": "Trends", "title": "Business Trends and Disruption", "content": "Explore digital transformation and emerging business models.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Leadership", "title": "Leadership in Practice", "content": "Reflect on leadership development and personal growth.", "duration_minutes": 25, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Transition", "title": "Transitioning to Professional Life", "content": "Prepare for your first role and continued development.", "duration_minutes": 25, "difficulty": "beginner"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Business Trends",
                "title": "Business Trends Quiz",
                "questions": [
                    {"id": "q1", "question": "Digital transformation means:", "options": ["Just buying computers", "Integrating digital tech across business operations", "Having a website", "Automation only"], "correct_answer": "Integrating digital tech across business operations", "explanation": "Digital transformation fundamentally changes how businesses operate and deliver value."},
                    {"id": "q2", "question": "Disruption occurs when:", "options": ["New entrants change market dynamics", "Prices increase", "Regulations change", "Nothing happens"], "correct_answer": "New entrants change market dynamics", "explanation": "Disruptive innovation creates new markets or transforms existing ones."},
                    {"id": "q3", "question": "Continuous learning is important because:", "options": ["Business environments change rapidly", "It's required by law", "It's easy", "It's optional"], "correct_answer": "Business environments change rapidly", "explanation": "Rapid change requires ongoing skill development."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand business trends", "Reflect on leadership", "Discuss ethical challenges", "Prepare for career"]
    },
    "con401": {
        "title": "Concentration Course 1",
        "topics": ["Specialized Topic 1", "Advanced Methods", "Industry Applications", "Case Studies", "Practitioner Insights"],
        "lessons": [
            {"id": "lesson_1", "topic": "Fundamentals", "title": "Concentration Fundamentals", "content": "Build foundation in your chosen concentration area.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Advanced", "title": "Advanced Techniques", "content": "Master advanced methods in your specialty.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Applications", "title": "Real-World Applications", "content": "Apply specialized knowledge to industry problems.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Specialization",
                "title": "Concentration Quiz",
                "questions": [
                    {"id": "q1", "question": "Choosing a concentration helps you:", "options": ["Graduate faster", "Develop deep expertise in a specific area", "Avoid difficult courses", "Take easier classes"], "correct_answer": "Develop deep expertise in a specific area", "explanation": "Concentrations build specialized expertise valued by employers."},
                    {"id": "q2", "question": "Industry-specific knowledge is valuable because:", "options": ["Employers seek specialized skills", "It's easier", "Everyone has it", "It's optional"], "correct_answer": "Employers seek specialized skills", "explanation": "Specialized skills differentiate candidates in competitive job markets."},
                    {"id": "q3", "question": "Applying theory to practice requires:", "options": ["Memorization only", "Critical thinking and adaptation", "Following formulas blindly", "Ignoring context"], "correct_answer": "Critical thinking and adaptation", "explanation": "Real problems require adapting principles to specific contexts."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Master concentration fundamentals", "Apply specialized methods", "Analyze industry cases", "Build professional expertise"]
    },
    "con402": {
        "title": "Concentration Course 2",
        "topics": ["Advanced Topics", "Research Methods", "Strategic Applications", "Innovation", "Professional Practice"],
        "lessons": [
            {"id": "lesson_1", "topic": "Advanced Topics", "title": "Deep Dive into Specialization", "content": "Explore complex topics in your concentration.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Research", "title": "Research and Analysis", "content": "Conduct research in your specialized area.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Innovation", "title": "Innovation in Practice", "content": "Apply innovative approaches to field challenges.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Advanced Specialization",
                "title": "Advanced Concentration Quiz",
                "questions": [
                    {"id": "q1", "question": "Advanced concentration courses prepare you for:", "options": ["Entry-level positions only", "Specialized roles requiring expertise", "General management", "Avoiding specialization"], "correct_answer": "Specialized roles requiring expertise", "explanation": "Advanced courses build expertise for specialized positions."},
                    {"id": "q2", "question": "Research skills in your field enable you to:", "options": ["Memorize facts", "Investigate complex problems independently", "Follow instructions only", "Avoid analysis"], "correct_answer": "Investigate complex problems independently", "explanation": "Research skills enable independent problem investigation."},
                    {"id": "q3", "question": "Staying current in your specialization requires:", "options": ["Only formal education", "Continuous learning from multiple sources", "One-time training", "No updates"], "correct_answer": "Continuous learning from multiple sources", "explanation": "Fields evolve; professionals must continuously update knowledge."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Master advanced specialized topics", "Conduct field research", "Innovate in practice", "Build professional credentials"]
    },
    "con403": {
        "title": "Concentration Course 3",
        "topics": ["Expert-Level Topics", "Capstone Applications", "Industry Standards", "Best Practices", "Thought Leadership"],
        "lessons": [
            {"id": "lesson_1", "topic": "Expertise", "title": "Expert-Level Knowledge", "content": "Achieve mastery in your concentration area.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Standards", "title": "Industry Standards and Best Practices", "content": "Learn professional standards and frameworks.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Leadership", "title": "Thought Leadership", "content": "Develop perspectives and contribute to your field.", "duration_minutes": 30, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Professional Mastery",
                "title": "Mastery Quiz",
                "questions": [
                    {"id": "q1", "question": "Professional mastery involves:", "options": ["Knowing basic facts", "Deep understanding and practical application", "Avoiding challenges", "Following scripts"], "correct_answer": "Deep understanding and practical application", "explanation": "Mastery combines deep knowledge with effective practice."},
                    {"id": "q2", "question": "Industry certifications demonstrate:", "options": ["Nothing useful", "Validated expertise and commitment", "Only theoretical knowledge", "Shortcuts"], "correct_answer": "Validated expertise and commitment", "explanation": "Certifications signal verified skills to employers."},
                    {"id": "q3", "question": "Contributing to your field can involve:", "options": ["Keeping knowledge secret", "Sharing insights and best practices", "Avoiding collaboration", "Working in isolation"], "correct_answer": "Sharing insights and best practices", "explanation": "Professionals advance their fields through knowledge sharing."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Achieve professional mastery", "Apply industry standards", "Demonstrate thought leadership", "Build specialized portfolio"]
    },
    "con404": {
        "title": "Concentration Course 4",
        "topics": ["Capstone Integration", "Advanced Projects", "Emerging Trends", "Professional Networks", "Career Launch"],
        "lessons": [
            {"id": "lesson_1", "topic": "Integration", "title": "Integrating Concentration Knowledge", "content": "Synthesize learning across concentration courses.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Trends", "title": "Future of the Field", "content": "Explore where your specialization is heading.", "duration_minutes": 30, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Launch", "title": "Launching Your Career", "content": "Apply expertise to secure specialized positions.", "duration_minutes": 30, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Career Specialization",
                "title": "Career Specialization Quiz",
                "questions": [
                    {"id": "q1", "question": "A specialized career path offers:", "options": ["Less earning potential", "Higher expertise and earning potential", "Fewer opportunities", "No advantages"], "correct_answer": "Higher expertise and earning potential", "explanation": "Specialization often commands premium compensation."},
                    {"id": "q2", "question": "Positioning yourself as an expert requires:", "options": ["A degree only", "Continuous learning and demonstrated results", "No effort", "Avoiding challenges"], "correct_answer": "Continuous learning and demonstrated results", "explanation": "Expertise comes from ongoing learning and proven accomplishments."},
                    {"id": "q3", "question": "Your professional brand should reflect:", "options": ["Someone else's identity", "Your unique expertise and values", "Generic qualities", "Nothing specific"], "correct_answer": "Your unique expertise and values", "explanation": "Authentic personal branding highlights distinctive strengths."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Synthesize concentration learning", "Understand field trends", "Launch specialized career", "Establish professional identity"]
    },
    "elec1": {
        "title": "Business Elective 1",
        "topics": ["Elective Topic", "Practical Skills", "Industry Insights", "Supplementary Knowledge", "Career Exploration"],
        "lessons": [
            {"id": "lesson_1", "topic": "Introduction", "title": "Elective Overview", "content": "Explore this business topic to broaden your knowledge.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Applications", "title": "Practical Applications", "content": "Apply elective concepts to business scenarios.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Elective Skills",
                "title": "Elective Quiz",
                "questions": [
                    {"id": "q1", "question": "Business electives allow you to:", "options": ["Graduate late", "Explore interests and round out skills", "Avoid core courses", "Reduce workload"], "correct_answer": "Explore interests and round out skills", "explanation": "Electives provide flexibility to explore interests and build complementary skills."},
                    {"id": "q2", "question": "Choosing electives strategically means:", "options": ["Taking easiest courses", "Aligning with career goals and filling skill gaps", "Random selection", "Avoiding new topics"], "correct_answer": "Aligning with career goals and filling skill gaps", "explanation": "Strategic elective choices enhance career readiness."},
                    {"id": "q3", "question": "Interdisciplinary knowledge is valuable because:", "options": ["Business problems span multiple domains", "It's trendy", "Employers require it", "It's easier"], "correct_answer": "Business problems span multiple domains", "explanation": "Complex business challenges require diverse perspectives."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Explore new business topics", "Apply elective knowledge", "Broaden skill set", "Enhance career flexibility"]
    },
    "elec2": {
        "title": "Business Elective 2",
        "topics": ["Supplementary Topic", "Cross-Functional Skills", "Industry Perspectives", "Professional Growth", "Knowledge Integration"],
        "lessons": [
            {"id": "lesson_1", "topic": "Topic Overview", "title": "Elective Focus", "content": "Study this business area to complement your major.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Integration", "title": "Integrating Knowledge", "content": "Connect elective concepts with core business knowledge.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Complementary Skills",
                "title": "Elective Skills Quiz",
                "questions": [
                    {"id": "q1", "question": "Complementary skills help you:", "options": ["Avoid your major", "Add value by bridging different areas", "Replace core knowledge", "Confuse employers"], "correct_answer": "Add value by bridging different areas", "explanation": "Complementary skills create unique value combinations."},
                    {"id": "q2", "question": "Cross-functional knowledge enables:", "options": ["Working only in one area", "Collaborating across business functions", "Avoiding teamwork", "Specialization only"], "correct_answer": "Collaborating across business functions", "explanation": "Cross-functional skills improve collaboration and problem-solving."},
                    {"id": "q3", "question": "A well-rounded business education includes:", "options": ["Only core courses", "Core courses plus diverse electives", "Only electives", "No specialization"], "correct_answer": "Core courses plus diverse electives", "explanation": "Balance between depth (core) and breadth (electives) is ideal."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Gain complementary knowledge", "Integrate cross-functional skills", "Expand career options", "Build versatile expertise"]
    },
    "elec3": {
        "title": "Business Elective 3",
        "topics": ["Advanced Elective Topic", "Specialized Applications", "Contemporary Issues", "Professional Development", "Skill Enhancement"],
        "lessons": [
            {"id": "lesson_1", "topic": "Advanced Topic", "title": "Advanced Elective Content", "content": "Deepen knowledge in this specialized business area.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Application", "title": "Advanced Applications", "content": "Apply advanced concepts to complex scenarios.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Advanced Business Topics",
                "title": "Advanced Elective Quiz",
                "questions": [
                    {"id": "q1", "question": "Advanced electives prepare you for:", "options": ["Basic roles", "Complex challenges requiring specialized knowledge", "Avoiding specialization", "Entry-level only"], "correct_answer": "Complex challenges requiring specialized knowledge", "explanation": "Advanced electives build capability for sophisticated problems."},
                    {"id": "q2", "question": "Specialized knowledge differentiates you by:", "options": ["Making you less employable", "Offering unique value in specific domains", "Limiting opportunities", "Reducing skills"], "correct_answer": "Offering unique value in specific domains", "explanation": "Specialization creates competitive advantage in target roles."},
                    {"id": "q3", "question": "Professional differentiation comes from:", "options": ["Following the crowd", "Unique combinations of skills and experience", "Avoiding challenges", "Generic knowledge"], "correct_answer": "Unique combinations of skills and experience", "explanation": "Distinctive skill combinations create unique professional value."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Master advanced elective topics", "Apply specialized methods", "Differentiate professionally", "Enhance career prospects"]
    },
    "elec4": {
        "title": "Business Elective 4",
        "topics": ["Final Elective Topic", "Comprehensive Applications", "Professional Readiness", "Portfolio Building", "Career Positioning"],
        "lessons": [
            {"id": "lesson_1", "topic": "Final Topic", "title": "Final Elective Focus", "content": "Complete your elective learning with this advanced topic.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Portfolio", "title": "Building Your Portfolio", "content": "Showcase your work and skills professionally.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Career Readiness",
                "title": "Career Readiness Quiz",
                "questions": [
                    {"id": "q1", "question": "A professional portfolio demonstrates:", "options": ["Only grades", "Your skills, projects, and achievements", "Nothing useful", "Just coursework"], "correct_answer": "Your skills, projects, and achievements", "explanation": "Portfolios provide tangible evidence of capabilities."},
                    {"id": "q2", "question": "Your final semester should focus on:", "options": ["Easy classes", "Career preparation and skill completion", "Avoiding work", "Starting over"], "correct_answer": "Career preparation and skill completion", "explanation": "Senior year should finalize skills and launch your career."},
                    {"id": "q3", "question": "A complete business education includes:", "options": ["Only major requirements", "Core, concentration, and breadth from electives", "Just electives", "Minimum credits"], "correct_answer": "Core, concentration, and breadth from electives", "explanation": "Balanced education combines depth and breadth."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Complete elective education", "Build professional portfolio", "Position for career success", "Demonstrate comprehensive skills"]
    },
    "elec5": {
        "title": "Business Elective 5",
        "topics": ["Final Specialization", "Advanced Practice", "Professional Integration", "Career Launch", "Lifelong Learning"],
        "lessons": [
            {"id": "lesson_1", "topic": "Final Learning", "title": "Final Elective Study", "content": "Complete your business education with this final elective.", "duration_minutes": 30, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Integration", "title": "Integrating All Learning", "content": "Connect all your business knowledge into a cohesive whole.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Education Completion",
                "title": "Final Elective Quiz",
                "questions": [
                    {"id": "q1", "question": "As you complete your degree, you should:", "options": ["Stop learning", "Commit to lifelong learning", "Forget coursework", "Avoid challenges"], "correct_answer": "Commit to lifelong learning", "explanation": "Education continues throughout your career."},
                    {"id": "q2", "question": "Your business education provides:", "options": ["All answers", "Foundational knowledge to build upon", "No practical value", "Only theory"], "correct_answer": "Foundational knowledge to build upon", "explanation": "Formal education provides a foundation for continued growth."},
                    {"id": "q3", "question": "Successful business careers require:", "options": ["Degree only", "Continuous adaptation and learning", "No further development", "Staying the same"], "correct_answer": "Continuous adaptation and learning", "explanation": "Business environments change; careers require ongoing development."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Complete business education", "Integrate all learning", "Launch professional career", "Commit to continued growth"]
    },
    "engr301": {
        "title": "Engineering Design I",
        "topics": ["Design Process", "Requirements Engineering", "Concept Generation", "Design Analysis", "Prototyping"],
        "lessons": [
            {"id": "lesson_1", "topic": "Design Process", "title": "Engineering Design Methodology", "content": "Learn systematic design processes from problem to solution.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Requirements", "title": "Requirements and Constraints", "content": "Define technical requirements and constraints.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Prototyping", "title": "Prototyping and Testing", "content": "Build and test design prototypes.", "duration_minutes": 40, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Design Methodology",
                "title": "Design Process Quiz",
                "questions": [
                    {"id": "q1", "question": "The engineering design process typically includes:", "options": ["Define, Research, Ideate, Prototype, Test, Refine", "Just build it", "Copy existing designs", "Skip testing"], "correct_answer": "Define, Research, Ideate, Prototype, Test, Refine", "explanation": "Systematic design follows iterative steps from problem to solution."},
                    {"id": "q2", "question": "Design constraints include:", "options": ["Unlimited resources", "Technical, economic, and regulatory limits", "No limits", "Only cost"], "correct_answer": "Technical, economic, and regulatory limits", "explanation": "Real designs must satisfy multiple constraints."},
                    {"id": "q3", "question": "Prototypes are important because they:", "options": ["Are final products", "Test ideas before full-scale production", "Are decorative", "Waste resources"], "correct_answer": "Test ideas before full-scale production", "explanation": "Prototypes validate designs and identify issues early."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Apply design methodology", "Define requirements", "Generate design concepts", "Build and test prototypes"]
    },
    "engr302": {
        "title": "Engineering Design II",
        "topics": ["Detailed Design", "Manufacturing Considerations", "Design Optimization", "Safety Analysis", "Documentation"],
        "lessons": [
            {"id": "lesson_1", "topic": "Detailed Design", "title": "Design Specifications", "content": "Create detailed drawings and specifications.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Manufacturing", "title": "Design for Manufacturing", "content": "Design products that can be manufactured efficiently.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Documentation", "title": "Engineering Documentation", "content": "Create comprehensive technical documentation.", "duration_minutes": 30, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Detailed Design",
                "title": "Design Refinement Quiz",
                "questions": [
                    {"id": "q1", "question": "Detailed design includes:", "options": ["Rough sketches only", "Precise specifications and drawings", "Ideas only", "Marketing plans"], "correct_answer": "Precise specifications and drawings", "explanation": "Detailed design provides complete manufacturing information."},
                    {"id": "q2", "question": "Design for manufacturing (DFM) aims to:", "options": ["Complicate production", "Simplify manufacturing and reduce costs", "Ignore production", "Maximize complexity"], "correct_answer": "Simplify manufacturing and reduce costs", "explanation": "DFM makes designs easier and cheaper to produce."},
                    {"id": "q3", "question": "Safety factors in design:", "options": ["Reduce strength unnecessarily", "Account for uncertainties and ensure reliability", "Are always 1.0", "Don't matter"], "correct_answer": "Account for uncertainties and ensure reliability", "explanation": "Safety factors provide margin against failures and uncertainties."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Create detailed designs", "Apply DFM principles", "Optimize designs", "Document engineering work"]
    },
    "engr310": {
        "title": "Engineering Economics",
        "topics": ["Time Value of Money", "Cost Estimation", "Project Evaluation", "Depreciation", "Economic Decision Making"],
        "lessons": [
            {"id": "lesson_1", "topic": "TVM", "title": "Engineering Economic Analysis", "content": "Apply time value of money to engineering projects.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Evaluation", "title": "Project Evaluation Methods", "content": "Compare alternatives using NPV, IRR, and benefit-cost analysis.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Costs", "title": "Cost Estimation", "content": "Estimate and control engineering project costs.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Engineering Economics",
                "title": "Engineering Economics Quiz",
                "questions": [
                    {"id": "q1", "question": "Engineering economic analysis helps:", "options": ["Ignore costs", "Make financially sound engineering decisions", "Maximize complexity", "Avoid projects"], "correct_answer": "Make financially sound engineering decisions", "explanation": "Economic analysis ensures projects are financially viable."},
                    {"id": "q2", "question": "NPV > 0 indicates a project:", "options": ["Loses money", "Adds value", "Breaks even", "Is too risky"], "correct_answer": "Adds value", "explanation": "Positive NPV means the project creates value."},
                    {"id": "q3", "question": "Depreciation accounts for:", "options": ["Asset value decline over time", "Inflation only", "Maintenance costs", "Operating expenses"], "correct_answer": "Asset value decline over time", "explanation": "Depreciation allocates asset costs over useful life."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Apply engineering economics", "Evaluate projects financially", "Estimate costs", "Make economic decisions"]
    },
    "engr320": {
        "title": "Systems Engineering",
        "topics": ["Systems Thinking", "Requirements Engineering", "System Architecture", "Integration", "Verification and Validation"],
        "lessons": [
            {"id": "lesson_1", "topic": "Systems Thinking", "title": "Introduction to Systems", "content": "Understand complex systems and their interactions.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Architecture", "title": "System Architecture Design", "content": "Design system architectures and interfaces.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "V&V", "title": "Verification and Validation", "content": "Ensure systems meet requirements and user needs.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Systems Engineering",
                "title": "Systems Engineering Quiz",
                "questions": [
                    {"id": "q1", "question": "Systems engineering focuses on:", "options": ["Individual components only", "Holistic design and integration of complex systems", "Only software", "Only hardware"], "correct_answer": "Holistic design and integration of complex systems", "explanation": "Systems engineering considers the whole system lifecycle."},
                    {"id": "q2", "question": "Verification asks:", "options": ["Are we building it right?", "Are we building the right thing?", "Is it profitable?", "Is it fast?"], "correct_answer": "Are we building it right?", "explanation": "Verification checks if the system meets specifications."},
                    {"id": "q3", "question": "Validation asks:", "options": ["Are we building it right?", "Are we building the right thing?", "Is it cheap?", "Is it simple?"], "correct_answer": "Are we building the right thing?", "explanation": "Validation ensures the system meets user needs."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Apply systems thinking", "Design system architectures", "Manage system integration", "Perform V&V"]
    },
    "engr401": {
        "title": "Senior Capstone Project I",
        "topics": ["Project Definition", "Design and Analysis", "Teamwork", "Budget and Schedule", "Progress Reporting"],
        "lessons": [
            {"id": "lesson_1", "topic": "Definition", "title": "Defining Your Project", "content": "Identify and scope your capstone engineering project.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Design", "title": "Preliminary Design", "content": "Develop initial design concepts and analysis.", "duration_minutes": 45, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Management", "title": "Project Management", "content": "Manage timeline, budget, and team dynamics.", "duration_minutes": 30, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Capstone Projects",
                "title": "Engineering Capstone Quiz",
                "questions": [
                    {"id": "q1", "question": "A capstone project demonstrates:", "options": ["Memorization", "Integration of engineering knowledge and skills", "One topic only", "Basic concepts"], "correct_answer": "Integration of engineering knowledge and skills", "explanation": "Capstones synthesize learning across the curriculum."},
                    {"id": "q2", "question": "Effective team projects require:", "options": ["No communication", "Clear roles and regular communication", "One person doing all work", "Avoiding conflict"], "correct_answer": "Clear roles and regular communication", "explanation": "Successful teams have defined responsibilities and communicate well."},
                    {"id": "q3", "question": "Project documentation is important for:", "options": ["Wasting time", "Tracking progress and communicating results", "Avoiding work", "Decoration"], "correct_answer": "Tracking progress and communicating results", "explanation": "Documentation maintains project knowledge and communicates outcomes."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Define engineering projects", "Apply design methods", "Work in teams", "Manage projects"]
    },
    "engr402": {
        "title": "Senior Capstone Project II",
        "topics": ["Detailed Implementation", "Testing and Validation", "Final Presentation", "Technical Documentation", "Deployment"],
        "lessons": [
            {"id": "lesson_1", "topic": "Implementation", "title": "Building Your Design", "content": "Implement and refine your engineering solution.", "duration_minutes": 45, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Testing", "title": "Testing and Validation", "content": "Verify your design meets all requirements.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Presentation", "title": "Final Presentation", "content": "Present your project to faculty and industry professionals.", "duration_minutes": 30, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Project Completion",
                "title": "Capstone Completion Quiz",
                "questions": [
                    {"id": "q1", "question": "Testing validates that your design:", "options": ["Looks good", "Meets requirements and works correctly", "Is expensive", "Is simple"], "correct_answer": "Meets requirements and works correctly", "explanation": "Testing ensures functional and performance requirements are met."},
                    {"id": "q2", "question": "Technical presentations should:", "options": ["Include every detail", "Clearly communicate key results and significance", "Be overly complex", "Avoid visuals"], "correct_answer": "Clearly communicate key results and significance", "explanation": "Effective presentations convey essential information clearly."},
                    {"id": "q3", "question": "A complete capstone project includes:", "options": ["Just a working prototype", "Design, implementation, testing, and documentation", "Only documentation", "Concept only"], "correct_answer": "Design, implementation, testing, and documentation", "explanation": "Complete projects include all engineering deliverables."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Complete engineering project", "Validate designs", "Present technical work", "Deliver professional documentation"]
    },
    "engr410": {
        "title": "Engineering Ethics",
        "topics": ["Professional Responsibility", "Safety and Risk", "Sustainability", "Codes of Ethics", "Case Studies"],
        "lessons": [
            {"id": "lesson_1", "topic": "Responsibility", "title": "Engineering Professional Responsibility", "content": "Understand engineers' obligations to public safety.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Safety", "title": "Safety and Risk Management", "content": "Analyze risks and design for safety.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Sustainability", "title": "Sustainable Engineering", "content": "Design with environmental and social sustainability.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Engineering Ethics",
                "title": "Engineering Ethics Quiz",
                "questions": [
                    {"id": "q1", "question": "Engineers' primary obligation is to:", "options": ["Maximize profit", "Protect public safety, health, and welfare", "Follow orders blindly", "Avoid decisions"], "correct_answer": "Protect public safety, health, and welfare", "explanation": "Engineers hold paramount the safety and welfare of the public."},
                    {"id": "q2", "question": "Whistleblowing may be necessary when:", "options": ["You disagree with a manager", "Public safety is endangered and internal channels fail", "You want attention", "Projects are delayed"], "correct_answer": "Public safety is endangered and internal channels fail", "explanation": "Whistleblowing is a last resort to prevent serious harm."},
                    {"id": "q3", "question": "Sustainable design considers:", "options": ["Only initial cost", "Environmental, social, and economic impacts", "Only aesthetics", "Short-term gains"], "correct_answer": "Environmental, social, and economic impacts", "explanation": "Sustainability balances economic, environmental, and social goals."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand professional obligations", "Analyze ethical dilemmas", "Apply sustainability principles", "Uphold engineering standards"]
    },
    "engr420": {
        "title": "Engineering Management",
        "topics": ["Project Management", "Team Leadership", "Resource Allocation", "Risk Management", "Quality Management"],
        "lessons": [
            {"id": "lesson_1", "topic": "PM Basics", "title": "Engineering Project Management", "content": "Manage technical projects with schedules and budgets.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Leadership", "title": "Technical Team Leadership", "content": "Lead engineers and manage technical teams.", "duration_minutes": 30, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Quality", "title": "Quality Management Systems", "content": "Implement quality assurance in engineering.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Engineering Management",
                "title": "Engineering Management Quiz",
                "questions": [
                    {"id": "q1", "question": "Engineering project management requires:", "options": ["Only technical skills", "Both technical and managerial skills", "Only people skills", "No planning"], "correct_answer": "Both technical and managerial skills", "explanation": "Technical project management combines engineering and management expertise."},
                    {"id": "q2", "question": "Critical path in project scheduling is:", "options": ["Shortest path", "Longest sequence of dependent tasks", "Most expensive path", "Easiest path"], "correct_answer": "Longest sequence of dependent tasks", "explanation": "Critical path determines minimum project duration."},
                    {"id": "q3", "question": "Risk management in engineering involves:", "options": ["Ignoring risks", "Identifying, assessing, and mitigating risks", "Taking maximum risks", "Avoiding all projects"], "correct_answer": "Identifying, assessing, and mitigating risks", "explanation": "Risk management systematically addresses project uncertainties."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Manage engineering projects", "Lead technical teams", "Control costs and schedules", "Manage quality and risk"]
    },
    "engr430": {
        "title": "Professional Practice",
        "topics": ["Licensure", "Contracts", "Professional Conduct", "Career Development", "Continuing Education"],
        "lessons": [
            {"id": "lesson_1", "topic": "Licensure", "title": "Professional Engineering License", "content": "Understand the path to PE licensure and its importance.", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Contracts", "title": "Engineering Contracts", "content": "Navigate contracts, liability, and legal issues.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_3", "topic": "Career", "title": "Engineering Career Development", "content": "Plan your engineering career and continued growth.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Professional Practice",
                "title": "Professional Practice Quiz",
                "questions": [
                    {"id": "q1", "question": "A Professional Engineer (PE) license:", "options": ["Is optional and unimportant", "Allows independent practice and stamping plans", "Is only for managers", "Has no benefits"], "correct_answer": "Allows independent practice and stamping plans", "explanation": "PE license authorizes independent practice and approval of engineering work."},
                    {"id": "q2", "question": "Engineers must maintain competence through:", "options": ["Initial degree only", "Continuing education and professional development", "Avoiding new topics", "Staying the same"], "correct_answer": "Continuing education and professional development", "explanation": "Professional practice requires staying current with technology."},
                    {"id": "q3", "question": "Professional liability means engineers:", "options": ["Have no responsibility", "Can be held liable for negligent work", "Are never sued", "Can ignore standards"], "correct_answer": "Can be held liable for negligent work", "explanation": "Engineers are professionally responsible for their work quality."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Understand licensure", "Navigate professional obligations", "Manage legal issues", "Plan engineering career"]
    },
    "spec301": {
        "title": "Specialization Course 1",
        "topics": ["Specialization Fundamentals", "Technical Depth", "Industry Applications", "Design Projects", "Analysis Methods"],
        "lessons": [
            {"id": "lesson_1", "topic": "Fundamentals", "title": "Specialization Basics", "content": "Build foundation in your engineering specialization.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Applications", "title": "Industry Applications", "content": "Apply specialized knowledge to real problems.", "duration_minutes": 40, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Engineering Specialization",
                "title": "Specialization Quiz",
                "questions": [
                    {"id": "q1", "question": "Engineering specializations allow you to:", "options": ["Avoid math", "Develop expertise in specific engineering domains", "Graduate faster", "Take easier classes"], "correct_answer": "Develop expertise in specific engineering domains", "explanation": "Specializations build deep knowledge in areas like mechanical, electrical, civil, etc."},
                    {"id": "q2", "question": "Specialized engineers are valuable because:", "options": ["They know everything", "They solve domain-specific technical challenges", "They work alone", "They avoid complexity"], "correct_answer": "They solve domain-specific technical challenges", "explanation": "Specialists provide deep expertise for complex technical problems."},
                    {"id": "q3", "question": "Your specialization should align with:", "options": ["What's easiest", "Your interests and career goals", "What friends choose", "Random selection"], "correct_answer": "Your interests and career goals", "explanation": "Specialization should match your passion and career direction."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Master specialization basics", "Apply specialized methods", "Solve domain problems", "Build technical depth"]
    },
    "spec302": {
        "title": "Specialization Course 2",
        "topics": ["Advanced Specialization", "Design Techniques", "Analysis Tools", "Professional Standards", "Industry Practice"],
        "lessons": [
            {"id": "lesson_1", "topic": "Advanced Topics", "title": "Advanced Specialization Topics", "content": "Deepen expertise in your engineering specialty.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Tools", "title": "Specialized Tools and Software", "content": "Master industry-standard analysis and design tools.", "duration_minutes": 40, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Advanced Specialization",
                "title": "Advanced Specialization Quiz",
                "questions": [
                    {"id": "q1", "question": "Advanced specialization courses:", "options": ["Cover only basics", "Build expert-level technical knowledge", "Are optional", "Don't matter"], "correct_answer": "Build expert-level technical knowledge", "explanation": "Advanced courses develop professional-level expertise."},
                    {"id": "q2", "question": "Industry-standard tools are important because:", "options": ["Employers expect proficiency", "They're trendy", "They're easy", "They're optional"], "correct_answer": "Employers expect proficiency", "explanation": "Professionals must use standard industry tools."},
                    {"id": "q3", "question": "Specialization depth prepares you for:", "options": ["General engineering roles only", "Advanced technical positions and responsibility", "Management only", "Basic tasks"], "correct_answer": "Advanced technical positions and responsibility", "explanation": "Deep expertise enables handling complex technical challenges."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Master advanced specialized topics", "Use professional tools", "Apply industry standards", "Build expert knowledge"]
    },
    "spec303": {
        "title": "Specialization Course 3",
        "topics": ["Specialized Design", "System Integration", "Performance Optimization", "Research Methods", "Innovation"],
        "lessons": [
            {"id": "lesson_1", "topic": "Design", "title": "Specialized Design Methods", "content": "Apply advanced design techniques in your specialty.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Optimization", "title": "System Optimization", "content": "Optimize performance of specialized systems.", "duration_minutes": 40, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Specialized Design",
                "title": "Specialized Design Quiz",
                "questions": [
                    {"id": "q1", "question": "Optimization in engineering seeks to:", "options": ["Maximize or minimize objectives subject to constraints", "Ignore trade-offs", "Use trial and error only", "Avoid analysis"], "correct_answer": "Maximize or minimize objectives subject to constraints", "explanation": "Engineering optimization balances competing objectives and constraints."},
                    {"id": "q2", "question": "System integration challenges include:", "options": ["Everything works perfectly", "Interface compatibility and performance trade-offs", "No issues", "Simple assembly"], "correct_answer": "Interface compatibility and performance trade-offs", "explanation": "Integration requires managing interfaces and system-level performance."},
                    {"id": "q3", "question": "Innovation in specialized fields requires:", "options": ["Following old methods only", "Deep knowledge plus creative problem-solving", "Avoiding risks", "Random guessing"], "correct_answer": "Deep knowledge plus creative problem-solving", "explanation": "Innovation combines expertise with creative approaches."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Apply specialized design methods", "Optimize systems", "Integrate components", "Innovate in specialty"]
    },
    "spec304": {
        "title": "Specialization Lab",
        "topics": ["Experimental Methods", "Instrumentation", "Data Acquisition", "Analysis and Reporting", "Lab Safety"],
        "lessons": [
            {"id": "lesson_1", "topic": "Experiments", "title": "Experimental Design", "content": "Design and conduct engineering experiments.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Instrumentation", "title": "Measurement Systems", "content": "Use sensors and instruments for data acquisition.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_3", "topic": "Analysis", "title": "Experimental Data Analysis", "content": "Analyze experimental data and report results.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Laboratory Skills",
                "title": "Lab Skills Quiz",
                "questions": [
                    {"id": "q1", "question": "Experimental design aims to:", "options": ["Waste resources", "Test hypotheses systematically", "Avoid data", "Guess results"], "correct_answer": "Test hypotheses systematically", "explanation": "Experiments test hypotheses through controlled observations."},
                    {"id": "q2", "question": "Measurement uncertainty arises from:", "options": ["Perfect instruments", "Instrument limitations and random variations", "No factors", "Operator perfection"], "correct_answer": "Instrument limitations and random variations", "explanation": "All measurements have uncertainty from various sources."},
                    {"id": "q3", "question": "Lab safety is important because:", "options": ["Regulations require it", "Prevents injuries and protects researchers", "It's optional", "It slows work"], "correct_answer": "Prevents injuries and protects researchers", "explanation": "Safety protocols protect people and facilities."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Design experiments", "Use instrumentation", "Analyze experimental data", "Follow safety protocols"]
    },
    "spec401": {
        "title": "Advanced Specialization Course",
        "topics": ["Cutting-Edge Topics", "Advanced Research", "Industry Trends", "Innovation", "Professional Expertise"],
        "lessons": [
            {"id": "lesson_1", "topic": "Advanced Topics", "title": "State of the Art", "content": "Study cutting-edge developments in your specialization.", "duration_minutes": 40, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Research", "title": "Research Methods", "content": "Conduct advanced research in your specialty.", "duration_minutes": 40, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Advanced Expertise",
                "title": "Advanced Specialization Quiz",
                "questions": [
                    {"id": "q1", "question": "Advanced specialization prepares you for:", "options": ["Entry-level roles only", "Technical leadership and expert positions", "Non-technical roles", "Basic tasks"], "correct_answer": "Technical leadership and expert positions", "explanation": "Advanced study builds expertise for leadership and specialized roles."},
                    {"id": "q2", "question": "Staying current with field developments requires:", "options": ["No effort", "Reading journals, attending conferences, networking", "Only textbooks", "Avoiding new information"], "correct_answer": "Reading journals, attending conferences, networking", "explanation": "Professionals stay current through multiple channels."},
                    {"id": "q3", "question": "Contributing to engineering knowledge includes:", "options": ["Hoarding information", "Publishing research and sharing innovations", "Avoiding collaboration", "Keeping secrets"], "correct_answer": "Publishing research and sharing innovations", "explanation": "Engineers advance their fields by sharing knowledge."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Master advanced specialization", "Conduct research", "Understand field trends", "Build expert credentials"]
    },
    "elec401": {
        "title": "Technical Elective",
        "topics": ["Elective Topic", "Technical Applications", "Industry Practices", "Skill Enhancement", "Career Options"],
        "lessons": [
            {"id": "lesson_1", "topic": "Topic Overview", "title": "Elective Introduction", "content": "Explore this technical elective to broaden your engineering knowledge.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Applications", "title": "Technical Applications", "content": "Apply elective concepts to engineering problems.", "duration_minutes": 35, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Technical Breadth",
                "title": "Technical Elective Quiz",
                "questions": [
                    {"id": "q1", "question": "Technical electives provide:", "options": ["Reduced workload", "Breadth beyond your specialization", "Duplicate knowledge", "No value"], "correct_answer": "Breadth beyond your specialization", "explanation": "Electives broaden technical knowledge beyond core specialization."},
                    {"id": "q2", "question": "Interdisciplinary engineering knowledge helps with:", "options": ["Complex systems spanning multiple domains", "Simple single-discipline problems only", "Avoiding teamwork", "Nothing"], "correct_answer": "Complex systems spanning multiple domains", "explanation": "Modern systems often require interdisciplinary expertise."},
                    {"id": "q3", "question": "Career flexibility comes from:", "options": ["Narrow focus only", "Combination of depth and breadth", "Avoiding specialization", "Generic knowledge"], "correct_answer": "Combination of depth and breadth", "explanation": "Both specialization depth and breadth create career flexibility."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Explore technical topics", "Broaden engineering knowledge", "Apply diverse methods", "Enhance career versatility"]
    },
    "elec402": {
        "title": "Final Technical Elective",
        "topics": ["Advanced Elective Topic", "Professional Integration", "Career Preparation", "Portfolio Enhancement", "Lifelong Learning"],
        "lessons": [
            {"id": "lesson_1", "topic": "Advanced Content", "title": "Final Elective Study", "content": "Complete your technical education with this final elective.", "duration_minutes": 35, "difficulty": "advanced"},
            {"id": "lesson_2", "topic": "Integration", "title": "Knowledge Integration", "content": "Integrate all engineering knowledge for professional practice.", "duration_minutes": 30, "difficulty": "advanced"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Engineering Completion",
                "title": "Final Elective Quiz",
                "questions": [
                    {"id": "q1", "question": "Your engineering education provides:", "options": ["All answers for your career", "Foundation for continued professional growth", "Only theoretical knowledge", "No practical value"], "correct_answer": "Foundation for continued professional growth", "explanation": "Education provides a base; careers require ongoing learning."},
                    {"id": "q2", "question": "As technology evolves, engineers must:", "options": ["Stop learning after graduation", "Continuously update knowledge and skills", "Rely only on past education", "Avoid new developments"], "correct_answer": "Continuously update knowledge and skills", "explanation": "Rapid technological change requires lifelong learning."},
                    {"id": "q3", "question": "A successful engineering career requires:", "options": ["Degree only", "Technical skills, communication, and continuous learning", "Avoiding challenges", "Working alone always"], "correct_answer": "Technical skills, communication, and continuous learning", "explanation": "Professional success combines technical expertise with soft skills and growth mindset."}
                ],
                "passing_score": 70,
                "difficulty": "advanced"
            }
        ],
        "learning_outcomes": ["Complete technical education", "Integrate engineering knowledge", "Prepare for professional practice", "Commit to lifelong learning"]
    }
}


def get_course_content(course_id: str) -> dict | None:
    """Get learning content for a specific course"""
    return COURSE_CONTENT.get(course_id.lower())


def get_course_lessons(course_id: str) -> List[Dict]:
    """Get all lessons for a course"""
    content = get_course_content(course_id)
    return content["lessons"] if content else []


def get_course_quizzes(course_id: str) -> List[Dict]:
    """Get all quizzes for a course"""
    content = get_course_content(course_id)
    return content["quizzes"] if content else []


def get_lesson(course_id: str, lesson_id: str) -> Dict | None:
    """Get a specific lesson"""
    content = get_course_content(course_id)
    if not content:
        return None
    for lesson in content["lessons"]:
        if lesson["id"] == lesson_id:
            return lesson
    return None


def get_quiz(course_id: str, quiz_id: str) -> Dict | None:
    """Get a specific quiz"""
    content = get_course_content(course_id)
    if not content:
        return None
    for quiz in content["quizzes"]:
        if quiz["id"] == quiz_id:
            return quiz
    return None
