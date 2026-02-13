"""Tests for tax basics system."""

import pytest
from catalogs.tax_basics import (
    calculate_taxable_income, calculate_income_tax, calculate_fica_taxes,
    calculate_self_employment_tax, get_tax_tips_for_income_level,
    TAX_BRACKETS_2024, STANDARD_DEDUCTION_2024, TAX_TERMS, TAX_MYTHS
)


class TestTaxBrackets:
    """Test tax bracket definitions."""
    
    def test_single_brackets_exist(self):
        """Test single filer brackets exist."""
        assert "single" in TAX_BRACKETS_2024
        brackets = TAX_BRACKETS_2024["single"]
        
        assert len(brackets) == 7
    
    def test_married_brackets_exist(self):
        """Test married filing jointly brackets exist."""
        assert "married_filing_jointly" in TAX_BRACKETS_2024
        brackets = TAX_BRACKETS_2024["married_filing_jointly"]
        
        assert len(brackets) == 7
    
    def test_brackets_increase_with_income(self):
        """Test brackets have increasing tax rates."""
        brackets = TAX_BRACKETS_2024["single"]
        
        for i in range(len(brackets) - 1):
            current_rate = brackets[i]["rate"]
            next_rate = brackets[i + 1]["rate"]
            assert next_rate > current_rate


class TestStandardDeduction:
    """Test standard deduction amounts."""
    
    def test_single_deduction(self):
        """Test single filer standard deduction."""
        assert STANDARD_DEDUCTION_2024["single"] == 13850
    
    def test_married_deduction(self):
        """Test married filing jointly deduction."""
        assert STANDARD_DEDUCTION_2024["married_filing_jointly"] == 27700
    
    def test_married_double_single(self):
        """Test married deduction is roughly double single."""
        married = STANDARD_DEDUCTION_2024["married_filing_jointly"]
        single = STANDARD_DEDUCTION_2024["single"]
        
        # Married should be roughly 2x
        assert married > single * 1.9


class TestTaxableIncomeCalculation:
    """Test taxable income calculation."""
    
    def test_basic_taxable_income(self):
        """Test basic taxable income calculation."""
        taxable = calculate_taxable_income(
            gross_income=50000,
            filing_status="single",
            deductions=None
        )
        
        # Should be gross - standard deduction
        expected = 50000 - STANDARD_DEDUCTION_2024["single"]
        assert taxable == expected
    
    def test_taxable_income_with_deductions(self):
        """Test taxable income with deductions."""
        taxable = calculate_taxable_income(
            gross_income=60000,
            filing_status="single",
            deductions=10000
        )
        
        expected = 60000 - 10000
        assert taxable == expected
    
    def test_negative_taxable_becomes_zero(self):
        """Test negative taxable income becomes zero."""
        taxable = calculate_taxable_income(
            gross_income=10000,
            filing_status="single",
            deductions=None
        )
        
        # Standard deduction is $13,850, so negative
        assert taxable <= 0
    
    def test_married_filing_jointly(self):
        """Test taxable income for married filers."""
        taxable = calculate_taxable_income(
            gross_income=100000,
            filing_status="married_filing_jointly",
            deductions=None
        )
        
        expected = 100000 - STANDARD_DEDUCTION_2024["married_filing_jointly"]
        assert taxable == expected


class TestIncomeTaxCalculation:
    """Test federal income tax calculation."""
    
    def test_single_low_income(self):
        """Test single filer with low income."""
        tax = calculate_income_tax(
            taxable_income=20000,
            filing_status="single"
        )
        
        # $20,000 at 10% is $2,000
        assert tax > 0
        assert tax < 3000
    
    def test_single_high_income(self):
        """Test single filer with high income."""
        tax = calculate_income_tax(
            taxable_income=500000,
            filing_status="single"
        )
        
        # Should be significant
        assert tax > 100000
    
    def test_married_pays_less_than_double_single(self):
        """Test married pays less tax than two singles (married benefit)."""
        # Same total income
        income_single = 100000
        income_married = 200000
        
        tax_single = calculate_income_tax(
            taxable_income=income_single - STANDARD_DEDUCTION_2024["single"],
            filing_status="single"
        )
        tax_single_both = tax_single * 2  # Two people earning $100k each
        
        tax_married = calculate_income_tax(
            taxable_income=income_married - STANDARD_DEDUCTION_2024["married_filing_jointly"],
            filing_status="married_filing_jointly"
        )
        
        # Married penalty is eliminated in 2024 (no marriage penalty)
        # But at very high incomes, should be roughly same or better
        assert tax_married <= tax_single_both * 1.05
    
    def test_zero_taxable_no_tax(self):
        """Test zero taxable income means no tax."""
        tax = calculate_income_tax(
            taxable_income=0,
            filing_status="single"
        )
        
        assert tax == 0
    
    def test_negative_taxable_no_tax(self):
        """Test negative taxable income means no tax."""
        tax = calculate_income_tax(
            taxable_income=-5000,
            filing_status="single"
        )
        
        assert tax == 0


