from academics.curriculum_models import SemesterCurriculum, Course, CurriculumTopic

# Minimal curriculum used for playthroughs/tests
CURRICULUM = {
    "nyc_public": {
        "cs": {
            1: SemesterCurriculum(
                semester=1,
                notes="Intro track",
                courses=[Course(id="cs101", title="Intro Programming", credits=4, weekly_hours=10)],
            ),
        },
        "ba": {
            1: SemesterCurriculum(
                semester=1,
                courses=[Course(id="ba101", title="Intro Business", credits=3, weekly_hours=8)],
            )
        },
    },
    "nyc_private": {
        "cs": {
            1: SemesterCurriculum(
                semester=1,
                courses=[Course(id="csP101", title="Intro Programming (Private)", credits=4, weekly_hours=11)],
            )
        },
    },
}
