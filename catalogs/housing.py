from core_domain.player.player_model import Housing

# Housing options affect cashflow and (later) can affect GPA/social.
# Keep these stable IDs; UI and planning will reference option_id.

HOUSING_OPTIONS = {
    "dorm": Housing(
        option_id="dorm",
        name="On-Campus Dorm",
        monthly_cost=900.0,
        gpa_modifier=0.02,
        social_modifier=0.15
    ),
    "family": Housing(
        option_id="family",
        name="Living with Family",
        monthly_cost=0.0,
        gpa_modifier=0.00,
        social_modifier=-0.05
    ),
    "apt_shared": Housing(
        option_id="apt_shared",
        name="Shared Apartment",
        monthly_cost=700.0,
        gpa_modifier=-0.01,
        social_modifier=0.05
    ),
    "apt_studio": Housing(
        option_id="apt_studio",
        name="Small Studio",
        monthly_cost=1300.0,
        gpa_modifier=-0.02,
        social_modifier=-0.02
    ),
}
