"""Tax basics mini-game - teaches tax fundamentals."""

from typing import Dict, List, Optional, Literal
from pydantic import BaseModel, Field
import math


class TaxBracket(BaseModel):
    """A tax bracket for a filing status."""
    bracket_id: str
    filing_status: Literal["single", "married_filing_jointly", "married_filing_separately", "head_of_household"]
    year: int
    
    # Income ranges and rates (2024 tax year)
    brackets: List[Dict] = Field(default_factory=list)  # [{"min": 0, "max": 11000, "rate": 0.10}, ...]


class TaxScenario(BaseModel):
    """A tax filing scenario."""
    scenario_id: str
    
    # Income sources
    w2_income: float = 0  # Salary
    side_gig_income: float = 0
    investment_income: float = 0
    interest_earned: float = 0
    capital_gains: float = 0
    
    # Deductions
    filing_status: Literal["single", "married_filing_jointly", "married_filing_separately", "head_of_household"] = "single"
    use_standard_deduction: bool = True
    itemized_deductions: float = 0
    
    # Credits
    education_credits: float = 0
    child_tax_credits: float = 0
    earned_income_credit: float = 0
    
    # Results
    gross_income: float = 0
    taxable_income: float = 0
    income_tax: float = 0
    fica_tax: float = 0  # Social security + medicare
    total_tax: float = 0
    effective_tax_rate: float = 0
    refund_or_owed: float = 0


class TaxTerm(BaseModel):
    """A tax term/concept."""
    term_id: str
    term_name: str
    definition: str
    example: str
    importance: Literal["critical", "important", "nice_to_know"]


class TaxMythFact(BaseModel):
    """Tax myths vs facts."""
    myth_id: str
    myth: str
    fact: str
    financial_impact: Optional[str] = None


# Tax brackets for 2024 (simplified)
TAX_BRACKETS_2024: Dict[str, List[Dict]] = {
    "single": [
        {"min": 0, "max": 11000, "rate": 0.10},
        {"min": 11000, "max": 50000, "rate": 0.12},
        {"min": 50000, "max": 95375, "rate": 0.22},
        {"min": 95375, "max": 182100, "rate": 0.24},
        {"min": 182100, "max": 231250, "rate": 0.32},
        {"min": 231250, "max": 578125, "rate": 0.35},
        {"min": 578125, "max": float('inf'), "rate": 0.37},
    ],
    "married_filing_jointly": [
        {"min": 0, "max": 22000, "rate": 0.10},
        {"min": 22000, "max": 89075, "rate": 0.12},
        {"min": 89075, "max": 190750, "rate": 0.22},
        {"min": 190750, "max": 364200, "rate": 0.24},
        {"min": 364200, "max": 462500, "rate": 0.32},
        {"min": 462500, "max": 693750, "rate": 0.35},
        {"min": 693750, "max": float('inf'), "rate": 0.37},
    ]
}

STANDARD_DEDUCTION_2024 = {
    "single": 13850,
    "married_filing_jointly": 27700,
    "married_filing_separately": 13850,
    "head_of_household": 20800,
}


# Tax terms (simple dicts for API/tests)
TAX_TERMS: Dict[str, Dict[str, str]] = {
    "gross_income": {
        "term": "Gross Income",
        "definition": "Total income from all sources BEFORE deductions or taxes.",
        "example": "Salary of $50,000 + side gig $5,000 = $55,000 gross income",
    },
    "taxable_income": {
        "term": "Taxable Income",
        "definition": "Income after deductions that is subject to tax.",
        "example": "$52,500 AGI - $13,850 standard deduction = $38,650 taxable income",
    },
    "marginal_rate": {
        "term": "Marginal Rate",
        "definition": "The tax rate on your last dollar earned.",
        "example": "$50,000 income falls into 22% bracket, so marginal rate is 22%.",
    },
    "effective_rate": {
        "term": "Effective Rate",
        "definition": "Overall percentage of income paid in taxes.",
        "example": "$50,000 income, $5,000 tax = 10% effective rate.",
    },
    "standard_deduction": {
        "term": "Standard Deduction",
        "definition": "Fixed deduction everyone can take.",
        "example": "Single filer subtracts $13,850 from income.",
    },
    "itemized_deductions": {
        "term": "Itemized Deductions",
        "definition": "Specific deductions listed instead of standard deduction.",
        "example": "Mortgage interest + property taxes + charity = itemized total.",
    },
    "tax_credit": {
        "term": "Tax Credit",
        "definition": "Dollar-for-dollar reduction in taxes owed.",
        "example": "$1,000 credit reduces tax bill by $1,000.",
    },
    "fica": {
        "term": "FICA Taxes",
        "definition": "Social Security (6.2%) + Medicare (1.45%).",
        "example": "$50,000 salary -> $3,825 FICA.",
    },
    "w4": {
        "term": "W-4 Form",
        "definition": "Form that sets paycheck withholding.",
        "example": "Fewer allowances = bigger refund.",
    },
    "1099_income": {
        "term": "1099 Income",
        "definition": "Self-employment income with no employer withholding.",
        "example": "Freelance income requires quarterly taxes.",
    },
    "earned_income_credit": {
        "term": "Earned Income Credit",
        "definition": "Refundable credit for low-to-moderate earners.",
        "example": "Qualify for $2,000 EITC and get a refund.",
    },
    "estimated_taxes": {
        "term": "Estimated Taxes",
        "definition": "Quarterly payments for self-employment income.",
        "example": "Pay quarterly to avoid a big April bill.",
    },
}


