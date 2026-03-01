# Health System

## Overview

The Health System is a comprehensive gamified health and wellness mechanic that tracks physical fitness, mental health, preventive care, and medical conditions. Players must balance exercise, therapy, checkups, and rest to maintain their health while managing costs and time.

### Core Features

- **Physical Fitness**: Exercise tracking with 4 activity types
- **Mental Health**: Therapy and counseling options
- **Preventive Care**: Medical checkups and screenings
- **Health Conditions**: Illnesses and injuries with impacts on GPA and health
- **Achievement System**: 11 achievements across 4 tiers (Bronze → Platinum)
- **Streak Tracking**: Exercise streaks with multiplier bonuses
- **Story Integration**: 15+ narrative moments tied to health choices
- **Insurance System**: Cost reduction for medical expenses

---

## Health Metrics

### Primary Stats

1. **Health** (0-100)
   - Overall physical well-being
   - Decays without exercise (-10 per semester)
   - Affected by illnesses and conditions
   - Influences illness probability

2. **Fitness** (0-100)
   - Physical conditioning level
   - Improved through exercise
   - Multiplies exercise effectiveness
   - Reduces illness probability

3. **Mental Health** (0-100)
   - Psychological well-being
   - Improved through therapy/meditation
   - Decays when stress > 50 without therapy
   - Affects happiness and stress recovery

4. **Sleep Quality** (0-100)
   - Rest and recovery metric
   - Impacted by stress and health conditions
   - Affects GPA and energy levels

### Gamification Stats

- **Current Exercise Streak**: Consecutive exercises
- **Best Exercise Streak**: All-time record
- **Streak Power**: 1.0 + (streak × 0.05) — multiplies fitness gains
- **Fitness Multiplier**: Base 1.0, increased by achievements
- **Stress Reduction Bonus**: Extra stress reduction per activity
- **Mental Health Efficiency**: Multiplier for therapy effectiveness
- **Illness Probability Reduction**: Percentage reduction (from achievements)
- **GPA Health Bonus**: Direct GPA boost from health achievements
- **Checkup Cost Reduction**: Percentage discount on checkups
- **Illness Severity Reduction**: Reduces duration and health loss
- **Permanent Health Regen**: Passive per-semester recovery
- **All Health Multiplier**: Multiplies all health gains

---

## Exercise System

### Exercise Types

| Exercise Type | Cost | Fitness Gain | Mental Health | Notes |
|--------------|------|--------------|---------------|-------|
| **Campus Gym** | Free | +3 per session | — | Basic option, always available |
| **Running** | Free | +4 per session | — | Best free option |
| **Gym Membership** | $30/month | +5 per session | — | 4 sessions per month included |
| **Yoga** | $50/month | +3 per session | +5 per session | Mental health bonus |

### Streak Mechanics

1. **Building Streaks**
   - Each exercise increases streak by 1
   - Best streak tracked separately
   - Streak power: `1.0 + (current_streak × 0.05)`
   - Example: 5-day streak = 1.25× fitness gains

2. **Breaking Streaks**
   - Semester with zero exercises breaks streak
   - Best streak is preserved (all-time record)
   - Streak power resets to 1.0

3. **Streak Achievements**
   - **3-day streak**: "On Fire" 🔥 (Silver)
   - **7-day streak**: "Unstoppable" (Gold)

### Exercise Benefits

**Direct Effects:**
- Fitness: +3 to +5 (base) × streak_power × fitness_multiplier
- Health: +80% of fitness gain
- Stress: -2× fitness gain + stress_reduction_bonus
- Happiness: +5 per session

**Long-Term Benefits:**
- Reduces illness probability
- Improves GPA through health bonus
- Unlocks achievements
- Builds discipline and routine

---

## Mental Health & Therapy

### Therapy Options

| Therapy Type | Cost | Mental Health Gain | Stress Reduction | Notes |
|-------------|------|-------------------|------------------|-------|
| **Campus Counseling** | Free | +8 per session | -10 | Available to all students |
| **Professional Therapist** | $100/session | +10 per session | -15 | More effective |
| **Meditation App** | $10/month | +4 per session | -8 | Self-directed practice |

