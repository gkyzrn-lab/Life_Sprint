from catalogs.majors import MAJORS
from catalogs.colleges import COLLEGES
from catalogs.housing import HOUSING_OPTIONS
from catalogs.jobs import JOB_DEFS
from catalogs.activities import ACTIVITIES
from catalogs.life_events import LIFE_EVENTS

# Enhanced curriculum system
from catalogs.curriculums import CURRICULUMS
from catalogs.curriculum_achievements import (
    CURRICULUM_ACHIEVEMENTS,
    CURRICULUM_BADGES,
    SEMESTER_MILESTONES,
    PROGRESS_LEVELS,
    GAMIFICATION_POINTS,
    CURRICULUM_CHALLENGES
)
from catalogs.course_feedback import (
    SAMPLE_COURSE_FEEDBACK,
    COURSE_FEEDBACK_SUMMARIES,
    STUDENT_SUCCESS_STORIES,
    CourseFeedback
)
from catalogs.learning_paths import (
    LEARNING_PATHS,
    CAREER_INTERESTS,
    recommend_learning_path
)
from catalogs.student_progress import (
    SAMPLE_STUDENT_PROGRESS,
    StudentProgress,
    get_progress_insights,
    check_achievement_unlocked,
    ProgressUpdate
)
from catalogs.educational_resources import (
    COURSE_RESOURCES,
    GENERAL_RESOURCES,
    STUDY_RESOURCES,
    get_resources_for_course,
    get_free_resources_for_course
)

from catalogs.real_world_scenarios import get_course_scenarios
