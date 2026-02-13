# Life Sprint Frontend

A React 18 + Vite frontend for the Life Sprint college life simulator game. This UI integrates with the backend FastAPI server to provide a complete gaming experience.

## Features

- **Onboarding Tutorial**: Interactive 8-step tutorial introducing core game concepts
- **Player Dashboard**: View your character stats, finances, and planning
- **Real-time Stats**: Track GPA, stress level, health, and network
- **Financial Management**: Monitor cash balance, expenses, loans, and scholarships
- **Responsive Design**: Works on desktop and tablet devices

## Prerequisites

- Node.js 16+ and npm
- The Life Sprint backend running on `http://localhost:8000`

## Quick Start

```bash
# Install dependencies
npm install

# Start the development server (runs on http://localhost:3000)
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Project Structure

```
src/
├── components/
│   ├── OnboardingModal.tsx   # 8-step tutorial component
│   ├── OnboardingModal.css
│   ├── GameBoard.tsx         # Main game interface
│   └── GameBoard.css
├── utils/
│   └── api.ts               # API client with full TypeScript types
├── App.tsx                  # Main app component with routing logic
├── App.css
├── main.tsx                 # React entry point
index.html                   # HTML template
vite.config.ts              # Vite configuration
tsconfig.json               # TypeScript configuration
```

## How It Works

### Splash Screen
When the user first loads the app, they see a splash screen where they enter their player name. This name is used to create a new player on the backend.

### Onboarding Flow
After entering their name, the user goes through an 8-step tutorial:
1. Welcome to Life Sprint
2. Understanding Time Budget
3. Loans Explained
4. Housing Tradeoffs
5. Work-Study Balance
6. GPA Matters
7. Stress & Burnout Management
8. Planning Ahead

Each step shows:
- Step title and description
- Action hints
- Progress bar showing completion percentage
- Next/Skip buttons

### Game Board
After completing (or skipping) the tutorial, players access the main game:
- **Stats Tab**: View GPA, stress, network, and health metrics
- **Finance Tab**: Check cash balance, monthly expenses, tuition costs, and scholarships
- **Planning Tab**: Plan semester activities and time allocation

## API Integration

The frontend uses the `src/utils/api.ts` utility for all backend communication:

```typescript
// Create a new player
const player = await createPlayer(name, collegeId, majorId)

// Get tutorial sequence
const { sequence } = await getTutorialSequence()

// Complete a tutorial step
const progress = await completeTutorial(playerId, stepId)

// Dismiss a tooltip
await dismissTooltip(playerId, tooltipId)
```

All API functions are fully typed with TypeScript interfaces for better IDE support and type safety.

## Environment Variables

The frontend proxies API calls to the backend. Update the backend URL in `vite.config.ts` if needed:

```typescript
proxy: {
  '/api': {
    target: 'http://localhost:8000',  // Backend URL
    changeOrigin: true,
    rewrite: (path) => path.replace(/^\/api/, ''),
  }
}
```

## Styling

Components use CSS modules alongside regular CSS files for styling. Key design decisions:
- Purple gradient background for visual polish
- Card-based layout for dashboard
- Smooth animations and transitions
- Mobile-responsive grid layouts
- Semantic color coding (green for positive, red for warnings)

## Development

### Hot Reload
The dev server has hot reload enabled. Changes to `.tsx` and `.css` files are reflected immediately in the browser.

### Type Checking
TypeScript is configured in strict mode. The TypeScript compiler will catch type errors at compile time.

### Testing Connection

```bash
# Terminal 1: Start the backend
cd ../  # Go to Life_Sprint backend directory
./start.sh

# Terminal 2: Start the frontend
npm run dev
```

Then visit `http://localhost:3000` in your browser. You should see the splash screen.

## Troubleshooting

### Backend Connection Error
If you see "Failed to initialize game" with connection errors:
- Ensure the backend is running on `http://localhost:8000`
- Check that the API proxy is correctly configured in `vite.config.ts`
- Look at the browser console (F12) for detailed error messages

### Port Already in Use
If port 3000 is already in use:
```bash
# Specify a different port
npm run dev -- --port 3001
```

### TypeScript Errors
If you see TypeScript errors:
```bash
# Ensure all dependencies are installed
npm install

# Clear the build cache
rm -rf dist node_modules
npm install
```

## Next Steps

### Future Enhancements
- [ ] Add curriculum/course selection UI
- [ ] Add exam scheduling and study planning
- [ ] Add activity selection and time budget visualization
- [ ] Add messaging/notification system
- [ ] Add save/load game functionality
- [ ] Add multiplayer features
- [ ] Add achievement system
- [ ] Add in-game settings and preferences

### Integration Points
To add new game features:
1. Create new API functions in `src/utils/api.ts`
2. Create corresponding React components in `src/components/`
3. Add navigation in the GameBoard component
4. Import and use the API functions in your components

## Contributing

When adding new features:
1. Keep API functions in `api.ts` separate from UI logic
2. Create new components in `src/components/` with their own CSS
3. Use TypeScript interfaces for all data structures
4. Test with the backend before committing

## License

Same as the Life Sprint backend project.