### When to Seek Therapy

**Recommended:**
- Stress > 60: Consider campus counseling
- Stress > 75: Urgent — see therapist
- Depression condition: Therapy reduces duration
- Academic pressure: Reduces GPA impact

**Benefits:**
- Mental health gain × mental_health_efficiency
- Stress reduction + stress_reduction_bonus
- Happiness +4 per session
- Health +60% of mental health gain
- Reduces depression condition duration

---

## Preventive Care

### Checkup Types

| Checkup | Base Cost | Insurance Cost | Health Gain | Notes |
|---------|-----------|----------------|-------------|-------|
| **Annual Checkup** | $200 | $120 | +10 | Comprehensive physical exam |
| **Teeth Cleaning** | $100 | $60 | +5 | Dental health |
| **Eye Exam** | $150 | $90 | +3 | Vision screening |

### Insurance System

- **Medical Insurance**: Reduces all medical costs by 40%
- Covers checkups, illness treatments, injuries
- Annual cost: $1,200 (included in living expenses)
- Highly recommended for severe conditions

### Preventive Care Strategy

**Optimal Schedule:**
- Annual Checkup: Once per year (Semester 1, 3, 5, 7)
- Teeth Cleaning: Every 6 months (Semester 1, 3, 5, 7)
- Eye Exam: As needed or with insurance

**Benefits:**
- Reduces random illness probability
- Unlocks "Preventive Pro" achievement (3 checkups)
- Peace of mind (story event)
- Early detection of conditions

---

## Health Conditions & Illnesses

### Common Conditions

| Condition | Severity | Duration | GPA Impact | Health Loss | Medical Cost | Notes |
|-----------|----------|----------|------------|-------------|--------------|-------|
| **Cold** | Mild | 1 week | -0.2 | -15 | $50 | Common, short duration |
| **Flu** | Moderate | 2 weeks | -0.4 | -25 | $100 | More severe, longer |
| **Sleep Deprivation** | Moderate | 4 weeks | -0.3 | -20 | $0 | From stress/overwork |
| **Depression** | Moderate | 12 weeks | -0.5 | -30 | $200 | Therapy reduces duration |
| **Broken Arm** | Severe | 8 weeks | -0.3 | -40 | $5,000 | Expensive injury |

### Illness Probability

**Base Formula:**
```
adjusted_probability = base_probability × fitness_modifier × health_modifier × achievement_reduction

fitness_modifier = (100 - fitness) / 100
health_modifier = (100 - health) / 100
achievement_reduction = 1.0 - illness_probability_reduction
```

**Example:**
- Base cold probability: 5%
- Fitness 80, Health 90, No achievements:
  - (5% × 0.20 × 0.10 × 1.0) = 0.1% chance
- Fitness 40, Health 50, No achievements:
  - (5% × 0.60 × 0.50 × 1.0) = 1.5% chance

**Prevention Strategies:**
1. Maintain fitness > 70
2. Maintain health > 80
3. Unlock "Clean Bill of Health" achievement (30% reduction)
4. Get regular checkups
5. Reduce stress through therapy

---

## Achievement System

### Bronze Tier (Entry-Level)

#### 1. First Workout 💪
**Requirement:** Complete your first exercise
**Reward:**
- Fitness multiplier: 1.05×
- Unlock: Gym membership discount
- Story: "The Endorphin Rush"

#### 2. Gym Rat 🏋️
**Requirement:** Complete 10 gym sessions
**Reward:**
- Gym membership: 20% cost reduction
- Permanent +5 health regen

#### 3. Preventive Pro 🩺
**Requirement:** Complete 3 medical checkups
**Reward:**
- Checkup costs: 15% reduction
- Illness severity: -10% reduction

---

### Silver Tier (Dedicated)

