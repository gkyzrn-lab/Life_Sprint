"""
Mini-lessons delivered between semesters to teach real-world concepts.
Quick 30-60 second educational content.
"""

from typing import Dict, List
from enum import Enum

class LessonCategory(str, Enum):
    FINANCE = "finance"
    CAREER = "career"
    HEALTH = "health"
    SOCIAL = "social"
    ACADEMICS = "academics"

# Each lesson is designed to be read in 30-60 seconds
MINI_LESSONS = {
    # FINANCE LESSONS
    "budget_basics": {
        "id": "budget_basics",
        "category": LessonCategory.FINANCE,
        "title": "The 50/30/20 Budget Rule",
        "duration_seconds": 45,
        "content": """
The simplest budget rule that actually works:

**50%** = Needs (rent, food, utilities, loan payments)
**30%** = Wants (fun, entertainment, eating out)
**20%** = Savings & extra debt payments

Example: Make $2,000/month?
- $1,000 for needs
- $600 for wants
- $400 for savings

Pro tip: Automate that 20% savings - transfer it the day you get paid so you never see it!
        """.strip(),
        "key_takeaway": "Save 20% automatically before spending on anything else.",
        "unlocks_after_semester": 2
    },
    
    "emergency_fund": {
        "id": "emergency_fund",
        "category": LessonCategory.FINANCE,
        "title": "Why You NEED an Emergency Fund",
        "duration_seconds": 50,
        "content": """
78% of Americans live paycheck to paycheck. One emergency = debt spiral.

**Emergency Fund = Peace of Mind**

Goal: Save 3-6 months of expenses
Start: Even $500 makes a HUGE difference

What it covers:
- Car breakdown
- Medical emergency  
- Job loss
- Laptop dies before finals

Without it: You use credit cards (18% interest!) or panic. With it: Problem solved, move on with life.

Start TODAY with $20/week. In 6 months, you'll have $520!
        """.strip(),
        "key_takeaway": "Start with $500, build to 3-6 months of expenses.",
        "unlocks_after_semester": 3
    },
    
    "credit_score": {
        "id": "credit_score",
        "category": LessonCategory.FINANCE,
        "title": "Credit Score: Your Financial Reputation",
        "duration_seconds": 55,
        "content": """
Your credit score (300-850) affects EVERYTHING:
- Loan interest rates
- Apartment rentals
- Car insurance rates
- Some job applications!

**How to build good credit:**
1. Pay bills on time (35% of score)
2. Keep credit card balance under 30% of limit (30%)
3. Don't close old accounts (15%)
4. Don't apply for too much credit at once (10%)

Real impact: 
- 760+ score: 3.5% mortgage rate
- 620 score: 5.5% mortgage rate
- On $300K house = $90,000 difference over 30 years!

Build it NOW while you're young. Future you will thank you!
        """.strip(),
        "key_takeaway": "Pay everything on time. Keep credit card balances low.",
        "unlocks_after_semester": 4
    },
    
    "investing_basics": {
        "id": "investing_basics",
        "category": LessonCategory.FINANCE,
        "title": "Investing: Make Your Money Work For You",
        "duration_seconds": 60,
        "content": """
Saving = Money sits there
Investing = Money GROWS

**The S&P 500 averages 10% annual return (historically)**

$100/month invested from age 22-65:
- Total invested: $51,600
- Final value: $637,000+

Same $100/month starting at age 32:
- Total invested: $39,600
- Final value: $226,000

Starting 10 years earlier = $400,000 more!

**Where to start:**
1. 401(k) if employer matches (FREE money!)
2. Roth IRA ($6,500/year, tax-free growth)
3. Index funds (diversified, low fees)

Don't try to beat the market. Time in market > timing the market.
        """.strip(),
        "key_takeaway": "Start investing early, even $50/month. Use index funds. Be patient.",
        "unlocks_after_semester": 5
    },
    
    # CAREER LESSONS
    "networking_power": {
        "id": "networking_power",
        "category": LessonCategory.CAREER,
        "title": "The Hidden Job Market",
        "duration_seconds": 45,
        "content": """
**70-80% of jobs are NEVER posted publicly!**

They're filled through:
- Internal referrals
- Networking
- Former interns
- LinkedIn connections

"It's not what you know, it's who you know" is literally true.

**How to network (without being awkward):**
1. Actually help people (answer questions, share resources)
2. Stay in touch (message once every 3 months)
3. Ask for advice, not jobs
4. LinkedIn = your professional resume

One good connection can change your career trajectory.

Start building your network NOW, not when you need a job.
        """.strip(),
        "key_takeaway": "Build relationships now. Most jobs come from connections, not applications.",
        "unlocks_after_semester": 3
    },
    
    "resume_secrets": {
        "id": "resume_secrets",
        "category": LessonCategory.CAREER,
        "title": "Resumes: What Actually Works",
        "duration_seconds": 50,
        "content": """
Recruiters spend 6-7 SECONDS scanning your resume.

**What they look for:**
1. Quantified achievements (not duties)
   ❌ "Responsible for social media"
   ✅ "Grew Instagram 300% (2K→8K) in 6 months"

2. Relevant experience (internships, projects, leadership)
3. Skills that match the job description
4. Clean formatting, no typos

**Pro tips:**
- Use numbers everywhere possible
- Start bullets with action verbs
- Tailor resume for EACH job
- Include GitHub/portfolio links
- 1 page until you have 10+ years experience

Your resume isn't your life story - it's a marketing document to get an interview.
        """.strip(),
        "key_takeaway": "Quantify everything. Use numbers. Tailor for each job. Keep it to 1 page.",
        "unlocks_after_semester": 4
    },
    
    "interview_tips": {
        "id": "interview_tips",
        "category": LessonCategory.CAREER,
        "title": "Interview Hack: STAR Method",
        "duration_seconds": 55,
        "content": """
"Tell me about a time when..." questions = 80% of interviews

**Use the STAR Method:**

**S**ituation - Set the context (1 sentence)
**T**ask - What you needed to do (1 sentence)  
**A**ction - What YOU specifically did (2-3 sentences)
**R**esult - Quantified outcome (1 sentence with numbers!)

Example:
S: "Our team was behind on a project deadline..."
T: "I needed to coordinate 5 people and deliver in 3 days..."
A: "I created a shared timeline, delegated tasks by strengths, and held daily 15-min standups..."
R: "We delivered 2 days early and the client increased their contract by 40%."

Prepare 5-6 STAR stories. You can adapt them to any question!
        """.strip(),
        "key_takeaway": "Prepare STAR stories before interviews. Always include quantified results.",
        "unlocks_after_semester": 5
    },
    
    # HEALTH LESSONS
    "sleep_performance": {
        "id": "sleep_performance",
        "category": LessonCategory.HEALTH,
        "title": "Sleep: Your Secret Weapon",
        "duration_seconds": 50,
        "content": """
All-nighters are SCIENTIFICALLY proven to hurt performance.

**Sleep deprivation effects:**
- Memory consolidation drops 40%
- Reaction time = legally drunk
- Decision-making impaired
- Immunity compromised

**Sleep benefits:**
- Better grades (0.5 GPA difference!)
- Faster learning
- Better mood
- Athletic performance boost

**College sleep tips:**
1. 7-9 hours is non-negotiable
2. Same sleep schedule (even weekends)
3. No screens 1 hour before bed
4. Dark, cool room (65-68°F)

Pulling an all-nighter before an exam? You'd score better sleeping 7 hours and studying less.

Sleep isn't lazy - it's how your brain upgrades itself!
        """.strip(),
        "key_takeaway": "7-9 hours of sleep improves grades more than extra study time.",
        "unlocks_after_semester": 1
    },
    
    "stress_science": {
        "id": "stress_science",
        "category": LessonCategory.HEALTH,
        "title": "Understanding Stress vs. Burnout",
        "duration_seconds": 45,
        "content": """
Stress = Normal, temporary, manageable
Burnout = Chronic stress, exhaustion, can't recover

**Burnout warning signs:**
- Can't focus even after rest
- Everything feels pointless
- Physical symptoms (headaches, stomach issues)
- Isolation from friends
- Cynicism/negativity

**Prevention:**
1. Regular breaks (not rewards, but requirements!)
2. Exercise 3x/week minimum
3. Social connection weekly
4. Sleep 7-9 hours
5. Say "no" sometimes

You can't pour from an empty cup. Taking care of yourself isn't selfish - it's essential for performance.

If you're burned out, recovery takes MONTHS. Prevent it early!
        """.strip(),
        "key_takeaway": "Prevent burnout with regular breaks, exercise, sleep, and social time.",
        "unlocks_after_semester": 2
    },
    
    # SOCIAL LESSONS
    "meaningful_connections": {
        "id": "meaningful_connections",
        "category": LessonCategory.SOCIAL,
        "title": "Quality Over Quantity in Friendships",
        "duration_seconds": 40,
        "content": """
3-5 close friends > 100 Instagram followers

**Research shows:**
- People with strong friendships live 7 years longer
- Better mental health
- Higher income (network effect)
- More life satisfaction

**Building deep friendships:**
1. Consistency > intensity (weekly hangouts beat yearly trips)
2. Vulnerability (share real struggles, not just highlights)
3. Be the friend who checks in first
4. Do activities together (shared experiences bond people)

College is the EASIEST time to make lifelong friends. Everyone's in the same boat, same place, same schedule.

Invest time in friendships now. They're worth more than grades long-term.
        """.strip(),
        "key_takeaway": "Invest in 3-5 close friendships. Consistency and vulnerability matter most.",
        "unlocks_after_semester": 1
    },
    
    # ACADEMIC LESSONS
    "study_techniques": {
        "id": "study_techniques",
        "category": LessonCategory.ACADEMICS,
        "title": "Study Smarter, Not Harder",
        "duration_seconds": 55,
        "content": """
Re-reading textbooks = worst study method (but most common!)

**Effective study techniques (ranked by research):**

1. **Practice testing** - Quiz yourself repeatedly
   - Improves retention by 50%+
   - Use flashcards, practice problems, past exams

2. **Spaced repetition** - Study over time, not all at once
   - Review after 1 day, 3 days, 1 week, 1 month
   - Beats cramming by 200%

3. **Teaching others** - Explain concepts to friends
   - If you can teach it, you know it

4. **Interleaving** - Mix different topics in one session
   - Don't do 50 math problems in a row
   - Do 10 math, 10 chemistry, 10 history, repeat

**Worst methods:**
- Highlighting (passive)
- Re-reading (illusion of knowledge)
- Cramming (forget it after exam)

Study 2 hours effectively > 6 hours passively!
        """.strip(),
        "key_takeaway": "Practice testing + spaced repetition = 2-3x better retention than re-reading.",
        "unlocks_after_semester": 2
    },
    
    # CREDIT CARD EDUCATION LESSONS
    "credit_cards_101": {
        "id": "credit_cards_101",
        "category": LessonCategory.FINANCE,
        "title": "Credit Cards: Tool or Trap?",
        "duration_seconds": 60,
        "content": """
Credit cards can build wealth OR destroy it. Here's the truth:

THE GOLDEN RULE: Pay FULL balance every month = $0 interest.
Break this rule = you're paying 20-25% extra for everything.

**Real Example:**
- $1,000 laptop paid in full = $1,000 total
- $1,000 laptop, pay minimum = $1,680 over 5 years

That's a $680 "stupid tax" for the same laptop.

**How to Win:**
1. Get ONE card (not five)
2. Charge only what you can pay this month
3. Set up auto-pay for FULL balance
4. Never carry a balance

Do this = free money (cashback) + great credit score.
Carry balances = debt trap + ruined credit.

You choose which story you're living.
        """.strip(),
        "key_takeaway": "Pay full balance every month. That's the only rule that matters.",
        "unlocks_after_semester": 2
    },
    
    "building_credit_score": {
        "id": "building_credit_score",
        "category": LessonCategory.FINANCE,
        "title": "Credit Score: Your Financial Superpower",
        "duration_seconds": 55,
        "content": """
Your credit score (300-850) determines your adult life costs.

**What It Affects:**
- Apartment rentals (landlords check)
- Auto loan rates (4% vs 12% = $6,000 difference)
- Job offers (some employers check)
- Insurance rates (yes, really)

**What Builds It (in order):**
1. Payment history (35%): NEVER miss payments
2. Credit utilization (30%): Keep under 30% of limit
3. Credit age (15%): Older accounts = better
4. Credit mix (10%): Cards + loans = good
5. New credit (10%): Don't apply for too many cards

**The Fastest Way to Build:**
- Get ONE student credit card
- Charge $20-50 per month (groceries, gas)
- Pay FULL balance before due date
- Repeat for 6 months
- Boom: 700+ credit score

Start now. Your 30-year-old self will save $50,000+ on loan interest.
        """.strip(),
        "key_takeaway": "Good credit score saves you tens of thousands of dollars in your lifetime.",
        "unlocks_after_semester": 3
    },
    
    "apr_and_interest": {
        "id": "apr_and_interest",
        "category": LessonCategory.FINANCE,
        "title": "APR: The Hidden Tax on Your Money",
        "duration_seconds": 50,
        "content": """
APR = Annual Percentage Rate = the cost of borrowing money.

**Why It Matters:**
Lower APR = you pay less for the same debt.

**Real Comparison - $2,000 credit card balance:**

15% APR (premium card):
- Pay $100/month = 22 months to pay off
- Total paid: $2,150 (only $150 interest)

25% APR (starter card):
- Pay $100/month = 25 months to pay off
- Total paid: $2,425 ($425 interest!)

Same debt, same payments, $275 MORE just because of APR.

**The Strategy:**
- If you NEVER carry balances: APR doesn't matter, chase rewards
- If you EVER carry balances: Get LOWEST APR possible
- Most students: Get low APR "just in case" for emergencies

GOOD APR = 15-18% (hard to qualify)
OK APR = 18-21% (most students)
BAD APR = 21-25% (easy to get, expensive to use)
TERRIBLE APR = 25%+ (predatory)
        """.strip(),
        "key_takeaway": "Lower APR saves you money if you ever carry a balance. Compare carefully.",
        "unlocks_after_semester": 4
    },
    
    "credit_card_perks_lesson": {
        "id": "credit_card_perks_lesson",
        "category": LessonCategory.FINANCE,
        "title": "Credit Card Perks: Free Money or Marketing?",
        "duration_seconds": 45,
        "content": """
Credit card perks sound amazing: cashback, free gym, travel insurance!
But there's a catch: they're only valuable if you NEVER pay interest.

**The Math:**

Premium card: 2% cashback + $25/month gym membership
Spend $500/month, pay in full:
- Earn: $10 cashback + $25 gym = $35/month = $420/year
- Cost: $0 interest
- NET: +$420 🎉

Same card, carry $1,000 balance at 18% APR:
- Earn: $420 in perks
- Pay: $180 interest
- NET: +$240 (still good, but way less)

Same card, carry $2,000 balance at 18% APR:
- Earn: $420 in perks
- Pay: $360 interest
- NET: +$60 (barely worth it)

**The Strategy:**
- Perfect payer? Get card with BEST perks
- Sometimes carry balance? Get card with LOWEST APR
- Don't know yet? Start with low APR, upgrade later

Perks are AMAZING... for disciplined users only.
        """.strip(),
        "key_takeaway": "Perks only matter if you pay in full. One month of interest erases a year of rewards.",
        "unlocks_after_semester": 5
    }
}

