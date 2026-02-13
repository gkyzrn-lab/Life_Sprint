"""Tests for insurance education system."""

import pytest
from catalogs.insurance_basics import (
    get_insurance_type, get_all_insurance_types, get_insurance_by_category,
    get_scenario, get_all_scenarios, get_term, get_all_terms,
    get_myth, get_all_myths, get_tip, get_all_tips,
    INSURANCE_TYPES, INSURANCE_SCENARIOS, INSURANCE_TERMS, INSURANCE_MYTHS
)


class TestInsuranceTypes:
    """Test insurance type definitions."""
    
    def test_types_exist(self):
        """Test insurance types are defined."""
        assert len(INSURANCE_TYPES) > 0
    
    def test_health_insurance_exists(self):
        """Test health insurance is defined."""
        health = get_insurance_type("health_insurance")
        
        assert health is not None
        assert health.type_name == "Health Insurance"
        assert health.category == "health"
    
    def test_auto_insurance_exists(self):
        """Test auto insurance types exist."""
        liability = get_insurance_type("auto_liability")
        collision = get_insurance_type("auto_collision")
        comprehensive = get_insurance_type("auto_comprehensive")
        
        assert liability is not None
        assert collision is not None
        assert comprehensive is not None
    
    def test_life_insurance_exists(self):
        """Test life insurance types exist."""
        term = get_insurance_type("term_life")
        whole = get_insurance_type("whole_life")
        
        assert term is not None
        assert whole is not None
    
    def test_insurance_structure(self):
        """Test insurance type has required fields."""
        insurance = get_insurance_type("health_insurance")
        
        assert insurance.type_id == "health_insurance"
        assert len(insurance.description) > 0
        assert len(insurance.why_needed) > 0
        assert len(insurance.what_it_covers) > 0


class TestInsuranceCategories:
    """Test insurance by category."""
    
    def test_health_category(self):
        """Test health insurance category."""
        health_types = get_insurance_by_category("health")
        
        assert len(health_types) > 0
        assert health_types[0].type_id == "health_insurance"
    
    def test_property_category(self):
        """Test property insurance category."""
        property_types = get_insurance_by_category("property")
        
        assert len(property_types) > 0
        
        type_ids = {t.type_id for t in property_types}
        assert "auto_collision" in type_ids
        assert "renters_insurance" in type_ids
    
    def test_liability_category(self):
        """Test liability insurance category."""
        liability_types = get_insurance_by_category("liability")
        
        assert len(liability_types) > 0
        assert any(t.type_id == "auto_liability" for t in liability_types)


class TestInsuranceScenarios:
    """Test insurance scenarios."""
    
    def test_scenarios_exist(self):
        """Test insurance scenarios are defined."""
        assert len(INSURANCE_SCENARIOS) > 0
        assert len(INSURANCE_SCENARIOS) == 5
    
    def test_car_accident_scenario(self):
        """Test car accident scenario."""
        scenario = get_scenario("scenario_car_accident")
        
        assert scenario is not None
        assert scenario.cost_without_insurance > 100000
    
    def test_apartment_fire_scenario(self):
        """Test apartment fire scenario."""
        scenario = get_scenario("scenario_apartment_fire")
        
        assert scenario is not None
        assert scenario.cost_without_insurance > 5000
    
    def test_scenario_structure(self):
        """Test scenario has required fields."""
        scenario = get_scenario("scenario_car_accident")
        
        assert len(scenario.event_description) > 0
        assert scenario.cost_without_insurance > 0
        assert len(scenario.no_insurance_outcome) > 0
        assert len(scenario.with_insurance_outcome) > 0
        assert scenario.savings_with_insurance > 0
    
    def test_insurance_saves_money(self):
        """Test all scenarios show insurance savings."""
        for scenario in get_all_scenarios():
            scenario_data = get_scenario(scenario)
            assert scenario_data.savings_with_insurance > 0


