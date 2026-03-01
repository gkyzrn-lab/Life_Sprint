"""Unified course-topics formatter across majors."""

from typing import Dict, Any

from catalogs.ba_course_topics import format_course_topics_for_display as format_ba_topics
from catalogs.cs_course_topics import format_cs_topics_for_display
from catalogs.finance_course_topics import format_finance_accounting_topics
from catalogs.liberal_arts_course_topics import format_liberal_arts_topics
from catalogs.economics_course_topics import format_economics_topics
from catalogs.math_course_topics import format_math_topics
from catalogs.physics_course_topics import format_physics_topics
from catalogs.engineering_course_topics import format_engineering_topics
from catalogs.data_science_course_topics import format_data_science_topics
from catalogs.psychology_course_topics import format_psychology_topics
from catalogs.biology_course_topics import format_biology_topics
from catalogs.chemistry_course_topics import format_chemistry_topics
from catalogs.political_science_course_topics import format_political_science_topics
from catalogs.history_course_topics import format_history_topics


def format_course_topics(course_id: str) -> Dict[str, Any]:
    """Return enriched topics for supported course families."""
    cid = course_id.strip().lower()

    if cid.startswith("ba"):
        return format_ba_topics(cid)

    if cid.startswith("econ"):
        return format_economics_topics(cid)

    if cid.startswith("math"):
        return format_math_topics(cid)

    if cid.startswith("phys"):
        return format_physics_topics(cid)

    if cid.startswith("eng"):
        return format_engineering_topics(cid)

    if cid.startswith(("fin", "acc")):
        return format_finance_accounting_topics(cid)

    if cid.startswith("cs"):
        return format_cs_topics_for_display(cid)

    if cid.startswith("lib"):
        return format_liberal_arts_topics(cid)

    if cid.startswith("ds"):
        return format_data_science_topics(cid)

    if cid.startswith("psych"):
        return format_psychology_topics(cid)

    if cid.startswith("bio"):
        return format_biology_topics(cid)

    if cid.startswith("chem"):
        return format_chemistry_topics(cid)

    if cid.startswith("pol"):
        return format_political_science_topics(cid)

    if cid.startswith("hist"):
        return format_history_topics(cid)

    return {
        "course_id": cid,
        "found": False,
        "message": f"Topics not yet available for {cid}",
    }
