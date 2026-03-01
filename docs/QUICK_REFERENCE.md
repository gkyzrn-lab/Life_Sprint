# Life Sprint - Quick Reference Card

## 🚀 Quick Start (5 Minutes)

### Terminal 1: Backend
```bash
cd ~/Desktop/Life_Sprint
source .venv/bin/activate
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
✅ Backend ready at http://localhost:8000

### Terminal 2: Frontend
```bash
cd ~/Desktop/life-sprint-frontend

# First time only
npm install

# Start development server
npm run dev
```
✅ Frontend ready at http://localhost:3000

### Browser
Open http://localhost:3000 and **Play!**

---

## 📁 Project Structure

```
~/Desktop/Life_Sprint/                    # Backend (FastAPI)
├── main.py                              # App entry
├── api/router_onboarding.py             # Tutorial endpoints
├── api/router_health.py                 # Health endpoints
├── core_domain/tutorial.py              # Tutorial content
├── health/service.py                    # Health logic
└── ...other modules...

~/Desktop/life-sprint-frontend/          # Frontend (React)
├── src/
│   ├── components/
│   │   ├── OnboardingModal.tsx          # Tutorial UI (145 lines)
│   │   └── GameBoard.tsx                # Game UI (125 lines)
│   ├── utils/
│   │   └── api.ts                       # API client (155 lines)
│   ├── App.tsx                          # Main component (49 lines)
│   └── main.tsx                         # React entry
├── vite.config.ts                       # Dev server config
└── package.json                         # Dependencies
```

---

## 🎮 Gameplay Flow

1. **Splash Screen** → Enter player name
2. **Onboarding** → Complete 8 tutorial steps:
   - Welcome
   - Time Budget
   - Loans
   - Housing
   - Work-Study
   - GPA
   - Stress & Health
   - Planning
3. **Game Board** → View stats, finances, planning
4. **Logout** → Start over

---

## 🔧 Common Commands

### Backend
```bash
# Start (from ~/Desktop/Life_Sprint)
source .venv/bin/activate
uvicorn main:app --reload --host 127.0.0.1 --port 8000

# Run tests
pytest -q

# Check API docs
curl http://localhost:8000/docs
```

### Frontend
```bash
# Start (from ~/Desktop/life-sprint-frontend)
npm run dev                    # Development
npm run build                  # Production build
npm run preview               # Preview build
npm install <package>         # Add package
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Backend won't start | Check port 8000: `lsof -i :8000` then `kill -9 <PID>` |
| Frontend won't start | Install Node.js: `brew install node` |
| API connection error | Ensure backend running on port 8000 |
| "npm not found" | Install Node.js from https://nodejs.org/ |
| Hot reload not working | Check Vite is running: `npm run dev` |

---

## 📚 API Reference

All 13 API functions in `src/utils/api.ts`:

```typescript
// Player
createPlayer(name, collegeId, majorId)          // Create new game
getPlayer(playerId)                             // Get player data

// Tutorials
getTutorialSequence()                           // All 8 steps
getTutorial(stepId)                             // Single step
getContextTutorials(context)                    // Context help
completeTutorial(playerId, stepId)              // Mark complete
getTutorialProgress(playerId)                   // Completion %

// Tooltips
getAllTooltips()                                // All tooltips
getTooltip(tooltipId)                           // Single tooltip
dismissTooltip(playerId, tooltipId)             // Dismiss tooltip

// Preferences
enableTutorials(playerId)                       // Turn on tutorials
disableTutorials(playerId)                      // Turn off tutorials
```

---

## 📊 Frontend Components

### OnboardingModal.tsx
- **Purpose**: Display tutorial steps
- **Props**: playerName, onComplete callback
- **State**: currentStep, tutorials[], playerId, progress, loading, error
- **Features**: Progress bar, Next/Skip buttons, step tracking

### GameBoard.tsx
- **Purpose**: Main game interface
- **Props**: player, onLogout callback
- **Tabs**: Stats, Finance, Planning
- **Features**: Player info, stats grid, finance cards

### App.tsx
- **Purpose**: Main router component
- **Screens**: Splash (name input) → Onboarding → GameBoard
- **State**: playerName, player, showNameInput

---

## 🎨 Styling

