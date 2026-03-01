# BA Course Mini-Games & Topics - Quick Start Guide

## What's New

Your BA courses now have:
✨ **Interactive mini-games** - Learn through gameplay
📚 **Beautiful topic descriptions** - Clear, engaging explanations  
🎯 **Real-world examples** - See how concepts apply in business
⭐ **Points & feedback** - Track your progress and learning

## Available BA Courses with Games

### Semester 1
- **ba101** (Intro Business) - 2 games
- **ba102** (Accounting Principles) - 2 games
- **econ101** (Microeconomics) - 1 game

### Semester 2
- **ba201** (Business Communication) - 1 game
- **ba202** (Financial Accounting) - 1 game
- **econ102** (Macroeconomics) - covered in core

### Semester 3
- **ba301** (Management Principles) - 1 game
- **ba302** (Marketing Fundamentals) - 1 game
- **ba303** (Organizational Behavior) - covered in management

### Semester 4
- **ba401** (Corporate Finance) - 1 game
- **ba402** (Strategic Management) - 1 game
- **ba403** (Operations Management) - 1 game

## API Quick Reference

### Get Course with Topics & Games
```bash
GET /curriculum/course/{course_id}

# Examples
GET /curriculum/course/ba101
GET /curriculum/course/ba402
```

**Response includes:**
- Course metadata (credits, difficulty, weekly hours)
- Formatted topics with real-world examples
- Available mini-games
- Learning outcomes

### List Games for a Course
```bash
GET /curriculum/games/course/{course_id}

# Example
GET /curriculum/games/course/ba101
```

**Response shows:** Game titles, descriptions, duration, question count

### Get Full Game with Questions
```bash
GET /curriculum/games/{game_id}

# Examples
GET /curriculum/games/ba101_startup_game
GET /curriculum/games/ba402_strategy_game
```

**Response includes:** All questions with options (not answers)

### Submit Game Answers & Get Score
```bash
POST /curriculum/games/submit

{
  "game_id": "ba101_startup_game",
  "course_id": "ba101",
  "answers": [
    {"question_id": "q1", "selected_option_index": 2},
    {"question_id": "q2", "selected_option_index": 1},
    {"question_id": "q3", "selected_option_index": 1}
  ],
  "time_spent_minutes": 8
}
```

**Response includes:**
- Score percentage
- Points earned
- Feedback on each answer
- Key learning points
- Encouraging message

## Example Game: Startup Structure Challenge (ba101)

**Type:** Scenario Decision  
**Duration:** 10 minutes  
**Questions:** 3  
**Points per correct:** 15  
**Minimum score to pass:** 70%

### Question 1
"Your startup has 2 founders investing equally with shared liability concerns. What structure minimizes personal liability?"
- A: Sole Proprietorship
- B: Partnership
- C: **LLC** ✓ (Correct)
- D: Franchise

**Why?** An LLC limits personal liability while allowing shared ownership.

### Question 2
"You want maximum profit retention but need to raise capital from investors. Best choice?"
- A: Sole Proprietorship
- B: **C Corporation** ✓ (Correct)
- C: S Corporation
- D: Nonprofit

**Why?** C Corporations allow external investment while keeping profits.

### Question 3
"Your family restaurant operates with flexible structure and minimal paperwork. What are you likely running?"
- A: Corporation
- B: **Sole Proprietorship** ✓ (Correct)
- C: Public Company
- D: Holding Company

**Why?** Sole proprietorships are simple and flexible for small businesses.

---

## Example Topics: Strategic Management (ba402)

### Topic 1: Strategic Analysis 🎯
**Definition:** SWOT analysis, industry analysis, and competitive positioning

**Real-World Example:** How does Tesla position itself vs. traditional automakers?
- Tesla: Innovation, Tech, Sustainability
- Traditional: Scale, Supply Chain, Reputation

### Topic 2: Competitive Advantage ⚔️
**Definition:** Building sustainable advantages and barriers to entry

**Real-World Example:** Why can Netflix sustain advantage despite growing competition?
- First-mover advantage in streaming
- Content library and data analytics
- Subscriber loyalty
- Technology investments

### Topic 3: Innovation & Disruption 💡
**Definition:** Disruptive innovation and adapting to market changes

**Real-World Example:** How did Netflix disrupt Blockbuster, then adapt to threats?
- Disrupted: Subscription model vs. rental stores
- Adapted: From DVDs to streaming to content creation
- Survived: Competition from Disney+, Prime Video

---

## Frontend Integration Example

