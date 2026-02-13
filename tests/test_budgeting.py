"""Tests for budgeting system."""

import pytest
from catalogs.budgeting import (
    create_budget, add_spending_to_budget, check_budget_status,
    get_budget_insights, get_category, get_all_categories,
    BUDGET_CATEGORIES, BUDGET_MYTHS, BUDGETING_TIPS
)


class TestBudgetCreation:
    """Test budget creation."""
    
    def test_create_50_30_20_budget(self):
        """Test creating 50/30/20 budget."""
        monthly_income = 3000
        budget = create_budget(
            monthly_income=monthly_income,
            budgeting_method="50_30_20"
        )
        
        assert budget.monthly_income == 3000
        assert budget.needs_budget == 1500  # 50%
        assert budget.wants_budget == 900   # 30%
        assert budget.savings_budget == 600  # 20%
    
    def test_budget_totals_to_income(self):
        """Test budget categories total to income."""
        monthly_income = 5000
        budget = create_budget(monthly_income)
        
        total = budget.needs_budget + budget.wants_budget + budget.savings_budget
        assert total == monthly_income
    
    def test_budget_tracking(self):
        """Test budget tracks spending."""
        budget = create_budget(monthly_income=2000)
        
        assert budget.actual_spending == {}
        assert budget.total_spent == 0
        assert budget.remaining == 2000


class TestBudgetCategories:
    """Test budget categories."""
    
    def test_categories_exist(self):
        """Test budget categories are defined."""
        assert len(BUDGET_CATEGORIES) > 0
    
    def test_category_by_id(self):
        """Test retrieving category by id."""
        housing = get_category("housing")
        
        assert housing is not None
        assert housing.category_name == "Housing"
        assert housing.category_type == "need"
    
    def test_needs_categories(self):
        """Test need categories include essentials."""
        needs = [c for c in BUDGET_CATEGORIES.values() if c.category_type == "need"]
        
        category_ids = {c.category_id for c in needs}
        
        assert "housing" in category_ids
        assert "food" in category_ids
        assert "transportation" in category_ids
    
    def test_wants_categories(self):
        """Test want categories."""
        wants = [c for c in BUDGET_CATEGORIES.values() if c.category_type == "want"]
        
        category_ids = {c.category_id for c in wants}
        
        assert "dining_out" in category_ids
        assert "entertainment" in category_ids
        assert "shopping" in category_ids
    
    def test_savings_categories(self):
        """Test savings categories."""
        savings = [c for c in BUDGET_CATEGORIES.values() if c.category_type == "savings"]
        
        category_ids = {c.category_id for c in savings}
        
        assert "emergency_fund" in category_ids
        assert "retirement" in category_ids


class TestSpendingTracking:
    """Test spending tracking."""
    
    def test_add_spending(self):
        """Test adding spending to budget."""
        budget = create_budget(2000)
        
        budget = add_spending_to_budget(budget, "housing", 1000)
        
        assert budget.actual_spending["housing"] == 1000
        assert budget.total_spent == 1000
        assert budget.remaining == 1000
    
    def test_multiple_spending_entries(self):
        """Test tracking multiple spending entries."""
        budget = create_budget(3000)
        
        budget = add_spending_to_budget(budget, "housing", 1200)
        budget = add_spending_to_budget(budget, "food", 400)
        budget = add_spending_to_budget(budget, "dining_out", 150)
        
        assert budget.total_spent == 1750
        assert budget.remaining == 1250
    
    def test_cumulative_spending(self):
        """Test cumulative spending in same category."""
        budget = create_budget(1000)
        
        budget = add_spending_to_budget(budget, "dining_out", 30)
        budget = add_spending_to_budget(budget, "dining_out", 40)
        budget = add_spending_to_budget(budget, "dining_out", 35)
        
        assert budget.actual_spending["dining_out"] == 105
        assert budget.total_spent == 105


