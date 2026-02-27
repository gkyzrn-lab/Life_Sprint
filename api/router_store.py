# Store API Router - Endpoints for life purchases
# GET /api/store/available - List available purchases
# GET /api/store/categories - Get categories
# POST /api/store/purchase/{purchase_id} - Make a purchase
# GET /api/store/history - Get purchase history
# GET /api/store/financial-summary - Get financial integration data
# GET /api/store/affordability/{purchase_id} - Analyze if purchase is affordable
# GET /api/store/roi/{purchase_id} - Get return on investment analysis

from fastapi import APIRouter, HTTPException
from typing import List

from api.deps import require_player
from core_domain.store import STORE
from store.purchase_service import (
    make_purchase,
    get_player_purchase_history,
    suggest_purchases_for_player,
    PurchaseNotFound,
    InsufficientFunds,
)
from store.financial_integration import (
    get_financial_summary,
    get_purchase_affordability_analysis,
    analyze_purchase_roi,
    get_income_optimization_recommendations,
    create_financial_dashboard_data,
)
from catalogs.life_purchases import (
    get_available_purchases,
    get_purchase_categories,
    get_purchase,
    LIFE_PURCHASES,
)

router = APIRouter(prefix="/api/store", tags=["store"])


@router.get("/categories")
def list_store_categories():
    """Get all purchase categories"""
    try:
        categories = get_purchase_categories()
        return {"categories": categories}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/available")
def list_available_purchases(player_id: str):
    """
    Get all purchases available for the current player's semester.
    Filters by: semester unlock requirement
    """
    try:
        player = require_player(player_id)

        available = get_available_purchases(player.semester)
        
        # Add purchase metadata
        result = []
        for purchase in available:
            result.append({
                "purchase_id": purchase.purchase_id,
                "name": purchase.name,
                "emoji": purchase.emoji,
                "description": purchase.description,
                "cost": purchase.cost,
                "category": purchase.category,
                "one_time": purchase.one_time,
                "max_per_semester": purchase.max_per_semester,
                "effects": [
                    {"stat": e.stat_name, "change": e.change}
                    for e in purchase.effects
                ],
                "is_affordable": player.finance.balance >= purchase.cost,
                "current_balance": player.finance.balance,
            })
        
        return {"purchases": result}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/purchase/{purchase_id}")
def make_purchase_endpoint(purchase_id: str, player_id: str):
    """
    Make a purchase for the player.
    Deducts cost from balance, applies effects to stats.
    """
    try:
        player = require_player(player_id)

        result = make_purchase(player, purchase_id)
        
        # Update player in store
        STORE.put_player(player)

        if not result.success:
            raise HTTPException(status_code=400, detail=result.message)

        return {
            "success": True,
            "message": result.message,
            "purchase": {
                "id": result.purchase.purchase_id,
                "name": result.purchase.name,
                "cost": result.purchase.cost,
            },
            "balance_before": result.balance_before,
            "balance_after": result.balance_after,
            "effects": result.effects_applied,
        }

    except PurchaseNotFound:
        raise HTTPException(status_code=404, detail=f"Purchase '{purchase_id}' not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history")
def get_purchase_history(player_id: str):
    """Get player's purchase history"""
    try:
        player = require_player(player_id)

        history = get_player_purchase_history(player)
        
        result = []
        for event in history:
            purchase_id = event.label.replace("purchase:", "")
            purchase = get_purchase(purchase_id)
            if purchase:
                result.append({
                    "semester": event.semester,
                    "purchase_id": purchase_id,
                    "purchase_name": purchase.name,
                    "cost": event.details.get("cost", 0),
                    "effects": {
                        k: v for k, v in event.details.items()
                        if k not in ["cost", "balance_before", "balance_after"]
                    },
                })

        return {"history": result}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/suggestions")
