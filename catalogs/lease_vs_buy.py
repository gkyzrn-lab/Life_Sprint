"""Lease vs Buy calculator - compares financial implications of leasing vs buying."""

from typing import Dict, List, Optional, Literal
from pydantic import BaseModel, Field


class LeaseScenario(BaseModel):
    """Leasing scenario for a vehicle."""
    scenario_id: str
    vehicle_name: str
    
    # Lease terms
    monthly_payment: float
    lease_term_months: int
    mileage_allowance: int  # Annual miles included
    excess_mileage_cost: float  # Per mile over limit
    
    # Included in lease
    insurance_included: bool
    maintenance_included: bool
    wear_tear_included: bool
    road_assistance_included: bool
    
    # Additional costs (not included)
    registration: float = 0
    insurance_extra: float = 0  # If not included
    maintenance_extra: float = 0  # If not included
    acquisition_fee: float = 0
    disposition_fee: float = 0  # At end of lease
    
    # Usage
    expected_annual_mileage: int
    excess_mileage_estimate: float = 0


class BuyScenario(BaseModel):
    """Buying scenario for a vehicle."""
    scenario_id: str
    vehicle_name: str
    
    # Purchase price
    vehicle_price: float
    down_payment: float
    
    # Financing
    loan_amount: float = 0
    interest_rate: float
    loan_term_months: int  # Usually 36, 48, 60, 72
    monthly_payment: float
    
    # Ownership costs
    registration: float
    title: float
    annual_insurance: float
    annual_maintenance: float  # Increases with age
    annual_depreciation: float
    
    # Other
    expected_annual_mileage: int
    ownership_years: int


class LeaseVsBuyAnalysis(BaseModel):
    """Comparison of leasing vs buying."""
    scenario_id: str
    
    lease_scenario: LeaseScenario
    buy_scenario: BuyScenario
    
    # Analysis over time period (usually 3-6 years)
    analysis_period_years: int
    
    # Total costs
    total_lease_cost: float
    total_buy_cost: float
    total_ownership_cost: float  # Total buy minus residual value
    
    # Comparison
    lease_cheaper_by: float  # Positive if lease is cheaper
    winner: Literal["lease", "buy", "similar"]
    
    # Other factors
    mileage_impact: float  # Extra cost if over mileage
    wear_tear_impact: float  # Potential lease damage charges
    residual_value: float  # Car value at end of analysis


class LeaseProCon(BaseModel):
    """Pros and cons of leasing."""
    aspect: str
    lease_advantage: str
    buy_advantage: str


# Lease vs Buy Analysis Factors
LEASE_VS_BUY_FACTORS = {
    "mileage": LeaseProCon(
        aspect="Mileage",
        lease_advantage="12,000 miles/year is standard. Perfect if you drive under limit. Excess mileage costs $0.15-0.30/mile.",
        buy_advantage="Unlimited mileage. Drive as much as you want. No overage penalties."
    ),
    
    "wear_tear": LeaseProCon(
        aspect="Wear and Tear",
        lease_advantage="Lease covers normal wear. No charge for small dings, fading trim, worn floor mats.",
        buy_advantage="Your car, your responsibility. But you control maintenance, repairs, aesthetics."
    ),
    
    "maintenance": LeaseProCon(
        aspect="Maintenance",
        lease_advantage="Lease includes most maintenance. Oil changes, tire rotations, repairs under warranty. Predictable costs.",
        buy_advantage="You control maintenance. Can use cheaper parts/labor. Expensive repairs after warranty end."
    ),
    
    "repair_risk": LeaseProCon(
        aspect="Unexpected Repairs",
        lease_advantage="Warranty covers unexpected repairs. $0 for transmission failure, engine problems. Predictable.",
        buy_advantage="Responsible for all repairs. Transmission repair = $3,000+, engine = $5,000+. Risk is yours."
    ),
    
    "depreciation": LeaseProCon(
        aspect="Depreciation",
        lease_advantage="Ignore depreciation. Car loses 50%+ value in 5 years. Not your problem.",
        buy_advantage="If car depreciates slow, or you keep long-term, better value. Some cars hold value well."
    ),
    
    "ownership": LeaseProCon(
        aspect="Ownership",
        lease_advantage="Never own. Always get new cars. Latest technology, safety features.",
        buy_advantage="You own it. Keep as long as you want. Customize it. Build equity."
    ),
    
    "flexibility": LeaseProCon(
        aspect="Flexibility",
        lease_advantage="Get new car every 3 years. Tastes change, wants change. Easy to switch.",
        buy_advantage="Keep car beyond loan payoff. Own outright eventually. Only 2-3 car purchases in lifetime."
    ),
    
    "total_cost": LeaseProCon(
        aspect="Total Cost",
        lease_advantage="Fixed monthly payment. Predictable budget. No surprises (if you stay in mileage).",
        buy_advantage="No payment after loan ends (3-6 years). Can drive free for 5-10 years after."
    ),
}


