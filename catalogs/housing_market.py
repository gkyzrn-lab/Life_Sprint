"""
Housing Market Catalog

NYC vs NJ housing options with realistic pricing, commute times,
and buy vs rent trade-offs.
"""

from core_domain.housing.housing_models import HousingOption

# ==============================================================================
# NYC HOUSING OPTIONS
# ==============================================================================

NYC_HOUSING_OPTIONS = {
    # MANHATTAN - Expensive but short commute
    "nyc_manhattan_studio": HousingOption(
        option_id="nyc_manhattan_studio",
        name="Manhattan Studio",
        location="nyc_manhattan",
        housing_type="studio",
        monthly_rent=2800.0,
        purchase_price=650000.0,
        bedrooms=0,
        commute_time_minutes=20,
        neighborhood_quality=85,
        allows_roommates=False,
    ),
    "nyc_manhattan_1br": HousingOption(
        option_id="nyc_manhattan_1br",
        name="Manhattan 1-Bedroom",
        location="nyc_manhattan",
        housing_type="1br",
        monthly_rent=3500.0,
        purchase_price=850000.0,
        bedrooms=1,
        commute_time_minutes=20,
        neighborhood_quality=85,
        allows_roommates=False,
    ),
    "nyc_manhattan_2br": HousingOption(
        option_id="nyc_manhattan_2br",
        name="Manhattan 2-Bedroom (Shareable)",
        location="nyc_manhattan",
        housing_type="2br",
        monthly_rent=5200.0,
        purchase_price=1200000.0,
        bedrooms=2,
        commute_time_minutes=20,
        neighborhood_quality=85,
        allows_roommates=True,
    ),
    
    # BROOKLYN - Moderate pricing, reasonable commute
    "nyc_brooklyn_studio": HousingOption(
        option_id="nyc_brooklyn_studio",
        name="Brooklyn Studio",
        location="nyc_brooklyn",
        housing_type="studio",
        monthly_rent=2100.0,
        purchase_price=475000.0,
        bedrooms=0,
        commute_time_minutes=35,
        neighborhood_quality=75,
        allows_roommates=False,
    ),
    "nyc_brooklyn_1br": HousingOption(
        option_id="nyc_brooklyn_1br",
        name="Brooklyn 1-Bedroom",
        location="nyc_brooklyn",
        housing_type="1br",
        monthly_rent=2600.0,
        purchase_price=600000.0,
        bedrooms=1,
        commute_time_minutes=35,
        neighborhood_quality=75,
        allows_roommates=False,
    ),
    "nyc_brooklyn_2br": HousingOption(
        option_id="nyc_brooklyn_2br",
        name="Brooklyn 2-Bedroom (Shareable)",
        location="nyc_brooklyn",
        housing_type="2br",
        monthly_rent=3800.0,
        purchase_price=800000.0,
        bedrooms=2,
        commute_time_minutes=35,
        neighborhood_quality=75,
        allows_roommates=True,
    ),
    "nyc_brooklyn_3br": HousingOption(
        option_id="nyc_brooklyn_3br",
        name="Brooklyn 3-Bedroom (Shareable)",
        location="nyc_brooklyn",
        housing_type="3br",
        monthly_rent=4800.0,
        purchase_price=950000.0,
        bedrooms=3,
        commute_time_minutes=35,
        neighborhood_quality=75,
        allows_roommates=True,
    ),
    
    # QUEENS - More affordable, longer commute
    "nyc_queens_studio": HousingOption(
        option_id="nyc_queens_studio",
        name="Queens Studio",
        location="nyc_queens",
        housing_type="studio",
        monthly_rent=1700.0,
        purchase_price=380000.0,
        bedrooms=0,
        commute_time_minutes=50,
        neighborhood_quality=65,
        allows_roommates=False,
    ),
    "nyc_queens_1br": HousingOption(
        option_id="nyc_queens_1br",
        name="Queens 1-Bedroom",
        location="nyc_queens",
        housing_type="1br",
        monthly_rent=2100.0,
        purchase_price=480000.0,
        bedrooms=1,
        commute_time_minutes=50,
        neighborhood_quality=65,
        allows_roommates=False,
    ),
    "nyc_queens_2br": HousingOption(
        option_id="nyc_queens_2br",
        name="Queens 2-Bedroom (Shareable)",
        location="nyc_queens",
        housing_type="2br",
        monthly_rent=3000.0,
        purchase_price=620000.0,
        bedrooms=2,
        commute_time_minutes=50,
        neighborhood_quality=65,
        allows_roommates=True,
    ),
}

