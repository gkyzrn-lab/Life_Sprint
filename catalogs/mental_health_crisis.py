"""
Mental Health Crisis Catalog

IMPORTANT DESIGN PHILOSOPHY:
- This system is EDUCATIONAL and SUPPORTIVE
- It teaches that seeking help is the RIGHT choice
- It shows that treatment WORKS
- It ALWAYS provides resources
- It emphasizes HOPE and RECOVERY

This is NOT meant to glorify or trivialize mental health crises.
This IS meant to teach teens that help is available and recovery is possible.
"""

from core_domain.crisis.crisis_models import MentalHealthResource

# ==============================================================================
# EMERGENCY RESOURCES (ALWAYS AVAILABLE)
# ==============================================================================

EMERGENCY_RESOURCES = [
    {
        "resource_id": "988_lifeline",
        "name": "988 Suicide & Crisis Lifeline",
        "description": "Free, confidential support 24/7 for people in distress. Call or text 988.",
        "contact": "988 (call or text)",
        "available_24_7": True,
        "cost": "free",
        "priority": 1,  # Always show first
    },
    {
        "resource_id": "crisis_text_line",
        "name": "Crisis Text Line",
        "description": "Text HOME to 741741 for free, 24/7 crisis support via text message.",
        "contact": "Text HOME to 741741",
        "available_24_7": True,
        "cost": "free",
        "priority": 2,
    },
    {
        "resource_id": "trevor_project",
        "name": "The Trevor Project (LGBTQ+ Youth)",
        "description": "Crisis support for LGBTQ+ young people. Call 1-866-488-7386 or text START to 678-678.",
        "contact": "1-866-488-7386 or text START to 678-678",
        "available_24_7": True,
        "cost": "free",
        "priority": 3,
    },
    {
        "resource_id": "campus_counseling",
        "name": "Campus Counseling Center",
        "description": "Free or low-cost counseling services provided by your college. Usually 6-12 free sessions per year.",
        "contact": "Check your college's student services website",
        "available_24_7": False,
        "cost": "free",
        "priority": 4,
    },
    {
        "resource_id": "nami",
        "name": "NAMI (National Alliance on Mental Illness)",
        "description": "Education, support groups, and resources for mental health. Call 1-800-950-NAMI or text NAMI to 741741.",
        "contact": "1-800-950-6264",
        "available_24_7": False,
        "cost": "free",
        "priority": 5,
    },
]

# ==============================================================================
# THERAPY OPTIONS
# ==============================================================================

THERAPY_OPTIONS = {
    "individual": {
        "type": "individual",
        "name": "Individual Therapy",
        "description": "One-on-one counseling with a licensed therapist. Most effective for personalized treatment.",
        "sessions_per_month": 4,
        "cost_per_session": 150.0,  # Without insurance
        "insurance_typical_coverage": 0.70,  # 70% covered typical
        "effectiveness": 0.85,  # Highly effective
        "crisis_risk_reduction_per_session": 2.0,  # Reduces crisis risk by 2 points per session
        "mental_health_improvement_per_session": 3.0,
        "time_commitment_hours_per_week": 1.0,
    },
    "group": {
        "type": "group",
        "name": "Group Therapy",
        "description": "Therapy with 6-10 other people facing similar challenges. More affordable, builds community.",
        "sessions_per_month": 4,
        "cost_per_session": 50.0,
        "insurance_typical_coverage": 0.70,
        "effectiveness": 0.70,  # Effective, especially for social support
        "crisis_risk_reduction_per_session": 1.5,
        "mental_health_improvement_per_session": 2.0,
        "time_commitment_hours_per_week": 1.5,
    },
    "intensive": {
        "type": "intensive",
        "name": "Intensive Outpatient Program (IOP)",
        "description": "3-5 sessions per week for severe cases. Comprehensive treatment while living at home.",
        "sessions_per_month": 12,
        "cost_per_session": 200.0,
        "insurance_typical_coverage": 0.80,  # Usually better coverage for intensive
        "effectiveness": 0.95,  # Very effective for severe cases
        "crisis_risk_reduction_per_session": 4.0,
        "mental_health_improvement_per_session": 5.0,
        "time_commitment_hours_per_week": 9.0,  # Significant commitment
    },
    "campus": {
        "type": "individual",
        "name": "Campus Counseling (Free)",
        "description": "Free counseling through your college. Limited sessions (6-12/year) but no cost.",
        "sessions_per_month": 2,  # Limited availability
        "cost_per_session": 0.0,  # FREE
        "insurance_typical_coverage": 1.0,
        "effectiveness": 0.75,  # Effective but limited
        "crisis_risk_reduction_per_session": 1.5,
        "mental_health_improvement_per_session": 2.0,
        "time_commitment_hours_per_week": 0.5,
        "sessions_per_year_limit": 10,
    },
}