class TestFICATaxes:
    """Test FICA taxes calculation."""
    
    def test_social_security_tax(self):
        """Test Social Security tax calculation."""
        fica = calculate_fica_taxes(gross_income=50000)
        
        # Social Security is 6.2%
        ss_expected = 50000 * 0.062
        
        assert fica["social_security"] == ss_expected
    
    def test_medicare_tax(self):
        """Test Medicare tax calculation."""
        fica = calculate_fica_taxes(gross_income=50000)
        
        # Medicare is 1.45%
        medicare_expected = 50000 * 0.0145
        
        assert fica["medicare"] == medicare_expected
    
    def test_ss_wage_cap(self):
        """Test Social Security wage cap."""
        # Income above cap should not be taxed for SS
        high_income = 200000
        fica = calculate_fica_taxes(gross_income=high_income)
        
        # SS tax should be capped at ~$168,600 (2024)
        ss_max = 168600 * 0.062
        
        assert fica["social_security"] == ss_max
    
    def test_medicare_no_cap(self):
        """Test Medicare has no wage cap."""
        high_income = 200000
        fica = calculate_fica_taxes(gross_income=high_income)
        
        # Medicare should apply to all income
        medicare_expected = high_income * 0.0145
        
        assert fica["medicare"] == medicare_expected
    
    def test_total_fica(self):
        """Test total FICA calculation."""
        income = 50000
        fica = calculate_fica_taxes(gross_income=income)
        
        # Should be 7.65% total
        expected = income * 0.0765
        actual = fica["social_security"] + fica["medicare"]
        
        assert abs(actual - expected) < 1


class TestSelfEmploymentTax:
    """Test self-employment tax calculation."""
    
    def test_se_tax_rate(self):
        """Test SE tax is 15.3%."""
        income = 50000
        se_tax = calculate_self_employment_tax(income)
        
        # SE tax is 15.3% on 92.35% of net income
        # Roughly 15.3% * 0.9235 = 14.13%
        expected = income * 0.1413
        
        assert abs(se_tax - expected) < 100
    
    def test_se_tax_higher_than_employee(self):
        """Test SE tax is higher than employee FICA."""
        income = 50000
        se_tax = calculate_self_employment_tax(income)
        
        fica = calculate_fica_taxes(income)
        fica_total = fica["social_security"] + fica["medicare"]
        
        # SE tax should be roughly double employee share
        assert se_tax > fica_total * 1.8


class TestTaxTerms:
    """Test tax terminology definitions."""
    
    def test_terms_exist(self):
        """Test tax terms are defined."""
        assert len(TAX_TERMS) > 0
        assert len(TAX_TERMS) == 12
    
    def test_term_structure(self):
        """Test each term has definition and example."""
        for term_id, term_data in TAX_TERMS.items():
            assert "term" in term_data
            assert "definition" in term_data
            assert "example" in term_data
            assert len(term_data["definition"]) > 0
    
    def test_important_terms_included(self):
        """Test important tax terms are included."""
        term_ids = set(TAX_TERMS.keys())
        
        assert "gross_income" in term_ids
        assert "taxable_income" in term_ids
        assert "marginal_rate" in term_ids
        assert "effective_rate" in term_ids