All components use CSS for styling:
- **Splash**: Purple gradient background
- **Onboarding**: Modal overlay with animations
- **Game**: Card-based dashboard layout
- **Responsive**: CSS Grid for layouts
- **Colors**: Green (positive), Red (warnings), Blue (primary)

---

## 🔌 API Endpoints

### Backend Endpoints Used
```
POST   /player/start                              # Create player
GET    /player/{id}                               # Get player
GET    /onboarding/tutorial-sequence              # All tutorials
GET    /onboarding/tutorial/{step_id}             # Single tutorial
GET    /onboarding/tutorials/context/{context}    # Context help
POST   /onboarding/tutorial/complete              # Mark complete
GET    /onboarding/{player_id}/progress           # Completion %
GET    /onboarding/tooltips                       # All tooltips
GET    /onboarding/tooltip/{id}                   # Single tooltip
POST   /onboarding/tooltip/dismiss                # Dismiss tooltip
POST   /onboarding/{player_id}/enable-tutorials   # Enable tutorials
POST   /onboarding/{player_id}/disable-tutorials  # Disable tutorials
```

All responses are JSON with proper error handling.

### Health Endpoints (new)
```
POST   /health/exercise
POST   /health/therapy
POST   /health/checkup
POST   /health/condition
POST   /health/batch-actions
GET    /health/{player_id}/summary
GET    /health/{player_id}/achievements
GET    /health/{player_id}/achievement-progress
GET    /health/{player_id}/history
GET    /health/{player_id}/streaks
POST   /health/{player_id}/progress-semester
```

See [HEALTH_SYSTEM.md](legacy-root-notes/systems/HEALTH_SYSTEM.md) for full health mechanics and examples.

---

## 📋 Development Checklist

- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] Can see splash screen
- [ ] Can enter player name
- [ ] Onboarding tutorial loads
- [ ] Can complete tutorial steps
- [ ] Game board displays correctly
- [ ] Can view stats/finance/planning
- [ ] Can logout and play again

---

## 🚢 Production Deployment

```bash
# Build frontend
cd ~/Desktop/life-sprint-frontend
npm run build                    # Creates dist/ folder

# Deploy dist/ to:
# - Vercel (vercel deploy)
# - Netlify (drag & drop dist/)
# - AWS S3 + CloudFront
# - Any static hosting

# Backend deployment (separate):
# - Use gunicorn for production ASGI server
# - Set up database for persistence
# - Configure CORS for frontend domain
```

---

## 📞 Useful Links

- **Frontend README**: `~/Desktop/life-sprint-frontend/README.md`
- **Complete Setup Guide**: `~/Desktop/COMPLETE_SETUP_GUIDE.md`
- **Backend API Docs**: http://localhost:8000/docs (when running)
- **GitHub**: Add when available
- **Issues**: Report bugs and feature requests

---

## 💡 Next Feature Ideas

1. **Curriculum UI** - Select courses each semester
2. **Exams** - Study and take exams
3. **Activities** - Join clubs and activities
4. **Notifications** - Game events and alerts
5. **Achievements** - Badges and milestones
6. **Leaderboards** - Compare with other players
7. **Mobile App** - React Native version
8. **Multiplayer** - Play with friends

---

## 📞 Quick Support

### Check Backend Health
```bash
curl http://localhost:8000/docs
# Should return Swagger UI HTML
```

### Check Frontend Connection
Open browser DevTools (F12) → Console
Look for API call logs and errors

### View All Tutorials
```bash
curl http://localhost:8000/onboarding/tutorial-sequence | python -m json.tool
```

### View Player Data
```bash
# After creating a player, replace <PLAYER_ID>
curl http://localhost:8000/player/<PLAYER_ID> | python -m json.tool
```

---

## ⚡ Performance Tips

- Frontend loads in < 1 second (Vite optimization)
- API calls < 100ms (localhost)
- Progress bar updates smoothly (CSS animations)
- No performance issues for current feature set

---

## 📝 Summary

✅ **Backend**: FastAPI with 8-step tutorial + 11 API endpoints  
✅ **Frontend**: React 18 with 3 main components + API client  
✅ **Type Safety**: Full TypeScript on frontend, Pydantic on backend  
✅ **Development**: Hot reload on both backend (Uvicorn) and frontend (Vite)  
✅ **Documentation**: Complete setup guides and API reference  

**You're all set!** Run the commands above and play Life Sprint 🎮
