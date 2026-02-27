from __future__ import annotations

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("life_sprint")

app = FastAPI(
    title="Life Sprint Backend",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def _try_include(module_path: str, attr: str = "router", prefix_label: str = ""):
    try:
        import importlib
        mod = importlib.import_module(module_path)
        router = getattr(mod, attr)
        app.include_router(router)
        logger.info(f"✅ Router loaded: {prefix_label or module_path}")
    except Exception as exc:
        logger.error(f"❌ Failed to load router '{module_path}': {exc}")

_try_include("api.router_player",                   prefix_label="player")
_try_include("api.router_onboarding",               prefix_label="onboarding")
_try_include("api.router_catalogs",                 prefix_label="catalogs")
_try_include("api.router_curriculum",               prefix_label="curriculum")
_try_include("api.router_planning",                 prefix_label="planning")
_try_include("api.router_exams",                    prefix_label="exams")
_try_include("api.router_finance",                  prefix_label="finance")
_try_include("api.router_progression",              prefix_label="progression")
_try_include("api.router_health",                   prefix_label="health")
_try_include("api.router_career",                   prefix_label="career")
_try_include("api.router_financial_responsibility", prefix_label="financial_responsibility")
_try_include("api.router_housing_market",           prefix_label="housing_market")
_try_include("api.router_side_gigs",                prefix_label="side_gigs")
_try_include("api.router_store",                    prefix_label="store")

@app.get("/")
def root():
    routes = []
    for route in app.routes:
        if hasattr(route, "methods") and hasattr(route, "path"):
            routes.append({
                "path": route.path,
                "methods": sorted(route.methods),
                "name": route.name,
            })
    return {
        "status": "ok",
        "message": "Life Sprint Backend running",
        "total_routes": len(routes),
        "routes": routes,
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": app.version}