def calculate_lease_cost(lease: LeaseScenario, analysis_years: int) -> Dict[str, float]:
    """Calculate total lease cost over analysis period."""
    
    total_months = analysis_years * 12
    
    # Monthly costs
    total_payments = lease.monthly_payment * total_months
    
    # Annual costs
    total_registration = lease.registration * analysis_years
    total_insurance = lease.insurance_extra * analysis_years if not lease.insurance_included else 0
    total_maintenance = lease.maintenance_extra * analysis_years if not lease.maintenance_included else 0
    
    # Acquisition and disposition
    acquisition = lease.acquisition_fee
    disposition = lease.disposition_fee
    
    # Mileage
    expected_total_miles = lease.expected_annual_mileage * analysis_years
    included_miles = lease.mileage_allowance * analysis_years
    excess_miles = max(0, expected_total_miles - included_miles)
    excess_mileage_cost = excess_miles * lease.excess_mileage_cost
    
    total_cost = (
        total_payments +
        total_registration +
        total_insurance +
        total_maintenance +
        acquisition +
        disposition +
        excess_mileage_cost
    )
    
    return {
        "monthly_payments": total_payments,
        "registration": total_registration,
        "insurance": total_insurance,
        "maintenance": total_maintenance,
        "acquisition_fee": acquisition,
        "disposition_fee": disposition,
        "excess_mileage": excess_mileage_cost,
        "total_cost": total_cost,
        "cost_per_month": total_cost / total_months,
    }


def calculate_buy_cost(buy: BuyScenario, analysis_years: int) -> Dict[str, float]:
    """Calculate total ownership cost over analysis period."""
    
    total_months = analysis_years * 12
    
    # Loan payments
    total_loan_payments = buy.monthly_payment * min(buy.loan_term_months, total_months)
    
    # Registration and title (one-time)
    upfront = buy.down_payment + buy.registration + buy.title
    
    # Annual costs
    total_insurance = buy.annual_insurance * analysis_years
    total_maintenance = buy.annual_maintenance * analysis_years
    total_depreciation = buy.annual_depreciation * analysis_years
    
    # Residual value (estimated)
    residual_value = buy.vehicle_price - total_depreciation
    
    total_cost = (
        upfront +
        total_loan_payments +
        total_insurance +
        total_maintenance +
        total_depreciation
    )
    
    # Net cost after selling
    net_cost = total_cost - residual_value
    
    return {
        "down_payment": buy.down_payment,
        "registration_title": buy.registration + buy.title,
        "loan_payments": total_loan_payments,
        "insurance": total_insurance,
        "maintenance": total_maintenance,
        "depreciation": total_depreciation,
        "residual_value": residual_value,
        "total_cost": total_cost,
        "net_cost": net_cost,
        "cost_per_month": net_cost / total_months,
    }


def compare_lease_vs_buy(lease: LeaseScenario, buy: BuyScenario, analysis_years: int) -> Dict:
    """Compare leasing vs buying."""
    
    lease_cost = calculate_lease_cost(lease, analysis_years)
    buy_cost = calculate_buy_cost(buy, analysis_years)
    
    lease_total = lease_cost["total_cost"]
    buy_total = buy_cost["net_cost"]
    
    difference = lease_total - buy_total
    
    if difference < -500:  # Buying is cheaper (within $500 margin)
        winner = "buy"
    elif difference > 500:  # Leasing is cheaper
        winner = "lease"
    else:
        winner = "similar"
    
    return {
        "lease_analysis": lease_cost,
        "buy_analysis": buy_cost,
        "comparison": {
            "lease_total": lease_total,
            "buy_total": buy_total,
            "difference": difference,
            "winner": winner,
            "lease_cheaper_by": max(0, -difference),
            "buy_cheaper_by": max(0, difference),
        }
    }


