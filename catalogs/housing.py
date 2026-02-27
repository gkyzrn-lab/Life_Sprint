from core_domain.player.player_model import Housing
from typing import Dict, List

# Enhanced housing options with multiple choices per category
# Includes lease requirements, commute times, and stress levels
HOUSING_CATALOG = {
    "dorm": {
        "category": "Dorm",
        "description": "On-campus housing with flexible terms",
        "min_lease_semesters": 1,
        "penalty_fee": 0.0,
        "options": [
            {
                "id": "dorm_standard",
                "name": "Standard Dorm",
                "monthly_cost": 900.0,
                "upfront_cost": 0.0,
                "commute_minutes": 5,
                "stress_level": "Low",  # Very convenient, nearby classes
                "gpa_modifier": 0.02,
                "social_modifier": 0.15,
                "benefits": [
                    "💰 Moderate cost ($900/month)",
                    "😊 Low stress - walking distance",
                    "👥 Built-in social community",
                    "⚡ No commute time",
                    "✅ No lease commitment"
                ],
                "cons": [
                    "🚪 Limited personal space",
                    "🔊 Noise from roommates",
                    "🚿 Shared bathroom facilities",
                    "📦 Limited storage space",
                    "👀 Minimal privacy"
                ]
            }
        ]
    },
    "family": {
        "category": "Family",
        "description": "Living with family members",
        "min_lease_semesters": 1,
        "penalty_fee": 0.0,
        "options": [
            {
                "id": "family_stay",
                "name": "Live with Family",
                "monthly_cost": 0.0,
                "upfront_cost": 0.0,
                "commute_minutes": 45,
                "stress_level": "Medium",
                "gpa_modifier": 0.0,
                "social_modifier": -0.05,
                "benefits": [
                    "💰 FREE - saves $10,000+/year",
                    "👨‍👩‍👧‍👦 Family emotional support",
                    "🍽️ Home-cooked meals",
                    "✅ No lease or financial risk",
                    "🛡️ Financial safety net"
                ],
                "cons": [
                    "😓 High stress from 45min commute",
                    "⏰ 1.5 hours daily travel time",
                    "👥 Limited social independence",
                    "🚫 Harder to attend campus events",
                    "🏠 Less personal freedom"
                ]
            }
        ]
    },
    "rent": {
        "category": "Rent",
        "description": "Rent your own apartment (2+ semester commitment required)",
        "min_lease_semesters": 2,
        "penalty_fee": 3000.0,  # $3000 early termination fee
        "options": [
            {
                "id": "apt_cozy_budget",
                "name": "Cozy Budget Apartment",
                "monthly_cost": 1100.0,
                "upfront_cost": 2200.0,  # 2 months deposit
                "commute_minutes": 25,
                "stress_level": "Medium",
                "gpa_modifier": -0.01,
                "social_modifier": 0.05,
                "benefits": [
                    "🏠 Your own private space",
                    "💰 Affordable at $1,100/month",
                    "⏰ Reasonable 25min commute",
                    "✅ Live independently",
                    "🔑 Complete privacy"
                ],
                "cons": [
                    "💸 $2,200 upfront deposit",
                    "📝 2-semester lease minimum",
                    "⚠️ $3,000 penalty if break lease",
                    "💡 Utilities not included (~$150/mo)",
                    "😓 Medium stress from commute"
                ]
            },
            {
                "id": "apt_spacious",
                "name": "Spacious Modern Apartment",
                "monthly_cost": 1500.0,
                "upfront_cost": 3000.0,  # 2 months deposit
                "commute_minutes": 15,
                "stress_level": "Low",
                "gpa_modifier": 0.01,
                "social_modifier": 0.08,
                "benefits": [
                    "🏠 Spacious personal space",
                    "✨ Modern amenities included",
                    "⏰ Only 15min to campus",
                    "😊 Low stress lifestyle",
                    "📚 Great study environment"
                ],
                "cons": [
                    "💸 $3,000 upfront deposit",
                    "💰 Higher rent at $1,500/month",
                    "📝 2-semester lease minimum",
                    "⚠️ $3,000 penalty if break lease",
                    "💡 Utilities add ~$150/month"
                ]
            },
            {
                "id": "apt_luxury",
                "name": "Luxury Apartment Complex",
                "monthly_cost": 2000.0,
                "upfront_cost": 4000.0,  # 2 months deposit
                "commute_minutes": 10,
                "stress_level": "Low",
                "gpa_modifier": 0.02,
                "social_modifier": 0.15,
                "benefits": [
                    "🏆 Premium amenities (gym, pool)",
                    "🏠 Maximum personal space",
                    "⏰ Just 10min to campus",
                    "😊 Minimal stress",
                    "👥 Great social scene"
                ],
                "cons": [
                    "💸 $4,000 upfront deposit",
                    "💰 Very expensive: $2,000/month",
                    "📝 2-semester lease commitment",
                    "⚠️ $3,000 penalty if break lease",
                    "💎 Total cost ~$24,000/year"
                ]
            }
        ]
    },
    "shared": {
        "category": "House Sharing",
        "description": "Share a house/apartment with roommates (1+ semester commitment)",
        "min_lease_semesters": 1,
        "penalty_fee": 1500.0,  # $1500 early termination fee (less than full rent)
        "options": [
            {
                "id": "shared_basic",
                "name": "Basic Shared House",
                "monthly_cost": 650.0,
                "upfront_cost": 1300.0,  # 2 months deposit
                "commute_minutes": 30,
                "stress_level": "Medium-High",
                "gpa_modifier": -0.02,
                "social_modifier": 0.12,
                "benefits": [
                    "💰 Very affordable: $650/month",
                    "👥 Built-in social life",
                    "⚡ Shared utilities (~$50/person)",
                    "🤝 Learn to live with others",
                    "💸 Save $5,000+/year vs solo"
                ],
                "cons": [
                    "😓 High stress from roommate conflicts",
                    "🔊 Noise and distractions",
                    "🚪 Limited personal space",
                    "⏰ 30min commute",
                    "⚠️ $1,500 penalty if break lease"
                ]
            },
            {
                "id": "shared_comfortable",
                "name": "Comfortable Shared Apartment",
                "monthly_cost": 850.0,
                "upfront_cost": 1700.0,  # 2 months deposit
                "commute_minutes": 20,
                "stress_level": "Medium",
                "gpa_modifier": 0.0,
                "social_modifier": 0.15,
                "benefits": [
                    "💰 Affordable: $850/month",
                    "🏠 Better space than basic",
                    "👥 Good social balance",
                    "⏰ Only 20min commute",
                    "🤝 Compatible roommates"
                ],
                "cons": [
                    "🚪 Still shared living space",
                    "😓 Medium stress potential",
                    "📝 1-semester lease minimum",
                    "⚠️ $1,500 penalty if break lease",
                    "🔊 Occasional conflicts"
                ]
            },
            {
                "id": "shared_upscale",
                "name": "Upscale Shared Loft",
                "monthly_cost": 1100.0,
                "upfront_cost": 2200.0,  # 2 months deposit
                "commute_minutes": 12,
                "stress_level": "Low",
                "gpa_modifier": 0.01,
                "social_modifier": 0.18,
                "benefits": [
                    "🏠 Modern, spacious loft",
                    "⏰ Just 12min to campus",
                    "😊 Low stress environment",
                    "👥 Great community vibe",
                    "✨ Premium amenities"
                ],
                "cons": [
                    "💸 $2,200 upfront deposit",
                    "💰 Higher cost: $1,100/month",
                    "🚪 Still shared spaces",
                    "📝 1-semester lease minimum",
                    "⚠️ $1,500 penalty if break lease"
                ]
            }
        ]
    }
}

