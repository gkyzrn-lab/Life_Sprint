# catalogs/major_exploration.py
# ================================================================
# Day-in-the-life exploration system for majors.
# Players can experience what a major FEELS like before committing.
# No quizzes — just immersive scenarios that reveal the reality.
# ================================================================

from __future__ import annotations
from typing import List, Dict

# ── Data Structure ────────────────────────────────────────────────

class Scenario:
    def __init__(self, time: str, situation: str, choices: List[Dict], insight: str):
        self.time = time               # e.g. "8:00 AM Monday"
        self.situation = situation     # what's happening
        self.choices = choices         # what the player can do (no wrong answer)
        self.insight = insight         # what this reveals about the major


MAJOR_EXPLORATIONS = {

    "cs": {
        "title": "A Day in Computer Science",
        "tagline": "You're a CS sophomore. It's Monday morning.",
        "mood": "intense but exciting",
        "scenarios": [
            {
                "time": "8:00 AM",
                "situation": (
                    "Your alarm goes off. You stayed up until 2 AM debugging a program "
                    "that kept crashing. You finally fixed it at 1:47 AM — turns out you "
                    "missed a single semicolon. You feel tired but oddly satisfied."
                ),
                "choices": [
                    {"label": "💻 Check if your fix actually worked", "reaction": "It works! You do a quiet fist pump. This feeling never gets old."},
                    {"label": "☕ Coffee first, code second", "reaction": "Smart. Caffeine is basically a CS course requirement."},
                    {"label": "😴 Sleep 15 more minutes", "reaction": "Rookie mistake — 15 becomes 45. You sprint to class."},
                ],
                "insight": "Late nights debugging are real — but so is the satisfaction of solving hard problems."
            },
            {
                "time": "10:00 AM",
                "situation": (
                    "Data Structures lecture. The professor writes a complex algorithm on the board. "
                    "Half the class looks confused. You actually understand it — because you saw "
                    "something similar in your side project last week."
                ),
                "choices": [
                    {"label": "🙋 Answer the professor's question", "reaction": "You explain it clearly. Two classmates ask for your notes after class."},
                    {"label": "📝 Write it down carefully", "reaction": "Good call. This exact pattern appears on the midterm."},
                    {"label": "🤔 Think about how to use this in your project", "reaction": "Your brain is already connecting theory to practice. That's the CS mindset."},
                ],
                "insight": "CS rewards curiosity. The more you build on your own, the easier class becomes."
            },
            {
                "time": "2:00 PM",
                "situation": (
                    "Group project meeting. Your team needs to build a web app in 3 weeks. "
                    "One teammate wants to use a framework nobody knows. Another wants to "
                    "start from scratch. You have to decide the direction."
                ),
                "choices": [
                    {"label": "🧑‍💻 Suggest a framework everyone knows", "reaction": "The team agrees. You lose an hour but save the project weeks of confusion."},
                    {"label": "📚 Volunteer to learn the new framework fast", "reaction": "Bold move. You spend the weekend on tutorials — and become the team expert."},
                    {"label": "🗳️ Take a vote and go with the majority", "reaction": "Democratic. This is actually how real engineering teams work."},
                ],
                "insight": "CS is 50% coding, 50% collaboration. Communication skills matter more than most expect."
            },
            {
                "time": "7:00 PM",
                "situation": (
                    "You just got an email. A startup you applied to wants to interview you "
                    "next week — technical interview included. They'll ask you to code live "
                    "on a whiteboard while someone watches. Your stomach drops a little."
                ),
                "choices": [
                    {"label": "📖 Start reviewing algorithms tonight", "reaction": "Smart prep. Technical interviews reward consistent practice, not cramming."},
                    {"label": "😰 Google 'how to survive a technical interview'", "reaction": "Everyone does this. You find LeetCode. Your life changes forever."},
                    {"label": "🎮 Take the night off — you earned it", "reaction": "Balance matters. You'll prep tomorrow with a fresher mind."},
                ],
                "insight": "Internships are everything in CS. Real experience beats GPA in most hiring decisions."
            },
        ],
        "reality_check": [
            "📐 You WILL take Calculus, Linear Algebra, and Discrete Math — not just coding",
            "🐛 Debugging is 60% of the job — patience is a skill you'll build",
            "🔁 Technology changes fast — you never stop learning",
            "💰 Entry salaries are high but so is competition for top roles",
            "🌙 Late nights happen — but you control how often",
        ],
        "best_fit_for": "People who love puzzles, don't mind frustration, and enjoy building things that work.",
        "not_great_if": "You hate math, want a 9-to-5 with no surprises, or prefer working with people over computers.",
    },

    "mechanical_engineering": {
        "title": "A Day in Mechanical Engineering",
        "tagline": "You're a junior ME student. It's Tuesday.",
        "mood": "methodical and hands-on",
        "scenarios": [
            {
                "time": "9:00 AM",
                "situation": (
                    "Thermodynamics exam in 2 hours. You've been studying the Carnot cycle "
                    "for a week but one equation still isn't clicking. Your study group meets "
                    "in 20 minutes."
                ),
                "choices": [
                    {"label": "📚 Study solo — you work better alone", "reaction": "You find a YouTube video that explains it perfectly. The exam goes well."},
                    {"label": "👥 Join the study group", "reaction": "A classmate explains it with a drawing. It clicks instantly. Groups have power."},
                    {"label": "🚶 Walk to clear your head first", "reaction": "Sometimes stepping away is the best study technique. You return focused."},
                ],
                "insight": "ME has some of the hardest exams in any major. Study strategies matter enormously."
            },
            {
                "time": "1:00 PM",
                "situation": (
                    "Machine Design lab. You're designing a gear system in CAD software. "
                    "Your simulation shows the design will fail under load. You have "
                    "45 minutes to fix it before the lab ends."
                ),
                "choices": [
                    {"label": "🔧 Increase the gear thickness", "reaction": "It works — but now it's too heavy. Engineering is always a trade-off."},
                    {"label": "📊 Re-check your load calculations first", "reaction": "Good instinct. The input force was wrong. One fix solves everything."},
                    {"label": "🤝 Ask the TA for a hint", "reaction": "TAs are there to help. You find the issue in 5 minutes together."},
                ],
                "insight": "ME is about solving real physical constraints. Every design involves trade-offs."
            },
            {
                "time": "4:00 PM",
                "situation": (
                    "A guest speaker — a NASA engineer — talks about working on the Mars rover. "
                    "He mentions they ran 10,000 simulations before building a single prototype. "
                    "The room is completely silent. Everyone is locked in."
                ),
                "choices": [
                    {"label": "🚀 Ask about how to get into aerospace", "reaction": "He gives you his LinkedIn. This is how careers start."},
                    {"label": "📝 Write down every word", "reaction": "You fill 3 pages of notes. Future-you will be grateful."},
                    {"label": "💭 Daydream about working on something like this", "reaction": "Motivation is fuel. Hold onto that feeling on hard days."},
                ],
                "insight": "ME opens doors to aerospace, automotive, robotics, energy — the physical world is your canvas."
            },
        ],
        "reality_check": [
            "📐 Physics, Thermodynamics, Fluid Mechanics — these are non-negotiable",
            "🖥️ CAD software (SolidWorks, AutoCAD) is a skill you'll spend hours on",
            "🏭 Many jobs involve visiting factories or construction sites",
            "📜 PE license required for senior engineering roles — more exams after graduation",
            "⚙️ Projects take months — you need patience for long feedback loops",
        ],
        "best_fit_for": "People who want to build physical things, love physics, and think in systems.",
        "not_great_if": "You prefer digital/virtual work, dislike math, or want results quickly.",
    },

    "biology": {
        "title": "A Day in Biology",
        "tagline": "You're a sophomore Bio student. It's Wednesday.",
        "mood": "curious and detail-oriented",
        "scenarios": [
            {
                "time": "8:30 AM",
                "situation": (
                    "Cell Biology lecture. The professor explains how mitochondria regulate "
                    "cell death. It sounds abstract — until she says this mechanism is what "
                    "cancer hijacks to survive. Suddenly everyone is paying attention."
                ),
                "choices": [
                    {"label": "🔬 Ask how this connects to cancer treatment", "reaction": "The professor smiles. This exact question led to a Nobel Prize in 2016."},
                    {"label": "📝 Draw the pathway diagram carefully", "reaction": "Visual learners dominate biology. Your diagram becomes your best study tool."},
                    {"label": "💭 Think about what drew you to biology", "reaction": "These 'why does this matter?' moments are why biology students keep going."},
                ],
                "insight": "Biology rewards curiosity. The best students always ask 'but why does this happen?'"
            },
            {
                "time": "11:00 AM",
                "situation": (
                    "Lab practical. You're pipetting samples for a PCR experiment. "
                    "One wrong microliter ruins the whole sample. Your hands are "
                    "steady but your lab partner just contaminated their sample."
                ),
                "choices": [
                    {"label": "🧪 Help them redo it carefully", "reaction": "Good teammate. Lab skills are built through repetition — everyone makes this mistake."},
                    {"label": "📋 Document exactly what happened", "reaction": "Lab notebooks are sacred in biology. Accurate records are half the science."},
                    {"label": "🎯 Focus on your own sample first", "reaction": "Fair. You can't help others if your own work suffers. Balance matters."},
                ],
                "insight": "Lab work requires patience and precision. Small errors have big consequences."
            },
            {
                "time": "3:00 PM",
                "situation": (
                    "Your professor pulls you aside. She's looking for an undergraduate "
                    "research assistant for her lab studying antibiotic resistance. "
                    "Unpaid, 10 hrs/week, but you'd co-author a paper if results are good."
                ),
                "choices": [
                    {"label": "✅ Say yes immediately", "reaction": "Published research as an undergrad is gold for med school or PhD applications."},
                    {"label": "🤔 Ask about the time commitment first", "reaction": "Smart. 10 hrs is significant — you need to know if your schedule allows it."},
                    {"label": "❌ Decline — you need a paying job", "reaction": "Completely valid. Financial reality is real. You're not alone in this choice."},
                ],
                "insight": "Research experience is crucial in biology — but it competes with your time and finances."
            },
        ],
        "reality_check": [
            "🧬 Memorization is real — taxonomy, pathways, processes — there's a LOT",
            "🔬 Lab hours are time-consuming and mandatory",
            "💊 Most good biology jobs require a Masters or PhD",
            "🏥 Pre-med track is brutally competitive — GPA must stay high",
            "💰 Entry-level salaries without grad school are modest ($40-55K)",
        ],
        "best_fit_for": "Detail-oriented people fascinated by living systems, health, and discovery.",
        "not_great_if": "You want high income right after undergrad or dislike memorization and lab work.",
    },

    "ba": {
        "title": "A Day in Business Administration",
        "tagline": "You're a junior BA student. It's Thursday.",
        "mood": "fast-paced and social",
        "scenarios": [
            {
                "time": "9:00 AM",
                "situation": (
                    "Marketing class. Your team presents a campaign strategy for a real local business. "
                    "The professor plays the role of the client and pushes back hard on your pricing model. "
                    "The room watches how you respond."
                ),
                "choices": [
                    {"label": "💼 Defend your numbers with data", "reaction": "Confidence backed by evidence. The 'client' nods. This is what business school trains you for."},
                    {"label": "🔄 Pivot and offer an alternative", "reaction": "Flexibility under pressure is a prized business skill. The class is impressed."},
                    {"label": "🤝 Ask what the client's main concern is", "reaction": "Listening first is advanced. You find out the real objection and address it directly."},
                ],
                "insight": "Business is performative — presentations, pitches, and persuasion are constant."
            },
            {
                "time": "12:00 PM",
                "situation": (
                    "Networking lunch with alumni. You're sitting next to a VP at a consulting firm. "
                    "You have 20 minutes before the next speaker starts. "
                    "You know nobody got hired here without making an impression first."
                ),
                "choices": [
                    {"label": "🗣️ Ask about their career path", "reaction": "People love talking about themselves. You learn more in 10 minutes than a semester of class."},
                    {"label": "📇 Exchange LinkedIn info right away", "reaction": "Efficient. They connect with you that afternoon."},
                    {"label": "😅 Stick to small talk — networking feels awkward", "reaction": "Honest. Most people feel this way. It gets easier with practice — this IS the practice."},
                ],
                "insight": "In business, who you know is as important as what you know. Network early."
            },
            {
                "time": "3:00 PM",
                "situation": (
                    "Finance class. You're analyzing a real company's balance sheet. "
                    "The numbers tell a story — revenue is up but cash flow is negative. "
                    "The professor asks what's wrong with this company."
                ),
                "choices": [
                    {"label": "📊 Spot the accounts receivable problem", "reaction": "Exactly right. They're selling but not collecting. You think like a CFO."},
                    {"label": "🤷 Guess and see what happens", "reaction": "Wrong answer, but you learn more from the explanation than if you'd been right."},
                    {"label": "📝 Write down the framework for next time", "reaction": "Pattern recognition is the core business skill. You're building it."},
                ],
                "insight": "Business requires both big-picture thinking and attention to financial details."
            },
        ],
        "reality_check": [
            "🤝 Networking is not optional — it's part of the curriculum",
            "📊 You will take accounting and finance even if you want to do marketing",
            "💼 Internships are essential — classroom alone won't get you hired",
            "📜 MBA is expected for senior roles at top companies",
            "🌐 The degree is broad — specialization is what makes you competitive",
        ],
        "best_fit_for": "Social, ambitious people who enjoy strategy, people management, and variety.",
        "not_great_if": "You prefer deep technical specialization or working alone without client interaction.",
    },

    "psychology": {
        "title": "A Day in Psychology",
        "tagline": "You're a junior Psych student. It's Friday.",
        "mood": "reflective and people-focused",
        "scenarios": [
            {
                "time": "10:00 AM",
                "situation": (
                    "Abnormal Psychology. The professor describes a real case study — "
                    "a person whose behavior changed completely after a small brain injury. "
                    "The class is riveted. You realize the brain controls everything."
                ),
                "choices": [
                    {"label": "🧠 Connect it to a paper you read last week", "reaction": "You mention the connection out loud. The professor adds it to the discussion."},
                    {"label": "📓 Write the case details to remember later", "reaction": "Case studies are the backbone of psychology education. Good instinct."},
                    {"label": "💭 Think about people you know who changed after trauma", "reaction": "Psychology gets personal. That's both its power and its emotional weight."},
                ],
                "insight": "Psychology makes you see human behavior differently — forever. That's a gift and a burden."
            },
            {
                "time": "1:00 PM",
                "situation": (
                    "Research Methods lab. You're analyzing survey data from 200 participants. "
                    "Your hypothesis was wrong — the data shows the opposite of what you predicted. "
                    "Your report is due Monday."
                ),
                "choices": [
                    {"label": "📊 Report the actual results honestly", "reaction": "This is science. Disconfirmed hypotheses are still valuable findings."},
                    {"label": "🔍 Look for a subgroup where it IS true", "reaction": "Careful — this is how p-hacking starts. Stick to your original hypothesis."},
                    {"label": "🤔 Discuss why you think you were wrong", "reaction": "Excellent scientific thinking. The best papers explain unexpected results thoughtfully."},
                ],
                "insight": "Psychology is more scientific than people expect. Statistics and research methods are core."
            },
            {
                "time": "4:00 PM",
                "situation": (
                    "You volunteer at a campus counseling center as a peer support listener. "
                    "A student comes in visibly upset about their family situation. "
                    "You're not a therapist — but you're trained to listen."
                ),
                "choices": [
                    {"label": "👂 Listen fully before saying anything", "reaction": "The most powerful thing you can do. They leave calmer just from being heard."},
                    {"label": "💡 Offer suggestions to solve their problem", "reaction": "Natural impulse — but premature advice often backfires. Listen first, always."},
                    {"label": "📋 Refer them to a professional counselor", "reaction": "Knowing your limits is a professional skill. This was the right call."},
                ],
                "insight": "Emotional labor is real in psychology. You carry others' pain — self-care becomes essential."
            },
        ],
        "reality_check": [
            "📊 You will take Statistics — it's mandatory and used constantly",
            "🎓 A bachelor's alone limits your options — most clinical roles need a Masters or PhD",
            "💸 Graduate school for therapy is expensive and competitive",
            "❤️ Emotionally demanding work — hearing others' trauma affects you",
            "🌟 BUT: careers in UX research, HR, and corporate consulting are growing fast",
        ],
        "best_fit_for": "Empathetic people who want to understand why humans think and behave the way they do.",
        "not_great_if": "You want high income right after undergrad or struggle to separate others' emotions from your own.",
    },

    "finance": {
        "title": "A Day in Finance",
        "tagline": "You're a junior Finance student. It's Monday.",
        "mood": "fast, high-stakes, numbers-driven",
        "scenarios": [
            {
                "time": "8:00 AM",
                "situation": (
                    "Markets opened 30 minutes ago. Your Investment Analysis professor "
                    "pulls up live stock data. A company you analyzed last week just "
                    "dropped 12% on bad earnings. Your recommendation was 'buy.'"
                ),
                "choices": [
                    {"label": "📉 Analyze what you missed in your model", "reaction": "This is how great analysts are made. You find a cash flow assumption you underweighted."},
                    {"label": "🗣️ Defend your original thesis", "reaction": "One data point doesn't invalidate an analysis. You explain your long-term reasoning well."},
                    {"label": "😬 Stay quiet and hope nobody remembers", "reaction": "The professor definitely remembers. But everyone's wrong sometimes — owning it matters more."},
                ],
                "insight": "Finance involves being wrong publicly and learning fast. Ego is expensive here."
            },
            {
                "time": "11:00 AM",
                "situation": (
                    "Corporate Finance class. You're valuing a fictional company using DCF analysis. "
                    "Small changes in your assumptions swing the valuation by millions. "
                    "The professor says: 'All models are wrong. Some are useful.'"
                ),
                "choices": [
                    {"label": "📊 Run sensitivity analysis on your assumptions", "reaction": "Professional level thinking. This is exactly what analysts do on Wall Street."},
                    {"label": "🎯 Pick the assumptions that give the 'best' answer", "reaction": "Tempting — but this is how financial crises start. Good finance demands honesty."},
                    {"label": "💭 Think about what assumptions really drive value", "reaction": "You're developing financial intuition. That's rare and valuable."},
                ],
                "insight": "Finance is about judgment under uncertainty, not just spreadsheet skills."
            },
            {
                "time": "6:00 PM",
                "situation": (
                    "Finance club meeting. A speaker from Goldman Sachs talks about investment banking. "
                    "He mentions working 90-hour weeks as a first-year analyst. "
                    "He also mentions his first-year salary was $110,000."
                ),
                "choices": [
                    {"label": "💰 That salary makes the hours worth it", "reaction": "For some people it genuinely is. Know yourself before choosing this path."},
                    {"label": "⚖️ Ask about work-life balance in year 3-4", "reaction": "Smart. It does improve — but takes years. The question shows maturity."},
                    {"label": "🤔 Wonder if there's a better path in finance", "reaction": "Corporate finance, fintech, and asset management all offer better balance with good pay."},
                ],
                "insight": "Finance has many paths — investment banking is just the loudest one. Choose yours deliberately."
            },
        ],
        "reality_check": [
            "📐 Calculus, Statistics, and Accounting are required — math is unavoidable",
            "⏰ Investment banking = extreme hours. Corporate finance = more balanced",
            "📜 Licenses (Series 7, CFA) required for many senior roles",
            "📈 Market cycles affect hiring — finance jobs fluctuate with the economy",
            "💼 Internships at banks/firms are essentially required for top jobs",
        ],
        "best_fit_for": "Analytical, competitive people who thrive under pressure and are motivated by markets.",
        "not_great_if": "You dislike math, want predictable hours, or are uncomfortable with financial risk.",
    },

    "nursing": {
        "title": "A Day in Nursing",
        "tagline": "You're a junior Nursing student. It's Tuesday — clinical day.",
        "mood": "intense, human, and purposeful",
        "scenarios": [
            {
                "time": "6:00 AM",
                "situation": (
                    "Clinical shift starts at 7. You review your assigned patient's chart at home — "
                    "elderly woman, post-surgery, three medications with potential interactions. "
                    "You flag something that doesn't look right."
                ),
                "choices": [
                    {"label": "🚨 Note it and tell the supervising nurse immediately", "reaction": "The nurse checks — you were right. The attending physician is notified. You potentially prevented harm."},
                    {"label": "📚 Double-check in your pharmacology textbook first", "reaction": "Good instinct to verify. Thorough preparation is a nursing strength."},
                    {"label": "🤔 Wait to see if the day nurse catches it too", "reaction": "In nursing, waiting on patient safety concerns is never the right call. Speak up early."},
                ],
                "insight": "Nursing is high-stakes. Attention to detail and speaking up can save lives."
            },
            {
                "time": "10:00 AM",
                "situation": (
                    "A patient is scared before a procedure. They grab your hand and ask if everything "
                    "will be okay. Medically, the procedure is routine. But they're terrified. "
                    "You have 3 other patients waiting."
                ),
                "choices": [
                    {"label": "🤝 Stay 5 minutes and talk them through it", "reaction": "This is the heart of nursing. Their vitals stabilize before the procedure. Calm patients heal faster."},
                    {"label": "💬 Give a quick reassurance and move on", "reaction": "Sometimes time forces this. You feel the tension between compassion and capacity."},
                    {"label": "👥 Ask a colleague to sit with them briefly", "reaction": "Good resource management. Delegation is a real nursing skill."},
                ],
                "insight": "Nursing is emotionally demanding. The human connection is the reward — and the cost."
            },
            {
                "time": "3:00 PM",
                "situation": (
                    "End of shift. You're exhausted. A patient you cared for last week "
                    "didn't make it. The team is quiet. Your supervisor checks in on everyone individually."
                ),
                "choices": [
                    {"label": "💬 Talk about it with your supervisor", "reaction": "Processing grief is part of the job. Nurses who don't burn out have support systems."},
                    {"label": "🏃 Head straight home to decompress alone", "reaction": "Everyone processes differently. But over time, isolation increases burnout risk."},
                    {"label": "📓 Write about it in your reflection journal", "reaction": "Many nursing programs require this. It builds emotional resilience over time."},
                ],
                "insight": "Grief is part of nursing. The strongest nurses build real coping systems — not walls."
            },
        ],
        "reality_check": [
            "⏰ Shifts are 12 hours — nights, weekends, and holidays are part of the job",
            "🏥 You will see suffering — emotional resilience is a skill you must build",
            "📚 NCLEX licensing exam is required after graduation — significant prep needed",
            "💪 Physical demands are real — lifting, standing, moving all day",
            "💰 Strong job security and salary growth with specialization (ICU, OR, NP)",
        ],
        "best_fit_for": "Compassionate, calm-under-pressure people who want direct human impact every single day.",
        "not_great_if": "You need emotional distance from your work or prefer desk-based, predictable environments.",
    },

    "data_science": {
        "title": "A Day in Data Science",
        "tagline": "You're a junior Data Science student. It's Wednesday.",
        "mood": "analytical, creative, constantly evolving",
        "scenarios": [
            {
                "time": "9:00 AM",
                "situation": (
                    "Machine Learning class. The professor introduces a new algorithm. "
                    "Half the math you recognize from statistics. The other half is new. "
                    "The professor says: 'Don't memorize this — understand WHY it works.'"
                ),
                "choices": [
                    {"label": "📐 Derive it from first principles", "reaction": "Hard but powerful. You understand it at a level most classmates don't."},
                    {"label": "💻 Code it up to see what it actually does", "reaction": "Hands-on learners often outperform theoretical ones in data science jobs."},
                    {"label": "📖 Find a visual explanation online", "reaction": "3Blue1Brown has a video on this. Your understanding clicks in 12 minutes."},
                ],
                "insight": "Data science blends math, coding, and intuition. You need all three."
            },
            {
                "time": "1:00 PM",
                "situation": (
                    "Capstone project. Your team is analyzing real hospital data to predict "
                    "patient readmissions. The model is 89% accurate. But your professor "
                    "asks: 'Accurate for WHICH patients?' You run the breakdown by demographic."
                ),
                "choices": [
                    {"label": "😟 Discover the model performs worse for elderly patients", "reaction": "This is AI bias in the real world. You've just done more important work than most data scientists."},
                    {"label": "🔧 Try to fix the imbalance in the training data", "reaction": "This is called fairness-aware machine learning. It's a growing and critical field."},
                    {"label": "📊 Report both findings honestly in your presentation", "reaction": "Integrity in data science is rare and valued. Your professor specifically praises this."},
                ],
                "insight": "Data science has real ethical dimensions. The best analysts ask uncomfortable questions."
            },
            {
                "time": "5:00 PM",
                "situation": (
                    "You see a job posting: Data Scientist at a streaming company. "
                    "Requirements: Python, SQL, Machine Learning, Statistics, Communication skills. "
                    "You have all of these — except you've never explained technical findings "
                    "to a non-technical audience before."
                ),
                "choices": [
                    {"label": "📝 Apply and mention you're building presentation skills", "reaction": "Honesty about growth areas is respected. You get an interview."},
                    {"label": "🎤 Join a club to practice presenting this semester", "reaction": "Proactive gap-filling. This one skill unlocks senior roles faster than any technical cert."},
                    {"label": "💻 Build a portfolio project to show instead of tell", "reaction": "A great portfolio beats a resume every time in data science."},
                ],
                "insight": "Technical skills get you interviews. Communication skills get you promoted."
            },
        ],
        "reality_check": [
            "📐 Linear Algebra, Statistics, and Calculus are the foundation — no shortcuts",
            "🐍 Python and SQL are non-negotiable — start learning now if you haven't",
            "🔄 The field changes fast — tools you learn today may be replaced in 3 years",
            "💬 Explaining insights to non-technical people is 40% of the job",
            "💰 One of the highest-paying fields — but competition for top roles is intense",
        ],
        "best_fit_for": "Curious analytical people who enjoy finding patterns and can bridge math and communication.",
        "not_great_if": "You dislike math or statistics, or prefer working with physical/tangible systems.",
    },

    # Fallback for majors without full scenarios
    "_default": {
        "title": "Exploring This Major",
        "tagline": "Get a feel for what this field is really like.",
        "mood": "exploratory",
        "scenarios": [],
        "reality_check": [],
        "best_fit_for": "See the major description for details.",
        "not_great_if": "See the major description for details.",
    }
}


