"""Real-world scenarios and case studies for curriculum courses."""

from __future__ import annotations

from typing import Dict, List

from catalogs.curriculums import CURRICULUMS

Scenario = Dict[str, str]

OVERRIDES: Dict[str, List[Scenario]] = {
    "CS101": [
        {
            "title": "Campus Event Registration App",
            "summary": "Build a simple registration app to track attendees, waitlists, and email confirmations for a campus event."
        },
        {
            "title": "Study Buddy Matching",
            "summary": "Create a small script that pairs students based on availability and shared classes."
        }
    ],
    "CS102": [
        {
            "title": "Library Book Search",
            "summary": "Implement stacks and queues to manage holds and returns in a digital library system."
        },
        {
            "title": "Real-Time Chat Buffer",
            "summary": "Use linked lists to store and display the latest messages without slowing the app."
        }
    ],
    "CS203": [
        {
            "title": "Delivery Route Optimization",
            "summary": "Compare sorting and shortest-path algorithms to minimize delivery times across a city map."
        }
    ],
    "CS220": [
        {
            "title": "Process Scheduling at Scale",
            "summary": "Simulate CPU scheduling to reduce lag in a multiplayer game server."
        }
    ],
    "CS225": [
        {
            "title": "Student Records Database",
            "summary": "Design tables and queries for course enrollment, grades, and prerequisite checks."
        }
    ],
    "CS230": [
        {
            "title": "Team Sprint Planning",
            "summary": "Apply agile workflows to ship a campus marketplace feature in two-week sprints."
        }
    ],
    "CS301": [
        {
            "title": "Dorm Wi-Fi Troubleshooting",
            "summary": "Diagnose latency and packet loss using network layers and protocols."
        }
    ],
    "CS310": [
        {
            "title": "Scholarship Prediction",
            "summary": "Train a model to predict scholarship eligibility using anonymized student data."
        }
    ],
    "CS320": [
        {
            "title": "Phishing Defense Lab",
            "summary": "Analyze phishing patterns and design safer login flows for a student portal."
        }
    ],
    "CS350": [
        {
            "title": "Capstone Prototype",
            "summary": "Build an MVP that solves a real campus problem and test it with users."
        }
    ],
    "CS351": [
        {
            "title": "Capstone Launch",
            "summary": "Harden, deploy, and demo your project to stakeholders and recruiters."
        }
    ],
    "BUS101": [
        {
            "title": "Club Budget Case",
            "summary": "Balance a student club budget across events, marketing, and emergency reserves."
        }
    ],
    "ACC201": [
        {
            "title": "Startup Financials",
            "summary": "Prepare basic statements for a campus startup to evaluate runway."
        }
    ],
    "FIN301": [
        {
            "title": "Investment Pitch",
            "summary": "Evaluate a company using DCF and present a buy/hold/sell recommendation."
        }
    ],
    "MKT201": [
        {
            "title": "Campus Campaign",
            "summary": "Design a go-to-market plan to grow attendance for a student event."
        }
    ],
    "MGT301": [
        {
            "title": "Team Performance",
            "summary": "Diagnose a team conflict and propose leadership interventions."
        }
    ],
    "OPS301": [
        {
            "title": "Cafeteria Flow",
            "summary": "Reduce wait times by redesigning prep and service workflows."
        }
    ],
    "BUS490": [
        {
            "title": "Capstone Business Plan",
            "summary": "Deliver a full business plan including pricing, marketing, and operations."
        }
    ],
    "CHEM101": [
        {
            "title": "Water Quality Testing",
            "summary": "Analyze samples and interpret results for a local water report."
        }
    ],
    "PHYS141": [
        {
            "title": "Skate Park Safety",
            "summary": "Model forces and motion to improve ramp design safety guidelines."
        }
    ],
    "ENGR201": [
        {
            "title": "Bridge Load Analysis",
            "summary": "Calculate stress distribution to validate design safety margins."
        }
    ],
    "ENGR210": [
        {
            "title": "Energy Efficiency Retrofit",
            "summary": "Evaluate HVAC efficiency improvements for a campus building."
        }
    ],
    "ENGR301": [
        {
            "title": "Prototype Sprint",
            "summary": "Design, test, and iterate a device prototype based on user feedback."
        }
    ],
    "ENGR401": [
        {
            "title": "Capstone Phase 1",
            "summary": "Define requirements, scope, and system architecture for a real client."
        }
    ],
    "ENGR402": [
        {
            "title": "Capstone Phase 2",
            "summary": "Deliver the final system, test against KPIs, and present results."
        }
    ]
}


def _generic_scenarios(course_name: str) -> List[Scenario]:
    return [
        {
            "title": f"{course_name} in Practice",
            "summary": f"Apply {course_name} concepts to solve a real problem for a campus org, startup, or internship project."
        },
        {
            "title": "Case Study Sprint",
            "summary": f"Analyze a real-world case study and present a solution using tools from {course_name}."
        }
    ]


def build_default_scenarios() -> Dict[str, List[Scenario]]:
    scenarios: Dict[str, List[Scenario]] = {}
    for major in CURRICULUMS.values():
        for semester in major["semesters"].values():
            for course in semester["courses"]:
                course_id = course["id"]
                course_name = course.get("name", course_id)
                scenarios[course_id] = _generic_scenarios(course_name)
    scenarios.update(OVERRIDES)
    return scenarios


COURSE_SCENARIOS = build_default_scenarios()


def get_course_scenarios(course_id: str, course_name: str) -> List[Scenario]:
    """Return real-world scenarios for a course, falling back to a generic case study."""
    return COURSE_SCENARIOS.get(course_id) or _generic_scenarios(course_name)