#### 4. 5K Runner 🏃
**Requirement:** Complete 5 exercises
**Reward:**
- Fitness multiplier: 1.10×
- Stress reduction: +5 per exercise

#### 5. Mental Health Advocate 🧠
**Requirement:** Attend 4 therapy sessions
**Reward:**
- Therapy cost: 15% reduction
- Mental health efficiency: 1.10×

#### 6. On Fire 🔥
**Requirement:** Achieve 3-day exercise streak
**Reward:**
- Permanent stress reduction: -2 per day
- Streak motivation bonus
- Story: "You're On Fire!"

---

### Gold Tier (Advanced)

#### 7. Workout Warrior ⚡
**Requirement:** Complete 20 exercises
**Reward:**
- Fitness multiplier: 1.15×
- Stress reduction: +8 per exercise

#### 8. Zen Master 🧘
**Requirement:** Attend 10 therapy sessions
**Reward:**
- Mental health efficiency: 1.20×
- Permanent stress reduction: -5

#### 9. Unstoppable 💥
**Requirement:** Achieve 7-day exercise streak
**Reward:**
- Fitness multiplier: 1.20×
- Unlock: Personal trainer role
- Story: "Unstoppable Force"

#### 10. Clean Bill of Health ✅
**Requirement:** Go 4 semesters without illness
**Reward:**
- Illness probability: -30% reduction
- Permanent +10 health

---

### Platinum Tier (Elite)

#### 11. Health Wisdom 🏆
**Requirement:** Combined achievement
- 10+ exercises
- 5+ therapy sessions
- 2+ medical checkups

**Reward:**
- All health multipliers: 1.20×
- GPA bonus: +0.15
- Unlock: Complete health mastery
- Story: "The Connection"

---

## API Endpoints

### Exercise

#### `POST /api/health/exercise`
Record an exercise session.

**Request:**
```json
{
  "player_id": "p1",
  "exercise_type": "running"
}
```

**Response:**
```json
{
  "exercise_type": "running",
  "fitness_gain": 5.2,
  "health_gain": 4.16,
  "stress_reduction": 12.4,
  "cost": 0.0,
  "total_exercises_this_semester": 1,
  "exercise_streak": {
    "streak_continuing": true,
    "current_streak": 1,
    "best_streak": 1,
    "streak_power": 1.05
  },
  "achievements_unlocked": [
    {
      "id": "first_workout",
      "title": "First Workout",
      "tier": "bronze",
      "message": "Your fitness journey begins! +5% fitness multiplier forever."
    }
  ],
  "story": {
    "id": "first_exercise_high",
    "title": "The Endorphin Rush",
    "message": "💪 You finish your workout and feel... different. Better...",
    "tone": "triumphant"
  }
}
```

---

### Therapy

#### `POST /api/health/therapy`
Attend therapy or mental health session.

**Request:**
```json
{
  "player_id": "p1",
  "therapy_type": "campus_counseling"
}
```

**Response:**
```json
{
  "therapy_type": "campus_counseling",
  "mental_health_gain": 8.8,
  "stress_reduction": 15.0,
  "cost": 0.0,
  "total_sessions": 1,
  "achievements_unlocked": [],
  "story": null
}
```

---

### Checkup

#### `POST /api/health/checkup`
Schedule medical checkup or preventive care.

**Request:**
```json
{
  "player_id": "p1",
  "checkup_type": "annual_checkup"
}
```

**Response:**
```json
{
  "checkup_type": "annual_checkup",
  "health_gain": 10.0,
  "cost": 120.0,
  "cost_before_insurance": 200.0,
  "insurance_savings": 80.0,
  "last_checkup_semester": 1,
  "achievements_unlocked": [],
  "story": {
    "id": "checkup_relief",
    "title": "Peace of Mind",
    "message": "The doctor says you're fine...",
    "tone": "reassuring"
  }
}
```

---

### Batch Actions

#### `POST /api/health/batch-actions`
Perform multiple health actions in one request.

