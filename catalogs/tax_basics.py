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
        {"min": 11000, "max": 44725, "rate": 0.12},
        {"min": 44725, "max": 95375, "rate": 0.22},
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


# Tax terms
TAX_TERMS: Dict[str, TaxTerm] = {
    "gross_income": TaxTerm(
        term_id="gross_income",
        term_name="Gross Income",
        definition="Total income from all sources BEFORE deductions or taxes.",
        example="Salary of $50,000 + side gig $5,000 = $55,000 gross income",
        importance="critical"
    ),
    
    "adjusted_gross_income": TaxTerm(
        term_id="adjusted_gross_income",
        term_name="Adjusted Gross Income (AGI)",
        definition="Gross income minus specific deductions like student loan interest, IRA contributions, etc.",
        example="$55,000 gross income - $2,500 student loan interest = $52,500 AGI",
        importance="critical"
    ),
    
    "taxable_income": TaxTerm(
        term_id="taxable_income",
        term_name="Taxable Income",
        definition="AGI minus either standard or itemized deduction. This is the income that gets taxed.",
        example="$52,500 AGI - $13,850 standard deduction = $38,650 taxable income",
        importance="critical"
    ),
    
    "marginal_tax_rate": TaxTerm(
        term_id="marginal_tax_rate",
        term_name="Marginal Tax Rate",
        definition="The tax rate on your LAST dollar earned. Not your overall rate! The bracket your income falls into.",
        example="$38,650 income falls in 22% bracket = 22% marginal rate. But you don't pay 22% on all income.",
        importance="critical"
    ),
    
    "effective_tax_rate": TaxTerm(
        term_id="effective_tax_rate",
        term_name="Effective Tax Rate",
        definition="Actual percentage of total income that goes to taxes. Usually MUCH lower than marginal rate.",
        example="$50,000 salary, pay $5,000 in taxes = 10% effective rate (even though marginal rate is 22%)",
        importance="critical"
    ),
    
    "standard_deduction": TaxTerm(
        term_id="standard_deduction",
        term_name="Standard Deduction",
        definition="Fixed deduction everyone can take. In 2024: $13,850 single, $27,700 married. Simpler than itemizing.",
        example="Single, $50,000 income: Subtract $13,850 standard deduction = $36,150 taxable",
        importance="critical"
    ),
    
    "itemized_deductions": TaxTerm(
        term_id="itemized_deductions",
        term_name="Itemized Deductions",
        definition="When you list out specific deductions (mortgage interest, property taxes, charitable donations) instead of standard deduction.",
        example="Home owner: Mortgage interest $12,000 + property tax $5,000 + charity $2,000 = $19,000 itemized (better than $13,850 standard)",
        importance="important"
    ),
    
    "tax_credit": TaxTerm(
        term_id="tax_credit",
        term_name="Tax Credit",
        definition="Dollar-for-dollar reduction in taxes owed. $1 credit = $1 less tax (much better than deduction!).",
        example="$2,000 child tax credit = $2,000 off your tax bill. $2,000 deduction = only saves $2,000 × your rate (~$400)",
        importance="critical"
    ),
    
    "fica_taxes": TaxTerm(
        term_id="fica_taxes",
        term_name="FICA Taxes",
        definition="Social Security (6.2%) + Medicare (1.45%) = 7.65% of wages. Employer matches it.",
        example="$50,000 salary: Pay $3,825 in FICA. Employer pays another $3,825. Total: $7,650/year.",
        importance="critical"
    ),
    
    "w4_form": TaxTerm(
        term_id="w4_form",
        term_name="W-4 Form",
        definition="Form you fill out with employer to set tax withholding. Controls how much tax is taken from paycheck.",
        example="Claim 0 dependents = more withholding = bigger refund. Claim 2 = less withholding = smaller refund.",
        importance="important"
    ),
    
    "1099_income": TaxTerm(
        term_id="1099_income",
        term_name="1099 Income (Self-Employment)",
        definition="Income from side gigs, freelancing, etc. You're responsible for ALL taxes (no employer to match FICA).",
        example="Earn $10,000 from Uber: Pay income tax + 15.3% self-employment tax (~$1,530). Not just ~$1,000 like W-2.",
        importance="critical"
    ),
    
    "earned_income_credit": TaxTerm(
        term_id="earned_income_credit",
        term_name="Earned Income Credit (EITC)",
        definition="Tax credit for low-to-moderate income workers. Can be up to $3,995 for single, $6,932 for families.",
        example="Single, $25,000 income: Qualify for $2,000 EITC. Tax bill is $0, get $2,000 refund!",
        importance="important"
    ),
    
    "capital_gains": TaxTerm(
        term_id="capital_gains",
        term_name="Capital Gains",
        definition="Profit from selling stocks, real estate, etc. Taxed at lower rate than regular income (0%, 15%, or 20%).",
        example="Buy stock for $1,000, sell for $1,500: $500 gain taxed at 15% = $75 tax. Regular income at same rate = ~$110 tax.",
        importance="important"
    ),
    
    "estimated_taxes": TaxTerm(
        term_id="estimated_taxes",
        term_name="Estimated Taxes",
        definition="Quarterly tax payments you make if you have self-employment or side gig income (no employer withholding).",
        example="Earn $20,000 from freelancing: Make 4 quarterly payments of ~$800-1,000 throughout year instead of surprise bill in April.",
        importance="important"
    ),
}


