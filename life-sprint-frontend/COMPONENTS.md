# BitLife-Style Visual Components Documentation

## Overview

The Life Sprint frontend has been enhanced with BitLife-style visual components that create an engaging, game-like interface for the financial education game. All components follow a consistent color scheme and design language inspired by the popular BitLife game.

## Component Architecture

### 1. GameLayout (Main Container)
**File**: `GameLayout.tsx`

The main layout component that orchestrates the entire visual interface. It features a three-column layout with:
- **Top Info Bar**: Quick access to key stats (Age, Year, Net Worth, Health, Happiness)
- **Left Sidebar**: Character profile or timeline view
- **Center Content**: Age progression and life milestone display
- **Right Sidebar**: Navigation panels and quick stats

**Props**:
```typescript
interface GameLayoutProps {
  playerName: string
  age: number
  year: number
  stats: {
    health: number
    happiness: number
    intelligence: number
    attractiveness: number
  }
  finance: {
    cash: number
    savings: number
    investments: number
    loans: number
    netWorth: number
  }
}
```

**Usage**:
```tsx
<GameLayout
  playerName="Alex Chen"
  age={22}
  year={2024}
  stats={{ health: 75, happiness: 82, intelligence: 88, attractiveness: 72 }}
  finance={{ cash: 45000, savings: 15000, investments: 8000, loans: 32000, netWorth: 36000 }}
/>
```

---

### 2. CharacterCard
**File**: `CharacterCard.tsx`

Displays character statistics and profile information with dynamic stat bars.

**Features**:
- Character name and avatar
- Net worth display
- Four stat bars (Health, Happiness, Intelligence, Attractiveness)
- Color-coded stat values (green for high, red for low)
- Responsive avatar support

**Props**:
```typescript
interface CharacterCardProps {
  name: string
  stats: CharacterStats
  avatar?: string
}

interface CharacterStats {
  health: number
  happiness: number
  intelligence: number
  attractiveness: number
  age: number
  net_worth: number
}
```

**Usage**:
```tsx
<CharacterCard
  name="Alex Chen"
  stats={{
    health: 75,
    happiness: 82,
    intelligence: 88,
    attractiveness: 72,
    age: 22,
    net_worth: 36000
  }}
  avatar="https://example.com/avatar.png"
/>
```

---

### 3. AgeProgression
**File**: `AgeProgression.tsx`

Visual timeline showing the player's progression through life stages.

**Features**:
- Age and year display
- Life stage indicator (Childhood, Teen, Young Adult, etc.)
- Life progress bar with percentage
- Milestone markers (age 0, 13, 20, 30, 45, 65, 80)
- Years lived / Years remaining statistics
- Interactive milestones with emoji indicators

**Props**:
```typescript
interface AgeProgressionProps {
  currentAge: number
  currentYear: number
  lifeExpectancy?: number // Default: 80
}
```

**Usage**:
```tsx
<AgeProgression
  currentAge={22}
  currentYear={2024}
  lifeExpectancy={80}
/>
```

---

### 4. FinancialDashboard
**File**: `FinancialDashboard.tsx`

Comprehensive financial overview with assets, liabilities, and cash flow.

**Features**:
- Net worth prominently displayed
- Assets section (Cash, Savings, Investments)
- Liabilities section (Loans)
- Income/Expense breakdown
- Monthly balance calculation
- Color-coded values (green for positive, red for negative)
- Formatted currency display

**Props**:
```typescript
interface FinancialDashboardProps {
  data: FinancialData
  income?: number
  expenses?: number
}

interface FinancialData {
  cash: number
  savings: number
  investments: number
  loans: number
  netWorth: number
  salary?: number
}
```

**Usage**:
```tsx
<FinancialDashboard
  data={{
    cash: 45000,
    savings: 15000,
    investments: 8000,
    loans: 32000,
    netWorth: 36000,
  }}
  income={5000}
  expenses={2000}
/>
```