**Request:**
```json
{
  "player_id": "p1",
  "actions": [
    {"type": "exercise", "exercise_type": "running"},
    {"type": "therapy", "therapy_type": "meditation"},
    {"type": "checkup", "checkup_type": "teeth_cleaning"}
  ]
}
```

**Response:**
```json
{
  "actions_performed": 3,
  "actions_failed": 0,
  "results": [
    {"action": "exercise", "success": true, "result": {...}},
    {"action": "therapy", "success": true, "result": {...}},
    {"action": "checkup", "success": true, "result": {...}}
  ],
  "total_cost": 60.0,
  "achievements_unlocked": [...],
  "stories_triggered": [...],
  "health_summary": {...}
}
```

---

### Health Summary

#### `GET /api/health/{player_id}/summary`
Get comprehensive health status.

**Response:**
```json
{
  "overall_status": "Excellent",
  "health": 92.5,
  "fitness": 78.3,
  "mental_health": 85.0,
  "sleep_quality": 70.0,
  "active_conditions": 0,
  "total_conditions_history": 12,
  "exercises_this_semester": 5,
  "therapy_sessions": 2,
  "medical_insurance": true,
  "gym_membership_active": false,
  "current_exercise_streak": 5,
  "best_exercise_streak": 7,
  "total_exercises_all_time": 23,
  "total_therapy_sessions_all_time": 8,
  "total_checkups_all_time": 3,
  "achievements_unlocked": 6,
  "streak_power": 1.25
}
```

---

### Achievement Progress

#### `GET /api/health/{player_id}/achievement-progress`
Get detailed achievement progress.

**Response:**
```json
{
  "total_achievements": 11,
  "unlocked_count": 3,
  "unlocked": [
    {
      "id": "first_workout",
      "title": "First Workout",
      "description": "Complete your first exercise",
      "tier": "bronze",
      "reward": "+5% fitness multiplier forever",
      "unlocked_semester": 1
    }
  ],
  "in_progress": [
    {
      "id": "5k_runner",
      "title": "5K Runner",
      "description": "Complete 5 exercises",
      "tier": "silver",
      "reward": "+10% fitness multiplier",
      "progress": "3/5 exercises",
      "current_value": 3,
      "target_value": 5,
      "percentage": 60.0
    }
  ],
  "locked": [...]
}
```

---

### Health History

#### `GET /api/health/{player_id}/history?limit=20`
Get timeline of health events.

**Response:**
```json
{
  "recent_events": [
    {
      "event_id": "exercise_5",
      "event_type": "exercise",
      "semester": 1,
      "severity": null,
      "health_impact": 4.16,
      "stress_impact": -10.4,
      "cost": 0.0
    },
    {
      "event_id": "therapy_2",
      "event_type": "therapy",
      "semester": 1,
      "severity": null,
      "health_impact": 5.28,
      "stress_impact": -15.0,
      "cost": 0.0
    }
  ],
  "total_events": 12,
  "event_counts": {
    "exercise": 5,
    "therapy": 2,
    "checkup": 1,
    "illness": 4
  },
  "current_conditions": []
}
```

---

### Streaks

#### `GET /api/health/{player_id}/streaks`
Get streak details and motivation.

**Response:**
```json
{
  "current_exercise_streak": 5,
  "best_exercise_streak": 7,
  "streak_fire_display": "🔥🔥",
  "streak_power": 1.25,
  "streak_message": "You're on fire! 7 days unlocks 'Unstoppable' achievement!",
  "exercises_all_time": 23
}
```

---

## Story Events

### Positive Moments

1. **"The Endorphin Rush"** — First exercise
   - +5 happiness, +3 mental health
   - Tone: Triumphant

2. **"You're On Fire! 🔥"** — 3-day streak
   - +8 confidence, +6 happiness
   - Tone: Empowering

3. **"The Connection"** — High health + GPA increase
   - +10 motivation, -5 stress
   - Tone: Revelatory
   - "Taking care of your body IS taking care of your future"

4. **"Someone Gets It"** — Therapy with high stress
   - -12 stress, +8 mental health, +7 happiness
   - Tone: Supportive

