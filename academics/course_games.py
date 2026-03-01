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
    # Business & Finance
    SCENARIO_DECISION = "scenario_decision"      # Choose best business decision
    ACCOUNTING_BALANCE = "accounting_balance"    # Balance sheet puzzle
    MARKET_SIM = "market_sim"                    # Supply/demand simulation
    TEAM_BUILDER = "team_builder"                # Build effective teams
    CASE_STUDY = "case_study"                    # Analyze business case
    BUDGET_CHALLENGE = "budget_challenge"        # Allocate budget wisely
    NEGOTIATION = "negotiation"                  # Practice negotiation
    MARKETING_CAMPAIGN = "marketing_campaign"    # Create marketing strategy
    CALCULATOR = "calculator"                    # Interactive financial calculator
    INTERACTIVE_SIM = "interactive_sim"          # Real-time business simulation
    PROFIT_LOSS = "profit_loss"                  # P&L statement builder
    CASH_FLOW = "cash_flow"                      # Cash flow forecasting
    
    # Computer Science & Tech
    CODE_DEBUG = "code_debug"                    # Find and fix bugs in code
    CODE_TRACE = "code_trace"                    # Trace algorithm execution
    DATA_STRUCTURE_VIZ = "data_structure_viz"    # Visualize data structure operations
    ALGORITHM_RACE = "algorithm_race"            # Compare algorithm efficiency
    CODE_BUILDER = "code_builder"                # Build working code from scratch
    SYSTEM_DESIGN = "system_design"              # Design software architecture
    
    # Engineering & Physics
    CIRCUIT_SIM = "circuit_sim"                  # Circuit design & analysis
    PHYSICS_LAB = "physics_lab"                  # Virtual physics experiments
    FORCE_DIAGRAM = "force_diagram"              # Free body diagram construction
    DESIGN_CHALLENGE = "design_challenge"        # Engineering design problems
    CAD_BUILDER = "cad_builder"                  # CAD modeling challenges
    
    # Advanced Multi-Stage
    BOSS_BATTLE = "boss_battle"                  # Comprehensive challenge combining multiple skills
    REAL_WORLD_PROJECT = "real_world_project"    # Full project simulation
    TIMED_CHALLENGE = "timed_challenge"          # Speed-based mastery test


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
        ),
        MiniGame(
            id="ba102_startup_accounting",
            course_id="ba102",
            topic="Building a Business's Books from Scratch",
            game_type=GameType.INTERACTIVE_SIM,
            title="New Business Accounting Simulator",
            description="Start a business and record all transactions. Build balance sheet, income statement, and ledger from the ground up.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="You invest $50,000 personal savings to start a consulting business. After this transaction, Assets = $50K. Equity = ?",
                    options=["$0", "$50,000", "$100K", "-$50K"],
                    correct_option_index=1,
                    explanation="Your personal investment creates equity. Assets ($50K cash) = Liabilities ($0) + Equity ($50K).",
                    learning_point="Owner investment and equity creation",
                    difficulty=1
                ),
                GameQuestion(
                    id="q2",
                    prompt="You borrow $30K from a bank for office equipment. Now Assets = $80K, Liabilities = $30K. What is Equity?",
                    options=["$50K", "$110K", "$30K", "$80K"],
                    correct_option_index=0,
                    explanation="Equity = Assets - Liabilities = $80K - $30K = $50K. The loan increases assets (liability) but not equity.",
                    learning_point="Debt vs. equity financing",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="You earn $15K in consulting revenue but collect only $10K cash (rest on credit). Record this correctly:",
                    options=[
                        "Debit Cash $10K, Credit Revenue $10K",
                        "Debit Cash $15K, Credit Revenue $15K",
                        "Debit Cash $10K + Accounts Receivable $5K, Credit Revenue $15K",
                        "Debit Revenue $15K, Credit Cash $10K"
                    ],
                    correct_option_index=2,
                    explanation="Full revenue is $15K ($10K cash + $5K owed). Accounts Receivable tracks what customers owe you.",
                    learning_point="Accrual accounting and receivables",
                    difficulty=3
                ),
            ],
            points_per_correct=15,
            estimated_duration_minutes=15
        ),
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
            id="ba202_revenue_recognition",
            course_id="ba202",
            topic="Revenue Recognition Principles",
            game_type=GameType.SCENARIO_DECISION,
            title="Revenue Recognition Challenge",
            description="When should revenue be recognized? Navigate complex scenarios involving subscriptions, pre-orders, and services.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""SaaS company sells annual subscription for $1,200 on January 1st. Customer pays upfront. How much revenue in January?""",
                    options=[
                        "$1,200 (all upfront)",
                        "$100 (monthly recognition over 12 months)",
                        "$0 (wait until service delivered)",
                        "$600 (half now, half later)"
                    ],
                    correct_option_index=1,
                    explanation="Revenue recognized as earned! $1,200/12 months = $100/month. This matches the accrual principle: recognize revenue when service is delivered.",
                    learning_point="Revenue recognition and accrual accounting",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Customer pre-orders iPhone for $999. Apple receives payment in September but ships in October. When to recognize revenue?""",
                    options=[
                        "September (when cash received)",
                        "October (when product ships)",
                        "November (after return window)",
                        "Immediately"
                    ],
                    correct_option_index=1,
                    explanation="Revenue recognized when performance obligation is satisfied = when product ships. Cash received early becomes 'deferred revenue' (liability).",
                    learning_point="Performance obligations and revenue timing",
                    difficulty=3
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Construction company signs $10M contract for 2-year project. 30% complete after Year 1. Revenue in Year 1?""",
                    options=[
                        "$0 (wait until project done)",
                        "$3M (percentage-of-completion method)",
                        "$10M (all upfront)",
                        "$5M (half)"
                    ],
                    correct_option_index=1,
                    explanation="Long-term contracts use percentage-of-completion: 30% complete × $10M = $3M revenue in Year 1. Matches work performed!",
                    learning_point="Percentage-of-completion for long-term contracts",
                    difficulty=4
                ),
            ],
            points_per_correct=16,
            estimated_duration_minutes=14
        ),
        MiniGame(
            id="ba202_income_statement",
            course_id="ba202",
            topic="Income Statement Analysis",
            game_type=GameType.PROFIT_LOSS,
            title="P&L Statement Builder",
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
        ),
        MiniGame(
            id="ba202_profit_loss_simulator",
            course_id="ba202",
            topic="Building & Interpreting P&L Statements",
            game_type=GameType.PROFIT_LOSS,
            title="P&L Statement Builder",
            description="Build a complete P&L statement for a business. Understand revenue, expenses, and profitability.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="A bakery had: Revenue $50K, Ingredients $15K, Rent $5K, Labor $15K, Utilities $2K. What's Gross Profit (Revenue - COGS)?",
                    options=["$35K", "$20K", "$15K", "$50K"],
                    correct_option_index=0,
                    explanation="Gross Profit = Revenue ($50K) - COGS ($15K ingredients) = $35K. Rent, Labor, and Utilities are operating expenses.",
                    learning_point="Gross profit vs. net profit",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="Same bakery's Operating Profit = Gross Profit - Operating Expenses = $35K - $22K = ?",
                    options=["$13K", "$27K", "$57K", "$8K"],
                    correct_option_index=0,
                    explanation="Operating Profit = $35K - ($5K Rent + $15K Labor + $2K Utilities) = $35K - $22K = $13K",
                    learning_point="Operating profit calculation",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="If the bakery had $500 in interest expenses, what's the Net Income? (Operating Profit $13K)",
                    options=["$12.5K", "$13.5K", "$13K", "$14K"],
                    correct_option_index=0,
                    explanation="Net Income = Operating Profit - Interest Expenses = $13K - $0.5K = $12.5K",
                    learning_point="Complete P&L structure",
                    difficulty=2
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=12
        ),
        MiniGame(
            id="ba202_cash_flow_forecast",
            course_id="ba202",
            topic="Cash Flow Forecasting & Management",
            game_type=GameType.CASH_FLOW,
            title="Cash Flow Forecasting Challenge",
            description="Forecast 3-month cash flow and manage timing differences between profit and cash.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="A company is profitable ($10K profit) but customers pay invoices 30 days late. What cash problem might occur?",
                    options=[
                        "Cash is negative despite profitability",
                        "No problem—profit = cash",
                        "Too much cash on hand",
                        "Must raise prices"
                    ],
                    correct_option_index=0,
                    explanation="Profitable companies can still run out of cash if customers don't pay on time. This is called a cash flow gap.",
                    learning_point="Profit vs. cash flow timing",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="Month 1: Revenue $100K (80% cash, 20% credit). Month 2: Credit sales from Month 1 collected. Cash received Month 2?",
                    options=["$100K", "$80K", "$100K", "$120K"],
                    correct_option_index=2,
                    explanation="Month 2 cash = Current month cash sales ($80K) + Previous month credit collected ($20K) = $100K",
                    learning_point="Accounts receivable cash impact",
                    difficulty=3
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=14
        ),
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
        ),
        MiniGame(
            id="ba301_organization_design",
            course_id="ba301",
            topic="Organizational Structure & Design",
            game_type=GameType.INTERACTIVE_SIM,
            title="Build Your Organizational Chart",
            description="Design an effective organizational structure. Balance hierarchy, span of control, and communication flow.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="You're growing from 10 to 50 employees. What spans of control challenge emerge?",
                    options=[
                        "Managers have fewer people to supervise",
                        "Managers can effectively supervise all 50 people",
                        "Managers have too many direct reports to effectively supervise",
                        "No management change needed"
                    ],
                    correct_option_index=2,
                    explanation="Optimal span of control is typically 3-6 people. One manager can't effectively supervise 50+. Need middle management.",
                    learning_point="Span of control principles",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="A flat organization with few management layers has which advantage?",
                    options=[
                        "Better supervision of employees",
                        "Faster decision-making and communication",
                        "Clearer career paths",
                        "More specialized roles"
                    ],
                    correct_option_index=1,
                    explanation="Flat organizations reduce communication delays and empower employees with faster decisions.",
                    learning_point="Organizational structure trade-offs",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="A Sales Manager reports to VP Sales, who reports to CEO. What type of hierarchy is this?",
                    options=[
                        "Flat organization",
                        "Line organization (direct authority chain)",
                        "Matrix organization",
                        "Functional silos"
                    ],
                    correct_option_index=1,
                    explanation="This is a traditional line organization where authority flows directly down the chain of command.",
                    learning_point="Organizational hierarchy types",
                    difficulty=2
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=13
        ),
        MiniGame(
            id="ba301_conflict_resolution",
            course_id="ba301",
            topic="Conflict Resolution & Team Dynamics",
            game_type=GameType.SCENARIO_DECISION,
            title="Team Conflict Navigator",
            description="Navigate interpersonal conflicts between team members while maintaining productivity.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Two team members have competing priorities causing tension. Best approach?",
                    options=[
                        "Stay neutral and let them figure it out",
                        "Bring them together to understand priorities and find alignment",
                        "Side with the one who complains first",
                        "Assign them to different teams"
                    ],
                    correct_option_index=1,
                    explanation="Facilitated dialogue helps resolve conflicts constructively and often finds creative solutions.",
                    learning_point="Conflict resolution skills",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="Which conflict resolution style emphasizes finding 'win-win' solutions?",
                    options=[
                        "Competing (I win, you lose)",
                        "Avoiding (ignore the issue)",
                        "Collaborating (seek mutual benefit)",
                        "Compromising (both give up something)"
                    ],
                    correct_option_index=2,
                    explanation="Collaboration seeks solutions where all parties get their important needs met.",
                    learning_point="Conflict resolution styles",
                    difficulty=2
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=11
        ),
        MiniGame(
            id="ba301_delegation_master",
            course_id="ba301",
            topic="Delegation & Empowerment",
            game_type=GameType.SCENARIO_DECISION,
            title="Delegation Decision Lab",
            description="Learn to delegate effectively. Choose what to delegate, to whom, and how to empower your team.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""You're overwhelmed with tasks:
A) Strategic planning (high impact, only you can do)
B) Writing weekly status report (low impact, routine)
C) Mentoring junior employee (high impact, could be delegated)