def get_purchase_suggestions(player_id: str):
    """Get AI-suggested purchases based on player's current stats"""
    try:
        player = require_player(player_id)

        suggestions = suggest_purchases_for_player(player)
        
        result = []
        for purchase, reason in suggestions:
            result.append({
                "purchase_id": purchase.purchase_id,
                "name": purchase.name,
                "emoji": purchase.emoji,
                "cost": purchase.cost,
                "reason": reason,
                "is_affordable": player.finance.balance >= purchase.cost,
            })

        return {"suggestions": result}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/purchase/{purchase_id}")
def get_purchase_details(purchase_id: str):
    """Get detailed info for a specific purchase"""
    try:
        purchase = get_purchase(purchase_id)
        if not purchase:
            raise HTTPException(status_code=404, detail=f"Purchase '{purchase_id}' not found")

        return {
            "purchase_id": purchase.purchase_id,
            "name": purchase.name,
            "emoji": purchase.emoji,
            "description": purchase.description,
            "cost": purchase.cost,
            "category": purchase.category,
            "one_time": purchase.one_time,
            "max_per_semester": purchase.max_per_semester,
            "requires_semester_min": purchase.requires_semester_min,
            "effects": [
                {"stat": e.stat_name, "change": e.change, "duration": e.duration}
                for e in purchase.effects
            ],
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/financial-summary")
def get_financial_summary_endpoint(player_id: str):
    """
    Get comprehensive financial summary including job income, tuition costs,
    and monthly budget. Used for strategic purchase decisions.
    
    Returns:
    {
        "current_balance": player's wallet,
        "semester_income": projected income from job,
        "semester_tuition": cost of tuition,
        "monthly_subscriptions": recurring monthly costs,
        "income_after_essentials": available after bills,
        "monthly_available": average monthly spending money,
        "job_title": current job,
        "job_hours": hours per week,
        "performance_rating": job performance (0-100),
        "financial_health": "critical" | "tight" | "comfortable" | "excellent"
    }
    """
    try:
        player = require_player(player_id)
        summary = get_financial_summary(player)
        return {"success": True, "data": summary}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/affordability/{purchase_id}")
def get_purchase_affordability_endpoint(purchase_id: str, player_id: str):
    """
    Analyze if a specific purchase makes financial sense.
    
    Shows:
    - Can afford now?
    - How many days of work needed?
    - Impact on monthly budget if recurring?
    - Financial warnings/advice
    """
    try:
        player = require_player(player_id)
        analysis = get_purchase_affordability_analysis(player, purchase_id)
        return {"success": True, "analysis": analysis}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/roi/{purchase_id}")
def get_purchase_roi_endpoint(purchase_id: str, player_id: str):
    """
    Get return-on-investment analysis for a purchase.
    
    For wellness items (therapy, spa):
    - Shows stress reduction → performance improvement → income gain
    
    For career items (laptop, car):
    - Shows opportunity unlock → long-term income gain
    
    Returns payback period and ROI summary.
    """
    try:
        player = require_player(player_id)
        roi = analyze_purchase_roi(player, purchase_id)
        return {"success": True, "roi": roi}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/recommendations")
def get_income_recommendations_endpoint(player_id: str):
    """
    Get personalized recommendations for improving financial situation.
    
    Suggests:
    - Job opportunities based on financial need
    - Wellness investments that boost income
    - Strategic purchases for career advancement
    """
    try:
        player = require_player(player_id)
        recommendations = get_income_optimization_recommendations(player)
        return {"success": True, "recommendations": recommendations}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/dashboard")
def get_financial_dashboard_endpoint(player_id: str):
    """
    Get complete financial dashboard combining all integration data.
    
    Comprehensive view including:
    - Financial summary
    - Personalized recommendations
    - Critical warnings
    - Financial opportunities
    """
    try:
        player = require_player(player_id)
        dashboard = create_financial_dashboard_data(player)
        return {"success": True, "dashboard": dashboard}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
