"""
Tutorial Mini-Games for New Player Onboarding

Interactive games that teach core mechanics while being fun and engaging.
Designed for zero-knowledge players to learn the game within 5 minutes.
"""

from __future__ import annotations
from typing import List, Dict, Any
from pydantic import BaseModel


class TutorialGameQuestion(BaseModel):
    """Single question in a tutorial game"""
    id: str
    text: str
    choices: List[Dict[str, Any]]  # [{id, text, correct, explanation}]
    hint: str
    learning_objective: str


class TutorialGame(BaseModel):
    """A tutorial mini-game teaching one core mechanic"""
    id: str
    title: str
    description: str
    mascot_dialogue: str  # What the guide character says
    game_type: str
    questions: List[TutorialGameQuestion]
    points_reward: int
    estimated_duration_seconds: int
    teaches_mechanic: str  # e.g., "financial_planning", "time_management"


# =============================================
# Tutorial Game Definitions
# =============================================

TUTORIAL_GAMES: Dict[str, TutorialGame] = {
    "tutorial_welcome": TutorialGame(
        id="tutorial_welcome",
        title="🎓 Welcome to College!",
        description="Learn the basics of managing your college life",
        mascot_dialogue="Hey there! I'm Sprint, your guide. Let's learn how this game works! Choose wisely—your choices have real consequences.",
        game_type="scenario_decision",
        teaches_mechanic="basic_choices",
        points_reward=50,
        estimated_duration_seconds=60,
        questions=[
            TutorialGameQuestion(
                id="t_welcome_q1",
                text="You just arrived at college with $5,000 in your account. What should you do FIRST?",
                hint="Emergency funds are important, but you need immediate essentials too.",
                learning_objective="Understand balance between preparation and immediate needs",
                choices=[
                    {
                        "id": "a",
                        "text": "Spend it all on a gaming PC and new clothes to impress people",
                        "correct": False,
                        "explanation": "Ouch! 😅 While having nice things is tempting, blowing your entire budget leaves you vulnerable to emergencies. Try to balance wants vs needs."
                    },
                    {
                        "id": "b",
                        "text": "Put all of it in savings and live on ramen noodles",
                        "correct": False,
                        "explanation": "Saving is good, but extreme! 🍜 You need some baseline quality of life. Balance is key."
                    },
                    {
                        "id": "c",
                        "text": "Set aside $1,000 emergency fund, budget the rest for semester needs",
                        "correct": True,
                        "explanation": "Perfect! 🎯 You're balancing safety (emergency fund) with practical needs. This is smart money management."
                    },
                    {
                        "id": "d",
                        "text": "Invest it all in crypto—you heard it's going up!",
                        "correct": False,
                        "explanation": "Yikes! 📉 Never invest money you can't afford to lose, especially when it's your only cash. Keep emergency funds liquid and safe."
                    }
                ]
            )
        ]
    ),
    
    "tutorial_time_management": TutorialGame(
        id="tutorial_time_management",
        title="⏰ Time is Everything",
        description="Learn how to balance classes, work, and life",
        mascot_dialogue="College is about balance. Too much work? Burnout. Too much play? Fail out. Let's learn to manage your weekly time!",
        game_type="scenario_decision",
        teaches_mechanic="time_management",
        points_reward=50,
        estimated_duration_seconds=90,
        questions=[
            TutorialGameQuestion(
                id="t_time_q1",
                text="You have 60 hours per week for classes, work, and activities. Your classes take 20 hours. What's a balanced schedule?",
                hint="Most students work 10-15 hours and save time for wellbeing.",
                learning_objective="Understand the 60-hour weekly time budget",
                choices=[
                    {
                        "id": "a",
                        "text": "30-hour part-time job + 10 hours activities",
                        "correct": False,
                        "explanation": "This is 60 hours total—max capacity! 😰 You'll burn out fast with zero buffer. Leave some breathing room."
                    },
                    {
                        "id": "b",
                        "text": "15-hour job + 15 hours activities + 10 hours buffer",
                        "correct": True,
                        "explanation": "Great balance! 👍 You have income, social life, and recovery time. This is sustainable."
                    },
                    {
                        "id": "c",
                        "text": "No job, 40 hours of activities (party mode)",
                        "correct": False,
                        "explanation": "Living the dream, but... 💸 How will you pay for things? You need income unless you have family support."
                    },
                    {
                        "id": "d",
                        "text": "40-hour job, no activities",
                        "correct": False,
                        "explanation": "You're overloaded! ⚠️ This is unsustainable. You'll burn out and your grades will tank. Balance is crucial."
                    }
                ]
            ),
            TutorialGameQuestion(
                id="t_time_q2",
                text="It's Week 3 and you're already feeling stressed. What should you do?",
                hint="Stress management is critical. Don't wait until it's too late.",
                learning_objective="Learn to recognize and respond to stress signals",
                choices=[
                    {
                        "id": "a",
                        "text": "Push through—complaining is for quitters",
                        "correct": False,
                        "explanation": "Not smart! 😤 Ignoring stress leads to burnout, which tanks your GPA and happiness. Seek help early."
                    },
                    {
                        "id": "b",
                        "text": "Reduce work hours or drop an activity temporarily",
                        "correct": True,
                        "explanation": "Wise choice! 🧠 Adjusting your load early prevents bigger problems. Use emergency changes when needed."
                    },
                    {
                        "id": "c",
                        "text": "Start binge-drinking energy drinks and all-nighters",
                        "correct": False,
                        "explanation": "Recipe for disaster! ☠️ This damages your health stat and makes stress worse long-term."
                    },
                    {
                        "id": "d",
                        "text": "Drop out of college—it's too hard",
                        "correct": False,
                        "explanation": "Way too drastic! 😨 Stress is manageable with small adjustments. Don't give up—adjust your load instead."
                    }
                ]
            )
        ]
    ),
    
    "tutorial_financial_planning": TutorialGame(
        id="tutorial_financial_planning",
        title="💰 Show Me the Money",
        description="Master the basics of budgeting and avoiding debt traps",
        mascot_dialogue="Money management makes or breaks your college experience. Let's learn to budget smart!",
        game_type="budget_challenge",
        teaches_mechanic="financial_planning",
        points_reward=75,
        estimated_duration_seconds=120,
        questions=[
            TutorialGameQuestion(
                id="t_finance_q1",
                text="Your tuition is $8,000 this semester, but you only have $2,000. What do you do?",
                hint="Loans aren't evil—they're tools. Use them wisely.",
                learning_objective="Understand when and how to borrow strategically",
                choices=[
                    {
                        "id": "a",
                        "text": "Take $6,000 in subsidized loans (0% interest while in school)",
                        "correct": True,
                        "explanation": "Smart borrowing! ✅ Subsidized loans don't accrue interest in school, so this is the cheapest option. Pay it back after graduation."
                    },
                    {
                        "id": "b",
                        "text": "Drop out this semester and work to save up $8,000",
                        "correct": False,
                        "explanation": "Too extreme! 😬 You'd lose momentum and time. Strategic borrowing is better than delaying education."
                    },
                    {
                        "id": "c",
                        "text": "Max out a credit card at 22% APR",
                        "correct": False,
                        "explanation": "Terrible idea! 💳 Credit card interest is way higher than student loans. This will cost you thousands extra."
                    },
                    {
                        "id": "d",
                        "text": "Ask a loan shark for $6,000",
                        "correct": False,
                        "explanation": "Never! 🚫 This is illegal and dangerous. Use legitimate financial aid options."
                    }
                ]
            ),
            TutorialGameQuestion(
                id="t_finance_q2",
                text="You borrowed $20,000 in loans. After graduation, what's your repayment strategy?",
                hint="Income-driven plans can help if you're struggling financially.",
                learning_objective="Understand loan repayment options",
                choices=[
                    {
                        "id": "a",
                        "text": "Ignore the bills—they'll forget about me eventually",
                        "correct": False,
                        "explanation": "NEVER! 🚨 Student loans don't disappear. They'll garnish wages, tank your credit, and haunt you forever. Always pay."
                    },
                    {
                        "id": "b",
                        "text": "Pay only minimum required, invest extra cash elsewhere",
                        "correct": False,
                        "explanation": "Risky! ⚠️ Loan interest compounds. Unless you're getting >6% guaranteed returns, pay down debt faster."
                    },
                    {
                        "id": "c",
                        "text": "Use income-driven repayment if salary is low, standard if high",
                        "correct": True,
                        "explanation": "Perfect strategy! 🎯 Match repayment to your income level. This prevents financial strain while paying efficiently."
                    },
                    {
                        "id": "d",
                        "text": "Pay it all off immediately by selling your car and furniture",
                        "correct": False,
                        "explanation": "Too aggressive! 😅 You need basic assets to function. Pay aggressively, but don't sacrifice essentials."
                    }
                ]
            )
        ]
    ),
    
    "tutorial_gpa_matters": TutorialGame(
        id="tutorial_gpa_matters",
        title="📚 GPA: Your Future Currency",
        description="Discover why your grades actually matter (hint: it's not just a number)",
        mascot_dialogue="GPA opens doors—scholarships, internships, grad school. Let's see why it matters!",
        game_type="scenario_decision",
        teaches_mechanic="gpa_importance",
        points_reward=50,
        estimated_duration_seconds=90,
        questions=[
            TutorialGameQuestion(
                id="t_gpa_q1",
                text="You have a 2.3 GPA. What opportunities are you LOSING access to?",
                hint="Many programs require 3.0+ minimum GPA.",
                learning_objective="Understand GPA thresholds and their consequences",
                choices=[
                    {
                        "id": "a",
                        "text": "Nothing—GPA doesn't matter in the real world",
                        "correct": False,
                        "explanation": "Wrong! 📉 GPA affects scholarships, internships, grad school, and even some job opportunities. It matters more than you think."
                    },
                    {
                        "id": "b",
                        "text": "Most competitive internships, many scholarships, grad school",
                        "correct": True,
                        "explanation": "Exactly! 🎯 Below 3.0 locks you out of many opportunities. Protect your GPA—it's an investment."
                    },
                    {
                        "id": "c",
                        "text": "Only grad school, nothing else",
                        "correct": False,
                        "explanation": "Too narrow! 🚪 GPA affects scholarships (money!), internships (experience), and your first job search too."
                    },
                    {
                        "id": "d",
                        "text": "Just bragging rights with friends",
                        "correct": False,
                        "explanation": "Way more important! 💼 GPA has real financial consequences through scholarships and career opportunities."
                    }
                ]
            )
        ]
    ),
    
    "tutorial_emergency_planning": TutorialGame(
        id="tutorial_emergency_planning",
        title="🚨 When Plans Go Wrong",
        description="Learn how to handle unexpected life events without derailing your semester",
        mascot_dialogue="Life doesn't always go according to plan. Here's how to handle emergencies!",
        game_type="scenario_decision",
        teaches_mechanic="emergency_management",
        points_reward=50,
        estimated_duration_seconds=75,
        questions=[
            TutorialGameQuestion(
                id="t_emergency_q1",
                text="Week 8: Your roommate moves out suddenly and rent doubles. You have 2 emergency tokens. What do?",
                hint="Emergency tokens let you change housing/job mid-semester, but they're limited.",
                learning_objective="Understand emergency tokens and when to use them",
                choices=[
                    {
                        "id": "a",
                        "text": "Use emergency token to find cheaper housing immediately",
                        "correct": True,
                        "explanation": "Smart! ✅ Housing cost affects every month. Using a token here prevents financial spiral. This is what tokens are for."
                    },
                    {
                        "id": "b",
                        "text": "Tough it out—pay double rent and go into debt",
                        "correct": False,
                        "explanation": "Ouch! 💸 This accumulates debt fast. Emergency tokens exist for exactly this situation—use them!"
                    },
                    {
                        "id": "c",
                        "text": "Drop out of school to avoid the rent crisis",
                        "correct": False,
                        "explanation": "Way too drastic! 😨 Use your emergency token. Don't let housing derail your entire education."
                    },
                    {
                        "id": "d",
                        "text": "Work 60 hours/week to afford it",
                        "correct": False,
                        "explanation": "Unrealistic! ⚠️ You'd exceed the 60-hour weekly budget and crash academically. Use the emergency system."
                    }
                ]
            )
        ]
    ),
    
    "tutorial_final_challenge": TutorialGame(
        id="tutorial_final_challenge",
        title="🎯 Your First Semester Plan",
        description="Put it all together—plan your entire first semester!",
        mascot_dialogue="You've learned the basics! Now let's plan your FIRST SEMESTER. Choose your housing, job, and activities. Make it count!",
        game_type="case_study",
        teaches_mechanic="semester_planning",
        points_reward=100,
        estimated_duration_seconds=180,
        questions=[
            TutorialGameQuestion(
                id="t_final_q1",
                text="Choose your housing for Semester 1. You have $5,000 starting balance.",
                hint="Cheaper housing = more savings, but impacts happiness.",
                learning_objective="Understand housing trade-offs",
                choices=[
                    {
                        "id": "a",
                        "text": "Campus Dorm ($900/mo): Safe, social, convenient",
                        "correct": True,
                        "explanation": "Solid choice! 🏠 Dorms are the default for first semester. You'll meet people and stay close to campus."
                    },
                    {
                        "id": "b",
                        "text": "Budget Apartment ($600/mo): Cheaper, but isolating",
                        "correct": True,
                        "explanation": "Frugal! 💵 You'll save money, but might miss social opportunities. Trade-offs are real."
                    },
                    {
                        "id": "c",
                        "text": "Luxury Apartment ($1,800/mo): Amazing, but expensive",
                        "correct": False,
                        "explanation": "Can't afford it! 💸 You'd burn through your savings in 3 months. Live within your means."
                    },
                    {
                        "id": "d",
                        "text": "Live in your car to save money",
                        "correct": False,
                        "explanation": "Not viable! 🚗 This would destroy your health and happiness stats. Housing is non-negotiable."
                    }
                ]
            ),
            TutorialGameQuestion(
                id="t_final_q2",
                text="Now choose a part-time job. Remember: you have 60 hours/week total, classes take ~20-25 hours.",
                hint="Balance income needs vs time availability.",
                learning_objective="Understand work-life balance",
                choices=[
                    {
                        "id": "a",
                        "text": "Campus Library (10 hrs/week, $15/hr): Light, flexible",
                        "correct": True,
                        "explanation": "Perfect starter job! 📚 Low hours, decent pay, on-campus convenience. Leaves time for academics."
                    },
                    {
                        "id": "b",
                        "text": "Retail Store (20 hrs/week, $16/hr): More money, busier",
                        "correct": True,
                        "explanation": "Ambitious! 💼 This works if you manage time well. Watch your stress levels."
                    },
                    {
                        "id": "c",
                        "text": "Full-time warehouse (40 hrs/week, $18/hr)",
                        "correct": False,
                        "explanation": "Overload! 🚨 40 + 25 = 65 hours—you're over budget! This will destroy your GPA and health."
                    },
                    {
                        "id": "d",
                        "text": "No job—focus only on academics",
                        "correct": True,
                        "explanation": "Valid if you have savings! 🎓 No job means more study time, but watch your money carefully."
                    }
                ]
            ),
            TutorialGameQuestion(
                id="t_final_q3",
                text="Final choice: What activities will you join? (Each takes 3-5 hrs/week)",
                hint="Activities boost happiness and social skills but consume time.",
                learning_objective="Understand activity trade-offs",
                choices=[
                    {
                        "id": "a",
                        "text": "Join 5 clubs (Drama, Sports, Debate, Student Gov, Gaming)",
                        "correct": False,
                        "explanation": "Way too much! 🤯 That's 15-25 hours on top of everything else. Pick 1-2 to start."
                    },
                    {
                        "id": "b",
                        "text": "1-2 clubs you're genuinely interested in",
                        "correct": True,
                        "explanation": "Perfect balance! ⚖️ You get social benefits without overcommitting. Quality over quantity."
                    },
                    {
                        "id": "c",
                        "text": "No activities—I'm here to work, not make friends",
                        "correct": False,
                        "explanation": "Too isolated! 😔 Activities boost happiness and networking. At least join one thing you enjoy."
                    },
                    {
                        "id": "d",
                        "text": "Party every night (20+ hrs/week 'social activities')",
                        "correct": False,
                        "explanation": "Not sustainable! 🍺 This will tank your GPA and drain your wallet. Balance is key."
                    }
                ]
            )
        ]
    ),
}