5. **"Peace of Mind"** — Checkup with relief
   - -8 stress, +5 health, +5 happiness
   - Tone: Reassuring

### Warning Moments

6. **"⚠️ You're Overwhelmed"** — Stress > 75
   - Unlock therapy reminder
   - Tone: Cautionary

7. **"🚨 BURNOUT ALERT"** — Stress > 85 + Health < 40
   - Force intervention, -0.3 GPA, emergency contact
   - Tone: Urgent

8. **"🤒 You're Not Feeling Well"** — Getting sick
   - Warning to rest
   - Tone: Cautionary

---

## Gameplay Strategies

### Early Game (Semesters 1-2)

**Focus: Build Foundation**

1. **Start Simple**: Use free campus gym or running
2. **Build Streak**: Aim for 3-day streak (On Fire achievement)
3. **Mental Health**: Use free campus counseling if stress > 60
4. **First Checkup**: Get annual checkup Semester 1 (with insurance)

**Weekly Routine:**
- Monday: Running (free, +4 fitness)
- Wednesday: Campus gym (free, +3 fitness)
- Friday: Running again
- As needed: Campus counseling (stress management)

**Expected Costs:** $0-10/week (all free options)

---

### Mid Game (Semesters 3-5)

**Focus: Optimize & Achieve**

1. **Upgrade Exercise**: Consider gym membership if you exercise 4+ times/month
2. **Mental Health Investment**: If stress consistently > 60, consider meditation app ($10/month)
3. **Streak Building**: Aim for 7-day streak (Unstoppable achievement)
4. **Preventive Care**: Schedule teeth cleaning + annual checkup

**Weekly Routine:**
- Mon/Wed/Fri: Gym membership workouts (+5 fitness each)
- Tuesday/Thursday: Meditation app (-8 stress each)
- Semester 3/5: Annual checkup + teeth cleaning

**Expected Costs:** $40-60/month (gym + meditation + insurance)

---

### Late Game (Semesters 6-8)

**Focus: Mastery & Platinum**

1. **Platinum Goal**: Work toward Health Wisdom (10 exercises, 5 therapy, 2 checkups)
2. **Advanced Exercise**: Add yoga for mental health bonus
3. **Professional Therapy**: If needed for severe stress/depression
4. **Maintain Streaks**: Protect your best streak record

**Weekly Routine:**
- Mon/Tue/Thu/Fri: Varied exercises (running, gym, yoga)
- Wednesday: Professional therapy if needed
- Maintain all preventive care appointments

**Expected Costs:** $50-150/month (premium options)

---

### Achievement Hunting

**Bronze Tier (Easy):**
- First Workout: Automatic first exercise
- Preventive Pro: 3 checkups over 2 years
- Gym Rat: 10 gym sessions (3 months)

**Silver Tier (Medium):**
- 5K Runner: 5 exercises (2 weeks if consistent)
- Mental Health Advocate: 4 therapy sessions (1 semester)
- On Fire: 3-day streak (1 week)

**Gold Tier (Hard):**
- Workout Warrior: 20 exercises (2 semesters)
- Zen Master: 10 therapy sessions (2 semesters)
- Unstoppable: 7-day streak (1 week intense)
- Clean Bill of Health: 4 semesters no illness (maintain high fitness/health)

**Platinum Tier (Elite):**
- Health Wisdom: Combined 10/5/2 (2-3 semesters focused effort)

---

### Cost Management

**Free Options:**
- Campus gym: $0
- Running: $0
- Campus counseling: $0
- Total: $0/month

**Budget Options ($30-50/month):**
- Gym membership: $30/month
- Meditation app: $10/month
- Medical insurance: $100/month (required)
- Total: $140/month

**Premium Options ($100-200/month):**
- Yoga: $50/month
- Professional therapist: $100/session
- All checkups: $200-400/semester with insurance
- Total: $150-300/month

