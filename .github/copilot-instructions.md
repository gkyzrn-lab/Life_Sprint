# Copilot / AI Agent Instructions for Life Sprint Backend

This file gives focused, actionable guidance so an AI coding agent can be immediately productive in this repository.

1) Big picture
- Service: FastAPI application defined in [main.py](main.py). The app composes multiple routers under `/api/*` style prefixes.
- Domain: core domain models and rules live under [core_domain/](core_domain/) (models, config, utils, `STORE`).
- Catalogs: static definitions (colleges, majors, housing, jobs, activities) live under [catalogs/](catalogs/) and are used as authoritative lookup tables.
- Business logic: per-area service modules under top-level folders (e.g. [finance/service.py](finance/service.py), [planning/service.py](planning/service.py), [academics/exam_service.py](academics/exam_service.py)). Services mutate `Player` in-place.

2) Important patterns & conventions
- Routers import pattern: `main.py` imports routers inside `try/except` blocks so a broken module should not prevent app startup. When editing routers, avoid hard import side-effects and keep imports local where possible.
- In-memory persistence: `STORE` in [core_domain/store.py](core_domain/store.py) is an in-memory store used by tests and runtime. Code expects `STORE.put_player()` and `STORE.get_player()` to exist—do not replace without migrating callers.
- Mutable domain objects: services operate on `Player` objects (from `core_domain.player.player_model`) by mutating fields (finance, stats, plan). Return values are often API-friendly objects or the same mutated instance.
- Catalogs are plain dicts keyed by id strings. Validate IDs against the catalogs rather than assuming existence (see `router_player.py` and `planning/service.py`).
- Error handling: HTTP errors are raised with `fastapi.HTTPException` from routers/services to return proper status codes.

3) Developer workflows (commands)
- Activate virtualenv: `. .venv/bin/activate`
- Install deps: `pip install -r requirements.txt`
- Run server locally: `uvicorn main:app --reload --host 127.0.0.1 --port 8000`
- Run tests: `pytest -q`

4) What to check when changing behavior
- If you modify a router, ensure it does not import heavy modules at import time—use local imports inside endpoints if necessary to preserve `main.py` resilience.
- Services assume time/finance constants in [core_domain/config.py](core_domain/config.py). Changing those values impacts many calculations.
- Loan/repayment logic mutates loan objects in `finance/service.py`. Preserve semantics: interest accrual, grace handling, capitalization, and repayment allocation order (highest-rate-first).

5) Quick file map (where to look for common tasks)
- App entry: [main.py](main.py)
- API routers: [api/](api/) (e.g. `router_player.py`, `router_curriculum.py`)
- Domain models & store: [core_domain/](core_domain/) (`models.py`, `store.py`, `config.py`)
- Static data: [catalogs/](catalogs/)
- Finance logic: [finance/service.py](finance/service.py)
- Planning logic: [planning/service.py](planning/service.py)

6) Tests & local constraints
- Tests use the in-memory `STORE`—avoid persistent side-effects when running unit tests locally.
- The app deliberately tolerates broken submodules during development; CI should run full import validation and tests to catch hidden import-time errors.

7) Examples to follow
- Validate catalog ids before use (see [api/router_player.py](api/router_player.py)).
- Mutate `Player` and then append `HistoryEvent` records (see [planning/service.py](planning/service.py)).

If any of these sections are unclear or you want additional examples (e.g., how to add a new catalog or a router), tell me which area to expand and I'll iterate.
