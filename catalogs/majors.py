# Comprehensive major catalog with realistic challenges and career paths
# Each major includes difficulty, job prospects, and real-world context

MAJORS = {
    # STEM Fields
    "cs": {
        "id": "cs",
        "name": "Computer Science",
        "description": (
            "Learn programming, data structures, algorithms, and software engineering. "
            "High earning potential but demanding coursework (advanced math, problem-solving). "
            "Leads to tech careers, startups, and innovation roles. Career challenges: "
            "staying current with rapidly evolving tech, intense competition, work-life balance in high-pressure roles."
        ),
        "difficulty": "high",
        "avg_gpa_required": 3.3,
        "job_outlook": "excellent",
        "typical_salaries": "$80K-$150K entry level",
        "tuition_multiplier": 1.15,
    },
    "mechanical_engineering": {
        "id": "mechanical_engineering",
        "name": "Mechanical Engineering",
        "description": (
            "Design and analyze mechanical systems, engines, robotics, and manufacturing processes. "
            "Heavy physics, thermodynamics, and CAD work. Versatile career paths in automotive, aerospace, energy. "
            "Career challenges: licensing requirements (PE exam), competitive field, project deadlines are unforgiving, "
            "some roles involve travel to manufacturing sites."
        ),
        "difficulty": "very_high",
        "avg_gpa_required": 3.4,
        "job_outlook": "strong",
        "typical_salaries": "$70K-$85K entry level",
        "tuition_multiplier": 1.20,
    },
    "electrical_engineering": {
        "id": "electrical_engineering",
        "name": "Electrical Engineering",
        "description": (
            "Design circuits, power systems, electronics, and telecommunications. "
            "Advanced math and physics with hands-on lab work. Critical for tech, energy, and hardware development. "
            "Career challenges: rapid technology changes require constant learning, licensing requirements (PE exam), "
            "highly technical problem-solving, safety-critical work (power systems)."
        ),
        "difficulty": "very_high",
        "avg_gpa_required": 3.5,
        "job_outlook": "excellent",
        "typical_salaries": "$75K-$95K entry level",
        "tuition_multiplier": 1.22,
    },
    "industrial_engineering": {
        "id": "industrial_engineering",
        "name": "Industrial Engineering",
        "description": (
            "Optimize complex processes, supply chains, and production systems. "
            "Combines engineering, business, and data analytics. Focus on efficiency and cost reduction. "
            "Career challenges: requires understanding both technical and business sides, "
            "project management pressure, balancing cost vs. quality, persuading teams to adopt changes."
        ),
        "difficulty": "high",
        "avg_gpa_required": 3.3,
        "job_outlook": "strong",
        "typical_salaries": "$68K-$80K entry level",
        "tuition_multiplier": 1.12,
    },
    "biology": {
        "id": "biology",
        "name": "Biology / Life Sciences",
        "description": (
            "Study living organisms, genetics, ecology, and cellular processes. "
            "Combines lab work with theory. Pathway to medicine, research, or environmental roles. "
            "Career challenges: pre-med competitiveness, lab funding volatility in research, "
            "need for advanced degrees (Masters, PhD) for many positions."
        ),
        "difficulty": "high",
        "avg_gpa_required": 3.4,
        "job_outlook": "moderate",
        "typical_salaries": "$40K-$70K entry level (Research/Lab Tech)",
        "tuition_multiplier": 1.10,
    },
    "mathematics": {
        "id": "mathematics",
        "name": "Mathematics",
        "description": (
            "Master abstract thinking, proofs, and quantitative reasoning. "
            "Applies to finance, cryptography, AI, and research. "
            "Career challenges: limited direct employment without specialization, "
            "often requires graduate study, competition with specialized STEM fields."
        ),
        "difficulty": "very_high",
        "avg_gpa_required": 3.5,
        "job_outlook": "moderate",
        "typical_salaries": "$55K-$95K (with specialization)",
        "tuition_multiplier": 1.0,
    },

    # Social Sciences
    "psychology": {
        "id": "psychology",
        "name": "Psychology",
        "description": (
            "Understand human behavior, cognition, and mental health. Mix of lab research, "
            "observation, and statistics. Diverse careers: clinical work, HR, UX research, counseling. "
            "Career challenges: licensing requirements (PhD/Masters for therapy), emotionally demanding work, "
            "heavy student debt for graduate programs, competitive psychology PhD programs."
        ),
        "difficulty": "medium",
        "avg_gpa_required": 3.2,
        "job_outlook": "moderate",
        "typical_salaries": "$45K-$65K entry level (without license)",
        "tuition_multiplier": 0.95,
    },
    "economics": {
        "id": "economics",
        "name": "Economics",
        "description": (
            "Analyze markets, policy, data, and human decision-making. Heavy on math and statistics. "
            "Leads to policy roles, finance, consulting, research. Real-world impact on society and markets. "
            "Career challenges: technical complexity, debates over methodology, need for strong math skills, "
            "policy roles require political navigation."
        ),
        "difficulty": "high",
        "avg_gpa_required": 3.3,
        "job_outlook": "strong",
        "typical_salaries": "$60K-$100K entry level",
        "tuition_multiplier": 1.05,
    },
    "politics": {
        "id": "politics",
        "name": "Political Science",
        "description": (
            "Study government systems, political theory, international relations, and policy. "
            "Leads to public service, law, diplomacy, advocacy, and research. "
            "Career challenges: salaries can be lower than private sector, requires networking and reputation building, "
            "political climate can affect job availability, work is often relationship-dependent."
        ),
        "difficulty": "medium",
        "avg_gpa_required": 3.1,
        "job_outlook": "moderate",
        "typical_salaries": "$45K-$75K entry level",
        "tuition_multiplier": 0.90,
    },
    "history": {
        "id": "history",
        "name": "History",
        "description": (
            "Research, analyze, and interpret past events and societies. Develops critical thinking, "
            "writing, and research skills. Careers: academia, museums, cultural institutions, law, journalism, policy. "
            "Career challenges: academia is highly competitive with limited positions, "
            "requires advanced degrees, low salaries in many history-specific roles, teaching positions declining."
        ),
        "difficulty": "medium",
        "avg_gpa_required": 3.0,
        "job_outlook": "limited",
        "typical_salaries": "$40K-$60K entry level",
        "tuition_multiplier": 0.85,
    },
    "sociology": {
        "id": "sociology",
        "name": "Sociology",
        "description": (
            "Study human groups, institutions, culture, and social change. "
            "Research-oriented with quantitative and qualitative methods. Applies to public policy, nonprofits, "
            "community work, and corporate research. Career challenges: research positions funding-dependent, "
            "field salaries moderate, requires building research portfolio."
        ),
        "difficulty": "medium",
        "avg_gpa_required": 3.0,
        "job_outlook": "moderate",
        "typical_salaries": "$45K-$65K entry level",
        "tuition_multiplier": 0.90,
    },

    # Business & Economics
    "ba": {
        "id": "ba",
        "name": "Business Administration",
        "description": (
            "Learn finance, operations, marketing, strategy, and organizational management. "
            "Versatile degree with many career paths. High earning potential with right specialization. "
            "Career challenges: competitive job market, constant need for additional certifications (MBA, CPA), "
            "work culture can be demanding, success depends heavily on internship network."
        ),
        "difficulty": "medium",
        "avg_gpa_required": 3.0,
        "job_outlook": "strong",
        "typical_salaries": "$50K-$85K entry level",
        "tuition_multiplier": 1.08,
    },
    "accounting": {
        "id": "accounting",
        "name": "Accounting",
        "description": (
            "Master financial systems, tax law, auditing, and business analytics. "
            "Clear career path: CPA license opens doors to high-paying roles. "
            "Career challenges: intense exam preparation (CPA exam requires months of study), "
            "busy seasons with long hours, requires continuing education, audit work can be repetitive."
        ),
        "difficulty": "high",
        "avg_gpa_required": 3.2,
        "job_outlook": "excellent",
        "typical_salaries": "$50K-$75K entry level (with CPA: $75K-$120K+)",
        "tuition_multiplier": 1.10,
    },
    "finance": {
        "id": "finance",
        "name": "Finance",
        "description": (
            "Study investments, corporate finance, financial markets, and risk management. "
            "Quantitative and fast-paced. High earning potential in investment/banking. "
            "Career challenges: market volatility affects job security, intense work hours in investment banking, "
            "high pressure decision-making with real money on the line, licensing requirements (Series 7, etc.)."
        ),
        "difficulty": "high",
        "avg_gpa_required": 3.3,
        "job_outlook": "strong",
        "typical_salaries": "$70K-$150K+ (varies widely by firm)",
        "tuition_multiplier": 1.12,
    },

    # Humanities
    "english": {
        "id": "english",
        "name": "English / Literature",
        "description": (
            "Develop deep reading, writing, and critical analysis skills. Careers in publishing, "
            "journalism, education, communications, law, and content creation. "
            "Career challenges: limited direct career paths, often requires advanced degree or portfolio building, "
            "low starting salaries, heavy competition for editorial/publishing roles, freelance instability."
        ),
        "difficulty": "medium",
        "avg_gpa_required": 3.1,
        "job_outlook": "limited",
        "typical_salaries": "$40K-$60K entry level",
        "tuition_multiplier": 0.85,
    },
    "communications": {
        "id": "communications",
        "name": "Communications / Media",
        "description": (
            "Learn journalism, digital media, PR, marketing communications. Practical, project-based learning. "
            "Leads to media, nonprofits, corporate communications, digital strategy. "
            "Career challenges: industry disruption (declining print journalism), requires strong portfolio, "
            "entry-level positions often unpaid internships, content creation is 24/7 in digital age."
        ),
        "difficulty": "medium",
        "avg_gpa_required": 3.0,
        "job_outlook": "changing",
        "typical_salaries": "$40K-$65K entry level",
        "tuition_multiplier": 0.92,
    },

    # Healthcare
    "nursing": {
        "id": "nursing",
        "name": "Nursing",
        "description": (
            "Rigorous clinical training to care for patients. Combines science, hands-on skills, and compassion. "
            "Strong job security and competitive salaries. Licenses required. "
            "Career challenges: physically and emotionally demanding work, night/weekend/holiday shifts, "
            "high stress environment (life-death decisions), patient safety responsibility, dealing with grief and illness daily."
        ),
        "difficulty": "high",
        "avg_gpa_required": 3.2,
        "job_outlook": "excellent",
        "typical_salaries": "$55K-$75K entry level (increases with experience/specialization)",
        "tuition_multiplier": 1.25,
    },

    # Interdisciplinary
    "data_science": {
        "id": "data_science",
        "name": "Data Science / Analytics",
        "description": (
            "Combine statistics, programming, and domain expertise to extract insights from data. "
            "High demand, lucrative, rapidly evolving field. Real-world impact on business decisions. "
            "Career challenges: rapidly changing tools and methods (constant learning required), "
            "need for both business and technical skills, results often contested by stakeholders, overwork culture in some firms."
        ),
        "difficulty": "very_high",
        "avg_gpa_required": 3.4,
        "job_outlook": "excellent",
        "typical_salaries": "$75K-$130K entry level",
        "tuition_multiplier": 1.18,
    },
}