**Insurance ROI:**
- Without insurance: $200 checkup + $5,000 broken arm = $5,200
- With insurance ($100/month): $120 checkup + $3,000 broken arm = $3,120
- Savings on serious condition: $2,000+

---

## Technical Implementation

### Service Functions

Located in `/health/service.py`:

1. **`exercise_session()`** — Process exercise with streaks & achievements
2. **`attend_therapy()`** — Process therapy with efficiency multipliers
3. **`schedule_checkup()`** — Process checkup with insurance
4. **`apply_health_condition()`** — Apply illness/injury
5. **`check_achievements()`** — Check all 11 achievement unlock conditions
6. **`get_achievement_progress()`** — Calculate progress toward locked achievements
7. **`get_health_history()`** — Return timeline of health events
8. **`get_health_summary()`** — Comprehensive health status
9. **`update_exercise_streak()`** — Streak tracking logic
10. **`trigger_health_stories()`** — Story event system
11. **`perform_batch_health_actions()`** — Multiple actions in one call
12. **`progress_health_semester()`** — End-of-semester changes

### Data Models

Located in `/core_domain/health/health_models.py`:

- **`Health`** — Main health data class
- **`HealthCondition`** — Active illness/injury
- **`HealthHistory`** — Historical event record
- **`Achievement`** — Unlocked achievement

### API Router

Located in `/api/router_health.py`:
- 15 endpoints total
- Request/response models with validation
- Integration with STORE for persistence

### Catalogs

- **`catalogs/health.py`** — Exercise types, therapy options, conditions
- **`catalogs/health_achievements.py`** — 11 achievement definitions
- **`catalogs/health_stories.py`** — 15+ narrative moments

---

## Testing

Comprehensive test suite in `/tests/test_health.py`:

**Test Coverage:**
- Exercise sessions with streaks
- Achievement unlocking (all 11)
- Therapy effectiveness
- Checkup insurance calculations
- Health conditions and illness probability
- Batch actions
- Semester progression
- Integration tests (full health journey)

**Run Tests:**
```bash
pytest tests/test_health.py -v
```

---

## Balance & Design Philosophy

### Core Principles

1. **Accessibility**: Free options for all core activities
2. **Progressive Enhancement**: Paid options are better but not required
3. **Real Consequences**: Ignoring health has real GPA/stress impact
4. **Positive Reinforcement**: Stories celebrate good choices
5. **Warning System**: Clear signals before crisis (burnout alert)

### Balance Targets

- **Minimum Viable**: 1-2 free exercises/week + campus counseling = healthy
- **Optimal Play**: 3-4 exercises/week + meditation + annual checkup = excellent
- **Premium Play**: Daily exercise + professional therapy + all checkups = mastery

### Risk vs. Reward

**High Risk:**
- Ignoring health → Illness → GPA loss + medical costs
- Example: Broken arm costs $3,000 (with insurance) + 8 weeks recovery

**High Reward:**
- Health Wisdom achievement → +0.15 GPA + all multipliers
- Value: ~0.15 GPA = difference between 3.5 and 3.65 (scholarship threshold)

---

## Future Enhancements

Potential additions:

1. **Nutrition System**: Meal planning, dining hall choices
2. **Sleep Tracker**: Direct sleep quality management
3. **Social Exercise**: Group fitness classes, intramural sports
4. **Wearable Integration**: Fitness tracker mini-game
5. **Recovery System**: Active recovery, foam rolling, massage
6. **Competition Events**: 5K races, fitness challenges
7. **Health Goals**: Player-set targets with rewards
8. **Seasonal Variations**: Summer training, winter indoor options

---

## Conclusion

The Health System provides deep, engaging mechanics that mirror real college health challenges. Through achievements, streaks, and stories, players learn that taking care of their body and mind is essential to academic success. The system rewards consistency, offers accessible free options, and creates meaningful consequences for neglect — all while maintaining the fun, gamified experience that makes Life Sprint engaging.

**Key Takeaway:** Your character's health is not separate from their success — it's foundational to it. 🏆