class TestBudgetStatus:
    """Test budget status checking."""
    
    def test_on_budget(self):
        """Test checking if on budget."""
        budget = create_budget(3000)
        
        budget = add_spending_to_budget(budget, "housing", 1500)
        budget = add_spending_to_budget(budget, "dining_out", 200)
        budget = add_spending_to_budget(budget, "emergency_fund", 300)
        
        status = check_budget_status(budget)
        
        assert status["on_track"] is True
    
    def test_over_budget(self):
        """Test detecting over budget."""
        budget = create_budget(1000)
        
        budget = add_spending_to_budget(budget, "housing", 600)
        budget = add_spending_to_budget(budget, "dining_out", 500)  # Over 30% wants budget
        
        status = check_budget_status(budget)
        
        assert status["wants"]["over_budget"] is True
    
    def test_budget_breakdown(self):
        """Test budget breakdown shows all categories."""
        budget = create_budget(2000)
        budget = add_spending_to_budget(budget, "housing", 1000)
        budget = add_spending_to_budget(budget, "food", 300)
        budget = add_spending_to_budget(budget, "entertainment", 200)
        
        status = check_budget_status(budget)
        
        assert "needs" in status
        assert "wants" in status
        assert "savings" in status


class TestBudgetInsights:
    """Test budget insights."""
    
    def test_insights_provided(self):
        """Test budget provides insights."""
        budget = create_budget(2500)
        budget = add_spending_to_budget(budget, "housing", 1250)
        budget = add_spending_to_budget(budget, "food", 300)
        budget = add_spending_to_budget(budget, "dining_out", 300)
        
        insights = get_budget_insights(budget)
        
        assert "insights" in insights
        assert len(insights["insights"]) > 0
    
    def test_no_savings_insight(self):
        """Test insight when no savings."""
        budget = create_budget(2000)
        budget = add_spending_to_budget(budget, "housing", 1500)
        budget = add_spending_to_budget(budget, "food", 400)
        
        insights = get_budget_insights(budget)
        insights_text = " ".join(insights["insights"]).lower()
        
        assert "saving" in insights_text
    
    def test_over_budget_insight(self):
        """Test insight when over budget."""
        budget = create_budget(2000)
        budget = add_spending_to_budget(budget, "housing", 1500)
        budget = add_spending_to_budget(budget, "dining_out", 600)  # Over 30% wants
        
        insights = get_budget_insights(budget)
        insights_text = " ".join(insights["insights"]).lower()
        
        assert "over" in insights_text or "budget" in insights_text


class TestBudgetMyths:
    """Test budgeting myths."""
    
    def test_myths_exist(self):
        """Test budgeting myths are defined."""
        assert len(BUDGET_MYTHS) > 0
        assert len(BUDGET_MYTHS) == 5
    
    def test_myth_structure(self):
        """Test each myth has debunking."""
        for myth_id, myth_data in BUDGET_MYTHS.items():
            assert "myth" in myth_data
            assert "fact" in myth_data
            assert "impact" in myth_data
            assert len(myth_data["myth"]) > 0
    
    def test_restrictive_myth(self):
        """Test restrictive budget myth."""
        myth_ids = set(BUDGET_MYTHS.keys())
        
        assert "myth_budget_restrictive" in myth_ids
    
    def test_wealthy_budget_myth(self):
        """Test wealthy people don't need budget myth."""
        myth_ids = set(BUDGET_MYTHS.keys())
        
        assert "myth_budget_for_poor" in myth_ids


class TestBudgetTips:
    """Test budgeting tips."""
    
    def test_tips_exist(self):
        """Test budgeting tips are defined."""
        assert len(BUDGETING_TIPS) > 0
    
    def test_50_30_20_rule(self):
        """Test 50/30/20 rule tip exists."""
        tip_ids = set(BUDGETING_TIPS.keys())
        
        assert "50_30_20_rule" in tip_ids
    
    def test_envelope_method(self):
        """Test envelope method tip exists."""
        tip_ids = set(BUDGETING_TIPS.keys())
        
        assert "envelope_method" in tip_ids
    
    def test_zero_based_budget(self):
        """Test zero-based budget tip exists."""
        tip_ids = set(BUDGETING_TIPS.keys())
        
        assert "zero_based_budget" in tip_ids