def get_lesson(lesson_id: str) -> Dict:
    """Get a specific mini-lesson."""
    return MINI_LESSONS.get(lesson_id)

def get_lessons_for_semester(semester: int, categories: List[LessonCategory] = None) -> List[Dict]:
    """
    Get all lessons available for a given semester.
    
    Args:
        semester: Current semester number
        categories: Filter by specific categories (optional)
    
    Returns:
        List of lessons unlocked at this semester
    """
    available = []
    
    for lesson_id, lesson in MINI_LESSONS.items():
        # Check if unlocked
        if lesson.get("unlocks_after_semester", 0) > semester:
            continue
        
        # Check category filter
        if categories and lesson["category"] not in categories:
            continue
        
        available.append(lesson)
    
    return available

def get_random_lesson(semester: int, exclude_seen: List[str] = None) -> Dict:
    """
    Get a random lesson appropriate for the semester that hasn't been seen.
    
    Args:
        semester: Current semester
        exclude_seen: List of lesson IDs already shown to player
    
    Returns:
        Random lesson dict or None
    """
    import random
    
    available = get_lessons_for_semester(semester)
    
    if exclude_seen:
        available = [l for l in available if l["id"] not in exclude_seen]
    
    return random.choice(available) if available else None

def get_all_lessons_by_category() -> Dict[str, List[Dict]]:
    """Get all lessons organized by category."""
    by_category = {cat.value: [] for cat in LessonCategory}
    
    for lesson in MINI_LESSONS.values():
        by_category[lesson["category"]].append(lesson)
    
    return by_category