---

### 5. LifeTimeline
**File**: `LifeTimeline.tsx`

Timeline visualization of life events and achievements.

**Features**:
- Chronological event display
- Color-coded event types (Achievement, Career, Education, Relationship, Financial, Health)
- Age and year tracking for each event
- Event descriptions and icons
- Scrollable event history
- Hover effects and interactive elements

**Event Types & Colors**:
- 🏆 **Achievement**: Gold (#FFD700)
- 💼 **Career**: Blue (#4A9EFF)
- 📚 **Education**: Green (#7ED321)
- ❤️ **Relationship**: Red (#FF6B6B)
- 💰 **Financial**: Teal (#50E3C2)
- 💚 **Health**: Light Green (#A8E6CF)

**Props**:
```typescript
interface LifeTimelineProps {
  currentAge: number
  events: LifeEvent[]
}

interface LifeEvent {
  age: number
  year: number
  title: string
  description: string
  type: 'achievement' | 'career' | 'education' | 'relationship' | 'financial' | 'health'
  icon: string
}
```

**Usage**:
```tsx
<LifeTimeline
  currentAge={22}
  events={[
    { age: 18, year: 2020, title: 'College Start', description: 'Started college', type: 'education', icon: '🎓' },
    { age: 20, year: 2022, title: 'First Job', description: 'Internship at TechCorp', type: 'career', icon: '💼' },
    { age: 22, year: 2024, title: 'Graduation', description: 'Completed degree', type: 'achievement', icon: '🏆' },
  ]}
/>
```

---

### 6. DecisionCard
**File**: `DecisionCard.tsx`

Interactive choice presentation for life decisions.

**Features**:
- Decision title and description
- Optional image/illustration
- Multiple choice options with outcomes
- Stat consequence preview
- Click handler for decision selection
- Golden border styling for prominence

**Props**:
```typescript
interface DecisionCardProps {
  title: string
  description: string
  image?: string
  options: DecisionOption[]
  onSelect: (optionId: string) => void
}

interface DecisionOption {
  id: string
  text: string
  outcome?: string
  consequences?: {
    health?: number
    happiness?: number
    intelligence?: number
    attractiveness?: number
    money?: number
  }
}
```

**Usage**:
```tsx
<DecisionCard
  title="Career Choice"
  description="Choose your career path carefully."
  options={[
    { id: '1', text: 'Tech Industry', outcome: '+Intelligence, +Money' },
    { id: '2', text: 'Arts & Culture', outcome: '+Happiness, -Money' },
  ]}
  onSelect={(id) => console.log('Selected:', id)}
/>
```

---

## Design System

### Color Palette
- **Primary Accent**: #50E3C2 (Cyan/Teal)
- **Secondary Accent**: #7ED321 (Green)
- **Tertiary Accent**: #FFD700 (Gold)
- **Background Dark**: #1a1a2e (Dark Navy)
- **Background Medium**: #16213e (Medium Navy)
- **Background Light**: #0f3460 (Lighter Navy)
- **Highlight**: #FF6B6B (Red for negative values)

### Typography
- **Font Family**: System fonts (Apple system fonts, Segoe UI, Roboto)
- **Heading**: Bold, large (18-48px)
- **Body**: Regular, medium (13-16px)
- **Label**: Small, uppercase (11-12px)

### Spacing & Sizing
- **Gap Between Elements**: 12-20px
- **Component Padding**: 16-24px
- **Border Radius**: 8-12px
- **Border Width**: 1-2px

### Interactive Elements
- **Hover Effect**: Color change + slight scaling
- **Active State**: Gradient background + color inversion
- **Transition Time**: 0.3s ease

---

## Integration with Backend

The components are designed to work seamlessly with the Python backend:

### Financial System Integration
Components can pull data from the finance system (tax basics, budgeting, credit):
```tsx
const financialData = {
  cash: player.finance.balance,
  savings: player.finance.balance * 0.3,
  investments: player.finance.balance * 0.2,
  loans: player.finance.loan_balance,
  netWorth: player.finance.balance - player.finance.loan_balance,
}
```

### Event Tracking
Events are generated from player history and decisions:
```tsx
const events = player.history_events.map(event => ({
  age: event.age,
  year: event.year,
  title: event.title,
  description: event.description,
  type: event.type,
  icon: getEventIcon(event.type),
}))
```

### Decision Integration
Decisions trigger backend calculations:
```tsx
const handleDecision = async (optionId: string) => {
  const result = await api.submitDecision({
    player_id: player.id,
    decision_id: currentDecision.id,
    option_id: optionId,
  })
  // Update UI with consequences
  updatePlayerStats(result.player)
}
```

---

## Responsive Design

All components are designed to be responsive:
- **Desktop** (1400px+): Full three-column layout
- **Tablet** (1024-1400px): Two-column layout
- **Mobile** (< 1024px): Single column with stacked components

### Mobile Optimization
```css
@media (max-width: 1024px) {
  .main-layout {
    grid-template-columns: 1fr;
  }
  .sidebar-left,
  .sidebar-right {
    display: none;
  }
}
```

---

## CSS Styling Files

Each component has an associated CSS file:
- `CharacterCard.css` - Profile stats display
- `AgeProgression.css` - Timeline and life stage
- `FinancialDashboard.css` - Money and assets
- `LifeTimeline.css` - Event history
- `DecisionCard.css` - Choice presentation
- `GameLayout.css` - Main container layout

---

## Accessibility Considerations

- High contrast color schemes for readability
- Clear visual hierarchy
- Descriptive labels for all interactive elements
- Keyboard navigation support
- ARIA labels where appropriate (to be added)

---

## Future Enhancements

- [ ] Character customization with multiple avatars
- [ ] Animated transitions between states
- [ ] Sound effects for events and decisions
- [ ] Achievement badges and unlockables
- [ ] Multiplayer leaderboards
- [ ] Save/Load game states
- [ ] Minimap for life overview
- [ ] Extended statistics panel

---

## Examples

### Complete Game Interface
```tsx
import { GameLayout } from './components'

export function LifeSprintGame() {
  const [player, setPlayer] = useState(defaultPlayer)

  return (
    <GameLayout
      playerName={player.name}
      age={player.age}
      year={player.year}
      stats={{
        health: player.stats.health,
        happiness: player.stats.happiness,
        intelligence: player.stats.intelligence,
        attractiveness: player.stats.attractiveness,
      }}
      finance={{
        cash: player.finance.cash,
        savings: player.finance.savings,
        investments: player.finance.investments,
        loans: player.finance.loans,
        netWorth: player.finance.netWorth,
      }}
    />
  )
}
```

### Custom Dashboard
```tsx
import { CharacterCard, FinancialDashboard, LifeTimeline } from './components'

export function CustomDashboard() {
  return (
    <div className="dashboard">
      <CharacterCard name="Alex" stats={playerStats} />
      <FinancialDashboard data={financialData} />
      <LifeTimeline currentAge={22} events={playerEvents} />
    </div>
  )
}
```

---

## Development Notes

- All components use TypeScript for type safety
- Components are functional React components with hooks
- CSS uses CSS modules and custom properties where applicable
- No external UI library dependencies (custom styling)
- Responsive design implemented with CSS Grid and Flexbox

---

## Related Backend Systems

The visual components integrate with these backend systems:
- **Finance Module**: `finance/service.py`, `catalogs/tax_basics.py`, `catalogs/budgeting.py`
- **Credit System**: `catalogs/credit_system.py`
- **Emergency Fund**: `catalogs/emergency_fund.py`
- **Insurance Basics**: `catalogs/insurance_basics.py`
- **Lease vs Buy**: `catalogs/lease_vs_buy.py`

---

For more information, see the individual component files in `/src/components/`.