# =============================================
# Tutorial Quest Chain
# =============================================

class QuestStep(BaseModel):
    """Single step in a quest chain"""
    id: str
    title: str
    description: str
    game_id: str  # Which tutorial game to play
    required_score: float  # Minimum score to pass (0-100)
    rewards: Dict[str, Any]  # {points, items, unlocks}
    next_step_id: str | None


class QuestChain(BaseModel):
    """Progressive quest chain for onboarding"""
    id: str
    title: str
    description: str
    steps: List[QuestStep]
    total_points_reward: int
    estimated_total_minutes: int
    completion_badge: str  # Badge ID earned on completion


NEW_PLAYER_QUEST: QuestChain = QuestChain(
    id="new_player_quest",
    title="🎓 Welcome to Life Sprint",
    description="Learn the ropes and start your college journey",
    total_points_reward=375,
    estimated_total_minutes=10,
    completion_badge="badge_tutorial_complete",
    steps=[
        QuestStep(
            id="quest_step_1",
            title="First Day Orientation",
            description="Make your first big decision",
            game_id="tutorial_welcome",
            required_score=70.0,
            rewards={"points": 50, "unlocks": ["time_management_tutorial"]},
            next_step_id="quest_step_2"
        ),
        QuestStep(
            id="quest_step_2",
            title="Time Management 101",
            description="Learn to balance your schedule",
            game_id="tutorial_time_management",
            required_score=70.0,
            rewards={"points": 50, "unlocks": ["financial_tutorial"]},
            next_step_id="quest_step_3"
        ),
        QuestStep(
            id="quest_step_3",
            title="Money Matters",
            description="Master basic budgeting",
            game_id="tutorial_financial_planning",
            required_score=70.0,
            rewards={"points": 75, "unlocks": ["emergency_tutorial"]},
            next_step_id="quest_step_4"
        ),
        QuestStep(
            id="quest_step_4",
            title="Handling Emergencies",
            description="Learn crisis management",
            game_id="tutorial_emergency_planning",
            required_score=70.0,
            rewards={"points": 50, "unlocks": ["final_challenge"]},
            next_step_id="quest_step_5"
        ),
        QuestStep(
            id="quest_step_5",
            title="Plan Your Semester",
            description="Put everything together",
            game_id="tutorial_final_challenge",
            required_score=70.0,
            rewards={"points": 100, "badge": "badge_tutorial_complete", "unlocks": ["main_game"]},
            next_step_id=None
        ),
    ]
)


