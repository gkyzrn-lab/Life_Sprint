"""
Mini-games for course learning - makes course content interactive and engaging.
Each game teaches course concepts while providing points/rewards.

Focus: Business Administration (BA) major courses
"""

from __future__ import annotations
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from enum import Enum


class GameType(str, Enum):
    """Types of learning games available"""
    SCENARIO_DECISION = "scenario_decision"      # Choose best business decision
    ACCOUNTING_BALANCE = "accounting_balance"    # Balance sheet puzzle
    MARKET_SIM = "market_sim"                    # Supply/demand simulation
    TEAM_BUILDER = "team_builder"                # Build effective teams
    CASE_STUDY = "case_study"                    # Analyze business case
    BUDGET_CHALLENGE = "budget_challenge"        # Allocate budget wisely
    NEGOTIATION = "negotiation"                  # Practice negotiation
    MARKETING_CAMPAIGN = "marketing_campaign"    # Create marketing strategy


class GameQuestion(BaseModel):
    """A single question/prompt in a mini-game"""
    id: str
    prompt: str
    options: List[str]
    correct_option_index: int
    explanation: str
    learning_point: str  # Key concept being taught
    difficulty: int = Field(default=1, ge=1, le=5)


class MiniGame(BaseModel):
    """A complete mini-game for a course topic"""
    id: str
    course_id: str
    topic: str
    game_type: GameType
    title: str
    description: str
    questions: List[GameQuestion]
    points_per_correct: int = 10
    points_per_incorrect: int = -2
    min_passing_score: float = 70.0  # percentage
    estimated_duration_minutes: int


class GameResult(BaseModel):
    """Result of playing a mini-game"""
    game_id: str
    course_id: str
    score_percent: float
    points_earned: int
    passed: bool
    time_spent_minutes: int
    feedback: str
    key_learnings: List[str]


# ============================================
# BA COURSE GAMES
# ============================================

