"""
Enhanced BA Course Topics and Learning Materials
Provides detailed, engaging topic descriptions for Business Administration courses.
Focuses on practical, real-world applications.
"""

from typing import Dict, List

BA_COURSE_TOPICS: Dict[str, Dict[str, Any]] = {
    # SEMESTER 1
    "ba101": {
        "title": "Intro Business",
        "description": "Foundations of business including organizational structures, functions, and management principles.",
        "key_topics": [
            {
                "name": "Business Types & Structures",
                "description": "Sole proprietorships, partnerships, LLCs, corporations, and franchises.",
                "real_world": "Why does Jeff Bezos's Amazon choose to be incorporated?"
            },
            {
                "name": "Business Functions",
                "description": "Finance, Marketing, Operations, Human Resources, and their interdependencies.",
                "real_world": "How do HR and Marketing teams collaborate in hiring?"
            },
            {
                "name": "Stakeholders & Ethics",
                "description": "Identifying stakeholders, understanding competing interests, ethical decision-making.",
                "real_world": "Should a profitable company shut down an unsafe factory?"
            },
            {
                "name": "Business Environment",
                "description": "External factors: economic, social, technological, legal.",
                "real_world": "How did COVID-19 force businesses to pivot digitally?"
            },
            {
                "name": "Entrepreneurship Basics",
                "description": "Starting a business, identifying opportunities, feasibility analysis.",
                "real_world": "How do startup founders validate their business ideas?"
            }
        ]
    },
    "ba102": {
        "title": "Accounting Principles",
        "description": "Fundamentals of financial accounting, the language of business.",
        "key_topics": [
            {
                "name": "The Accounting Equation",
                "description": "Assets = Liabilities + Equity. The foundation of accounting.",
                "real_world": "When a small business borrows $50K, how does the balance sheet change?"
            },
            {
                "name": "Double-Entry Accounting",
                "description": "Every transaction affects at least two accounts (debits and credits).",
                "real_world": "If you pay rent with cash, which accounts change?"
            },
            {
                "name": "Journal Entries & Posting",
                "description": "Recording transactions in journals and posting to ledgers.",
                "real_world": "How does a transaction flow from a receipt to the financial statements?"
            },
            {
                "name": "Financial Statements",
                "description": "Income Statement, Balance Sheet, and Cash Flow Statement.",
                "real_world": "Why would a profitable company still run out of cash?"
            },
            {
                "name": "Accrual vs. Cash Accounting",
                "description": "Timing differences in recognizing revenues and expenses.",
                "real_world": "Should you recognize revenue when you invoice or when you're paid?"
            }
        ]
    },
    "econ101": {
        "title": "Microeconomics",
        "description": "How individual markets, consumers, and firms make economic decisions.",
        "key_topics": [
            {
                "name": "Supply & Demand",
                "description": "How prices are determined by market forces of supply and demand.",
                "real_world": "Why did concert ticket prices skyrocket after Taylor Swift's announcement?"
            },
            {
                "name": "Price Elasticity",
                "description": "How sensitive demand is to price changes.",
                "real_world": "When gas prices surge, why don't people stop driving to work immediately?"
            },
            {
                "name": "Consumer Behavior",
                "description": "How consumers make purchasing decisions and budget constraints.",
                "real_world": "Why do you buy premium coffee when cheaper alternatives exist?"
            },
            {
                "name": "Production & Costs",
                "description": "Fixed costs, variable costs, and economies of scale.",
                "real_world": "Why is manufacturing at scale cheaper per unit than small batches?"
            },
            {
                "name": "Market Structures",
                "description": "Perfect competition, monopolistic competition, oligopoly, monopoly.",
                "real_world": "How is Apple's market different from farmers in a competitive market?"
            }
        ]
    },
    # SEMESTER 2
    "ba201": {
        "title": "Business Communication",
        "description": "Professional written and verbal communication for business success.",
        "key_topics": [
            {
                "name": "Professional Writing",
                "description": "Emails, reports, memos, and business correspondence.",
                "real_world": "How do you professionally email your boss about a serious mistake?"
            },
            {
                "name": "Persuasive Communication",
                "description": "Influencing others through clear, compelling messages.",
                "real_world": "How do you pitch your business idea to investors?"
            },
            {
                "name": "Presentations & Public Speaking",
                "description": "Structuring talks, managing anxiety, engaging audiences.",
                "real_world": "How do CEOs deliver quarterly earnings presentations?"
            },
            {
                "name": "Listening & Interpersonal Skills",
                "description": "Active listening, feedback, and conflict resolution.",
                "real_world": "Why do good managers spend more time listening than talking?"
            },
            {
                "name": "Team Communication",
                "description": "Cross-functional collaboration and meeting management.",
                "real_world": "How do remote teams communicate effectively across time zones?"
            }
        ]
    },
    "econ102": {
        "title": "Macroeconomics",
        "description": "National and global economic systems, growth, and policy.",
        "key_topics": [
            {
                "name": "GDP & Economic Growth",
                "description": "Measuring national output and standards of living.",
                "real_world": "When GDP falls, what happens to job markets?"
            },
            {
                "name": "Inflation & Deflation",
                "description": "Rising/falling price levels and their impacts.",
                "real_world": "Why does 'too much inflation' harm both savers and borrowers?"
            },
            {
                "name": "Unemployment",
                "description": "Types of unemployment and labor market dynamics.",
                "real_world": "Why doesn't unemployment fall to zero even in strong economies?"
            },
            {
                "name": "Monetary Policy",
                "description": "How central banks (Fed) control money supply and interest rates.",
                "real_world": "How does raising interest rates reduce inflation?"
            },
            {
                "name": "Fiscal Policy",
                "description": "Government spending and taxation effects on the economy.",
                "real_world": "Why do governments increase spending during recessions?"
            }
        ]
    },
    "ba202": {
        "title": "Financial Accounting",
        "description": "Advanced accounting covering financial reporting standards and analysis.",
        "key_topics": [
            {
                "name": "Income Statement Analysis",
                "description": "Profitability metrics and trend analysis.",
                "real_world": "Why is margin declining even when revenue is growing?"
            },
            {
                "name": "Balance Sheet Analysis",
                "description": "Asset quality, liability structure, and financial position.",
                "real_world": "What does a company's debt-to-equity ratio tell you?"
            },
            {
                "name": "Cash Flow Statement",
                "description": "Operating, investing, and financing cash flows.",
                "real_world": "Why can a profitable company run out of cash?"
            },
            {
                "name": "Ratio Analysis",
                "description": "Profitability, liquidity, efficiency, and solvency ratios.",
                "real_world": "How do investors use ratios to compare companies?"
            },
            {
                "name": "Accounting Standards",
                "description": "GAAP and IFRS compliance and regulatory requirements.",
                "real_world": "Why would a company report different earnings under GAAP vs IFRS?"
            }
        ]
    },
    # SEMESTER 3
    "ba301": {
        "title": "Management Principles",
        "description": "Planning, organizing, leading, and controlling organizational resources.",
        "key_topics": [
            {
                "name": "Planning & Strategy",
                "description": "Setting goals, developing strategies, and long-term planning.",
                "real_world": "How does a CEO set a 5-year strategic plan?"
            },
            {
                "name": "Organizational Structure",
                "description": "Hierarchies, flat organizations, and organizational design.",
                "real_world": "Why do tech startups have flat structures while governments are hierarchical?"
            },
            {
                "name": "Leadership Styles",
                "description": "Autocratic, democratic, and laissez-faire approaches.",
                "real_world": "Which leadership style works best for your team?"
            },
            {
                "name": "Motivation Theories",
                "description": "Maslow, Herzberg, McGregor, and modern motivation research.",
                "real_world": "Why do some employees work hard while others are disengaged?"
            },
            {
                "name": "Control & Performance",
                "description": "Setting standards, monitoring performance, and taking corrective action.",
                "real_world": "How do managers measure whether projects are on track?"
            }
        ]
    },
    "ba302": {
        "title": "Marketing Fundamentals",
        "description": "Understanding customers, creating value, and competitive positioning.",
        "key_topics": [
            {
                "name": "Market Segmentation",
                "description": "Dividing markets into distinct customer groups.",
                "real_world": "Should a car company market the same vehicle to young and old drivers?"
            },
            {
                "name": "Consumer Behavior",
                "description": "Psychological, social, and economic factors in purchasing decisions.",
                "real_world": "Why do people buy premium brands when budget alternatives exist?"
            },
            {
                "name": "The Marketing Mix",
                "description": "Product, Price, Place (Distribution), Promotion (4Ps).",
                "real_world": "Why does Starbucks charge $6 for coffee when a deli sells it for $2?"
            },
            {
                "name": "Branding & Positioning",
                "description": "Building brand equity and competitive differentiation.",
                "real_world": "What makes the Apple brand so valuable?"
            },
            {
                "name": "Digital Marketing",
                "description": "Online channels, social media, SEO, content marketing.",
                "real_world": "How do companies reach younger consumers on TikTok and Instagram?"
            }
        ]
    },
    "ba303": {
        "title": "Organizational Behavior",
        "description": "Understanding people, teams, and organizational dynamics.",
        "key_topics": [
            {
                "name": "Individual Behavior",
                "description": "Personality, perception, attitudes, and learning.",
                "real_world": "Why do two employees react differently to the same feedback?"
            },
            {
                "name": "Motivation & Job Satisfaction",
                "description": "What drives performance and engagement at work.",
                "real_world": "Why do raises sometimes fail to boost motivation?"
            },
            {
                "name": "Group Dynamics",
                "description": "Team formation, cohesion, conflict, and performance.",
                "real_world": "When does team diversity increase or decrease performance?"
            },
            {
                "name": "Communication Patterns",
                "description": "Formal and informal communication networks.",
                "real_world": "Why do rumors spread faster than official company announcements?"
            },
            {
                "name": "Organizational Culture",
                "description": "Values, norms, and shared beliefs shaping behavior.",
                "real_world": "Why is Google's culture different from traditional banks?"
            }
        ]
    },
    # SEMESTER 4
    "ba401": {
        "title": "Corporate Finance",
        "description": "Managing corporate resources for value creation and growth.",
        "key_topics": [
            {
                "name": "Time Value of Money",
                "description": "Present value, future value, and discounting.",
                "real_world": "Is $1,000 today worth more than $1,000 in 5 years?"
            },
            {
                "name": "Capital Budgeting",
                "description": "Evaluating long-term investments using NPV, IRR, payback period.",
                "real_world": "How do companies decide which factories or stores to build?"
            },
            {
                "name": "Financing Decisions",
                "description": "Debt vs. equity financing and optimal capital structure.",
                "real_world": "Should a company borrow or issue stock to fund expansion?"
            },
            {
                "name": "Valuation & M&A",
                "description": "Valuing firms and analyzing mergers and acquisitions.",
                "real_world": "Why did Elon Musk pay $44B for Twitter?"
            },
            {
                "name": "Working Capital Management",
                "description": "Managing cash, inventory, receivables, and payables.",
                "real_world": "Why do companies sometimes offer discounts for early payment?"
            }
        ]
    },
    "ba402": {
        "title": "Strategic Management",
        "description": "Competitive strategy, positioning, and long-term value creation.",
        "key_topics": [
            {
                "name": "Strategic Analysis",
                "description": "SWOT analysis, industry analysis, and competitive positioning.",
                "real_world": "How does Tesla position itself vs. traditional automakers?"
            },
            {
                "name": "Generic Strategies",
                "description": "Cost leadership, differentiation, and focus strategies.",
                "real_world": "Why is Walmart's strategy different from Luxury brands?"
            },
            {
                "name": "Competitive Advantage",
                "description": "Building sustainable advantages and barriers to entry.",
                "real_world": "Why can Netflix sustain advantage despite growing competition?"
            },
            {
                "name": "Growth Strategies",
                "description": "Market penetration, product development, diversification.",
                "real_world": "Should Apple expand into cars or focus on phones?"
            },
            {
                "name": "Innovation & Disruption",
                "description": "Disruptive innovation and adapting to market changes.",
                "real_world": "How did Netflix disrupt Blockbuster, then adapt to streaming threats?"
            }
        ]
    },
    "ba403": {
        "title": "Operations Management",
        "description": "Managing production and service delivery for efficiency and quality.",
        "key_topics": [
            {
                "name": "Process Design & Optimization",
                "description": "Lean, Six Sigma, and continuous improvement.",
                "real_world": "How does Toyota reduce waste while improving quality?"
            },
            {
                "name": "Supply Chain Management",
                "description": "Sourcing, procurement, and distribution.",
                "real_world": "Why did supply chain disruption cause $50 chips shortages?"
            },
            {
                "name": "Quality Management",
                "description": "Quality standards, control, and customer expectations.",
                "real_world": "How do car manufacturers reduce defects and warranty claims?"
            },
            {
                "name": "Inventory Management",
                "description": "Balancing stock levels with demand uncertainty.",
                "real_world": "Why do stores run out of PS5s while sitting on old products?"
            },
            {
                "name": "Project Management",
                "description": "Planning, scheduling, budgeting, and execution.",
                "real_world": "How do construction projects stay on budget and schedule?"
            }
        ]
    }
}