# ==============================================================================
# MEDICATION OPTIONS
# ==============================================================================

MEDICATION_OPTIONS = {
    "ssri_antidepressant": {
        "type": "antidepressant",
        "name": "SSRI Antidepressant",
        "description": "Selective Serotonin Reuptake Inhibitor. Treats depression and anxiety. Takes 4-6 weeks to work fully.",
        "monthly_cost": 30.0,  # Generic with insurance
        "monthly_cost_uninsured": 150.0,
        "insurance_typical_coverage": 0.80,
        "effectiveness": 0.70,  # 70% of people see significant improvement
        "mental_health_baseline_increase": 20.0,  # Raises baseline by 20 points
        "crisis_threshold_increase": 15.0,  # Raises crisis threshold
        "weeks_to_full_effect": 6,
        "common_side_effects": [
            {"name": "nausea", "severity": 0.3, "duration_weeks": 2},
            {"name": "fatigue", "severity": 0.4, "duration_weeks": 3},
            {"name": "sleep_changes", "severity": 0.2, "duration_weeks": 4},
        ],
        "benefits": "Reduces depression symptoms, improves mood stability, lowers anxiety",
    },
    "snri_antidepressant": {
        "type": "antidepressant",
        "name": "SNRI Antidepressant",
        "description": "Serotonin-Norepinephrine Reuptake Inhibitor. Treats depression and chronic pain/anxiety.",
        "monthly_cost": 40.0,
        "monthly_cost_uninsured": 180.0,
        "insurance_typical_coverage": 0.80,
        "effectiveness": 0.72,
        "mental_health_baseline_increase": 22.0,
        "crisis_threshold_increase": 16.0,
        "weeks_to_full_effect": 6,
        "common_side_effects": [
            {"name": "nausea", "severity": 0.4, "duration_weeks": 3},
            {"name": "increased_blood_pressure", "severity": 0.2, "duration_weeks": 0},  # Ongoing
            {"name": "dry_mouth", "severity": 0.2, "duration_weeks": 0},
        ],
        "benefits": "Reduces depression, improves energy, helps with anxiety and pain",
    },
    "anti_anxiety": {
        "type": "anti_anxiety",
        "name": "Anti-Anxiety Medication (Buspirone)",
        "description": "Non-addictive anti-anxiety medication. Helps with generalized anxiety disorder.",
        "monthly_cost": 25.0,
        "monthly_cost_uninsured": 100.0,
        "insurance_typical_coverage": 0.80,
        "effectiveness": 0.65,
        "mental_health_baseline_increase": 15.0,
        "crisis_threshold_increase": 12.0,
        "weeks_to_full_effect": 4,
        "common_side_effects": [
            {"name": "dizziness", "severity": 0.3, "duration_weeks": 2},
            {"name": "headache", "severity": 0.2, "duration_weeks": 1},
        ],
        "benefits": "Reduces anxiety, improves stress tolerance, non-addictive",
    },
    "combination": {
        "type": "both",
        "name": "Antidepressant + Anti-Anxiety",
        "description": "Combination therapy for depression and anxiety. More comprehensive treatment.",
        "monthly_cost": 55.0,
        "monthly_cost_uninsured": 250.0,
        "insurance_typical_coverage": 0.80,
        "effectiveness": 0.78,
        "mental_health_baseline_increase": 28.0,
        "crisis_threshold_increase": 20.0,
        "weeks_to_full_effect": 6,
        "common_side_effects": [
            {"name": "nausea", "severity": 0.4, "duration_weeks": 3},
            {"name": "fatigue", "severity": 0.3, "duration_weeks": 4},
            {"name": "dizziness", "severity": 0.2, "duration_weeks": 2},
        ],
        "benefits": "Addresses both depression and anxiety comprehensively",
    },
}

