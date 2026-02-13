from core_domain.player.player_model import Job

# Expanded job catalog with major-specific career paths
# Jobs gated by difficulty, GPA, and major
# Real-world salary ranges and stress levels based on role characteristics

JOB_DEFS = {
    # Entry-level / Low-tier jobs (available to anyone)
    "barista_low": Job(
        job_id="barista_low",
        title="Barista (Local Café)",
        hourly_wage=15.0,
        hours_per_week=12,
        stress_per_semester=6.0,
        network_gain=2.0,
        tier="low"
    ),
    "retail_cashier": Job(
        job_id="retail_cashier",
        title="Retail Cashier",
        hourly_wage=14.5,
        hours_per_week=15,
        stress_per_semester=5.0,
        network_gain=1.0,
        tier="low"
    ),
    "food_service": Job(
        job_id="food_service",
        title="Food Service Worker",
        hourly_wage=15.5,
        hours_per_week=14,
        stress_per_semester=8.0,
        network_gain=1.5,
        tier="low"
    ),

    # Mid-tier jobs (require 3.0+ GPA or specific major)
    "it_help_mid": Job(
        job_id="it_help_mid",
        title="IT Helpdesk (Campus)",
        hourly_wage=19.0,
        hours_per_week=10,
        stress_per_semester=8.0,
        network_gain=4.0,
        tier="mid"
    ),
    "tutor_mid": Job(
        job_id="tutor_mid",
        title="Academic Tutor",
        hourly_wage=20.0,
        hours_per_week=8,
        stress_per_semester=7.0,
        network_gain=5.0,
        tier="mid"
    ),
    "research_assistant": Job(
        job_id="research_assistant",
        title="Lab/Research Assistant",
        hourly_wage=18.0,
        hours_per_week=12,
        stress_per_semester=10.0,
        network_gain=8.0,
        tier="mid"
    ),
    "writing_assistant": Job(
        job_id="writing_assistant",
        title="Writing Center Tutor",
        hourly_wage=17.5,
        hours_per_week=10,
        stress_per_semester=6.0,
        network_gain=5.0,
        tier="mid"
    ),
    "policy_intern": Job(
        job_id="policy_intern",
        title="Government Policy Intern",
        hourly_wage=16.0,
        hours_per_week=15,
        stress_per_semester=9.0,
        network_gain=10.0,
        tier="mid"
    ),

    # High-tier internships (require 3.2+ GPA or strong major fit)
    "intern_high": Job(
        job_id="intern_high",
        title="Intern (Big Company)",
        hourly_wage=26.0,
        hours_per_week=16,
        stress_per_semester=14.0,
        network_gain=8.0,
        tier="high"
    ),
    "cs_intern": Job(
        job_id="cs_intern",
        title="Software Engineering Intern",
        hourly_wage=28.0,
        hours_per_week=16,
        stress_per_semester=15.0,
        network_gain=9.0,
        tier="high"
    ),
    "finance_intern": Job(
        job_id="finance_intern",
        title="Finance/Investment Banking Intern",
        hourly_wage=32.0,
        hours_per_week=20,
        stress_per_semester=20.0,
        network_gain=10.0,
        tier="high"
    ),
    "consulting_intern": Job(
        job_id="consulting_intern",
        title="Management Consulting Intern",
        hourly_wage=30.0,
        hours_per_week=18,
        stress_per_semester=18.0,
        network_gain=12.0,
        tier="high"
    ),
    "nursing_preceptor": Job(
        job_id="nursing_preceptor",
        title="Certified Nursing Assistant (CNA)",
        hourly_wage=18.0,
        hours_per_week=12,
        stress_per_semester=16.0,
        network_gain=7.0,
        tier="high"
    ),
    "hospital_intern": Job(
        job_id="hospital_intern",
        title="Hospital Intern (Pre-Med)",
        hourly_wage=16.0,
        hours_per_week=14,
        stress_per_semester=12.0,
        network_gain=9.0,
        tier="high"
    ),
    "journalism_intern": Job(
        job_id="journalism_intern",
        title="Journalism/Media Intern",
        hourly_wage=15.0,
        hours_per_week=15,
        stress_per_semester=13.0,
        network_gain=11.0,
        tier="high"
    ),

    # Startup/entrepreneurial tier
    "startup_intern": Job(
        job_id="startup_intern",
        title="Startup Intern",
        hourly_wage=22.0,
        hours_per_week=18,
        stress_per_semester=18.0,
        network_gain=10.0,
        tier="startup"
    ),
    "startup_technical": Job(
        job_id="startup_technical",
        title="Technical Startup Role",
        hourly_wage=25.0,
        hours_per_week=20,
        stress_per_semester=20.0,
        network_gain=12.0,
        tier="startup"
    ),

    # Post-grad pathways (future reference)
    "accountant": Job(
        job_id="accountant",
        title="Junior Accountant (CPA track)",
        hourly_wage=32.0,
        hours_per_week=45,
        stress_per_semester=25.0,
        network_gain=6.0,
        tier="high"
    ),
    "software_engineer": Job(
        job_id="software_engineer",
        title="Software Engineer",
        hourly_wage=55.0,
        hours_per_week=45,
        stress_per_semester=18.0,
        network_gain=5.0,
        tier="high"
    ),
}