# =============================================
# Mascot System
# =============================================

class MascotDialogue(BaseModel):
    """Mascot character dialogue for personality"""
    context: str  # When this dialogue triggers
    text: str
    emotion: str  # "excited", "encouraging", "concerned", "proud"


MASCOT_DIALOGUES: List[MascotDialogue] = [
    MascotDialogue(
        context="tutorial_start",
        text="Welcome to Life Sprint! I'm Sprint, your personal guide. Think of me as your college survival coach. Ready to learn the ropes?",
        emotion="excited"
    ),
    MascotDialogue(
        context="first_correct_answer",
        text="Nice! 🎉 You're getting the hang of this. Keep it up!",
        emotion="proud"
    ),
    MascotDialogue(
        context="first_wrong_answer",
        text="No worries! 😊 Mistakes are how we learn. Read the explanation and try the next one!",
        emotion="encouraging"
    ),
    MascotDialogue(
        context="quest_step_complete",
        text="Quest step complete! ⭐ You're making great progress. Ready for the next challenge?",
        emotion="proud"
    ),
    MascotDialogue(
        context="struggling_multiple_wrong",
        text="I can see you're having trouble. 🤔 Take your time, read the hints, and think it through. You've got this!",
        emotion="encouraging"
    ),
    MascotDialogue(
        context="quest_chain_complete",
        text="🎊 AMAZING! You completed the tutorial! You're ready for the real game. Go show college who's boss!",
        emotion="excited"
    ),
    MascotDialogue(
        context="returning_player",
        text="Welcome back! 👋 Ready to continue your journey?",
        emotion="excited"
    ),
    MascotDialogue(
        context="player_struggling_in_game",
        text="Hey, I noticed you're having a tough time. 😟 Want to take a break or check out some tips? Remember, this is supposed to be fun!",
        emotion="concerned"
    ),
]


