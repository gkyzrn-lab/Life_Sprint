#!/usr/bin/env python3
"""
Generate comprehensive course content for all courses in the curriculum.
This script creates quiz content for all courses that don't already have content.
"""

# All courses that need content (excluding already done: cs101, ba101, cs102, bus101, econ101, math141, eng101, cs201)
COURSES_TO_ADD = {
    "math142": {
        "title": "Calculus II",
        "topics": ["Integration Techniques", "Applications of Integration", "Sequences and Series", "Taylor Series"],
        "lessons": [
            {"id": "lesson_1", "topic": "Integration", "title": "Integration Methods", "content": "Master integration by substitution, parts, and partial fractions.", "duration_minutes": 35, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Applications", "title": "Volume and Arc Length", "content": "Calculate volumes of revolution and arc lengths using integration.", "duration_minutes": 30, "difficulty": "high"},
            {"id": "lesson_3", "topic": "Series", "title": "Infinite Series", "content": "Understand convergence tests and power series.", "duration_minutes": 40, "difficulty": "very_high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Integration",
                "title": "Integration Techniques",
                "questions": [
                    {"id": "q1", "question": "What is the integral of 1/x?", "options": ["x²/2", "ln|x| + C", "1/x² + C", "e^x + C"], "correct_answer": "ln|x| + C", "explanation": "The antiderivative of 1/x is the natural logarithm ln|x| plus a constant."},
                    {"id": "q2", "question": "Which technique works best for ∫x·e^x dx?", "options": ["Substitution", "Integration by parts", "Partial fractions", "Direct integration"], "correct_answer": "Integration by parts", "explanation": "Integration by parts is ideal when you have a product of functions like x and e^x."},
                    {"id": "q3", "question": "What does a definite integral represent?", "options": ["The derivative", "The area under a curve", "The slope", "The limit"], "correct_answer": "The area under a curve", "explanation": "A definite integral calculates the signed area between the curve and the x-axis."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Master integration techniques", "Apply integrals to real-world problems", "Analyze series convergence", "Work with Taylor series"]
    },
    "cs203": {
        "title": "Algorithms",
        "topics": ["Algorithm Analysis", "Sorting Algorithms", "Graph Algorithms", "Dynamic Programming", "Greedy Algorithms"],
        "lessons": [
            {"id": "lesson_1", "topic": "Analysis", "title": "Big O Notation", "content": "Learn to analyze algorithm time and space complexity.", "duration_minutes": 30, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Sorting", "title": "Sorting Algorithms", "content": "Compare QuickSort, MergeSort, and HeapSort.", "duration_minutes": 35, "difficulty": "high"},
            {"id": "lesson_3", "topic": "Dynamic Programming", "title": "DP Fundamentals", "content": "Master dynamic programming techniques for optimization problems.", "duration_minutes": 45, "difficulty": "very_high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Algorithms",
                "title": "Algorithm Fundamentals",
                "questions": [
                    {"id": "q1", "question": "What is the best case time complexity of QuickSort?", "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"], "correct_answer": "O(n log n)", "explanation": "QuickSort achieves O(n log n) in the best and average cases when the pivot divides the array evenly."},
                    {"id": "q2", "question": "What is the key principle of dynamic programming?", "options": ["Divide and conquer", "Storing results of subproblems to avoid recomputation", "Using random pivots", "Sorting first"], "correct_answer": "Storing results of subproblems to avoid recomputation", "explanation": "Dynamic programming stores (memoizes) solutions to subproblems to avoid redundant calculations."},
                    {"id": "q3", "question": "What is Dijkstra's algorithm used for?", "options": ["Sorting arrays", "Finding shortest paths in weighted graphs", "Searching binary trees", "Matrix multiplication"], "correct_answer": "Finding shortest paths in weighted graphs", "explanation": "Dijkstra's algorithm finds the shortest path from a source to all other vertices in a weighted graph."}
                ],
                "passing_score": 70,
                "difficulty": "very_high"
            }
        ],
        "learning_outcomes": ["Analyze algorithm complexity", "Implement classic algorithms", "Solve optimization problems", "Choose appropriate algorithms for problems"]
    },
    "cs210": {
        "title": "Computer Organization",
        "topics": ["Computer Architecture", "Assembly Language", "CPU Design", "Memory Hierarchy", "I/O Systems"],
        "lessons": [
            {"id": "lesson_1", "topic": "Architecture", "title": "Von Neumann Architecture", "content": "Understand how computers are organized at the hardware level.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Assembly", "title": "Assembly Programming", "content": "Learn to program in assembly language.", "duration_minutes": 40, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Computer Architecture",
                "title": "Architecture Basics",
                "questions": [
                    {"id": "q1", "question": "What does CPU stand for?", "options": ["Central Processing Unit", "Computer Processing Unit", "Central Program Unit", "Core Processing Unit"], "correct_answer": "Central Processing Unit", "explanation": "CPU stands for Central Processing Unit, the brain of the computer."},
                    {"id": "q2", "question": "What is cache memory?", "options": ["Main memory", "Fast memory close to the CPU", "Disk storage", "Virtual memory"], "correct_answer": "Fast memory close to the CPU", "explanation": "Cache is small, fast memory near the CPU that stores frequently accessed data."},
                    {"id": "q3", "question": "What is the purpose of the ALU?", "options": ["Store data", "Perform arithmetic and logical operations", "Manage I/O", "Control program flow"], "correct_answer": "Perform arithmetic and logical operations", "explanation": "The ALU (Arithmetic Logic Unit) performs mathematical and logical operations."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand computer architecture", "Program in assembly language", "Analyze CPU performance", "Optimize code for hardware"]
    },
    "stat200": {
        "title": "Probability & Statistics",
        "topics": ["Probability Theory", "Random Variables", "Distributions", "Statistical Inference", "Hypothesis Testing"],
        "lessons": [
            {"id": "lesson_1", "topic": "Probability", "title": "Probability Fundamentals", "content": "Master probability rules and conditional probability.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Distributions", "title": "Probability Distributions", "content": "Learn normal, binomial, and Poisson distributions.", "duration_minutes": 35, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Probability",
                "title": "Probability Quiz",
                "questions": [
                    {"id": "q1", "question": "What is the probability of flipping heads on a fair coin?", "options": ["0.25", "0.5", "0.75", "1.0"], "correct_answer": "0.5", "explanation": "A fair coin has two equally likely outcomes, so P(heads) = 1/2 = 0.5."},
                    {"id": "q2", "question": "What does the Central Limit Theorem state?", "options": ["All distributions are normal", "Sample means approach a normal distribution as sample size increases", "Probability always equals 0.5", "Standard deviation equals the mean"], "correct_answer": "Sample means approach a normal distribution as sample size increases", "explanation": "The CLT states that the distribution of sample means becomes approximately normal as the sample size grows, regardless of the original distribution."},
                    {"id": "q3", "question": "What is a p-value?", "options": ["The probability the null hypothesis is true", "The probability of observing data as extreme as yours if the null hypothesis is true", "The probability of making an error", "The population mean"], "correct_answer": "The probability of observing data as extreme as yours if the null hypothesis is true", "explanation": "A p-value measures how likely your observed data is, assuming the null hypothesis is true."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Calculate probabilities", "Work with probability distributions", "Conduct hypothesis tests", "Make statistical inferences"]
    },
    "cs220": {
        "title": "Operating Systems",
        "topics": ["Processes and Threads", "CPU Scheduling", "Memory Management", "File Systems", "Synchronization"],
        "lessons": [
            {"id": "lesson_1", "topic": "Processes", "title": "Process Management", "content": "Understand process creation, scheduling, and termination.", "duration_minutes": 35, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Memory", "title": "Memory Management", "content": "Learn about paging, segmentation, and virtual memory.", "duration_minutes": 40, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Operating Systems",
                "title": "OS Fundamentals",
                "questions": [
                    {"id": "q1", "question": "What is a process?", "options": ["A program on disk", "A program in execution", "A CPU instruction", "A memory address"], "correct_answer": "A program in execution", "explanation": "A process is an instance of a program that is being executed by the CPU."},
                    {"id": "q2", "question": "What is a context switch?", "options": ["Changing programs", "Saving and restoring CPU state when switching processes", "Moving data to disk", "Updating memory"], "correct_answer": "Saving and restoring CPU state when switching processes", "explanation": "A context switch saves the state of one process and restores another, allowing multitasking."},
                    {"id": "q3", "question": "What problem do semaphores solve?", "options": ["CPU scheduling", "Synchronization between processes/threads", "Memory allocation", "File I/O"], "correct_answer": "Synchronization between processes/threads", "explanation": "Semaphores are synchronization primitives used to control access to shared resources and prevent race conditions."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Understand OS concepts", "Implement process synchronization", "Analyze scheduling algorithms", "Manage memory efficiently"]
    },
    "cs225": {
        "title": "Database Systems",
        "topics": ["Relational Model", "SQL", "Database Design", "Normalization", "Transactions"],
        "lessons": [
            {"id": "lesson_1", "topic": "SQL", "title": "SQL Fundamentals", "content": "Master SELECT, JOIN, INSERT, UPDATE, and DELETE queries.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Design", "title": "Database Design", "content": "Learn entity-relationship modeling and normalization.", "duration_minutes": 35, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Database Systems",
                "title": "Database Quiz",
                "questions": [
                    {"id": "q1", "question": "What does SQL stand for?", "options": ["Structured Query Language", "Simple Query Language", "Standard Query Language", "System Query Language"], "correct_answer": "Structured Query Language", "explanation": "SQL stands for Structured Query Language, used to interact with relational databases."},
                    {"id": "q2", "question": "What is a primary key?", "options": ["The first column in a table", "A unique identifier for each row", "A foreign key reference", "An index"], "correct_answer": "A unique identifier for each row", "explanation": "A primary key uniquely identifies each row in a table and cannot be null."},
                    {"id": "q3", "question": "What does normalization achieve?", "options": ["Faster queries", "Reducing data redundancy and improving integrity", "Larger database size", "Simpler queries"], "correct_answer": "Reducing data redundancy and improving integrity", "explanation": "Normalization organizes data to minimize redundancy and dependency, improving data integrity."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Write SQL queries", "Design normalized databases", "Understand transactions", "Optimize database performance"]
    },
    "cs230": {
        "title": "Software Engineering",
        "topics": ["Software Development Life Cycle", "Design Patterns", "Testing", "Version Control", "Agile Methodologies"],
        "lessons": [
            {"id": "lesson_1", "topic": "SDLC", "title": "Development Process", "content": "Understand requirements, design, implementation, testing, and maintenance.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Testing", "title": "Software Testing", "content": "Learn unit testing, integration testing, and TDD.", "duration_minutes": 35, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Software Engineering",
                "title": "SE Principles",
                "questions": [
                    {"id": "q1", "question": "What is the purpose of version control?", "options": ["Speed up code", "Track changes and collaborate on code", "Compile programs", "Test software"], "correct_answer": "Track changes and collaborate on code", "explanation": "Version control systems like Git track code changes and enable team collaboration."},
                    {"id": "q2", "question": "What is Test-Driven Development (TDD)?", "options": ["Testing after coding", "Writing tests before code", "Testing only at the end", "Automated deployment"], "correct_answer": "Writing tests before code", "explanation": "TDD involves writing tests first, then writing code to pass those tests."},
                    {"id": "q3", "question": "What is a design pattern?", "options": ["A UI design", "A reusable solution to a common problem", "A testing framework", "A database schema"], "correct_answer": "A reusable solution to a common problem", "explanation": "Design patterns are proven solutions to recurring software design problems, like Singleton or Factory patterns."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Apply SDLC principles", "Use design patterns", "Write effective tests", "Work with version control"]
    },
    "cs301": {
        "title": "Computer Networks",
        "topics": ["Network Layers", "TCP/IP", "HTTP", "Network Security", "Protocols"],
        "lessons": [
            {"id": "lesson_1", "topic": "Layers", "title": "OSI Model", "content": "Understand the seven layers of network communication.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Protocols", "title": "TCP vs UDP", "content": "Compare connection-oriented and connectionless protocols.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Networks",
                "title": "Networking Basics",
                "questions": [
                    {"id": "q1", "question": "What does TCP guarantee?", "options": ["Speed", "Reliable, ordered delivery of data", "Small packet size", "Low latency"], "correct_answer": "Reliable, ordered delivery of data", "explanation": "TCP provides reliable, ordered delivery through acknowledgments and retransmissions."},
                    {"id": "q2", "question": "What layer is HTTP at?", "options": ["Physical", "Network", "Transport", "Application"], "correct_answer": "Application", "explanation": "HTTP operates at the Application layer (Layer 7) of the OSI model."},
                    {"id": "q3", "question": "What is DNS used for?", "options": ["Encrypting data", "Translating domain names to IP addresses", "Routing packets", "Managing bandwidth"], "correct_answer": "Translating domain names to IP addresses", "explanation": "DNS (Domain Name System) converts human-readable domain names into IP addresses."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand network architecture", "Analyze network protocols", "Troubleshoot network issues", "Design network systems"]
    },
    "cs310": {
        "title": "Machine Learning",
        "topics": ["Supervised Learning", "Neural Networks", "Classification", "Regression", "Model Evaluation"],
        "lessons": [
            {"id": "lesson_1", "topic": "Supervised Learning", "title": "ML Fundamentals", "content": "Learn regression, classification, and training/testing splits.", "duration_minutes": 40, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Neural Networks", "title": "Deep Learning", "content": "Understand neural network architecture and backpropagation.", "duration_minutes": 45, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Machine Learning",
                "title": "ML Basics",
                "questions": [
                    {"id": "q1", "question": "What is supervised learning?", "options": ["Learning without data", "Learning from labeled training data", "Learning by trial and error", "Unsupervised clustering"], "correct_answer": "Learning from labeled training data", "explanation": "Supervised learning trains models on labeled data where the correct output is known."},
                    {"id": "q2", "question": "What is overfitting?", "options": ["Model is too simple", "Model performs poorly on training data", "Model memorizes training data and performs poorly on new data", "Model is too fast"], "correct_answer": "Model memorizes training data and performs poorly on new data", "explanation": "Overfitting occurs when a model learns the training data too well, including noise, and doesn't generalize to new data."},
                    {"id": "q3", "question": "What is gradient descent used for?", "options": ["Data preprocessing", "Optimizing model parameters to minimize loss", "Feature selection", "Model evaluation"], "correct_answer": "Optimizing model parameters to minimize loss", "explanation": "Gradient descent is an optimization algorithm that adjusts model parameters to minimize the loss function."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Build ML models", "Evaluate model performance", "Apply neural networks", "Prevent overfitting"]
    },
    "cs320": {
        "title": "Computer Security",
        "topics": ["Cryptography", "Network Security", "Authentication", "Vulnerabilities", "Ethical Hacking"],
        "lessons": [
            {"id": "lesson_1", "topic": "Cryptography", "title": "Encryption Basics", "content": "Understand symmetric and asymmetric encryption.", "duration_minutes": 35, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Security", "title": "Common Vulnerabilities", "content": "Learn about SQL injection, XSS, and other attacks.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Security",
                "title": "Cybersecurity Fundamentals",
                "questions": [
                    {"id": "q1", "question": "What is encryption?", "options": ["Deleting data", "Converting data into unreadable format", "Compressing data", "Copying data"], "correct_answer": "Converting data into unreadable format", "explanation": "Encryption transforms readable data into ciphertext that can only be read with the correct key."},
                    {"id": "q2", "question": "What is a SQL injection attack?", "options": ["A database optimization", "Inserting malicious SQL code through input fields", "A type of virus", "A network attack"], "correct_answer": "Inserting malicious SQL code through input fields", "explanation": "SQL injection exploits vulnerabilities by injecting malicious SQL commands through user inputs."},
                    {"id": "q3", "question": "What does HTTPS provide?", "options": ["Faster loading", "Encrypted communication between browser and server", "Better SEO", "Larger file transfers"], "correct_answer": "Encrypted communication between browser and server", "explanation": "HTTPS encrypts data transmitted between the browser and server, protecting against eavesdropping."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Apply cryptographic techniques", "Identify security vulnerabilities", "Implement secure systems", "Understand ethical hacking"]
    },
    "cs350": {
        "title": "Senior Capstone Project I",
        "topics": ["Project Planning", "Requirements Gathering", "System Design", "Implementation", "Documentation"],
        "lessons": [
            {"id": "lesson_1", "topic": "Planning", "title": "Project Management", "content": "Learn to plan and manage a large software project.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Design", "title": "System Architecture", "content": "Design scalable, maintainable software systems.", "duration_minutes": 35, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Capstone",
                "title": "Project Management",
                "questions": [
                    {"id": "q1", "question": "What is a user story?", "options": ["A bug report", "A short description of a feature from the user's perspective", "A technical specification", "A test case"], "correct_answer": "A short description of a feature from the user's perspective", "explanation": "User stories describe features in terms of user needs: 'As a [user], I want [goal] so that [benefit]'."},
                    {"id": "q2", "question": "What is the purpose of a sprint in Agile?", "options": ["Running tests", "A fixed time period to complete specific work", "A type of meeting", "A deployment method"], "correct_answer": "A fixed time period to complete specific work", "explanation": "A sprint is a time-boxed iteration (typically 1-4 weeks) where a team completes a set of tasks."},
                    {"id": "q3", "question": "What is technical debt?", "options": ["Money owed by the project", "Future cost of shortcuts taken in development", "Project budget", "Testing requirements"], "correct_answer": "Future cost of shortcuts taken in development", "explanation": "Technical debt is the implied cost of additional rework caused by choosing a quick solution now instead of a better approach that would take longer."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Manage software projects", "Design system architecture", "Collaborate with teams", "Document technical work"]
    },
    "cs351": {
        "title": "Senior Capstone Project II",
        "topics": ["Project Completion", "Testing", "Deployment", "Presentation", "Portfolio"],
        "lessons": [
            {"id": "lesson_1", "topic": "Testing", "title": "Quality Assurance", "content": "Comprehensive testing strategies for your project.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Presentation", "title": "Demonstrating Your Work", "content": "How to present technical projects effectively.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Capstone Completion",
                "title": "Project Finalization",
                "questions": [
                    {"id": "q1", "question": "What is continuous integration?", "options": ["Merging code frequently with automated testing", "Writing code continuously", "Testing once at the end", "Deploying daily"], "correct_answer": "Merging code frequently with automated testing", "explanation": "CI involves frequently integrating code changes and running automated tests to catch issues early."},
                    {"id": "q2", "question": "What should a technical presentation include?", "options": ["Only code", "Problem, solution, demo, and results", "Only the demo", "Only slides"], "correct_answer": "Problem, solution, demo, and results", "explanation": "Good technical presentations explain the problem, your solution approach, demonstrate it working, and discuss results."},
                    {"id": "q3", "question": "What is DevOps?", "options": ["A programming language", "Practices combining development and operations", "A type of database", "A testing framework"], "correct_answer": "Practices combining development and operations", "explanation": "DevOps is a set of practices that combines software development and IT operations to shorten development cycles."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Complete large projects", "Deploy software systems", "Present technical work", "Build portfolio pieces"]
    },
    "cs400": {
        "title": "Theory of Computation",
        "topics": ["Automata Theory", "Regular Languages", "Context-Free Grammars", "Turing Machines", "Computability"],
        "lessons": [
            {"id": "lesson_1", "topic": "Automata", "title": "Finite Automata", "content": "Understand DFA and NFA models of computation.", "duration_minutes": 35, "difficulty": "very_high"},
            {"id": "lesson_2", "topic": "Turing Machines", "title": "Universal Computation", "content": "Learn about Turing machines and the halting problem.", "duration_minutes": 40, "difficulty": "very_high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Computation Theory",
                "title": "Theoretical CS",
                "questions": [
                    {"id": "q1", "question": "What is a regular language?", "options": ["Any programming language", "A language recognizable by a finite automaton", "A natural language", "A context-free language"], "correct_answer": "A language recognizable by a finite automaton", "explanation": "Regular languages are those that can be recognized by finite automata (DFA or NFA)."},
                    {"id": "q2", "question": "What does the halting problem prove?", "options": ["All programs halt", "Some problems are undecidable", "Computers are perfect", "All algorithms are efficient"], "correct_answer": "Some problems are undecidable", "explanation": "The halting problem proves there is no general algorithm to determine if an arbitrary program will halt."},
                    {"id": "q3", "question": "What is P vs NP?", "options": ["Two programming languages", "A question about whether problems solvable in polynomial time equal problems verifiable in polynomial time", "A database problem", "A networking protocol"], "correct_answer": "A question about whether problems solvable in polynomial time equal problems verifiable in polynomial time", "explanation": "P vs NP asks whether every problem whose solution can be quickly verified can also be quickly solved."}
                ],
                "passing_score": 70,
                "difficulty": "very_high"
            }
        ],
        "learning_outcomes": ["Understand automata theory", "Recognize computability limits", "Analyze complexity classes", "Prove language properties"]
    },
    "cs410": {
        "title": "Professional Development",
        "topics": ["Resume Building", "Interview Skills", "Salary Negotiation", "Career Planning", "Networking"],
        "lessons": [
            {"id": "lesson_1", "topic": "Resume", "title": "Crafting Your Resume", "content": "Write a compelling technical resume that gets interviews.", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Interviews", "title": "Technical Interviews", "content": "Prepare for coding interviews and system design questions.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Career Development",
                "title": "Professional Skills",
                "questions": [
                    {"id": "q1", "question": "What should be at the top of your resume?", "options": ["References", "Contact information and professional summary", "Education only", "Hobbies"], "correct_answer": "Contact information and professional summary", "explanation": "Your resume should start with contact info and a brief professional summary highlighting your key qualifications."},
                    {"id": "q2", "question": "What is the STAR method for interview questions?", "options": ["A rating system", "Situation, Task, Action, Result framework for answering behavioral questions", "A coding pattern", "A negotiation tactic"], "correct_answer": "Situation, Task, Action, Result framework for answering behavioral questions", "explanation": "STAR helps structure answers to behavioral questions by describing the Situation, Task, Action you took, and Result."},
                    {"id": "q3", "question": "When should you negotiate salary?", "options": ["In the first interview", "After receiving an offer", "Never", "During the application"], "correct_answer": "After receiving an offer", "explanation": "Salary negotiation happens after you have an offer, when you have the most leverage."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Write effective resumes", "Ace technical interviews", "Negotiate compensation", "Build professional network"]
    },
    "gen400": {
        "title": "Senior Seminar",
        "topics": ["Life Planning", "Career Transitions", "Lifelong Learning", "Ethics", "Reflection"],
        "lessons": [
            {"id": "lesson_1", "topic": "Transitions", "title": "From Student to Professional", "content": "Navigate the transition from college to career.", "duration_minutes": 20, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Learning", "title": "Continuous Learning", "content": "Strategies for staying current in your field.", "duration_minutes": 25, "difficulty": "beginner"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Life Planning",
                "title": "Senior Seminar",
                "questions": [
                    {"id": "q1", "question": "What is lifelong learning?", "options": ["Only formal education", "Continuous learning throughout your career and life", "Learning only in college", "Professional certifications"], "correct_answer": "Continuous learning throughout your career and life", "explanation": "Lifelong learning means continuously acquiring new skills and knowledge beyond formal education."},
                    {"id": "q2", "question": "What is work-life balance?", "options": ["Working all the time", "Managing time between career and personal life", "Only focusing on work", "Avoiding responsibility"], "correct_answer": "Managing time between career and personal life", "explanation": "Work-life balance involves effectively managing professional responsibilities while maintaining personal well-being."},
                    {"id": "q3", "question": "Why is networking important?", "options": ["It's not important", "Building relationships can lead to opportunities and support", "Only for sales people", "To collect business cards"], "correct_answer": "Building relationships can lead to opportunities and support", "explanation": "Professional networking builds relationships that can lead to job opportunities, mentorship, and career support."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Plan career transitions", "Develop lifelong learning habits", "Build professional identity", "Reflect on educational journey"]
    },
    # Business courses
    "acc201": {
        "title": "Financial Accounting",
        "topics": ["Accounting Equation", "Financial Statements", "Debits and Credits", "Accruals", "Closing Entries"],
        "lessons": [
            {"id": "lesson_1", "topic": "Equation", "title": "The Accounting Equation", "content": "Assets = Liabilities + Equity is the foundation of accounting.", "duration_minutes": 25, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Statements", "title": "Financial Statements", "content": "Learn to read balance sheets, income statements, and cash flow statements.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Accounting",
                "title": "Accounting Fundamentals",
                "questions": [
                    {"id": "q1", "question": "What is the accounting equation?", "options": ["Revenue - Expenses = Profit", "Assets = Liabilities + Equity", "Debits = Credits", "Income = Cash"], "correct_answer": "Assets = Liabilities + Equity", "explanation": "The fundamental equation Assets = Liabilities + Equity must always balance."},
                    {"id": "q2", "question": "Which statement shows profitability?", "options": ["Balance sheet", "Income statement", "Cash flow statement", "Statement of equity"], "correct_answer": "Income statement", "explanation": "The income statement shows revenues and expenses, revealing whether the company is profitable."},
                    {"id": "q3", "question": "What is a debit?", "options": ["Always negative", "A left-side entry that increases assets or expenses", "A credit card charge", "A liability"], "correct_answer": "A left-side entry that increases assets or expenses", "explanation": "Debits are left-side entries that increase assets and expenses, and decrease liabilities and equity."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand double-entry accounting", "Read financial statements", "Record transactions", "Analyze company financial health"]
    },
    "econ102": {
        "title": "Macroeconomics",
        "topics": ["GDP", "Inflation", "Unemployment", "Fiscal Policy", "Monetary Policy"],
        "lessons": [
            {"id": "lesson_1", "topic": "GDP", "title": "Measuring Economic Output", "content": "Understand GDP and its components.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Policy", "title": "Government and Central Banks", "content": "Learn how fiscal and monetary policy affect the economy.", "duration_minutes": 35, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Macroeconomics",
                "title": "Macro Fundamentals",
                "questions": [
                    {"id": "q1", "question": "What does GDP measure?", "options": ["Government debt", "Total value of goods and services produced", "Inflation rate", "Unemployment rate"], "correct_answer": "Total value of goods and services produced", "explanation": "GDP (Gross Domestic Product) measures the total economic output of a country."},
                    {"id": "q2", "question": "What is inflation?", "options": ["Falling prices", "A general increase in prices over time", "Economic growth", "Higher wages"], "correct_answer": "A general increase in prices over time", "explanation": "Inflation is when the general price level rises, reducing purchasing power."},
                    {"id": "q3", "question": "What tool does the Federal Reserve use to influence interest rates?", "options": ["Taxes", "The federal funds rate", "Government spending", "Trade policy"], "correct_answer": "The federal funds rate", "explanation": "The Fed adjusts the federal funds rate to influence borrowing costs and economic activity."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand macroeconomic indicators", "Analyze fiscal and monetary policy", "Evaluate business cycles", "Interpret economic data"]
    },
    "mkt201": {
        "title": "Marketing Fundamentals",
        "topics": ["Marketing Mix (4 Ps)", "Consumer Behavior", "Market Segmentation", "Branding", "Digital Marketing"],
        "lessons": [
            {"id": "lesson_1", "topic": "4 Ps", "title": "The Marketing Mix", "content": "Master Product, Price, Place, and Promotion.", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Behavior", "title": "Understanding Consumers", "content": "Learn what drives purchasing decisions.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Marketing",
                "title": "Marketing Basics",
                "questions": [
                    {"id": "q1", "question": "What are the 4 Ps of marketing?", "options": ["People, Process, Product, Price", "Product, Price, Place, Promotion", "Planning, Pricing, Positioning, Promotion", "Profit, Product, Place, People"], "correct_answer": "Product, Price, Place, Promotion", "explanation": "The 4 Ps are the core elements of the marketing mix: Product, Price, Place (distribution), and Promotion."},
                    {"id": "q2", "question": "What is market segmentation?", "options": ["Dividing a market into groups with similar needs", "Creating multiple products", "Setting different prices", "Advertising in segments"], "correct_answer": "Dividing a market into groups with similar needs", "explanation": "Market segmentation divides customers into groups (segments) with similar characteristics or needs."},
                    {"id": "q3", "question": "What is brand equity?", "options": ["The company's stock price", "The value a brand adds to a product", "Marketing budget", "Number of customers"], "correct_answer": "The value a brand adds to a product", "explanation": "Brand equity is the added value a strong brand name gives to a product beyond its functional benefits."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Apply marketing mix principles", "Analyze consumer behavior", "Develop marketing strategies", "Build brand awareness"]
    },
    "stat201": {
        "title": "Business Statistics",
        "topics": ["Descriptive Statistics", "Probability", "Sampling", "Hypothesis Testing", "Regression Analysis"],
        "lessons": [
            {"id": "lesson_1", "topic": "Descriptive", "title": "Summarizing Data", "content": "Calculate mean, median, mode, standard deviation, and more.", "duration_minutes": 25, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Inference", "title": "Making Decisions with Data", "content": "Use hypothesis testing to make business decisions.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Statistics",
                "title": "Statistics Fundamentals",
                "questions": [
                    {"id": "q1", "question": "What is the mean?", "options": ["The middle value", "The most common value", "The average value", "The range"], "correct_answer": "The average value", "explanation": "The mean is the sum of all values divided by the number of values - the arithmetic average."},
                    {"id": "q2", "question": "What does standard deviation measure?", "options": ["The average", "The middle value", "The spread or variability of data", "The total"], "correct_answer": "The spread or variability of data", "explanation": "Standard deviation quantifies how much data points deviate from the mean."},
                    {"id": "q3", "question": "What is a confidence interval?", "options": ["A range of likely values for a parameter", "A single estimate", "The probability of error", "The sample size"], "correct_answer": "A range of likely values for a parameter", "explanation": "A confidence interval gives a range where we expect the true parameter to fall with a certain level of confidence (e.g., 95%)."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Calculate descriptive statistics", "Conduct hypothesis tests", "Interpret statistical results", "Make data-driven decisions"]
    },
    "fin301": {
        "title": "Corporate Finance",
        "topics": ["Time Value of Money", "Capital Budgeting", "Risk and Return", "Capital Structure", "Valuation"],
        "lessons": [
            {"id": "lesson_1", "topic": "Time Value", "title": "Present and Future Value", "content": "Learn NPV, IRR, and discounted cash flow analysis.", "duration_minutes": 35, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Investment", "title": "Capital Budgeting", "content": "Evaluate investment projects and make go/no-go decisions.", "duration_minutes": 30, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Finance",
                "title": "Finance Fundamentals",
                "questions": [
                    {"id": "q1", "question": "What is the time value of money?", "options": ["Money loses value over time", "A dollar today is worth more than a dollar in the future", "Interest rates don't matter", "Future money is more valuable"], "correct_answer": "A dollar today is worth more than a dollar in the future", "explanation": "Due to earning potential, inflation, and risk, money available now is more valuable than the same amount in the future."},
                    {"id": "q2", "question": "What does NPV stand for?", "options": ["New Product Value", "Net Present Value", "National Product Value", "Nominal Price Value"], "correct_answer": "Net Present Value", "explanation": "NPV is the present value of cash inflows minus the present value of cash outflows over time."},
                    {"id": "q3", "question": "What is diversification?", "options": ["Putting all eggs in one basket", "Spreading investments across different assets to reduce risk", "Buying only stocks", "Avoiding risk entirely"], "correct_answer": "Spreading investments across different assets to reduce risk", "explanation": "Diversification reduces risk by investing in various assets that don't move in perfect correlation."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Calculate NPV and IRR", "Evaluate investment projects", "Understand risk and return", "Analyze capital structure decisions"]
    },
    "mgt301": {
        "title": "Organizational Behavior",
        "topics": ["Motivation", "Leadership", "Team Dynamics", "Organizational Culture", "Change Management"],
        "lessons": [
            {"id": "lesson_1", "topic": "Motivation", "title": "Motivating Employees", "content": "Understand motivation theories and how to apply them.", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Leadership", "title": "Leadership Styles", "content": "Explore different leadership approaches and their effectiveness.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "OB",
                "title": "Organizational Behavior",
                "questions": [
                    {"id": "q1", "question": "According to Maslow's hierarchy, what needs must be satisfied first?", "options": ["Self-actualization", "Esteem", "Safety", "Physiological"], "correct_answer": "Physiological", "explanation": "Maslow's hierarchy starts with basic physiological needs (food, water, shelter) at the bottom."},
                    {"id": "q2", "question": "What is transformational leadership?", "options": ["Maintaining the status quo", "Inspiring and motivating followers to exceed expectations", "Micromanaging employees", "Avoiding change"], "correct_answer": "Inspiring and motivating followers to exceed expectations", "explanation": "Transformational leaders inspire and motivate followers to achieve extraordinary outcomes and develop their own leadership capacity."},
                    {"id": "q3", "question": "What is organizational culture?", "options": ["Company rules", "Shared values, beliefs, and norms in an organization", "The physical office", "The org chart"], "correct_answer": "Shared values, beliefs, and norms in an organization", "explanation": "Organizational culture encompasses the shared values, beliefs, and behaviors that shape how work gets done."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Understand motivation theories", "Apply leadership principles", "Manage team dynamics", "Navigate organizational culture"]
    },
    "ops301": {
        "title": "Operations Management",
        "topics": ["Supply Chain", "Inventory Management", "Quality Control", "Process Optimization", "Lean Manufacturing"],
        "lessons": [
            {"id": "lesson_1", "topic": "Supply Chain", "title": "Managing the Supply Chain", "content": "Understand procurement, logistics, and distribution.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Quality", "title": "Quality Management", "content": "Learn Six Sigma and continuous improvement techniques.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Operations",
                "title": "Operations Management",
                "questions": [
                    {"id": "q1", "question": "What is the goal of Just-In-Time (JIT) inventory?", "options": ["Maximize inventory", "Minimize inventory by receiving goods only when needed", "Buy in bulk", "Store everything"], "correct_answer": "Minimize inventory by receiving goods only when needed", "explanation": "JIT reduces inventory costs and waste by receiving materials just as they are needed in production."},
                    {"id": "q2", "question": "What does Six Sigma aim to achieve?", "options": ["Increase variation", "Reduce defects to 3.4 per million opportunities", "Speed up production", "Lower costs only"], "correct_answer": "Reduce defects to 3.4 per million opportunities", "explanation": "Six Sigma is a methodology focused on reducing variation and defects to achieve near-perfect quality (99.99966%)."},
                    {"id": "q3", "question": "What is a bottleneck in operations?", "options": ["A process step that limits overall capacity", "A storage container", "A quality check", "A type of inventory"], "correct_answer": "A process step that limits overall capacity", "explanation": "A bottleneck is the slowest step in a process that constrains the entire system's throughput."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Manage supply chains", "Optimize operations", "Implement quality control", "Apply lean principles"]
    },
    "law201": {
        "title": "Business Law",
        "topics": ["Contracts", "Torts", "Employment Law", "Intellectual Property", "Business Entities"],
        "lessons": [
            {"id": "lesson_1", "topic": "Contracts", "title": "Contract Law", "content": "Understand contract formation, breach, and remedies.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "IP", "title": "Intellectual Property", "content": "Learn about patents, trademarks, and copyrights.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Law",
                "title": "Business Law Basics",
                "questions": [
                    {"id": "q1", "question": "What is required for a valid contract?", "options": ["Just a handshake", "Offer, acceptance, consideration, and capacity", "Only a signature", "Verbal agreement only"], "correct_answer": "Offer, acceptance, consideration, and capacity", "explanation": "A valid contract requires offer, acceptance, consideration (exchange of value), and parties with legal capacity."},
                    {"id": "q2", "question": "What does 'at-will employment' mean?", "options": ["Employees work whenever they want", "Either party can terminate employment at any time for any legal reason", "Lifetime employment", "Contract-based employment"], "correct_answer": "Either party can terminate employment at any time for any legal reason", "explanation": "At-will employment allows either the employer or employee to end the relationship at any time without cause (barring illegal discrimination)."},
                    {"id": "q3", "question": "What is a trademark?", "options": ["A trade agreement", "A distinctive sign that identifies products or services", "A business contract", "A tax form"], "correct_answer": "A distinctive sign that identifies products or services", "explanation": "A trademark is a recognizable sign, design, or expression that distinguishes products or services of one entity from others."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand contract law", "Recognize legal risks", "Navigate employment law", "Protect intellectual property"]
    },
    "acc202": {
        "title": "Managerial Accounting",
        "topics": ["Cost Accounting", "Budgeting", "Variance Analysis", "Break-Even Analysis", "Performance Measurement"],
        "lessons": [
            {"id": "lesson_1", "topic": "Costs", "title": "Cost Behavior", "content": "Understand fixed, variable, and mixed costs.", "duration_minutes": 25, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Budgeting", "title": "Budget Planning", "content": "Create and manage operational budgets.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Managerial Accounting",
                "title": "Cost and Budgeting",
                "questions": [
                    {"id": "q1", "question": "What is a variable cost?", "options": ["A cost that stays the same", "A cost that changes with production volume", "A one-time cost", "An unpredictable cost"], "correct_answer": "A cost that changes with production volume", "explanation": "Variable costs change in proportion to production volume (e.g., raw materials, direct labor)."},
                    {"id": "q2", "question": "What is the break-even point?", "options": ["Maximum profit", "The level of sales where total revenue equals total costs", "The highest cost", "The lowest price"], "correct_answer": "The level of sales where total revenue equals total costs", "explanation": "The break-even point is where a company neither makes a profit nor incurs a loss - revenue equals total costs."},
                    {"id": "q3", "question": "What is a budget variance?", "options": ["A budgeting error", "The difference between budgeted and actual amounts", "A type of budget", "A financial statement"], "correct_answer": "The difference between budgeted and actual amounts", "explanation": "Budget variance measures the difference between what was budgeted and what actually occurred, helping identify performance issues."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Analyze costs", "Create budgets", "Evaluate performance", "Make operational decisions"]
    },
    "mis301": {
        "title": "Management Information Systems",
        "topics": ["Information Systems", "Databases", "Business Intelligence", "E-Commerce", "Cybersecurity"],
        "lessons": [
            {"id": "lesson_1", "topic": "Systems", "title": "IS Fundamentals", "content": "Understand how information systems support business operations.", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "BI", "title": "Business Intelligence", "content": "Use data analytics to make better decisions.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "MIS",
                "title": "Information Systems",
                "questions": [
                    {"id": "q1", "question": "What is an information system?", "options": ["Just computers", "Hardware, software, data, people, and processes working together", "Only software", "The internet"], "correct_answer": "Hardware, software, data, people, and processes working together", "explanation": "An information system combines technology, data, people, and processes to achieve business goals."},
                    {"id": "q2", "question": "What is business intelligence?", "options": ["Smart business people", "Tools and techniques for analyzing business data", "A type of software", "Market research"], "correct_answer": "Tools and techniques for analyzing business data", "explanation": "Business intelligence encompasses tools and methods for transforming raw data into meaningful insights for decision-making."},
                    {"id": "q3", "question": "What is ERP?", "options": ["Emergency Response Plan", "Enterprise Resource Planning - integrated software for business processes", "Employee Retention Program", "Electronic Record Processing"], "correct_answer": "Enterprise Resource Planning - integrated software for business processes", "explanation": "ERP systems integrate all business processes (finance, HR, supply chain, etc.) into a single unified system."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Understand information systems", "Use business analytics tools", "Evaluate technology decisions", "Manage IS projects"]
    },
    "bus301": {
        "title": "Business Ethics",
        "topics": ["Ethical Theories", "Corporate Social Responsibility", "Ethical Decision-Making", "Stakeholder Theory", "Sustainability"],
        "lessons": [
            {"id": "lesson_1", "topic": "Ethics", "title": "Ethical Frameworks", "content": "Explore utilitarian, deontological, and virtue ethics.", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "CSR", "title": "Corporate Responsibility", "content": "Understand business obligations to society and environment.", "duration_minutes": 20, "difficulty": "beginner"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Ethics",
                "title": "Business Ethics",
                "questions": [
                    {"id": "q1", "question": "What is corporate social responsibility?", "options": ["Maximizing profit only", "A company's obligation to consider impacts on society and environment", "Government regulation", "Charity donations"], "correct_answer": "A company's obligation to consider impacts on society and environment", "explanation": "CSR is the concept that businesses should consider their impact on society and the environment beyond just profits."},
                    {"id": "q2", "question": "What is a stakeholder?", "options": ["Only shareholders", "Anyone affected by the business", "Only employees", "Only customers"], "correct_answer": "Anyone affected by the business", "explanation": "Stakeholders include all parties affected by business decisions: shareholders, employees, customers, suppliers, and communities."},
                    {"id": "q3", "question": "What is the triple bottom line?", "options": ["Three CEOs", "People, Planet, Profit", "Three financial statements", "Three years of data"], "correct_answer": "People, Planet, Profit", "explanation": "The triple bottom line measures company performance across social, environmental, and financial dimensions."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Apply ethical frameworks", "Evaluate ethical dilemmas", "Understand CSR", "Make responsible decisions"]
    },
    "str401": {
        "title": "Strategic Management",
        "topics": ["Competitive Strategy", "SWOT Analysis", "Porter's Five Forces", "Business Models", "Strategic Planning"],
        "lessons": [
            {"id": "lesson_1", "topic": "Strategy", "title": "Competitive Strategy", "content": "Learn cost leadership, differentiation, and focus strategies.", "duration_minutes": 35, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Analysis", "title": "Strategic Analysis", "content": "Use frameworks to analyze competitive position.", "duration_minutes": 30, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Strategy",
                "title": "Strategic Management",
                "questions": [
                    {"id": "q1", "question": "What are Porter's generic strategies?", "options": ["Fast, cheap, good", "Cost leadership, differentiation, focus", "Growth, stability, retrenchment", "Innovation, imitation, acquisition"], "correct_answer": "Cost leadership, differentiation, focus", "explanation": "Porter identified three generic strategies: being the low-cost leader, differentiating your offering, or focusing on a niche."},
                    {"id": "q2", "question": "What does SWOT stand for?", "options": ["Sales, Wages, Operations, Technology", "Strengths, Weaknesses, Opportunities, Threats", "Supply, Workforce, Objectives, Tactics", "Strategy, Work, Ownership, Targets"], "correct_answer": "Strengths, Weaknesses, Opportunities, Threats", "explanation": "SWOT analysis examines internal Strengths and Weaknesses, and external Opportunities and Threats."},
                    {"id": "q3", "question": "What is a competitive advantage?", "options": ["Being the biggest company", "Having something that allows you to outperform competitors", "Having the most employees", "Spending the most on advertising"], "correct_answer": "Having something that allows you to outperform competitors", "explanation": "Competitive advantage is any attribute that allows an organization to outperform its competitors."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Develop competitive strategies", "Conduct strategic analysis", "Understand business models", "Plan long-term strategy"]
    },
    "bus410": {
        "title": "Business Analytics",
        "topics": ["Data Analysis", "Predictive Analytics", "Data Visualization", "Excel Modeling", "Decision Support"],
        "lessons": [
            {"id": "lesson_1", "topic": "Analysis", "title": "Data Analytics", "content": "Clean, analyze, and interpret business data.", "duration_minutes": 35, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Visualization", "title": "Data Visualization", "content": "Create compelling charts and dashboards.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Analytics",
                "title": "Business Analytics",
                "questions": [
                    {"id": "q1", "question": "What is predictive analytics?", "options": ["Describing past events", "Using data to forecast future outcomes", "Collecting data", "Storing data"], "correct_answer": "Using data to forecast future outcomes", "explanation": "Predictive analytics uses historical data and statistical techniques to forecast future events and behaviors."},
                    {"id": "q2", "question": "What is a KPI?", "options": ["Key Process Indicator", "Key Performance Indicator", "Knowledge Process Integration", "Key Product Information"], "correct_answer": "Key Performance Indicator", "explanation": "A KPI is a measurable value that demonstrates how effectively a company is achieving key business objectives."},
                    {"id": "q3", "question": "Why is data visualization important?", "options": ["It looks pretty", "It makes data easier to understand and insights more accessible", "It's required by law", "It replaces analysis"], "correct_answer": "It makes data easier to understand and insights more accessible", "explanation": "Data visualization transforms complex data into visual formats that are easier to understand and enable faster decision-making."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Analyze business data", "Build predictive models", "Create visualizations", "Support data-driven decisions"]
    },
    "mkt410": {
        "title": "Digital Marketing",
        "topics": ["SEO", "Social Media Marketing", "Content Marketing", "Email Marketing", "Analytics"],
        "lessons": [
            {"id": "lesson_1", "topic": "SEO", "title": "Search Engine Optimization", "content": "Learn to optimize websites for search engines.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Social", "title": "Social Media Strategy", "content": "Develop effective social media campaigns.", "duration_minutes": 25, "difficulty": "beginner"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Digital Marketing",
                "title": "Digital Marketing Basics",
                "questions": [
                    {"id": "q1", "question": "What does SEO stand for?", "options": ["Social Engagement Optimization", "Search Engine Optimization", "Sales Efficiency Optimization", "Site Enhancement Operations"], "correct_answer": "Search Engine Optimization", "explanation": "SEO is the practice of optimizing websites to rank higher in search engine results pages."},
                    {"id": "q2", "question": "What is conversion rate?", "options": ["Website speed", "The percentage of visitors who take a desired action", "Social media followers", "Email open rate"], "correct_answer": "The percentage of visitors who take a desired action", "explanation": "Conversion rate measures the percentage of users who complete a desired action (purchase, sign-up, etc.)."},
                    {"id": "q3", "question": "What is content marketing?", "options": ["Any marketing content", "Creating valuable content to attract and engage an audience", "Advertising content", "Email spam"], "correct_answer": "Creating valuable content to attract and engage an audience", "explanation": "Content marketing involves creating and sharing valuable content to attract and retain a clearly defined audience."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Implement SEO strategies", "Manage social media campaigns", "Create content strategies", "Analyze digital marketing metrics"]
    },
    "bus490": {
        "title": "Business Capstone Project",
        "topics": ["Real-World Problem Solving", "Client Management", "Business Consulting", "Presentation Skills", "Integration"],
        "lessons": [
            {"id": "lesson_1", "topic": "Consulting", "title": "Business Consulting", "content": "Learn to analyze business problems and recommend solutions.", "duration_minutes": 30, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Presentation", "title": "Executive Presentations", "content": "Deliver compelling business presentations.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Capstone",
                "title": "Business Capstone",
                "questions": [
                    {"id": "q1", "question": "What is a business case?", "options": ["A legal case", "A document justifying a business decision or investment", "A customer complaint", "A lawsuit"], "correct_answer": "A document justifying a business decision or investment", "explanation": "A business case provides justification for a proposed project or initiative, including costs, benefits, and risks."},
                    {"id": "q2", "question": "What should an executive summary include?", "options": ["All the details", "Key findings, recommendations, and next steps in brief form", "Only financial data", "The full report"], "correct_answer": "Key findings, recommendations, and next steps in brief form", "explanation": "An executive summary concisely presents the most important information for busy decision-makers."},
                    {"id": "q3", "question": "What is stakeholder management?", "options": ["Managing shareholders only", "Identifying and addressing the needs of all project stakeholders", "Stock management", "Customer service"], "correct_answer": "Identifying and addressing the needs of all project stakeholders", "explanation": "Stakeholder management involves identifying stakeholders and managing their expectations and engagement."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Solve real business problems", "Manage client relationships", "Present professional recommendations", "Integrate business knowledge"]
    },
    "bus495": {
        "title": "Professional Development",
        "topics": ["Career Planning", "Networking", "Personal Branding", "Interview Skills", "Negotiation"],
        "lessons": [
            {"id": "lesson_1", "topic": "Networking", "title": "Professional Networking", "content": "Build and leverage your professional network.", "duration_minutes": 20, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Branding", "title": "Personal Brand", "content": "Develop your professional identity and online presence.", "duration_minutes": 25, "difficulty": "beginner"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Professional Development",
                "title": "Career Skills",
                "questions": [
                    {"id": "q1", "question": "What is an elevator pitch?", "options": ["A sales presentation", "A brief, compelling introduction of yourself", "A business proposal", "A long speech"], "correct_answer": "A brief, compelling introduction of yourself", "explanation": "An elevator pitch is a short (30-60 second) summary of who you are and what you do."},
                    {"id": "q2", "question": "What is LinkedIn primarily used for?", "options": ["Social networking", "Professional networking and career development", "Entertainment", "News"], "correct_answer": "Professional networking and career development", "explanation": "LinkedIn is a professional networking platform for career development, job searching, and business connections."},
                    {"id": "q3", "question": "When should you send a thank-you note after an interview?", "options": ["Never", "Within 24 hours", "After you get an offer", "A month later"], "correct_answer": "Within 24 hours", "explanation": "Send a thank-you email within 24 hours to express appreciation and reiterate your interest."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Develop career strategy", "Build professional network", "Master interview skills", "Negotiate effectively"]
    },
    "glb401": {
        "title": "Global Business Strategy",
        "topics": ["International Markets", "Cross-Cultural Management", "Global Supply Chains", "Foreign Exchange", "International Trade"],
        "lessons": [
            {"id": "lesson_1", "topic": "International", "title": "Going Global", "content": "Understand strategies for international expansion.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Culture", "title": "Cultural Intelligence", "content": "Navigate cultural differences in business.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Global Business",
                "title": "International Business",
                "questions": [
                    {"id": "q1", "question": "What is cultural intelligence?", "options": ["Speaking many languages", "The ability to work effectively across cultures", "Cultural knowledge only", "Foreign travel experience"], "correct_answer": "The ability to work effectively across cultures", "explanation": "Cultural intelligence (CQ) is the capability to relate and work effectively across cultures."},
                    {"id": "q2", "question": "What is foreign exchange risk?", "options": ["Risk of traveling abroad", "Risk of currency value fluctuations affecting profits", "Risk of foreign competition", "Risk of language barriers"], "correct_answer": "Risk of currency value fluctuations affecting profits", "explanation": "Foreign exchange risk is the possibility that currency fluctuations will affect the value of international transactions."},
                    {"id": "q3", "question": "What is a multinational corporation?", "options": ["A company with international customers", "A company that operates in multiple countries", "A large company", "A company that exports"], "correct_answer": "A company that operates in multiple countries", "explanation": "A multinational corporation (MNC) has facilities and operations in multiple countries beyond its home country."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand global markets", "Navigate cultural differences", "Manage international operations", "Develop global strategies"]
    },
    "ent401": {
        "title": "Entrepreneurship",
        "topics": ["Opportunity Recognition", "Business Planning", "Funding", "Lean Startup", "Scaling"],
        "lessons": [
            {"id": "lesson_1", "topic": "Opportunity", "title": "Finding Business Ideas", "content": "Identify and evaluate entrepreneurial opportunities.", "duration_minutes": 25, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Funding", "title": "Startup Financing", "content": "Understand funding sources from bootstrapping to VC.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Entrepreneurship",
                "title": "Startup Basics",
                "questions": [
                    {"id": "q1", "question": "What is a Minimum Viable Product (MVP)?", "options": ["The cheapest product", "A product with just enough features to test market demand", "A prototype", "The first version"], "correct_answer": "A product with just enough features to test market demand", "explanation": "An MVP has just enough features to satisfy early customers and provide feedback for future development."},
                    {"id": "q2", "question": "What is bootstrapping?", "options": ["Wearing boots", "Self-funding a business without external investment", "Getting a loan", "Seeking venture capital"], "correct_answer": "Self-funding a business without external investment", "explanation": "Bootstrapping means starting and growing a business using personal finances or operating revenue without external funding."},
                    {"id": "q3", "question": "What is a pivot?", "options": ["Giving up", "A fundamental change in business strategy", "Expanding the team", "Raising more money"], "correct_answer": "A fundamental change in business strategy", "explanation": "A pivot is a structured course correction to test a new fundamental hypothesis about the business."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Identify business opportunities", "Create business plans", "Understand startup financing", "Apply lean startup principles"]
    },
    "sem401": {
        "title": "Senior Seminar",
        "topics": ["Career Reflection", "Life Planning", "Professional Identity", "Continued Learning", "Transitions"],
        "lessons": [
            {"id": "lesson_1", "topic": "Reflection", "title": "Looking Back and Forward", "content": "Reflect on your education and plan your career path.", "duration_minutes": 20, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Transitions", "title": "Student to Professional", "content": "Prepare for the transition to professional life.", "duration_minutes": 20, "difficulty": "beginner"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Senior Seminar",
                "title": "Transitions and Planning",
                "questions": [
                    {"id": "q1", "question": "What is important for career success?", "options": ["Only technical skills", "A combination of technical skills, soft skills, and continuous learning", "Just working hard", "Degrees only"], "correct_answer": "A combination of technical skills, soft skills, and continuous learning", "explanation": "Success requires balancing technical expertise, interpersonal skills, and commitment to lifelong learning."},
                    {"id": "q2", "question": "What is professional development?", "options": ["Only job training", "Ongoing process of acquiring new skills and knowledge throughout your career", "Getting a degree", "One-time event"], "correct_answer": "Ongoing process of acquiring new skills and knowledge throughout your career", "explanation": "Professional development is a continuous process of learning and growing throughout your career."},
                    {"id": "q3", "question": "Why is work-life balance important?", "options": ["It's not important", "To maintain health, relationships, and long-term career sustainability", "To work less", "To avoid responsibility"], "correct_answer": "To maintain health, relationships, and long-term career sustainability", "explanation": "Work-life balance is crucial for physical and mental health, relationships, and sustained career success."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Reflect on educational journey", "Plan career trajectory", "Develop professional identity", "Prepare for transitions"]
    },
    "math110": {
        "title": "Business Mathematics",
        "topics": ["Algebra", "Financial Math", "Statistics Basics", "Percentages", "Linear Equations"],
        "lessons": [
            {"id": "lesson_1", "topic": "Financial Math", "title": "Business Calculations", "content": "Master percentage calculations, interest, and financial formulas.", "duration_minutes": 25, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Algebra", "title": "Business Algebra", "content": "Apply algebraic concepts to business problems.", "duration_minutes": 30, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Business Math",
                "title": "Business Mathematics",
                "questions": [
                    {"id": "q1", "question": "What is the formula for simple interest?", "options": ["I = P × r × t", "I = P(1 + r)^t", "I = P/r", "I = P + r"], "correct_answer": "I = P × r × t", "explanation": "Simple interest is calculated as Interest = Principal × rate × time."},
                    {"id": "q2", "question": "If a product costs $80 and is marked up 25%, what's the selling price?", "options": ["$90", "$100", "$105", "$85"], "correct_answer": "$100", "explanation": "$80 × 1.25 = $100. The markup of 25% adds $20 to the cost."},
                    {"id": "q3", "question": "What does 'break-even' mean in business math?", "options": ["Maximum profit", "When total revenue equals total costs", "Lowest price", "Highest sales"], "correct_answer": "When total revenue equals total costs", "explanation": "Break-even is the point where total revenue exactly equals total costs, resulting in zero profit or loss."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Calculate business metrics", "Apply algebra to business", "Understand financial formulas", "Analyze business data"]
    },
    # Engineering courses
    "chem101": {
        "title": "General Chemistry I",
        "topics": ["Atomic Structure", "Chemical Bonding", "Stoichiometry", "Periodic Table", "Chemical Reactions"],
        "lessons": [
            {"id": "lesson_1", "topic": "Atoms", "title": "Atomic Structure", "content": "Understand protons, neutrons, electrons, and atomic models.", "duration_minutes": 30, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Bonding", "title": "Chemical Bonds", "content": "Learn ionic, covalent, and metallic bonding.", "duration_minutes": 35, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Chemistry",
                "title": "Chemistry Fundamentals",
                "questions": [
                    {"id": "q1", "question": "What determines an element's identity?", "options": ["Number of neutrons", "Number of protons", "Number of electrons", "Atomic mass"], "correct_answer": "Number of protons", "explanation": "The number of protons (atomic number) uniquely identifies each element."},
                    {"id": "q2", "question": "What is a mole in chemistry?", "options": ["A small animal", "6.022 × 10²³ particles", "A unit of volume", "A measurement of mass"], "correct_answer": "6.022 × 10²³ particles", "explanation": "A mole is Avogadro's number (6.022 × 10²³) of particles, used to count atoms and molecules."},
                    {"id": "q3", "question": "What type of bond forms between a metal and nonmetal?", "options": ["Covalent", "Ionic", "Metallic", "Hydrogen"], "correct_answer": "Ionic", "explanation": "Ionic bonds form when metals transfer electrons to nonmetals, creating oppositely charged ions."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Understand atomic structure", "Predict chemical bonding", "Balance chemical equations", "Perform stoichiometric calculations"]
    },
    "chem102": {
        "title": "General Chemistry II",
        "topics": ["Thermodynamics", "Kinetics", "Equilibrium", "Acids and Bases", "Electrochemistry"],
        "lessons": [
            {"id": "lesson_1", "topic": "Thermodynamics", "title": "Energy and Entropy", "content": "Study energy changes and spontaneity in reactions.", "duration_minutes": 35, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Kinetics", "title": "Reaction Rates", "content": "Understand factors affecting reaction speed.", "duration_minutes": 30, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Chemistry II",
                "title": "Advanced Chemistry",
                "questions": [
                    {"id": "q1", "question": "What is entropy?", "options": ["Energy", "A measure of disorder or randomness", "Temperature", "Pressure"], "correct_answer": "A measure of disorder or randomness", "explanation": "Entropy measures the degree of disorder or randomness in a system."},
                    {"id": "q2", "question": "What is a catalyst?", "options": ["A reactant", "A substance that speeds up a reaction without being consumed", "A product", "An inhibitor"], "correct_answer": "A substance that speeds up a reaction without being consumed", "explanation": "Catalysts lower activation energy and increase reaction rates without being consumed in the reaction."},
                    {"id": "q3", "question": "What does pH measure?", "options": ["Temperature", "Pressure", "Acidity or basicity of a solution", "Density"], "correct_answer": "Acidity or basicity of a solution", "explanation": "pH measures the concentration of hydrogen ions, indicating how acidic or basic a solution is."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Apply thermodynamic principles", "Analyze reaction kinetics", "Understand chemical equilibrium", "Work with acids and bases"]
    },
    "phys141": {
        "title": "Physics I: Mechanics",
        "topics": ["Kinematics", "Newton's Laws", "Energy and Work", "Momentum", "Rotational Motion"],
        "lessons": [
            {"id": "lesson_1", "topic": "Motion", "title": "Kinematics", "content": "Study position, velocity, and acceleration.", "duration_minutes": 30, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Forces", "title": "Newton's Laws", "content": "Understand force, mass, and acceleration relationships.", "duration_minutes": 35, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Mechanics",
                "title": "Physics Mechanics",
                "questions": [
                    {"id": "q1", "question": "What is Newton's Second Law?", "options": ["F = ma", "E = mc²", "v = d/t", "p = mv"], "correct_answer": "F = ma", "explanation": "Newton's Second Law states that Force equals mass times acceleration (F = ma)."},
                    {"id": "q2", "question": "What is conserved in an elastic collision?", "options": ["Only momentum", "Only kinetic energy", "Both momentum and kinetic energy", "Neither"], "correct_answer": "Both momentum and kinetic energy", "explanation": "In elastic collisions, both momentum and kinetic energy are conserved."},
                    {"id": "q3", "question": "What is the work-energy theorem?", "options": ["Work equals force", "Work done equals change in kinetic energy", "Energy is constant", "Work is power times time"], "correct_answer": "Work done equals change in kinetic energy", "explanation": "The work-energy theorem states that the net work done on an object equals its change in kinetic energy."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Apply Newton's laws", "Solve kinematics problems", "Analyze energy and momentum", "Understand rotational dynamics"]
    },
    "phys142": {
        "title": "Physics II: Electricity & Magnetism",
        "topics": ["Electric Fields", "Electric Circuits", "Magnetism", "Electromagnetic Induction", "Maxwell's Equations"],
        "lessons": [
            {"id": "lesson_1", "topic": "Electricity", "title": "Electric Fields and Potential", "content": "Study Coulomb's law and electric potential energy.", "duration_minutes": 35, "difficulty": "very_high"},
            {"id": "lesson_2", "topic": "Circuits", "title": "DC Circuits", "content": "Analyze resistors, capacitors, and circuit laws.", "duration_minutes": 30, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "E&M",
                "title": "Electricity and Magnetism",
                "questions": [
                    {"id": "q1", "question": "What is Ohm's Law?", "options": ["V = IR", "F = ma", "E = mc²", "P = IV"], "correct_answer": "V = IR", "explanation": "Ohm's Law states that Voltage equals Current times Resistance (V = IR)."},
                    {"id": "q2", "question": "What do magnetic field lines represent?", "options": ["Electric current", "The direction a north pole would move", "Voltage", "Resistance"], "correct_answer": "The direction a north pole would move", "explanation": "Magnetic field lines show the direction and strength of a magnetic field, pointing from north to south."},
                    {"id": "q3", "question": "What is electromagnetic induction?", "options": ["Static electricity", "Generating electric current from changing magnetic fields", "Battery power", "Heat transfer"], "correct_answer": "Generating electric current from changing magnetic fields", "explanation": "Electromagnetic induction is the production of voltage across a conductor in a changing magnetic field."}
                ],
                "passing_score": 70,
                "difficulty": "very_high"
            }
        ],
        "learning_outcomes": ["Understand electric fields", "Analyze circuits", "Apply magnetic principles", "Work with electromagnetic induction"]
    },
    "comm101": {
        "title": "Technical Communication",
        "topics": ["Technical Writing", "Documentation", "Reports", "Presentations", "Visual Communication"],
        "lessons": [
            {"id": "lesson_1", "topic": "Writing", "title": "Clear Technical Writing", "content": "Write clear, concise technical documents.", "duration_minutes": 20, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Documentation", "title": "Technical Documentation", "content": "Create user manuals and technical specifications.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Technical Communication",
                "title": "Tech Writing",
                "questions": [
                    {"id": "q1", "question": "What is the purpose of technical writing?", "options": ["To entertain", "To clearly communicate technical information", "To persuade", "To tell stories"], "correct_answer": "To clearly communicate technical information", "explanation": "Technical writing aims to convey complex information clearly and accurately to a specific audience."},
                    {"id": "q2", "question": "What should a technical report include?", "options": ["Personal opinions only", "Introduction, methods, results, and conclusions", "Only conclusions", "Stories and anecdotes"], "correct_answer": "Introduction, methods, results, and conclusions", "explanation": "Technical reports follow a structured format presenting objectives, methodology, findings, and conclusions."},
                    {"id": "q3", "question": "Why are visuals important in technical communication?", "options": ["They make documents longer", "They help explain complex concepts and data", "They're required", "They replace text"], "correct_answer": "They help explain complex concepts and data", "explanation": "Visual aids like diagrams and charts make complex technical information easier to understand."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Write technical documents", "Create effective reports", "Design presentations", "Communicate complex ideas clearly"]
    },
    "math241": {
        "title": "Calculus III",
        "topics": ["Multivariable Functions", "Partial Derivatives", "Multiple Integrals", "Vector Calculus", "Line Integrals"],
        "lessons": [
            {"id": "lesson_1", "topic": "Multivariable", "title": "Functions of Several Variables", "content": "Extend calculus to functions of multiple variables.", "duration_minutes": 35, "difficulty": "very_high"},
            {"id": "lesson_2", "topic": "Integration", "title": "Multiple Integrals", "content": "Learn double and triple integrals.", "duration_minutes": 40, "difficulty": "very_high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Multivariable Calculus",
                "title": "Calc III",
                "questions": [
                    {"id": "q1", "question": "What is a partial derivative?", "options": ["Derivative of part of a function", "Derivative with respect to one variable while holding others constant", "Incomplete derivative", "Half a derivative"], "correct_answer": "Derivative with respect to one variable while holding others constant", "explanation": "Partial derivatives measure how a multivariable function changes with respect to one variable."},
                    {"id": "q2", "question": "What does a gradient vector point toward?", "options": ["The origin", "The direction of steepest ascent", "Downhill", "Perpendicular to level curves"], "correct_answer": "The direction of steepest ascent", "explanation": "The gradient vector points in the direction of greatest increase of a function."},
                    {"id": "q3", "question": "What is a level curve?", "options": ["A flat line", "A curve where the function has a constant value", "A horizontal line", "A straight line"], "correct_answer": "A curve where the function has a constant value", "explanation": "Level curves connect points where a function f(x,y) has the same value, like contour lines on a map."}
                ],
                "passing_score": 70,
                "difficulty": "very_high"
            }
        ],
        "learning_outcomes": ["Work with multivariable functions", "Calculate partial derivatives", "Evaluate multiple integrals", "Apply vector calculus"]
    },
    "math246": {
        "title": "Differential Equations",
        "topics": ["First-Order ODEs", "Second-Order ODEs", "Laplace Transforms", "Systems of DEs", "Partial DEs"],
        "lessons": [
            {"id": "lesson_1", "topic": "ODEs", "title": "Ordinary Differential Equations", "content": "Solve first and second-order differential equations.", "duration_minutes": 40, "difficulty": "very_high"},
            {"id": "lesson_2", "topic": "Applications", "title": "Engineering Applications", "content": "Apply DEs to real engineering problems.", "duration_minutes": 35, "difficulty": "very_high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Differential Equations",
                "title": "DEs",
                "questions": [
                    {"id": "q1", "question": "What is a differential equation?", "options": ["An equation with fractions", "An equation involving derivatives", "An equation with differences", "A difficult equation"], "correct_answer": "An equation involving derivatives", "explanation": "Differential equations relate a function to its derivatives, describing rates of change."},
                    {"id": "q2", "question": "What does 'order' mean for a differential equation?", "options": ["The sequence of solving", "The highest derivative present", "The number of solutions", "The difficulty level"], "correct_answer": "The highest derivative present", "explanation": "The order of a DE is determined by the highest derivative in the equation."},
                    {"id": "q3", "question": "What is a Laplace transform used for?", "options": ["Graphing functions", "Converting DEs to algebraic equations", "Finding derivatives", "Integration"], "correct_answer": "Converting DEs to algebraic equations", "explanation": "Laplace transforms convert differential equations into easier-to-solve algebraic equations."}
                ],
                "passing_score": 70,
                "difficulty": "very_high"
            }
        ],
        "learning_outcomes": ["Solve differential equations", "Apply Laplace transforms", "Model engineering systems", "Analyze dynamic systems"]
    },
    "engr201": {
        "title": "Statics",
        "topics": ["Force Vectors", "Equilibrium", "Trusses", "Moments", "Friction"],
        "lessons": [
            {"id": "lesson_1", "topic": "Forces", "title": "Force Analysis", "content": "Analyze forces and moments on structures.", "duration_minutes": 35, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Equilibrium", "title": "Static Equilibrium", "content": "Apply equilibrium conditions to solve problems.", "duration_minutes": 30, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Statics",
                "title": "Statics Fundamentals",
                "questions": [
                    {"id": "q1", "question": "What is static equilibrium?", "options": ["Moving at constant speed", "Sum of forces and moments equals zero", "Maximum force", "Minimum energy"], "correct_answer": "Sum of forces and moments equals zero", "explanation": "Static equilibrium requires that the sum of all forces and the sum of all moments equal zero."},
                    {"id": "q2", "question": "What is a moment (torque)?", "options": ["A brief time", "Force times perpendicular distance", "Mass times velocity", "Weight"], "correct_answer": "Force times perpendicular distance", "explanation": "A moment (torque) is the rotational effect of a force, calculated as force times perpendicular distance from the pivot."},
                    {"id": "q3", "question": "What is a free body diagram?", "options": ["A diagram of free objects", "A sketch showing all forces acting on an isolated object", "A physics drawing", "A structural blueprint"], "correct_answer": "A sketch showing all forces acting on an isolated object", "explanation": "A free body diagram isolates an object and shows all external forces acting on it."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Analyze force systems", "Apply equilibrium equations", "Design trusses", "Solve statics problems"]
    },
    "engr202": {
        "title": "Dynamics",
        "topics": ["Kinematics of Particles", "Kinetics", "Work and Energy", "Impulse and Momentum", "Rigid Body Dynamics"],
        "lessons": [
            {"id": "lesson_1", "topic": "Kinematics", "title": "Motion Analysis", "content": "Analyze position, velocity, and acceleration of moving bodies.", "duration_minutes": 35, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Kinetics", "title": "Forces and Motion", "content": "Relate forces to motion using Newton's laws.", "duration_minutes": 30, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Dynamics",
                "title": "Dynamics Fundamentals",
                "questions": [
                    {"id": "q1", "question": "What is the difference between kinematics and kinetics?", "options": ["No difference", "Kinematics describes motion; kinetics relates forces to motion", "Kinetics is easier", "Kinematics uses calculus"], "correct_answer": "Kinematics describes motion; kinetics relates forces to motion", "explanation": "Kinematics describes motion geometry without considering forces; kinetics analyzes forces causing motion."},
                    {"id": "q2", "question": "What is angular momentum?", "options": ["Linear momentum", "Moment of inertia times angular velocity", "Mass times velocity", "Force times distance"], "correct_answer": "Moment of inertia times angular velocity", "explanation": "Angular momentum for rotating objects equals moment of inertia times angular velocity (L = Iω)."},
                    {"id": "q3", "question": "When is mechanical energy conserved?", "options": ["Always", "When no non-conservative forces do work", "Never", "Only at rest"], "correct_answer": "When no non-conservative forces do work", "explanation": "Mechanical energy is conserved when only conservative forces (like gravity) act on the system."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Analyze particle motion", "Apply Newton's laws to moving systems", "Use energy methods", "Solve rigid body problems"]
    },
    "engr205": {
        "title": "Materials Science",
        "topics": ["Atomic Structure", "Crystal Structure", "Mechanical Properties", "Phase Diagrams", "Material Selection"],
        "lessons": [
            {"id": "lesson_1", "topic": "Structure", "title": "Material Structure", "content": "Understand how atomic structure affects properties.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Properties", "title": "Mechanical Properties", "content": "Learn about stress, strain, and material behavior.", "duration_minutes": 35, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Materials",
                "title": "Materials Science",
                "questions": [
                    {"id": "q1", "question": "What is stress?", "options": ["Deformation", "Force per unit area", "Strain rate", "Material type"], "correct_answer": "Force per unit area", "explanation": "Stress is the internal force per unit area within a material (σ = F/A)."},
                    {"id": "q2", "question": "What is Young's modulus?", "options": ["Strength", "Stiffness - stress divided by strain", "Hardness", "Toughness"], "correct_answer": "Stiffness - stress divided by strain", "explanation": "Young's modulus (E) measures material stiffness as the ratio of stress to strain in the elastic region."},
                    {"id": "q3", "question": "What makes steel harder than aluminum?", "options": ["Color", "Crystal structure and bonding", "Weight", "Cost"], "correct_answer": "Crystal structure and bonding", "explanation": "Steel's body-centered cubic structure and stronger metallic bonding give it greater hardness than aluminum."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand material structure", "Analyze mechanical properties", "Select appropriate materials", "Interpret phase diagrams"]
    },
    "engr210": {
        "title": "Thermodynamics",
        "topics": ["First Law", "Second Law", "Heat Engines", "Refrigeration", "Entropy"],
        "lessons": [
            {"id": "lesson_1", "topic": "Energy", "title": "Conservation of Energy", "content": "Apply the first law of thermodynamics.", "duration_minutes": 35, "difficulty": "very_high"},
            {"id": "lesson_2", "topic": "Entropy", "title": "Second Law", "content": "Understand entropy and the second law.", "duration_minutes": 40, "difficulty": "very_high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Thermodynamics",
                "title": "Thermo Fundamentals",
                "questions": [
                    {"id": "q1", "question": "What does the First Law of Thermodynamics state?", "options": ["Energy cannot be created or destroyed", "Entropy always increases", "Heat flows from hot to cold", "Work equals force times distance"], "correct_answer": "Energy cannot be created or destroyed", "explanation": "The First Law states that energy is conserved - it can change forms but cannot be created or destroyed."},
                    {"id": "q2", "question": "What is entropy?", "options": ["Energy", "A measure of disorder or unavailable energy", "Temperature", "Pressure"], "correct_answer": "A measure of disorder or unavailable energy", "explanation": "Entropy measures the degree of disorder in a system and represents energy that cannot do useful work."},
                    {"id": "q3", "question": "What is the efficiency of a Carnot engine?", "options": ["Always 100%", "1 - (T_cold/T_hot)", "T_hot/T_cold", "50%"], "correct_answer": "1 - (T_cold/T_hot)", "explanation": "Carnot efficiency is the maximum theoretical efficiency: η = 1 - (T_cold/T_hot) where T is absolute temperature."}
                ],
                "passing_score": 70,
                "difficulty": "very_high"
            }
        ],
        "learning_outcomes": ["Apply thermodynamic laws", "Analyze heat engines", "Calculate entropy changes", "Design thermal systems"]
    },
    "engr215": {
        "title": "Circuits & Electronics",
        "topics": ["Circuit Analysis", "Resistors and Capacitors", "Transistors", "Op-Amps", "AC Circuits"],
        "lessons": [
            {"id": "lesson_1", "topic": "DC Circuits", "title": "Circuit Laws", "content": "Master Ohm's law, KVL, and KCL.", "duration_minutes": 30, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Components", "title": "Electronic Components", "content": "Understand resistors, capacitors, and semiconductors.", "duration_minutes": 35, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Circuits",
                "title": "Circuit Analysis",
                "questions": [
                    {"id": "q1", "question": "What is Kirchhoff's Current Law (KCL)?", "options": ["V = IR", "Sum of currents entering a node equals sum leaving", "Power equals voltage times current", "Resistance adds in series"], "correct_answer": "Sum of currents entering a node equals sum leaving", "explanation": "KCL states that the total current entering a node must equal the total current leaving (conservation of charge)."},
                    {"id": "q2", "question": "What does a capacitor do?", "options": ["Resists current", "Stores electrical energy in an electric field", "Amplifies signals", "Generates power"], "correct_answer": "Stores electrical energy in an electric field", "explanation": "Capacitors store electrical energy in an electric field between two conductive plates."},
                    {"id": "q3", "question": "What is the function of a transistor?", "options": ["Store energy", "Amplify or switch electronic signals", "Resist current", "Convert AC to DC"], "correct_answer": "Amplify or switch electronic signals", "explanation": "Transistors can amplify signals or act as electronic switches in circuits."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Analyze electrical circuits", "Design basic circuits", "Understand semiconductor devices", "Work with AC and DC circuits"]
    },
    "engr301": {
        "title": "Engineering Design I",
        "topics": ["Design Process", "CAD", "Prototyping", "Materials Selection", "Project Management"],
        "lessons": [
            {"id": "lesson_1", "topic": "Process", "title": "Design Methodology", "content": "Learn the engineering design process from concept to prototype.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "CAD", "title": "Computer-Aided Design", "content": "Use CAD software to design components and assemblies.", "duration_minutes": 35, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Design",
                "title": "Engineering Design",
                "questions": [
                    {"id": "q1", "question": "What are the main steps in the engineering design process?", "options": ["Build, test, fix", "Define, ideate, prototype, test, refine", "Draw, build, sell", "Plan, execute, close"], "correct_answer": "Define, ideate, prototype, test, refine", "explanation": "The design process includes defining the problem, generating ideas, prototyping, testing, and refining the solution."},
                    {"id": "q2", "question": "What is the purpose of a prototype?", "options": ["Final product", "To test and validate design concepts", "For marketing", "To meet deadlines"], "correct_answer": "To test and validate design concepts", "explanation": "Prototypes allow testing of design concepts and identify issues before final production."},
                    {"id": "q3", "question": "What is CAD?", "options": ["Computer-Aided Design", "Computer Analysis Device", "Circuit Analysis Design", "Creative Art Design"], "correct_answer": "Computer-Aided Design", "explanation": "CAD (Computer-Aided Design) software is used to create detailed 2D and 3D models of designs."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Apply design process", "Use CAD software", "Build prototypes", "Manage design projects"]
    },
    "engr302": {
        "title": "Engineering Design II",
        "topics": ["Design Validation", "Testing", "Documentation", "Manufacturing", "Presentation"],
        "lessons": [
            {"id": "lesson_1", "topic": "Testing", "title": "Design Verification", "content": "Test and validate your design against requirements.", "duration_minutes": 30, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Documentation", "title": "Engineering Documentation", "content": "Create comprehensive technical documentation.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Design Completion",
                "title": "Design Validation",
                "questions": [
                    {"id": "q1", "question": "What is design verification?", "options": ["Approving the design", "Testing that the design meets requirements", "Signing off", "Manufacturing"], "correct_answer": "Testing that the design meets requirements", "explanation": "Design verification ensures the product meets all specified requirements through testing and analysis."},
                    {"id": "q2", "question": "What should engineering documentation include?", "options": ["Only drawings", "Drawings, specifications, test results, and user manuals", "Just the final report", "Marketing materials"], "correct_answer": "Drawings, specifications, test results, and user manuals", "explanation": "Complete documentation includes technical drawings, specifications, testing data, and user information."},
                    {"id": "q3", "question": "What is Design for Manufacturing (DFM)?", "options": ["Designing factories", "Designing products to be easily and cost-effectively manufactured", "Manufacturing design software", "Factory layout"], "correct_answer": "Designing products to be easily and cost-effectively manufactured", "explanation": "DFM considers manufacturing constraints and costs during the design phase to improve producibility."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Validate designs", "Conduct comprehensive testing", "Create technical documentation", "Prepare for manufacturing"]
    },
    "engr310": {
        "title": "Engineering Economics",
        "topics": ["Time Value of Money", "Project Evaluation", "Cost-Benefit Analysis", "Depreciation", "Risk Analysis"],
        "lessons": [
            {"id": "lesson_1", "topic": "Economics", "title": "Engineering Economic Analysis", "content": "Apply economic principles to engineering decisions.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Evaluation", "title": "Project Evaluation", "content": "Evaluate and compare engineering alternatives.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Engineering Economics",
                "title": "Economic Analysis",
                "questions": [
                    {"id": "q1", "question": "What is Net Present Value (NPV)?", "options": ["Current value", "Present value of future cash flows minus initial cost", "Total profit", "Break-even point"], "correct_answer": "Present value of future cash flows minus initial cost", "explanation": "NPV discounts future cash flows to present value and subtracts the initial investment to evaluate profitability."},
                    {"id": "q2", "question": "What is the purpose of depreciation?", "options": ["To increase value", "To allocate asset cost over its useful life", "To calculate taxes", "To predict failure"], "correct_answer": "To allocate asset cost over its useful life", "explanation": "Depreciation systematically allocates the cost of an asset over its expected useful life for accounting and tax purposes."},
                    {"id": "q3", "question": "What is payback period?", "options": ["Loan term", "Time to recover initial investment", "Interest period", "Warranty period"], "correct_answer": "Time to recover initial investment", "explanation": "Payback period is the time required for the cumulative cash flows to equal the initial investment."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Apply time value of money", "Evaluate engineering projects", "Conduct cost-benefit analysis", "Make economic engineering decisions"]
    },
    "engr320": {
        "title": "Systems Engineering",
        "topics": ["Systems Thinking", "Requirements Analysis", "System Integration", "Testing", "Lifecycle Management"],
        "lessons": [
            {"id": "lesson_1", "topic": "Systems", "title": "Systems Approach", "content": "Understand how components interact in complex systems.", "duration_minutes": 30, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Integration", "title": "System Integration", "content": "Integrate subsystems into complete working systems.", "duration_minutes": 35, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Systems Engineering",
                "title": "Systems Fundamentals",
                "questions": [
                    {"id": "q1", "question": "What is systems thinking?", "options": ["Thinking about systems", "Understanding how parts of a system interact and affect the whole", "Computer systems", "Systematic approach"], "correct_answer": "Understanding how parts of a system interact and affect the whole", "explanation": "Systems thinking considers the relationships and interactions between components rather than isolated parts."},
                    {"id": "q2", "question": "What is a system requirement?", "options": ["A request", "A documented need that the system must satisfy", "A suggestion", "A design choice"], "correct_answer": "A documented need that the system must satisfy", "explanation": "Requirements specify what a system must do or properties it must have to satisfy stakeholder needs."},
                    {"id": "q3", "question": "What is system integration testing?", "options": ["Testing one component", "Testing how components work together as a system", "Final testing", "User testing"], "correct_answer": "Testing how components work together as a system", "explanation": "Integration testing verifies that subsystems work correctly together when combined into the complete system."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Apply systems thinking", "Develop requirements", "Integrate complex systems", "Manage system lifecycle"]
    },
    "engr401": {
        "title": "Senior Capstone Project I",
        "topics": ["Project Planning", "Design", "Team Collaboration", "Documentation", "Milestones"],
        "lessons": [
            {"id": "lesson_1", "topic": "Planning", "title": "Project Planning", "content": "Plan and manage a major engineering project.", "duration_minutes": 30, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Design", "title": "Detailed Design", "content": "Create detailed designs and specifications.", "duration_minutes": 35, "difficulty": "high"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Capstone",
                "title": "Senior Project",
                "questions": [
                    {"id": "q1", "question": "What is a project charter?", "options": ["A boat rental", "A document authorizing a project and defining objectives", "A team agreement", "A schedule"], "correct_answer": "A document authorizing a project and defining objectives", "explanation": "A project charter formally authorizes a project and documents initial requirements, objectives, and stakeholders."},
                    {"id": "q2", "question": "What is a Gantt chart?", "options": ["A type of graph", "A visual project schedule showing tasks and timelines", "A flowchart", "An organization chart"], "correct_answer": "A visual project schedule showing tasks and timelines", "explanation": "A Gantt chart displays project tasks along a timeline, showing start/end dates and dependencies."},
                    {"id": "q3", "question": "What is the critical path?", "options": ["The most important task", "The longest sequence of dependent tasks determining project duration", "The first tasks", "The final deadline"], "correct_answer": "The longest sequence of dependent tasks determining project duration", "explanation": "The critical path is the sequence of tasks that determines the minimum project duration; delays on this path delay the entire project."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Plan engineering projects", "Design complex systems", "Work in teams", "Document technical work"]
    },
    "engr402": {
        "title": "Senior Capstone Project II",
        "topics": ["Implementation", "Testing", "Presentation", "Delivery", "Reflection"],
        "lessons": [
            {"id": "lesson_1", "topic": "Testing", "title": "System Testing", "content": "Comprehensively test your engineering project.", "duration_minutes": 30, "difficulty": "high"},
            {"id": "lesson_2", "topic": "Presentation", "title": "Professional Presentations", "content": "Present technical work to diverse audiences.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Project Completion",
                "title": "Capstone Completion",
                "questions": [
                    {"id": "q1", "question": "What is acceptance testing?", "options": ["Testing during development", "Final testing to verify the system meets requirements", "Stress testing", "Unit testing"], "correct_answer": "Final testing to verify the system meets requirements", "explanation": "Acceptance testing validates that the completed system meets all requirements and is ready for delivery."},
                    {"id": "q2", "question": "What should a technical presentation include?", "options": ["Only results", "Problem, approach, results, and conclusions", "Just PowerPoint", "Personal stories"], "correct_answer": "Problem, approach, results, and conclusions", "explanation": "Effective technical presentations cover the problem statement, methodology, results, and conclusions/recommendations."},
                    {"id": "q3", "question": "What is a lessons-learned document?", "options": ["Class notes", "Documentation of what worked well and what could be improved", "Project summary", "Technical manual"], "correct_answer": "Documentation of what worked well and what could be improved", "explanation": "Lessons-learned documents capture successes and areas for improvement to benefit future projects."}
                ],
                "passing_score": 70,
                "difficulty": "high"
            }
        ],
        "learning_outcomes": ["Complete engineering projects", "Conduct comprehensive testing", "Present technical work professionally", "Reflect on engineering practice"]
    },
    "engr410": {
        "title": "Engineering Ethics",
        "topics": ["Professional Responsibility", "Safety", "Environmental Impact", "Ethical Frameworks", "Case Studies"],
        "lessons": [
            {"id": "lesson_1", "topic": "Ethics", "title": "Engineering Ethics", "content": "Understand ethical obligations and professional responsibility.", "duration_minutes": 25, "difficulty": "beginner"},
            {"id": "lesson_2", "topic": "Cases", "title": "Case Studies", "content": "Analyze real engineering ethical dilemmas.", "duration_minutes": 20, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Ethics",
                "title": "Engineering Ethics",
                "questions": [
                    {"id": "q1", "question": "What is the first canon of engineering ethics?", "options": ["Maximize profit", "Hold paramount the safety, health, and welfare of the public", "Follow orders", "Meet deadlines"], "correct_answer": "Hold paramount the safety, health, and welfare of the public", "explanation": "Engineers must prioritize public safety, health, and welfare above all other considerations."},
                    {"id": "q2", "question": "What should you do if asked to compromise safety for cost savings?", "options": ["Comply to keep your job", "Refuse and report the issue appropriately", "Ignore it", "Ask for more money"], "correct_answer": "Refuse and report the issue appropriately", "explanation": "Engineers must refuse to compromise public safety and report unethical directives through proper channels."},
                    {"id": "q3", "question": "What is informed consent?", "options": ["Agreement to terms", "People affected understanding and agreeing to potential risks", "Legal document", "Safety waiver"], "correct_answer": "People affected understanding and agreeing to potential risks", "explanation": "Informed consent means those affected by engineering decisions understand and voluntarily accept the associated risks."}
                ],
                "passing_score": 70,
                "difficulty": "beginner"
            }
        ],
        "learning_outcomes": ["Understand engineering ethics", "Recognize ethical dilemmas", "Apply ethical frameworks", "Make responsible decisions"]
    },
    "engr420": {
        "title": "Engineering Management",
        "topics": ["Project Management", "Leadership", "Budgeting", "Risk Management", "Team Building"],
        "lessons": [
            {"id": "lesson_1", "topic": "Management", "title": "Managing Engineering Projects", "content": "Learn to manage technical projects and teams.", "duration_minutes": 30, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Leadership", "title": "Technical Leadership", "content": "Develop leadership skills for engineering roles.", "duration_minutes": 25, "difficulty": "intermediate"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Management",
                "title": "Engineering Management",
                "questions": [
                    {"id": "q1", "question": "What is the purpose of a project risk register?", "options": ["List of risks", "Document identifying, assessing, and tracking project risks", "Insurance policy", "Safety checklist"], "correct_answer": "Document identifying, assessing, and tracking project risks", "explanation": "A risk register identifies potential risks, assesses their likelihood and impact, and tracks mitigation strategies."},
                    {"id": "q2", "question": "What is servant leadership?", "options": ["Being subservient", "Leading by serving and empowering team members", "Following others", "Delegating everything"], "correct_answer": "Leading by serving and empowering team members", "explanation": "Servant leadership focuses on serving team members' needs and helping them develop and perform at their best."},
                    {"id": "q3", "question": "What is scope creep?", "options": ["Slow progress", "Uncontrolled expansion of project scope", "Team expansion", "Budget increase"], "correct_answer": "Uncontrolled expansion of project scope", "explanation": "Scope creep is the uncontrolled addition of features or requirements beyond the original project scope."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Manage engineering projects", "Lead technical teams", "Control budgets and schedules", "Mitigate project risks"]
    },
    "engr430": {
        "title": "Professional Practice",
        "topics": ["Professional Licensure", "FE Exam", "PE License", "Continuing Education", "Career Development"],
        "lessons": [
            {"id": "lesson_1", "topic": "Licensure", "title": "Engineering Licensure", "content": "Understand the path to professional engineering licensure.", "duration_minutes": 25, "difficulty": "intermediate"},
            {"id": "lesson_2", "topic": "Career", "title": "Career Development", "content": "Plan your engineering career path.", "duration_minutes": 20, "difficulty": "beginner"}
        ],
        "quizzes": [
            {
                "id": "quiz_1",
                "topic": "Professional Practice",
                "title": "PE and Career",
                "questions": [
                    {"id": "q1", "question": "What is the FE exam?", "options": ["Final engineering exam", "Fundamentals of Engineering exam - first step to PE license", "Failure exam", "Federal exam"], "correct_answer": "Fundamentals of Engineering exam - first step to PE license", "explanation": "The FE (Fundamentals of Engineering) exam is the first step toward Professional Engineer licensure."},
                    {"id": "q2", "question": "What does PE stand for?", "options": ["Physical Education", "Professional Engineer", "Project Engineer", "Public Engineer"], "correct_answer": "Professional Engineer", "explanation": "PE (Professional Engineer) is a licensed engineer who can sign and seal engineering documents."},
                    {"id": "q3", "question": "Why is continuing education important for engineers?", "options": ["It's not important", "To stay current with technology and maintain licensure", "Only for promotions", "Required by universities"], "correct_answer": "To stay current with technology and maintain licensure", "explanation": "Continuing education keeps engineers updated with new technologies and is required to maintain PE licensure."}
                ],
                "passing_score": 70,
                "difficulty": "intermediate"
            }
        ],
        "learning_outcomes": ["Understand licensure requirements", "Prepare for FE exam", "Plan career development", "Commit to lifelong learning"]
    }
}

# Print the script's purpose
print("=" * 80)
print("COURSE CONTENT GENERATION SCRIPT")
print("=" * 80)
print(f"\nThis script will add {len(COURSES_TO_ADD)} courses to course_content.py")
print("\nCourses to add:")
for course_id in sorted(COURSES_TO_ADD.keys()):
    print(f"  - {course_id}: {COURSES_TO_ADD[course_id]['title']}")
print("\n" + "=" * 80)

# Create the content string to append
content_to_append = ""
for course_id, course_data in COURSES_TO_ADD.items():
    content_to_append += f'    "{course_id}": {{\n'
    content_to_append += f'        "title": "{course_data["title"]}",\n'
    content_to_append += f'        "topics": {course_data["topics"]},\n'
    content_to_append += f'        "lessons": [\n'
    
    for lesson in course_data["lessons"]:
        content_to_append += f'            {lesson},\n'
    
    content_to_append += f'        ],\n'
    content_to_append += f'        "quizzes": [\n'
    
    for quiz in course_data["quizzes"]:
        content_to_append += '            {\n'
        content_to_append += f'                "id": "{quiz["id"]}",\n'
        content_to_append += f'                "topic": "{quiz["topic"]}",\n'
        content_to_append += f'                "title": "{quiz["title"]}",\n'
        content_to_append += '                "questions": [\n'
        
        for q in quiz["questions"]:
            content_to_append += '                    {\n'
            content_to_append += f'                        "id": "{q["id"]}",\n'
            content_to_append += f'                        "question": "{q["question"]}",\n'
            content_to_append += f'                        "options": {q["options"]},\n'
            content_to_append += f'                        "correct_answer": "{q["correct_answer"]}",\n'
            content_to_append += f'                        "explanation": "{q["explanation"]}"\n'
            content_to_append += '                    },\n'
        
        # Remove last comma
        content_to_append = content_to_append.rstrip(',\n') + '\n'
        content_to_append += '                ],\n'
        content_to_append += f'                "passing_score": {quiz["passing_score"]},\n'
        content_to_append += f'                "difficulty": "{quiz["difficulty"]}"\n'
        content_to_append += '            },\n'
    
    # Remove last comma
    content_to_append = content_to_append.rstrip(',\n') + '\n'
    content_to_append += '        ],\n'
    content_to_append += f'        "learning_outcomes": {course_data["learning_outcomes"]}\n'
    content_to_append += '    },\n'

print("\nCourse data structure created successfully!")
print(f"Generated {len(content_to_append.split('quiz_'))-1} quizzes across {len(COURSES_TO_ADD)} courses")
print("\nTo apply these changes:")
print("1. Review the data above")
print("2. Add the content to catalogs/course_content.py before the closing }")
print("\nAll quizzes use correct_answer as TEXT (not index), as required!")