# Tax myths
TAX_MYTHS: Dict[str, TaxMythFact] = {
    "myth_refund_free_money": TaxMythFact(
        myth_id="myth_refund_free_money",
        myth="Getting a big tax refund is great - it means you're getting money back!",
        fact="A refund just means you overpaid taxes (lent money to government interest-free). A $3,000 refund = $3,000 you could have earned interest on all year. Adjust W-4 to get refund closer to $0.",
        financial_impact="$3,000 refund at 4% interest = $120/year you're losing"
    ),
    
    "myth_deduction_better_than_credit": TaxMythFact(
        myth_id="myth_deduction_better_than_credit",
        myth="A tax deduction and tax credit are the same thing.",
        fact="$1 credit = $1 off your taxes. $1 deduction = only saves ~$0.22-$0.37 depending on bracket. Credits are MUCH better.",
        financial_impact="$1,000 credit saves $1,000. $1,000 deduction saves ~$220"
    ),
    
    "myth_side_gig_taxes": TaxMythFact(
        myth_id="myth_side_gig_taxes",
        myth="You don't owe taxes on side gig income under $600.",
        fact="WRONG. You owe taxes on ALL income. 1099 threshold is just when companies report it. Failing to report is tax evasion (illegal).",
        financial_impact="$5,000 unreported side gig income = ~$1,200 unpaid taxes + penalties/interest"
    ),
    
    "myth_cash_income_untaxed": TaxMythFact(
        myth_id="myth_cash_income_untaxed",
        myth="Cash income is untaxed because there's no record.",
        fact="WRONG. You're legally required to report all income, cash or not. Getting caught = penalties + back interest (~30% total).",
        financial_impact="$10,000 cash income: Owe $2,200 tax. Don't report: Owe $2,200 + 20% penalty + interest = ~$3,000"
    ),
    
    "myth_charitable_donations": TaxMythFact(
        myth_id="myth_charitable_donations",
        myth="All charitable donations give you a tax break.",
        fact="Only itemizers benefit. Most people use standard deduction. If deduction < itemized ($13,850 single), you get $0 benefit.",
        financial_impact="Donate $5,000 without itemizing = $0 tax benefit. Donate with itemizing = $1,150 tax benefit (22% rate)"
    ),
    
    "myth_no_w2_no_tax": TaxMythFact(
        myth_id="myth_no_w2_no_tax",
        myth="If you don't get a W-2, you don't have to pay taxes.",
        fact="You owe taxes on all income sources. 1099, cash, side gigs - all taxable. Report it or face penalties.",
        financial_impact="Fail to report $15,000 1099 income = $3,300 unpaid tax + 20% penalty = ~$4,000 owed"
    ),
    
    "myth_dependent_exemption": TaxMythFact(
        myth_id="myth_dependent_exemption",
        myth="Having a dependent exempts you from paying federal taxes.",
        fact="Dependents give you credits/deductions, not an exemption from taxes. You still owe taxes; dependents just reduce them.",
        financial_impact="Each child = $2,000 child tax credit (not exemption from taxes entirely)"
    ),
}


