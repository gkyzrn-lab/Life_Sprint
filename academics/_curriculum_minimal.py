from academics.curriculum_models import SemesterCurriculum, Course, CurriculumTopic

CURRICULUM = {
    "nyc_public": {
        "cs": {
            1: SemesterCurriculum(
                semester=1,
                notes="Intro track",
                courses=[
                    Course(id="cs101", title="Intro Programming", credits=4, weekly_hours=10)
                ],
            ),
        },
    },
}
