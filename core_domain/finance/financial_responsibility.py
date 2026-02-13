"""Financial responsibility models for Life Sprint.

Tracks:
- Income and taxes (federal, state, FICA)
- Monthly expenses (rent, utilities, food, transport, insurance)
- Debt (student loans, credit cards)
- Emergency fund and savings
- Financial stress (affects health)
- Surprising costs and financial literacy
"""

from __future__ import annotations

from typing import List, Optional, Literal
from pydantic import BaseModel, Field


class TaxRecord(BaseModel):
    """Tax filing information for a tax year."""
    tax_year: int
    gross_income: float  # Total before taxes
    federal_tax: float
    state_tax: float
    fica_tax: float  # Social Security + Medicare
    total_tax: float
    net_income: float  # Take-home
    effective_rate: float  # percentage paid in taxes


class MonthlyExpense(BaseModel):
    """A monthly recurring expense."""
    category: Literal["rent", "utilities", "food", "transport", "insurance", "entertainment", "other"]
    name: str
    amount: float
    description: str = ""


class UnexpectedExpense(BaseModel):
    """Surprise expense that impacts budget."""
    expense_id: str
    name: str
    amount: float
    category: Literal["medical", "car_repair", "emergency", "replacement", "other"]
    semester: int
    severity: Literal["minor", "moderate", "major"]  # impacts stress
    resolved: bool = False


class FinancialAchievement(BaseModel):
    """Financial milestone achievement."""
    achievement_id: str
    title: str
    milestone_type: Literal["savings", "debt_free", "budget_master", "wealth", "responsibility"]
    achieved_semester: int
    description: str


class FinancialStress(BaseModel):
    """Financial stress tracking (affects health)."""
    stress_level: float = 0.0  # 0-100
    debt_ratio: float = 0.0  # debt / annual_income (0-infinity)
    emergency_fund_months: float = 0.0  # months of expenses saved
    bankruptcy_risk: float = 0.0  # 0-1.0 probability


class FinancialLiteracy(BaseModel):
    """Player's understanding of finances."""
    # How much they understand about:
    tax_awareness: float = 10.0  # 0-100, starts low
    budget_skill: float = 20.0  # starts weak
    investment_knowledge: float = 5.0  # starts very low
    debt_management: float = 15.0  # starts weak
    
    # Major financial lessons learned
    lessons_learned: List[str] = Field(default_factory=list)
    
    # Has experienced major financial events?
    experienced_major_expense: bool = False
    experienced_tax_shock: bool = False
    experienced_debt_crisis: bool = False
    experienced_high_stress: bool = False


class FinancialResponsibility(BaseModel):
    """Complete financial state beyond basic balance."""
    
    # Current finances
    gross_annual_income: float = 0.0  # from career
    take_home_annual: float = 0.0  # after taxes
    monthly_expenses: List[MonthlyExpense] = Field(default_factory=list)
    total_monthly_cost: float = 0.0
    
    # Tax state
    current_tax_year: int = 2026
    tax_records: List[TaxRecord] = Field(default_factory=list)
    taxes_owed_this_year: float = 0.0
    effective_tax_rate: float = 0.0
    
    # Debt tracking (beyond student loans)
    credit_card_debt: float = 0.0
    emergency_debt: float = 0.0  # debt from unexpected expenses
    total_non_student_debt: float = 0.0
    
    # Emergency fund & savings
    emergency_fund: float = 0.0  # 3-6 months expenses is ideal
    emergency_fund_goal: float = 0.0  # calculated as 4x monthly expenses
    savings_rate: float = 0.0  # % of take-home going to savings
    
    # Financial stress
    financial_stress: FinancialStress = Field(default_factory=FinancialStress)
    
    # Literacy
    literacy: FinancialLiteracy = Field(default_factory=FinancialLiteracy)
    
    # Unexpected expenses history
    unexpected_expenses: List[UnexpectedExpense] = Field(default_factory=list)
    total_unexpected_costs: float = 0.0
    
    # Achievements
    unlocked_achievements: List[FinancialAchievement] = Field(default_factory=list)
    
    # Stories shown
    stories_shown: List[str] = Field(default_factory=list)
    
    # Financial history
    financial_awareness_triggered: bool = False  # has player seen "taxes aren't free" message?
    months_until_tax_day: int = 12  # countdown to tax filing
    has_had_tax_filing: bool = False
    total_taxes_paid_lifetime: float = 0.0
    
    # Financial insights
    financial_literacy_level: Literal["unaware", "basic", "informed", "responsible", "expert"] = "unaware"
