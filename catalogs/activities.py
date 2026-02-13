from core_domain.models import Activity

# Activity catalog. These are optional levers players can choose in planning.
# hours_per_week affects time budget; deltas apply per semester.

ACTIVITIES = {
    "gym": Activity(
        id="gym",
        name="Gym 3x/week",
        hours_per_week=3,
        stress_delta_per_semester=-8.0,
        happiness_delta_per_semester=4.0,
        cost_per_semester=80.0
    ),
    "tutoring": Activity(
        id="tutoring",
        name="Tutoring / Office Hours",
        hours_per_week=3,
        stress_delta_per_semester=-4.0,
        happiness_delta_per_semester=1.0,
        cost_per_semester=0.0
    ),
    "social": Activity(
        id="social",
        name="Social Nights",
        hours_per_week=4,
        stress_delta_per_semester=-6.0,
        happiness_delta_per_semester=8.0,
        cost_per_semester=120.0
    ),
    "therapy": Activity(
        id="therapy",
        name="Therapy / Coaching",
        hours_per_week=1,
        stress_delta_per_semester=-10.0,
        happiness_delta_per_semester=3.0,
        cost_per_semester=200.0
    ),
}
