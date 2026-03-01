# 🎯 Career Advancement & Progression System

## Overview

Career is now a **fully-fledged system** that teaches teens about:
- **Real career progression** (can't jump from entry → CEO)
- **Work-life balance tradeoffs** (higher salary = more burnout risk)
- **How education affects careers** (GPA unlocks better jobs)
- **Health impacts performance** (can't excel if burned out)
- **Delayed gratification** (consistent performance leads to promotions)

---

## Core Mechanics

### 1. Career Paths (4 Major Paths)

Each path has **4 tiers**: Entry → Mid → Senior → Lead

```
Tech:        Junior Dev → Developer → Senior Engineer → Engineering Lead
Finance:     Junior Analyst → Analyst → Senior Manager → Director/VP
Education:   TA → Adjunct → Instructor → Professor
Healthcare:  Medical Asst → Nurse → Senior Nurse → Director/Physician
```

**Key detail:** Each promotion requires:
- Minimum GPA (increases per tier)
- Minimum performance rating (70→75→80)
- Time in current role (2-3+ semesters)
- Can't get promoted for X semesters after last promotion (prevents gaming)

### 2. Performance Rating (0-100)

**Calculated from:**
- GPA (3.5 GPA = +35 points)
- Health (better health = +5% performance)
- Mental health (better mental = +5% performance)
- Time in job (+5 per semester, max +20)
- **Burnout penalty (-1.5 per burnout point)**

**Impact:**
- Determines promotion eligibility
- Affects salary growth
- Visibility: manager notices if performance drops

### 3. Burnout System (0-100)

**Accumulation:**
- Job stress → burnout (15% conversion rate)
- High-tier jobs have higher burnout multiplier:
  - Entry level: 0.8x (lower stress)
  - Mid: 1.0x
  - High: 1.3x (demanding roles)
  - Startup: 1.6x (chaotic, high-stress)

**Recovery:**
- Health reduces burnout (better health = faster recovery)
- Therapy sessions reduce burnout immediately
- Rest/low-stress periods gradually recover

**Consequences:**
- Burnout > 60: Warning story ("You're Overwhelmed")
- Burnout > 85: CRITICAL story + immediate health penalties
- Reduces health/mental health per semester (can become cycle of decay)

### 4. Earnings Calculation

```
Base Annual Salary × Hours/Week × 52 weeks = Annual Salary
Annual Salary ÷ 52 weeks ÷ Hours/Week = Hourly rate

Semester Earnings = Base Salary × Hours/Week × 16 weeks
```

**Example:**
- Junior Dev at $65k/year, 10 hrs/week
- Semester earnings = $65,000 × 10 × 16 ÷ 52 = $20,000

**Modifiers:**
- Performance rating affects raise frequency
- Promotions jump salary by 20-30%
- No limit on raises (merit-based)

### 5. Career Progression Timeline

**Year 1-2:** Entry level
- Start at entry job (barista, retail, TA, etc)
- Build network and skills
- Can't skip levels

**Year 2-3:** Mid-tier
- Promotion to mid-tier role (+20% salary)
- Performance matters more
- Network effects visible

**Year 3-4:** Senior/Lead
- Final promotion to leadership (+25% salary)
- Can manage others
- Higher stress, higher reward

---

## Interconnections to Other Systems

### 💪 Health → Career Performance
- Poor health = lower performance rating = harder to get promoted
- Burnout reduces mental health
- Health recovery helps reduce burnout

### 📚 Education → Career Options
- GPA requirements unlock better jobs
- Better major → better starting position
- Education affects long-term career ceiling

### 💰 Career → Finance
- Earnings add to player balance
- Burnout → therapy costs (health system)
- High salary = less loan pressure
- Financial stress can cause burnout (future mechanic)

### 📈 Career → Stats
- Career advancement raises confidence
- Burnout lowers motivation
- Leadership roles increase charisma

---

## Achievements (Career Milestones)

| Achievement | Trigger | Reward |
|---|---|---|
| **First Promotion** 📈 | Get 1st promotion | Unlocked |
| **Climber** 🚀 | Get 5+ promotions | Special prestige |
| **Six Figures! 💰** | Reach $100k salary | +5% all earnings |
| **Manager / Lead** 👔 | Reach leadership role | Unlocks opportunities |
| **Work-Life Balance** ⚖️ | Keep burnout < 30 all semester | +5 mental health |
| **Resilient** 💪 | Recover from severe burnout | +10 willpower |
| **Employee of Semester** ⭐ | Maintain 95+ performance | Raise unlocked |

---

## Career Stories (15 Narrative Moments)

### 🎯 Positive Triggers
- **"First Day"** - Starting first job (hopeful)
- **"First Paycheck"** - Earned your first money (triumphant)
- **"Congratulations!"** - Promotion announced (triumphant + mental health +5)
- **"You've Come Far"** - Reflection at 3+ promotions (reflective)

### ⚠️ Warning Triggers
- **"Something's Off"** - Burnout > 60 (cautionary)
- **"Sick Days Add Up"** - Health < 40 while working (cautionary)
- **"Is It Worth It?"** - High salary but high burnout (reflective)

### 🚨 Critical Triggers
- **"You Need Help"** - Burnout > 85 (urgent)

---

## API Endpoints

### Career Actions
```
POST /career/accept-job
  {player_id, job_id}
  → {job_title, salary, message}

POST /career/check-promotion
  {player_id}
  → {success, new_title, raise_amount, achievements_unlocked}

POST /career/raise
  {player_id, amount}
  → {old_salary, new_salary, cumulative_raises}

POST /career/update-semester
  {player_id}
  → {performance, burnout, health_impact, achievements_unlocked}

POST /career/burnout-therapy
  {player_id, therapy_effectiveness}
  → {old_burnout, new_burnout, reduction}
```

### Career Info
```
GET /career/{player_id}/summary
  → {current_job, performance, burnout, career_stats, achievements, next_promotion_eligible}

GET /career/{player_id}/earnings
  → {gross_semester_earnings, hours_per_week, performance_multiplier}

GET /career/{player_id}/history
  → {history[{event_type, job_title, semester, salary_before, salary_after, reason}]}
```

---

## Design Decisions

### Why Time-Gating Promotions?
Without minimum semester requirement, players could:
- Save up performance, get 3 promotions instantly
- Game the system by job-hopping

**Solution:** Must be in role for 2+ semesters before eligible. After promotion, can't get another for 3 semesters.

### Why Burnout Affects Health?
Realistic: Burnout causes actual health problems
- Sleep disruption
- Increased illness (weakened immune)
- Depression/anxiety (mental health drop)

Teaches: **Can't ignore your wellbeing** for career

### Why High-Tier Jobs Have Higher Burnout?
Realistic: CEO roles ARE more stressful
- More responsibility
- More hours
- More pressure

Teaches: **Success has tradeoffs** - more money but less time/health

### Why Performance Depends on Health?
Realistic: You can't excel if exhausted
- Decision-making suffers
- Attendance/punctuality issues
- Creativity drops

Teaches: **Wellbeing drives success**, not just hard work

---

## Teen Teaching Moments

### Lesson 1: Delayed Gratification
"You worked hard for 2 semesters. Your promotion is earned, not instant."

### Lesson 2: Tradeoffs
"Higher salary is great, but you're burning out. Is it worth it?"

### Lesson 3: Interconnected Life
"Your health affects your job. Your job affects your health. They're connected."

### Lesson 4: Skill > Luck
"Getting promoted isn't random - it's GPA, performance, and consistency."

### Lesson 5: Help-Seeking
"When burnout hits 85, you NEED to get help. Ignoring it makes it worse."

### Lesson 6: Life Decisions Matter
"Starting with retail at 14 still gives you path to $100k+ career by 22."

---

## Example Teen Journey

```
SEMESTER 1-2: Entry Level
- Age 17-18, High school GPA 3.2
- Gets barista job ($15/hr)
- Earns $4,800 this semester
- Burnout: 5 (low, relaxed job)
- Performance: 52 (GPA helps)
- Story: "First Paycheck" ✓

SEMESTER 3: Better Opportunity
- Switches to IT Helpdesk ($19/hr, campus)
- More hours, but better network
- Burnout: 15 (more demanding)
- Performance: 58 (higher GPA now 3.4)
- Story: None yet

SEMESTER 5: First Promotion!
- Gets promoted to Junior Developer
- $65k salary (vs $19/hr)
- Burnout: 25 (higher tier = higher stress)
- Performance: 72 (meets requirement)
- Achievement: "First Promotion" unlocked 📈
- Story: "Congratulations!" ✓
- Message: Salary +$30k - this feels real

SEMESTER 8: Warning Signs
- Still Junior Dev (can't promote yet)
- Working overtime (stress accumulating)
- Burnout: 68 (warning level)
- Performance: 65 (declining due to burnout)
- Story: "Something's Off" - manager notices

SEMESTER 9: Crisis
- Burnout reaches 82 (CRITICAL)
- Health dropped to 35
- Mental health: 42
- Story: "You Need Help" 🚨
- Decision point: Take action or spiral

SEMESTER 10: Recovery
- Goes to therapy
- Burnout reduces to 62
- Health recovering: 52
- Decides to stay in job (not job-hop)
- Performance slowly improving: 70

SEMESTER 12: Redemption
- Promotion eligible, meets all requirements
- Gets promoted to Software Developer
- Salary: $85k (+$20k from first promotion)
- Achievement: "Climber" 🚀 (2 promotions)
- Story: "You've Come Far"
- Burnout resets to 20 (new role, fresh start)

YEAR 4: Success
- Now at Senior Engineer ($110k)
- Promotions: 3
- Burnout managed below 40
- Health: 75, Fitness: 80
- Realized: Consistency > Speed
- Learned: Health = Performance = Career
```

**Teaching outcome:** Player sees that:
1. Burnout is real and has consequences
2. Getting help matters (not weakness)
3. Promotions are earned, not given
4. Health affects career success
5. Salary grows with effort, not luck
6. Long-term thinking beats short-term grinding

---

## Next: Integration with Other Systems

### Priority: Connect Career to GPA
- Burnout should impact grades (studying harder to focus)
- Career stress reduces time available for classes
- Time management becomes real decision

### Future: Career Affects Relationships
- Overwork makes dating harder
- Relationships provide stress relief (reduce burnout)
- Need to balance career and personal life

### Future: Financial Impact
- Earnings pay loans directly
- High salary reduces loan stress
- Financial security affects health

---

## Summary

Career Advancement & Progression is built to:
- ✅ Teach realistic career paths (4 tiers, must earn advancement)
- ✅ Model work-life balance (higher pay = burnout risk)
- ✅ Connect to health (burnout affects performance and health)
- ✅ Connect to education (GPA unlocks opportunities)
- ✅ Celebrate progress (achievements, promotions, milestones)
- ✅ Tell stories (narrative context for mechanical outcomes)
- ✅ Drive engagement (progression feels earned, not arbitrary)

It's **realistic** (take 2+ semesters to get promoted), **fun** (achievements + stories), and **interconnected** (health matters, education matters, consistency matters).

For a 16-year-old player: *"This is how real careers actually work. I can see myself in this."*