class TestInsuranceTerms:
    """Test insurance terminology."""
    
    def test_terms_exist(self):
        """Test insurance terms are defined."""
        assert len(INSURANCE_TERMS) > 0
        assert len(INSURANCE_TERMS) == 9
    
    def test_deductible_term(self):
        """Test deductible definition."""
        term = get_term("deductible")
        
        assert term is not None
        assert term.term == "Deductible"
        assert len(term.definition) > 0
    
    def test_premium_term(self):
        """Test premium definition."""
        term = get_term("premium")
        
        assert term is not None
        assert "monthly" in term.definition.lower() or "annual" in term.definition.lower()
    
    def test_coverage_limit_term(self):
        """Test coverage limit definition."""
        term = get_term("coverage_limit")
        
        assert term is not None
        assert "maximum" in term.definition.lower()
    
    def test_term_has_example(self):
        """Test each term has example."""
        for term_id, term_data in INSURANCE_TERMS.items():
            assert len(term_data.example) > 0


class TestInsuranceMyths:
    """Test insurance myths."""
    
    def test_myths_exist(self):
        """Test insurance myths are defined."""
        assert len(INSURANCE_MYTHS) > 0
        assert len(INSURANCE_MYTHS) == 6
    
    def test_young_no_insurance_myth(self):
        """Test young people don't need insurance myth."""
        myth = get_myth("myth_young_no_insurance")
        
        assert myth is not None
        assert "FALSE" in myth.fact or "false" in myth.fact.lower()
    
    def test_myth_structure(self):
        """Test myth has required fields."""
        myth = get_myth("myth_young_no_insurance")
        
        assert len(myth.myth) > 0
        assert len(myth.fact) > 0
        assert myth.financial_impact > 0
    
    def test_myths_debunk_common_beliefs(self):
        """Test myths debunk common wrong beliefs."""
        myth_ids = set(INSURANCE_MYTHS.keys())
        
        # Should include key myths
        assert "myth_young_no_insurance" in myth_ids
        assert "myth_renters_landlord" in myth_ids


class TestInsuranceTips:
    """Test insurance tips."""
    
    def test_tips_exist(self):
        """Test insurance tips are provided."""
        tips = get_all_tips()
        
        assert len(tips) > 0
    
    def test_health_tips(self):
        """Test health insurance tips."""
        tip = get_tip("health_preventive")
        
        assert tip is not None
        assert "preventive" in tip.lower() or "free" in tip.lower()
    
    def test_auto_tips(self):
        """Test auto insurance tips."""
        tip = get_tip("auto_discount")
        
        assert tip is not None
        assert "discount" in tip.lower()
    
    def test_life_insurance_tips(self):
        """Test life insurance tips."""
        tip = get_tip("life_term_young")
        
        assert tip is not None
        assert "young" in tip.lower() or "age" in tip.lower()


class TestHealthInsuranceCoverage:
    """Test health insurance coverage."""
    
    def test_preventive_covered(self):
        """Test preventive care is covered."""
        health = get_insurance_type("health_insurance")
        
        covered = [c.lower() for c in health.what_it_covers]
        assert any("preventive" in c for c in covered)
    
    def test_emergency_covered(self):
        """Test emergency room is covered."""
        health = get_insurance_type("health_insurance")
        
        covered = [c.lower() for c in health.what_it_covers]
        assert any("emergency" in c for c in covered)


class TestAutoInsuranceCoverage:
    """Test auto insurance coverage."""
    
    def test_liability_required(self):
        """Test liability is legally required."""
        liability = get_insurance_type("auto_liability")
        
        assert "legally" in liability.why_needed.lower() or "required" in liability.why_needed.lower()
    
    def test_collision_covers_accidents(self):
        """Test collision covers accident damage."""
        collision = get_insurance_type("auto_collision")
        
        covered = [c.lower() for c in collision.what_it_covers]
        assert any("accident" in c for c in covered)
    
    def test_comprehensive_covers_theft(self):
        """Test comprehensive covers theft."""
        comprehensive = get_insurance_type("auto_comprehensive")
        
        covered = [c.lower() for c in comprehensive.what_it_covers]
        assert any("theft" in c for c in covered)


