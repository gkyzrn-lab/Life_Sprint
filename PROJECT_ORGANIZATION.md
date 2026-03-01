# Project Organization (February 2026)

This file explains the folder cleanup and where files were moved.

## Root is now code-first

The repository root now keeps only runtime/code essentials:

- app source folders (`api/`, `core_domain/`, `academics/`, `finance/`, etc.)
- app entry/config (`main.py`, `pytest.ini`, `requirements.txt`, `start.sh`)
- tests (`tests/`, selected test scripts)
- frontend app (`life-sprint-frontend/`)

## Documentation moved out of root

Most root-level `.md`/`.txt` files were moved to:

- `docs/legacy-root-notes/`

They were then grouped by topic:

- `analytics/`
- `academics/`
- `systems/`
- `store/`
- `visual/`
- `onboarding/`
- `project/`
- `reports/`
- `misc/`

## Frontend examples moved

The following root files were moved to `examples/frontend/`:

- `ONBOARDING_INTEGRATION.tsx.example`
- `COURSE_PROGRESSION_HANDLERS.tsx`

## Notes

- Existing source-code module paths were not changed.
- Runtime behavior should remain unaffected by this cleanup.
- If any old doc links still point to root-level files, update those links to `docs/legacy-root-notes/...`.
