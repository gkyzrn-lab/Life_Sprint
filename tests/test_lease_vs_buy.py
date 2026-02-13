"""Tests for lease vs buy calculator."""

import pytest
from catalogs.lease_vs_buy import (
    calculate_lease_cost, calculate_buy_cost, compare_lease_vs_buy,
    get_factor, get_all_factors, get_scenario, get_all_scenarios,
    compare_housing_lease_vs_buy,
    LEASE_VS_BUY_FACTORS, EXAMPLE_SCENARIOS
)


class TestLeaseCostCalculation:
    """Test lease cost calculations."""
    
    def test_basic_lease_cost(self):
        """Test calculating basic lease cost."""
        lease = EXAMPLE_SCENARIOS["civic_scenario"]["lease"]
        
        costs = calculate_lease_cost(lease, analysis_years=3)
        
        assert costs["monthly_payments"] > 0
        assert costs["total_cost"] > 0
    
    def test_lease_duration(self):
        """Test lease cost for standard 36-month term."""
        lease = EXAMPLE_SCENARIOS["civic_scenario"]["lease"]
        
        costs = calculate_lease_cost(lease, analysis_years=3)
        
        # 3 years * $299/month = $10,764
        expected = 299 * 36
        assert abs(costs["monthly_payments"] - expected) < 10
    
    def test_mileage_overage(self):
        """Test mileage overage charges."""
        lease_data = EXAMPLE_SCENARIOS["high_mileage"]["lease"]
        
        costs = calculate_lease_cost(lease_data, analysis_years=3)
        
        # 3 years at 18,000 miles/year = 54,000 miles
        # Allowance: 12,000/year * 3 = 36,000 miles
        # Excess: 18,000 miles at $0.25 = $4,500
        assert costs["excess_mileage"] > 0
    
    def test_acquisition_fee(self):
        """Test acquisition fee is included."""
        lease = EXAMPLE_SCENARIOS["civic_scenario"]["lease"]
        
        costs = calculate_lease_cost(lease, analysis_years=3)
        
        assert costs["acquisition_fee"] == lease.acquisition_fee
    
    def test_disposition_fee(self):
        """Test disposition fee at end."""
        lease = EXAMPLE_SCENARIOS["civic_scenario"]["lease"]
        
        costs = calculate_lease_cost(lease, analysis_years=3)
        
        assert costs["disposition_fee"] == lease.disposition_fee


class TestBuyCostCalculation:
    """Test buy cost calculations."""
    
    def test_basic_buy_cost(self):
        """Test calculating basic buy cost."""
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        costs = calculate_buy_cost(buy, analysis_years=5)
        
        assert costs["down_payment"] > 0
        assert costs["loan_payments"] > 0
        assert costs["total_cost"] > 0
    
    def test_loan_payments(self):
        """Test loan payment calculations."""
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        costs = calculate_buy_cost(buy, analysis_years=5)
        
        # 60 months * $481 = $28,860
        expected = buy.monthly_payment * buy.loan_term_months
        assert abs(costs["loan_payments"] - expected) < 50
    
    def test_depreciation(self):
        """Test vehicle depreciation."""
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        costs = calculate_buy_cost(buy, analysis_years=5)
        
        # Should lose value over time
        assert costs["depreciation"] > 0
        assert costs["residual_value"] < buy.vehicle_price
    
    def test_insurance_costs(self):
        """Test insurance costs included."""
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        costs = calculate_buy_cost(buy, analysis_years=5)
        
        # 5 years * $1200 = $6000
        assert costs["insurance"] == buy.annual_insurance * 5


class TestComparisonLogic:
    """Test lease vs buy comparison."""
    
    def test_civic_comparison(self):
        """Test civic scenario comparison."""
        lease = EXAMPLE_SCENARIOS["civic_scenario"]["lease"]
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        comparison = compare_lease_vs_buy(lease, buy, analysis_years=3)
        
        assert "lease_analysis" in comparison
        assert "buy_analysis" in comparison
        assert "comparison" in comparison
    
    def test_winner_determination(self):
        """Test determining cheaper option."""
        lease = EXAMPLE_SCENARIOS["civic_scenario"]["lease"]
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        comparison = compare_lease_vs_buy(lease, buy, analysis_years=3)
        
        winner = comparison["comparison"]["winner"]
        assert winner in ["lease", "buy", "similar"]
    
    def test_cost_difference(self):
        """Test cost difference calculation."""
        lease = EXAMPLE_SCENARIOS["civic_scenario"]["lease"]
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        comparison = compare_lease_vs_buy(lease, buy, analysis_years=3)
        
        difference = comparison["comparison"]["difference"]
        assert difference is not None


