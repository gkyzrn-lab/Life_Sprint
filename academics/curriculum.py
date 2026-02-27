from academics.curriculum_models import SemesterCurriculum, Course, CurriculumTopic

# Complete 4-year curriculum for all majors
CURRICULUM = {
    "nyc_public": {
        # ===== COMPUTER SCIENCE TRACK =====
        "cs": {
            1: SemesterCurriculum(
                semester=1,
                notes="Foundation & Programming Basics",
                courses=[
                    Course(id="cs101", title="Intro Programming", credits=4, difficulty=4, weekly_hours=10, skills=["Python", "Problem Solving"]),
                    Course(id="cs102", title="Computer Science Fundamentals", credits=3, difficulty=4, weekly_hours=6, skills=["Logic", "Binary"]),
                    Course(id="math101", title="Calculus I", credits=4, difficulty=5, weekly_hours=8, skills=["Calculus", "Math"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Data Structures & Algorithms",
                courses=[
                    Course(id="cs201", title="Data Structures", credits=4, difficulty=5, weekly_hours=10, skills=["Algorithms", "Data Structures"]),
                    Course(id="cs202", title="Discrete Mathematics", credits=3, difficulty=6, weekly_hours=7, skills=["Logic", "Proofs"]),
                    Course(id="math102", title="Calculus II", credits=4, difficulty=5, weekly_hours=8, skills=["Calculus", "Integration"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Object-Oriented Programming & Systems",
                courses=[
                    Course(id="cs301", title="Object-Oriented Programming", credits=4, difficulty=5, weekly_hours=10, skills=["OOP", "Java", "Design"]),
                    Course(id="cs302", title="Computer Organization", credits=3, difficulty=6, weekly_hours=7, skills=["Architecture", "CPU"]),
                    Course(id="cs303", title="Database Systems", credits=3, difficulty=5, weekly_hours=6, skills=["SQL", "Database Design"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Algorithms & Analysis",
                courses=[
                    Course(id="cs401", title="Advanced Algorithms", credits=4, difficulty=7, weekly_hours=10, skills=["Algorithms", "Complexity"]),
                    Course(id="cs402", title="Software Engineering", credits=3, difficulty=5, weekly_hours=6, skills=["Design Patterns", "Testing"]),
                    Course(id="elec1", title="Technical Elective I", credits=3, difficulty=5, weekly_hours=6, skills=["Specialization"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Upper-Level Specialization",
                courses=[
                    Course(id="cs501", title="Operating Systems", credits=4, difficulty=7, weekly_hours=10, skills=["Systems", "C", "Concurrency"]),
                    Course(id="cs502", title="Theory of Computation", credits=3, difficulty=7, weekly_hours=7, skills=["Formal Languages", "Automata"]),
                    Course(id="elec2", title="Technical Elective II", credits=3, difficulty=5, weekly_hours=6, skills=["Specialization"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Advanced Topics & Systems",
                courses=[
                    Course(id="cs601", title="Machine Learning", credits=3, difficulty=7, weekly_hours=8, skills=["ML", "Python", "Statistics"]),
                    Course(id="cs602", title="Compiler Design", credits=3, difficulty=7, weekly_hours=6, skills=["Compilers", "Parsing"]),
                    Course(id="elec3", title="Technical Elective III", credits=3, difficulty=5, weekly_hours=6, skills=["Specialization"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Capstone & Professional",
                courses=[
                    Course(id="cs701", title="Cybersecurity Fundamentals", credits=3, difficulty=6, weekly_hours=7, skills=["Security", "Cryptography"]),
                    Course(id="cs702", title="Advanced Networking", credits=3, difficulty=6, weekly_hours=6, skills=["Networking", "Protocols"]),
                    Course(id="elec4", title="Technical Elective IV", credits=3, difficulty=5, weekly_hours=6, skills=["Specialization"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone Project & Career Preparation",
                courses=[
                    Course(id="cs801", title="Capstone Project I", credits=4, difficulty=7, weekly_hours=10, skills=["Project Management", "Integration"]),
                    Course(id="cs802", title="Professional Development", credits=1, difficulty=2, weekly_hours=2, skills=["Resume", "Interview"]),
                ],
            ),
        },
        
        # ===== BUSINESS TRACK =====
        "ba": {
            1: SemesterCurriculum(
                semester=1,
                notes="Business Foundation",
                courses=[
                    Course(id="ba101", title="Intro Business", credits=3, difficulty=3, weekly_hours=6, skills=["Business Fundamentals"]),
                    Course(id="ba102", title="Accounting Principles", credits=3, difficulty=4, weekly_hours=6, skills=["Accounting", "Finance"]),
                    Course(id="econ101", title="Microeconomics", credits=3, difficulty=4, weekly_hours=6, skills=["Economics", "Markets"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Economics & Financial Analysis",
                courses=[
                    Course(id="ba201", title="Business Communication", credits=3, difficulty=3, weekly_hours=5, skills=["Writing", "Presentation"]),
                    Course(id="econ102", title="Macroeconomics", credits=3, difficulty=4, weekly_hours=6, skills=["Economics", "Policy"]),
                    Course(id="ba202", title="Financial Accounting", credits=3, difficulty=4, weekly_hours=7, skills=["Accounting", "Financial Statements"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Management & Marketing",
                courses=[
                    Course(id="ba301", title="Management Principles", credits=3, difficulty=4, weekly_hours=6, skills=["Leadership", "Organization"]),
                    Course(id="ba302", title="Marketing Fundamentals", credits=3, difficulty=4, weekly_hours=6, skills=["Marketing", "Consumer Behavior"]),
                    Course(id="ba303", title="Organizational Behavior", credits=3, difficulty=4, weekly_hours=6, skills=["Psychology", "Teams"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Finance & Strategy",
                courses=[
                    Course(id="ba401", title="Corporate Finance", credits=3, difficulty=5, weekly_hours=7, skills=["Finance", "Valuation"]),
                    Course(id="ba402", title="Strategic Management", credits=3, difficulty=5, weekly_hours=6, skills=["Strategy", "Analysis"]),
                    Course(id="ba403", title="Operations Management", credits=3, difficulty=4, weekly_hours=6, skills=["Operations", "Supply Chain"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Specialized Business Topics",
                courses=[
                    Course(id="ba501", title="Entrepreneurship", credits=3, difficulty=5, weekly_hours=6, skills=["Innovation", "Startup"]),
                    Course(id="ba502", title="Business Analytics", credits=3, difficulty=5, weekly_hours=7, skills=["Data Analysis", "Statistics"]),
                    Course(id="ba503", title="International Business", credits=3, difficulty=4, weekly_hours=6, skills=["Global Markets", "Trade"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Advanced Specialization",
                courses=[
                    Course(id="ba601", title="Digital Marketing", credits=3, difficulty=4, weekly_hours=6, skills=["Social Media", "Analytics"]),
                    Course(id="ba602", title="Investment Analysis", credits=3, difficulty=5, weekly_hours=7, skills=["Investing", "Portfolio"]),
                    Course(id="ba603", title="Business Ethics", credits=3, difficulty=3, weekly_hours=5, skills=["Ethics", "Leadership"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Capstone Preparation",
                courses=[
                    Course(id="ba701", title="Business Policy", credits=3, difficulty=5, weekly_hours=6, skills=["Policy", "Decision Making"]),
                    Course(id="ba702", title="Consulting Project", credits=3, difficulty=5, weekly_hours=8, skills=["Consulting", "Problem Solving"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career Readiness",
                courses=[
                    Course(id="ba801", title="Capstone Case Study", credits=3, difficulty=5, weekly_hours=8, skills=["Integration", "Analysis"]),
                    Course(id="ba802", title="Career Readiness", credits=1, difficulty=2, weekly_hours=2, skills=["Networking", "Job Search"]),
                ],
            ),
        },
        
        # ===== ENGINEERING TRACK =====
        "eng": {
            1: SemesterCurriculum(
                semester=1,
                notes="Engineering Foundation",
                courses=[
                    Course(id="eng101", title="Engineering Design", credits=3, difficulty=4, weekly_hours=8, skills=["Design", "CAD"]),
                    Course(id="phys101", title="Physics I", credits=4, difficulty=5, weekly_hours=9, skills=["Mechanics", "Physics"]),
                    Course(id="math101", title="Calculus I", credits=4, difficulty=5, weekly_hours=8, skills=["Calculus", "Math"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Physics & Mathematics",
                courses=[
                    Course(id="phys102", title="Physics II", credits=4, difficulty=5, weekly_hours=9, skills=["Electricity", "Waves"]),
                    Course(id="math102", title="Calculus II", credits=4, difficulty=5, weekly_hours=8, skills=["Integration", "Calculus"]),
                    Course(id="eng102", title="Engineering Analysis", credits=3, difficulty=4, weekly_hours=6, skills=["Statics", "Analysis"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Circuits & Materials",
                courses=[
                    Course(id="eng301", title="Circuit Analysis", credits=4, difficulty=5, weekly_hours=9, skills=["Electronics", "Circuits"]),
                    Course(id="eng302", title="Materials Science", credits=3, difficulty=5, weekly_hours=7, skills=["Materials", "Properties"]),
                    Course(id="math201", title="Linear Algebra", credits=3, difficulty=5, weekly_hours=6, skills=["Linear Algebra", "Matrices"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Systems & Thermodynamics",
                courses=[
                    Course(id="eng401", title="Thermodynamics", credits=4, difficulty=6, weekly_hours=9, skills=["Thermodynamics", "Energy"]),
                    Course(id="eng402", title="Digital Systems", credits=3, difficulty=5, weekly_hours=8, skills=["Digital Logic", "HDL"]),
                    Course(id="eng403", title="Signal Processing", credits=3, difficulty=6, weekly_hours=7, skills=["Signals", "Filtering"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Control & Advanced Topics",
                courses=[
                    Course(id="eng501", title="Control Systems", credits=4, difficulty=6, weekly_hours=8, skills=["Controls", "Feedback"]),
                    Course(id="eng502", title="Power Systems", credits=3, difficulty=6, weekly_hours=7, skills=["Power", "Grid"]),
                    Course(id="eng503", title="Mechanical Design", credits=3, difficulty=5, weekly_hours=8, skills=["Mechanical Design", "CAD"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Specialization & Applications",
                courses=[
                    Course(id="eng601", title="Advanced Controls", credits=3, difficulty=7, weekly_hours=7, skills=["Advanced Control", "Optimization"]),
                    Course(id="eng602", title="Renewable Energy", credits=3, difficulty=5, weekly_hours=6, skills=["Solar", "Wind"]),
                    Course(id="eng603", title="Engineering Management", credits=3, difficulty=4, weekly_hours=5, skills=["Project Management", "Leadership"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Capstone Preparation",
                courses=[
                    Course(id="eng701", title="Systems Integration", credits=3, difficulty=6, weekly_hours=7, skills=["Integration", "Testing"]),
                    Course(id="eng702", title="Engineering Ethics", credits=2, difficulty=2, weekly_hours=3, skills=["Ethics", "Professional"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone Project & Professional",
                courses=[
                    Course(id="eng801", title="Capstone Design Project", credits=4, difficulty=7, weekly_hours=10, skills=["Design", "Integration"]),
                    Course(id="eng802", title="Professional Practice", credits=1, difficulty=2, weekly_hours=2, skills=["PE Prep", "Career"]),
                ],
            ),
        },
    },
    
    # ===== PRIVATE UNIVERSITY VARIANT =====
    "nyc_private": {
        "cs": {
            1: SemesterCurriculum(
                semester=1,
                notes="Foundation & Programming Basics (Private)",
                courses=[
                    Course(id="csP101", title="Intro Programming (Private)", credits=4, difficulty=4, weekly_hours=11, skills=["Python", "Problem Solving", "Mentoring"]),
                    Course(id="csP102", title="Computer Science Fundamentals", credits=3, difficulty=4, weekly_hours=7, skills=["Logic", "Binary"]),
                    Course(id="mathP101", title="Calculus I (Honors)", credits=4, difficulty=6, weekly_hours=9, skills=["Calculus", "Proofs"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Data Structures & Algorithms (Private)",
                courses=[
                    Course(id="csP201", title="Data Structures", credits=4, difficulty=6, weekly_hours=11, skills=["Algorithms", "Data Structures"]),
                    Course(id="csP202", title="Discrete Mathematics", credits=3, difficulty=7, weekly_hours=8, skills=["Logic", "Proofs", "Advanced Math"]),
                    Course(id="mathP102", title="Calculus II (Honors)", credits=4, difficulty=6, weekly_hours=9, skills=["Calculus", "Series"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="OOP & Systems",
                courses=[
                    Course(id="csP301", title="Object-Oriented Programming", credits=4, difficulty=5, weekly_hours=11, skills=["OOP", "Design Patterns", "Java"]),
                    Course(id="csP302", title="Computer Organization", credits=3, difficulty=6, weekly_hours=8, skills=["Architecture", "Assembly"]),
                    Course(id="csP303", title="Database Design", credits=3, difficulty=5, weekly_hours=7, skills=["SQL", "Database"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Algorithms & Advanced Topics",
                courses=[
                    Course(id="csP401", title="Advanced Algorithms", credits=4, difficulty=8, weekly_hours=11, skills=["Complexity", "Optimization"]),
                    Course(id="csP402", title="Software Engineering", credits=3, difficulty=6, weekly_hours=7, skills=["Design Patterns", "Agile"]),
                    Course(id="elecP1", title="Research Seminar", credits=3, difficulty=6, weekly_hours=6, skills=["Research"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Systems & Specialization",
                courses=[
                    Course(id="csP501", title="Operating Systems", credits=4, difficulty=7, weekly_hours=11, skills=["Systems", "Concurrency"]),
                    Course(id="csP502", title="Theory of Computation", credits=3, difficulty=8, weekly_hours=8, skills=["Formal Languages"]),
                    Course(id="elecP2", title="Distributed Systems", credits=3, difficulty=7, weekly_hours=7, skills=["Distributed Computing"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="AI & Specialization",
                courses=[
                    Course(id="csP601", title="Machine Learning", credits=3, difficulty=8, weekly_hours=9, skills=["ML", "Deep Learning"]),
                    Course(id="csP602", title="Compiler Design", credits=3, difficulty=8, weekly_hours=7, skills=["Compilers", "Language Design"]),
                    Course(id="elecP3", title="Research Project", credits=3, difficulty=7, weekly_hours=8, skills=["Research", "Innovation"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Advanced Topics",
                courses=[
                    Course(id="csP701", title="Cybersecurity", credits=3, difficulty=7, weekly_hours=8, skills=["Security", "Cryptography"]),
                    Course(id="csP702", title="Computer Networks", credits=3, difficulty=7, weekly_hours=7, skills=["Networking", "Protocols"]),
                    Course(id="elecP4", title="Advanced Topics", credits=3, difficulty=7, weekly_hours=6, skills=["Specialization"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Professional",
                courses=[
                    Course(id="csP801", title="Capstone Project II", credits=4, difficulty=8, weekly_hours=11, skills=["Integration", "Research"]),
                    Course(id="csP802", title="Professional Development", credits=1, difficulty=2, weekly_hours=2, skills=["Career"]),
                ],
            ),
        },
        "ba": {
            1: SemesterCurriculum(
                semester=1,
                notes="Business Foundation (Private)",
                courses=[
                    Course(id="baP101", title="Intro Business (Private)", credits=3, difficulty=3, weekly_hours=7, skills=["Business Fundamentals", "Networking"]),
                    Course(id="baP102", title="Accounting Principles", credits=3, difficulty=4, weekly_hours=7, skills=["Accounting", "Finance"]),
                    Course(id="econP101", title="Microeconomics", credits=3, difficulty=4, weekly_hours=7, skills=["Economics"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Economics & Finance",
                courses=[
                    Course(id="baP201", title="Business Communication", credits=3, difficulty=3, weekly_hours=6, skills=["Presentation", "Writing"]),
                    Course(id="econP102", title="Macroeconomics", credits=3, difficulty=4, weekly_hours=7, skills=["Economics", "Policy"]),
                    Course(id="baP202", title="Financial Accounting", credits=3, difficulty=4, weekly_hours=8, skills=["Accounting"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Management & Marketing",
                courses=[
                    Course(id="baP301", title="Management Principles", credits=3, difficulty=4, weekly_hours=7, skills=["Leadership"]),
                    Course(id="baP302", title="Marketing Fundamentals", credits=3, difficulty=4, weekly_hours=7, skills=["Marketing"]),
                    Course(id="baP303", title="Organizational Behavior", credits=3, difficulty=4, weekly_hours=7, skills=["Psychology", "Teams"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Finance & Strategy",
                courses=[
                    Course(id="baP401", title="Corporate Finance", credits=3, difficulty=5, weekly_hours=8, skills=["Finance", "Valuation"]),
                    Course(id="baP402", title="Strategic Management", credits=3, difficulty=5, weekly_hours=7, skills=["Strategy"]),
                    Course(id="baP403", title="Operations Management", credits=3, difficulty=4, weekly_hours=7, skills=["Operations"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Specialized Topics",
                courses=[
                    Course(id="baP501", title="Entrepreneurship", credits=3, difficulty=5, weekly_hours=7, skills=["Innovation", "Startup"]),
                    Course(id="baP502", title="Business Analytics", credits=3, difficulty=5, weekly_hours=8, skills=["Analytics"]),
                    Course(id="baP503", title="International Business", credits=3, difficulty=4, weekly_hours=7, skills=["Global"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Advanced Specialization",
                courses=[
                    Course(id="baP601", title="Digital Marketing", credits=3, difficulty=4, weekly_hours=7, skills=["Social Media"]),
                    Course(id="baP602", title="Investment Analysis", credits=3, difficulty=5, weekly_hours=8, skills=["Investing"]),
                    Course(id="baP603", title="Business Ethics", credits=3, difficulty=3, weekly_hours=6, skills=["Ethics"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Capstone Preparation",
                courses=[
                    Course(id="baP701", title="Business Policy", credits=3, difficulty=5, weekly_hours=7, skills=["Policy"]),
                    Course(id="baP702", title="Consulting Project", credits=3, difficulty=5, weekly_hours=9, skills=["Consulting"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="baP801", title="Capstone Case Study", credits=3, difficulty=5, weekly_hours=9, skills=["Integration"]),
                    Course(id="baP802", title="Career Readiness", credits=1, difficulty=2, weekly_hours=2, skills=["Networking", "Job Search"]),
                ],
            ),
        },
    },
}