# IMPORTANT NOTE: Medication HELPS when prescribed appropriately.
# Side effects are REAL but typically MANAGEABLE and DECREASE over time.
# Benefits typically OUTWEIGH side effects for those who need medication.

# ==============================================================================
# SEMESTER LEAVE OPTIONS
# ==============================================================================

LEAVE_OPTIONS = {
    "partial_load": {
        "type": "partial",
        "name": "Reduced Course Load",
        "description": "Drop to 2-3 courses instead of full-time. Remain enrolled, reduce stress.",
        "courses_dropped": 2,
        "tuition_refund_percent": 0.0,  # No refund, still enrolled
        "graduation_delay_semesters": 0,  # May extend by a semester
        "financial_aid_affected": False,
        "recovery_rate_multiplier": 1.3,  # 30% faster recovery
        "stress_reduction": 30.0,
        "mental_health_improvement_per_week": 2.0,
        "can_work_more": True,
    },
    "medical_withdrawal": {
        "type": "medical_withdrawal",
        "name": "Medical Withdrawal",
        "description": "Withdraw from all courses with doctor's note. GPA protected, partial tuition refund.",
        "courses_dropped": 5,  # All courses
        "tuition_refund_percent": 0.50,  # 50% refund typical
        "graduation_delay_semesters": 1,
        "financial_aid_affected": False,  # Protected if medical
        "recovery_rate_multiplier": 2.5,  # Much faster recovery
        "stress_reduction": 70.0,
        "mental_health_improvement_per_week": 5.0,
        "gpa_protected": True,  # No W's on transcript
        "requires_documentation": True,
    },
    "leave_of_absence": {
        "type": "full_semester",
        "name": "Leave of Absence (Full Semester)",
        "description": "Take a full semester off. No tuition, return when ready. Delays graduation.",
        "courses_dropped": 5,
        "tuition_refund_percent": 1.0,  # Full refund if done before semester
        "graduation_delay_semesters": 1,
        "financial_aid_affected": True,  # May affect future aid
        "recovery_rate_multiplier": 3.0,  # Maximum recovery
        "stress_reduction": 90.0,
        "mental_health_improvement_per_week": 8.0,
        "can_work_fulltime": True,
        "can_travel": True,
    },
}

# ==============================================================================
# CRISIS TRIGGERS (Educational - shows what causes crises)
# ==============================================================================

CRISIS_TRIGGERS = {
    "academic_overload": {
        "name": "Academic Overload",
        "description": "Taking too many difficult courses simultaneously",
        "stress_increase": 15.0,
        "burnout_increase": 20.0,
        "warning": "You're taking 18 credits of hard classes while working 20 hours/week. This is unsustainable.",
    },
    "exam_failure": {
        "name": "Failed Major Exam",
        "description": "Failed an important exam or course",
        "stress_increase": 25.0,
        "mental_health_decrease": 10.0,
        "warning": "One exam doesn't define you. Your college has tutoring and academic support.",
    },
    "financial_crisis": {
        "name": "Financial Crisis",
        "description": "Unable to pay rent or tuition",
        "stress_increase": 30.0,
        "financial_stress_increase": 40.0,
        "warning": "Financial stress is real. Talk to financial aid office about emergency grants.",
    },
    "breakup": {
        "name": "Relationship Breakup",
        "description": "End of significant relationship",
        "stress_increase": 20.0,
        "social_isolation_increase": 25.0,
        "mental_health_decrease": 15.0,
        "warning": "Breakups hurt. Lean on friends and campus counseling.",
    },
    "social_isolation": {
        "name": "Severe Loneliness",
        "description": "No friends or support network",
        "social_isolation_increase": 40.0,
        "mental_health_decrease": 20.0,
        "warning": "You're not alone. Join clubs, talk to classmates, visit counseling center.",
    },
    "family_crisis": {
        "name": "Family Emergency",
        "description": "Serious family illness or crisis",
        "stress_increase": 35.0,
        "mental_health_decrease": 20.0,
        "warning": "Family crises are incredibly stressful. Dean of students can help with leave options.",
    },
    "sleep_deprivation": {
        "name": "Chronic Sleep Deprivation",
        "description": "Consistently sleeping < 4 hours/night",
        "sleep_deprivation_increase": 30.0,
        "mental_health_decrease": 15.0,
        "burnout_increase": 20.0,
        "warning": "Sleep is not optional. Your brain needs 7-9 hours to function.",
    },
}

