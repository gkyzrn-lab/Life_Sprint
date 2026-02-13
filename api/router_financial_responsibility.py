"""Financial responsibility API routes."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from api.deps import require_player
from financial_responsibility.service import (
    process_first_paycheck_tax_shock,
    set_monthly_expenses,
    generate_unexpected_expense,
    contribute_to_emergency_fund,
    pay_off_debt,
    update_financial_stress,
    get_financial_summary,
    calculate_taxes,
)

router = APIRouter(prefix="/financial-responsibility", tags=["financial-responsibility"])


class TaxShockRequest(BaseModel):
    player_id: str


class SetExpensesRequest(BaseModel):
    player_id: str
    housing_type: str = "on_campus_dorm"


class UnexpectedExpenseRequest(BaseModel):
    player_id: str
    force_category: str = None


class EmergencyFundRequest(BaseModel):
    player_id: str
    amount: float


class DebtPaymentRequest(BaseModel):
    player_id: str
    amount: float
    debt_type: str = "emergency"


class TaxCalculationRequest(BaseModel):
    gross_income: float
    state: str = "general"


@router.post("/tax-shock")
def financial_tax_shock(req: TaxShockRequest):
    """
    Process first paycheck tax shock (surprise mechanic).
    This is when player realizes taxes take 25-35% of earnings.
    """
    player = require_player(req.player_id)
    result = process_first_paycheck_tax_shock(player)
    return result


@router.post("/set-expenses")
def financial_set_expenses(req: SetExpensesRequest):
    """Set monthly expenses based on housing type."""
    player = require_player(req.player_id)
    result = set_monthly_expenses(player, req.housing_type)
    return result


@router.post("/unexpected-expense")
def financial_unexpected_expense(req: UnexpectedExpenseRequest):
    """
    Generate an unexpected expense (surprise mechanic).
    This teaches emergency preparedness.
    """
    player = require_player(req.player_id)
    result = generate_unexpected_expense(player, req.force_category)
    return result


@router.post("/emergency-fund/contribute")
def financial_contribute_emergency(req: EmergencyFundRequest):
    """Contribute to emergency fund."""
    player = require_player(req.player_id)
    result = contribute_to_emergency_fund(player, req.amount)
    return result


@router.post("/debt/pay")
def financial_pay_debt(req: DebtPaymentRequest):
    """Pay off emergency or credit card debt."""
    player = require_player(req.player_id)
    result = pay_off_debt(player, req.amount, req.debt_type)
    return result


@router.post("/update-stress")
def financial_update_stress(player_id: str):
    """
    Update financial stress (called each semester).
    Affects health and mental health.
    """
    player = require_player(player_id)
    result = update_financial_stress(player)
    return result


@router.get("/{player_id}/summary")
def financial_get_summary(player_id: str):
    """Get complete financial responsibility summary."""
    player = require_player(player_id)
    return get_financial_summary(player)


@router.post("/calculate-taxes")
def financial_calculate_taxes(req: TaxCalculationRequest):
    """Calculate taxes on gross income (utility endpoint)."""
    result = calculate_taxes(req.gross_income, req.state)
    return result


@router.get("/{player_id}/tax-burden")
def financial_get_tax_burden(player_id: str):
    """Get player's current tax burden breakdown."""
    player = require_player(player_id)
    
    if not hasattr(player, 'financial_responsibility'):
        return {"message": "No financial data yet"}
    
    fr = player.financial_responsibility
    
    return {
        "gross_income": float(fr.gross_annual_income),
        "take_home": float(fr.take_home_annual),
        "taxes_paid": float(fr.taxes_owed_this_year),
        "effective_rate": float(fr.effective_tax_rate),
        "tax_records": [
            {
                "tax_year": r.tax_year,
                "gross": float(r.gross_income),
                "federal": float(r.federal_tax),
                "state": float(r.state_tax),
                "fica": float(r.fica_tax),
                "total": float(r.total_tax),
                "net": float(r.net_income),
                "rate": float(r.effective_rate),
            }
            for r in fr.tax_records
        ],
        "total_lifetime_taxes": float(fr.total_taxes_paid_lifetime),
    }


@router.get("/{player_id}/emergency-fund")
def financial_get_emergency_fund(player_id: str):
    """Get emergency fund status."""
    player = require_player(player_id)
    
    if not hasattr(player, 'financial_responsibility'):
        return {"emergency_fund": 0, "goal": 0}
    
    fr = player.financial_responsibility
    
    return {
        "current": float(fr.emergency_fund),
        "goal": float(fr.emergency_fund_goal),
        "percent_to_goal": float((fr.emergency_fund / fr.emergency_fund_goal) * 100) if fr.emergency_fund_goal > 0 else 0,
        "months_covered": float(fr.financial_stress.emergency_fund_months),
        "status": "excellent" if fr.financial_stress.emergency_fund_months >= 6 else "good" if fr.financial_stress.emergency_fund_months >= 3 else "insufficient",
    }


@router.get("/{player_id}/stress")
def financial_get_stress(player_id: str):
    """Get financial stress level."""
    player = require_player(player_id)
    
    if not hasattr(player, 'financial_responsibility'):
        return {"stress_level": 0}
    
    stress = player.financial_responsibility.financial_stress
    
    return {
        "stress_level": float(stress.stress_level),
        "status": "Low" if stress.stress_level < 20 else "Moderate" if stress.stress_level < 40 else "High" if stress.stress_level < 60 else "Severe" if stress.stress_level < 80 else "CRITICAL",
        "debt_ratio": float(stress.debt_ratio),
        "emergency_fund_months": float(stress.emergency_fund_months),
        "bankruptcy_risk": float(stress.bankruptcy_risk),
        "warning": stress.stress_level > 60,
    }


@router.get("/{player_id}/achievements")
def financial_get_achievements(player_id: str):
    """Get financial achievements."""
    player = require_player(player_id)
    
    if not hasattr(player, 'financial_responsibility'):
        return {"achievements": []}
    
    return {
        "achievements": [
            {
                "id": a.achievement_id,
                "title": a.title,
                "type": a.milestone_type,
                "semester": a.achieved_semester,
                "description": a.description,
            }
            for a in player.financial_responsibility.unlocked_achievements
        ],
        "total": len(player.financial_responsibility.unlocked_achievements),
    }
