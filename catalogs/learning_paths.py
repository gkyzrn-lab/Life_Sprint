# Personalized learning paths and specialization tracks
# Students can customize their education based on career goals and interests

from typing import Dict, List
from pydantic import BaseModel


class LearningPath(BaseModel):
    """Model for a personalized learning path"""
    path_id: str
    name: str
    description: str
    major_id: str
    career_focus: str
    recommended_electives: List[str]
    recommended_activities: List[str]
    skills_developed: List[str]
    typical_careers: List[str]


# Specialization tracks within majors
LEARNING_PATHS = {
    # Computer Science Paths
    "cs_fullstack": {
        "path_id": "cs_fullstack",
        "name": "Full-Stack Web Development",
        "description": "Focus on building complete web applications from frontend to backend to database.",
        "major_id": "cs",
        "career_focus": "Web Development",
        "recommended_electives": [
            "Web Development Fundamentals",
            "Frontend Frameworks (React/Vue)",
            "Backend Development with Node.js",
            "Database Design & Management",
            "Cloud Computing & AWS",
            "Mobile Development"
        ],
        "recommended_activities": [
            "Join hackathons - build projects in 24-48 hours",
            "Contribute to open-source projects on GitHub",
            "Build a personal portfolio website",
            "Freelance on Upwork or Fiverr for experience",
            "Join the Web Development Club"
        ],
        "skills_developed": [
            "HTML/CSS/JavaScript",
            "React or Vue.js",
            "Node.js and Express",
            "SQL and NoSQL databases",
            "RESTful API design",
            "Git and version control",
            "Cloud deployment (AWS/Azure)"
        ],
        "typical_careers": [
            "Full-Stack Developer",
            "Frontend Engineer",
            "Backend Engineer",
            "Web Application Developer",
            "Software Engineer"
        ]
    },
    "cs_ml_ai": {
        "path_id": "cs_ml_ai",
        "name": "Machine Learning & Artificial Intelligence",
        "description": "Specialize in training machines to learn from data and make intelligent decisions.",
        "major_id": "cs",
        "career_focus": "AI/ML Engineering",
        "recommended_electives": [
            "Machine Learning",
            "Deep Learning & Neural Networks",
            "Natural Language Processing",
            "Computer Vision",
            "Big Data Analytics",
            "AI Ethics"
        ],
        "recommended_activities": [
            "Kaggle competitions - practice ML on real datasets",
            "Join AI research lab",
            "Build ML projects for portfolio",
            "Take online courses (fast.ai, Coursera)",
            "Attend AI conferences"
        ],
        "skills_developed": [
            "Python (NumPy, Pandas, Scikit-learn)",
            "TensorFlow or PyTorch",
            "Neural network architectures",
            "Data preprocessing and feature engineering",
            "Model evaluation and tuning",
            "Mathematics for ML (linear algebra, calculus)"
        ],
        "typical_careers": [
            "Machine Learning Engineer",
            "Data Scientist",
            "AI Research Scientist",
            "Computer Vision Engineer",
            "NLP Engineer"
        ]
    },
    "cs_security": {
        "path_id": "cs_security",
        "name": "Cybersecurity & Ethical Hacking",
        "description": "Protect systems from threats and learn to think like both defender and attacker.",
        "major_id": "cs",
        "career_focus": "Cybersecurity",
        "recommended_electives": [
            "Network Security",
            "Cryptography",
            "Ethical Hacking & Penetration Testing",
            "Secure Coding Practices",
            "Digital Forensics",
            "Security Policy & Management"
        ],
        "recommended_activities": [
            "HackTheBox and TryHackMe challenges",
            "Participate in CTF competitions",
            "Get security certifications (CEH, Security+)",
            "Join Cybersecurity Club",
            "Attend DefCon or similar conferences"
        ],
        "skills_developed": [
            "Network protocols and vulnerabilities",
            "Penetration testing tools",
            "Cryptographic algorithms",
            "Security assessment",
            "Incident response",
            "Linux system administration"
        ],
        "typical_careers": [
            "Cybersecurity Analyst",
            "Penetration Tester",
            "Security Engineer",
            "Security Consultant",
            "SOC Analyst"
        ]
    },
    
    # Business Paths
    "business_finance": {
        "path_id": "business_finance",
        "name": "Corporate Finance & Investment",
        "description": "Master financial analysis, investment strategies, and corporate financial management.",
        "major_id": "business",
        "career_focus": "Finance",
        "recommended_electives": [
            "Investment Analysis",
            "Financial Modeling",
            "Corporate Valuation",
            "Portfolio Management",
            "Derivatives & Options",
            "Mergers & Acquisitions"
        ],
        "recommended_activities": [
            "Join Investment Club",
            "Compete in stock market simulations",
            "Get Bloomberg Terminal certification",
            "Intern at investment bank or firm",
            "Study for CFA Level 1"
        ],
        "skills_developed": [
            "Financial modeling in Excel",
            "Valuation techniques (DCF, comparables)",
            "Financial statement analysis",
            "Risk assessment",
            "Investment portfolio management",
            "Bloomberg Terminal proficiency"
        ],
        "typical_careers": [
            "Financial Analyst",
            "Investment Banker",
            "Portfolio Manager",
            "Corporate Finance Analyst",
            "Private Equity Associate"
        ]
    },
    "business_marketing": {
        "path_id": "business_marketing",
        "name": "Digital Marketing & Brand Strategy",
        "description": "Build brands, engage customers, and drive growth through modern marketing strategies.",
        "major_id": "business",
        "career_focus": "Marketing",
        "recommended_electives": [
            "Digital Marketing Strategy",
            "Social Media Marketing",
            "Content Marketing",
            "Consumer Behavior",
            "Brand Management",
            "Marketing Analytics"
        ],
        "recommended_activities": [
            "Manage social media for student org",
            "Run Google/Facebook ad campaigns",
            "Get Google Analytics certification",
            "Join American Marketing Association",
            "Build personal brand on LinkedIn"
        ],
        "skills_developed": [
            "Social media marketing",
            "SEO and SEM",
            "Content creation",
            "Marketing analytics (Google Analytics)",
            "Ad campaign management",
            "Brand strategy",
            "A/B testing"
        ],
        "typical_careers": [
            "Digital Marketing Manager",
            "Brand Manager",
            "Marketing Analyst",
            "Social Media Manager",
            "Content Marketing Manager"
        ]
    },
    "business_consulting": {
        "path_id": "business_consulting",
        "name": "Management Consulting",
        "description": "Solve complex business problems and advise companies on strategy and operations.",
        "major_id": "business",
        "career_focus": "Consulting",
        "recommended_electives": [
            "Strategic Management",
            "Business Analytics",
            "Change Management",
            "Project Management",
            "Organizational Development",
            "Case Study Analysis"
        ],
        "recommended_activities": [
            "Join consulting club",
            "Compete in case competitions",
            "Work on pro bono consulting projects",
            "Practice case interviews intensively",
            "Network at consulting firm events"
        ],
        "skills_developed": [
            "Problem-solving frameworks",
            "Case interview skills",
            "Data analysis and Excel",
            "PowerPoint presentations",
            "Business strategy",
            "Project management",
            "Client communication"
        ],
        "typical_careers": [
            "Management Consultant",
            "Strategy Consultant",
            "Operations Consultant",
            "Business Analyst",
            "Project Manager"
        ]
    },
    
    # Engineering Paths
    "eng_software": {
        "path_id": "eng_software",
        "name": "Software Engineering",
        "description": "Apply engineering principles to software design and development.",
        "major_id": "engineering",
        "career_focus": "Software",
        "recommended_electives": [
            "Software Design Patterns",
            "Agile Development",
            "DevOps & CI/CD",
            "Cloud Architecture",
            "Microservices",
            "Software Testing"
        ],
        "recommended_activities": [
            "Contribute to open source",
            "Build side projects",
            "Attend tech meetups",
            "Participate in hackathons",
            "Intern at tech companies"
        ],
        "skills_developed": [
            "Multiple programming languages",
            "Software architecture",
            "Testing and QA",
            "DevOps practices",
            "Agile methodologies",
            "System design"
        ],
        "typical_careers": [
            "Software Engineer",
            "DevOps Engineer",
            "Solutions Architect",
            "Technical Lead",
            "Engineering Manager"
        ]
    },
    "eng_mechanical": {
        "path_id": "eng_mechanical",
        "name": "Mechanical Engineering Design",
        "description": "Design and build physical systems, machines, and mechanical products.",
        "major_id": "engineering",
        "career_focus": "Mechanical",
        "recommended_electives": [
            "Mechanical Design",
            "Robotics",
            "Manufacturing Processes",
            "Finite Element Analysis",
            "Heat Transfer",
            "Fluid Mechanics"
        ],
        "recommended_activities": [
            "Join Formula SAE or robotics team",
            "Work in machine shop",
            "CAD certification (SolidWorks)",
            "Internship at manufacturing company",
            "Build personal engineering projects"
        ],
        "skills_developed": [
            "CAD (SolidWorks, AutoCAD)",
            "Mechanical design",
            "Manufacturing knowledge",
            "FEA simulation",
            "Prototyping",
            "System integration"
        ],
        "typical_careers": [
            "Mechanical Engineer",
            "Product Design Engineer",
            "Manufacturing Engineer",
            "Robotics Engineer",
            "R&D Engineer"
        ]
    },
    "eng_renewable": {
        "path_id": "eng_renewable",
        "name": "Renewable Energy & Sustainability",
        "description": "Engineer solutions for clean energy and environmental sustainability.",
        "major_id": "engineering",
        "career_focus": "Sustainability",
        "recommended_electives": [
            "Solar Energy Systems",
            "Wind Energy",
            "Energy Storage",
            "Sustainable Design",
            "Environmental Engineering",
            "Green Building"
        ],
        "recommended_activities": [
            "Join sustainability club",
            "Solar Decathlon competition",
            "Intern at renewable energy company",
            "LEED certification",
            "Research in clean energy lab"
        ],
        "skills_developed": [
            "Renewable energy systems",
            "Sustainability analysis",
            "Energy modeling",
            "Environmental impact assessment",
            "Green building design",
            "Policy and regulations"
        ],
        "typical_careers": [
            "Renewable Energy Engineer",
            "Sustainability Consultant",
            "Energy Analyst",
            "Environmental Engineer",
            "Green Building Consultant"
        ]
    }
}