# ==============================================================================
# ACHIEVEMENTS (Rewards seeking help and recovering)
# ==============================================================================

CRISIS_ACHIEVEMENTS = [
    {
        "achievement_id": "reached_out",
        "name": "I Reached Out 🤝",
        "description": "You asked for help when you needed it. That takes courage.",
        "tier": "bronze",
        "trigger": "Accept crisis intervention or start therapy",
        "message": "Asking for help is a sign of strength, not weakness.",
    },
    {
        "achievement_id": "therapy_started",
        "name": "Starting Therapy 💬",
        "description": "You started therapy. This is an investment in yourself.",
        "tier": "bronze",
        "trigger": "Attend first therapy session",
        "message": "Therapy works. Give it time.",
    },
    {
        "achievement_id": "medication_courage",
        "name": "Trying Medication 💊",
        "description": "You tried medication for mental health. That's brave.",
        "tier": "bronze",
        "trigger": "Start medication",
        "message": "Medication helps millions of people. There's no shame in it.",
    },
    {
        "achievement_id": "crisis_survived",
        "name": "I Survived 💪",
        "description": "You got through a mental health crisis with support.",
        "tier": "silver",
        "trigger": "Recover from crisis (crisis level < 30)",
        "message": "You made it through. You're stronger than you think.",
    },
    {
        "achievement_id": "semester_recovered",
        "name": "Taking Care of Myself 🌱",
        "description": "You took a semester off to focus on mental health. That's self-care.",
        "tier": "silver",
        "trigger": "Complete semester leave and return",
        "message": "Taking time off doesn't mean you failed. It means you're smart.",
    },
    {
        "achievement_id": "stable_six_months",
        "name": "Six Months Stable 🌟",
        "description": "Six months without a crisis. You're building resilience.",
        "tier": "gold",
        "trigger": "180 days since last crisis",
        "message": "Look how far you've come. Recovery is possible.",
    },
    {
        "achievement_id": "helping_others",
        "name": "Paying It Forward ❤️",
        "description": "You helped someone else who was struggling.",
        "tier": "gold",
        "trigger": "Provide peer support",
        "message": "Your experience can help others. That's powerful.",
    },
    {
        "achievement_id": "mental_health_advocate",
        "name": "Mental Health Advocate 🗣️",
        "description": "You openly talk about mental health and reduce stigma.",
        "tier": "platinum",
        "trigger": "Complete recovery journey, help others",
        "message": "You're breaking down stigma. Thank you.",
    },
]

# ==============================================================================
# STORIES (Supportive, educational, hopeful)
# ==============================================================================

