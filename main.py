from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers explicitly to avoid package import side-effects;
# each router import is attempted and skipped on failure so the app
# can still start for development.


app = FastAPI(
    title="Life Sprint Backend",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# Add CORS middleware to allow frontend on different port to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",      # Local frontend development
        "http://127.0.0.1:3000",      # Local frontend (127.0.0.1 variant)
        "http://localhost:5173",      # Vite default port (alternative)
        "http://127.0.0.1:5173",      # Vite default port (127.0.0.1 variant)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Try to import and include routers individually so a broken submodule
# won't prevent the whole app from starting during development.
try:
    from api.router_player import router as player_router
    app.include_router(player_router)
except Exception:
    pass

try:
    from api.router_onboarding import router as onboarding_router
    app.include_router(onboarding_router)
except Exception:
    pass

try:
    from api.router_catalogs import router as catalogs_router
    app.include_router(catalogs_router)
except Exception:
    pass

try:
    from api.router_curriculum import router as curriculum_router
    app.include_router(curriculum_router)
except Exception:
    pass

try:
    from api.router_planning import router as planning_router
    app.include_router(planning_router)
except Exception:
    pass

try:
    from api.router_exams import router as exams_router
    app.include_router(exams_router)
except Exception:
    pass

try:
    from api.router_finance import router as finance_router
    app.include_router(finance_router)
except Exception:
    pass

try:
    from api.router_progression import router as progression_router
    app.include_router(progression_router)
except Exception:
    pass

try:
    from api.router_health import router as health_router
    app.include_router(health_router)
except Exception:
    pass

try:
    from api.router_career import router as career_router
    app.include_router(career_router)
except Exception:
    pass

try:
    from api.router_financial_responsibility import router as financial_responsibility_router
    app.include_router(financial_responsibility_router)
except Exception:
    pass

try:
    from api.router_housing_market import router as housing_market_router
    app.include_router(housing_market_router)
except Exception:
    pass

try:
    from api.router_side_gigs import router as side_gigs_router
    app.include_router(side_gigs_router)
except Exception:
    pass


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Life Sprint Backend running",
        "routes": [
            "/player/start",
            "/onboarding/tutorial-sequence",
            "/onboarding/tutorial/{step_id}",
            "/onboarding/tutorials/context/{context}",
            "/onboarding/tooltips",
            "/onboarding/tooltip/{tooltip_id}",
            "/onboarding/tutorial/complete",
            "/onboarding/tooltip/dismiss",
            "/onboarding/{player_id}/progress",
            "/catalogs/*",
            "/curriculum/*",
            "/planning/*",
            "/exams/*",
            "/finance/*",
            "/health/*",
            "/career/*",
            "/financial-responsibility/*",
            "/housing-market/*",
            "/side-gigs/*",
            "/progress/advance",
        ],
    }