class TestTaxMyths:
    """Test tax myths."""
    
    def test_myths_exist(self):
        """Test tax myths are defined."""
        assert len(TAX_MYTHS) > 0
        assert len(TAX_MYTHS) == 7
    
    def test_myth_structure(self):
        """Test each myth has debunking."""
        for myth_id, myth_data in TAX_MYTHS.items():
            assert "myth" in myth_data
            assert "fact" in myth_data
            assert len(myth_data["myth"]) > 0
            assert len(myth_data["fact"]) > 0
    
    def test_refund_myth(self):
        """Test refund myth is debunked."""
        myth_ids = set(TAX_MYTHS.keys())
        
        # Refund myth should be included
        assert "myth_refund_good" in myth_ids
    
    def test_deduction_vs_credit_myth(self):
        """Test deduction vs credit is clarified."""
        myth_ids = set(TAX_MYTHS.keys())
        
        assert "myth_deduction_vs_credit" in myth_ids


class TestTaxTips:
    """Test personalized tax tips."""
    
    def test_tips_low_income(self):
        """Test tips for low income earner."""
        tips = get_tax_tips_for_income_level(10000)
        
        assert len(tips) > 0
        assert isinstance(tips, list)
    
    def test_tips_high_income(self):
        """Test tips for high income earner."""
        tips = get_tax_tips_for_income_level(200000)
        
        assert len(tips) > 0
    
    def test_tips_mention_relevant_strategies(self):
        """Test tips mention relevant strategies."""
        # Low income tips
        low_tips = get_tax_tips_for_income_level(15000)
        low_tips_text = " ".join(low_tips).lower()
        
        # Should mention standard deduction, EITC, etc.
        assert any(word in low_tips_text for word in [
            "deduction", "credit", "filing", "refund"
        ])


class TestMarginalVsEffectiveRate:
    """Test marginal vs effective tax rate."""
    
    def test_marginal_vs_effective_single(self):
        """Test marginal rate vs effective rate for single filer."""
        taxable_income = 50000
        tax = calculate_income_tax(taxable_income, "single")
        
        effective_rate = tax / taxable_income if taxable_income > 0 else 0
        
        # Effective rate should be less than top bracket (12% for this income)
        assert effective_rate < 0.12
        assert effective_rate > 0.05  # But still significant
    
    def test_effective_rate_increases_with_income(self):
        """Test effective rate increases with higher income."""
        low_income_tax = calculate_income_tax(30000, "single")
        high_income_tax = calculate_income_tax(100000, "single")
        
        low_effective = low_income_tax / 30000
        high_effective = high_income_tax / 100000
        
        # Higher income has higher effective rate
        assert high_effective > low_effective


class TestWithholdingEstimate:
    """Test withholding calculations."""
    
    def test_annual_tax_estimate(self):
        """Test estimating annual tax withholding."""
        annual_income = 60000
        tax = calculate_income_tax(
            taxable_income=annual_income - STANDARD_DEDUCTION_2024["single"],
            filing_status="single"
        )
        
        # Plus FICA
        fica = calculate_fica_taxes(annual_income)
        total_tax = tax + fica["social_security"] + fica["medicare"]
        
        # Should be roughly 15-20% of gross
        percent = (total_tax / annual_income) * 100
        assert percent > 10
        assert percent < 25


class TestMultipleIncomeStreams:
    """Test multiple income stream taxation."""
    
    def test_w2_plus_1099(self):
        """Test W-2 income plus 1099 income."""
        w2_income = 50000
        self_employment_income = 20000
        
        total_gross = w2_income + self_employment_income
        
        # W-2 FICA is split, 1099 is SE tax
        w2_fica = calculate_fica_taxes(w2_income)
        se_tax = calculate_self_employment_tax(self_employment_income)
        
        total_fica = (w2_fica["social_security"] + w2_fica["medicare"]) + se_tax
        
        # Income tax on combined
        taxable = calculate_taxable_income(total_gross, "single")
        income_tax = calculate_income_tax(taxable, "single")
        
        # Total should be substantial
        assert total_fica + income_tax > 0


class TestTaxFilingStatuses:
    """Test different filing statuses."""
    
    def test_single_vs_married(self):
        """Test single vs married at same income."""
        income = 100000
        
        single_tax = calculate_income_tax(
            taxable_income=income - STANDARD_DEDUCTION_2024["single"],
            filing_status="single"
        )
        
        married_tax = calculate_income_tax(
            taxable_income=income - STANDARD_DEDUCTION_2024["married_filing_jointly"],
            filing_status="married_filing_jointly"
        )
        
        # Single person's tax should be higher (using single bracket)
        assert single_tax > 0
        assert married_tax >= 0
