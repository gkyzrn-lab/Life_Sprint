# Life Sprint Onboarding & Tutorial System

## Overview

A comprehensive tutorial system for first-time players in Life Sprint. The onboarding system guides players through core game concepts and mechanics.

## Features

- **Tutorial Sequence**: 8 structured tutorial steps covering core concepts
- **Context-Specific Tutorials**: Tutorials recommended for specific game contexts (e.g., planning page, finance page)
- **Tooltips**: Inline help explaining key terms (GPA, stress, balance, etc.)
- **Progress Tracking**: Track which tutorials players have completed
- **Enable/Disable**: Players can toggle tutorial mode on/off at any time

## Core Concepts Covered

1. **Welcome** - Introduction to Life Sprint
2. **Time Budget** - Managing semester hours across activities
3. **Loans & Finance** - Understanding tuition, scholarships, and debt
4. **Housing** - Living costs and lifestyle trade-offs
5. **Work & Study Balance** - Part-time jobs vs. academic focus
6. **GPA & Academics** - How grades affect future prospects
7. **Stress & Burnout** - Managing workload and well-being
8. **Semester Planning** - Planning ahead to prevent chaos

## API Endpoints

### Fetch Tutorials

**GET** `/onboarding/tutorial-sequence`
- Returns the recommended tutorial sequence for first-time players
- Response includes all 8 tutorial steps with full metadata

**GET** `/onboarding/tutorial/{step_id}`
- Fetch a single tutorial step by ID
- Example: `/onboarding/tutorial/intro_welcome`

**GET** `/onboarding/tutorials/context/{context}`
- Fetch tutorials relevant to a specific context
- Contexts: `player_start`, `planning_page`, `finance_page`, `academics_page`, `job_selection`, `semester_begin`

### Fetch Tooltips

**GET** `/onboarding/tooltips`
- Fetch all available tooltips

**GET** `/onboarding/tooltip/{tooltip_id}`
- Fetch a single tooltip by ID
- Examples: `what_is_gpa`, `what_is_stress`, `what_is_balance`, `interest_explained`, `what_is_network`, `what_is_time_budget`

### Track Progress

**GET** `/onboarding/{player_id}/progress`
- Get player's tutorial progress
- Returns: completed steps, dismissed tooltips, tutorials enabled flag, completion percentage

**POST** `/onboarding/tutorial/complete`
```json
{
  "player_id": "uuid",
  "step_id": "intro_welcome"
}
```
- Mark a tutorial step as completed

**POST** `/onboarding/tooltip/dismiss`
```json
{
  "player_id": "uuid",
  "tooltip_id": "what_is_gpa"
}
```
- Mark a tooltip as dismissed (won't show again)

### Manage Tutorial Mode

**POST** `/onboarding/{player_id}/enable-tutorials`
- Re-enable tutorials for a player

**POST** `/onboarding/{player_id}/disable-tutorials`
- Disable tutorials for a player

## Integration with Player Model

When a new player is created via `POST /player/start`, the player object includes:

```python
tutorial_state: TutorialState = {
    completed_steps: [],
    dismissed_tooltips: [],
    tutorials_enabled: True,
    current_focus: None
}
```

## Example Flow

### 1. Create a Player
```bash
curl -X POST http://localhost:8000/player/start \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice",
    "college_id": "nyc_public",
    "major_id": "cs",
    "housing_option_id": "dorm"
  }'
```
→ Response includes `tutorial_state` with tutorials enabled

### 2. Get Recommended Sequence
```bash
curl http://localhost:8000/onboarding/tutorial-sequence
```
→ Returns 8 tutorial steps in recommended order

### 3. Show Tutorial to Player
```bash
curl http://localhost:8000/onboarding/tutorial/intro_welcome
```
→ Returns step details: title, description, action hint

### 4. Player Completes Tutorial
```bash
curl -X POST http://localhost:8000/onboarding/tutorial/complete \
  -H "Content-Type: application/json" \
  -d '{
    "player_id": "player-uuid",
    "step_id": "intro_welcome"
  }'
```
→ Progress updates to 12.5% (1 of 8 steps)

### 5. Show Context-Specific Help
When player visits planning page:
```bash
curl http://localhost:8000/onboarding/tutorials/context/planning_page
```
→ Returns relevant tutorials for that page

### 6. Inline Tooltips
When player hovers over "GPA" label:
```bash
curl http://localhost:8000/onboarding/tooltip/what_is_gpa
```
→ Returns tooltip explanation

## Implementation Details

### Files

- **[core_domain/tutorial.py](../core_domain/tutorial.py)** - Tutorial definitions, tooltips, and lookup functions
- **[api/router_onboarding.py](../api/router_onboarding.py)** - FastAPI router with all tutorial endpoints
- **[core_domain/player/player_model.py](../core_domain/player/player_model.py)** - Updated Player model with `tutorial_state` field
- **[main.py](../main.py)** - Registered onboarding router
- **[tests/test_onboarding.py](../tests/test_onboarding.py)** - 11 comprehensive tests

### Key Classes

**TutorialStep**
```python
class TutorialStep:
    step_id: str              # unique ID
    title: str                # human-readable title
    description: str          # detailed explanation
    context: str              # where shown (e.g. "planning_page")
    priority: int             # ordering (higher = earlier)
    action_hint: Optional[str] # UI hint for next action
```

**Tooltip**
```python
class Tooltip:
    tooltip_id: str           # unique ID
    label: str                # short label for UI
    content: str              # detailed explanation
    related_concept: str      # link to tutorial step
```

**TutorialState** (on Player)
```python
class TutorialState:
    completed_steps: List[str]      # IDs of completed steps
    dismissed_tooltips: List[str]   # IDs of dismissed tooltips
    tutorials_enabled: bool         # can be toggled by player
    current_focus: Optional[str]    # highlight a specific concept
```

## Testing

Run onboarding tests:
```bash
pytest tests/test_onboarding.py -v
```

All 11 tests verify:
- Tutorial retrieval and metadata
- Tutorial progress tracking
- Tooltip management
- Context-specific recommendations
- Player initialization with tutorial state
- Enable/disable functionality

## Future Enhancements

- Add video tutorials or interactive walkthroughs
- Track which tutorials help players most (telemetry)
- Adaptive tutorials based on player behavior (show additional help if struggling)
- Localization support for international players
- Difficulty-based tutorial variations (harder topics for advanced players)
- Optional "master class" tutorials for advanced strategies
