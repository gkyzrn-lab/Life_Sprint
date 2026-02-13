from __future__ import annotations

from core_domain.finance.finance_models import RepaymentProfile


def amortized_payment(principal: float, annual_rate: float, months: int) -> float:
    """
    Standard fixed monthly payment for amortizing loan.
    """
    if principal <= 0 or months <= 0:
        return 0.0
    r = annual_rate / 12.0
    if r == 0:
        return principal / months
    return principal * (r * (1 + r) ** months) / ((1 + r) ** months - 1)


def compute_idr_monthly_payment(profile: RepaymentProfile) -> float:
    """
    Simple IDR model:
      - poverty threshold = poverty_line_annual * discretionary_multiplier * family_adjust
      - discretionary = max(0, income - threshold)
      - payment = idr_percent * discretionary / 12

    family_adjust is a simple curve: +35% threshold per extra family member.
    """
    fam = max(1, int(profile.family_size))
    family_adj = 1.0 + 0.35 * max(0, fam - 1)

    poverty_threshold = float(profile.poverty_line_annual) * float(profile.discretionary_multiplier) * family_adj
    discretionary_income = max(0.0, float(profile.annual_income) - poverty_threshold)

    annual_payment = float(profile.idr_percent) * discretionary_income
    monthly = max(0.0, annual_payment / 12.0)
    return monthly