# Legacy HOUSING_OPTIONS dictionary for backward compatibility
# Maps to Housing model objects with relevant option data
HOUSING_OPTIONS = {
    "dorm_standard": Housing(
        option_id="dorm_standard",
        name="Standard Dorm",
        monthly_cost=900.0,
        gpa_modifier=0.02,
        social_modifier=0.15
    ),
    "family_stay": Housing(
        option_id="family_stay",
        name="Live with Family",
        monthly_cost=0.0,
        gpa_modifier=0.00,
        social_modifier=-0.05
    ),
    "apt_cozy_budget": Housing(
        option_id="apt_cozy_budget",
        name="Cozy Budget Apartment",
        monthly_cost=1100.0,
        gpa_modifier=-0.01,
        social_modifier=0.05
    ),
    "apt_spacious": Housing(
        option_id="apt_spacious",
        name="Spacious Modern Apartment",
        monthly_cost=1500.0,
        gpa_modifier=0.01,
        social_modifier=0.08
    ),
    "apt_luxury": Housing(
        option_id="apt_luxury",
        name="Luxury Apartment Complex",
        monthly_cost=2000.0,
        gpa_modifier=0.02,
        social_modifier=0.15
    ),
    "shared_basic": Housing(
        option_id="shared_basic",
        name="Basic Shared House",
        monthly_cost=650.0,
        gpa_modifier=-0.02,
        social_modifier=0.12
    ),
    "shared_comfortable": Housing(
        option_id="shared_comfortable",
        name="Comfortable Shared Apartment",
        monthly_cost=850.0,
        gpa_modifier=0.0,
        social_modifier=0.15
    ),
    "shared_upscale": Housing(
        option_id="shared_upscale",
        name="Upscale Shared Loft",
        monthly_cost=1100.0,
        gpa_modifier=0.01,
        social_modifier=0.18
    ),
}

# Keep old names for backward compatibility with existing code
HOUSING_OPTIONS["dorm"] = HOUSING_OPTIONS["dorm_standard"]
HOUSING_OPTIONS["family"] = HOUSING_OPTIONS["family_stay"]
HOUSING_OPTIONS["apt_shared"] = HOUSING_OPTIONS["shared_basic"]
HOUSING_OPTIONS["apt_studio"] = HOUSING_OPTIONS["apt_spacious"]


def get_housing_options_by_category(category: str) -> List[Dict]:
    """Get all housing options for a specific category"""
    if category in HOUSING_CATALOG:
        return HOUSING_CATALOG[category]["options"]
    return []


def get_housing_option_details(option_id: str) -> Dict:
    """Get detailed info about a specific housing option"""
    for category_data in HOUSING_CATALOG.values():
        for option in category_data["options"]:
            if option["id"] == option_id:
                return option
    return None


def get_lease_requirement(option_id: str) -> tuple:
    """Get lease requirement and penalty fee for a housing option"""
    for category_data in HOUSING_CATALOG.values():
        for option in category_data["options"]:
            if option["id"] == option_id:
                return (category_data["min_lease_semesters"], category_data["penalty_fee"])
    return (1, 0.0)


def can_break_lease(option_id: str, semesters_lived: int) -> bool:
    """Check if player can break lease without penalty"""
    min_semesters, _ = get_lease_requirement(option_id)
    return semesters_lived >= min_semesters


def get_early_termination_fee(option_id: str, semesters_lived: int) -> float:
    """Get the penalty fee for breaking lease early"""
    min_semesters, penalty_fee = get_lease_requirement(option_id)
    if semesters_lived >= min_semesters:
        return 0.0
    return penalty_fee