BA_COURSE_GAMES: Dict[str, List[MiniGame]] = {
    # SEMESTER 1 COURSES
    "ba101": [  # Intro Business
        MiniGame(
            id="ba101_startup_game",
            course_id="ba101",
            topic="Business Types & Structure",
            game_type=GameType.SCENARIO_DECISION,
            title="Startup Structure Challenge",
            description="You're launching a new tech company. Choose the right business structure based on scenarios.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Your startup has 2 founders investing equally with shared liability concerns. What structure minimizes personal liability?",
                    options=["Sole Proprietorship", "Partnership", "LLC", "Franchise"],
                    correct_option_index=2,
                    explanation="An LLC (Limited Liability Company) protects personal assets while allowing shared ownership.",
                    learning_point="Business structures and liability protection",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="You want maximum profit retention but need to raise capital from investors. Best choice?",
                    options=["Sole Proprietorship", "C Corporation", "S Corporation", "Nonprofit"],
                    correct_option_index=1,
                    explanation="A C Corporation allows external investment while potentially offering corporate tax benefits.",
                    learning_point="Capital raising and business structures",
                    difficulty=3
                ),
                GameQuestion(
                    id="q3",
                    prompt="Your family restaurant operates with flexible structure and minimal paperwork. What are you likely running?",
                    options=["Corporation", "Sole Proprietorship", "Public Company", "Holding Company"],
                    correct_option_index=1,
                    explanation="A Sole Proprietorship is simple, flexible, and common for small family businesses.",
                    learning_point="Sole proprietorship advantages",
                    difficulty=1
                ),
            ],
            points_per_correct=15,
            estimated_duration_minutes=10
        ),
        MiniGame(
            id="ba101_stakeholder_game",
            course_id="ba101",
            topic="Stakeholders & Ethics",
            game_type=GameType.CASE_STUDY,
            title="Stakeholder Navigation",
            description="Navigate competing interests from employees, customers, shareholders, and community.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Your company discovers a cost-saving manufacturing process that pollutes the environment. Stakeholder impact?",
                    options=[
                        "Only shareholders care about profit",
                        "Community and environment are key stakeholders",
                        "Only employees matter",
                        "Customers don't care about ethics"
                    ],
                    correct_option_index=1,
                    explanation="Stakeholder theory recognizes that communities and environmental groups are legitimate stakeholders.",
                    learning_point="Stakeholder identification and responsibility",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="Which stakeholder group is typically MOST affected by a company's working conditions?",
                    options=["Shareholders", "Competitors", "Employees", "Government"],
                    correct_option_index=2,
                    explanation="Employees directly experience working conditions daily.",
                    learning_point="Employee stakeholder importance",
                    difficulty=1
                ),
            ],
            points_per_correct=12,
            estimated_duration_minutes=8
        )
    ],
    
    "ba102": [  # Accounting Principles
        MiniGame(
            id="ba102_balance_sheet",
            course_id="ba102",
            topic="Balance Sheet Fundamentals",
            game_type=GameType.ACCOUNTING_BALANCE,
            title="Balance Sheet Builder",
            description="Classify accounts and keep the fundamental equation (Assets = Liabilities + Equity) balanced.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Cash in the bank is classified as what?",
                    options=["Liability", "Asset", "Equity", "Expense"],
                    correct_option_index=1,
                    explanation="Cash is an asset—a resource the company owns.",
                    learning_point="Asset classification",
                    difficulty=1
                ),
                GameQuestion(
                    id="q2",
                    prompt="Bank loan borrowed to buy equipment is what?",
                    options=["Asset", "Equity", "Liability", "Revenue"],
                    correct_option_index=2,
                    explanation="A bank loan is money owed, so it's a liability.",
                    learning_point="Liability identification",
                    difficulty=1
                ),
                GameQuestion(
                    id="q3",
                    prompt="If Assets = $100K and Liabilities = $60K, what is Equity?",
                    options=["$40K", "$160K", "$60K", "$100K"],
                    correct_option_index=0,
                    explanation="Equity = Assets - Liabilities = $100K - $60K = $40K",
                    learning_point="Balance sheet equation",
                    difficulty=2
                ),
            ],
            points_per_correct=10,
            estimated_duration_minutes=12
        ),
        MiniGame(
            id="ba102_journal_entry",
            course_id="ba102",
            topic="Journal Entries & Debits/Credits",
            game_type=GameType.SCENARIO_DECISION,
            title="Transaction Recording Game",
            description="Record business transactions correctly using debits and credits.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Company receives $5,000 cash from a customer. What accounts are affected?",
                    options=[
                        "Debit: Accounts Receivable, Credit: Cash",
                        "Debit: Cash, Credit: Revenue",
                        "Debit: Expense, Credit: Cash",
                        "Debit: Asset, Credit: Liability"
                    ],
                    correct_option_index=1,
                    explanation="Cash increases (debit asset), Revenue increases (credit revenue).",
                    learning_point="Transaction recording and revenue recognition",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="Company pays $2,000 rent for the month. How to record?",
                    options=[
                        "Debit: Rent Expense, Credit: Cash",
                        "Debit: Cash, Credit: Rent Payable",
                        "Debit: Asset, Credit: Asset",
                        "Debit: Revenue, Credit: Expense"
                    ],
                    correct_option_index=0,
                    explanation="Expenses increase with debits; cash (asset) decreases with credits.",
                    learning_point="Expense recognition",
                    difficulty=2
                ),
            ],
            points_per_correct=12,
            estimated_duration_minutes=10
        )
    ],
    
    "econ101": [  # Microeconomics
        MiniGame(
            id="econ101_supply_demand",
            course_id="econ101",
            topic="Supply & Demand",
            game_type=GameType.MARKET_SIM,
            title="Market Equilibrium Simulator",
            description="Observe how supply and demand curves shift with market changes.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="A new competitor enters the market selling similar products cheaper. What happens to demand for your product?",
                    options=[
                        "Demand increases",
                        "Demand decreases",
                        "Supply changes",
                        "Price stays the same"
                    ],
                    correct_option_index=1,
                    explanation="New competition at lower prices shifts demand away from your product.",
                    learning_point="Competitive dynamics and demand shifts",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="A natural disaster disrupts production of a commodity. What happens to price?",
                    options=[
                        "Price decreases (less supply)",
                        "Price increases (supply shock)",
                        "Price stays stable",
                        "Demand increases"
                    ],
                    correct_option_index=1,
                    explanation="Supply disruption causes supply to shift left, increasing price.",
                    learning_point="Supply shocks and price mechanism",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="Consumer incomes increase. What happens to demand for normal goods?",
                    options=[
                        "Demand decreases",
                        "Demand increases",
                        "Supply increases",
                        "No change"
                    ],
                    correct_option_index=1,
                    explanation="Higher incomes increase purchasing power and demand for normal goods.",
                    learning_point="Income effects on demand",
                    difficulty=2
                ),
            ],
            points_per_correct=11,
            estimated_duration_minutes=12
        )
    ],

    # SEMESTER 2 COURSES
    "ba201": [  # Business Communication
        MiniGame(
            id="ba201_email_game",
            course_id="ba201",
            topic="Professional Written Communication",
            game_type=GameType.SCENARIO_DECISION,
            title="Email Etiquette Challenge",
            description="Choose the most professional and effective email response to various business scenarios.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Your boss sends you a critical email about a missed deadline. What's your best response?",
                    options=[
                        "Reply defending why it wasn't your fault",
                        "Acknowledge the mistake, explain briefly, propose a solution",
                        "Ignore it and hope they forget",
                        "Reply with excuses about being busy"
                    ],
                    correct_option_index=1,
                    explanation="Professional communication takes accountability and proposes forward-looking solutions.",
                    learning_point="Professional accountability in communication",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="You're requesting time off from work. What tone is most appropriate?",
                    options=[
                        "Demanding and entitled",
                        "Casual and joking",
                        "Polite, specific, and professional",
                        "Vague and unclear"
                    ],
                    correct_option_index=2,
                    explanation="Professional requests are clear, courteous, and specific about dates and reasons.",
                    learning_point="Professional tone and clarity",
                    difficulty=1
                ),
            ],
            points_per_correct=10,
            estimated_duration_minutes=8
        )
    ],
    
    "ba202": [  # Financial Accounting
        MiniGame(
            id="ba202_income_statement",
            course_id="ba202",
            topic="Income Statement Analysis",
            game_type=GameType.SCENARIO_DECISION,
            title="Profit & Loss Detective",
            description="Analyze income statements to identify profitability trends and issues.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Company A has Revenue=$100K, COGS=$60K, Operating Expenses=$20K. What is Net Income?",
                    options=["$80K", "$40K", "$20K", "$60K"],
                    correct_option_index=2,
                    explanation="Net Income = Revenue - COGS - Operating Expenses = $100K - $60K - $20K = $20K",
                    learning_point="Income statement calculation",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="If a company's COGS increased but revenue stayed flat, what effect?",
                    options=[
                        "Profit increases",
                        "Profit decreases",
                        "No effect on profit",
                        "Revenue increases"
                    ],
                    correct_option_index=1,
                    explanation="Higher COGS with the same revenue reduces gross profit and net income.",
                    learning_point="Cost pressure on profitability",
                    difficulty=1
                ),
            ],
            points_per_correct=12,
            estimated_duration_minutes=10
        )
    ],

    # SEMESTER 3 COURSES
    "ba301": [  # Management Principles
        MiniGame(
            id="ba301_leadership_game",
            course_id="ba301",
            topic="Leadership & Decision Making",
            game_type=GameType.TEAM_BUILDER,
            title="Team Leadership Challenge",
            description="Make management decisions affecting team motivation, productivity, and morale.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Your team morale is low after a project failure. Best first step?",
                    options=[
                        "Immediately assign new tasks to move on",
                        "Listen to understand root causes and show support",
                        "Blame underperformers publicly",
                        "Ignore the issue and focus on the next project"
                    ],
                    correct_option_index=1,
                    explanation="Effective leaders show empathy, understand issues, and rebuild trust before moving forward.",
                    learning_point="Emotional intelligence in leadership",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="You notice a high performer is disengaged. What's your approach?",
                    options=[
                        "Assume they're looking for a new job and do nothing",
                        "Have a private conversation to understand their concerns",
                        "Give them more work to re-engage them",
                        "Wait to see if they quit"
                    ],
                    correct_option_index=1,
                    explanation="Proactive one-on-one communication helps retain talent and address issues early.",
                    learning_point="Talent retention and engagement",
                    difficulty=2
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=12
        )
    ],
    
    "ba302": [  # Marketing Fundamentals
        MiniGame(
            id="ba302_marketing_campaign",
            course_id="ba302",
            topic="Marketing Strategy & Segmentation",
            game_type=GameType.MARKETING_CAMPAIGN,
            title="Target Market Strategy",
            description="Design a marketing campaign targeting the right audience with the right message.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Luxury watch company: best target audience segment?",
                    options=[
                        "College students with limited budgets",
                        "High-income professionals aged 35-60",
                        "Teenagers interested in fashion",
                        "Retirees on fixed incomes"
                    ],
                    correct_option_index=1,
                    explanation="Luxury products target affluent demographics with disposable income.",
                    learning_point="Market segmentation and targeting",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="Which marketing channel reaches Gen Z most effectively?",
                    options=[
                        "Traditional TV commercials",
                        "Newspaper ads",
                        "Social media and influencers",
                        "Radio spots"
                    ],
                    correct_option_index=2,
                    explanation="Gen Z primarily engages with digital content, social platforms, and influencer marketing.",
                    learning_point="Channel selection for target demographics",
                    difficulty=2
                ),
            ],
            points_per_correct=11,
            estimated_duration_minutes=10
        )
    ],

    # SEMESTER 4 COURSES
    "ba401": [  # Corporate Finance
        MiniGame(
            id="ba401_capital_budget",
            course_id="ba401",
            topic="Capital Budgeting & Investment Decisions",
            game_type=GameType.BUDGET_CHALLENGE,
            title="Capital Investment Simulator",
            description="Evaluate projects using NPV, ROI, and payback period. Make smart capital allocation decisions.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Project A: Cost $100K, returns $30K/year for 4 years. Project B: Cost $100K, returns $35K/year for 3 years. Which is better using payback period?",
                    options=[
                        "Project A (4 years vs 3 years)",
                        "Project B (returns faster)",
                        "Both equally good",
                        "Neither is viable"
                    ],
                    correct_option_index=1,
                    explanation="Project B pays back in ~2.9 years vs Project A in ~3.3 years. Faster payback reduces risk.",
                    learning_point="Payback period evaluation",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="A project has a negative NPV. Should you invest?",
                    options=[
                        "Yes, NPV doesn't matter",
                        "No, negative NPV destroys shareholder value",
                        "Always invest in projects",
                        "Only if it creates jobs"
                    ],
                    correct_option_index=1,
                    explanation="Negative NPV means the project returns less than the cost of capital. It destroys value.",
                    learning_point="NPV decision rule",
                    difficulty=3
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=13
        )
    ],
    
    "ba402": [  # Strategic Management
        MiniGame(
            id="ba402_strategy_game",
            course_id="ba402",
            topic="Strategic Analysis & Competitive Advantage",
            game_type=GameType.CASE_STUDY,
            title="Competitive Strategy Challenge",
            description="Analyze competitive position and develop strategies to sustain advantage.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Company has high-quality products but competitors are cheaper. Viable strategy?",
                    options=[
                        "Lower quality to cut costs",
                        "Build brand loyalty emphasizing quality/service",
                        "Exit the market",
                        "Copy competitor pricing exactly"
                    ],
                    correct_option_index=1,
                    explanation="Differentiation on quality/premium positioning is a sustainable strategy against price competitors.",
                    learning_point="Differentiation strategy",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="Your competitive advantage relies on a patent expiring in 2 years. Best action?",
                    options=[
                        "Do nothing and hope for the best",
                        "Start innovating now to maintain leadership after expiration",
                        "Raise prices immediately",
                        "Merge with competitors"
                    ],
                    correct_option_index=1,
                    explanation="Proactive innovation and building brand loyalty sustain advantages beyond patent protection.",
                    learning_point="Sustainable competitive advantage",
                    difficulty=3
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=12
        )
    ]
}


def get_course_games(course_id: str) -> List[MiniGame]:
    """Get all mini-games for a specific course"""
    return BA_COURSE_GAMES.get(course_id, [])


def get_game_by_id(game_id: str) -> Optional[MiniGame]:
    """Get a specific game by ID"""
    for games_list in BA_COURSE_GAMES.values():
        for game in games_list:
            if game.id == game_id:
                return game
    return None


def calculate_game_score(correct_answers: int, total_questions: int, game: MiniGame) -> Dict[str, Any]:
    """Calculate score and points for a completed game"""
    score_percent = (correct_answers / total_questions * 100) if total_questions > 0 else 0
    points_earned = (correct_answers * game.points_per_correct) + ((total_questions - correct_answers) * game.points_per_incorrect)
    points_earned = max(0, points_earned)  # Don't go below 0
    passed = score_percent >= game.min_passing_score
    
    return {
        "score_percent": round(score_percent, 1),
        "points_earned": points_earned,
        "passed": passed,
        "correct_answers": correct_answers,
        "total_questions": total_questions
    }