class TestRentersInsurance:
    """Test renters insurance."""
    
    def test_covers_belongings(self):
        """Test renters covers belongings."""
        renters = get_insurance_type("renters_insurance")
        
        assert "belongings" in renters.why_needed.lower()
    
    def test_landlord_responsible_for_building(self):
        """Test clarification on landlord responsibility."""
        renters = get_insurance_type("renters_insurance")
        
        not_covered = [c.lower() for c in renters.what_it_doesnt_cover]
        assert any("building" in c for c in not_covered)


class TestLifeInsurance:
    """Test life insurance."""
    
    def test_term_is_affordable(self):
        """Test term life is affordable."""
        term = get_insurance_type("term_life")
        
        assert "affordable" in term.why_needed.lower() or "cheap" in term.why_needed.lower()
    
    def test_whole_is_expensive(self):
        """Test whole life is more expensive."""
        whole = get_insurance_type("whole_life")
        
        assert "expensive" in whole.why_needed.lower() or "higher" in whole.why_needed.lower()
    
    def test_life_has_death_benefit(self):
        """Test life insurance provides death benefit."""
        term = get_insurance_type("term_life")
        
        covered = [c.lower() for c in term.what_it_covers]
        assert any("death benefit" in c or "benefit" in c for c in covered)


class TestDisabilityInsurance:
    """Test disability insurance."""
    
    def test_short_term_exists(self):
        """Test short-term disability exists."""
        short_term = get_insurance_type("short_term_disability")
        
        assert short_term is not None
    
    def test_long_term_exists(self):
        """Test long-term disability exists."""
        long_term = get_insurance_type("long_term_disability")
        
        assert long_term is not None
    
    def test_replaces_income(self):
        """Test disability replaces income."""
        short_term = get_insurance_type("short_term_disability")
        
        assert "income" in short_term.what_it_covers[0].lower()


class TestScenarioFinancialImpact:
    """Test scenario financial impacts."""
    
    def test_car_accident_expensive(self):
        """Test car accident is expensive without insurance."""
        scenario = get_scenario("scenario_car_accident")
        
        # Lawsuits and injuries are expensive
        assert scenario.cost_without_insurance > 200000
    
    def test_apartment_fire_savings(self):
        """Test apartment fire shows insurance savings."""
        scenario = get_scenario("scenario_apartment_fire")
        
        # Insurance saves thousands
        assert scenario.savings_with_insurance > 5000
    
    def test_medical_bankruptcy_level(self):
        """Test medical costs are bankruptcy-level."""
        scenario = get_scenario("scenario_heart_attack")
        
        # Hospital stay is expensive
        assert scenario.cost_without_insurance > 50000


class TestMythsDebunked:
    """Test myths are properly debunked."""
    
    def test_myth_vs_fact_contradictory(self):
        """Test myth and fact contradict each other."""
        myth = get_myth("myth_young_no_insurance")
        
        # Myth says one thing, fact says opposite
        assert myth.myth != myth.fact
    
    def test_financial_impact_quantified(self):
        """Test myths include financial impact."""
        for myth_id, myth_data in INSURANCE_MYTHS.items():
            assert myth_data.financial_impact > 0


class TestInsuranceTipActionability:
    """Test tips are actionable."""
    
    def test_tips_have_specific_actions(self):
        """Test tips suggest specific actions."""
        bundling_tip = get_tip("auto_bundling")
        
        # Should mention specific action
        assert "compare" in bundling_tip.lower() or "bundle" in bundling_tip.lower()
    
    def test_discount_tips(self):
        """Test discount tips are specific."""
        discount_tip = get_tip("auto_discount")
        
        # Should mention specific discounts
        assert "driver" in discount_tip.lower() or "discount" in discount_tip.lower()
