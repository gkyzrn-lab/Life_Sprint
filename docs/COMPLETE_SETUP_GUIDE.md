# Life Sprint - Complete Setup & Deployment Guide

This guide walks you through setting up and running the **complete** Life Sprint game system (backend + frontend) on your local machine.

## System Requirements

- **macOS** (this guide is macOS-specific)
- **Python 3.8+** (for backend)
- **Node.js 16+** (for frontend - will be installed if needed)
- **Git** (optional, for version control)

## Step 1: Backend Setup

The backend uses FastAPI and runs on Python. It's already implemented with:
- 8-step interactive tutorial system
- Player management with persistent state
- Finance, planning, and academic modules
- Full REST API with Swagger documentation

### 1a. Navigate to Backend Directory

```bash
cd ~/Desktop/Life_Sprint
```

### 1b. Create & Activate Virtual Environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate
```

You should see `(.venv)` prefix in your terminal.

### 1c. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### 1d. Start the Backend Server

The backend will run on `http://localhost:8000`:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

**Keep this terminal open.** The backend is now ready to receive API requests.

To verify it's working, visit:
- API Documentation: http://localhost:8000/docs (Swagger UI)
- Root endpoint: http://localhost:8000/

## Step 2: Frontend Setup

The frontend is a React 18 application built with Vite. It provides the user interface and communicates with the backend API.

### 2a. Open a New Terminal (Keep Backend Running)

Keep the backend terminal open and open a **new terminal window**:

```bash
# This opens a fresh terminal
cmd + t  # On macOS
```

### 2b. Install Node.js (If Not Already Installed)

Node.js includes npm (Node Package Manager). Check if you have it:

```bash
node --version
npm --version
```

If you see version numbers, skip ahead to **2c**. If not, install Node.js:

**Option A: Using Homebrew** (if installed)
```bash
brew install node
```

**Option B: Using Conda** (if you have Anaconda/Miniconda)
```bash
conda install -c conda-forge nodejs
```

**Option C: Direct Installation**
Download from: https://nodejs.org/ (LTS version recommended)

After installation, verify:
```bash
node --version
npm --version
```

### 2c. Navigate to Frontend Directory

```bash
cd ~/Desktop/life-sprint-frontend
```

### 2d. Install Frontend Dependencies

```bash
npm install
```

This creates a `node_modules` folder with all required packages. It may take 1-2 minutes.

### 2e. Start the Frontend Development Server

```bash
npm run dev
```

You should see:
```
VITE v5.0.0  ready in 123 ms

➜  Local:   http://localhost:3000/
➜  press h to show help
```

**Keep this terminal open too.** The frontend is now running.

## Step 3: Play the Game!

Now you have both systems running:
- **Backend API**: http://localhost:8000
- **Frontend UI**: http://localhost:3000

### Open Your Browser

Visit **http://localhost:3000** in your web browser.

You should see the splash screen with "Life Sprint" title.

### Complete the Flow

1. **Enter Your Name**: Type your player name and click "Start Playing"
2. **Onboarding Tutorial**: Go through the 8-step tutorial introducing:
   - Welcome to Life Sprint
   - Understanding Time Budget
   - Loans Explained
   - Housing Tradeoffs
   - Work-Study Balance
   - GPA Matters
   - Stress & Burnout Management
   - Planning Ahead
3. **View Dashboard**: After onboarding, see your character stats, finances, and planning tools

Each tutorial step shows:
- A title and description
- Action hints explaining the concept
- A progress bar showing completion
- Next/Skip buttons

### Available Tabs in Game

After onboarding:
- **📊 Stats Tab**: GPA, Stress, Network, Health
- **💰 Finance Tab**: Cash balance, expenses, tuition, scholarships
- **📅 Planning Tab**: Semester planning tools

## Troubleshooting

### Issue: "Cannot connect to backend"

**Solution**: 
- Check that backend is running: `curl http://localhost:8000`
- Should see HTML response from Swagger UI
- If not running, go to backend terminal and run:
  ```bash
  uvicorn main:app --reload --host 127.0.0.1 --port 8000
  ```

### Issue: "npm: command not found"

**Solution**: Node.js is not installed. Install it:
```bash
# Using conda if available
conda install -c conda-forge nodejs

# Or download from https://nodejs.org/
```

Then verify:
```bash
npm --version
```

### Issue: Port 3000 or 8000 already in use

**For Backend** (different port):
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8001
```
Then update the proxy in `vite.config.ts` to point to port 8001.

**For Frontend** (different port):
```bash
npm run dev -- --port 3001
```
Then visit `http://localhost:3001`

### Issue: "Cannot find module" errors in frontend

**Solution**:
```bash
# Delete old dependencies
rm -rf node_modules

# Reinstall
npm install
```

### Issue: Backend "Address already in use"

Some other process is using the port. Find and stop it:

```bash
# Check what's using port 8000
lsof -i :8000

# Kill the process (replace PID with actual number)
kill -9 <PID>

# Then start backend again
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## Production Deployment

### Building the Frontend for Production

```bash
cd ~/Desktop/life-sprint-frontend
npm run build
```

This creates a `dist/` folder with optimized files ready for deployment.

### Deploying Backend

For production, use a production-grade ASGI server:

```bash
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

## Development Workflow

### Making Changes to Backend

1. Edit Python files in `~/Desktop/Life_Sprint/`
2. Uvicorn auto-reloads on file changes (due to `--reload` flag)
3. Refresh browser to see changes

### Making Changes to Frontend

1. Edit TypeScript/CSS files in `~/Desktop/life-sprint-frontend/src/`
2. Vite automatically reloads the browser
3. See changes instantly

### Adding New Game Features

1. **Backend**: Add endpoints in `api/router_*.py` or create new routers
2. **Frontend**: Add new components in `src/components/`
3. **API Client**: Add functions to `src/utils/api.ts`
4. **UI**: Import and use components in game pages

## Architecture Overview

### Backend (Python + FastAPI)

```
main.py                          # FastAPI app
├── api/                         # REST API routers
│   ├── router_player.py         # Player management
│   ├── router_onboarding.py     # Tutorial system
│   ├── router_finance.py        # Finance endpoints
│   ├── router_planning.py       # Planning endpoints
│   └── ...other routers...
├── core_domain/                 # Core game logic
│   ├── models.py                # Data models
│   ├── store.py                 # In-memory storage
│   ├── player/player_model.py   # Player class
│   ├── tutorial.py              # Tutorial definitions
│   └── ...other domain...
├── finance/                     # Finance logic
├── planning/                    # Planning logic
├── academics/                   # Academic logic
└── catalogs/                    # Static data
```

### Frontend (React + TypeScript)

```
src/
├── components/
│   ├── OnboardingModal.tsx      # Tutorial UI
│   ├── GameBoard.tsx            # Main game UI
│   └── ...other components...
├── utils/
│   └── api.ts                   # API client library
├── pages/
│   └── ...page components...
├── App.tsx                      # Main app component
└── main.tsx                     # React entry point
```

### Communication Flow

```
User Action → React Component → API Client (api.ts)
                                    ↓
                            HTTP Request to Backend
                                    ↓
                         FastAPI Router Handler
                                    ↓
                         Core Domain Logic (Service)
                                    ↓
                            In-Memory Data Store
                                    ↓
                            HTTP Response (JSON)
                                    ↓
                        React Updates UI with New Data
```

## Useful Commands

### Backend

```bash
# Start backend
cd ~/Desktop/Life_Sprint
source .venv/bin/activate
uvicorn main:app --reload --host 127.0.0.1 --port 8000

# Run tests
pytest -v

# Check imports
python -c "import main"
```

### Frontend

```bash
# Start development server
cd ~/Desktop/life-sprint-frontend
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Install new package
npm install <package-name>
```

## Next Steps & Future Enhancements

### Immediate Tasks
- [ ] Implement curriculum/course selection UI
- [ ] Add exam scheduling and study planning
- [ ] Add activity selection with time visualization
- [ ] Add messaging/notification system

### Advanced Features
- [ ] Save/load game state
- [ ] Multiplayer support
- [ ] Achievement system
- [ ] User authentication and accounts
- [ ] Mobile app version

### Performance Improvements
- [ ] Add caching layer
- [ ] Implement pagination for large datasets
- [ ] Add API response compression
- [ ] Optimize React component rendering

## Monitoring & Debugging

### Backend Logs

The backend terminal shows:
- Request logs (method, path, status)
- Errors with tracebacks
- Startup/shutdown messages

### Frontend Developer Tools

In browser, press `F12` to open Developer Tools:
- **Console tab**: See JavaScript errors and logs
- **Network tab**: See API requests/responses
- **Application tab**: See browser storage and cookies

### Testing the API Directly

```bash
# Get all tutorials
curl http://localhost:8000/onboarding/tutorial-sequence

# Create a player
curl -X POST http://localhost:8000/player/start \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","college_id":"nyc_public","major_id":"cs"}'
```

## Support & Documentation

- **API Documentation**: http://localhost:8000/docs (when backend is running)
- **Frontend README**: `~/Desktop/life-sprint-frontend/README.md`
- **Backend Guides**: Check `*.md` files in `~/Desktop/Life_Sprint/`

## Summary

You now have a complete, working Life Sprint game system with:

✅ **Backend API** - FastAPI with 8-step tutorial, player management, finance, planning  
✅ **Frontend UI** - React 18 with onboarding modal, game board, stats tracking  
✅ **Real-time Synchronization** - Frontend and backend working together  
✅ **Development Environment** - Hot reload for rapid iteration  

**Have fun playing Life Sprint!** 🎮