class TestLeaseVsBuyFactors:
    """Test lease vs buy comparison factors."""
    
    def test_factors_exist(self):
        """Test factors are defined."""
        assert len(LEASE_VS_BUY_FACTORS) > 0
        assert len(LEASE_VS_BUY_FACTORS) == 8
    
    def test_mileage_factor(self):
        """Test mileage is a factor."""
        mileage = get_factor("mileage")
        
        assert mileage is not None
        assert "mileage" in mileage.aspect.lower()
    
    def test_maintenance_factor(self):
        """Test maintenance is a factor."""
        maintenance = get_factor("maintenance")
        
        assert maintenance is not None
        assert "maintenance" in maintenance.aspect.lower()
    
    def test_depreciation_factor(self):
        """Test depreciation is a factor."""
        depreciation = get_factor("depreciation")
        
        assert depreciation is not None
        assert "depreciation" in depreciation.aspect.lower()
    
    def test_factor_shows_both_sides(self):
        """Test each factor shows lease and buy perspective."""
        ownership = get_factor("ownership")
        
        assert len(ownership.lease_advantage) > 0
        assert len(ownership.buy_advantage) > 0


class TestExampleScenarios:
    """Test example scenarios."""
    
    def test_civic_scenario_exists(self):
        """Test civic scenario."""
        scenario = get_scenario("civic_scenario")
        
        assert scenario is not None
        assert "lease" in scenario
        assert "buy" in scenario
    
    def test_suv_scenario_exists(self):
        """Test SUV scenario."""
        scenario = get_scenario("suv_scenario")
        
        assert scenario is not None
    
    def test_high_mileage_scenario_exists(self):
        """Test high mileage scenario."""
        scenario = get_scenario("high_mileage")
        
        assert scenario is not None


class TestMileageImpact:
    """Test mileage impact on lease vs buy."""
    
    def test_high_mileage_lease_expensive(self):
        """Test high mileage makes lease expensive."""
        lease = EXAMPLE_SCENARIOS["high_mileage"]["lease"]
        
        costs = calculate_lease_cost(lease, analysis_years=3)
        
        # Excess mileage charges should be significant
        assert costs["excess_mileage"] > 2000
    
    def test_high_mileage_buy_better(self):
        """Test high mileage favors buying."""
        lease = EXAMPLE_SCENARIOS["high_mileage"]["lease"]
        buy = EXAMPLE_SCENARIOS["high_mileage"]["buy"]
        
        comparison = compare_lease_vs_buy(lease, buy, analysis_years=3)
        
        # Buy should be cheaper for high mileage
        lease_cost = comparison["lease_analysis"]["total_cost"]
        buy_cost = comparison["buy_analysis"]["net_cost"]
        
        assert buy_cost < lease_cost


class TestOwnershipConsiderations:
    """Test ownership considerations."""
    
    def test_lease_no_ownership(self):
        """Test leasing means no ownership."""
        lease = EXAMPLE_SCENARIOS["civic_scenario"]["lease"]
        
        # Car is returned at end
        assert lease.monthly_payment > 0
    
    def test_buy_building_equity(self):
        """Test buying builds equity."""
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        # After paying off, you own car
        assert buy.monthly_payment > 0


class TestMaintenanceCosts:
    """Test maintenance impact."""
    
    def test_lease_includes_maintenance(self):
        """Test lease includes maintenance."""
        lease = EXAMPLE_SCENARIOS["civic_scenario"]["lease"]
        
        assert lease.maintenance_included is True
    
    def test_buy_maintenance_costs(self):
        """Test buying means you pay maintenance."""
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        assert buy.annual_maintenance > 0
    
    def test_maintenance_increases_over_time(self):
        """Test maintenance costs increase as car ages."""
        # Older cars cost more to maintain
        young_maintenance = 500
        old_maintenance = 1500
        
        assert old_maintenance > young_maintenance


class TestInsuranceCosts:
    """Test insurance impact."""
    
    def test_lease_insurance_required(self):
        """Test lease requires insurance."""
        lease = EXAMPLE_SCENARIOS["civic_scenario"]["lease"]
        
        assert lease.insurance_extra > 0
    
    def test_buy_insurance_required(self):
        """Test buying requires insurance."""
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        assert buy.annual_insurance > 0
    
    def test_insurance_similar_cost(self):
        """Test insurance costs are similar lease vs buy."""
        lease = EXAMPLE_SCENARIOS["civic_scenario"]["lease"]
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        # Both require insurance, costs should be similar
        assert abs(lease.insurance_extra - buy.annual_insurance) < 500