# Career interest assessment questions
CAREER_INTERESTS = {
    "questions": [
        {
            "id": 1,
            "question": "What type of work environment appeals to you?",
            "options": {
                "A": "Fast-paced tech startup",
                "B": "Corporate office environment",
                "C": "Lab or manufacturing facility",
                "D": "Remote/flexible work"
            }
        },
        {
            "id": 2,
            "question": "What motivates you most in a career?",
            "options": {
                "A": "Building innovative products",
                "B": "Financial success and stability",
                "C": "Solving technical challenges",
                "D": "Making societal impact"
            }
        },
        {
            "id": 3,
            "question": "What's your ideal work style?",
            "options": {
                "A": "Independent work on projects",
                "B": "Collaborative team environment",
                "C": "Mix of both",
                "D": "Leading and managing others"
            }
        },
        {
            "id": 4,
            "question": "Which skill set interests you most?",
            "options": {
                "A": "Creative and design",
                "B": "Analytical and data-driven",
                "C": "Technical and hands-on",
                "D": "Strategic and big-picture thinking"
            }
        },
        {
            "id": 5,
            "question": "What industry excites you?",
            "options": {
                "A": "Technology and software",
                "B": "Finance and business",
                "C": "Engineering and manufacturing",
                "D": "Healthcare or education"
            }
        }
    ],
    "path_mapping": {
        "tech_focused": ["cs_fullstack", "cs_ml_ai", "cs_security", "eng_software"],
        "business_focused": ["business_finance", "business_marketing", "business_consulting"],
        "hands_on_focused": ["eng_mechanical", "eng_renewable"],
        "analytical_focused": ["cs_ml_ai", "business_finance", "eng_software"]
    }
}


# Personalized recommendations based on player attributes
def recommend_learning_path(major_id: str, interests: List[str], skills: List[str]) -> List[str]:
    """
    Recommend learning paths based on major, interests, and skills.
    This is a simple algorithm - could be enhanced with ML.
    """
    recommendations = []
    
    # Filter paths by major
    major_paths = {k: v for k, v in LEARNING_PATHS.items() if v["major_id"] == major_id}
    
    # Simple scoring based on interest and skill overlap
    for path_id, path_data in major_paths.items():
        score = 0
        
        # Check interest overlap
        for interest in interests:
            if interest.lower() in path_data["description"].lower():
                score += 2
            if interest.lower() in path_data["career_focus"].lower():
                score += 3
        
        # Check skill overlap
        for skill in skills:
            if any(skill.lower() in dev_skill.lower() for dev_skill in path_data["skills_developed"]):
                score += 1
        
        recommendations.append({
            "path_id": path_id,
            "path_name": path_data["name"],
            "score": score,
            "match_percentage": min(100, score * 10)  # Simple conversion to percentage
        })
    
    # Sort by score and return top 3
    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return recommendations[:3]