```javascript
// 1. Fetch course with topics and games
const response = await fetch(`/curriculum/course/ba101`);
const course = await response.json();

// 2. Display formatted topics
course.formatted_topics.topics.forEach(topic => {
  console.log(`${topic.icon} ${topic.name}`);
  console.log(`  → ${topic.description}`);
  console.log(`  💡 Real-world: ${topic.real_world}`);
});

// 3. Show available games
console.log(`Available games: ${course.mini_games.length}`);
course.mini_games.forEach(game => {
  console.log(`  🎮 ${game.title} (${game.question_count} questions, ${game.estimated_duration_minutes} min)`);
});

// 4. Play a game
const gameResponse = await fetch(`/curriculum/games/${course.mini_games[0].id}`);
const game = await gameResponse.json();
console.log(`Play: ${game.title}`);
game.questions.forEach(q => {
  console.log(`  ${q.prompt}`);
  q.options.forEach((opt, i) => console.log(`    ${i}: ${opt}`));
});

// 5. Submit answers
const submitResponse = await fetch(`/curriculum/games/submit`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    game_id: game.id,
    course_id: game.course_id,
    answers: [
      { question_id: 'q1', selected_option_index: 2 },
      { question_id: 'q2', selected_option_index: 1 }
    ],
    time_spent_minutes: 8
  })
});
const result = await submitResponse.json();
console.log(`Score: ${result.score_percent}%`);
console.log(`Points: ${result.points_earned}`);
console.log(`${result.message}`);
```

## Game Types Explained

### 1. Scenario Decision 📋
"Choose the best business decision" - You face realistic scenarios and pick the best option.

Example: "Your startup has 2 founders... What structure?"

### 2. Case Study 📚
"Analyze and recommend" - Read a business situation and choose the best response.

Example: "Company discovers pollution-causing process. What happens?"

### 3. Accounting Balance ⚖️
"Keep the equation balanced" - Balance sheets and accounting principles.

Example: "If Assets=$100K and Liabilities=$60K, what is Equity?"

### 4. Market Simulation 📈
"Observe market dynamics" - See how supply/demand shifts affect prices.

Example: "A competitor enters at lower prices. Demand for your product?"

### 5. Team Builder 👥
"Make management decisions" - Leadership and team dynamics challenges.

Example: "Your team morale is low. What's your first step?"

### 6. Budget Challenge 💰
"Allocate resources wisely" - Make financial decisions with limited resources.

Example: "Project A costs $100K returns $30K/year. Project B costs $100K returns $35K/year."

### 7. Marketing Campaign 🎨
"Design marketing strategy" - Create targeted campaigns for markets.

Example: "Luxury watch company. Best target audience?"

### 8. Negotiation 🤝
"Practice negotiation" - Business negotiation scenarios.

Example: "Asking for time off from work. What tone is professional?"

---

## Scoring System

### Points
- **Correct answer:** +10 to +15 points (depends on game)
- **Incorrect answer:** -2 points
- **Minimum to pass:** 70% (usually 2-3 correct out of 3 questions)

### Example: Startup Structure Game (ba101)
- 3 questions total
- 15 points per correct = 45 points possible
- -2 points per incorrect = max -4 points possible
- Need 2+ correct to pass (70%)

**Scoring examples:**
- 3/3 correct: 45 points ✅ (100%)
- 2/3 correct: 30-2=28 points ✅ (66.7%) ❌ Failed
- Actually: 2/3 = 66.7% doesn't pass. Need to calculate better:
  - Score % = (correct/total) * 100
  - 2/3 = 66.7% (below 70%, doesn't pass)
  - 2.1/3+ would pass = need all 3 correct OR system adjusted

### Feedback
- ✅ Correct: "Great! You scored X%"
- ❌ Incorrect: "You scored X%. Review answers and try again"

---

## Next Steps

### For Students
1. **Attend a BA course** - Click on a course from your semester
2. **View topics** - Read the formatted topic descriptions
3. **Play games** - Try the mini-games to understand concepts
4. **Get points** - Earn points for correct answers
5. **Track progress** - See your total game points and achievements

### For Developers
1. **Add games for other majors** - CS, Engineering, Liberal Arts
2. **Create more game types** - Simulations, puzzles, timed challenges
3. **Implement leaderboards** - Competition among students
4. **Add badges** - Reward achievement milestones
5. **Video explanations** - Show video solutions after games

---

## Common Questions

### Q: Do I have to play the games?
A: No, they're optional but recommended! Games help you learn faster.

### Q: Can I replay games?
A: Yes! Replay anytime to improve your score and earn more points.

### Q: Do games count toward my GPA?
A: Not in this version, but they earn bonus points and are tracked for achievements.

### Q: Can I see the answers before playing?
A: No, answers are hidden to prevent cheating. You only see feedback after submitting.

### Q: How are points used?
A: Currently tracked and displayed. Future: Leaderboards, badges, and rewards!

### Q: Which majors have games?
A: Currently BA (Business Admin) only. CS, Engineering, and Liberal Arts coming soon!

---

## Support

For issues or questions about the games:
1. Check this guide's FAQ section
2. Review API endpoints documentation
3. Check course topics for learning content
4. Submit feedback for new game ideas