def calculate_taxable_income(
    gross_income: float,
    filing_status: str = "single",
    itemized_deductions: float = 0,
    agi_adjustments: float = 0
) -> Dict[str, float]:
    """Calculate taxable income.
    
    Returns:
        {
            "gross_income": ...,
            "agi": ...,
            "deduction_used": ...,
            "taxable_income": ...
        }
    """
    
    # Calculate AGI
    agi = gross_income - agi_adjustments
    
    # Determine deduction
    standard_ded = STANDARD_DEDUCTION_2024.get(filing_status, STANDARD_DEDUCTION_2024["single"])
    deduction = max(standard_ded, itemized_deductions)
    
    # Calculate taxable income
    taxable = max(0, agi - deduction)
    
    return {
        "gross_income": gross_income,
        "agi": agi,
        "deduction_amount": deduction,
        "deduction_type": "itemized" if itemized_deductions > standard_ded else "standard",
        "taxable_income": taxable
    }


def calculate_income_tax(taxable_income: float, filing_status: str = "single") -> float:
    """Calculate income tax owed based on brackets."""
    
    brackets = TAX_BRACKETS_2024.get(filing_status, TAX_BRACKETS_2024["single"])
    tax = 0
    
    for bracket in brackets:
        if taxable_income <= bracket["min"]:
            break
        
        # Income in this bracket
        bracket_min = max(taxable_income, bracket["min"])
        bracket_max = min(taxable_income, bracket["max"])
        
        if bracket_min < bracket_max:
            income_in_bracket = bracket_max - bracket_min
            tax += income_in_bracket * bracket["rate"]
    
    return max(0, tax)


def calculate_fica_taxes(w2_income: float) -> Dict[str, float]:
    """Calculate Social Security and Medicare taxes."""
    
    ss_rate = 0.062
    medicare_rate = 0.0145
    ss_wage_cap = 168600  # 2024
    
    # Social Security (capped at wage cap)
    ss_wages = min(w2_income, ss_wage_cap)
    ss_tax = ss_wages * ss_rate
    
    # Medicare (no cap)
    medicare_tax = w2_income * medicare_rate
    
    # Additional Medicare if income > $200,000 (single)
    additional_medicare_rate = 0.009
    if w2_income > 200000:
        additional_medicare_tax = (w2_income - 200000) * additional_medicare_rate
        medicare_tax += additional_medicare_tax
    
    total_fica = ss_tax + medicare_tax
    
    return {
        "social_security_tax": ss_tax,
        "medicare_tax": medicare_tax,
        "total_fica": total_fica,
        "fica_rate": round((total_fica / w2_income) * 100, 2) if w2_income > 0 else 0
    }


def calculate_self_employment_tax(self_employment_income: float) -> Dict[str, float]:
    """Calculate self-employment tax (1099 income)."""
    
    # SE tax is FICA for self-employed (you pay both sides)
    net_se_income = self_employment_income * 0.9235  # Adjust for deductible portion
    
    ss_tax = min(net_se_income, 168600) * 0.124  # Double the rate
    medicare_tax = net_se_income * 0.029
    
    total_se_tax = ss_tax + medicare_tax
    
    # Can deduct half of SE tax
    se_tax_deduction = total_se_tax / 2
    
    return {
        "self_employment_tax": total_se_tax,
        "se_tax_deduction": se_tax_deduction,
        "effective_rate": round((total_se_tax / self_employment_income) * 100, 2)
    }


def get_term(term_id: str) -> Optional[TaxTerm]:
    """Get a tax term."""
    return TAX_TERMS.get(term_id)


def get_all_terms() -> List[TaxTerm]:
    """Get all tax terms."""
    return list(TAX_TERMS.values())


def get_myth(myth_id: str) -> Optional[TaxMythFact]:
    """Get a tax myth."""
    return TAX_MYTHS.get(myth_id)


def get_all_myths() -> List[TaxMythFact]:
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