def get_major_exploration(major_id: str) -> dict:
    """
    Get the full day-in-the-life exploration for a major.
    Falls back to default if no exploration exists yet.
    """
    from catalogs.majors import MAJORS

    exploration = MAJOR_EXPLORATIONS.get(major_id, MAJOR_EXPLORATIONS["_default"])
    major_info = MAJORS.get(major_id, {})

    return {
        "major_id": major_id,
        "major_name": major_info.get("name", major_id),
        "difficulty": major_info.get("difficulty", "unknown"),
        "typical_salaries": major_info.get("typical_salaries", "varies"),
        "job_outlook": major_info.get("job_outlook", "unknown"),
        "exploration": exploration,
        "scenario_count": len(exploration.get("scenarios", [])),
        "has_full_exploration": major_id in MAJOR_EXPLORATIONS,
    }


def list_all_explorations() -> list:
    """List which majors have full explorations available."""
    from catalogs.majors import MAJORS
    return [
        {
            "major_id": mid,
            "major_name": MAJORS.get(mid, {}).get("name", mid),
            "has_exploration": mid in MAJOR_EXPLORATIONS,
            "scenario_count": len(MAJOR_EXPLORATIONS.get(mid, {}).get("scenarios", [])),
        }
        for mid in MAJORS
    ]