# Example scenarios
EXAMPLE_SCENARIOS = {
    "civic_scenario": {
        "lease": LeaseScenario(
            scenario_id="civic_lease",
            vehicle_name="2026 Honda Civic (Lease)",
            monthly_payment=299,
            lease_term_months=36,
            mileage_allowance=12000,
            excess_mileage_cost=0.25,
            insurance_included=False,
            maintenance_included=True,
            wear_tear_included=True,
            road_assistance_included=True,
            registration=150,
            insurance_extra=1200,  # Annual
            acquisition_fee=695,
            disposition_fee=395,
            expected_annual_mileage=12000,
        ),
        "buy": BuyScenario(
            scenario_id="civic_buy",
            vehicle_name="2026 Honda Civic (Buy)",
            vehicle_price=28000,
            down_payment=3000,
            loan_amount=25000,
            interest_rate=0.065,
            loan_term_months=60,
            monthly_payment=481,
            registration=200,
            title=50,
            annual_insurance=1200,
            annual_maintenance=500,  # Year 1-3: oil changes, tires. Year 4-5: more
            annual_depreciation=3500,  # Car depreciates ~$3500/year for 5 years
            expected_annual_mileage=12000,
            ownership_years=5,
        )
    },
    
    "suv_scenario": {
        "lease": LeaseScenario(
            scenario_id="suv_lease",
            vehicle_name="2026 Toyota RAV4 (Lease)",
            monthly_payment=399,
            lease_term_months=36,
            mileage_allowance=12000,
            excess_mileage_cost=0.25,
            insurance_included=False,
            maintenance_included=True,
            wear_tear_included=True,
            road_assistance_included=True,
            registration=200,
            insurance_extra=1500,  # Annual
            acquisition_fee=795,
            disposition_fee=395,
            expected_annual_mileage=12000,
        ),
        "buy": BuyScenario(
            scenario_id="suv_buy",
            vehicle_name="2026 Toyota RAV4 (Buy)",
            vehicle_price=35000,
            down_payment=5000,
            loan_amount=30000,
            interest_rate=0.068,
            loan_term_months=60,
            monthly_payment=590,
            registration=250,
            title=75,
            annual_insurance=1500,
            annual_maintenance=600,  # Higher for SUV
            annual_depreciation=4200,
            expected_annual_mileage=12000,
            ownership_years=5,
        )
    },
    
    "high_mileage": {
        "lease": LeaseScenario(
            scenario_id="high_mileage_lease",
            vehicle_name="Car Lease (High Mileage)",
            monthly_payment=299,
            lease_term_months=36,
            mileage_allowance=12000,
            excess_mileage_cost=0.25,
            insurance_included=False,
            maintenance_included=True,
            wear_tear_included=True,
            road_assistance_included=True,
            registration=150,
            insurance_extra=1200,
            acquisition_fee=695,
            disposition_fee=395,
            expected_annual_mileage=18000,  # High mileage!
        ),
        "buy": BuyScenario(
            scenario_id="high_mileage_buy",
            vehicle_name="Car (High Mileage)",
            vehicle_price=20000,  # Used car (better for high mileage)
            down_payment=2000,
            loan_amount=18000,
            interest_rate=0.08,
            loan_term_months=48,
            monthly_payment=441,
            registration=180,
            title=40,
            annual_insurance=1100,
            annual_maintenance=800,  # Higher maintenance for used
            annual_depreciation=1800,  # Used car depreciates slower
            expected_annual_mileage=18000,
            ownership_years=4,
        )
    }
}


def get_factor(aspect: str) -> Optional[LeaseProCon]:
    """Get lease vs buy factor."""
    return LEASE_VS_BUY_FACTORS.get(aspect)


def get_all_factors() -> List[LeaseProCon]:
    """Get all factors."""
    return list(LEASE_VS_BUY_FACTORS.values())


def get_scenario(scenario_name: str) -> Optional[Dict]:
    """Get example scenario."""
    return EXAMPLE_SCENARIOS.get(scenario_name)


def get_all_scenarios() -> List[str]:
    """Get all scenario names."""
    return list(EXAMPLE_SCENARIOS.keys())


