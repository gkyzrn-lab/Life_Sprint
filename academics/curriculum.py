from academics.curriculum_models import SemesterCurriculum, Course, CurriculumTopic

# Complete 4-year curriculum for all majors at all colleges
# Key structure: CURRICULUM[college_id][major_id][semester] = SemesterCurriculum
CURRICULUM = {
    # ===== CUNY BARUCH (Public, Business-focused) =====
    "cuny_baruch": {
        # Business Administration at Baruch
        "ba": {
            1: SemesterCurriculum(
                semester=1,
                notes="Business Foundation",
                courses=[
                    Course(id="ba101", title="Intro to Business", credits=3, difficulty=3, weekly_hours=6, skills=["Business Fundamentals"]),
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
        # Accounting at Baruch
        "accounting": {
            1: SemesterCurriculum(
                semester=1,
                notes="Accounting Foundation",
                courses=[
                    Course(id="acc101", title="Principles of Accounting I", credits=3, difficulty=4, weekly_hours=7, skills=["Accounting Equation", "Debits/Credits"]),
                    Course(id="ba101", title="Intro to Business", credits=3, difficulty=3, weekly_hours=6, skills=["Business Fundamentals"]),
                    Course(id="econ101", title="Microeconomics", credits=3, difficulty=4, weekly_hours=6, skills=["Economics"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Financial Accounting",
                courses=[
                    Course(id="acc102", title="Principles of Accounting II", credits=3, difficulty=4, weekly_hours=7, skills=["Financial Statements", "GAAP"]),
                    Course(id="ba201", title="Business Communication", credits=3, difficulty=3, weekly_hours=5, skills=["Writing"]),
                    Course(id="econ102", title="Macroeconomics", credits=3, difficulty=4, weekly_hours=6, skills=["Economics"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Intermediate Accounting",
                courses=[
                    Course(id="acc301", title="Intermediate Accounting I", credits=3, difficulty=6, weekly_hours=9, skills=["Financial Reporting"]),
                    Course(id="acc302", title="Cost Accounting", credits=3, difficulty=5, weekly_hours=7, skills=["Costing", "Managerial"]),
                    Course(id="ba401", title="Corporate Finance", credits=3, difficulty=5, weekly_hours=7, skills=["Finance"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Advanced Accounting & Tax",
                courses=[
                    Course(id="acc401", title="Intermediate Accounting II", credits=3, difficulty=6, weekly_hours=9, skills=["Advanced Financial"]),
                    Course(id="acc402", title="Tax Accounting I", credits=3, difficulty=5, weekly_hours=7, skills=["Tax Law", "IRS"]),
                    Course(id="ba402", title="Strategic Management", credits=3, difficulty=5, weekly_hours=6, skills=["Strategy"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Audit & Tax Advanced",
                courses=[
                    Course(id="acc501", title="Auditing", credits=3, difficulty=6, weekly_hours=8, skills=["Audit", "Internal Controls"]),
                    Course(id="acc502", title="Tax Accounting II", credits=3, difficulty=5, weekly_hours=7, skills=["Corporate Tax"]),
                    Course(id="ba502", title="Business Analytics", credits=3, difficulty=5, weekly_hours=7, skills=["Analytics"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="CPA Preparation",
                courses=[
                    Course(id="acc601", title="Advanced Auditing", credits=3, difficulty=6, weekly_hours=8, skills=["CPA Prep"]),
                    Course(id="acc602", title="Accounting Information Systems", credits=3, difficulty=5, weekly_hours=6, skills=["IT", "ERP"]),
                    Course(id="acc603", title="Business Law", credits=3, difficulty=4, weekly_hours=6, skills=["Law", "Contracts"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Advanced Topics & Ethics",
                courses=[
                    Course(id="acc701", title="Advanced Tax", credits=3, difficulty=6, weekly_hours=7, skills=["Tax Strategy"]),
                    Course(id="acc702", title="Forensic Accounting", credits=3, difficulty=5, weekly_hours=6, skills=["Fraud Detection"]),
                    Course(id="ba603", title="Business Ethics", credits=3, difficulty=3, weekly_hours=5, skills=["Ethics"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & CPA Exam Prep",
                courses=[
                    Course(id="acc801", title="Accounting Capstone", credits=3, difficulty=6, weekly_hours=8, skills=["Integration", "CPA Prep"]),
                    Course(id="acc802", title="Professional Practice", credits=1, difficulty=2, weekly_hours=2, skills=["Career", "CPA Exam"]),
                ],
            ),
        },
        # Economics at Baruch
        "economics": {
            1: SemesterCurriculum(
                semester=1,
                notes="Economics Foundation",
                courses=[
                    Course(id="econ101", title="Microeconomics", credits=3, difficulty=4, weekly_hours=6, skills=["Micro", "Markets"]),
                    Course(id="econ102", title="Macroeconomics", credits=3, difficulty=4, weekly_hours=6, skills=["Macro", "Policy"]),
                    Course(id="math101", title="Calculus I", credits=4, difficulty=5, weekly_hours=8, skills=["Calculus"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Intermediate Economics",
                courses=[
                    Course(id="econ201", title="Intermediate Microeconomics", credits=3, difficulty=5, weekly_hours=7, skills=["Consumer Theory"]),
                    Course(id="econ202", title="Intermediate Macroeconomics", credits=3, difficulty=5, weekly_hours=7, skills=["IS-LM", "Growth"]),
                    Course(id="math102", title="Calculus II", credits=4, difficulty=5, weekly_hours=8, skills=["Calculus"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Econometrics & Statistics",
                courses=[
                    Course(id="econ301", title="Econometrics I", credits=3, difficulty=6, weekly_hours=8, skills=["Regression", "Stats"]),
                    Course(id="econ302", title="Game Theory", credits=3, difficulty=6, weekly_hours=7, skills=["Strategy", "Incentives"]),
                    Course(id="math201", title="Linear Algebra", credits=3, difficulty=5, weekly_hours=6, skills=["Matrices"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Applied Economics",
                courses=[
                    Course(id="econ401", title="Labor Economics", credits=3, difficulty=5, weekly_hours=6, skills=["Labor Markets"]),
                    Course(id="econ402", title="Public Economics", credits=3, difficulty=5, weekly_hours=6, skills=["Tax", "Policy"]),
                    Course(id="econ403", title="Econometrics II", credits=3, difficulty=6, weekly_hours=8, skills=["Advanced Stats"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Specialized Topics",
                courses=[
                    Course(id="econ501", title="International Trade", credits=3, difficulty=5, weekly_hours=6, skills=["Trade", "Comparative Advantage"]),
                    Course(id="econ502", title="Monetary Economics", credits=3, difficulty=5, weekly_hours=6, skills=["Fed", "Interest Rates"]),
                    Course(id="econ503", title="Development Economics", credits=3, difficulty=5, weekly_hours=6, skills=["Growth", "Poverty"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Advanced Topics",
                courses=[
                    Course(id="econ601", title="Industrial Organization", credits=3, difficulty=6, weekly_hours=7, skills=["Market Structure"]),
                    Course(id="econ602", title="Behavioral Economics", credits=3, difficulty=5, weekly_hours=6, skills=["Psychology", "Decisions"]),
                    Course(id="econ603", title="Environmental Economics", credits=3, difficulty=5, weekly_hours=6, skills=["Climate", "Externalities"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Research Methods",
                courses=[
                    Course(id="econ701", title="Advanced Econometrics", credits=3, difficulty=7, weekly_hours=8, skills=["Causal Inference"]),
                    Course(id="econ702", title="Economic Research Methods", credits=3, difficulty=6, weekly_hours=7, skills=["Research Design"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="econ801", title="Economics Capstone", credits=3, difficulty=6, weekly_hours=9, skills=["Thesis", "Research"]),
                    Course(id="econ802", title="Career Preparation", credits=1, difficulty=2, weekly_hours=2, skills=["Career"]),
                ],
            ),
        },
        # Finance at Baruch
        "finance": {
            1: SemesterCurriculum(
                semester=1,
                notes="Finance Foundation",
                courses=[
                    Course(id="fin101", title="Intro to Finance", credits=3, difficulty=4, weekly_hours=6, skills=["Finance Basics"]),
                    Course(id="ba102", title="Accounting Principles", credits=3, difficulty=4, weekly_hours=6, skills=["Accounting"]),
                    Course(id="econ101", title="Microeconomics", credits=3, difficulty=4, weekly_hours=6, skills=["Economics"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Financial Markets",
                courses=[
                    Course(id="fin201", title="Financial Markets", credits=3, difficulty=4, weekly_hours=7, skills=["Markets", "Trading"]),
                    Course(id="econ102", title="Macroeconomics", credits=3, difficulty=4, weekly_hours=6, skills=["Economics"]),
                    Course(id="ba202", title="Financial Accounting", credits=3, difficulty=4, weekly_hours=7, skills=["Accounting"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Corporate Finance",
                courses=[
                    Course(id="fin301", title="Corporate Finance", credits=3, difficulty=5, weekly_hours=8, skills=["Valuation", "DCF"]),
                    Course(id="fin302", title="Investment Analysis", credits=3, difficulty=5, weekly_hours=7, skills=["Equity Analysis"]),
                    Course(id="ba301", title="Management Principles", credits=3, difficulty=4, weekly_hours=6, skills=["Management"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Portfolio & Derivatives",
                courses=[
                    Course(id="fin401", title="Portfolio Management", credits=3, difficulty=6, weekly_hours=8, skills=["Portfolio Theory"]),
                    Course(id="fin402", title="Derivatives", credits=3, difficulty=6, weekly_hours=8, skills=["Options", "Futures"]),
                    Course(id="ba502", title="Business Analytics", credits=3, difficulty=5, weekly_hours=7, skills=["Analytics"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Advanced Finance",
                courses=[
                    Course(id="fin501", title="Fixed Income Securities", credits=3, difficulty=6, weekly_hours=7, skills=["Bonds", "Yield"]),
                    Course(id="fin502", title="Risk Management", credits=3, difficulty=5, weekly_hours=7, skills=["Hedging", "Risk"]),
                    Course(id="fin503", title="International Finance", credits=3, difficulty=5, weekly_hours=6, skills=["FX", "Global"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Specialized Finance",
                courses=[
                    Course(id="fin601", title="M&A and Corporate Restructuring", credits=3, difficulty=6, weekly_hours=8, skills=["M&A", "LBO"]),
                    Course(id="fin602", title="Real Estate Finance", credits=3, difficulty=5, weekly_hours=6, skills=["Real Estate"]),
                    Course(id="fin603", title="Fintech & Digital Banking", credits=3, difficulty=5, weekly_hours=6, skills=["Fintech"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Capstone Preparation",
                courses=[
                    Course(id="fin701", title="Financial Modeling", credits=3, difficulty=6, weekly_hours=8, skills=["Excel", "Modeling"]),
                    Course(id="fin702", title="Investment Banking", credits=3, difficulty=6, weekly_hours=8, skills=["IB", "M&A"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="fin801", title="Finance Capstone", credits=3, difficulty=6, weekly_hours=9, skills=["Integration"]),
                    Course(id="fin802", title="CFA Prep / Career Readiness", credits=1, difficulty=2, weekly_hours=2, skills=["CFA", "Career"]),
                ],
            ),
        },
        # Liberal Arts at Baruch
        "liberal_arts": {
            1: SemesterCurriculum(
                semester=1,
                notes="Liberal Arts Foundation",
                courses=[
                    Course(id="lib101", title="Critical Thinking", credits=3, difficulty=3, weekly_hours=5, skills=["Logic", "Reasoning"]),
                    Course(id="lib102", title="World History", credits=3, difficulty=3, weekly_hours=6, skills=["History"]),
                    Course(id="lib103", title="English Composition", credits=3, difficulty=3, weekly_hours=6, skills=["Writing"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Humanities & Social Science",
                courses=[
                    Course(id="lib201", title="Philosophy", credits=3, difficulty=4, weekly_hours=6, skills=["Ethics", "Philosophy"]),
                    Course(id="lib202", title="Sociology", credits=3, difficulty=3, weekly_hours=6, skills=["Society"]),
                    Course(id="lib203", title="Literature", credits=3, difficulty=3, weekly_hours=6, skills=["Reading", "Analysis"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Cultural Studies",
                courses=[
                    Course(id="lib301", title="Art History", credits=3, difficulty=3, weekly_hours=6, skills=["Art", "Culture"]),
                    Course(id="lib302", title="Political Science", credits=3, difficulty=4, weekly_hours=6, skills=["Politics"]),
                    Course(id="lib303", title="Psychology", credits=3, difficulty=4, weekly_hours=6, skills=["Psych"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Advanced Humanities",
                courses=[
                    Course(id="lib401", title="Ethics & Society", credits=3, difficulty=4, weekly_hours=6, skills=["Ethics"]),
                    Course(id="lib402", title="Gender Studies", credits=3, difficulty=4, weekly_hours=6, skills=["Gender", "Culture"]),
                    Course(id="lib403", title="Environmental Studies", credits=3, difficulty=4, weekly_hours=6, skills=["Environment"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Specialization",
                courses=[
                    Course(id="lib501", title="Modern Philosophy", credits=3, difficulty=5, weekly_hours=7, skills=["Philosophy"]),
                    Course(id="lib502", title="Cultural Anthropology", credits=3, difficulty=4, weekly_hours=6, skills=["Anthropology"]),
                    Course(id="lib503", title="Creative Writing", credits=3, difficulty=4, weekly_hours=6, skills=["Writing"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Advanced Topics",
                courses=[
                    Course(id="lib601", title="Global Studies", credits=3, difficulty=4, weekly_hours=6, skills=["Global"]),
                    Course(id="lib602", title="Media Studies", credits=3, difficulty=4, weekly_hours=6, skills=["Media"]),
                    Course(id="lib603", title="Urban Studies", credits=3, difficulty=4, weekly_hours=6, skills=["Cities"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Senior Seminar",
                courses=[
                    Course(id="lib701", title="Senior Seminar", credits=3, difficulty=5, weekly_hours=7, skills=["Research"]),
                    Course(id="lib702", title="Independent Study", credits=3, difficulty=5, weekly_hours=8, skills=["Self-Direction"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone Project",
                courses=[
                    Course(id="lib801", title="Liberal Arts Capstone", credits=3, difficulty=5, weekly_hours=9, skills=["Integration"]),
                    Course(id="lib802", title="Career Development", credits=1, difficulty=2, weekly_hours=2, skills=["Career"]),
                ],
            ),
        },
    },

    # ===== NYU (Private, Comprehensive) =====
    "nyu": {
        # Computer Science at NYU
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
                    Course(id="cs403", title="Web Development", credits=3, difficulty=5, weekly_hours=6, skills=["Frontend", "Backend"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Upper-Level Specialization",
                courses=[
                    Course(id="cs501", title="Operating Systems", credits=4, difficulty=7, weekly_hours=10, skills=["Systems", "C", "Concurrency"]),
                    Course(id="cs502", title="Theory of Computation", credits=3, difficulty=7, weekly_hours=7, skills=["Formal Languages", "Automata"]),
                    Course(id="cs503", title="Computer Networks", credits=3, difficulty=6, weekly_hours=6, skills=["Networking", "TCP/IP"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Advanced Topics & Systems",
                courses=[
                    Course(id="cs601", title="Machine Learning", credits=3, difficulty=7, weekly_hours=8, skills=["ML", "Python", "Statistics"]),
                    Course(id="cs602", title="Compiler Design", credits=3, difficulty=7, weekly_hours=6, skills=["Compilers", "Parsing"]),
                    Course(id="cs603", title="Mobile App Development", credits=3, difficulty=5, weekly_hours=6, skills=["iOS", "Android"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Capstone & Professional",
                courses=[
                    Course(id="cs701", title="Cybersecurity Fundamentals", credits=3, difficulty=6, weekly_hours=7, skills=["Security", "Cryptography"]),
                    Course(id="cs702", title="Distributed Systems", credits=3, difficulty=7, weekly_hours=6, skills=["Distributed Computing", "Cloud"]),
                    Course(id="cs703", title="AI & Deep Learning", credits=3, difficulty=7, weekly_hours=7, skills=["Neural Networks", "AI"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone Project & Career Preparation",
                courses=[
                    Course(id="cs801", title="Capstone Project", credits=4, difficulty=7, weekly_hours=10, skills=["Project Management", "Integration"]),
                    Course(id="cs802", title="Professional Development", credits=1, difficulty=2, weekly_hours=2, skills=["Resume", "Interview"]),
                ],
            ),
        },
        # Business Administration at NYU (difficulty +1)
        "ba": {
            1: SemesterCurriculum(
                semester=1,
                notes="Business Foundation",
                courses=[
                    Course(id="ba101", title="Intro to Business", credits=3, difficulty=4, weekly_hours=6, skills=["Business Fundamentals"]),
                    Course(id="ba102", title="Accounting Principles", credits=3, difficulty=5, weekly_hours=6, skills=["Accounting", "Finance"]),
                    Course(id="econ101", title="Microeconomics", credits=3, difficulty=5, weekly_hours=6, skills=["Economics", "Markets"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Economics & Financial Analysis",
                courses=[
                    Course(id="ba201", title="Business Communication", credits=3, difficulty=4, weekly_hours=5, skills=["Writing", "Presentation"]),
                    Course(id="econ102", title="Macroeconomics", credits=3, difficulty=5, weekly_hours=6, skills=["Economics", "Policy"]),
                    Course(id="ba202", title="Financial Accounting", credits=3, difficulty=5, weekly_hours=7, skills=["Accounting", "Financial Statements"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Management & Marketing",
                courses=[
                    Course(id="ba301", title="Management Principles", credits=3, difficulty=5, weekly_hours=6, skills=["Leadership", "Organization"]),
                    Course(id="ba302", title="Marketing Fundamentals", credits=3, difficulty=5, weekly_hours=6, skills=["Marketing", "Consumer Behavior"]),
                    Course(id="ba303", title="Organizational Behavior", credits=3, difficulty=5, weekly_hours=6, skills=["Psychology", "Teams"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Finance & Strategy",
                courses=[
                    Course(id="ba401", title="Corporate Finance", credits=3, difficulty=6, weekly_hours=7, skills=["Finance", "Valuation"]),
                    Course(id="ba402", title="Strategic Management", credits=3, difficulty=6, weekly_hours=6, skills=["Strategy", "Analysis"]),
                    Course(id="ba403", title="Operations Management", credits=3, difficulty=5, weekly_hours=6, skills=["Operations", "Supply Chain"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Specialized Business Topics",
                courses=[
                    Course(id="ba501", title="Entrepreneurship", credits=3, difficulty=6, weekly_hours=6, skills=["Innovation", "Startup"]),
                    Course(id="ba502", title="Business Analytics", credits=3, difficulty=6, weekly_hours=7, skills=["Data Analysis", "Statistics"]),
                    Course(id="ba503", title="International Business", credits=3, difficulty=5, weekly_hours=6, skills=["Global Markets", "Trade"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Advanced Specialization",
                courses=[
                    Course(id="ba601", title="Digital Marketing", credits=3, difficulty=5, weekly_hours=6, skills=["Social Media", "Analytics"]),
                    Course(id="ba602", title="Investment Analysis", credits=3, difficulty=6, weekly_hours=7, skills=["Investing", "Portfolio"]),
                    Course(id="ba603", title="Business Ethics", credits=3, difficulty=4, weekly_hours=5, skills=["Ethics", "Leadership"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Capstone Preparation",
                courses=[
                    Course(id="ba701", title="Business Policy", credits=3, difficulty=6, weekly_hours=6, skills=["Policy", "Decision Making"]),
                    Course(id="ba702", title="Consulting Project", credits=3, difficulty=6, weekly_hours=8, skills=["Consulting", "Problem Solving"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career Readiness",
                courses=[
                    Course(id="ba801", title="Capstone Case Study", credits=3, difficulty=6, weekly_hours=8, skills=["Integration", "Analysis"]),
                    Course(id="ba802", title="Career Readiness", credits=1, difficulty=2, weekly_hours=2, skills=["Networking", "Job Search"]),
                ],
            ),
        },
        # Engineering at NYU
        "engineering": {
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
        # Data Science at NYU
        "data_science": {
            1: SemesterCurriculum(
                semester=1,
                notes="Data Science Foundation",
                courses=[
                    Course(id="ds101", title="Intro to Data Science", credits=3, difficulty=4, weekly_hours=7, skills=["Python", "Data"]),
                    Course(id="math101", title="Calculus I", credits=4, difficulty=5, weekly_hours=8, skills=["Calculus"]),
                    Course(id="cs101", title="Intro Programming", credits=4, difficulty=4, weekly_hours=10, skills=["Python"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Statistics & Probability",
                courses=[
                    Course(id="ds201", title="Probability & Statistics", credits=4, difficulty=5, weekly_hours=8, skills=["Statistics", "Probability"]),
                    Course(id="math102", title="Calculus II", credits=4, difficulty=5, weekly_hours=8, skills=["Calculus"]),
                    Course(id="cs201", title="Data Structures", credits=4, difficulty=5, weekly_hours=10, skills=["Algorithms"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Machine Learning Basics",
                courses=[
                    Course(id="ds301", title="Machine Learning I", credits=4, difficulty=6, weekly_hours=9, skills=["ML", "Supervised Learning"]),
                    Course(id="math201", title="Linear Algebra", credits=3, difficulty=5, weekly_hours=6, skills=["Matrices"]),
                    Course(id="cs303", title="Database Systems", credits=3, difficulty=5, weekly_hours=6, skills=["SQL"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Advanced ML & Big Data",
                courses=[
                    Course(id="ds401", title="Machine Learning II", credits=4, difficulty=7, weekly_hours=9, skills=["Deep Learning", "Neural Networks"]),
                    Course(id="ds402", title="Big Data Technologies", credits=3, difficulty=6, weekly_hours=7, skills=["Spark", "Hadoop"]),
                    Course(id="ds403", title="Data Visualization", credits=3, difficulty=4, weekly_hours=6, skills=["Visualization", "Tableau"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="NLP & Computer Vision",
                courses=[
                    Course(id="ds501", title="Natural Language Processing", credits=3, difficulty=7, weekly_hours=8, skills=["NLP", "Text Mining"]),
                    Course(id="ds502", title="Computer Vision", credits=3, difficulty=7, weekly_hours=8, skills=["CV", "Image Processing"]),
                    Course(id="ds503", title="Time Series Analysis", credits=3, difficulty=6, weekly_hours=7, skills=["Forecasting"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="AI & Ethics",
                courses=[
                    Course(id="ds601", title="Deep Reinforcement Learning", credits=3, difficulty=8, weekly_hours=8, skills=["RL", "AI"]),
                    Course(id="ds602", title="Data Ethics & Privacy", credits=3, difficulty=4, weekly_hours=5, skills=["Ethics", "Privacy"]),
                    Course(id="ds603", title="Cloud Computing for DS", credits=3, difficulty=5, weekly_hours=6, skills=["AWS", "Cloud"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Advanced Topics",
                courses=[
                    Course(id="ds701", title="Advanced Deep Learning", credits=3, difficulty=8, weekly_hours=8, skills=["Transformers", "GANs"]),
                    Course(id="ds702", title="Causal Inference", credits=3, difficulty=7, weekly_hours=7, skills=["Causality", "Experiments"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="ds801", title="Data Science Capstone", credits=4, difficulty=7, weekly_hours=10, skills=["Project", "Integration"]),
                    Course(id="ds802", title="Career Preparation", credits=1, difficulty=2, weekly_hours=2, skills=["Interview", "Portfolio"]),
                ],
            ),
        },
        # Economics at NYU (same as Baruch but difficulty +1)
        "economics": {
            1: SemesterCurriculum(
                semester=1,
                notes="Economics Foundation",
                courses=[
                    Course(id="econ101", title="Microeconomics", credits=3, difficulty=5, weekly_hours=6, skills=["Micro", "Markets"]),
                    Course(id="econ102", title="Macroeconomics", credits=3, difficulty=5, weekly_hours=6, skills=["Macro", "Policy"]),
                    Course(id="math101", title="Calculus I", credits=4, difficulty=5, weekly_hours=8, skills=["Calculus"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Intermediate Economics",
                courses=[
                    Course(id="econ201", title="Intermediate Microeconomics", credits=3, difficulty=6, weekly_hours=7, skills=["Consumer Theory"]),
                    Course(id="econ202", title="Intermediate Macroeconomics", credits=3, difficulty=6, weekly_hours=7, skills=["IS-LM", "Growth"]),
                    Course(id="math102", title="Calculus II", credits=4, difficulty=5, weekly_hours=8, skills=["Calculus"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Econometrics & Statistics",
                courses=[
                    Course(id="econ301", title="Econometrics I", credits=3, difficulty=7, weekly_hours=8, skills=["Regression", "Stats"]),
                    Course(id="econ302", title="Game Theory", credits=3, difficulty=7, weekly_hours=7, skills=["Strategy", "Incentives"]),
                    Course(id="math201", title="Linear Algebra", credits=3, difficulty=5, weekly_hours=6, skills=["Matrices"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Applied Economics",
                courses=[
                    Course(id="econ401", title="Labor Economics", credits=3, difficulty=6, weekly_hours=6, skills=["Labor Markets"]),
                    Course(id="econ402", title="Public Economics", credits=3, difficulty=6, weekly_hours=6, skills=["Tax", "Policy"]),
                    Course(id="econ403", title="Econometrics II", credits=3, difficulty=7, weekly_hours=8, skills=["Advanced Stats"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Specialized Topics",
                courses=[
                    Course(id="econ501", title="International Trade", credits=3, difficulty=6, weekly_hours=6, skills=["Trade", "Comparative Advantage"]),
                    Course(id="econ502", title="Monetary Economics", credits=3, difficulty=6, weekly_hours=6, skills=["Fed", "Interest Rates"]),
                    Course(id="econ503", title="Development Economics", credits=3, difficulty=6, weekly_hours=6, skills=["Growth", "Poverty"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Advanced Topics",
                courses=[
                    Course(id="econ601", title="Industrial Organization", credits=3, difficulty=7, weekly_hours=7, skills=["Market Structure"]),
                    Course(id="econ602", title="Behavioral Economics", credits=3, difficulty=6, weekly_hours=6, skills=["Psychology", "Decisions"]),
                    Course(id="econ603", title="Environmental Economics", credits=3, difficulty=6, weekly_hours=6, skills=["Climate", "Externalities"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Research Methods",
                courses=[
                    Course(id="econ701", title="Advanced Econometrics", credits=3, difficulty=8, weekly_hours=8, skills=["Causal Inference"]),
                    Course(id="econ702", title="Economic Research Methods", credits=3, difficulty=7, weekly_hours=7, skills=["Research Design"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="econ801", title="Economics Capstone", credits=3, difficulty=7, weekly_hours=9, skills=["Thesis", "Research"]),
                    Course(id="econ802", title="Career Preparation", credits=1, difficulty=2, weekly_hours=2, skills=["Career"]),
                ],
            ),
        },
        # Finance at NYU (same as Baruch but difficulty +1)
        "finance": {
            1: SemesterCurriculum(
                semester=1,
                notes="Finance Foundation",
                courses=[
                    Course(id="fin101", title="Intro to Finance", credits=3, difficulty=5, weekly_hours=6, skills=["Finance Basics"]),
                    Course(id="ba102", title="Accounting Principles", credits=3, difficulty=5, weekly_hours=6, skills=["Accounting"]),
                    Course(id="econ101", title="Microeconomics", credits=3, difficulty=5, weekly_hours=6, skills=["Economics"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Financial Markets",
                courses=[
                    Course(id="fin201", title="Financial Markets", credits=3, difficulty=5, weekly_hours=7, skills=["Markets", "Trading"]),
                    Course(id="econ102", title="Macroeconomics", credits=3, difficulty=5, weekly_hours=6, skills=["Economics"]),
                    Course(id="ba202", title="Financial Accounting", credits=3, difficulty=5, weekly_hours=7, skills=["Accounting"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Corporate Finance",
                courses=[
                    Course(id="fin301", title="Corporate Finance", credits=3, difficulty=6, weekly_hours=8, skills=["Valuation", "DCF"]),
                    Course(id="fin302", title="Investment Analysis", credits=3, difficulty=6, weekly_hours=7, skills=["Equity Analysis"]),
                    Course(id="ba301", title="Management Principles", credits=3, difficulty=5, weekly_hours=6, skills=["Management"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Portfolio & Derivatives",
                courses=[
                    Course(id="fin401", title="Portfolio Management", credits=3, difficulty=7, weekly_hours=8, skills=["Portfolio Theory"]),
                    Course(id="fin402", title="Derivatives", credits=3, difficulty=7, weekly_hours=8, skills=["Options", "Futures"]),
                    Course(id="ba502", title="Business Analytics", credits=3, difficulty=6, weekly_hours=7, skills=["Analytics"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Advanced Finance",
                courses=[
                    Course(id="fin501", title="Fixed Income Securities", credits=3, difficulty=7, weekly_hours=7, skills=["Bonds", "Yield"]),
                    Course(id="fin502", title="Risk Management", credits=3, difficulty=6, weekly_hours=7, skills=["Hedging", "Risk"]),
                    Course(id="fin503", title="International Finance", credits=3, difficulty=6, weekly_hours=6, skills=["FX", "Global"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Specialized Finance",
                courses=[
                    Course(id="fin601", title="M&A and Corporate Restructuring", credits=3, difficulty=7, weekly_hours=8, skills=["M&A", "LBO"]),
                    Course(id="fin602", title="Real Estate Finance", credits=3, difficulty=6, weekly_hours=6, skills=["Real Estate"]),
                    Course(id="fin603", title="Fintech & Digital Banking", credits=3, difficulty=6, weekly_hours=6, skills=["Fintech"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Capstone Preparation",
                courses=[
                    Course(id="fin701", title="Financial Modeling", credits=3, difficulty=7, weekly_hours=8, skills=["Excel", "Modeling"]),
                    Course(id="fin702", title="Investment Banking", credits=3, difficulty=7, weekly_hours=8, skills=["IB", "M&A"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="fin801", title="Finance Capstone", credits=3, difficulty=7, weekly_hours=9, skills=["Integration"]),
                    Course(id="fin802", title="CFA Prep / Career Readiness", credits=1, difficulty=2, weekly_hours=2, skills=["CFA", "Career"]),
                ],
            ),
        },
        # Communications at NYU
        "communications": {
            1: SemesterCurriculum(
                semester=1,
                notes="Communications Foundation",
                courses=[
                    Course(id="comm101", title="Intro to Communications", credits=3, difficulty=3, weekly_hours=6, skills=["Communication Theory"]),
                    Course(id="comm102", title="Media Writing", credits=3, difficulty=3, weekly_hours=6, skills=["Writing"]),
                    Course(id="comm103", title="Public Speaking", credits=3, difficulty=3, weekly_hours=5, skills=["Speaking", "Presentation"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Digital Media",
                courses=[
                    Course(id="comm201", title="Digital Media Production", credits=3, difficulty=4, weekly_hours=7, skills=["Video", "Editing"]),
                    Course(id="comm202", title="Social Media Strategy", credits=3, difficulty=3, weekly_hours=6, skills=["Social Media"]),
                    Course(id="comm203", title="Journalism Basics", credits=3, difficulty=4, weekly_hours=6, skills=["Reporting", "Writing"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Broadcasting & PR",
                courses=[
                    Course(id="comm301", title="Broadcast Journalism", credits=3, difficulty=4, weekly_hours=7, skills=["Broadcasting", "Production"]),
                    Course(id="comm302", title="Public Relations", credits=3, difficulty=4, weekly_hours=6, skills=["PR", "Crisis Management"]),
                    Course(id="comm303", title="Media Law & Ethics", credits=3, difficulty=4, weekly_hours=5, skills=["Law", "Ethics"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Strategic Communication",
                courses=[
                    Course(id="comm401", title="Strategic Communication", credits=3, difficulty=5, weekly_hours=6, skills=["Strategy", "Campaigns"]),
                    Course(id="comm402", title="Advertising", credits=3, difficulty=4, weekly_hours=6, skills=["Advertising", "Creativity"]),
                    Course(id="comm403", title="Media Research", credits=3, difficulty=5, weekly_hours=7, skills=["Research", "Analytics"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Advanced Production",
                courses=[
                    Course(id="comm501", title="Documentary Production", credits=3, difficulty=5, weekly_hours=8, skills=["Documentary", "Storytelling"]),
                    Course(id="comm502", title="Podcast Production", credits=3, difficulty=4, weekly_hours=6, skills=["Audio", "Podcasting"]),
                    Course(id="comm503", title="Corporate Communication", credits=3, difficulty=4, weekly_hours=6, skills=["Corporate Comm"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Specialization",
                courses=[
                    Course(id="comm601", title="Interactive Media", credits=3, difficulty=5, weekly_hours=7, skills=["Interactive", "Web"]),
                    Course(id="comm602", title="Media Management", credits=3, difficulty=4, weekly_hours=6, skills=["Management", "Business"]),
                    Course(id="comm603", title="Global Communication", credits=3, difficulty=4, weekly_hours=6, skills=["Global", "Culture"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Professional Practice",
                courses=[
                    Course(id="comm701", title="Internship", credits=3, difficulty=3, weekly_hours=10, skills=["Professional Experience"]),
                    Course(id="comm702", title="Advanced Media Project", credits=3, difficulty=5, weekly_hours=8, skills=["Project", "Portfolio"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="comm801", title="Communications Capstone", credits=3, difficulty=5, weekly_hours=9, skills=["Portfolio", "Integration"]),
                    Course(id="comm802", title="Career Development", credits=1, difficulty=2, weekly_hours=2, skills=["Career", "Networking"]),
                ],
            ),
        },
        # Psychology at NYU
        "psychology": {
            1: SemesterCurriculum(
                semester=1,
                notes="Psychology Foundation",
                courses=[
                    Course(id="psych101", title="Intro to Psychology", credits=3, difficulty=3, weekly_hours=6, skills=["Psychology Basics"]),
                    Course(id="psych102", title="Research Methods", credits=3, difficulty=4, weekly_hours=7, skills=["Research", "Methodology"]),
                    Course(id="bio101", title="Biology I", credits=4, difficulty=4, weekly_hours=8, skills=["Biology"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Cognitive & Developmental",
                courses=[
                    Course(id="psych201", title="Cognitive Psychology", credits=3, difficulty=4, weekly_hours=6, skills=["Cognition", "Memory"]),
                    Course(id="psych202", title="Developmental Psychology", credits=3, difficulty=4, weekly_hours=6, skills=["Development", "Lifespan"]),
                    Course(id="stat101", title="Statistics", credits=3, difficulty=5, weekly_hours=7, skills=["Statistics"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Social & Personality",
                courses=[
                    Course(id="psych301", title="Social Psychology", credits=3, difficulty=4, weekly_hours=6, skills=["Social Behavior"]),
                    Course(id="psych302", title="Personality Psychology", credits=3, difficulty=4, weekly_hours=6, skills=["Personality", "Traits"]),
                    Course(id="psych303", title="Biopsychology", credits=3, difficulty=5, weekly_hours=7, skills=["Neuroscience", "Brain"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Abnormal & Clinical",
                courses=[
                    Course(id="psych401", title="Abnormal Psychology", credits=3, difficulty=5, weekly_hours=6, skills=["Mental Health", "Disorders"]),
                    Course(id="psych402", title="Clinical Psychology", credits=3, difficulty=5, weekly_hours=6, skills=["Clinical", "Therapy"]),
                    Course(id="psych403", title="Learning & Behavior", credits=3, difficulty=4, weekly_hours=6, skills=["Learning", "Conditioning"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Advanced Topics",
                courses=[
                    Course(id="psych501", title="Health Psychology", credits=3, difficulty=4, weekly_hours=6, skills=["Health", "Wellness"]),
                    Course(id="psych502", title="Organizational Psychology", credits=3, difficulty=4, weekly_hours=6, skills=["Workplace", "Organizations"]),
                    Course(id="psych503", title="Advanced Research Methods", credits=3, difficulty=6, weekly_hours=7, skills=["Research Design"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Applied Psychology",
                courses=[
                    Course(id="psych601", title="Psychological Testing", credits=3, difficulty=5, weekly_hours=7, skills=["Testing", "Assessment"]),
                    Course(id="psych602", title="Counseling Psychology", credits=3, difficulty=5, weekly_hours=6, skills=["Counseling", "Intervention"]),
                    Course(id="psych603", title="Educational Psychology", credits=3, difficulty=4, weekly_hours=6, skills=["Education", "Teaching"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Research & Practice",
                courses=[
                    Course(id="psych701", title="Independent Research", credits=3, difficulty=6, weekly_hours=9, skills=["Research", "Thesis"]),
                    Course(id="psych702", title="Psychology Practicum", credits=3, difficulty=5, weekly_hours=8, skills=["Practical Experience"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="psych801", title="Psychology Capstone", credits=3, difficulty=6, weekly_hours=9, skills=["Integration", "Thesis"]),
                    Course(id="psych802", title="Career Preparation", credits=1, difficulty=2, weekly_hours=2, skills=["Career", "Graduate School"]),
                ],
            ),
        },
    },

    # ===== COLUMBIA (Elite Private, Research University) =====
    "columbia": {
        # Computer Science at Columbia (difficulty +2)
        "cs": {
            1: SemesterCurriculum(
                semester=1,
                notes="Foundation & Programming Basics",
                courses=[
                    Course(id="cs101", title="Intro Programming", credits=4, difficulty=6, weekly_hours=11, skills=["Python", "Problem Solving"]),
                    Course(id="cs102", title="Computer Science Fundamentals", credits=3, difficulty=6, weekly_hours=7, skills=["Logic", "Binary"]),
                    Course(id="math101", title="Calculus I", credits=4, difficulty=7, weekly_hours=9, skills=["Calculus", "Math"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Data Structures & Algorithms",
                courses=[
                    Course(id="cs201", title="Data Structures", credits=4, difficulty=7, weekly_hours=11, skills=["Algorithms", "Data Structures"]),
                    Course(id="cs202", title="Discrete Mathematics", credits=3, difficulty=8, weekly_hours=8, skills=["Logic", "Proofs"]),
                    Course(id="math102", title="Calculus II", credits=4, difficulty=7, weekly_hours=9, skills=["Calculus", "Integration"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Object-Oriented Programming & Systems",
                courses=[
                    Course(id="cs301", title="Object-Oriented Programming", credits=4, difficulty=7, weekly_hours=11, skills=["OOP", "Java", "Design"]),
                    Course(id="cs302", title="Computer Organization", credits=3, difficulty=8, weekly_hours=8, skills=["Architecture", "CPU"]),
                    Course(id="cs303", title="Database Systems", credits=3, difficulty=7, weekly_hours=7, skills=["SQL", "Database Design"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Algorithms & Analysis",
                courses=[
                    Course(id="cs401", title="Advanced Algorithms", credits=4, difficulty=9, weekly_hours=11, skills=["Algorithms", "Complexity"]),
                    Course(id="cs402", title="Software Engineering", credits=3, difficulty=7, weekly_hours=7, skills=["Design Patterns", "Testing"]),
                    Course(id="cs403", title="Web Development", credits=3, difficulty=7, weekly_hours=7, skills=["Frontend", "Backend"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Upper-Level Specialization",
                courses=[
                    Course(id="cs501", title="Operating Systems", credits=4, difficulty=9, weekly_hours=11, skills=["Systems", "C", "Concurrency"]),
                    Course(id="cs502", title="Theory of Computation", credits=3, difficulty=9, weekly_hours=8, skills=["Formal Languages", "Automata"]),
                    Course(id="cs503", title="Computer Networks", credits=3, difficulty=8, weekly_hours=7, skills=["Networking", "TCP/IP"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Advanced Topics & Systems",
                courses=[
                    Course(id="cs601", title="Machine Learning", credits=3, difficulty=9, weekly_hours=9, skills=["ML", "Python", "Statistics"]),
                    Course(id="cs602", title="Compiler Design", credits=3, difficulty=9, weekly_hours=7, skills=["Compilers", "Parsing"]),
                    Course(id="cs603", title="Mobile App Development", credits=3, difficulty=7, weekly_hours=7, skills=["iOS", "Android"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Capstone & Professional",
                courses=[
                    Course(id="cs701", title="Cybersecurity Fundamentals", credits=3, difficulty=8, weekly_hours=8, skills=["Security", "Cryptography"]),
                    Course(id="cs702", title="Distributed Systems", credits=3, difficulty=9, weekly_hours=7, skills=["Distributed Computing", "Cloud"]),
                    Course(id="cs703", title="AI & Deep Learning", credits=3, difficulty=9, weekly_hours=8, skills=["Neural Networks", "AI"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone Project & Career Preparation",
                courses=[
                    Course(id="cs801", title="Capstone Project", credits=4, difficulty=9, weekly_hours=11, skills=["Project Management", "Integration"]),
                    Course(id="cs802", title="Professional Development", credits=1, difficulty=2, weekly_hours=2, skills=["Resume", "Interview"]),
                ],
            ),
        },
        # Business Administration at Columbia (difficulty +2)
        "ba": {
            1: SemesterCurriculum(
                semester=1,
                notes="Business Foundation",
                courses=[
                    Course(id="ba101", title="Intro to Business", credits=3, difficulty=5, weekly_hours=7, skills=["Business Fundamentals"]),
                    Course(id="ba102", title="Accounting Principles", credits=3, difficulty=6, weekly_hours=7, skills=["Accounting", "Finance"]),
                    Course(id="econ101", title="Microeconomics", credits=3, difficulty=6, weekly_hours=7, skills=["Economics", "Markets"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Economics & Financial Analysis",
                courses=[
                    Course(id="ba201", title="Business Communication", credits=3, difficulty=5, weekly_hours=6, skills=["Writing", "Presentation"]),
                    Course(id="econ102", title="Macroeconomics", credits=3, difficulty=6, weekly_hours=7, skills=["Economics", "Policy"]),
                    Course(id="ba202", title="Financial Accounting", credits=3, difficulty=6, weekly_hours=8, skills=["Accounting", "Financial Statements"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Management & Marketing",
                courses=[
                    Course(id="ba301", title="Management Principles", credits=3, difficulty=6, weekly_hours=7, skills=["Leadership", "Organization"]),
                    Course(id="ba302", title="Marketing Fundamentals", credits=3, difficulty=6, weekly_hours=7, skills=["Marketing", "Consumer Behavior"]),
                    Course(id="ba303", title="Organizational Behavior", credits=3, difficulty=6, weekly_hours=7, skills=["Psychology", "Teams"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Finance & Strategy",
                courses=[
                    Course(id="ba401", title="Corporate Finance", credits=3, difficulty=7, weekly_hours=8, skills=["Finance", "Valuation"]),
                    Course(id="ba402", title="Strategic Management", credits=3, difficulty=7, weekly_hours=7, skills=["Strategy", "Analysis"]),
                    Course(id="ba403", title="Operations Management", credits=3, difficulty=6, weekly_hours=7, skills=["Operations", "Supply Chain"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Specialized Business Topics",
                courses=[
                    Course(id="ba501", title="Entrepreneurship", credits=3, difficulty=7, weekly_hours=7, skills=["Innovation", "Startup"]),
                    Course(id="ba502", title="Business Analytics", credits=3, difficulty=7, weekly_hours=8, skills=["Data Analysis", "Statistics"]),
                    Course(id="ba503", title="International Business", credits=3, difficulty=6, weekly_hours=7, skills=["Global Markets", "Trade"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Advanced Specialization",
                courses=[
                    Course(id="ba601", title="Digital Marketing", credits=3, difficulty=6, weekly_hours=7, skills=["Social Media", "Analytics"]),
                    Course(id="ba602", title="Investment Analysis", credits=3, difficulty=7, weekly_hours=8, skills=["Investing", "Portfolio"]),
                    Course(id="ba603", title="Business Ethics", credits=3, difficulty=5, weekly_hours=6, skills=["Ethics", "Leadership"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Capstone Preparation",
                courses=[
                    Course(id="ba701", title="Business Policy", credits=3, difficulty=7, weekly_hours=7, skills=["Policy", "Decision Making"]),
                    Course(id="ba702", title="Consulting Project", credits=3, difficulty=7, weekly_hours=9, skills=["Consulting", "Problem Solving"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career Readiness",
                courses=[
                    Course(id="ba801", title="Capstone Case Study", credits=3, difficulty=7, weekly_hours=9, skills=["Integration", "Analysis"]),
                    Course(id="ba802", title="Career Readiness", credits=1, difficulty=2, weekly_hours=2, skills=["Networking", "Job Search"]),
                ],
            ),
        },
        # Engineering at Columbia (difficulty +2)
        "engineering": {
            1: SemesterCurriculum(
                semester=1,
                notes="Engineering Foundation",
                courses=[
                    Course(id="eng101", title="Engineering Design", credits=3, difficulty=6, weekly_hours=9, skills=["Design", "CAD"]),
                    Course(id="phys101", title="Physics I", credits=4, difficulty=7, weekly_hours=10, skills=["Mechanics", "Physics"]),
                    Course(id="math101", title="Calculus I", credits=4, difficulty=7, weekly_hours=9, skills=["Calculus", "Math"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Physics & Mathematics",
                courses=[
                    Course(id="phys102", title="Physics II", credits=4, difficulty=7, weekly_hours=10, skills=["Electricity", "Waves"]),
                    Course(id="math102", title="Calculus II", credits=4, difficulty=7, weekly_hours=9, skills=["Integration", "Calculus"]),
                    Course(id="eng102", title="Engineering Analysis", credits=3, difficulty=6, weekly_hours=7, skills=["Statics", "Analysis"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Circuits & Materials",
                courses=[
                    Course(id="eng301", title="Circuit Analysis", credits=4, difficulty=7, weekly_hours=10, skills=["Electronics", "Circuits"]),
                    Course(id="eng302", title="Materials Science", credits=3, difficulty=7, weekly_hours=8, skills=["Materials", "Properties"]),
                    Course(id="math201", title="Linear Algebra", credits=3, difficulty=7, weekly_hours=7, skills=["Linear Algebra", "Matrices"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Systems & Thermodynamics",
                courses=[
                    Course(id="eng401", title="Thermodynamics", credits=4, difficulty=8, weekly_hours=10, skills=["Thermodynamics", "Energy"]),
                    Course(id="eng402", title="Digital Systems", credits=3, difficulty=7, weekly_hours=9, skills=["Digital Logic", "HDL"]),
                    Course(id="eng403", title="Signal Processing", credits=3, difficulty=8, weekly_hours=8, skills=["Signals", "Filtering"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Control & Advanced Topics",
                courses=[
                    Course(id="eng501", title="Control Systems", credits=4, difficulty=8, weekly_hours=9, skills=["Controls", "Feedback"]),
                    Course(id="eng502", title="Power Systems", credits=3, difficulty=8, weekly_hours=8, skills=["Power", "Grid"]),
                    Course(id="eng503", title="Mechanical Design", credits=3, difficulty=7, weekly_hours=9, skills=["Mechanical Design", "CAD"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Specialization & Applications",
                courses=[
                    Course(id="eng601", title="Advanced Controls", credits=3, difficulty=9, weekly_hours=8, skills=["Advanced Control", "Optimization"]),
                    Course(id="eng602", title="Renewable Energy", credits=3, difficulty=7, weekly_hours=7, skills=["Solar", "Wind"]),
                    Course(id="eng603", title="Engineering Management", credits=3, difficulty=6, weekly_hours=6, skills=["Project Management", "Leadership"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Capstone Preparation",
                courses=[
                    Course(id="eng701", title="Systems Integration", credits=3, difficulty=8, weekly_hours=8, skills=["Integration", "Testing"]),
                    Course(id="eng702", title="Engineering Ethics", credits=2, difficulty=2, weekly_hours=3, skills=["Ethics", "Professional"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone Project & Professional",
                courses=[
                    Course(id="eng801", title="Capstone Design Project", credits=4, difficulty=9, weekly_hours=11, skills=["Design", "Integration"]),
                    Course(id="eng802", title="Professional Practice", credits=1, difficulty=2, weekly_hours=2, skills=["PE Prep", "Career"]),
                ],
            ),
        },
        # Data Science at Columbia (difficulty +2)
        "data_science": {
            1: SemesterCurriculum(
                semester=1,
                notes="Data Science Foundation",
                courses=[
                    Course(id="ds101", title="Intro to Data Science", credits=3, difficulty=6, weekly_hours=8, skills=["Python", "Data"]),
                    Course(id="math101", title="Calculus I", credits=4, difficulty=7, weekly_hours=9, skills=["Calculus"]),
                    Course(id="cs101", title="Intro Programming", credits=4, difficulty=6, weekly_hours=11, skills=["Python"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Statistics & Probability",
                courses=[
                    Course(id="ds201", title="Probability & Statistics", credits=4, difficulty=7, weekly_hours=9, skills=["Statistics", "Probability"]),
                    Course(id="math102", title="Calculus II", credits=4, difficulty=7, weekly_hours=9, skills=["Calculus"]),
                    Course(id="cs201", title="Data Structures", credits=4, difficulty=7, weekly_hours=11, skills=["Algorithms"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Machine Learning Basics",
                courses=[
                    Course(id="ds301", title="Machine Learning I", credits=4, difficulty=8, weekly_hours=10, skills=["ML", "Supervised Learning"]),
                    Course(id="math201", title="Linear Algebra", credits=3, difficulty=7, weekly_hours=7, skills=["Matrices"]),
                    Course(id="cs303", title="Database Systems", credits=3, difficulty=7, weekly_hours=7, skills=["SQL"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Advanced ML & Big Data",
                courses=[
                    Course(id="ds401", title="Machine Learning II", credits=4, difficulty=9, weekly_hours=10, skills=["Deep Learning", "Neural Networks"]),
                    Course(id="ds402", title="Big Data Technologies", credits=3, difficulty=8, weekly_hours=8, skills=["Spark", "Hadoop"]),
                    Course(id="ds403", title="Data Visualization", credits=3, difficulty=6, weekly_hours=7, skills=["Visualization", "Tableau"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="NLP & Computer Vision",
                courses=[
                    Course(id="ds501", title="Natural Language Processing", credits=3, difficulty=9, weekly_hours=9, skills=["NLP", "Text Mining"]),
                    Course(id="ds502", title="Computer Vision", credits=3, difficulty=9, weekly_hours=9, skills=["CV", "Image Processing"]),
                    Course(id="ds503", title="Time Series Analysis", credits=3, difficulty=8, weekly_hours=8, skills=["Forecasting"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="AI & Ethics",
                courses=[
                    Course(id="ds601", title="Deep Reinforcement Learning", credits=3, difficulty=10, weekly_hours=9, skills=["RL", "AI"]),
                    Course(id="ds602", title="Data Ethics & Privacy", credits=3, difficulty=6, weekly_hours=6, skills=["Ethics", "Privacy"]),
                    Course(id="ds603", title="Cloud Computing for DS", credits=3, difficulty=7, weekly_hours=7, skills=["AWS", "Cloud"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Advanced Topics",
                courses=[
                    Course(id="ds701", title="Advanced Deep Learning", credits=3, difficulty=10, weekly_hours=9, skills=["Transformers", "GANs"]),
                    Course(id="ds702", title="Causal Inference", credits=3, difficulty=9, weekly_hours=8, skills=["Causality", "Experiments"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="ds801", title="Data Science Capstone", credits=4, difficulty=9, weekly_hours=11, skills=["Project", "Integration"]),
                    Course(id="ds802", title="Career Preparation", credits=1, difficulty=2, weekly_hours=2, skills=["Interview", "Portfolio"]),
                ],
            ),
        },
        # Economics at Columbia (difficulty +2)
        "economics": {
            1: SemesterCurriculum(
                semester=1,
                notes="Economics Foundation",
                courses=[
                    Course(id="econ101", title="Microeconomics", credits=3, difficulty=6, weekly_hours=7, skills=["Micro", "Markets"]),
                    Course(id="econ102", title="Macroeconomics", credits=3, difficulty=6, weekly_hours=7, skills=["Macro", "Policy"]),
                    Course(id="math101", title="Calculus I", credits=4, difficulty=7, weekly_hours=9, skills=["Calculus"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Intermediate Economics",
                courses=[
                    Course(id="econ201", title="Intermediate Microeconomics", credits=3, difficulty=7, weekly_hours=8, skills=["Consumer Theory"]),
                    Course(id="econ202", title="Intermediate Macroeconomics", credits=3, difficulty=7, weekly_hours=8, skills=["IS-LM", "Growth"]),
                    Course(id="math102", title="Calculus II", credits=4, difficulty=7, weekly_hours=9, skills=["Calculus"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Econometrics & Statistics",
                courses=[
                    Course(id="econ301", title="Econometrics I", credits=3, difficulty=8, weekly_hours=9, skills=["Regression", "Stats"]),
                    Course(id="econ302", title="Game Theory", credits=3, difficulty=8, weekly_hours=8, skills=["Strategy", "Incentives"]),
                    Course(id="math201", title="Linear Algebra", credits=3, difficulty=7, weekly_hours=7, skills=["Matrices"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Applied Economics",
                courses=[
                    Course(id="econ401", title="Labor Economics", credits=3, difficulty=7, weekly_hours=7, skills=["Labor Markets"]),
                    Course(id="econ402", title="Public Economics", credits=3, difficulty=7, weekly_hours=7, skills=["Tax", "Policy"]),
                    Course(id="econ403", title="Econometrics II", credits=3, difficulty=8, weekly_hours=9, skills=["Advanced Stats"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Specialized Topics",
                courses=[
                    Course(id="econ501", title="International Trade", credits=3, difficulty=7, weekly_hours=7, skills=["Trade", "Comparative Advantage"]),
                    Course(id="econ502", title="Monetary Economics", credits=3, difficulty=7, weekly_hours=7, skills=["Fed", "Interest Rates"]),
                    Course(id="econ503", title="Development Economics", credits=3, difficulty=7, weekly_hours=7, skills=["Growth", "Poverty"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Advanced Topics",
                courses=[
                    Course(id="econ601", title="Industrial Organization", credits=3, difficulty=8, weekly_hours=8, skills=["Market Structure"]),
                    Course(id="econ602", title="Behavioral Economics", credits=3, difficulty=7, weekly_hours=7, skills=["Psychology", "Decisions"]),
                    Course(id="econ603", title="Environmental Economics", credits=3, difficulty=7, weekly_hours=7, skills=["Climate", "Externalities"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Research Methods",
                courses=[
                    Course(id="econ701", title="Advanced Econometrics", credits=3, difficulty=9, weekly_hours=9, skills=["Causal Inference"]),
                    Course(id="econ702", title="Economic Research Methods", credits=3, difficulty=8, weekly_hours=8, skills=["Research Design"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="econ801", title="Economics Capstone", credits=3, difficulty=8, weekly_hours=10, skills=["Thesis", "Research"]),
                    Course(id="econ802", title="Career Preparation", credits=1, difficulty=2, weekly_hours=2, skills=["Career"]),
                ],
            ),
        },
        # Finance at Columbia (difficulty +2)
        "finance": {
            1: SemesterCurriculum(
                semester=1,
                notes="Finance Foundation",
                courses=[
                    Course(id="fin101", title="Intro to Finance", credits=3, difficulty=6, weekly_hours=7, skills=["Finance Basics"]),
                    Course(id="ba102", title="Accounting Principles", credits=3, difficulty=6, weekly_hours=7, skills=["Accounting"]),
                    Course(id="econ101", title="Microeconomics", credits=3, difficulty=6, weekly_hours=7, skills=["Economics"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Financial Markets",
                courses=[
                    Course(id="fin201", title="Financial Markets", credits=3, difficulty=6, weekly_hours=8, skills=["Markets", "Trading"]),
                    Course(id="econ102", title="Macroeconomics", credits=3, difficulty=6, weekly_hours=7, skills=["Economics"]),
                    Course(id="ba202", title="Financial Accounting", credits=3, difficulty=6, weekly_hours=8, skills=["Accounting"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Corporate Finance",
                courses=[
                    Course(id="fin301", title="Corporate Finance", credits=3, difficulty=7, weekly_hours=9, skills=["Valuation", "DCF"]),
                    Course(id="fin302", title="Investment Analysis", credits=3, difficulty=7, weekly_hours=8, skills=["Equity Analysis"]),
                    Course(id="ba301", title="Management Principles", credits=3, difficulty=6, weekly_hours=7, skills=["Management"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Portfolio & Derivatives",
                courses=[
                    Course(id="fin401", title="Portfolio Management", credits=3, difficulty=8, weekly_hours=9, skills=["Portfolio Theory"]),
                    Course(id="fin402", title="Derivatives", credits=3, difficulty=8, weekly_hours=9, skills=["Options", "Futures"]),
                    Course(id="ba502", title="Business Analytics", credits=3, difficulty=7, weekly_hours=8, skills=["Analytics"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Advanced Finance",
                courses=[
                    Course(id="fin501", title="Fixed Income Securities", credits=3, difficulty=8, weekly_hours=8, skills=["Bonds", "Yield"]),
                    Course(id="fin502", title="Risk Management", credits=3, difficulty=7, weekly_hours=8, skills=["Hedging", "Risk"]),
                    Course(id="fin503", title="International Finance", credits=3, difficulty=7, weekly_hours=7, skills=["FX", "Global"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Specialized Finance",
                courses=[
                    Course(id="fin601", title="M&A and Corporate Restructuring", credits=3, difficulty=8, weekly_hours=9, skills=["M&A", "LBO"]),
                    Course(id="fin602", title="Real Estate Finance", credits=3, difficulty=7, weekly_hours=7, skills=["Real Estate"]),
                    Course(id="fin603", title="Fintech & Digital Banking", credits=3, difficulty=7, weekly_hours=7, skills=["Fintech"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Capstone Preparation",
                courses=[
                    Course(id="fin701", title="Financial Modeling", credits=3, difficulty=8, weekly_hours=9, skills=["Excel", "Modeling"]),
                    Course(id="fin702", title="Investment Banking", credits=3, difficulty=8, weekly_hours=9, skills=["IB", "M&A"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="fin801", title="Finance Capstone", credits=3, difficulty=8, weekly_hours=10, skills=["Integration"]),
                    Course(id="fin802", title="CFA Prep / Career Readiness", credits=1, difficulty=2, weekly_hours=2, skills=["CFA", "Career"]),
                ],
            ),
        },
        # Mathematics at Columbia
        "mathematics": {
            1: SemesterCurriculum(
                semester=1,
                notes="Mathematics Foundation",
                courses=[
                    Course(id="math101", title="Calculus I", credits=4, difficulty=7, weekly_hours=9, skills=["Calculus", "Limits"]),
                    Course(id="math102", title="Calculus II", credits=4, difficulty=7, weekly_hours=9, skills=["Integration", "Series"]),
                    Course(id="cs101", title="Intro Programming", credits=4, difficulty=6, weekly_hours=11, skills=["Python"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Advanced Calculus & Algebra",
                courses=[
                    Course(id="math201", title="Linear Algebra", credits=3, difficulty=7, weekly_hours=7, skills=["Matrices", "Vector Spaces"]),
                    Course(id="math202", title="Multivariable Calculus", credits=4, difficulty=8, weekly_hours=9, skills=["Partial Derivatives"]),
                    Course(id="math203", title="Differential Equations", credits=3, difficulty=7, weekly_hours=8, skills=["ODEs"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Abstract Algebra & Analysis",
                courses=[
                    Course(id="math301", title="Abstract Algebra I", credits=3, difficulty=8, weekly_hours=8, skills=["Groups", "Rings"]),
                    Course(id="math302", title="Real Analysis I", credits=3, difficulty=9, weekly_hours=9, skills=["Proofs", "Analysis"]),
                    Course(id="math303", title="Probability Theory", credits=3, difficulty=7, weekly_hours=7, skills=["Probability"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Advanced Topics",
                courses=[
                    Course(id="math401", title="Abstract Algebra II", credits=3, difficulty=8, weekly_hours=8, skills=["Field Theory", "Galois"]),
                    Course(id="math402", title="Real Analysis II", credits=3, difficulty=9, weekly_hours=9, skills=["Measure Theory"]),
                    Course(id="math403", title="Complex Analysis", credits=3, difficulty=8, weekly_hours=8, skills=["Complex Functions"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Topology & Geometry",
                courses=[
                    Course(id="math501", title="Topology", credits=3, difficulty=9, weekly_hours=8, skills=["Topological Spaces"]),
                    Course(id="math502", title="Differential Geometry", credits=3, difficulty=9, weekly_hours=8, skills=["Manifolds", "Curvature"]),
                    Course(id="math503", title="Number Theory", credits=3, difficulty=7, weekly_hours=7, skills=["Prime Numbers", "Cryptography"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Applied Mathematics",
                courses=[
                    Course(id="math601", title="Numerical Analysis", credits=3, difficulty=7, weekly_hours=8, skills=["Numerical Methods"]),
                    Course(id="math602", title="Partial Differential Equations", credits=3, difficulty=8, weekly_hours=8, skills=["PDEs"]),
                    Course(id="math603", title="Optimization Theory", credits=3, difficulty=7, weekly_hours=7, skills=["Optimization"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Advanced Research Topics",
                courses=[
                    Course(id="math701", title="Advanced Topics Seminar", credits=3, difficulty=9, weekly_hours=8, skills=["Research", "Seminars"]),
                    Course(id="math702", title="Mathematical Logic", credits=3, difficulty=8, weekly_hours=7, skills=["Logic", "Set Theory"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="math801", title="Mathematics Capstone", credits=3, difficulty=9, weekly_hours=10, skills=["Thesis", "Research"]),
                    Course(id="math802", title="Career Preparation", credits=1, difficulty=2, weekly_hours=2, skills=["Graduate School", "Industry"]),
                ],
            ),
        },
        # Psychology at Columbia (difficulty +2)
        "psychology": {
            1: SemesterCurriculum(
                semester=1,
                notes="Psychology Foundation",
                courses=[
                    Course(id="psych101", title="Intro to Psychology", credits=3, difficulty=5, weekly_hours=7, skills=["Psychology Basics"]),
                    Course(id="psych102", title="Research Methods", credits=3, difficulty=6, weekly_hours=8, skills=["Research", "Methodology"]),
                    Course(id="bio101", title="Biology I", credits=4, difficulty=6, weekly_hours=9, skills=["Biology"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Cognitive & Developmental",
                courses=[
                    Course(id="psych201", title="Cognitive Psychology", credits=3, difficulty=6, weekly_hours=7, skills=["Cognition", "Memory"]),
                    Course(id="psych202", title="Developmental Psychology", credits=3, difficulty=6, weekly_hours=7, skills=["Development", "Lifespan"]),
                    Course(id="stat101", title="Statistics", credits=3, difficulty=7, weekly_hours=8, skills=["Statistics"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Social & Personality",
                courses=[
                    Course(id="psych301", title="Social Psychology", credits=3, difficulty=6, weekly_hours=7, skills=["Social Behavior"]),
                    Course(id="psych302", title="Personality Psychology", credits=3, difficulty=6, weekly_hours=7, skills=["Personality", "Traits"]),
                    Course(id="psych303", title="Biopsychology", credits=3, difficulty=7, weekly_hours=8, skills=["Neuroscience", "Brain"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Abnormal & Clinical",
                courses=[
                    Course(id="psych401", title="Abnormal Psychology", credits=3, difficulty=7, weekly_hours=7, skills=["Mental Health", "Disorders"]),
                    Course(id="psych402", title="Clinical Psychology", credits=3, difficulty=7, weekly_hours=7, skills=["Clinical", "Therapy"]),
                    Course(id="psych403", title="Learning & Behavior", credits=3, difficulty=6, weekly_hours=7, skills=["Learning", "Conditioning"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Advanced Topics",
                courses=[
                    Course(id="psych501", title="Health Psychology", credits=3, difficulty=6, weekly_hours=7, skills=["Health", "Wellness"]),
                    Course(id="psych502", title="Organizational Psychology", credits=3, difficulty=6, weekly_hours=7, skills=["Workplace", "Organizations"]),
                    Course(id="psych503", title="Advanced Research Methods", credits=3, difficulty=8, weekly_hours=8, skills=["Research Design"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Applied Psychology",
                courses=[
                    Course(id="psych601", title="Psychological Testing", credits=3, difficulty=7, weekly_hours=8, skills=["Testing", "Assessment"]),
                    Course(id="psych602", title="Counseling Psychology", credits=3, difficulty=7, weekly_hours=7, skills=["Counseling", "Intervention"]),
                    Course(id="psych603", title="Educational Psychology", credits=3, difficulty=6, weekly_hours=7, skills=["Education", "Teaching"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Research & Practice",
                courses=[
                    Course(id="psych701", title="Independent Research", credits=3, difficulty=8, weekly_hours=10, skills=["Research", "Thesis"]),
                    Course(id="psych702", title="Psychology Practicum", credits=3, difficulty=7, weekly_hours=9, skills=["Practical Experience"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="psych801", title="Psychology Capstone", credits=3, difficulty=8, weekly_hours=10, skills=["Integration", "Thesis"]),
                    Course(id="psych802", title="Career Preparation", credits=1, difficulty=2, weekly_hours=2, skills=["Career", "Graduate School"]),
                ],
            ),
        },
        # Politics at Columbia
        "politics": {
            1: SemesterCurriculum(
                semester=1,
                notes="Political Science Foundation",
                courses=[
                    Course(id="pol101", title="Intro to Political Science", credits=3, difficulty=4, weekly_hours=6, skills=["Politics", "Government"]),
                    Course(id="pol102", title="American Government", credits=3, difficulty=4, weekly_hours=6, skills=["US Politics"]),
                    Course(id="pol103", title="Political Theory", credits=3, difficulty=5, weekly_hours=7, skills=["Theory", "Philosophy"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Comparative & International",
                courses=[
                    Course(id="pol201", title="Comparative Politics", credits=3, difficulty=5, weekly_hours=6, skills=["Comparative Analysis"]),
                    Course(id="pol202", title="International Relations", credits=3, difficulty=5, weekly_hours=6, skills=["IR", "Global Politics"]),
                    Course(id="pol203", title="Research Methods", credits=3, difficulty=5, weekly_hours=7, skills=["Research", "Methods"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Advanced Theory & Analysis",
                courses=[
                    Course(id="pol301", title="Political Economy", credits=3, difficulty=6, weekly_hours=7, skills=["Economics", "Politics"]),
                    Course(id="pol302", title="Public Policy", credits=3, difficulty=5, weekly_hours=6, skills=["Policy", "Analysis"]),
                    Course(id="pol303", title="Constitutional Law", credits=3, difficulty=6, weekly_hours=7, skills=["Law", "Constitution"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Regional Studies",
                courses=[
                    Course(id="pol401", title="European Politics", credits=3, difficulty=5, weekly_hours=6, skills=["Europe", "EU"]),
                    Course(id="pol402", title="Asian Politics", credits=3, difficulty=5, weekly_hours=6, skills=["Asia", "China"]),
                    Course(id="pol403", title="Middle East Politics", credits=3, difficulty=5, weekly_hours=6, skills=["Middle East"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Specialized Topics",
                courses=[
                    Course(id="pol501", title="Security Studies", credits=3, difficulty=6, weekly_hours=7, skills=["Security", "Defense"]),
                    Course(id="pol502", title="Human Rights", credits=3, difficulty=5, weekly_hours=6, skills=["Human Rights", "Justice"]),
                    Course(id="pol503", title="Environmental Politics", credits=3, difficulty=5, weekly_hours=6, skills=["Environment", "Climate"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Advanced Seminars",
                courses=[
                    Course(id="pol601", title="Political Behavior", credits=3, difficulty=6, weekly_hours=7, skills=["Voting", "Behavior"]),
                    Course(id="pol602", title="Political Communication", credits=3, difficulty=5, weekly_hours=6, skills=["Media", "Communication"]),
                    Course(id="pol603", title="Democracy & Democratization", credits=3, difficulty=6, weekly_hours=7, skills=["Democracy"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Research Project",
                courses=[
                    Course(id="pol701", title="Senior Thesis I", credits=3, difficulty=7, weekly_hours=9, skills=["Research", "Writing"]),
                    Course(id="pol702", title="Advanced Seminar", credits=3, difficulty=6, weekly_hours=7, skills=["Specialization"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="pol801", title="Senior Thesis II", credits=3, difficulty=7, weekly_hours=10, skills=["Thesis", "Defense"]),
                    Course(id="pol802", title="Career Preparation", credits=1, difficulty=2, weekly_hours=2, skills=["Career", "Public Service"]),
                ],
            ),
        },
        # History at Columbia
        "history": {
            1: SemesterCurriculum(
                semester=1,
                notes="History Foundation",
                courses=[
                    Course(id="hist101", title="World History I", credits=3, difficulty=4, weekly_hours=6, skills=["World History", "Ancient"]),
                    Course(id="hist102", title="American History I", credits=3, difficulty=4, weekly_hours=6, skills=["US History", "Colonial"]),
                    Course(id="hist103", title="Historical Methods", credits=3, difficulty=5, weekly_hours=7, skills=["Research", "Methods"]),
                ],
            ),
            2: SemesterCurriculum(
                semester=2,
                notes="Regional & Thematic History",
                courses=[
                    Course(id="hist201", title="World History II", credits=3, difficulty=4, weekly_hours=6, skills=["Modern History"]),
                    Course(id="hist202", title="American History II", credits=3, difficulty=4, weekly_hours=6, skills=["US Modern"]),
                    Course(id="hist203", title="European History", credits=3, difficulty=5, weekly_hours=6, skills=["Europe"]),
                ],
            ),
            3: SemesterCurriculum(
                semester=3,
                notes="Specialized Periods",
                courses=[
                    Course(id="hist301", title="Medieval History", credits=3, difficulty=5, weekly_hours=6, skills=["Medieval", "Middle Ages"]),
                    Course(id="hist302", title="Renaissance & Reformation", credits=3, difficulty=5, weekly_hours=6, skills=["Renaissance"]),
                    Course(id="hist303", title="Asian History", credits=3, difficulty=5, weekly_hours=6, skills=["Asia", "China"]),
                ],
            ),
            4: SemesterCurriculum(
                semester=4,
                notes="Modern History",
                courses=[
                    Course(id="hist401", title="Modern European History", credits=3, difficulty=5, weekly_hours=6, skills=["20th Century"]),
                    Course(id="hist402", title="Latin American History", credits=3, difficulty=5, weekly_hours=6, skills=["Latin America"]),
                    Course(id="hist403", title="African History", credits=3, difficulty=5, weekly_hours=6, skills=["Africa"]),
                ],
            ),
            5: SemesterCurriculum(
                semester=5,
                notes="Thematic Studies",
                courses=[
                    Course(id="hist501", title="Military History", credits=3, difficulty=5, weekly_hours=6, skills=["War", "Strategy"]),
                    Course(id="hist502", title="Economic History", credits=3, difficulty=6, weekly_hours=7, skills=["Economics", "Development"]),
                    Course(id="hist503", title="Social History", credits=3, difficulty=5, weekly_hours=6, skills=["Society", "Culture"]),
                ],
            ),
            6: SemesterCurriculum(
                semester=6,
                notes="Advanced Topics",
                courses=[
                    Course(id="hist601", title="Intellectual History", credits=3, difficulty=6, weekly_hours=7, skills=["Ideas", "Philosophy"]),
                    Course(id="hist602", title="Gender & History", credits=3, difficulty=5, weekly_hours=6, skills=["Gender", "Women"]),
                    Course(id="hist603", title="Environmental History", credits=3, difficulty=5, weekly_hours=6, skills=["Environment"]),
                ],
            ),
            7: SemesterCurriculum(
                semester=7,
                notes="Research Seminar",
                courses=[
                    Course(id="hist701", title="Historiography", credits=3, difficulty=6, weekly_hours=7, skills=["Historical Theory"]),
                    Course(id="hist702", title="Senior Research Seminar", credits=3, difficulty=7, weekly_hours=9, skills=["Research", "Thesis"]),
                ],
            ),
            8: SemesterCurriculum(
                semester=8,
                notes="Capstone & Career",
                courses=[
                    Course(id="hist801", title="History Capstone", credits=3, difficulty=7, weekly_hours=10, skills=["Thesis", "Writing"]),
                    Course(id="hist802", title="Career Preparation", credits=1, difficulty=2, weekly_hours=2, skills=["Career", "Museums"]),
                ],
            ),
        },
    },
}