# ==============================================================================
# NEW JERSEY HOUSING OPTIONS - Cheaper but longer commute
# ==============================================================================

NJ_HOUSING_OPTIONS = {
    # JERSEY CITY - Close to NYC, moderate savings
    "nj_jersey_city_studio": HousingOption(
        option_id="nj_jersey_city_studio",
        name="Jersey City Studio",
        location="nj_jersey_city",
        housing_type="studio",
        monthly_rent=1900.0,
        purchase_price=400000.0,
        bedrooms=0,
        commute_time_minutes=45,
        neighborhood_quality=70,
        allows_roommates=False,
    ),
    "nj_jersey_city_1br": HousingOption(
        option_id="nj_jersey_city_1br",
        name="Jersey City 1-Bedroom",
        location="nj_jersey_city",
        housing_type="1br",
        monthly_rent=2300.0,
        purchase_price=520000.0,
        bedrooms=1,
        commute_time_minutes=45,
        neighborhood_quality=70,
        allows_roommates=False,
    ),
    "nj_jersey_city_2br": HousingOption(
        option_id="nj_jersey_city_2br",
        name="Jersey City 2-Bedroom (Shareable)",
        location="nj_jersey_city",
        housing_type="2br",
        monthly_rent=3200.0,
        purchase_price=680000.0,
        bedrooms=2,
        commute_time_minutes=45,
        neighborhood_quality=70,
        allows_roommates=True,
    ),
    
    # HOBOKEN - Similar to Jersey City
    "nj_hoboken_studio": HousingOption(
        option_id="nj_hoboken_studio",
        name="Hoboken Studio",
        location="nj_hoboken",
        housing_type="studio",
        monthly_rent=2000.0,
        purchase_price=420000.0,
        bedrooms=0,
        commute_time_minutes=40,
        neighborhood_quality=72,
        allows_roommates=False,
    ),
    "nj_hoboken_1br": HousingOption(
        option_id="nj_hoboken_1br",
        name="Hoboken 1-Bedroom",
        location="nj_hoboken",
        housing_type="1br",
        monthly_rent=2400.0,
        purchase_price=540000.0,
        bedrooms=1,
        commute_time_minutes=40,
        neighborhood_quality=72,
        allows_roommates=False,
    ),
    "nj_hoboken_2br": HousingOption(
        option_id="nj_hoboken_2br",
        name="Hoboken 2-Bedroom (Shareable)",
        location="nj_hoboken",
        housing_type="2br",
        monthly_rent=3400.0,
        purchase_price=700000.0,
        bedrooms=2,
        commute_time_minutes=40,
        neighborhood_quality=72,
        allows_roommates=True,
    ),
    
    # NEWARK - Most affordable, longest commute
    "nj_newark_studio": HousingOption(
        option_id="nj_newark_studio",
        name="Newark Studio",
        location="nj_newark",
        housing_type="studio",
        monthly_rent=1400.0,
        purchase_price=280000.0,
        bedrooms=0,
        commute_time_minutes=60,
        neighborhood_quality=55,
        allows_roommates=False,
    ),
    "nj_newark_1br": HousingOption(
        option_id="nj_newark_1br",
        name="Newark 1-Bedroom",
        location="nj_newark",
        housing_type="1br",
        monthly_rent=1700.0,
        purchase_price=340000.0,
        bedrooms=1,
        commute_time_minutes=60,
        neighborhood_quality=55,
        allows_roommates=False,
    ),
    "nj_newark_2br": HousingOption(
        option_id="nj_newark_2br",
        name="Newark 2-Bedroom (Shareable)",
        location="nj_newark",
        housing_type="2br",
        monthly_rent=2300.0,
        purchase_price=450000.0,
        bedrooms=2,
        commute_time_minutes=60,
        neighborhood_quality=55,
        allows_roommates=True,
    ),
    "nj_newark_3br": HousingOption(
        option_id="nj_newark_3br",
        name="Newark 3-Bedroom (Shareable)",
        location="nj_newark",
        housing_type="3br",
        monthly_rent=2900.0,
        purchase_price=550000.0,
        bedrooms=3,
        commute_time_minutes=60,
        neighborhood_quality=55,
        allows_roommates=True,
    ),
}

# Combine all options
ALL_HOUSING_OPTIONS = {**NYC_HOUSING_OPTIONS, **NJ_HOUSING_OPTIONS}

# ==============================================================================
# ROOMMATE CONFIGURATIONS
# ==============================================================================