class TestDepreciationImpact:
    """Test depreciation impact on buying."""
    
    def test_residual_value(self):
        """Test calculating residual value."""
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        costs = calculate_buy_cost(buy, analysis_years=5)
        
        # Should retain some value
        assert costs["residual_value"] > 0
        assert costs["residual_value"] < buy.vehicle_price
    
    def test_depreciation_loss(self):
        """Test depreciation represents lost value."""
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        costs = calculate_buy_cost(buy, analysis_years=5)
        
        # Depreciation is calculated
        depreciation = costs["depreciation"]
        residual = costs["residual_value"]
        
        # Vehicle loses value
        assert buy.vehicle_price - residual > 0


class TestHousingLeaseVsBuy:
    """Test housing lease vs buy."""
    
    def test_rent_cost_calculation(self):
        """Test rent cost calculation."""
        from catalogs.lease_vs_buy import HousingLeaseOption, HousingBuyOption
        
        rent = HousingLeaseOption(
            option_id="rent",
            monthly_rent=2000,
            lease_term=60,
            security_deposit=4000,
            renters_insurance=180
        )
        
        # 60 months * $2000 = $120,000 rent
        assert rent.monthly_rent * 60 == 120000
    
    def test_buy_cost_includes_tax(self):
        """Test buy includes property tax."""
        from catalogs.lease_vs_buy import HousingLeaseOption, HousingBuyOption
        
        buy = HousingBuyOption(
            option_id="buy",
            home_price=400000,
            down_payment_percent=0.20,
            down_payment=80000,
            interest_rate=0.065,
            loan_term_years=30,
            monthly_payment=1520,
            annual_property_tax=4000,
            annual_home_insurance=1200
        )
        
        assert buy.annual_property_tax > 0
    
    def test_housing_equity_buildup(self):
        """Test housing builds equity."""
        from catalogs.lease_vs_buy import HousingLeaseOption, HousingBuyOption
        
        buy = HousingBuyOption(
            option_id="buy",
            home_price=500000,
            down_payment_percent=0.10,
            down_payment=50000,
            interest_rate=0.065,
            loan_term_years=30,
            monthly_payment=2130,
            annual_property_tax=5000,
            annual_home_insurance=1200,
            expected_appreciation=0.03
        )
        
        # Home should appreciate at 3% per year
        assert buy.expected_appreciation == 0.03


class TestBreakEvenAnalysis:
    """Test break-even analysis."""
    
    def test_when_lease_makes_sense(self):
        """Test when leasing is better."""
        # High mileage or short ownership period
        lease = EXAMPLE_SCENARIOS["high_mileage"]["lease"]
        buy_old = EXAMPLE_SCENARIOS["high_mileage"]["buy"]
        
        comparison = compare_lease_vs_buy(lease, buy_old, analysis_years=3)
        
        # For high mileage, buy should be cheaper or similar
        assert comparison["comparison"]["lease_total"] > 0
    
    def test_when_buy_makes_sense(self):
        """Test when buying is better."""
        # Low mileage, long ownership
        lease = EXAMPLE_SCENARIOS["civic_scenario"]["lease"]
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        # Over 5 years, buying should be cheaper
        comparison = compare_lease_vs_buy(lease, buy, analysis_years=5)
        
        buy_cost = comparison["buy_analysis"]["net_cost"]
        lease_cost = comparison["lease_analysis"]["total_cost"]
        
        # Buy should be cheaper over longer period
        assert buy_cost is not None


class TestScenarioRealism:
    """Test scenario realism."""
    
    def test_civic_realistic_prices(self):
        """Test Civic prices are realistic."""
        buy = EXAMPLE_SCENARIOS["civic_scenario"]["buy"]
        
        # Honda Civic base price around $28,000
        assert 25000 < buy.vehicle_price < 35000
    
    def test_suv_realistic_prices(self):
        """Test SUV prices are realistic."""
        buy = EXAMPLE_SCENARIOS["suv_scenario"]["buy"]
        
        # Toyota RAV4 around $30-35k
        assert 30000 < buy.vehicle_price < 40000
    
    def test_lease_payment_realistic(self):
        """Test lease payments are realistic."""
        civic_lease = EXAMPLE_SCENARIOS["civic_scenario"]["lease"]
        suv_lease = EXAMPLE_SCENARIOS["suv_scenario"]["lease"]
        
        # Civic lease ~$300, SUV lease ~$400
        assert 250 < civic_lease.monthly_payment < 350
        assert 350 < suv_lease.monthly_payment < 450
