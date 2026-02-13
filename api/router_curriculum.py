from __future__ import annotations

from fastapi import APIRouter, HTTPException

from academics.curriculum import CURRICULUM
from api.deps import require_player

router = APIRouter(prefix="/curriculum", tags=["curriculum"])


@router.get("/player/{player_id}/semester/{semester}")
def get_player_semester_curriculum(player_id: str, semester: int):
    p = require_player(player_id)
    sem = CURRICULUM.get(p.college_id, {}).get(p.major_id, {}).get(int(semester))
    if not sem:
        raise HTTPException(status_code=404, detail="Curriculum not found for this selection")
    return sem.model_dump()


@router.get("/{college_id}/{major_id}")
def get_full_curriculum(college_id: str, major_id: str):
    block = CURRICULUM.get(college_id, {}).get(major_id)
    if not block:
        raise HTTPException(status_code=404, detail="Curriculum not found for this college/major")
    return {str(k): v.model_dump() for k, v in block.items()}