ROOMMATE_CONFIGS = {
    "alone": {
        "num_roommates": 0,
        "rent_split_percent": 1.0,
        "privacy_level": 100,
        "description": "Living alone - full privacy, full cost",
    },
    "one_roommate": {
        "num_roommates": 1,
        "rent_split_percent": 0.5,
        "privacy_level": 70,
        "description": "One roommate - shared costs, moderate privacy",
    },
    "two_roommates": {
        "num_roommates": 2,
        "rent_split_percent": 0.33,
        "privacy_level": 50,
        "description": "Two roommates - lowest costs, minimal privacy",
    },
}

# ==============================================================================
# MORTGAGE PRODUCTS
# ==============================================================================

MORTGAGE_PRODUCTS = {
    "conventional_30": {
        "name": "30-Year Fixed Conventional",
        "term_years": 30,
        "min_down_payment_percent": 0.20,  # 20% down to avoid PMI
        "interest_rate": 0.065,  # 6.5% (2026 realistic rate)
        "closing_costs_percent": 0.03,  # 3% of purchase price
    },
    "conventional_15": {
        "name": "15-Year Fixed Conventional",
        "term_years": 15,
        "min_down_payment_percent": 0.20,
        "interest_rate": 0.055,  # 5.5% (lower for 15-year)
        "closing_costs_percent": 0.03,
    },
    "fha_loan": {
        "name": "FHA Loan (First-Time Buyer)",
        "term_years": 30,
        "min_down_payment_percent": 0.035,  # 3.5% down (FHA allows low down payment)
        "interest_rate": 0.07,  # 7.0% (slightly higher rate)
        "closing_costs_percent": 0.035,
        "requires_pmi": True,  # Private mortgage insurance
        "pmi_monthly_percent": 0.005,  # 0.5% of loan amount annually
    },
}

# ==============================================================================
# PROPERTY OWNERSHIP COSTS (Monthly averages)
# ==============================================================================

OWNERSHIP_COSTS = {
    "property_tax_rate": 0.0125,  # 1.25% of home value annually (NYC average)
    "home_insurance_rate": 0.004,  # 0.4% of home value annually
    "maintenance_rate": 0.01,  # 1% of home value annually (rule of thumb)
    "hoa_fees": {
        "nyc_manhattan": 800,  # High HOA in Manhattan condos
        "nyc_brooklyn": 400,
        "nyc_queens": 200,
        "nj_jersey_city": 300,
        "nj_hoboken": 300,
        "nj_newark": 150,
    },
}

# ==============================================================================
# RENT INFLATION MECHANICS
# ==============================================================================

RENT_INFLATION = {
    "base_annual_rate": 0.05,  # 5% annual rent increase after graduation
    "market_modifiers": {
        "cold": -0.02,  # Recession: 3% increases
        "normal": 0.0,  # Normal: 5% increases
        "hot": 0.03,  # Hot market: 8% increases
    },
    "nyc_premium": 0.01,  # NYC rents increase 1% faster than NJ
}

# ==============================================================================
# COMMUTE COSTS
# ==============================================================================

COMMUTE_COSTS = {
    "time_cost_per_hour": 25.0,  # Value of time ($/hour) for trade-off calculations
    "transit_cost_per_minute": 0.15,  # Monthly transit costs per minute of commute
    "stress_per_hour_commute": 5,  # Mental health impact per hour of daily commuting
}

# ==============================================================================
# ACHIEVEMENTS
# ==============================================================================

HOUSING_ACHIEVEMENTS = [
    {
        "achievement_id": "first_apartment",
        "name": "First Real Apartment 🏠",
        "description": "Signed your first post-graduation lease",
        "tier": "bronze",
        "trigger": "Move into first post-college apartment",
    },
    {
        "achievement_id": "roommate_savings",
        "name": "Smart Saver 💡",
        "description": "Saved $500+/month by living with roommates",
        "tier": "bronze",
        "trigger": "Live with roommates for 6 months",
    },
    {
        "achievement_id": "commute_warrior",
        "name": "Commute Warrior ⏰",
        "description": "Endured 60+ minute daily commute for 1 year",
        "tier": "bronze",
        "trigger": "Long commute for 12 months",
    },
    {
        "achievement_id": "down_payment_saved",
        "name": "Down Payment Ready 💰",
        "description": "Saved enough for a 20% down payment",
        "tier": "silver",
        "trigger": "Save down payment goal",
    },
    {
        "achievement_id": "first_home_purchase",
        "name": "Homeowner 🏡",
        "description": "Purchased your first property",
        "tier": "gold",
        "trigger": "Buy first home",
    },
    {
        "achievement_id": "mortgage_paid_off",
        "name": "Mortgage-Free! 🎉",
        "description": "Paid off your mortgage completely",
        "tier": "platinum",
        "trigger": "Pay off full mortgage",
    },
    {
        "achievement_id": "rent_regret",
        "name": "Rent Regret 💸",
        "description": "Paid $100k+ in rent with nothing to show for it",
        "tier": "bronze",
        "trigger": "Total rent exceeds $100k",
    },
]