# Housing lease vs buy

class HousingLeaseOption(BaseModel):
    """Renting a home."""
    option_id: str
    monthly_rent: float
    lease_term: int  # months
    security_deposit: float
    annual_property_tax: float = 0  # Included in rent
    renters_insurance: float = 0  # Annual
    utilities: float = 0  # Annual (estimated)
    maintenance_cost: float = 0  # Should be $0 (landlord)


class HousingBuyOption(BaseModel):
    """Buying a home."""
    option_id: str
    home_price: float
    down_payment_percent: float  # 3%, 5%, 10%, 20%
    down_payment: float = 0
    
    # Loan
    loan_amount: float = 0
    interest_rate: float
    loan_term_years: int  # 15, 30
    monthly_payment: float
    
    # Taxes and insurance
    annual_property_tax: float
    annual_home_insurance: float
    annual_hoa: float = 0
    
    # Maintenance
    annual_maintenance: float = 0  # 1-2% of home value
    
    # Utilities
    utilities: float = 0  # Annual
    
    # Equity buildup
    expected_appreciation: float = 0.03  # 3% per year


def compare_housing_lease_vs_buy(
    rent_option: HousingLeaseOption,
    buy_option: HousingBuyOption,
    analysis_years: int = 5
) -> Dict:
    """Compare housing lease vs buy."""
    
    # Renting costs
    total_rent = rent_option.monthly_rent * 12 * analysis_years
    total_renters_insurance = rent_option.renters_insurance * analysis_years
    total_utilities = rent_option.utilities * analysis_years
    total_rent_cost = (
        total_rent +
        rent_option.security_deposit +
        total_renters_insurance +
        total_utilities
    )
    
    # Buying costs
    # Down payment
    down_payment = buy_option.down_payment
    
    # Loan payments
    total_loan_payments = buy_option.monthly_payment * 12 * analysis_years
    
    # Annual costs
    total_taxes = buy_option.annual_property_tax * analysis_years
    total_insurance = buy_option.annual_home_insurance * analysis_years
    total_hoa = buy_option.annual_hoa * analysis_years
    total_maintenance = buy_option.annual_maintenance * analysis_years
    total_utilities_buy = buy_option.utilities * analysis_years
    
    total_buy_cost = (
        down_payment +
        total_loan_payments +
        total_taxes +
        total_insurance +
        total_hoa +
        total_maintenance +
        total_utilities_buy
    )
    
    # Home appreciation
    home_value = buy_option.home_price
    for _ in range(analysis_years):
        home_value *= (1 + buy_option.expected_appreciation)
    
    equity = home_value - (buy_option.loan_amount - (buy_option.monthly_payment * 12 * analysis_years * 0.3))  # Rough estimate
    
    return {
        "rent_analysis": {
            "monthly_rent": total_rent / (analysis_years * 12),
            "total_rent": total_rent,
            "insurance_utilities": total_renters_insurance + total_utilities,
            "upfront": rent_option.security_deposit,
            "total_cost": total_rent_cost,
            "cost_per_month": total_rent_cost / (analysis_years * 12),
        },
        "buy_analysis": {
            "down_payment": down_payment,
            "monthly_payment": buy_option.monthly_payment,
            "annual_taxes": buy_option.annual_property_tax,
            "annual_insurance": buy_option.annual_home_insurance,
            "annual_maintenance": buy_option.annual_maintenance,
            "total_loan_payments": total_loan_payments,
            "total_taxes": total_taxes,
            "total_insurance": total_insurance,
            "total_maintenance": total_maintenance,
            "total_cost": total_buy_cost,
            "cost_per_month": total_buy_cost / (analysis_years * 12),
            "home_appreciation": home_value - buy_option.home_price,
            "estimated_equity": equity,
        },
        "comparison": {
            "rent_total": total_rent_cost,
            "buy_total": total_buy_cost,
            "difference": total_rent_cost - total_buy_cost,
            "rent_cheaper_by": max(0, total_buy_cost - total_rent_cost),
            "buy_cheaper_by": max(0, total_rent_cost - total_buy_cost),
            "note": "Buy appears cheaper but you build equity. Rent is pure expense. Decision depends on plans (stay 5+ years = buy better)"
        }
    }