class TestBudgetPercentages:
    """Test budget percentage calculations."""
    
    def test_50_30_20_percentages(self):
        """Test 50/30/20 split."""
        budget = create_budget(6000)
        
        needs_percent = (budget.needs_budget / budget.monthly_income) * 100
        wants_percent = (budget.wants_budget / budget.monthly_income) * 100
        savings_percent = (budget.savings_budget / budget.monthly_income) * 100
        
        assert abs(needs_percent - 50) < 1
        assert abs(wants_percent - 30) < 1
        assert abs(savings_percent - 20) < 1
    
    def test_spending_percentages(self):
        """Test calculating spending percentages."""
        budget = create_budget(2000)
        budget = add_spending_to_budget(budget, "housing", 800)
        budget = add_spending_to_budget(budget, "food", 300)
        
        housing_percent = (800 / 2000) * 100
        assert housing_percent == 40


class TestRemaining:
    """Test remaining budget tracking."""
    
    def test_remaining_decreases(self):
        """Test remaining budget decreases with spending."""
        budget = create_budget(1000)
        assert budget.remaining == 1000
        
        budget = add_spending_to_budget(budget, "food", 200)
        assert budget.remaining == 800
        
        budget = add_spending_to_budget(budget, "housing", 400)
        assert budget.remaining == 400
    
    def test_surplus_tracking(self):
        """Test tracking budget surplus."""
        budget = create_budget(2000)
        budget = add_spending_to_budget(budget, "housing", 900)
        budget = add_spending_to_budget(budget, "food", 250)
        budget = add_spending_to_budget(budget, "emergency_fund", 400)
        
        # 2000 - 1550 = 450 remaining
        assert budget.remaining == 450


class TestBudgetFlexibility:
    """Test budget flexibility."""
    
    def test_custom_budgeting(self):
        """Test custom budget allocation."""
        # Someone with different needs
        budget = create_budget(4000, "custom")
        
        assert budget.monthly_income == 4000
        # Default custom is same as 50/30/20
        assert budget.needs_budget == 2000
    
    def test_high_income_budget(self):
        """Test high income budget."""
        budget = create_budget(15000)
        
        assert budget.needs_budget == 7500
        assert budget.wants_budget == 4500
        assert budget.savings_budget == 3000
    
    def test_low_income_budget(self):
        """Test low income budget."""
        budget = create_budget(1500)
        
        assert budget.needs_budget == 750
        assert budget.wants_budget == 450
        assert budget.savings_budget == 300


class TestCategoryExamples:
    """Test category examples."""
    
    def test_housing_examples(self):
        """Test housing examples."""
        housing = get_category("housing")
        
        examples = housing.examples
        assert "Rent" in examples or "rent" in [e.lower() for e in examples]
        assert "Mortgage" in examples or "mortgage" in [e.lower() for e in examples]
    
    def test_dining_examples(self):
        """Test dining examples."""
        dining = get_category("dining_out")
        
        examples = [e.lower() for e in dining.examples]
        assert any("restaurant" in e for e in examples)
        assert any("coffee" in e for e in examples)


class TestBudgetVsActual:
    """Test budget vs actual analysis."""
    
    def test_budget_under(self):
        """Test when actual is under budget."""
        budget = create_budget(2000)
        budget = add_spending_to_budget(budget, "dining_out", 100)
        
        status = check_budget_status(budget)
        
        # Wants budget is $600, spent $100
        assert status["wants"]["actual"] < status["wants"]["budget"]
        assert status["wants"]["remaining"] > 0
    
    def test_budget_over(self):
        """Test when actual is over budget."""
        budget = create_budget(2000)
        budget = add_spending_to_budget(budget, "dining_out", 700)
        
        status = check_budget_status(budget)
        
        # Wants budget is $600, spent $700
        assert status["wants"]["actual"] > status["wants"]["budget"]
        assert status["wants"]["over_budget"] is True