# ==============================================================================
# STORIES
# ==============================================================================

HOUSING_STORIES = [
    {
        "story_id": "first_apartment_shock",
        "title": "Sticker Shock 😱",
        "message": "You tour your first post-grad apartment. The rent is ${rent:,}/month. That's more than your entire college semester budget. Welcome to adult housing costs.",
        "tone": "shock",
        "trigger": "View first expensive apartment",
    },
    {
        "story_id": "roommate_added",
        "title": "Roommate Deal 🤝",
        "message": "You found a roommate! Your rent drops from ${old_rent:,} to ${new_rent:,}/month. You're saving ${savings:,}/month, but you can hear them watching TV through the wall at 2 AM.",
        "tone": "informative",
        "trigger": "Add first roommate",
    },
    {
        "story_id": "roommate_conflict",
        "title": "Roommate Drama 😤",
        "message": "Your roommate ate your food again. And didn't pay utilities on time. And their friends are always over. The savings are nice, but is it worth it?",
        "tone": "cautionary",
        "trigger": "High conflict level",
    },
    {
        "story_id": "long_commute_reality",
        "title": "Commute Hell 🚇",
        "message": "You're spending {hours:.1f} hours PER DAY commuting. That's {hours_per_week:.0f} hours a week. Over a year, that's {days_per_year:.0f} full days on the train. You save ${savings:,}/month on rent, but at what cost?",
        "tone": "cautionary",
        "trigger": "Long commute for 3 months",
    },
    {
        "story_id": "rent_increase",
        "title": "Rent Going Up 📈",
        "message": "Your landlord just raised your rent by {percent:.0f}%. Your new rent is ${new_rent:,}/month. This is why people buy houses.",
        "tone": "cautionary",
        "trigger": "Annual rent increase",
    },
    {
        "story_id": "rent_regret",
        "title": "Money Down the Drain 💸",
        "message": "You've now paid ${total_rent:,} in rent over {years} years. That could have been a down payment. Or equity. Instead, it's just... gone.",
        "tone": "cautionary",
        "trigger": "Cross $50k total rent paid",
    },
    {
        "story_id": "buy_vs_rent_analysis",
        "title": "The Math 🧮",
        "message": "If you buy: ${buy_monthly:,}/month → builds ${equity:,} equity in {years} years. If you rent: ${rent_monthly:,}/month → $0 equity. But buying needs ${down_payment:,} down payment. Choose wisely.",
        "tone": "informative",
        "trigger": "Run buy vs rent calculator",
    },
    {
        "story_id": "down_payment_progress",
        "title": "Down Payment Progress 💪",
        "message": "You've saved ${saved:,} toward your ${goal:,} down payment goal. That's {percent:.0f}% of the way there. Keep going!",
        "tone": "triumphant",
        "trigger": "Hit 50% of down payment goal",
    },
    {
        "story_id": "home_purchase",
        "title": "Homeowner! 🏡",
        "message": "You just bought a ${price:,} home with a ${down_payment:,} down payment. Your mortgage is ${monthly_payment:,}/month. It's yours. Well, the bank's for the next {years} years. But still!",
        "tone": "triumphant",
        "trigger": "Purchase first home",
    },
    {
        "story_id": "mortgage_reality",
        "title": "Mortgage Reality Check 💰",
        "message": "Your ${mortgage_payment:,}/month mortgage payment is actually: ${principal:,} principal + ${interest:,} interest + ${tax:,} property tax + ${insurance:,} insurance + ${hoa:,} HOA. Total: ${total:,}/month. Homeownership is expensive.",
        "tone": "informative",
        "trigger": "First month of homeownership",
    },
    {
        "story_id": "property_appreciation",
        "title": "Home Value Up! 📈",
        "message": "Your home has appreciated from ${purchase:,} to ${current:,}. You've gained ${gain:,} in equity just from market growth. This is why people say 'real estate is an investment.'",
        "tone": "triumphant",
        "trigger": "Significant appreciation",
    },
]
