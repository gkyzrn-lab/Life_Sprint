# Course Content Examples - Brief Info & Quiz Samples

This document shows example content for newly added courses to demonstrate the "brief info pop-up" data and quiz alignment.

---

## Computer Science Examples

### CS350: Senior Capstone Project I

**Brief Info** (from curriculum):
- **Name**: Senior Capstone Project I
- **Description**: Start building a substantial software project. Apply everything you've learned.
- **Skills**: Project management, Full-stack development
- **Real-World Application**: Portfolio piece for job applications
- **Credits**: 3 | **Difficulty**: Advanced

**Topics Covered**:
1. Project Planning
2. Requirements Analysis
3. System Design
4. Implementation
5. Team Collaboration

**Sample Quiz Question**:
> **Q**: A well-defined project scope includes:
> - Clear objectives and deliverables ✓
> - Only deadlines
> - No constraints
> - Just ideas
>
> **Explanation**: Scope defines what will and won't be delivered.

---

### CS400: Theory of Computation

**Brief Info** (from curriculum):
- **Name**: Theory of Computation
- **Description**: Formal languages, automata, and computational complexity. The theory behind computing.
- **Skills**: Theoretical CS, Complexity theory
- **Real-World Application**: Understand fundamental limits of computation
- **Credits**: 3 | **Difficulty**: Very High

**Topics Covered**:
1. Automata Theory
2. Formal Languages
3. Computability
4. Complexity Classes
5. Decidability

**Sample Quiz Questions**:

**Automata Quiz**:
> **Q**: A DFA has:
> - One start state and deterministic transitions ✓
> - Multiple start states
> - Non-deterministic transitions
> - No accept states
>
> **Explanation**: DFAs have exactly one transition per symbol from each state.

**Computability Quiz**:
> **Q**: The halting problem is:
> - Decidable
> - Undecidable ✓
> - Solvable in polynomial time
> - Trivial
>
> **Explanation**: No algorithm can determine if arbitrary programs halt.

---

## Business Administration Examples

### BUS410: Business Analytics

**Brief Info** (from curriculum):
- **Name**: Business Analytics
- **Description**: Data-driven decision making, predictive analytics, and business intelligence.
- **Skills**: Data analytics, Excel, Business intelligence
- **Real-World Application**: Hot skill - every company needs data-savvy people
- **Credits**: 3 | **Difficulty**: Medium

**Topics Covered**:
1. Data Analysis
2. Predictive Analytics
3. Business Intelligence
4. Data Visualization
5. Analytics Tools

**Sample Quiz Questions**:

**Data Analysis Quiz**:
> **Q**: Exploratory data analysis involves:
> - Summarizing and visualizing data to understand patterns ✓
> - Only hypothesis testing
> - Deploying models
> - Writing code
>
> **Explanation**: EDA discovers patterns before formal modeling.

**Predictive Analytics Quiz**:
> **Q**: Predictive analytics aims to:
> - Describe past data
> - Forecast future outcomes ✓
> - Only visualize
> - Replace decisions
>
> **Explanation**: Predictive analytics uses data to forecast future events.

---

### ENT401: Entrepreneurship

**Brief Info** (from curriculum):
- **Name**: Entrepreneurship
- **Description**: Start-up creation, business planning, and innovation.
- **Skills**: Entrepreneurial mindset, Business planning
- **Real-World Application**: Maybe you'll start your own company someday
- **Credits**: 3 | **Difficulty**: Medium

**Topics Covered**:
1. Opportunity Recognition
2. Business Planning
3. Funding and Valuation
4. Lean Startup
5. Growth Strategies

**Sample Quiz Question**:
> **Q**: A viable business opportunity requires:
> - Just an idea
> - Market need, feasibility, and profit potential ✓
> - Only capital
> - No competition
>
> **Explanation**: Opportunities must meet a need, be feasible, and offer returns.

---

## Engineering Examples

### ENGR301: Engineering Design I

**Brief Info** (from curriculum):
- **Name**: Engineering Design I
- **Description**: Design process, prototyping, and project planning.
- **Skills**: Design process, CAD, Prototyping
- **Real-World Application**: Turn ideas into physical products
- **Credits**: 3 | **Difficulty**: Medium

**Topics Covered**:
1. Design Process
2. Requirements Engineering
3. Concept Generation
4. Design Analysis
5. Prototyping