# =============================================
# Helper Functions
# =============================================

def get_tutorial_game(game_id: str) -> TutorialGame | None:
    """Retrieve a tutorial game by ID"""
    return TUTORIAL_GAMES.get(game_id)


def get_new_player_quest() -> QuestChain:
    """Get the new player quest chain"""
    return NEW_PLAYER_QUEST


def get_mascot_dialogue(context: str) -> str:
    """Get mascot dialogue for a specific context"""
    for dialogue in MASCOT_DIALOGUES:
        if dialogue.context == context:
            return dialogue.text
    return "Keep going! You're doing great! 🎮"


def calculate_quest_progress(completed_steps: List[str]) -> Dict[str, Any]:
    """Calculate player's progress through the tutorial quest"""
    quest = NEW_PLAYER_QUEST
    total_steps = len(quest.steps)
    completed_count = len(completed_steps)
    
    # Find current step
    current_step = None
    for step in quest.steps:
        if step.id not in completed_steps:
            current_step = step
            break
    
    progress_percent = (completed_count / total_steps) * 100 if total_steps > 0 else 0
    
    return {
        "quest_id": quest.id,
        "quest_title": quest.title,
        "total_steps": total_steps,
        "completed_steps": completed_count,
        "progress_percent": progress_percent,
        "current_step": current_step.model_dump() if current_step else None,
        "is_complete": completed_count >= total_steps,
        "total_points_earned": sum(
            step.rewards.get("points", 0) 
            for step in quest.steps 
            if step.id in completed_steps
        ),
    }