# Tax myths (simple dicts)
TAX_MYTHS: Dict[str, Dict[str, str]] = {
    "myth_refund_good": {
        "myth": "Getting a big tax refund is great - it means you're getting money back!",
        "fact": "FALSE. A refund means you overpaid and gave the government an interest-free loan.",
    },
    "myth_deduction_vs_credit": {
        "myth": "A tax deduction and tax credit are the same thing.",
        "fact": "FALSE. A credit reduces taxes dollar-for-dollar; a deduction only reduces taxable income.",
    },
    "myth_side_gig_taxes": {
        "myth": "You don't owe taxes on side gig income under $600.",
        "fact": "FALSE. You owe taxes on all income, regardless of 1099 threshold.",
    },
    "myth_cash_income_untaxed": {
        "myth": "Cash income is untaxed because there's no record.",
        "fact": "FALSE. Cash income is still taxable and must be reported.",
    },
    "myth_charitable_donations": {
        "myth": "All charitable donations give you a tax break.",
        "fact": "Only itemizers benefit; most people use the standard deduction.",
    },
    "myth_no_w2_no_tax": {
        "myth": "If you don't get a W-2, you don't have to pay taxes.",
        "fact": "FALSE. 1099, cash, and side gigs are taxable.",
    },
    "myth_dependent_exemption": {
        "myth": "Having a dependent exempts you from paying federal taxes.",
        "fact": "Dependents reduce taxes but do not exempt you from them.",
    },
}


def calculate_taxable_income(
    gross_income: float,
    filing_status: str = "single",
    deductions: Optional[float] = None,
) -> float:
    """Calculate taxable income as a single numeric value."""
    if deductions is None:
        deduction = STANDARD_DEDUCTION_2024.get(filing_status, STANDARD_DEDUCTION_2024["single"])
    else:
        deduction = deductions
    return gross_income - deduction


def calculate_income_tax(taxable_income: float, filing_status: str = "single") -> float:
    """Calculate income tax owed based on brackets."""
    
    brackets = TAX_BRACKETS_2024.get(filing_status, TAX_BRACKETS_2024["single"])
    tax = 0
    
    for bracket in brackets:
        if taxable_income <= bracket["min"]:
            break

        bracket_min = bracket["min"]
        bracket_max = bracket["max"]
        income_in_bracket = min(taxable_income, bracket_max) - bracket_min
        if income_in_bracket > 0:
            tax += income_in_bracket * bracket["rate"]
    
    return max(0, tax)


def calculate_fica_taxes(gross_income: float) -> Dict[str, float]:
    """Calculate Social Security and Medicare taxes."""
    
    ss_rate = 0.062
    medicare_rate = 0.0145
    ss_wage_cap = 168600  # 2024
    
    # Social Security (capped at wage cap)
    ss_wages = min(gross_income, ss_wage_cap)
    ss_tax = ss_wages * ss_rate
    
    # Medicare (no cap)
    medicare_tax = gross_income * medicare_rate
    
    # Additional Medicare if income > $200,000 (single)
    additional_medicare_rate = 0.009
    if gross_income > 200000:
        additional_medicare_tax = (gross_income - 200000) * additional_medicare_rate
        medicare_tax += additional_medicare_tax
    
    total_fica = ss_tax + medicare_tax
    
    return {
        "social_security": ss_tax,
        "medicare": medicare_tax,
        "total_fica": total_fica,
        "fica_rate": round((total_fica / gross_income) * 100, 2) if gross_income > 0 else 0
    }


def calculate_self_employment_tax(self_employment_income: float) -> float:
    """Calculate self-employment tax (1099 income)."""
    
    # SE tax is FICA for self-employed (you pay both sides)
    net_se_income = self_employment_income * 0.9235  # Adjust for deductible portion
    
    ss_tax = min(net_se_income, 168600) * 0.124  # Double the rate
    medicare_tax = net_se_income * 0.029
    
    total_se_tax = ss_tax + medicare_tax
    
    # Can deduct half of SE tax
    se_tax_deduction = total_se_tax / 2
    
    return total_se_tax


def get_term(term_id: str) -> Optional[Dict[str, str]]:
    """Get a tax term."""
    return TAX_TERMS.get(term_id)


def get_all_terms() -> List[Dict[str, str]]:
    """Get all tax terms."""
    return list(TAX_TERMS.values())


def get_myth(myth_id: str) -> Optional[Dict[str, str]]:
    """Get a tax myth."""
    return TAX_MYTHS.get(myth_id)


def get_all_myths() -> List[Dict[str, str]]:
    """Get all tax myths."""
    return list(TAX_MYTHS.values())


def get_tax_tips_for_income_level(income: float) -> List[str]:
    """Get personalized tax tips based on income level."""
    
    tips = []
    
    if income < 15000:
        tips.append("💰 You likely qualify for the Earned Income Credit (EITC). File a tax return to get it - it's free money!")
        tips.append("📝 Report all income, even cash. No tax owed if under the limit, but filing gets you EITC.")
    elif income < 50000:
        tips.append("📊 Check your W-4. You might be overpaying taxes and getting a refund (free loan to the government).")
        tips.append("📝 If you have side income, set aside 25-30% for taxes and estimated quarterly payments.")
    elif income < 100000:
        tips.append("💼 If married, consider filing status: MFJ vs MFS can save thousands.")
        tips.append("🏡 If you own a home, itemized deductions might be better than standard deduction.")
    else:
        tips.append("💎 Consider working with a CPA/tax professional. At this income level, tax optimization saves thousands.")
        tips.append("📈 Look into income deferral strategies (401k, traditional IRA) to reduce taxable income.")
    
    return tips