CRISIS_STORIES = [
    {
        "story_id": "crisis_detected",
        "title": "Something's Not Right",
        "message": "You've been pushing yourself too hard. Your stress is {stress:.0f}/100. Your mental health is {mental_health:.0f}/100. This is serious.\n\n**You don't have to go through this alone.**\n\n📞 988 Suicide & Crisis Lifeline: Call or text 988\n💬 Crisis Text Line: Text HOME to 741741\n🏫 Campus Counseling: Free sessions available\n\nWhat do you want to do?",
        "tone": "supportive",
        "trigger": "Crisis level >= 60",
        "resources_included": True,
    },
    {
        "story_id": "first_therapy",
        "title": "First Therapy Session",
        "message": "You walked into the counseling center. It felt vulnerable. But the therapist listened without judgment. They said: 'What you're feeling is valid. And we can work on this together.'\n\nYou don't feel fixed yet. But you feel heard. That's a start.",
        "tone": "supportive",
        "trigger": "First therapy session",
    },
    {
        "story_id": "medication_start",
        "title": "Starting Medication",
        "message": "You picked up your prescription. The pharmacist said it'll take 4-6 weeks to feel the full effect. You might have some side effects at first.\n\nYou're nervous. But your doctor said: '70% of people see significant improvement. Let's see if this helps you.'\n\nYou're trying. That's what matters.",
        "tone": "supportive",
        "trigger": "Start medication",
    },
    {
        "story_id": "side_effects",
        "title": "Medication Side Effects",
        "message": "The first two weeks were rough. Nausea. Fatigue. You almost quit.\n\nBut your doctor said: 'Side effects usually decrease. The benefits take longer. Give it 6 weeks.'\n\nWeek 6: The nausea is gone. Your mood is better. It was worth pushing through.",
        "tone": "educational",
        "trigger": "6 weeks on medication",
    },
    {
        "story_id": "therapy_working",
        "title": "Therapy Is Helping",
        "message": "You've been in therapy for 2 months. You're learning coping skills. How to set boundaries. How to challenge negative thoughts.\n\nLast week, you had a stressful day. Normally, you'd spiral. But this time, you used a technique from therapy. It helped.\n\nProgress isn't linear. But you're healing.",
        "tone": "triumphant",
        "trigger": "8+ therapy sessions",
    },
    {
        "story_id": "considering_leave",
        "title": "Maybe I Need a Break",
        "message": "You're exhausted. You can't focus. You're failing classes. You feel like you're drowning.\n\nYour advisor said: 'Taking a semester off isn't giving up. It's taking care of yourself so you can succeed long-term.'\n\nGraduation can wait. Your mental health can't.",
        "tone": "supportive",
        "trigger": "Crisis level >= 80",
    },
    {
        "story_id": "took_leave",
        "title": "I Took Time Off",
        "message": "You withdrew for the semester. Medical withdrawal - your GPA is protected.\n\nAt first, you felt like a failure. But then:\n- You started sleeping 8 hours\n- You went to therapy weekly\n- Your medication kicked in\n- You reconnected with hobbies\n\nThree months later: You feel like yourself again.",
        "tone": "triumphant",
        "trigger": "Complete semester leave",
    },
    {
        "story_id": "crisis_prevented",
        "title": "Crisis Averted",
        "message": "You felt it coming. The stress. The darkness. But this time, you knew what to do:\n\n✓ Called your therapist\n✓ Reached out to friends\n✓ Used coping skills\n✓ Asked for extensions on assignments\n\nYou didn't spiral. You caught it early. That's growth.",
        "tone": "triumphant",
        "trigger": "High stress but effective intervention",
    },
    {
        "story_id": "six_months_stable",
        "title": "I'm Doing Better",
        "message": "It's been six months since your last crisis. You:\n- Go to therapy every other week\n- Take your medication consistently\n- Have a support network\n- Know your triggers\n- Practice self-care\n\nYou're not 'cured.' But you're managing. And that's huge.",
        "tone": "triumphant",
        "trigger": "180 days stable",
    },
    {
        "story_id": "helped_a_friend",
        "title": "I Helped Someone Else",
        "message": "Your friend was struggling. You recognized the signs because you'd been there.\n\nYou said: 'I know this is hard. I've been there. Want to talk? Or I can just sit with you.'\n\nThey said: 'Thank you. I needed that.'\n\nYour pain gave you empathy. That's powerful.",
        "tone": "triumphant",
        "trigger": "Provide peer support",
    },
]