**Sample Quiz Question**:
> **Q**: The engineering design process typically includes:
> - Define, Research, Ideate, Prototype, Test, Refine ✓
> - Just build it
> - Copy existing designs
> - Skip testing
>
> **Explanation**: Systematic design follows iterative steps from problem to solution.

---

### ENGR410: Engineering Ethics

**Brief Info** (from curriculum):
- **Name**: Engineering Ethics
- **Description**: Professional responsibility, safety, and ethical decision-making.
- **Skills**: Professional ethics, Safety
- **Real-World Application**: Engineers have lives in their hands - ethics matter
- **Credits**: 3 | **Difficulty**: Medium

**Topics Covered**:
1. Professional Responsibility
2. Safety and Risk
3. Sustainability
4. Codes of Ethics
5. Case Studies

**Sample Quiz Question**:
> **Q**: Engineers' primary obligation is to:
> - Maximize profit
> - Protect public safety, health, and welfare ✓
> - Follow orders blindly
> - Avoid decisions
>
> **Explanation**: Engineers hold paramount the safety and welfare of the public.

---

### SPEC301: Specialization Course 1

**Brief Info** (from curriculum):
- **Name**: Specialization Course 1
- **Description**: Begin your specialization (Mechanical, Electrical, or Industrial Engineering).
- **Skills**: Specialization fundamentals, Technical analysis
- **Real-World Application**: Develop expertise in your chosen engineering field
- **Credits**: 3 | **Difficulty**: Medium

**Topics Covered**:
1. Specialization Fundamentals
2. Technical Depth
3. Industry Applications
4. Design Projects
5. Analysis Methods

**Sample Quiz Question**:
> **Q**: Engineering specializations allow you to:
> - Avoid math
> - Develop expertise in specific engineering domains ✓
> - Graduate faster
> - Take easier classes
>
> **Explanation**: Specializations build deep knowledge in areas like mechanical, electrical, civil, etc.

---

## How Frontend Should Display Course Info

### Pop-up/Modal Structure

When player hovers or clicks a course, show:

```
┌─────────────────────────────────────────────────┐
│  CS400: Theory of Computation                   │
│                                                 │
│  Formal languages, automata, and computational  │
│  complexity. The theory behind computing.       │
│                                                 │
│  Skills: Theoretical CS, Complexity theory      │
│                                                 │
│  Real-World: Understand fundamental limits of   │
│              computation                        │
│                                                 │
│  Topics:                                        │
│  • Automata Theory                              │
│  • Formal Languages                             │
│  • Computability                                │
│  • Complexity Classes                           │
│  • Decidability                                 │
│                                                 │
│  [Start Lessons] [Take Quiz]                    │
└─────────────────────────────────────────────────┘
```

### Data Sources

1. **Course metadata** → `GET /api/curriculum/{major}/semester/{semester}`
   - Returns: id, name, description, credits, difficulty, skills[], real_world

2. **Detailed topics & lessons** → `GET /api/curriculum/course/{course_id}/content`
   - Returns: title, topics[], lessons[], learning_outcomes[]

3. **Quizzes** → `GET /api/exams/course/{course_id}/quizzes`
   - Returns: quizzes[] with questions, options, correct_answer

---

## Quiz Grading Verification

All quizzes use **text-based answers** that match exactly with option strings:

```javascript
// Frontend grading logic (already implemented correctly in GameBoard.tsx)
const userAnswer = userAnswers[index]; // e.g., "One start state and deterministic transitions"
const correctAnswer = question.correct_answer; // e.g., "One start state and deterministic transitions"
const isCorrect = userAnswer === correctAnswer; // String comparison
```

**Important**: Both values are strings, comparison is case-sensitive and requires exact match.

---

## Content Statistics by Major

| Major | Courses | Quizzes | Questions | Avg Q/Course |
|-------|---------|---------|-----------|--------------|
| Computer Science | 23 | 54 | 162 | 7.0 |
| Business Admin | 27 | 51 | 153 | 5.7 |
| Engineering | 31 | 47 | 143 | 4.6 |
| **Total** | **81** | **152** | **458** | **5.7** |

---

## Status: COMPLETE ✓

All 81 unique courses across all three majors now have:
- ✓ Course title and description
- ✓ Topics list (5+ topics each)
- ✓ Lessons with content (2-5 lessons each)
- ✓ Quizzes with text-based answers (1-5 quizzes each)
- ✓ Learning outcomes (3-5 outcomes each)
- ✓ Aligned content (quizzes match course descriptions)

**Ready for in-game testing.**
