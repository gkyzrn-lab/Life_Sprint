from __future__ import annotations

from pydantic import BaseModel


class BorrowForSemesterRequest(BaseModel):
    player_id: str
    needed_amount: float


class BorrowForSemesterResponse(BaseModel):
    player_id: str
    borrowed_total: float
    remaining_uncovered: float
    new_balance: float


class SetRepaymentProfileRequest(BaseModel):
    player_id: str
    plan_type: str  # "standard" or "idr"
    annual_income: float
    family_size: int = 1


class RepayMonthsRequest(BaseModel):
    player_id: str
    months: int = 1


class RepayMonthsResponse(BaseModel):
    player_id: str
    months: int
    total_paid: float
    ending_balance: float
    total_principal_remaining: float