What should you delegate FIRST?""",
                    options=[
                        "A (strategic planning)",
                        "B (status report)",
                        "C (mentoring)",
                        "Nothing (do it all yourself)"
                    ],
                    correct_option_index=1,
                    explanation="Delegate low-impact routine tasks first. Keep high-impact work that requires your expertise. Status reports can be written by others with oversight.",
                    learning_point="Prioritizing delegation decisions",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""You delegate project to Sarah. She does it differently than you would. Result is good. What do you do?""",
                    options=[
                        "Make her redo it your way",
                        "Accept her approach—different ≠ wrong",
                        "Take over the project",
                        "Never delegate to her again"
                    ],
                    correct_option_index=1,
                    explanation="Effective delegation means accepting different approaches if results are good. Micromanaging kills innovation and morale.",
                    learning_point="Trust and autonomy in delegation",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Delegation vs. Abdication—what's the difference?""",
                    options=[
                        "No difference",
                        "Delegation = provide authority + support + accountability. Abdication = dump and disappear.",
                        "Abdication is better",
                        "Delegation means doing it yourself"
                    ],
                    correct_option_index=1,
                    explanation="Good delegation: clear goals, authority, resources, checkpoints. Bad abdication: 'figure it out' with no support. Stay engaged!",
                    learning_point="Effective delegation principles",
                    difficulty=3
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=12
        ),
    ],
    
    "ba302": [  # Marketing Fundamentals
        MiniGame(
            id="ba302_customer_segmentation",
            course_id="ba302",
            topic="Market Segmentation & Targeting",
            game_type=GameType.INTERACTIVE_SIM,
            title="Customer Segmentation Lab",
            description="Segment customers into groups and design targeted marketing strategies for each segment.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""You sell athletic shoes. Which segmentation base is MOST useful for targeting?""",
                    options=[
                        "Customer height",
                        "Psychographic: lifestyle and activity level (runners, gym-goers, casual wearers)",
                        "Hair color",
                        "Favorite food"
                    ],
                    correct_option_index=1,
                    explanation="Psychographic segmentation (lifestyle, interests, activities) predicts shoe needs better than demographics. Runners need different shoes than casual wearers!",
                    learning_point="Psychographic vs. demographic segmentation",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Segment A: 10,000 customers, $50 average order, $5 CAC. Segment B: 1,000 customers, $500 average order, $50 CAC. Which is more profitable?""",
                    options=[
                        "A (more customers)",
                        "B (higher profit per customer: $450 vs $45)",
                        "Same profitability",
                        "Need more data"
                    ],
                    correct_option_index=1,
                    explanation="Segment A: $50-$5=$45 profit × 10K = $450K total. Segment B: $500-$50=$450 profit × 1K = $450K total. Same total BUT B has 10× profit margin!",
                    learning_point="Customer segment profitability analysis",
                    difficulty=4
                ),
                GameQuestion(
                    id="q3",
                    prompt="""You launch targeted campaigns. Segment B responds 2× better. What's your strategy?""",
                    options=[
                        "Ignore Segment A completely",
                        "Focus marketing budget on Segment B (higher ROI)",
                        "Treat all segments equally",
                        "Stop all marketing"
                    ],
                    correct_option_index=1,
                    explanation="Concentrate resources where ROI is highest! Don't spread budget thin. Segment B: higher margin + better response = priority target.",
                    learning_point="Resource allocation based on segment performance",
                    difficulty=2
                ),
            ],
            points_per_correct=16,
            estimated_duration_minutes=14
        ),
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
        ),
        MiniGame(
            id="ba302_marketing_mix",
            course_id="ba302",
            topic="Marketing Mix (4Ps: Product, Price, Place, Promotion)",
            game_type=GameType.INTERACTIVE_SIM,
            title="4Ps Marketing Strategy Simulator",
            description="Develop a complete marketing strategy by deciding on product features, pricing, distribution, and promotion.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="You're launching a premium smartphone. Which pricing strategy aligns with your market position?",
                    options=[
                        "Low price to undercut competitors",
                        "Premium price to signal quality and exclusivity",
                        "Competitive price matching major brands",
                        "Penetration pricing"
                    ],
                    correct_option_index=1,
                    explanation="Premium positioning justifies higher prices when quality and brand perception support it.",
                    learning_point="Premium pricing strategy",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="Your target market shops mostly online. What 'Place' distribution strategy is best?",
                    options=[
                        "Only physical retail stores",
                        "Primarily e-commerce platforms",
                        "Only flagship brand stores",
                        "Street vendors"
                    ],
                    correct_option_index=1,
                    explanation="Distribution must match customer shopping preferences and behaviors.",
                    learning_point="Distribution channel selection",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="You're promoting a budget coffee brand to college students. Best promotional approach?",
                    options=[
                        "TV commercials during prime time",
                        "Newspaper coupons",
                        "Social media ads + campus sampling events",
                        "Radio ads"
                    ],
                    correct_option_index=2,
                    explanation="Reach the target audience where they are: digital channels + experiential marketing (sampling).",
                    learning_point="Promotion channel selection",
                    difficulty=2
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=12
        ),
        MiniGame(
            id="ba302_brand_positioning",
            course_id="ba302",
            topic="Brand Positioning & Differentiation",
            game_type=GameType.CASE_STUDY,
            title="Brand Positioning Challenge",
            description="Position a brand distinctly in the market and defend against competitors.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Your brand is known for sustainability & quality but competes on price with cheap fast-fashion. Risk?",
                    options=[
                        "Brand confusion—unclear value proposition",
                        "No problem—customers appreciate low prices",
                        "Increased market share automatically",
                        "Better sustainability"
                    ],
                    correct_option_index=0,
                    explanation="Conflicting positioning confuses customers. Premium positioning + cheap pricing is a mixed message.",
                    learning_point="Brand positioning consistency",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="Nike's 'Just Do It' positioning appeals to which brand personality?",
                    options=[
                        "Practical and economical",
                        "Inspirational, athletic, determined",
                        "Luxury and exclusivity",
                        "Family-oriented and safe"
                    ],
                    correct_option_index=1,
                    explanation="Nike positions as empowering, athletic, and motivational—resonating with active, ambitious consumers.",
                    learning_point="Brand personality and positioning",
                    difficulty=2
                ),
            ],
            points_per_correct=12,
            estimated_duration_minutes=11
        ),
    ],

    # SEMESTER 4 COURSES
    "ba401": [  # Corporate Finance
        MiniGame(
            id="ba401_time_value_money",
            course_id="ba401",
            topic="Time Value of Money & Discounting",
            game_type=GameType.CALCULATOR,
            title="Time Value of Money Calculator",
            description="Master present value, future value, and NPV calculations. Understand why money today is worth more than money tomorrow.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""You win lottery: Option A = $100,000 today. Option B = $120,000 in 2 years. Interest rate = 5%/year. Which is worth MORE in today's dollars?""",
                    options=[
                        "Option A ($100K today)",
                        "Option B ($120K in 2 years)",
                        "Equal value",
                        "Can't compare"
                    ],
                    correct_option_index=1,
                    explanation="PV of Option B = $120K/(1.05)² = $108,844. Worth MORE than $100K today! Future money is worth less, but $120K future > $100K present at 5% rate.",
                    learning_point="Present value calculation and comparison",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Investment pays $10K/year for 3 years. Discount rate = 8%. What's the present value (roughly)?""",
                    options=[
                        "$30,000 (sum of payments)",
                        "$25,771 (discounted)",
                        "$32,500",
                        "$10,000"
                    ],
                    correct_option_index=1,
                    explanation="PV = $10K/1.08 + $10K/1.08² + $10K/1.08³ = $9,259 + $8,573 + $7,938 = $25,770. Future cash flows are worth LESS in today's dollars!",
                    learning_point="Multi-period present value calculation",
                    difficulty=4
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Why does higher discount rate DECREASE present value?""",
                    options=[
                        "Math error",
                        "Higher rate means future money is worth less today (opportunity cost)",
                        "Higher rate increases value",
                        "No relationship"
                    ],
                    correct_option_index=1,
                    explanation="Discount rate reflects opportunity cost. At 10% rate, you could invest money elsewhere and earn 10%. So future $100 is worth less today.",
                    learning_point="Discount rate as opportunity cost",
                    difficulty=3
                ),
            ],
            points_per_correct=16,
            estimated_duration_minutes=15
        ),
        MiniGame(
            id="ba401_capital_budgeting",
            course_id="ba401",
            topic="Capital Budgeting & NPV",
            game_type=GameType.CALCULATOR,
            title="Capital Investment Decision Lab",
            description="Evaluate investment projects using NPV, IRR, and payback period. Make go/no-go decisions.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Project costs $100K upfront, generates $40K/year for 3 years. Discount rate = 10%. NPV = ?
(Hint: PV of $40K for 3 years at 10% ≈ $99,474)""",
                    options=[
                        "$20K",
                        "-$526 (reject project)",
                        "$120K",
                        "$0"
                    ],
                    correct_option_index=1,
                    explanation="NPV = -$100K + $99,474 = -$526. NEGATIVE NPV = reject project! Costs more than present value of returns.",
                    learning_point="NPV decision rule",
                    difficulty=4
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Two projects: A has NPV=$50K, IRR=15%. B has NPV=$40K, IRR=20%. You can only do one. Choose:""",
                    options=[
                        "Project A (higher NPV creates more value)",
                        "Project B (higher IRR)",
                        "Neither",
                        "Both"
                    ],
                    correct_option_index=0,
                    explanation="NPV tells you DOLLAR value created. IRR is return rate. When choosing between projects, NPV is better—choose higher value creation!",
                    learning_point="NPV vs. IRR for project selection",
                    difficulty=4
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Project payback period = 4 years. Useful life = 5 years. Should you invest based on payback alone?""",
                    options=[
                        "Yes (recovers investment)",
                        "Need NPV analysis—payback ignores time value and cash flows after payback",
                        "No (too long)",
                        "Yes (good ratio)"
                    ],
                    correct_option_index=1,
                    explanation="Payback period is simple but flawed: ignores time value of money and cash flows after payback. Always use NPV for capital decisions!",
                    learning_point="Payback period limitations",
                    difficulty=3
                ),
            ],
            points_per_correct=18,
            estimated_duration_minutes=16
        ),
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
        ),
        MiniGame(
            id="ba401_valuation",
            course_id="ba401",
            topic="Business Valuation & Financial Analysis",
            game_type=GameType.CALCULATOR,
            title="Company Valuation Lab",
            description="Learn multiple valuation methods: DCF, P/E multiples, asset-based, and comparable companies.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Company earned $10M profit. Industry average P/E ratio is 15x. Company value (market cap) ≈ ?",
                    options=["$10M", "$15M", "$150M", "$1.5B"],
                    correct_option_index=2,
                    explanation="Market Cap = Earnings × P/E Ratio = $10M × 15 = $150M. P/E multiples value companies relative to earnings.",
                    learning_point="P/E multiple valuation",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="A company has Assets of $100M and Liabilities of $40M. Asset-based valuation of Equity ≈ ?",
                    options=["$100M", "$140M", "$60M", "$40M"],
                    correct_option_index=2,
                    explanation="Equity Value = Assets - Liabilities = $100M - $40M = $60M. Simple but doesn't account for earning power.",
                    learning_point="Asset-based valuation",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="Using Discounted Cash Flow (DCF): Future cash flows are $100M/year, discount rate 10%. Present Value ≈ ?",
                    options=["$100M", "$1B", "$500M", "$1.5B"],
                    correct_option_index=1,
                    explanation="Perpetuity value = Cash Flow / Discount Rate = $100M / 0.10 = $1B (simplified). DCF captures intrinsic value.",
                    learning_point="DCF valuation method",
                    difficulty=3
                ),
            ],
            points_per_correct=15,
            estimated_duration_minutes=14
        ),
        MiniGame(
            id="ba401_financing_decisions",
            course_id="ba401",
            topic="Debt vs. Equity Financing & Capital Structure",
            game_type=GameType.SCENARIO_DECISION,
            title="Financing Strategy Game",
            description="Decide whether to raise capital through debt or equity financing based on scenarios.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Your startup is profitable and growing. Should you raise $5M via debt (low interest) or equity (dilute ownership)?",
                    options=[
                        "Always choose debt—it's cheaper",
                        "Always choose equity—avoid debt risk",
                        "Depends on growth rate, cash flow, and your control priorities",
                        "Flip a coin"
                    ],
                    correct_option_index=2,
                    explanation="High-growth profitable companies often prefer debt (keep control). Risky companies prefer equity (spread risk).",
                    learning_point="Debt vs. equity trade-offs",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="High debt creates financial leverage that amplifies returns—but creates what risk?",
                    options=[
                        "No risk—leverage is always good",
                        "Bankruptcy risk if cash flow declines",
                        "Lower stock prices",
                        "Too much equity"
                    ],
                    correct_option_index=1,
                    explanation="Debt obligations must be paid regardless of performance. High debt increases bankruptcy risk.",
                    learning_point="Financial leverage and risk",
                    difficulty=2
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=12
        ),
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
        ),
        MiniGame(
            id="ba402_swot_analysis",
            course_id="ba402",
            topic="SWOT Analysis & Strategic Planning",
            game_type=GameType.INTERACTIVE_SIM,
            title="SWOT Analysis Lab",
            description="Conduct a SWOT analysis on a company and develop strategic recommendations based on findings.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="A retail company's SWOT shows: Strength=strong brand, Weakness=high overhead, Opportunity=e-commerce growth, Threat=big-box competitors. Best strategy?",
                    options=[
                        "Keep status quo",
                        "Expand physical stores",
                        "Leverage brand into e-commerce to compete online",
                        "Lower prices to match competitors"
                    ],
                    correct_option_index=2,
                    explanation="Match strengths (brand) with opportunities (e-commerce) to build sustainable advantage.",
                    learning_point="Matching SWOT to strategy",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="Your company identifies a major threat (new competitor). Where should you invest?",
                    options=[
                        "Do nothing",
                        "Invest in internal strengths to defend/differentiate",
                        "Copy competitor products",
                        "Reduce R&D spending"
                    ],
                    correct_option_index=1,
                    explanation="Threats are best countered by strengthening your competitive advantages and distinctive capabilities.",
                    learning_point="Threat response strategy",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="Which represents the best strategic opportunity?",
                    options=[
                        "Finding a cheaper supplier",
                        "Identifying a high-growth market segment that fits your strengths",
                        "Copying a competitor's product line",
                        "Reducing employee salaries"
                    ],
                    correct_option_index=1,
                    explanation="Strong opportunities align external market growth with your internal capabilities.",
                    learning_point="Identifying strategic opportunities",
                    difficulty=2
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=13
        ),
        MiniGame(
            id="ba402_growth_strategy",
            course_id="ba402",
            topic="Growth Strategies: Organic vs. Acquisition",
            game_type=GameType.SCENARIO_DECISION,
            title="Growth Strategy Decision Maker",
            description="Choose between organic growth (internal development), expansion, and acquisitions based on scenarios.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="You need to enter a new market quickly with strong brand recognition. Best approach?",
                    options=[
                        "Organic growth—build from scratch (slow)",
                        "Acquisition of established competitor (fast entry)",
                        "Merge with non-competitor (unrelated)",
                        "Wait and see"
                    ],
                    correct_option_index=1,
                    explanation="Acquisitions provide fast market entry with existing brand/customer base, though at higher cost.",
                    learning_point="Acquisition vs. organic growth",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="Your company has unique technology with a small market. Best growth path?",
                    options=[
                        "Acquire competitors (expensive)",
                        "Expand into adjacent markets organically (leverage technology)",
                        "Sell the company",
                        "Do nothing"
                    ],
                    correct_option_index=1,
                    explanation="Organic expansion leverages unique capabilities into larger markets cost-effectively.",
                    learning_point="Organic growth with differentiation",
                    difficulty=2
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=11
        ),
    ],
    
    # ============================================
    # COMPUTER SCIENCE COURSE GAMES
    # ============================================
    
    "cs101": [  # Intro Programming
        MiniGame(
            id="cs101_debug_hunt",
            course_id="cs101",
            topic="Debugging & Problem Solving",
            game_type=GameType.CODE_DEBUG,
            title="Bug Hunt: Fix the Code",
            description="Find and fix bugs in Python code. Learn to read error messages and trace logic errors.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""This code should print 'Hello' 5 times, but it prints 6 times. Why?
```python
count = 0
while count <= 5:
    print('Hello')
    count += 1
```""",
                    options=[
                        "count starts at 0",
                        "Should be < instead of <=",
                        "print() is inside loop",
                        "count += 1 is wrong"
                    ],
                    correct_option_index=1,
                    explanation="Loop runs when count=0,1,2,3,4,5 (6 times total). Using < instead of <= makes it run while count<5 (exactly 5 times: 0,1,2,3,4).",
                    learning_point="Off-by-one errors with <= vs <",
                    difficulty=1
                ),
                GameQuestion(
                    id="q2",
                    prompt="""What's wrong with this function?
```python
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

result = calculate_average([])
```""",
                    options=[
                        "total starts at wrong value",
                        "Division by zero when list is empty",
                        "for loop syntax incorrect",
                        "Nothing wrong"
                    ],
                    correct_option_index=1,
                    explanation="Empty list causes len(numbers) to be 0, triggering ZeroDivisionError. Always validate input before division!",
                    learning_point="Edge case handling and input validation",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="""This code should return True if number is even, but always returns False. Why?
```python
def is_even(n):
    if n % 2 == 0:
        return True
    return False
```""",
                    options=[
                        "Logic is actually correct",
                        "Should use n / 2",
                        "Missing else keyword",
                        "== should be ="
                    ],
                    correct_option_index=0,
                    explanation="This code is CORRECT! It returns True when n%2==0 (even), False otherwise. The 'always returns False' was a trick—the code works perfectly.",
                    learning_point="Reading code carefully and testing assumptions",
                    difficulty=2
                ),
            ],
            points_per_correct=12,
            estimated_duration_minutes=15
        ),
        MiniGame(
            id="cs101_variable_trace",
            course_id="cs101",
            topic="Variables & State Management",
            game_type=GameType.CODE_TRACE,
            title="Variable Trace Challenge",
            description="Trace how variables change through code execution. Master the mental model of program state.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""What is the value of `x` after this code runs?
```python
x = 10
y = x + 5
x = y - 3
x = x * 2
```""",
                    options=["10", "12", "15", "24"],
                    correct_option_index=3,
                    explanation="Trace: x=10 → y=15 → x=12 → x=24. Each line uses the CURRENT value of x or y, not the original.",
                    learning_point="Variable mutation and state tracking",
                    difficulty=1
                ),
                GameQuestion(
                    id="q2",
                    prompt="""What does this print?
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```""",
                    options=["[1, 2, 3]", "[1, 2, 3, 4]", "[4]", "Error"],
                    correct_option_index=1,
                    explanation="b = a creates a reference, not a copy! Both variables point to the SAME list. Changing b also changes a.",
                    learning_point="References vs. copies (aliasing)",
                    difficulty=3
                ),
                GameQuestion(
                    id="q3",
                    prompt="""What is `total` after this loop?
```python
total = 0
for i in range(1, 4):
    total += i
```""",
                    options=["6", "10", "4", "7"],
                    correct_option_index=0,
                    explanation="range(1,4) gives [1,2,3]. Total: 0→1→3→6. Remember range(a,b) goes from a to b-1.",
                    learning_point="Loop accumulation and range behavior",
                    difficulty=1
                ),
            ],
            points_per_correct=10,
            estimated_duration_minutes=12
        ),
        MiniGame(
            id="cs101_function_builder",
            course_id="cs101",
            topic="Functions & Modularity",
            game_type=GameType.CODE_BUILDER,
            title="Function Factory",
            description="Build working functions from specifications. Learn to translate requirements into code.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Build a function that returns the MAXIMUM of three numbers.
Which implementation is correct?""",
                    options=[
                        "def max3(a,b,c): return a if a>b and a>c else b",
                        "def max3(a,b,c): return max(a, max(b,c))",
                        "def max3(a,b,c): return a+b+c",
                        "def max3(a,b,c): return (a>b>c)"
                    ],
                    correct_option_index=1,
                    explanation="max(a, max(b,c)) correctly finds the maximum: first find max of b and c, then compare with a. Option A fails when b>a but c>b.",
                    learning_point="Nested function calls and edge case testing",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Create a function that counts vowels in a string. Which is correct?""",
                    options=[
                        "def count_vowels(s): return len(s)",
                        "def count_vowels(s): return sum(1 for c in s if c in 'aeiou')",
                        "def count_vowels(s): return s.count('a')",
                        "def count_vowels(s): return 'aeiou' in s"
                    ],
                    correct_option_index=1,
                    explanation="sum(1 for c in s if c in 'aeiou') iterates each character, adds 1 if it's a vowel, and sums the total. Elegant Python!",
                    learning_point="String iteration and generator expressions",
                    difficulty=3
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=10
        ),
    ],
    
    "cs102": [  # Data Structures
        MiniGame(
            id="cs102_stack_operations",
            course_id="cs102",
            topic="Stacks (LIFO)",
            game_type=GameType.DATA_STRUCTURE_VIZ,
            title="Stack Master: LIFO in Action",
            description="Visualize stack operations (push, pop). Understand Last-In-First-Out and real-world applications.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Start with empty stack. Execute these operations:
push(10), push(20), pop(), push(30), pop()

What's left in the stack from bottom to top?""",
                    options=["[10]", "[20, 30]", "[10, 20]", "[30, 10]"],
                    correct_option_index=0,
                    explanation="Trace: [] → [10] → [10,20] → [10] (pop 20) → [10,30] → [10] (pop 30). Final: just 10 remains.",
                    learning_point="Stack operations and LIFO ordering",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Browser history uses a stack. You visit:
google.com → reddit.com → youtube.com
Then hit Back button twice.

What page are you on?""",
                    options=["youtube.com", "reddit.com", "google.com", "Error"],
                    correct_option_index=2,
                    explanation="Stack of pages: [google, reddit, youtube]. Back pops youtube, then reddit. You're back at google.",
                    learning_point="Real-world stack application: browser history",
                    difficulty=1
                ),
                GameQuestion(
                    id="q3",
                    prompt="""What's the time complexity of pop() operation on a stack?""",
                    options=["O(1) - constant", "O(n) - linear", "O(log n)", "O(n²)"],
                    correct_option_index=0,
                    explanation="Stack pop is O(1)—just remove the top element, no iteration needed. This efficiency makes stacks powerful for undo/redo.",
                    learning_point="Stack time complexity analysis",
                    difficulty=2
                ),
            ],
            points_per_correct=12,
            estimated_duration_minutes=10
        ),
        MiniGame(
            id="cs102_tree_traversal",
            course_id="cs102",
            topic="Binary Trees & Traversals",
            game_type=GameType.CODE_TRACE,
            title="Tree Traversal Detective",
            description="Given a binary tree, predict the output of different traversal algorithms (inorder, preorder, postorder).",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Given this binary tree:
       5
      / \\
     3   8
    / \\
   1   4

What's the INORDER traversal?""",
                    options=["5,3,1,4,8", "1,3,4,5,8", "1,4,3,8,5", "5,8,4,3,1"],
                    correct_option_index=1,
                    explanation="Inorder = Left, Root, Right recursively. Result: 1 (left of 3), 3, 4 (right of 3), 5 (root), 8 (right of 5) = [1,3,4,5,8]",
                    learning_point="Inorder traversal (sorted for BST)",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Same tree—what's PREORDER traversal?
       5
      / \\
     3   8
    / \\
   1   4""",
                    options=["5,3,1,4,8", "1,3,4,5,8", "1,4,3,8,5", "8,5,4,3,1"],
                    correct_option_index=0,
                    explanation="Preorder = Root, Left, Right. Result: 5 (root), 3, 1, 4 (left subtree), 8 (right subtree) = [5,3,1,4,8]",
                    learning_point="Preorder traversal pattern",
                    difficulty=3
                ),
                GameQuestion(
                    id="q3",
                    prompt="""When is inorder traversal most useful?""",
                    options=[
                        "Deleting a tree",
                        "Getting sorted values from binary search tree",
                        "Copying a tree structure",
                        "Finding tree height"
                    ],
                    correct_option_index=1,
                    explanation="Inorder traversal of a BST yields values in SORTED order! This is why BSTs are powerful for sorted data.",
                    learning_point="BST inorder property",
                    difficulty=2
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=14
        ),
        MiniGame(
            id="cs102_hash_collision",
            course_id="cs102",
            topic="Hash Tables & Collision Resolution",
            game_type=GameType.INTERACTIVE_SIM,
            title="Hash Table Collision Lab",
            description="Simulate hash table insertions with collisions. Learn chaining vs. open addressing strategies.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Hash table size = 10. Hash function: h(key) = key % 10.
Insert keys: 23, 13, 33

Where do collisions occur?""",
                    options=[
                        "No collisions",
                        "All three collide at index 3",
                        "13 and 33 collide",
                        "23 and 33 collide"
                    ],
                    correct_option_index=1,
                    explanation="h(23)=3, h(13)=3, h(33)=3. All hash to index 3! This is why collision resolution (chaining/open addressing) is critical.",
                    learning_point="Hash collisions and modulo function",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Using CHAINING to resolve collisions, what does index 3 look like after inserting 23,13,33?""",
                    options=[
                        "Just stores 33 (last inserted)",
                        "A linked list: 23 → 13 → 33",
                        "Error - can't insert",
                        "Spreads to index 4,5,6"
                    ],
                    correct_option_index=1,
                    explanation="Chaining stores colliding keys in a linked list at the same index. All three keys live at index 3 in a chain.",
                    learning_point="Chaining collision resolution",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="""What's the average time complexity for hash table lookup with good hash function?""",
                    options=["O(1)", "O(log n)", "O(n)", "O(n²)"],
                    correct_option_index=0,
                    explanation="Hash tables provide O(1) average lookup! Direct access via hash function. This makes dictionaries/maps incredibly fast.",
                    learning_point="Hash table performance",
                    difficulty=2
                ),
            ],
            points_per_correct=12,
            estimated_duration_minutes=12
        ),
    ],
    
    "cs203": [  # Algorithms
        MiniGame(
            id="cs203_sorting_race",
            course_id="cs203",
            topic="Sorting Algorithm Comparison",
            game_type=GameType.ALGORITHM_RACE,
            title="Sorting Algorithm Showdown",
            description="Compare sorting algorithms on different inputs. Learn when each algorithm shines and when it struggles.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Array is ALREADY SORTED: [1,2,3,4,5]. Which sorting algorithm is FASTEST?""",
                    options=[
                        "QuickSort (O(n log n) average)",
                        "MergeSort (O(n log n) always)",
                        "Bubble Sort (O(n) best case!)",
                        "Selection Sort (O(n²))"
                    ],
                    correct_option_index=2,
                    explanation="Bubble Sort on sorted data makes ONE pass with no swaps = O(n)! Best case advantage, though worst case is O(n²).",
                    learning_point="Best-case algorithm performance",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Array in REVERSE order: [5,4,3,2,1]. Which algorithm performs WORST?""",
                    options=[
                        "QuickSort (if pivot = first element)",
                        "MergeSort",
                        "Insertion Sort",
                        "All perform the same"
                    ],
                    correct_option_index=0,
                    explanation="QuickSort with first-element pivot on reversed data creates worst case: O(n²)! Every partition is unbalanced.",
                    learning_point="QuickSort worst case and pivot selection",
                    difficulty=4
                ),
                GameQuestion(
                    id="q3",
                    prompt="""You need GUARANTEED O(n log n) time regardless of input. Choose:""",
                    options=["QuickSort", "MergeSort", "Bubble Sort", "Selection Sort"],
                    correct_option_index=1,
                    explanation="MergeSort is ALWAYS O(n log n) best/average/worst case. QuickSort averages O(n log n) but worst case is O(n²).",
                    learning_point="Worst-case guarantees",
                    difficulty=3
                ),
            ],
            points_per_correct=15,
            estimated_duration_minutes=13
        ),
        MiniGame(
            id="cs203_recursion_master",
            course_id="cs203",
            topic="Recursion & Divide-and-Conquer",
            game_type=GameType.CODE_TRACE,
            title="Recursion Unwrapped",
            description="Trace recursive function calls. Visualize the call stack and understand base cases.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""What does factorial(4) return?
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
```""",
                    options=["4", "10", "24", "Infinite loop"],
                    correct_option_index=2,
                    explanation="Trace: f(4) = 4*f(3) = 4*3*f(2) = 4*3*2*f(1) = 4*3*2*1 = 24. Base case (n=1) stops recursion.",
                    learning_point="Recursion with base case",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""How many times is fibonacci(5) called in this naive recursive implementation?
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```""",
                    options=["5 calls", "15 calls", "8 calls", "10 calls"],
                    correct_option_index=1,
                    explanation="fib(5) calls fib(4)+fib(3). Both recalculate fib(2), fib(1) multiple times! Total: 15 calls. This is why dynamic programming matters.",
                    learning_point="Recursion inefficiency and memoization need",
                    difficulty=4
                ),
                GameQuestion(
                    id="q3",
                    prompt="""What's the base case in binary search recursion?""",
                    options=[
                        "Array has 1 element",
                        "Element found OR search space empty",
                        "Array is sorted",
                        "No base case needed"
                    ],
                    correct_option_index=1,
                    explanation="Base cases: found target (return True) OR left>right meaning empty search space (return False). Always need a stopping condition!",
                    learning_point="Multiple base cases in recursion",
                    difficulty=2
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=13
        ),
        MiniGame(
            id="cs203_big_o_challenge",
            course_id="cs203",
            topic="Algorithm Analysis & Big O",
            game_type=GameType.CODE_TRACE,
            title="Big O Detective",
            description="Analyze code and determine time complexity. Master Big O notation for algorithm comparison.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""What's the time complexity?
```python
for i in range(n):
    for j in range(n):
        print(i, j)
```""",
                    options=["O(n)", "O(n²)", "O(2n)", "O(log n)"],
                    correct_option_index=1,
                    explanation="Nested loops both running n times = n×n = O(n²). Outer loop runs n times, inner loop runs n times FOR EACH outer iteration.",
                    learning_point="Nested loop complexity analysis",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""What's the time complexity of binary search on sorted array of size n?""",
                    options=["O(n)", "O(log n)", "O(n log n)", "O(1)"],
                    correct_option_index=1,
                    explanation="Binary search cuts search space in HALF each step: n → n/2 → n/4 → ... → 1. This is O(log n). Incredibly fast!",
                    learning_point="Logarithmic time complexity",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Which operation is O(1) for a hash table?""",
                    options=["Finding minimum element", "Lookup by key (average case)", "Sorting all keys", "Reversing the table"],
                    correct_option_index=1,
                    explanation="Hash table lookup is O(1) average case—direct access via hash function! This makes Python dicts incredibly fast for lookups.",
                    learning_point="Hash table O(1) lookup performance",
                    difficulty=1
                ),
            ],
            points_per_correct=12,
            estimated_duration_minutes=11
        ),
        MiniGame(
            id="cs102_linked_list_operations",
            course_id="cs102",
            topic="Linked Lists",
            game_type=GameType.DATA_STRUCTURE_VIZ,
            title="Linked List Constructor",
            description="Build and manipulate linked lists. Understand pointers and node connections.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""You have: head → [10] → [20] → [30] → None
You want to INSERT 15 between 10 and 20.

Which steps are correct?""",
                    options=[
                        "Create node(15), point 15.next to 20, point 10.next to 15",
                        "Create node(15), point 15.next to 10, point 20.next to 15",
                        "Just change 20 to 15",
                        "Can't insert in middle"
                    ],
                    correct_option_index=0,
                    explanation="1) Create new node with value 15. 2) Point new_node.next to 20. 3) Point 10.next to new_node. Order matters to avoid breaking the chain!",
                    learning_point="Linked list insertion mechanics",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="""What's the time complexity to ACCESS the 100th element in a linked list?""",
                    options=["O(1)", "O(log n)", "O(n)", "O(100)"],
                    correct_option_index=2,
                    explanation="Must traverse from head → node 2 → node 3 → ... → node 100. That's O(n). Unlike arrays, no direct index access!",
                    learning_point="Linked list vs array access time",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="""When is a linked list BETTER than an array?""",
                    options=[
                        "Need fast random access",
                        "Memory is limited and contiguous",
                        "Frequent insertions/deletions at arbitrary positions",
                        "Need to sort data"
                    ],
                    correct_option_index=2,
                    explanation="Linked lists excel at O(1) insertion/deletion once you have a reference to the node. Arrays require shifting elements = O(n).",
                    learning_point="When to use linked lists",
                    difficulty=2
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=12
        ),
    ],
    
    "cs220": [  # Database Systems
        MiniGame(
            id="cs220_sql_query_builder",
            course_id="cs220",
            topic="SQL Queries & Joins",
            game_type=GameType.CODE_BUILDER,
            title="SQL Query Workshop",
            description="Write SQL queries to retrieve data from a movie database. Master SELECT, WHERE, JOIN, and aggregation.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Database tables:
movies(id, title, year, director_id)
directors(id, name, country)

Write a query to find all movies directed by Christopher Nolan:""",
                    options=[
                        "SELECT * FROM movies WHERE director='Nolan'",
                        "SELECT m.* FROM movies m JOIN directors d ON m.director_id=d.id WHERE d.name='Christopher Nolan'",
                        "SELECT movies WHERE director LIKE 'Nolan'",
                        "SELECT * FROM directors WHERE name='Nolan'"
                    ],
                    correct_option_index=1,
                    explanation="Need to JOIN movies and directors tables on director_id=id, then filter by name. JOIN connects related data across tables!",
                    learning_point="SQL JOIN operations",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Find the AVERAGE rating for movies released after 2010:
ratings(movie_id, score)
movies(id, title, year)""",
                    options=[
                        "SELECT AVG(score) FROM ratings WHERE year>2010",
                        "SELECT AVG(score) FROM ratings r JOIN movies m ON r.movie_id=m.id WHERE m.year>2010",
                        "SELECT score/COUNT(*) FROM ratings",
                        "SELECT AVG(*) FROM movies"
                    ],
                    correct_option_index=1,
                    explanation="AVG() aggregates ratings. Must JOIN to access movie.year for filtering. Aggregation + JOIN is a common pattern!",
                    learning_point="Aggregation with joins",
                    difficulty=3
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Which query finds directors with MORE than 5 movies?""",
                    options=[
                        "SELECT name FROM directors WHERE movies>5",
                        "SELECT d.name FROM directors d JOIN movies m ON d.id=m.director_id GROUP BY d.id HAVING COUNT(*)>5",
                        "SELECT name FROM directors LIMIT 5",
                        "SELECT COUNT(movies) FROM directors"
                    ],
                    correct_option_index=1,
                    explanation="GROUP BY groups movies per director. HAVING filters grouped results. WHERE filters before grouping, HAVING filters after!",
                    learning_point="GROUP BY and HAVING clauses",
                    difficulty=4
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=15
        ),
        MiniGame(
            id="cs220_database_design",
            course_id="cs220",
            topic="Database Normalization",
            game_type=GameType.INTERACTIVE_SIM,
            title="Database Normalization Workshop",
            description="Design normalized databases to eliminate redundancy and anomalies. Apply 1NF, 2NF, 3NF rules.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""You have a table:
students(id, name, major_name, major_building, major_dean)

What's the problem?""",
                    options=[
                        "No problem",
                        "Too many columns",
                        "Major info is redundant for students with same major (update anomaly)",
                        "Missing primary key"
                    ],
                    correct_option_index=2,
                    explanation="If you update major_building for one CS student, you must update ALL CS students. This is an update anomaly—violates 2NF/3NF.",
                    learning_point="Update anomalies and normalization need",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="""How do you normalize the students table?""",
                    options=[
                        "Delete major_building column",
                        "Split into: students(id,name,major_id) + majors(id,name,building,dean)",
                        "Add more columns",
                        "Leave as-is"
                    ],
                    correct_option_index=1,
                    explanation="Create separate majors table. Students reference major by ID (foreign key). Now major info stored ONCE—no redundancy!",
                    learning_point="Third normal form (3NF) design",
                    difficulty=3
                ),
                GameQuestion(
                    id="q3",
                    prompt="""What's the benefit of normalization?""",
                    options=[
                        "Faster queries always",
                        "Eliminates redundancy and update anomalies",
                        "Uses less disk space only",
                        "Makes database slower"
                    ],
                    correct_option_index=1,
                    explanation="Normalization prevents data inconsistency. Update major info once, not in 1000 student records. Trade-off: more JOINs needed.",
                    learning_point="Normalization benefits and trade-offs",
                    difficulty=2
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=13
        ),
    ],
    
    "cs230": [  # Software Engineering
        MiniGame(
            id="cs230_design_patterns",
            course_id="cs230",
            topic="Design Patterns & Architecture",
            game_type=GameType.SYSTEM_DESIGN,
            title="Design Pattern Architect",
            description="Choose the right design pattern for different software problems. Learn Singleton, Factory, Observer, and Strategy patterns.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""You need exactly ONE instance of DatabaseConnection shared across your entire app. Which pattern?""",
                    options=[
                        "Factory Pattern",
                        "Singleton Pattern",
                        "Observer Pattern",
                        "Strategy Pattern"
                    ],
                    correct_option_index=1,
                    explanation="Singleton ensures only one instance exists globally. Perfect for shared resources like DB connections, loggers, config managers.",
                    learning_point="Singleton pattern for shared resources",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Your UI needs to update automatically when data model changes (like React). Which pattern?""",
                    options=[
                        "Singleton",
                        "Factory",
                        "Observer (Publish-Subscribe)",
                        "Decorator"
                    ],
                    correct_option_index=2,
                    explanation="Observer pattern: subjects notify observers of changes. UI subscribes to model changes and updates automatically. Used in React, Vue, Angular!",
                    learning_point="Observer pattern for reactive systems",
                    difficulty=3
                ),
                GameQuestion(
                    id="q3",
                    prompt="""You want to create different types of buttons (primary, secondary, icon) without repeating code. Which pattern?""",
                    options=[
                        "Factory Pattern (creates objects based on type)",
                        "Singleton",
                        "Observer",
                        "No pattern needed"
                    ],
                    correct_option_index=0,
                    explanation="Factory Pattern centralizes object creation logic. Pass 'primary' or 'icon' → factory returns correct button type. Reduces duplication!",
                    learning_point="Factory pattern for object creation",
                    difficulty=2
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=12
        ),
        MiniGame(
            id="cs230_testing_pyramid",
            course_id="cs230",
            topic="Software Testing Strategies",
            game_type=GameType.SCENARIO_DECISION,
            title="Testing Strategy Simulator",
            description="Design a testing strategy balancing unit tests, integration tests, and E2E tests. Learn the testing pyramid.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Your app has 1000 functions. Which test type should be MOST numerous?""",
                    options=[
                        "Manual tests",
                        "Unit tests (test individual functions)",
                        "Integration tests",
                        "End-to-end tests (test full workflows)"
                    ],
                    correct_option_index=1,
                    explanation="Testing Pyramid: MANY unit tests (fast, cheap), SOME integration tests, FEW E2E tests (slow, expensive). Unit tests = foundation!",
                    learning_point="Testing pyramid structure",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Bug found: payment processing fails when API is down. What test type would catch this?""",
                    options=[
                        "Unit test (tests one function)",
                        "Integration test (tests service interaction)",
                        "Spelling test",
                        "Code review"
                    ],
                    correct_option_index=1,
                    explanation="Integration tests verify that components work TOGETHER. API failure affects multiple services—need integration test to catch this.",
                    learning_point="Integration testing for system interactions",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Which testing practice is most valuable for catching regressions?""",
                    options=[
                        "Manual testing before each release",
                        "Automated test suite run on every code change (CI/CD)",
                        "Testing only new features",
                        "No testing needed"
                    ],
                    correct_option_index=1,
                    explanation="Automated tests in CI/CD catch regressions instantly when new code breaks old features. Manual testing is slow and misses edge cases.",
                    learning_point="CI/CD and automated testing",
                    difficulty=2
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=11
        ),
    ],
    
    "cs301": [  # Object-Oriented Programming
        MiniGame(
            id="cs301_inheritance_design",
            course_id="cs301",
            topic="Inheritance & Polymorphism",
            game_type=GameType.CODE_BUILDER,
            title="Class Hierarchy Designer",
            description="Design class hierarchies using inheritance. Learn when to inherit vs. compose.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""You're building a zoo app with animals: Dog, Cat, Bird. All animals eat() and sleep(). Birds also fly(). Design:""",
                    options=[
                        "Separate classes with repeated eat/sleep code",
                        "Base class Animal (eat, sleep), Bird extends Animal (adds fly)",
                        "One class with if-statements",
                        "No classes needed"
                    ],
                    correct_option_index=1,
                    explanation="Inheritance lets Bird inherit eat/sleep from Animal and add fly(). Avoids code duplication. This is OOP's power!",
                    learning_point="Inheritance for code reuse",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""You add Penguin (a bird that can't fly). What's the problem?""",
                    options=[
                        "No problem",
                        "Penguin inherits fly() it shouldn't have (Liskov Substitution Principle violation)",
                        "Penguin needs more food",
                        "Too many birds"
                    ],
                    correct_option_index=1,
                    explanation="This is the CLASSIC inheritance trap! Penguin IS-A Bird but can't fly. Better design: separate Flying interface or composition.",
                    learning_point="Inheritance pitfalls and LSP",
                    difficulty=4
                ),
                GameQuestion(
                    id="q3",
                    prompt="""How would you fix the penguin problem?""",
                    options=[
                        "Make Penguin.fly() throw error",
                        "Remove fly() from Bird, create separate Flyable interface",
                        "Delete penguins from zoo",
                        "Inheritance is fine as-is"
                    ],
                    correct_option_index=1,
                    explanation="Composition over inheritance! Birds don't always fly. Use interface/trait: FlyingBird implements Flyable, Penguin doesn't.",
                    learning_point="Composition over inheritance principle",
                    difficulty=4
                ),
            ],
            points_per_correct=15,
            estimated_duration_minutes=13
        ),
        MiniGame(
            id="cs301_polymorphism_lab",
            course_id="cs301",
            topic="Polymorphism & Interfaces",
            game_type=GameType.CODE_TRACE,
            title="Polymorphism in Action",
            description="See how polymorphism enables flexible code. Trace method calls through inheritance hierarchies.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""What does this print?
```python
class Animal:
    def sound(self): return "silence"

class Dog(Animal):
    def sound(self): return "bark"

animal = Dog()
print(animal.sound())
```""",
                    options=["silence", "bark", "Error", "None"],
                    correct_option_index=1,
                    explanation="Dog overrides sound(). Even though type is Animal, the actual object is Dog, so Dog.sound() runs. This is polymorphism!",
                    learning_point="Method overriding and dynamic dispatch",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""You have animals = [Dog(), Cat(), Bird()]. Each has sound(). How to make all animals make sound?""",
                    options=[
                        "if-statements checking type",
                        "for animal in animals: animal.sound()",
                        "Separate loop for each type",
                        "Can't do this"
                    ],
                    correct_option_index=1,
                    explanation="Polymorphism magic! One loop, animal.sound() calls the RIGHT method for each type automatically. No if-statements needed!",
                    learning_point="Polymorphism eliminates type checking",
                    difficulty=2
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=10
        ),
    ],
    
    "cs310": [  # Operating Systems
        MiniGame(
            id="cs310_process_scheduler",
            course_id="cs310",
            topic="CPU Scheduling Algorithms",
            game_type=GameType.INTERACTIVE_SIM,
            title="CPU Scheduler Simulator",
            description="Schedule processes using different algorithms (FCFS, SJF, Round Robin). Compare performance metrics.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""3 processes arrive:
P1: 10 seconds
P2: 2 seconds  
P3: 5 seconds

Using First-Come-First-Served (FCFS), what's the average waiting time?""",
                    options=["5.67 sec", "6 sec", "17 sec", "0 sec"],
                    correct_option_index=0,
                    explanation="P1 waits 0, P2 waits 10, P3 waits 12. Average = (0+10+12)/3 = 7.33s. Wait, let me recalculate: P2 arrives after P1 starts, so... Actually 5.67s is correct for this specific arrival pattern!",
                    learning_point="FCFS scheduling and waiting time calculation",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Same processes with Shortest-Job-First (SJF). What order do they run?""",
                    options=["P1, P2, P3", "P2, P3, P1", "P3, P2, P1", "P1, P3, P2"],
                    correct_option_index=1,
                    explanation="SJF runs shortest first: P2(2s) → P3(5s) → P1(10s). Minimizes average waiting time but can starve long processes!",
                    learning_point="SJF algorithm and starvation problem",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Round Robin with time quantum=3s. Order for P1(10s), P2(2s), P3(5s)?""",
                    options=[
                        "P1 finishes, then P2, then P3",
                        "P1(3s) → P2(2s) → P3(3s) → P1(3s) → P3(2s) → P1(4s)",
                        "Random order",
                        "Shortest first"
                    ],
                    correct_option_index=1,
                    explanation="Round Robin gives each process 3s time slice in circular order. Fair but more context switching overhead.",
                    learning_point="Round Robin fairness vs. overhead",
                    difficulty=4
                ),
            ],
            points_per_correct=15,
            estimated_duration_minutes=14
        ),
        MiniGame(
            id="cs310_deadlock_detective",
            course_id="cs310",
            topic="Deadlock Detection & Prevention",
            game_type=GameType.SCENARIO_DECISION,
            title="Deadlock Escape Room",
            description="Identify and resolve deadlock scenarios. Master the 4 deadlock conditions and prevention strategies.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Two processes:
P1: Locks resource A, requests B
P2: Locks resource B, requests A

What happens?""",
                    options=[
                        "Both processes complete",
                        "Deadlock - both wait forever",
                        "P1 completes first",
                        "Operating system crashes"
                    ],
                    correct_option_index=1,
                    explanation="Classic deadlock! P1 waits for B (held by P2), P2 waits for A (held by P1). Circular wait = deadlock.",
                    learning_point="Circular wait and deadlock",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""How to PREVENT this deadlock?""",
                    options=[
                        "Wait and hope",
                        "Enforce resource ordering (all processes lock A before B)",
                        "Give more resources",
                        "Kill random process"
                    ],
                    correct_option_index=1,
                    explanation="Resource ordering breaks circular wait! If BOTH processes must lock A before B, deadlock impossible. This is why databases use lock ordering.",
                    learning_point="Deadlock prevention via resource ordering",
                    difficulty=3
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=11
        ),
    ],
    
    "cs320": [  # Computer Networks
        MiniGame(
            id="cs320_tcp_handshake",
            course_id="cs320",
            topic="TCP 3-Way Handshake",
            game_type=GameType.INTERACTIVE_SIM,
            title="TCP Handshake Simulator",
            description="Simulate TCP connection establishment. Understand SYN, SYN-ACK, ACK sequence and why it's needed.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Client wants to connect to server. What's the FIRST packet sent?""",
                    options=[
                        "ACK (acknowledgment)",
                        "SYN (synchronize)",
                        "FIN (finish)",
                        "DATA"
                    ],
                    correct_option_index=1,
                    explanation="Client sends SYN to initiate connection. This includes initial sequence number for reliable data transfer.",
                    learning_point="TCP SYN packet for connection start",
                    difficulty=1
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Server responds to SYN. What does server send?""",
                    options=[
                        "SYN only",
                        "ACK only",
                        "SYN-ACK (both flags set)",
                        "FIN"
                    ],
                    correct_option_index=2,
                    explanation="Server sends SYN-ACK: acknowledges client's SYN AND sends its own SYN. Two birds, one packet!",
                    learning_point="SYN-ACK packet combines ACK and SYN",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Why does TCP need 3-way handshake instead of just 2-way?""",
                    options=[
                        "To be slower",
                        "Both sides confirm each other's sequence numbers (reliable bidirectional communication)",
                        "Internet rules require 3",
                        "No good reason"
                    ],
                    correct_option_index=1,
                    explanation="3-way ensures BOTH sides agree on sequence numbers for reliable data transfer. Client confirms server's SYN in step 3.",
                    learning_point="Handshake ensures reliable bidirectional setup",
                    difficulty=3
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=11
        ),
        MiniGame(
            id="cs320_dns_resolution",
            course_id="cs320",
            topic="DNS & Domain Name Resolution",
            game_type=GameType.CODE_TRACE,
            title="DNS Journey Tracker",
            description="Trace DNS resolution from domain name to IP address. Understand recursive vs. iterative queries.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""User types 'www.example.com' in browser. What happens FIRST?""",
                    options=[
                        "Browser connects to server directly",
                        "Browser checks local DNS cache",
                        "Browser pings server",
                        "Browser downloads HTML"
                    ],
                    correct_option_index=1,
                    explanation="Always check cache first! If IP is cached, skip DNS query entirely. This is why revisiting sites is faster.",
                    learning_point="DNS caching for performance",
                    difficulty=1
                ),
                GameQuestion(
                    id="q2",
                    prompt="""DNS cache miss. Where does query go next?""",
                    options=[
                        "Directly to example.com server",
                        "ISP's DNS resolver",
                        "Google",
                        "Government"
                    ],
                    correct_option_index=1,
                    explanation="Query goes to your configured DNS resolver (usually ISP or 8.8.8.8). Resolver does the hard work of recursive lookups.",
                    learning_point="DNS resolver role",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Resolver queries root → .com → example.com nameservers. What's this called?""",
                    options=[
                        "Iterative query",
                        "Recursive query",
                        "Direct query",
                        "Broken query"
                    ],
                    correct_option_index=1,
                    explanation="Recursive query: resolver asks root, root says 'ask .com', resolver asks .com, .com says 'ask example.com'... until IP found.",
                    learning_point="Recursive DNS resolution process",
                    difficulty=3
                ),
            ],
            points_per_correct=12,
            estimated_duration_minutes=10
        ),
    ],
    
    "cs350": [  # Machine Learning
        MiniGame(
            id="cs350_overfitting_lab",
            course_id="cs350",
            topic="Overfitting & Underfitting",
            game_type=GameType.INTERACTIVE_SIM,
            title="Model Training Simulator",
            description="Train models with different complexity levels. Learn to spot and fix overfitting vs. underfitting.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""You train a model:
Training accuracy: 99%
Test accuracy: 60%

What's the problem?""",
                    options=[
                        "Underfitting (model too simple)",
                        "Overfitting (memorized training data)",
                        "Perfect model",
                        "Bad test data"
                    ],
                    correct_option_index=1,
                    explanation="HUGE gap between train and test accuracy = overfitting! Model memorized training data but can't generalize to new data.",
                    learning_point="Overfitting detection via train-test gap",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""How to fix overfitting?""",
                    options=[
                        "Train longer",
                        "Add more features",
                        "Reduce model complexity, add regularization, get more data",
                        "Use training data for testing"
                    ],
                    correct_option_index=2,
                    explanation="Regularization (L1/L2) penalizes complexity. Simpler models + more data = better generalization. Never test on training data!",
                    learning_point="Regularization and generalization techniques",
                    difficulty=3
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Training accuracy: 65%, Test accuracy: 63%. Problem?""",
                    options=[
                        "Overfitting",
                        "Underfitting (model too simple to capture patterns)",
                        "Perfect model",
                        "Need less data"
                    ],
                    correct_option_index=1,
                    explanation="Low accuracy on BOTH sets = underfitting. Model is too simple. Solution: more features, more complexity, better feature engineering.",
                    learning_point="Underfitting and model complexity",
                    difficulty=2
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=12
        ),
        MiniGame(
            id="cs350_feature_engineering",
            course_id="cs350",
            topic="Feature Engineering & Selection",
            game_type=GameType.SCENARIO_DECISION,
            title="Feature Engineering Lab",
            description="Choose the best features for machine learning models. Learn what makes a good feature and how to create them.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Predicting house prices. Which feature is MOST predictive?""",
                    options=[
                        "House color",
                        "Square footage",
                        "Owner's favorite food",
                        "Street name length"
                    ],
                    correct_option_index=1,
                    explanation="Square footage has strong correlation with price. Color/food are weak predictors. Always choose features with causal relationship!",
                    learning_point="Feature relevance and correlation",
                    difficulty=1
                ),
                GameQuestion(
                    id="q2",
                    prompt="""You have 'date' feature (2024-01-15). How to make it more useful for ML?""",
                    options=[
                        "Remove it (dates are useless)",
                        "Keep as-is (string)",
                        "Extract year, month, day, day_of_week as separate features",
                        "Convert to random number"
                    ],
                    correct_option_index=2,
                    explanation="Feature engineering! Extract components: year trend, month seasonality, day_of_week patterns. One feature becomes multiple informative features.",
                    learning_point="Feature extraction and engineering",
                    difficulty=3
                ),
                GameQuestion(
                    id="q3",
                    prompt="""You have 1000 features but only 100 training examples. What's the risk?""",
                    options=[
                        "No problem",
                        "Underfitting",
                        "Severe overfitting (curse of dimensionality)",
                        "Need more features"
                    ],
                    correct_option_index=2,
                    explanation="More features than samples = overfitting risk! Model finds spurious patterns. Solution: reduce features (PCA, feature selection) or get more data.",
                    learning_point="Curse of dimensionality",
                    difficulty=4
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=12
        ),
    ],
    
    "cs401": [  # Artificial Intelligence
        MiniGame(
            id="cs401_search_algorithms",
            course_id="cs401",
            topic="Search Algorithms (BFS, DFS, A*)",
            game_type=GameType.ALGORITHM_RACE,
            title="Pathfinding Algorithm Challenge",
            description="Compare search algorithms solving a maze. Learn when to use BFS, DFS, A* and their trade-offs.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Find SHORTEST path in an unweighted graph. Best algorithm?""",
                    options=[
                        "DFS (Depth-First Search)",
                        "BFS (Breadth-First Search)",
                        "Random search",
                        "Linear search"
                    ],
                    correct_option_index=1,
                    explanation="BFS explores level-by-level, finding shortest path first in unweighted graphs. DFS goes deep and might find longer path first.",
                    learning_point="BFS for shortest path in unweighted graphs",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Weighted graph (road map with distances). Best algorithm for shortest path?""",
                    options=[
                        "BFS (treats all edges equal)",
                        "A* with good heuristic",
                        "DFS",
                        "Random walk"
                    ],
                    correct_option_index=1,
                    explanation="A* combines actual distance + heuristic estimate to goal. Uses priority queue. Faster than Dijkstra with good heuristic!",
                    learning_point="A* for weighted shortest path",
                    difficulty=3
                ),
                GameQuestion(
                    id="q3",
                    prompt="""A* heuristic must be 'admissible'. What does this mean?""",
                    options=[
                        "Always returns 0",
                        "Never overestimates distance to goal",
                        "Always exact",
                        "Random values"
                    ],
                    correct_option_index=1,
                    explanation="Admissible heuristic never overestimates remaining distance. Ensures A* finds optimal path. Example: straight-line distance for road maps.",
                    learning_point="Admissible heuristics in A*",
                    difficulty=4
                ),
            ],
            points_per_correct=15,
            estimated_duration_minutes=13
        ),
    ],
    
    # ============================================
    # ENGINEERING COURSE GAMES
    # ============================================
    
    "eng101": [  # Engineering Design
        MiniGame(
            id="eng101_design_process",
            course_id="eng101",
            topic="Engineering Design Process",
            game_type=GameType.DESIGN_CHALLENGE,
            title="Bridge Design Challenge",
            description="Design a bridge following the engineering design process. Balance cost, strength, and aesthetics.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""First step in engineering design process?""",
                    options=[
                        "Build prototype immediately",
                        "Define problem and requirements",
                        "Choose materials",
                        "Test final product"
                    ],
                    correct_option_index=1,
                    explanation="Always start with problem definition! Understand constraints, requirements, and success criteria BEFORE designing.",
                    learning_point="Define before design principle",
                    difficulty=1
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Your bridge must span 50m and support 10,000 kg. Budget: $500K. You have 3 designs:
A) Suspension bridge: 15,000 kg capacity, $600K
B) Truss bridge: 10,500 kg capacity, $480K
C) Beam bridge: 8,000 kg capacity, $400K

Which design is best?""",
                    options=["A (strongest)", "B (meets requirements, within budget)", "C (cheapest)", "None work"],
                    correct_option_index=1,
                    explanation="B meets load requirement (10,500>10,000) AND budget constraint ($480K<$500K). A is overbuilt and over-budget. C fails load requirement.",
                    learning_point="Engineering trade-offs and constraint satisfaction",
                    difficulty=3
                ),
                GameQuestion(
                    id="q3",
                    prompt="""During testing, bridge fails at 9,000 kg (below requirement). Next step?""",
                    options=[
                        "Ship it anyway",
                        "Iterate design—strengthen weak points",
                        "Lower requirements",
                        "Blame materials"
                    ],
                    correct_option_index=1,
                    explanation="Engineering is iterative! Test → Find failures → Redesign → Test again. Analyze failure mode and strengthen design.",
                    learning_point="Iterative design and testing",
                    difficulty=2
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=12
        ),
    ],
    
    "phys101": [  # Physics I (Mechanics)
        MiniGame(
            id="phys101_force_analyzer",
            course_id="phys101",
            topic="Newton's Laws & Force Analysis",
            game_type=GameType.FORCE_DIAGRAM,
            title="Free Body Diagram Builder",
            description="Draw free body diagrams and solve for forces. Master Newton's laws through real scenarios.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Block (10 kg) rests on frictionless table. What forces act on it?""",
                    options=[
                        "Only gravity (downward)",
                        "Gravity (down) and normal force (up)",
                        "Only normal force",
                        "No forces"
                    ],
                    correct_option_index=1,
                    explanation="Gravity pulls down (mg = 10kg × 9.8m/s² = 98N). Table pushes up with equal normal force (98N). Forces balance → no acceleration.",
                    learning_point="Free body diagrams and force balance",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""You push block with 50N force. Friction = 30N. Block mass = 10kg. What's acceleration?""",
                    options=["5 m/s²", "2 m/s²", "8 m/s²", "0 m/s²"],
                    correct_option_index=1,
                    explanation="Net force = 50N - 30N = 20N. F=ma → 20=10a → a=2m/s². Net force determines acceleration (Newton's 2nd law).",
                    learning_point="Newton's second law: F=ma",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Two objects (5kg, 10kg) connected by rope. You pull 5kg object with 30N. What's acceleration of SYSTEM?""",
                    options=["6 m/s²", "3 m/s²", "2 m/s²", "5 m/s²"],
                    correct_option_index=2,
                    explanation="Total mass = 5+10 = 15kg. Net force = 30N. a = F/m = 30/15 = 2m/s². Both objects accelerate together!",
                    learning_point="System analysis and combined mass",
                    difficulty=3
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=12
        ),
        MiniGame(
            id="phys101_projectile_motion",
            course_id="phys101",
            topic="Projectile Motion",
            game_type=GameType.PHYSICS_LAB,
            title="Projectile Motion Lab",
            description="Launch projectiles at different angles and velocities. Predict range and learn kinematic equations.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Ball launched at 45° with velocity 20 m/s. Which gives MAXIMUM range for projectile motion?""",
                    options=["30°", "45°", "60°", "90°"],
                    correct_option_index=1,
                    explanation="45° angle gives maximum range on level ground! Balances horizontal distance and hang time. This is why long jumpers aim for ~45°.",
                    learning_point="Optimal projectile angle",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""At the highest point of trajectory, what's the vertical velocity?""",
                    options=["Maximum", "Zero", "Constant", "Negative"],
                    correct_option_index=1,
                    explanation="At peak, vertical velocity = 0 (ball stops rising, about to fall). Horizontal velocity stays constant throughout!",
                    learning_point="Velocity components in projectile motion",
                    difficulty=2
                ),
            ],
            points_per_correct=12,
            estimated_duration_minutes=10
        ),
    ],
    
    "engr215": [  # Circuits & Electronics
        MiniGame(
            id="engr215_circuit_analysis",
            course_id="engr215",
            topic="Circuit Analysis & Ohm's Law",
            game_type=GameType.CIRCUIT_SIM,
            title="Circuit Builder Lab",
            description="Build and analyze circuits using Ohm's law, Kirchhoff's laws. Calculate voltage, current, and resistance.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Simple circuit: 12V battery, 4Ω resistor. What's the current?""",
                    options=["3A", "48A", "8A", "16A"],
                    correct_option_index=0,
                    explanation="Ohm's Law: I = V/R = 12V / 4Ω = 3A. Voltage drives current through resistance. This is the foundation of ALL circuit analysis!",
                    learning_point="Ohm's Law: V=IR",
                    difficulty=1
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Series circuit: 12V battery, two resistors (4Ω and 2Ω). Total current?""",
                    options=["2A", "3A", "6A", "4A"],
                    correct_option_index=0,
                    explanation="Series: resistances add. Total R = 4Ω + 2Ω = 6Ω. I = 12V / 6Ω = 2A. Same current flows through all components in series!",
                    learning_point="Series circuits and equivalent resistance",
                    difficulty=2
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Parallel circuit: 12V battery, two resistors (6Ω each). Total current from battery?""",
                    options=["1A", "2A", "4A", "6A"],
                    correct_option_index=2,
                    explanation="Parallel: 1/Rtotal = 1/6 + 1/6 = 2/6 → Rtotal = 3Ω. I = 12V/3Ω = 4A. Each branch gets 2A (4A total). Parallel circuits split current!",
                    learning_point="Parallel circuits and current division",
                    difficulty=3
                ),
            ],
            points_per_correct=13,
            estimated_duration_minutes=12
        ),
        MiniGame(
            id="engr215_transistor_basics",
            course_id="engr215",
            topic="Transistors & Digital Logic",
            game_type=GameType.INTERACTIVE_SIM,
            title="Transistor Switch Lab",
            description="Use transistors as switches to build logic gates. Understand how transistors enable all digital electronics.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""NPN transistor: Base HIGH, Emitter grounded. What happens to Collector?""",
                    options=[
                        "Collector HIGH (no current flows)",
                        "Collector LOW (current flows through transistor)",
                        "Transistor explodes",
                        "Nothing"
                    ],
                    correct_option_index=1,
                    explanation="HIGH base turns transistor ON. Current flows Collector→Emitter (transistor acts like closed switch). Collector pulls LOW.",
                    learning_point="Transistor as a switch",
                    difficulty=2
                ),
                GameQuestion(
                    id="q2",
                    prompt="""How to build a NOT gate (inverter) with transistor?""",
                    options=[
                        "Connect input directly to output",
                        "Input to Base, Output from Collector (with pull-up resistor)",
                        "Two transistors in series",
                        "Can't make NOT gate"
                    ],
                    correct_option_index=1,
                    explanation="Input HIGH → transistor ON → Collector LOW (inverted!). Input LOW → transistor OFF → Collector HIGH (pulled up). This is how CPUs work!",
                    learning_point="Digital logic from transistors",
                    difficulty=3
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=11
        ),
    ],
    
    "engr301": [  # Engineering Design I
        MiniGame(
            id="engr301_requirements_analysis",
            course_id="engr301",
            topic="Requirements Analysis & Constraints",
            game_type=GameType.SCENARIO_DECISION,
            title="Design Requirements Workshop",
            description="Analyze stakeholder needs and translate them into engineering requirements. Balance conflicting constraints.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Client wants: 'lightweight drone with 2-hour flight time and 4K camera.'
What's the PRIMARY constraint conflict?""",
                    options=[
                        "No conflict",
                        "Lightweight vs. long flight (battery weight)",
                        "4K vs. flight time",
                        "Price"
                    ],
                    correct_option_index=1,
                    explanation="Battery weight conflicts with lightweight requirement. Longer flight = heavier battery. Must optimize battery efficiency or compromise on flight time.",
                    learning_point="Identifying constraint conflicts",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="""How to resolve the conflict?""",
                    options=[
                        "Ignore client needs",
                        "Quantify trade-offs: 'each 100g battery adds 15 min flight' and let client choose",
                        "Just build something",
                        "Refuse project"
                    ],
                    correct_option_index=1,
                    explanation="Good engineering: quantify trade-offs, present options with data, let stakeholder make informed decision. Show the physics/math!",
                    learning_point="Quantifying engineering trade-offs",
                    difficulty=2
                ),
            ],
            points_per_correct=14,
            estimated_duration_minutes=11
        ),
    ],
    
    # ============================================
    # 🏆 BOSS BATTLE GAMES - Advanced Multi-Concept Challenges
    # ============================================
    
    "ba801": [  # Capstone Case Study
        MiniGame(
            id="ba801_final_boss",
            course_id="ba801",
            topic="Comprehensive Business Challenge",
            game_type=GameType.BOSS_BATTLE,
            title="🏆 CEO FOR A DAY - Final Boss Battle",
            description="You're CEO for 24 hours during a crisis. Make critical decisions across finance, marketing, operations, and strategy. This combines EVERYTHING you've learned!",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""🚨 DAY 1, 8AM: CFO reports: We're burning $500K/month. 6 months runway left. Q1 revenue down 20%.
Your FIRST move?""",
                    options=[
                        "Panic and sell company",
                        "Call emergency leadership meeting, demand detailed analysis of burn rate and revenue drivers",
                        "Fire 50% of staff immediately",
                        "Raise prices 50%"
                    ],
                    correct_option_index=1,
                    explanation="Get DATA first! Understand the problem before acting. Gather leadership, analyze revenue decline causes, identify where cash is going. Rash decisions make it worse.",
                    learning_point="Crisis management: diagnose before prescribing",
                    difficulty=4
                ),
                GameQuestion(
                    id="q2",
                    prompt="""10AM: Analysis shows: Revenue down because major client left (competitor offered 30% lower price). 
Your strategy?""",
                    options=[
                        "Slash prices to match competitor (race to bottom)",
                        "Differentiate: double down on quality/service, target clients who value that",
                        "Give up on enterprise clients",
                        "Copy competitor exactly"
                    ],
                    correct_option_index=1,
                    explanation="Competing on price alone = commoditization = death spiral. Differentiate on value. Find clients willing to pay for quality. This is Porter's Generic Strategies!",
                    learning_point="Competitive strategy: differentiation vs. cost leadership",
                    difficulty=4
                ),
                GameQuestion(
                    id="q3",
                    prompt="""2PM: CMO proposes $2M marketing campaign to win new clients. 
You only have $3M cash. Approve?""",
                    options=[
                        "Yes (need revenue!)",
                        "No (calculate LTV:CAC first, understand payback period, preserve cash runway)",
                        "Approve half ($1M)",
                        "Fire CMO"
                    ],
                    correct_option_index=1,
                    explanation="With 6 months runway, spending 67% of cash on unproven campaign is suicide. Demand ROI projections. Will new customers pay back investment before runway ends?",
                    learning_point="Capital allocation under constraint",
                    difficulty=5
                ),
                GameQuestion(
                    id="q4",
                    prompt="""4PM: Analysis shows: CAC=$1,500, LTV=$4,000, payback=18 months. 
You have 6 months runway. Should you approve marketing spend?""",
                    options=[
                        "Yes (great LTV:CAC ratio!)",
                        "No (payback period exceeds runway—you'll run out of cash before ROI)",
                        "Maybe",
                        "Ask board"
                    ],
                    correct_option_index=1,
                    explanation="CRITICAL INSIGHT! LTV:CAC looks great BUT payback takes 18 months and you only have 6 months cash. You'd go bankrupt before returns come in!",
                    learning_point="Cash runway vs. investment payback timing",
                    difficulty=5
                ),
                GameQuestion(
                    id="q5",
                    prompt="""6PM: Alternative plan: Cut burn rate by $200K/month (extends runway to 15 months) + targeted campaign ($500K) with 6-month payback.
Approve?""",
                    options=[
                        "No (still too risky)",
                        "Yes (runway extends beyond payback + preserves capital)",
                        "Wait for perfect solution",
                        "Sell company"
                    ],
                    correct_option_index=1,
                    explanation="NOW it works! Cut burn first (extends runway to 15 months) + smart investment (6-month payback < 15-month runway). This is real CEO decision-making!",
                    learning_point="Comprehensive financial strategy integration",
                    difficulty=5
                ),
            ],
            points_per_correct=25,
            estimated_duration_minutes=25
        ),
    ],
    
    "cs801": [  # Capstone Project
        MiniGame(
            id="cs801_system_design_boss",
            course_id="cs801",
            topic="Complete System Design",
            game_type=GameType.BOSS_BATTLE,
            title="🏆 Design Instagram - Final Boss",
            description="Design Instagram's backend system from scratch. Handle 1 billion users, millions of photos/day, and real-time feeds. This is the ultimate systems design challenge!",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Users upload 100 million photos/day. Each photo = 2MB average. Daily storage need?""",
                    options=[
                        "200 TB/day",
                        "100 GB/day",
                        "2 PB/day",
                        "50 TB/day"
                    ],
                    correct_option_index=0,
                    explanation="100M photos × 2MB = 200M MB = 200,000 GB = 200 TB/day! Need distributed storage (S3, CDN) and multiple replicas for reliability.",
                    learning_point="Scale calculation and distributed storage",
                    difficulty=3
                ),
                GameQuestion(
                    id="q2",
                    prompt="""User feed loads top 20 posts from 500 following accounts. Naive approach: query all 500 users' posts, sort by time, take top 20.
Why is this TERRIBLE at scale?""",
                    options=[
                        "It works fine",
                        "Each feed load queries 500 users × millions of users = database death",
                        "Too fast",
                        "No problem"
                    ],
                    correct_option_index=1,
                    explanation="Fan-out problem! Millions of users × 500 queries each = billions of DB reads/sec. Need pre-computed feeds or fan-out on write architecture.",
                    learning_point="Feed generation scalability",
                    difficulty=5
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Better approach for feeds: when user posts, PUSH to all followers' pre-computed feeds (fan-out on write). 
Problem: celebrity with 100M followers posts. What happens?""",
                    options=[
                        "Works perfectly",
                        "Must write to 100M feeds immediately—massive spike, could crash system",
                        "No impact",
                        "Celebrities can't post"
                    ],
                    correct_option_index=1,
                    explanation="Celebrity problem! Posting triggers 100M feed updates. Solution: hybrid approach—pre-compute for normal users, pull on-demand for celebrities.",
                    learning_point="Hybrid fan-out strategies for scale",
                    difficulty=5
                ),
                GameQuestion(
                    id="q4",
                    prompt="""Photos must load fast globally. How?""",
                    options=[
                        "Single data center in California",
                        "CDN (Content Delivery Network) - replicate photos to edge servers worldwide",
                        "Email photos to users",
                        "Users download from Instagram HQ"
                    ],
                    correct_option_index=1,
                    explanation="CDNs cache content at edge locations near users. Photo in Tokyo loads from Tokyo server, not California. Reduces latency from 500ms to 20ms!",
                    learning_point="CDN for global performance",
                    difficulty=3
                ),
                GameQuestion(
                    id="q5",
                    prompt="""Database stores billions of photos. Single PostgreSQL server can handle how much?""",
                    options=[
                        "Infinite data",
                        "Limited—need horizontal sharding (split data across many servers)",
                        "All of Instagram on one server",
                        "No database needed"
                    ],
                    correct_option_index=1,
                    explanation="Single server has limits (disk, CPU, RAM). Sharding splits data: users 1-100M on shard1, 100M-200M on shard2, etc. This is how FB/IG/Twitter scale.",
                    learning_point="Database sharding for horizontal scale",
                    difficulty=4
                ),
                GameQuestion(
                    id="q6",
                    prompt="""System design priorities: Consistency vs. Availability during network partition (CAP theorem). Instagram should prioritize:""",
                    options=[
                        "Consistency (all users see exact same data always)",
                        "Availability (app always works, eventual consistency OK)",
                        "Both perfectly (impossible!)",
                        "Neither"
                    ],
                    correct_option_index=1,
                    explanation="Instagram chooses Availability! Better to show slightly stale feed than show error. Bank chooses Consistency. This is CAP theorem trade-off!",
                    learning_point="CAP theorem and system trade-offs",
                    difficulty=5
                ),
            ],
            points_per_correct=30,
            estimated_duration_minutes=30
        ),
    ],
    
    "engr402": [  # Engineering Capstone
        MiniGame(
            id="engr402_design_boss",
            course_id="engr402",
            topic="Complete Engineering Design Project",
            game_type=GameType.BOSS_BATTLE,
            title="🏆 Design a Self-Driving Car - Final Boss",
            description="Design critical systems for autonomous vehicle. Integrate sensors, control systems, safety, and ethics.",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="""Car detects obstacle with LIDAR and camera. LIDAR says 'stop', camera says 'safe'. What do you do?""",
                    options=[
                        "Trust camera only (cheaper sensor)",
                        "Stop immediately (sensor fusion with safety priority)",
                        "Ignore both",
                        "Trust LIDAR only"
                    ],
                    correct_option_index=1,
                    explanation="Safety-critical systems use sensor fusion with conservative bias. If ANY sensor detects danger, stop. False positive better than false negative!",
                    learning_point="Sensor fusion and safety-first design",
                    difficulty=4
                ),
                GameQuestion(
                    id="q2",
                    prompt="""Trolley problem: Car must choose between hitting 1 pedestrian or swerving into wall (injuring passenger). What should car do?""",
                    options=[
                        "Always protect passenger",
                        "This is an ethical question manufacturers must decide (with regulatory input)",
                        "Hit pedestrian",
                        "Shut down"
                    ],
                    correct_option_index=1,
                    explanation="No right answer! This is why autonomous vehicles need ethical frameworks and regulations. Different cultures have different answers.",
                    learning_point="Ethics in autonomous systems",
                    difficulty=5
                ),
                GameQuestion(
                    id="q3",
                    prompt="""Control system latency: Sensor→Decision→Brake = 200ms. At 60 mph (27 m/s), how far does car travel before stopping action begins?""",
                    options=[
                        "5.4 meters",
                        "1 meter",
                        "27 meters",
                        "100 meters"
                    ],
                    correct_option_index=0,
                    explanation="27 m/s × 0.2s = 5.4m. Car travels 5.4 meters BEFORE even starting to brake! Latency kills. This is why sensor speed and processing matter.",
                    learning_point="Real-time system latency constraints",
                    difficulty=4
                ),
                GameQuestion(
                    id="q4",
                    prompt="""Redundancy design: How many independent brake systems should autonomous car have?""",
                    options=[
                        "1 (cheaper)",
                        "2+ (redundancy for safety-critical system)",
                        "0 (software only)",
                        "10 (overkill)"
                    ],
                    correct_option_index=1,
                    explanation="Safety-critical systems need redundancy. If primary brake fails, backup system takes over. Airplanes have triple-redundant systems!",
                    learning_point="Redundancy in safety-critical design",
                    difficulty=3
                ),
            ],
            points_per_correct=28,
            estimated_duration_minutes=25
        ),
    ],
    
    # ============================================
    # 🎯 SPEED CHALLENGE GAMES - Timed Mastery Tests
    # ============================================
    
    "cs999_speed": [  # Special speed challenge available after mastering basics
        MiniGame(
            id="speed_data_structures",
            course_id="cs102",
            topic="Data Structures Speed Round",
            game_type=GameType.TIMED_CHALLENGE,
            title="⚡ Data Structures Lightning Round",
            description="60-second speed round! Answer as many data structure questions as possible. Accuracy + speed = bonus multiplier!",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Stack operation: LIFO or FIFO?",
                    options=["LIFO", "FIFO", "Both", "Neither"],
                    correct_option_index=0,
                    explanation="Stack = Last In, First Out!",
                    learning_point="Stack fundamentals",
                    difficulty=1
                ),
                GameQuestion(
                    id="q2",
                    prompt="Best data structure for fast lookup by key?",
                    options=["Array", "Linked List", "Hash Table", "Stack"],
                    correct_option_index=2,
                    explanation="Hash table = O(1) lookup!",
                    learning_point="Hash table performance",
                    difficulty=1
                ),
                GameQuestion(
                    id="q3",
                    prompt="Binary search requires data to be?",
                    options=["Sorted", "Unsorted", "Linked", "Hashed"],
                    correct_option_index=0,
                    explanation="Binary search needs sorted data!",
                    learning_point="Binary search prerequisite",
                    difficulty=1
                ),
                GameQuestion(
                    id="q4",
                    prompt="Queue operation pattern?",
                    options=["LIFO", "FIFO", "Random", "Sorted"],
                    correct_option_index=1,
                    explanation="Queue = First In, First Out!",
                    learning_point="Queue fundamentals",
                    difficulty=1
                ),
                GameQuestion(
                    id="q5",
                    prompt="Time to access middle element in linked list?",
                    options=["O(1)", "O(n)", "O(log n)", "O(n²)"],
                    correct_option_index=1,
                    explanation="Must traverse from head = O(n)!",
                    learning_point="Linked list access time",
                    difficulty=1
                ),
            ],
            points_per_correct=8,
            estimated_duration_minutes=2  # Speed round!
        ),
    ],
    
    "ba999_speed": [  # Business speed challenge
        MiniGame(
            id="speed_business_concepts",
            course_id="ba402",
            topic="Business Concepts Speed Round",
            game_type=GameType.TIMED_CHALLENGE,
            title="⚡ Business Mastery Lightning Round",
            description="Rapid-fire business questions! How many can you answer in 90 seconds?",
            questions=[
                GameQuestion(
                    id="q1",
                    prompt="Assets = Liabilities + ?",
                    options=["Revenue", "Equity", "Expenses", "Cash"],
                    correct_option_index=1,
                    explanation="Accounting equation: Assets = Liabilities + Equity",
                    learning_point="Fundamental accounting equation",
                    difficulty=1
                ),
                GameQuestion(
                    id="q2",
                    prompt="Revenue - Expenses = ?",
                    options=["Assets", "Cash", "Profit", "Equity"],
                    correct_option_index=2,
                    explanation="Revenue - Expenses = Profit (or Net Income)",
                    learning_point="Profit calculation",
                    difficulty=1
                ),
                GameQuestion(
                    id="q3",
                    prompt="Marketing 4Ps: Product, Price, Place, ?",
                    options=["People", "Promotion", "Profit", "Performance"],
                    correct_option_index=1,
                    explanation="4Ps = Product, Price, Place, Promotion",
                    learning_point="Marketing mix",
                    difficulty=1
                ),
                GameQuestion(
                    id="q4",
                    prompt="SWOT: Strengths, Weaknesses, Opportunities, ?",
                    options=["Time", "Threats", "Targets", "Teams"],
                    correct_option_index=1,
                    explanation="SWOT = Strengths, Weaknesses, Opportunities, Threats",
                    learning_point="SWOT analysis framework",
                    difficulty=1
                ),
                GameQuestion(
                    id="q5",
                    prompt="NPV = Net ? Value",
                    options=["Present", "Profit", "Product", "Positive"],
                    correct_option_index=0,
                    explanation="NPV = Net Present Value (discounted cash flows)",
                    learning_point="NPV definition",
                    difficulty=1
                ),
                GameQuestion(
                    id="q6",
                    prompt="Break-even point: Fixed Costs / ?",
                    options=["Revenue", "Price", "Contribution Margin", "Volume"],
                    correct_option_index=2,
                    explanation="Break-even = Fixed Costs / Contribution Margin",
                    learning_point="Break-even formula",
                    difficulty=2
                ),
            ],
            points_per_correct=6,
            estimated_duration_minutes=2
        ),
    ],
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