def get_ba_course_topics(course_id: str) -> Dict[str, Any]:
    """Get detailed topics for a BA course"""
    return BA_COURSE_TOPICS.get(course_id, {})


def format_course_topics_for_display(course_id: str) -> Dict[str, Any]:
    """
    Format course topics in an engaging, visually appealing way for the frontend.
    """
    course_data = get_ba_course_topics(course_id)
    
    if not course_data:
        return {
            "course_id": course_id,
            "found": False,
            "message": f"Topics not yet available for {course_id}"
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
                "icon": get_topic_icon(topic["name"])
            }
            for topic in course_data.get("key_topics", [])
        ],
        "learning_outcomes": [
            f"Master {topic['name']}" if i % 2 == 0 else f"Understand: {topic['description']}"
            for i, topic in enumerate(course_data.get("key_topics", []))
        ][:5]  # Top 5
    }


def get_topic_icon(topic_name: str) -> str:
    """Get an appropriate emoji icon for a topic"""
    icon_map = {
        "Business Types": "🏢",
        "Business Functions": "⚙️",
        "Stakeholders": "👥",
        "Ethics": "⚖️",
        "Environment": "🌍",
        "Entrepreneurship": "🚀",
        "Accounting": "📊",
        "Balance": "⚖️",
        "Double-Entry": "📝",
        "Journal": "📔",
        "Financial": "💰",
        "Accrual": "📈",
        "Supply": "📦",
        "Demand": "📈",
        "Elasticity": "🔄",
        "Consumer": "🛍️",
        "Production": "🏭",
        "Market": "📊",
        "Writing": "✍️",
        "Communication": "💬",
        "Persuasive": "🎯",
        "Presentations": "🎤",
        "Listening": "👂",
        "Team": "👥",
        "GDP": "📊",
        "Inflation": "📈",
        "Unemployment": "📉",
        "Monetary": "🏦",
        "Fiscal": "💵",
        "Income": "📊",
        "Cash Flow": "💹",
        "Ratio": "📐",
        "Standards": "📋",
        "Planning": "🎯",
        "Structure": "🏗️",
        "Leadership": "👑",
        "Motivation": "⚡",
        "Control": "📊",
        "Segmentation": "🎯",
        "Behavior": "🧠",
        "Marketing Mix": "🎨",
        "Branding": "🏷️",
        "Digital": "💻",
        "Individual": "👤",
        "Motivation": "⚡",
        "Group": "👥",
        "Communication": "💬",
        "Culture": "🌟",
        "Time Value": "⏰",
        "Capital": "💰",
        "Financing": "💳",
        "Valuation": "💎",
        "Working": "💼",
        "Strategic": "🎯",
        "Analysis": "🔍",
        "Generic": "🎯",
        "Competitive": "⚔️",
        "Growth": "📈",
        "Innovation": "💡",
        "Process": "⚙️",
        "Supply": "📦",
        "Quality": "✅",
        "Inventory": "📦",
        "Project": "📋",
    }
    
    # Find matching icon based on topic name
    for key, icon in icon_map.items():
        if key.lower() in topic_name.lower():
            return icon
    
    return "📚"  # Default book icon
