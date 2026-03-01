# 🎮 Life Sprint - Quick Start Guide

## Start the Backend (1 Command)

```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
./start.sh
```

Or manually:
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
source .venv/bin/activate
uvicorn main:app --host 127.0.0.1 --port 8000
```

The API will start at: **http://localhost:8000**

## View the API Documentation

Once the server is running, open your browser:

👉 **http://localhost:8000/docs**

This opens an interactive Swagger UI where you can:
- See all available endpoints
- Test API calls directly
- View request/response examples

## Test the API

Get player status:
```bash
curl http://localhost:8000/player/{player_id}
```

Create a new player:
```bash
curl -X POST http://localhost:8000/player/start \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice",
    "college_id": "cuny_baruch",
    "major_id": "finance",
    "hs_gpa": 3.5,
    "parent_income": 70000,
    "starting_balance": 5000,
    "housing_option_id": "dorm"
  }'
```

Check your player:
```bash
curl http://localhost:8000/player/{player_id}
```

## Run Tests

```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
source .venv/bin/activate
pytest -q
```

Expected: **All selected tests passed** ✅

## Use the Frontend

A complete React frontend is included! Start it:

```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint/life-sprint-frontend
npm install  # First time only
npm run dev
```

Then open: **http://localhost:3000**

The frontend is fully integrated with the backend and includes:
- Player creation
- Dashboard
- Planning system
- Exam system
- And much more!

## Project Structure

```
Life_Sprint/
├── main.py                          ← FastAPI app entry point
├── requirements.txt                 ← Python dependencies
├── start.sh                         ← Quick start script (new!)
├── core_domain/
│   ├── tutorial.py                  ← Tutorial definitions (8 steps + 6 tooltips)
│   ├── player/player_model.py       ← Player model with tutorial_state
│   ├── store.py                     ← In-memory player storage
│   └── config.py                    ← Game configuration
├── api/
│   ├── router_onboarding.py        ← Tutorial/onboarding endpoints (11 routes)
│   ├── router_health.py            ← Health endpoints
│   ├── router_player.py             ← Player creation/management
│   ├── router_catalogs.py           ← Game data (colleges, majors, housing, jobs)
│   └── ... (6 more routers)
├── tests/
│   ├── test_onboarding.py           ← 11 tutorial tests
│   ├── test_health.py               ← 28 health tests
│   └── test_root.py                 ← 1 API test
└── docs/ (documentation)
    ├── ONBOARDING.md                ← API reference
  ├── ONBOARDING_INTEGRATION.tsx.example ← React code examples
  ├── HEALTH_SYSTEM.md             ← Health system reference
    ├── IMPLEMENTATION_SUMMARY.md    ← Architecture details
    └── CHANGES.md                   ← What was implemented
```

## Key Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/player/start` | Create new player |
| GET | `/player/{id}` | Get player data |
| GET | `/tutorial/{player_id}/start` | Start tutorial quest |
| GET | `/onboarding/tutorial/{id}` | Get single tutorial |
| POST | `/onboarding/tutorial/complete` | Mark tutorial complete |
| GET | `/onboarding/{player_id}/progress` | Get tutorial progress |

See [ONBOARDING.md](docs/legacy-root-notes/onboarding/ONBOARDING.md) for onboarding endpoints and [HEALTH_SYSTEM.md](docs/legacy-root-notes/systems/HEALTH_SYSTEM.md) for health endpoints.

## Development Workflow

**Terminal 1: Backend**
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
./start.sh
# Server running at http://localhost:8000/docs
```

**Terminal 2: Frontend**
```bash
cd your-frontend-project
npm start
# App running at http://localhost:3000
```

**Terminal 3: Tests (Optional)**
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
pytest -q --watch  # if pytest-watch is installed
```

## What's Implemented

✅ **Backend**
- Multi-system API endpoints
- 8 tutorial steps with metadata
- 6 interactive tooltips
- Player creation & persistence
- Tutorial progress tracking
- Context-specific recommendations
- Full type safety (Pydantic models)
- Onboarding and health test suites

⏳ **Frontend** (You build this!)
- Use `ONBOARDING_INTEGRATION.tsx.example` as a React example
- Adapt to Vue/Next.js/etc as needed
- API-ready for any frontend framework

## Troubleshooting

**Port 8000 already in use?**
```bash
./start.sh 8001  # Use different port
```

**Virtual environment issues?**
```bash
cd /Users/oktaygokayzeren/Desktop/Life_Sprint
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Tests failing?**
```bash
pytest -q -v  # Verbose output
pytest tests/test_onboarding.py -v  # Run specific test file
```

## Next Steps

1. ✅ Start backend: `./start.sh`
2. ✅ View API docs: http://localhost:8000/docs
3. ✅ Test endpoints (try them in Swagger UI)
4. 🔨 Build frontend (React/Vue/Next.js)
5. 🎮 Connect frontend to backend API
6. 🚀 Deploy!

## Need Help?

- **API Reference**: See [ONBOARDING.md](docs/legacy-root-notes/onboarding/ONBOARDING.md)
- **Code Examples**: See [ONBOARDING_INTEGRATION.tsx.example](examples/frontend/ONBOARDING_INTEGRATION.tsx.example)
- **Design Details**: See [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)
- **Run Tests**: `pytest -q`

---

**Ready to play? Run `./start.sh` now!** 🚀
