# Comprehensive curriculum data with detailed semester-by-semester breakdowns
# Each major includes courses with descriptions, difficulty, and real-world context

CURRICULUMS = {
    "cs": {
        "major_name": "Computer Science",
        "total_semesters": 8,
        "semesters": {
            1: {
                "semester": 1,
                "title": "Foundation Year - Fall",
                "description": "Build your programming foundation and learn computational thinking",
                "courses": [
                    {
                        "id": "CS101",
                        "name": "Introduction to Programming",
                        "credits": 4,
                        "description": "Master the basics of coding with Python. Learn variables, loops, functions, and problem-solving.",
                        "difficulty": "medium",
                        "skills": ["Python basics", "Problem solving", "Debugging"],
                        "real_world": "Foundation for all software development roles"
                    },
                    {
                        "id": "MATH141",
                        "name": "Calculus I",
                        "credits": 4,
                        "description": "Limits, derivatives, and their applications. Essential math for CS algorithms.",
                        "difficulty": "high",
                        "skills": ["Calculus", "Mathematical reasoning"],
                        "real_world": "Used in machine learning, graphics, and optimization"
                    },
                    {
                        "id": "ENG101",
                        "name": "English Composition",
                        "credits": 3,
                        "description": "Develop clear writing and communication skills for technical documentation.",
                        "difficulty": "low",
                        "skills": ["Technical writing", "Communication"],
                        "real_world": "Write clear code documentation and project proposals"
                    }
                ],
                "tips": "Focus on understanding programming concepts, not just syntax. Start coding projects early!"
            },
            2: {
                "semester": 2,
                "title": "Foundation Year - Spring",
                "description": "Deepen programming skills and explore data organization",
                "courses": [
                    {
                        "id": "CS102",
                        "name": "Data Structures",
                        "credits": 4,
                        "description": "Learn arrays, linked lists, stacks, queues, trees, and hash tables. Organize data efficiently.",
                        "difficulty": "high",
                        "skills": ["Data organization", "Algorithm complexity", "Memory management"],
                        "real_world": "Core skill for coding interviews and system design"
                    },
                    {
                        "id": "CS201",
                        "name": "Discrete Mathematics",
                        "credits": 3,
                        "description": "Logic, sets, graphs, and proof techniques. The math behind computer science.",
                        "difficulty": "high",
                        "skills": ["Logic", "Proofs", "Graph theory"],
                        "real_world": "Foundation for algorithms, cryptography, and databases"
                    },
                    {
                        "id": "MATH142",
                        "name": "Calculus II",
                        "credits": 4,
                        "description": "Integration, sequences, and series. Continue building mathematical foundation.",
                        "difficulty": "high",
                        "skills": ["Integration", "Series", "Advanced calculus"],
                        "real_world": "Applied in physics engines and scientific computing"
                    }
                ],
                "tips": "Data structures are crucial - practice implementing them from scratch!"
            },
            3: {
                "semester": 3,
                "title": "Sophomore Year - Fall",
                "description": "Master algorithms and start building systems",
                "courses": [
                    {
                        "id": "CS203",
                        "name": "Algorithms",
                        "credits": 4,
                        "description": "Sorting, searching, dynamic programming, greedy algorithms. Solve complex problems efficiently.",
                        "difficulty": "very_high",
                        "skills": ["Algorithm design", "Optimization", "Problem solving"],
                        "real_world": "Essential for technical interviews and system optimization"
                    },
                    {
                        "id": "CS210",
                        "name": "Computer Organization",
                        "credits": 3,
                        "description": "How computers work at the hardware level. Assembly language and architecture.",
                        "difficulty": "medium",
                        "skills": ["Assembly", "Hardware basics", "Low-level programming"],
                        "real_world": "Understanding performance and system limitations"
                    },
                    {
                        "id": "STAT200",
                        "name": "Probability & Statistics",
                        "credits": 3,
                        "description": "Probability theory, distributions, and statistical inference. Key for data science.",
                        "difficulty": "medium",
                        "skills": ["Probability", "Statistics", "Data analysis"],
                        "real_world": "Foundation for machine learning and data science"
                    }
                ],
                "tips": "Algorithms is the most important course - practice on LeetCode and HackerRank!"
            },
            4: {
                "semester": 4,
                "title": "Sophomore Year - Spring",
                "description": "Build real applications and understand operating systems",
                "courses": [
                    {
                        "id": "CS220",
                        "name": "Operating Systems",
                        "credits": 4,
                        "description": "Processes, threads, memory management, file systems. How OSes manage resources.",
                        "difficulty": "high",
                        "skills": ["Concurrency", "Memory management", "System programming"],
                        "real_world": "Critical for backend development and system programming"
                    },
                    {
                        "id": "CS225",
                        "name": "Database Systems",
                        "credits": 3,
                        "description": "SQL, database design, transactions, and indexing. Store and retrieve data efficiently.",
                        "difficulty": "medium",
                        "skills": ["SQL", "Database design", "Query optimization"],
                        "real_world": "Every application needs data storage - databases are universal"
                    },
                    {
                        "id": "CS230",
                        "name": "Software Engineering",
                        "credits": 3,
                        "description": "Design patterns, testing, version control, and team collaboration. Build real projects.",
                        "difficulty": "medium",
                        "skills": ["Git", "Testing", "Design patterns", "Teamwork"],
                        "real_world": "How professional software development actually works"
                    }
                ],
                "tips": "Start applying for summer internships - hands-on experience is invaluable!"
            },
            5: {
                "semester": 5,
                "title": "Junior Year - Fall",
                "description": "Specialize and explore advanced topics",
                "courses": [
                    {
                        "id": "CS301",
                        "name": "Computer Networks",
                        "credits": 3,
                        "description": "TCP/IP, HTTP, network protocols, and distributed systems. How the internet works.",
                        "difficulty": "medium",
                        "skills": ["Networking", "Protocols", "Client-server architecture"],
                        "real_world": "Build web apps, APIs, and understand cloud infrastructure"
                    },
                    {
                        "id": "CS310",
                        "name": "Machine Learning",
                        "credits": 3,
                        "description": "Supervised learning, neural networks, and AI algorithms. Teach computers to learn.",
                        "difficulty": "high",
                        "skills": ["ML algorithms", "Python libraries", "Data modeling"],
                        "real_world": "Hot field with high demand - AI is everywhere"
                    },
                    {
                        "id": "CS3XX",
                        "name": "Technical Elective 1",
                        "credits": 3,
                        "description": "Choose from: Mobile Dev, Web Dev, Cybersecurity, Cloud Computing, or Game Development.",
                        "difficulty": "medium",
                        "skills": ["Specialized skills"],
                        "real_world": "Follow your interests and career goals"
                    }
                ],
                "tips": "This is when you differentiate yourself - choose electives strategically!"
            },
            6: {
                "semester": 6,
                "title": "Junior Year - Spring",
                "description": "Advanced specialization and project work",
                "courses": [
                    {
                        "id": "CS320",
                        "name": "Computer Security",
                        "credits": 3,
                        "description": "Cryptography, network security, vulnerabilities, and ethical hacking.",
                        "difficulty": "medium",
                        "skills": ["Security", "Cryptography", "Ethical hacking"],
                        "real_world": "Security is critical for every company - always in demand"
                    },
                    {
                        "id": "CS350",
                        "name": "Senior Capstone Project I",
                        "credits": 3,
                        "description": "Start building a substantial software project. Apply everything you've learned.",
                        "difficulty": "high",
                        "skills": ["Project management", "Full-stack development"],
                        "real_world": "Portfolio piece for job applications"
                    },
                    {
                        "id": "CS3XX",
                        "name": "Technical Elective 2",
                        "credits": 3,
                        "description": "Continue specializing in your chosen area of focus.",
                        "difficulty": "medium",
                        "skills": ["Advanced specialized skills"],
                        "real_world": "Build depth in your chosen specialty"
                    }
                ],
                "tips": "Your capstone project will be a key talking point in interviews!"
            },
            7: {
                "semester": 7,
                "title": "Senior Year - Fall",
                "description": "Polish your skills and prepare for career",
                "courses": [
                    {
                        "id": "CS351",
                        "name": "Senior Capstone Project II",
                        "credits": 3,
                        "description": "Complete and polish your capstone. Present to faculty and industry professionals.",
                        "difficulty": "high",
                        "skills": ["Project completion", "Presentation", "Documentation"],
                        "real_world": "Showcase your abilities to potential employers"
                    },
                    {
                        "id": "CS400",
                        "name": "Theory of Computation",
                        "credits": 3,
                        "description": "Formal languages, automata, and computational complexity. The theory behind computing.",
                        "difficulty": "very_high",
                        "skills": ["Theoretical CS", "Complexity theory"],
                        "real_world": "Understand fundamental limits of computation"
                    },
                    {
                        "id": "CS4XX",
                        "name": "Technical Elective 3",
                        "credits": 3,
                        "description": "Advanced topics in your specialization area.",
                        "difficulty": "high",
                        "skills": ["Expert-level skills"],
                        "real_world": "Become an expert in your chosen field"
                    }
                ],
                "tips": "Start your job search early - attend career fairs and network actively!"
            },
            8: {
                "semester": 8,
                "title": "Senior Year - Spring",
                "description": "Final semester - tie up loose ends and graduate!",
                "courses": [
                    {
                        "id": "CS410",
                        "name": "Professional Development",
                        "credits": 2,
                        "description": "Resume building, interview prep, salary negotiation, and career planning.",
                        "difficulty": "low",
                        "skills": ["Interview skills", "Negotiation", "Career planning"],
                        "real_world": "Get the job and compensation you deserve"
                    },
                    {
                        "id": "CS4XX",
                        "name": "Technical Elective 4",
                        "credits": 3,
                        "description": "Final elective - explore something new or deepen expertise.",
                        "difficulty": "medium",
                        "skills": ["Diverse technical skills"],
                        "real_world": "Round out your skill set"
                    },
                    {
                        "id": "GEN400",
                        "name": "Senior Seminar",
                        "credits": 3,
                        "description": "Reflect on your education and prepare for the next chapter.",
                        "difficulty": "low",
                        "skills": ["Reflection", "Life planning"],
                        "real_world": "Transition from student to professional"
                    }
                ],
                "tips": "Enjoy your last semester, but stay focused on landing that great job!"
            }
        },
        "career_paths": [
            "Software Engineer",
            "Data Scientist",
            "Machine Learning Engineer",
            "Full Stack Developer",
            "DevOps Engineer",
            "Cybersecurity Analyst"
        ],
        "skills_gained": [
            "Programming in multiple languages",
            "Algorithm design and analysis",
            "System architecture",
            "Database management",
            "Software engineering practices",
            "Problem-solving and critical thinking"
        ]
    },
    "business": {
        "major_name": "Business Administration",
        "total_semesters": 8,
        "semesters": {
            1: {
                "semester": 1,
                "title": "Foundation Year - Fall",
                "description": "Introduction to business fundamentals and core concepts",
                "courses": [
                    {
                        "id": "BUS101",
                        "name": "Introduction to Business",
                        "credits": 3,
                        "description": "Overview of business principles, entrepreneurship, and the global economy.",
                        "difficulty": "low",
                        "skills": ["Business basics", "Economic literacy"],
                        "real_world": "Understand how businesses operate and create value"
                    },
                    {
                        "id": "ECON101",
                        "name": "Microeconomics",
                        "credits": 3,
                        "description": "Supply and demand, market structures, and individual decision-making.",
                        "difficulty": "medium",
                        "skills": ["Economic analysis", "Market thinking"],
                        "real_world": "Understand pricing, competition, and consumer behavior"
                    },
                    {
                        "id": "MATH110",
                        "name": "Business Mathematics",
                        "credits": 3,
                        "description": "Algebra, statistics, and quantitative analysis for business applications.",
                        "difficulty": "medium",
                        "skills": ["Quantitative analysis", "Financial calculations"],
                        "real_world": "Make data-driven business decisions"
                    },
                    {
                        "id": "ENG101",
                        "name": "Business Communication",
                        "credits": 3,
                        "description": "Professional writing, presentations, and communication skills.",
                        "difficulty": "low",
                        "skills": ["Professional communication", "Presentations"],
                        "real_world": "Essential for every business role - clear communication wins"
                    }
                ],
                "tips": "Network from day one - relationships matter as much as grades in business!"
            },
            2: {
                "semester": 2,
                "title": "Foundation Year - Spring",
                "description": "Build on fundamentals and explore different business functions",
                "courses": [
                    {
                        "id": "ACC201",
                        "name": "Financial Accounting",
                        "credits": 3,
                        "description": "Learn to read financial statements, understand debits/credits, and analyze company health.",
                        "difficulty": "medium",
                        "skills": ["Financial statements", "Accounting basics"],
                        "real_world": "Every business needs to track money - universal skill"
                    },
                    {
                        "id": "ECON102",
                        "name": "Macroeconomics",
                        "credits": 3,
                        "description": "GDP, inflation, monetary policy, and global economic trends.",
                        "difficulty": "medium",
                        "skills": ["Economic policy", "Global economics"],
                        "real_world": "Understand business cycles and economic conditions"
                    },
                    {
                        "id": "MKT201",
                        "name": "Marketing Fundamentals",
                        "credits": 3,
                        "description": "Consumer behavior, branding, and marketing strategy. Learn to create value.",
                        "difficulty": "low",
                        "skills": ["Marketing strategy", "Branding", "Customer insight"],
                        "real_world": "Marketing drives revenue - critical for any business"
                    },
                    {
                        "id": "STAT201",
                        "name": "Business Statistics",
                        "credits": 3,
                        "description": "Data analysis, hypothesis testing, and statistical decision-making.",
                        "difficulty": "medium",
                        "skills": ["Data analysis", "Statistical reasoning"],
                        "real_world": "Make informed decisions with data, not gut feelings"
                    }
                ],
                "tips": "Try to get a part-time job or volunteer for a student organization - experience matters!"
            },
            3: {
                "semester": 3,
                "title": "Sophomore Year - Fall",
                "description": "Explore core business functions in depth",
                "courses": [
                    {
                        "id": "FIN301",
                        "name": "Corporate Finance",
                        "credits": 3,
                        "description": "Investment decisions, capital budgeting, and financial management.",
                        "difficulty": "high",
                        "skills": ["Financial analysis", "Investment decisions"],
                        "real_world": "How companies manage money and make investment decisions"
                    },
                    {
                        "id": "MGT301",
                        "name": "Organizational Behavior",
                        "credits": 3,
                        "description": "Leadership, motivation, team dynamics, and workplace culture.",
                        "difficulty": "low",
                        "skills": ["Leadership", "Team management", "People skills"],
                        "real_world": "Managing people is the hardest part of business"
                    },
                    {
                        "id": "OPS301",
                        "name": "Operations Management",
                        "credits": 3,
                        "description": "Supply chain, logistics, quality control, and process optimization.",
                        "difficulty": "medium",
                        "skills": ["Process improvement", "Supply chain"],
                        "real_world": "How companies actually produce and deliver products"
                    },
                    {
                        "id": "LAW201",
                        "name": "Business Law",
                        "credits": 3,
                        "description": "Contracts, liability, employment law, and legal compliance.",
                        "difficulty": "medium",
                        "skills": ["Legal compliance", "Contract basics"],
                        "real_world": "Avoid costly legal mistakes and understand regulations"
                    }
                ],
                "tips": "Start thinking about your concentration - finance, marketing, management, etc."
            },
            4: {
                "semester": 4,
                "title": "Sophomore Year - Spring",
                "description": "Develop analytical and strategic thinking skills",
                "courses": [
                    {
                        "id": "ACC202",
                        "name": "Managerial Accounting",
                        "credits": 3,
                        "description": "Cost accounting, budgeting, and internal decision-making.",
                        "difficulty": "medium",
                        "skills": ["Cost analysis", "Budgeting"],
                        "real_world": "Help managers make better operational decisions"
                    },
                    {
                        "id": "MIS301",
                        "name": "Management Information Systems",
                        "credits": 3,
                        "description": "Business technology, databases, and digital transformation.",
                        "difficulty": "low",
                        "skills": ["Tech literacy", "Data systems"],
                        "real_world": "Every business is a tech business now"
                    },
                    {
                        "id": "BUS301",
                        "name": "Business Ethics",
                        "credits": 3,
                        "description": "Corporate responsibility, ethical dilemmas, and sustainable business practices.",
                        "difficulty": "low",
                        "skills": ["Ethical reasoning", "CSR"],
                        "real_world": "Build trust and avoid scandals - ethics matter"
                    },
                    {
                        "id": "ELEC1",
                        "name": "Business Elective 1",
                        "credits": 3,
                        "description": "Choose based on your interest: International Business, Entrepreneurship, or HR Management.",
                        "difficulty": "medium",
                        "skills": ["Specialized business knowledge"],
                        "real_world": "Start specializing in your area of interest"
                    }
                ],
                "tips": "Apply for summer internships now - they're crucial for full-time job offers!"
            },
            5: {
                "semester": 5,
                "title": "Junior Year - Fall",
                "description": "Specialize in your chosen concentration",
                "courses": [
                    {
                        "id": "STR401",
                        "name": "Strategic Management",
                        "credits": 3,
                        "description": "Competitive strategy, business models, and long-term planning.",
                        "difficulty": "high",
                        "skills": ["Strategic thinking", "Competitive analysis"],
                        "real_world": "Think like a CEO - see the big picture"
                    },
                    {
                        "id": "CON401",
                        "name": "Concentration Course 1",
                        "credits": 3,
                        "description": "Deep dive into your chosen specialty (Finance, Marketing, Management, etc.).",
                        "difficulty": "medium",
                        "skills": ["Specialized expertise"],
                        "real_world": "Become an expert in your field"
                    },
                    {
                        "id": "CON402",
                        "name": "Concentration Course 2",
                        "credits": 3,
                        "description": "Continue building expertise in your concentration.",
                        "difficulty": "medium",
                        "skills": ["Advanced specialized skills"],
                        "real_world": "Differentiate yourself from general business grads"
                    },
                    {
                        "id": "ELEC2",
                        "name": "Business Elective 2",
                        "credits": 3,
                        "description": "Explore adjacent areas or double down on your specialty.",
                        "difficulty": "medium",
                        "skills": ["Diverse business knowledge"],
                        "real_world": "Round out your skill set"
                    }
                ],
                "tips": "This is your chance to stand out - choose your concentration wisely!"
            },
            6: {
                "semester": 6,
                "title": "Junior Year - Spring",
                "description": "Advanced topics and practical application",
                "courses": [
                    {
                        "id": "CON403",
                        "name": "Concentration Course 3",
                        "credits": 3,
                        "description": "Advanced topics in your chosen area.",
                        "difficulty": "high",
                        "skills": ["Expert-level knowledge"],
                        "real_world": "Position yourself as a specialist"
                    },
                    {
                        "id": "BUS410",
                        "name": "Business Analytics",
                        "credits": 3,
                        "description": "Data-driven decision making, predictive analytics, and business intelligence.",
                        "difficulty": "high",
                        "skills": ["Data analytics", "Excel", "Business intelligence"],
                        "real_world": "Hot skill - every company needs data-savvy people"
                    },
                    {
                        "id": "MKT410",
                        "name": "Digital Marketing",
                        "credits": 3,
                        "description": "SEO, social media, content marketing, and online advertising.",
                        "difficulty": "low",
                        "skills": ["Digital marketing", "Social media", "Analytics"],
                        "real_world": "Marketing is increasingly digital - stay current"
                    },
                    {
                        "id": "ELEC3",
                        "name": "Business Elective 3",
                        "credits": 3,
                        "description": "Choose a course that complements your career goals.",
                        "difficulty": "medium",
                        "skills": ["Complementary skills"],
                        "real_world": "Build a unique skill combination"
                    }
                ],
                "tips": "Polish your resume and LinkedIn - recruiters are watching!"
            },
            7: {
                "semester": 7,
                "title": "Senior Year - Fall",
                "description": "Capstone experience and career preparation",
                "courses": [
                    {
                        "id": "BUS490",
                        "name": "Business Capstone Project",
                        "credits": 3,
                        "description": "Work with a real company to solve actual business problems. Apply everything you've learned.",
                        "difficulty": "high",
                        "skills": ["Project management", "Client management", "Integration"],
                        "real_world": "Demonstrate your value to future employers"
                    },
                    {
                        "id": "CON404",
                        "name": "Concentration Course 4",
                        "credits": 3,
                        "description": "Final deep dive into your specialty area.",
                        "difficulty": "high",
                        "skills": ["Mastery-level expertise"],
                        "real_world": "Complete your specialization"
                    },
                    {
                        "id": "ENT401",
                        "name": "Entrepreneurship",
                        "credits": 3,
                        "description": "Start-up creation, business planning, and innovation.",
                        "difficulty": "medium",
                        "skills": ["Entrepreneurial mindset", "Business planning"],
                        "real_world": "Maybe you'll start your own company someday"
                    },
                    {
                        "id": "ELEC4",
                        "name": "Business Elective 4",
                        "credits": 3,
                        "description": "Final chance to explore or specialize.",
                        "difficulty": "medium",
                        "skills": ["Final skill additions"],
                        "real_world": "Fill any gaps in your knowledge"
                    }
                ],
                "tips": "Attend every career fair and networking event - your network is your net worth!"
            },
            8: {
                "semester": 8,
                "title": "Senior Year - Spring",
                "description": "Final semester - prepare for career launch",
                "courses": [
                    {
                        "id": "BUS495",
                        "name": "Professional Development",
                        "credits": 2,
                        "description": "Interview skills, salary negotiation, networking, and career strategy.",
                        "difficulty": "low",
                        "skills": ["Interview prep", "Negotiation", "Networking"],
                        "real_world": "Land the job and maximize your offer"
                    },
                    {
                        "id": "GLB401",
                        "name": "Global Business Strategy",
                        "credits": 3,
                        "description": "International markets, cross-cultural management, and global expansion.",
                        "difficulty": "medium",
                        "skills": ["Global perspective", "Cultural intelligence"],
                        "real_world": "Business is global - understand international markets"
                    },
                    {
                        "id": "ELEC5",
                        "name": "Business Elective 5",
                        "credits": 3,
                        "description": "Final elective - explore something new.",
                        "difficulty": "low",
                        "skills": ["Diverse knowledge"],
                        "real_world": "Stay curious and keep learning"
                    },
                    {
                        "id": "SEM401",
                        "name": "Senior Seminar",
                        "credits": 2,
                        "description": "Reflect on your journey and plan your career path.",
                        "difficulty": "low",
                        "skills": ["Self-reflection", "Career planning"],
                        "real_world": "Transition from student to professional"
                    }
                ],
                "tips": "Celebrate your achievements, but stay focused on starting your career strong!"
            }
        },
        "career_paths": [
            "Financial Analyst",
            "Marketing Manager",
            "Management Consultant",
            "Operations Manager",
            "Business Analyst",
            "Entrepreneur"
        ],
        "skills_gained": [
            "Strategic thinking",
            "Financial analysis",
            "Marketing strategy",
            "Leadership and management",
            "Data-driven decision making",
            "Communication and presentation"
        ]
    },
    "engineering": {
        "major_name": "Engineering (General)",
        "total_semesters": 8,
        "semesters": {
            1: {
                "semester": 1,
                "title": "Foundation Year - Fall",
                "description": "Build strong math and science foundation",
                "courses": [
                    {
                        "id": "ENG101",
                        "name": "Introduction to Engineering",
                        "credits": 3,
                        "description": "Overview of engineering disciplines and problem-solving methodologies.",
                        "difficulty": "medium",
                        "skills": ["Engineering thinking", "Problem solving"],
                        "real_world": "Understand what engineers actually do"
                    },
                    {
                        "id": "MATH141",
                        "name": "Calculus I",
                        "credits": 4,
                        "description": "Limits, derivatives, and applications. Essential for all engineering.",
                        "difficulty": "high",
                        "skills": ["Calculus", "Mathematical modeling"],
                        "real_world": "Foundation for physics, circuits, and systems"
                    },
                    {
                        "id": "CHEM101",
                        "name": "General Chemistry I",
                        "credits": 4,
                        "description": "Atomic structure, bonding, and reactions. Materials science foundation.",
                        "difficulty": "high",
                        "skills": ["Chemistry", "Materials"],
                        "real_world": "Understand material properties and reactions"
                    },
                    {
                        "id": "CS101",
                        "name": "Programming for Engineers",
                        "credits": 3,
                        "description": "Learn Python/MATLAB for engineering calculations and simulations.",
                        "difficulty": "medium",
                        "skills": ["Programming", "Computation"],
                        "real_world": "Automate calculations and analyze data"
                    }
                ],
                "tips": "Engineering is hard - find a study group early and don't fall behind!"
            },
            2: {
                "semester": 2,
                "title": "Foundation Year - Spring",
                "description": "Continue building fundamental skills",
                "courses": [
                    {
                        "id": "MATH142",
                        "name": "Calculus II",
                        "credits": 4,
                        "description": "Integration, series, and differential equations.",
                        "difficulty": "very_high",
                        "skills": ["Integration", "Differential equations"],
                        "real_world": "Model dynamic systems and solve complex problems"
                    },
                    {
                        "id": "PHYS141",
                        "name": "Physics I: Mechanics",
                        "credits": 4,
                        "description": "Newton's laws, energy, momentum, and rotational motion.",
                        "difficulty": "high",
                        "skills": ["Mechanics", "Physics"],
                        "real_world": "Foundation for all mechanical systems"
                    },
                    {
                        "id": "CHEM102",
                        "name": "General Chemistry II",
                        "credits": 4,
                        "description": "Thermodynamics, kinetics, and equilibrium.",
                        "difficulty": "high",
                        "skills": ["Thermodynamics", "Chemical processes"],
                        "real_world": "Energy systems and chemical engineering"
                    },
                    {
                        "id": "COMM101",
                        "name": "Technical Communication",
                        "credits": 2,
                        "description": "Write clear technical reports and documentation.",
                        "difficulty": "low",
                        "skills": ["Technical writing"],
                        "real_world": "Communicate designs and findings effectively"
                    }
                ],
                "tips": "Physics and Calc II are brutal - use office hours and tutoring resources!"
            },
            3: {
                "semester": 3,
                "title": "Sophomore Year - Fall",
                "description": "Apply fundamentals to engineering problems",
                "courses": [
                    {
                        "id": "MATH241",
                        "name": "Calculus III",
                        "credits": 4,
                        "description": "Multivariable calculus and vector analysis.",
                        "difficulty": "very_high",
                        "skills": ["Multivariable calculus", "Vectors"],
                        "real_world": "Analyze 3D systems and fields"
                    },
                    {
                        "id": "PHYS142",
                        "name": "Physics II: Electricity & Magnetism",
                        "credits": 4,
                        "description": "Electric fields, circuits, and electromagnetic waves.",
                        "difficulty": "very_high",
                        "skills": ["Circuits", "Electromagnetism"],
                        "real_world": "Foundation for electrical engineering"
                    },
                    {
                        "id": "ENGR201",
                        "name": "Statics",
                        "credits": 3,
                        "description": "Forces, moments, and equilibrium of structures.",
                        "difficulty": "high",
                        "skills": ["Structural analysis", "Force balance"],
                        "real_world": "Design buildings, bridges, and mechanical systems"
                    },
                    {
                        "id": "ENGR205",
                        "name": "Materials Science",
                        "credits": 3,
                        "description": "Properties of metals, polymers, and composites.",
                        "difficulty": "medium",
                        "skills": ["Materials", "Material selection"],
                        "real_world": "Choose the right materials for applications"
                    }
                ],
                "tips": "The math gets harder - stay on top of homework and practice problems!"
            },
            4: {
                "semester": 4,
                "title": "Sophomore Year - Spring",
                "description": "Deepen engineering analysis skills",
                "courses": [
                    {
                        "id": "MATH246",
                        "name": "Differential Equations",
                        "credits": 3,
                        "description": "Solve ODEs and PDEs for engineering systems.",
                        "difficulty": "very_high",
                        "skills": ["Differential equations", "System modeling"],
                        "real_world": "Model everything from circuits to fluid flow"
                    },
                    {
                        "id": "ENGR202",
                        "name": "Dynamics",
                        "credits": 3,
                        "description": "Motion, acceleration, and kinetics of systems.",
                        "difficulty": "high",
                        "skills": ["Dynamics", "Motion analysis"],
                        "real_world": "Design moving systems like robots and vehicles"
                    },
                    {
                        "id": "ENGR210",
                        "name": "Thermodynamics",
                        "credits": 3,
                        "description": "Energy, heat transfer, and power systems.",
                        "difficulty": "very_high",
                        "skills": ["Energy systems", "Thermodynamics"],
                        "real_world": "Design engines, HVAC, and power plants"
                    },
                    {
                        "id": "ENGR215",
                        "name": "Circuits & Electronics",
                        "credits": 4,
                        "description": "Analyze and design electrical circuits.",
                        "difficulty": "high",
                        "skills": ["Circuit analysis", "Electronics"],
                        "real_world": "Every device has circuits - universal skill"
                    }
                ],
                "tips": "Engineering gets real now - start thinking about your specialization!"
            },
            5: {
                "semester": 5,
                "title": "Junior Year - Fall",
                "description": "Specialize and design real systems",
                "courses": [
                    {
                        "id": "ENGR301",
                        "name": "Engineering Design I",
                        "credits": 3,
                        "description": "Design process, prototyping, and project planning.",
                        "difficulty": "medium",
                        "skills": ["Design process", "CAD", "Prototyping"],
                        "real_world": "Turn ideas into physical products"
                    },
                    {
                        "id": "SPEC301",
                        "name": "Specialization Course 1",
                        "credits": 3,
                        "description": "Choose your track: Mechanical, Electrical, Civil, or Chemical Engineering.",
                        "difficulty": "high",
                        "skills": ["Specialized engineering"],
                        "real_world": "Become an expert in your chosen field"
                    },
                    {
                        "id": "SPEC302",
                        "name": "Specialization Course 2",
                        "credits": 3,
                        "description": "Continue building depth in your specialization.",
                        "difficulty": "high",
                        "skills": ["Advanced specialized skills"],
                        "real_world": "Differentiate yourself as a specialist"
                    },
                    {
                        "id": "ENGR310",
                        "name": "Engineering Economics",
                        "credits": 3,
                        "description": "Cost analysis, ROI, and project evaluation.",
                        "difficulty": "medium",
                        "skills": ["Cost analysis", "Project evaluation"],
                        "real_world": "Engineers need to understand business too"
                    }
                ],
                "tips": "Start looking for internships - hands-on experience is critical!"
            },
            6: {
                "semester": 6,
                "title": "Junior Year - Spring",
                "description": "Advanced topics and laboratory work",
                "courses": [
                    {
                        "id": "ENGR302",
                        "name": "Engineering Design II",
                        "credits": 3,
                        "description": "Complete design project with testing and validation.",
                        "difficulty": "high",
                        "skills": ["Design validation", "Testing"],
                        "real_world": "Prove your design works in the real world"
                    },
                    {
                        "id": "SPEC303",
                        "name": "Specialization Course 3",
                        "credits": 3,
                        "description": "Advanced topics in your engineering specialty.",
                        "difficulty": "very_high",
                        "skills": ["Expert-level knowledge"],
                        "real_world": "Master your specialty"
                    },
                    {
                        "id": "SPEC304",
                        "name": "Specialization Lab",
                        "credits": 2,
                        "description": "Hands-on laboratory work in your field.",
                        "difficulty": "medium",
                        "skills": ["Lab skills", "Experimental design"],
                        "real_world": "Learn by doing - test theories in practice"
                    },
                    {
                        "id": "ENGR320",
                        "name": "Systems Engineering",
                        "credits": 3,
                        "description": "Integrate components into complete systems.",
                        "difficulty": "high",
                        "skills": ["Systems thinking", "Integration"],
                        "real_world": "See the big picture - how parts work together"
                    }
                ],
                "tips": "Your design project is your portfolio piece - make it impressive!"
            },
            7: {
                "semester": 7,
                "title": "Senior Year - Fall",
                "description": "Capstone project and advanced specialization",
                "courses": [
                    {
                        "id": "ENGR401",
                        "name": "Senior Capstone Project I",
                        "credits": 3,
                        "description": "Major engineering project - design, build, and test a real system.",
                        "difficulty": "very_high",
                        "skills": ["Project management", "System design"],
                        "real_world": "Showcase your engineering abilities"
                    },
                    {
                        "id": "SPEC401",
                        "name": "Advanced Specialization Course",
                        "credits": 3,
                        "description": "Cutting-edge topics in your field.",
                        "difficulty": "very_high",
                        "skills": ["State-of-the-art knowledge"],
                        "real_world": "Stay current with latest technology"
                    },
                    {
                        "id": "ENGR410",
                        "name": "Engineering Ethics",
                        "credits": 2,
                        "description": "Professional responsibility, safety, and ethical decision-making.",
                        "difficulty": "low",
                        "skills": ["Professional ethics", "Safety"],
                        "real_world": "Engineers have lives in their hands - ethics matter"
                    },
                    {
                        "id": "ELEC401",
                        "name": "Technical Elective",
                        "credits": 3,
                        "description": "Explore adjacent fields or deepen expertise.",
                        "difficulty": "high",
                        "skills": ["Specialized knowledge"],
                        "real_world": "Build unique skill combinations"
                    }
                ],
                "tips": "Your capstone is what employers will ask about - put in the effort!"
            },
            8: {
                "semester": 8,
                "title": "Senior Year - Spring",
                "description": "Complete capstone and prepare for career",
                "courses": [
                    {
                        "id": "ENGR402",
                        "name": "Senior Capstone Project II",
                        "credits": 3,
                        "description": "Complete, test, and present your capstone project.",
                        "difficulty": "very_high",
                        "skills": ["Project completion", "Presentation"],
                        "real_world": "Demonstrate you can deliver real solutions"
                    },
                    {
                        "id": "ENGR420",
                        "name": "Engineering Management",
                        "credits": 3,
                        "description": "Project management, leadership, and team dynamics.",
                        "difficulty": "medium",
                        "skills": ["Project management", "Leadership"],
                        "real_world": "Engineers often become managers - prepare now"
                    },
                    {
                        "id": "ENGR430",
                        "name": "Professional Practice",
                        "credits": 2,
                        "description": "PE exam prep, licensure, and career development.",
                        "difficulty": "medium",
                        "skills": ["Professional licensing", "Career planning"],
                        "real_world": "Get licensed and advance your career"
                    },
                    {
                        "id": "ELEC402",
                        "name": "Final Technical Elective",
                        "credits": 3,
                        "description": "Last chance to explore new topics.",
                        "difficulty": "medium",
                        "skills": ["Diverse technical knowledge"],
                        "real_world": "Stay curious and keep learning"
                    }
                ],
                "tips": "Congratulations, engineer! Start studying for the FE exam and land that job!"
            }
        },
        "career_paths": [
            "Mechanical Engineer",
            "Electrical Engineer",
            "Civil Engineer",
            "Chemical Engineer",
            "Systems Engineer",
            "Project Engineer"
        ],
        "skills_gained": [
            "Mathematical modeling",
            "System design",
            "Problem-solving",
            "CAD and simulation",
            "Project management",
            "Technical communication"
        ]
    }
}