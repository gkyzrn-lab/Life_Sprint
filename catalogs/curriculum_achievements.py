# Gamification elements for curriculum progression
# Achievements, badges, and milestones that students can earn

CURRICULUM_ACHIEVEMENTS = {
    "first_semester": {
        "id": "first_semester",
        "name": "🎓 Freshman Survivor",
        "description": "Complete your first semester of college!",
        "icon": "🎓",
        "points": 100,
        "unlock_condition": "Complete semester 1"
    },
    "dean_list": {
        "id": "dean_list",
        "name": "⭐ Dean's List",
        "description": "Achieve a GPA of 3.5 or higher in a semester",
        "icon": "⭐",
        "points": 250,
        "unlock_condition": "GPA >= 3.5 in any semester"
    },
    "perfect_semester": {
        "id": "perfect_semester",
        "name": "💯 Perfect Semester",
        "description": "Get straight A's for an entire semester",
        "icon": "💯",
        "points": 500,
        "unlock_condition": "All A grades in semester"
    },
    "night_owl": {
        "id": "night_owl",
        "name": "🦉 Night Owl",
        "description": "Complete 10 late-night study sessions",
        "icon": "🦉",
        "points": 150,
        "unlock_condition": "Study after midnight 10 times"
    },
    "study_group_master": {
        "id": "study_group_master",
        "name": "👥 Study Group Master",
        "description": "Form or join 5 different study groups",
        "icon": "👥",
        "points": 200,
        "unlock_condition": "Participate in 5 study groups"
    },
    "sophomore_status": {
        "id": "sophomore_status",
        "name": "📚 Sophomore Status",
        "description": "Complete your second year of college",
        "icon": "📚",
        "points": 300,
        "unlock_condition": "Complete semester 4"
    },
    "halfway_there": {
        "id": "halfway_there",
        "name": "🎯 Halfway There",
        "description": "Complete half of your degree requirements",
        "icon": "🎯",
        "points": 400,
        "unlock_condition": "Complete 50% of credits"
    },
    "internship_secured": {
        "id": "internship_secured",
        "name": "💼 Internship Secured",
        "description": "Land your first internship",
        "icon": "💼",
        "points": 600,
        "unlock_condition": "Get accepted to an internship"
    },
    "junior_achievement": {
        "id": "junior_achievement",
        "name": "🚀 Junior Achievement",
        "description": "Complete your third year of college",
        "icon": "🚀",
        "points": 500,
        "unlock_condition": "Complete semester 6"
    },
    "capstone_crusader": {
        "id": "capstone_crusader",
        "name": "🏆 Capstone Crusader",
        "description": "Complete your capstone project",
        "icon": "🏆",
        "points": 1000,
        "unlock_condition": "Complete capstone course"
    },
    "job_offer": {
        "id": "job_offer",
        "name": "💰 Job Offer Champion",
        "description": "Receive a full-time job offer before graduation",
        "icon": "💰",
        "points": 800,
        "unlock_condition": "Get job offer in senior year"
    },
    "graduation_ready": {
        "id": "graduation_ready",
        "name": "🎉 Graduation Ready",
        "description": "Complete all degree requirements",
        "icon": "🎉",
        "points": 1500,
        "unlock_condition": "Complete semester 8"
    },
    "comeback_kid": {
        "id": "comeback_kid",
        "name": "💪 Comeback Kid",
        "description": "Improve your GPA by 0.5+ points in a semester",
        "icon": "💪",
        "points": 300,
        "unlock_condition": "Increase GPA by 0.5 or more"
    },
    "extra_credit": {
        "id": "extra_credit",
        "name": "➕ Extra Credit Hunter",
        "description": "Complete 5 extra credit assignments",
        "icon": "➕",
        "points": 200,
        "unlock_condition": "Do 5 extra credit assignments"
    },
    "mentor_network": {
        "id": "mentor_network",
        "name": "🤝 Mentor Network",
        "description": "Connect with 3 professors or industry mentors",
        "icon": "🤝",
        "points": 350,
        "unlock_condition": "Build 3 mentor relationships"
    },
    "research_assistant": {
        "id": "research_assistant",
        "name": "🔬 Research Assistant",
        "description": "Participate in academic research",
        "icon": "🔬",
        "points": 400,
        "unlock_condition": "Join a research project"
    },
    "club_president": {
        "id": "club_president",
        "name": "👑 Club President",
        "description": "Lead a student organization",
        "icon": "👑",
        "points": 500,
        "unlock_condition": "Become president of a club"
    },
    "conference_presenter": {
        "id": "conference_presenter",
        "name": "🎤 Conference Presenter",
        "description": "Present at an academic conference",
        "icon": "🎤",
        "points": 700,
        "unlock_condition": "Present research at conference"
    },
    "scholarship_winner": {
        "id": "scholarship_winner",
        "name": "💵 Scholarship Winner",
        "description": "Win an academic scholarship",
        "icon": "💵",
        "points": 600,
        "unlock_condition": "Receive scholarship award"
    },
    "networking_ninja": {
        "id": "networking_ninja",
        "name": "🥷 Networking Ninja",
        "description": "Attend 10 career networking events",
        "icon": "🥷",
        "points": 400,
        "unlock_condition": "Attend 10 networking events"
    }
}

# Badge-style rewards for milestone and course completion
CURRICULUM_BADGES = {
    "milestone_starter": {
        "id": "milestone_starter",
        "name": "🏅 Milestone Starter",
        "description": "Complete your first academic milestone",
        "icon": "🏅",
        "tier": "bronze",
        "points": 100,
        "unlock_condition": "Complete semester milestone 1"
    },
    "course_streak": {
        "id": "course_streak",
        "name": "🔥 Course Streak",
        "description": "Finish 5 courses in a row without a withdraw",
        "icon": "🔥",
        "tier": "silver",
        "points": 250,
        "unlock_condition": "Complete 5 consecutive courses"
    },
    "honors_track": {
        "id": "honors_track",
        "name": "🎖️ Honors Track",
        "description": "Maintain a 3.7+ GPA for two semesters",
        "icon": "🎖️",
        "tier": "gold",
        "points": 500,
        "unlock_condition": "GPA >= 3.7 for 2 consecutive semesters"
    },
    "research_rising": {
        "id": "research_rising",
        "name": "🧪 Research Rising",
        "description": "Join a research project or lab",
        "icon": "🧪",
        "tier": "silver",
        "points": 300,
        "unlock_condition": "Participate in a research project"
    },
    "capstone_star": {
        "id": "capstone_star",
        "name": "🌟 Capstone Star",
        "description": "Complete your capstone with distinction",
        "icon": "🌟",
        "tier": "platinum",
        "points": 800,
        "unlock_condition": "Complete capstone with an A"
    },
    "career_ready": {
        "id": "career_ready",
        "name": "💼 Career Ready",
        "description": "Complete an internship or co-op",
        "icon": "💼",
        "tier": "gold",
        "points": 600,
        "unlock_condition": "Finish an internship or co-op"
    }
}

# Semester milestones with descriptions
SEMESTER_MILESTONES = {
    1: {
        "title": "Welcome to College!",
        "description": "Your journey begins. Focus on building good habits.",
        "achievements": ["first_semester"],
        "tips": [
            "Attend every class - attendance matters more than you think",
            "Form study groups early",
            "Visit your professors during office hours",
            "Explore campus clubs and activities"
        ]
    },
    2: {
        "title": "Finding Your Rhythm",
        "description": "You've survived one semester - now optimize your approach.",
        "achievements": [],
        "tips": [
            "Apply lessons learned from first semester",
            "Start building relationships with professors",
            "Consider joining a research lab or project",
            "Think about summer internships"
        ]
    },
    3: {
        "title": "Sophomore Start",
        "description": "Classes get harder, but you're more prepared.",
        "achievements": [],
        "tips": [
            "Courses become more specialized now",
            "Start thinking about your career direction",
            "Network with upperclassmen in your major",
            "Update your resume and LinkedIn"
        ]
    },
    4: {
        "title": "Halfway Checkpoint",
        "description": "You're halfway through! Time to specialize.",
        "achievements": ["sophomore_status", "halfway_there"],
        "tips": [
            "Apply for summer internships NOW",
            "Choose your concentration/specialization",
            "Consider studying abroad",
            "Start building a portfolio of projects"
        ]
    },
    5: {
        "title": "Junior Year Intensity",
        "description": "The hardest year begins. Stay focused.",
        "achievements": [],
        "tips": [
            "Summer internship experience is crucial",
            "Take on leadership roles in clubs",
            "Start thinking about capstone project ideas",
            "Build your professional network"
        ]
    },
    6: {
        "title": "Junior Spring - Preparation Mode",
        "description": "Prepare for senior year and job hunting.",
        "achievements": ["junior_achievement"],
        "tips": [
            "Start your capstone project planning",
            "Polish your resume and portfolio",
            "Connect with career services",
            "Attend career fairs actively"
        ]
    },
    7: {
        "title": "Senior Year - The Final Push",
        "description": "Last year! Focus on capstone and job search.",
        "achievements": ["capstone_crusader"],
        "tips": [
            "Job search is your priority now",
            "Complete capstone with excellence",
            "Network intensively",
            "Practice interview skills"
        ]
    },
    8: {
        "title": "Graduation Approaches!",
        "description": "Final semester - finish strong and celebrate!",
        "achievements": ["graduation_ready"],
        "tips": [
            "Finalize your capstone and present well",
            "Negotiate job offers carefully",
            "Thank your mentors and professors",
            "Prepare for the next chapter of life"
        ]
    }
}

# Progress tracking levels
PROGRESS_LEVELS = {
    "freshman": {
        "name": "Freshman",
        "min_semester": 1,
        "max_semester": 2,
        "icon": "🌱",
        "description": "New to college life - learning the ropes"
    },
    "sophomore": {
        "name": "Sophomore",
        "min_semester": 3,
        "max_semester": 4,
        "icon": "🌿",
        "description": "Getting serious - finding your path"
    },
    "junior": {
        "name": "Junior",
        "min_semester": 5,
        "max_semester": 6,
        "icon": "🌳",
        "description": "Deep into your major - building expertise"
    },
    "senior": {
        "name": "Senior",
        "min_semester": 7,
        "max_semester": 8,
        "icon": "🎓",
        "description": "Almost there - preparing for career launch"
    }
}

# Point rewards for different actions
GAMIFICATION_POINTS = {
    "complete_course_low": 50,
    "complete_course_medium": 75,
    "complete_course_high": 100,
    "complete_course_very_high": 150,
    "grade_a": 100,
    "grade_b": 75,
    "grade_c": 50,
    "grade_d": 25,
    "complete_semester": 200,
    "join_study_group": 25,
    "attend_office_hours": 20,
    "complete_extra_credit": 50,
    "attend_networking_event": 30,
    "get_internship": 500,
    "get_job_offer": 1000,
    "complete_capstone": 800,
    "present_research": 400,
    "win_scholarship": 600,
    "become_club_leader": 300
}

# Challenges that students can undertake
CURRICULUM_CHALLENGES = {
    "perfectionist": {
        "id": "perfectionist",
        "name": "The Perfectionist",
        "description": "Complete a semester with all A grades",
        "difficulty": "hard",
        "reward_points": 500,
        "reward_description": "Unlock special 'Perfect Student' badge"
    },
    "overachiever": {
        "id": "overachiever",
        "name": "The Overachiever",
        "description": "Take 18+ credits in a semester and maintain 3.5+ GPA",
        "difficulty": "very_hard",
        "reward_points": 750,
        "reward_description": "Unlock 'Overachiever' title and bonus internship opportunities"
    },
    "comeback_story": {
        "id": "comeback_story",
        "name": "The Comeback Story",
        "description": "Improve from below 3.0 GPA to above 3.5 GPA",
        "difficulty": "hard",
        "reward_points": 600,
        "reward_description": "Inspirational story bonus and mentor recognition"
    },
    "balanced_life": {
        "id": "balanced_life",
        "name": "The Balanced Life",
        "description": "Maintain 3.0+ GPA while participating in 3+ extracurriculars",
        "difficulty": "medium",
        "reward_points": 400,
        "reward_description": "Work-life balance achievement and recruiter attention"
    },
    "early_bird": {
        "id": "early_bird",
        "name": "The Early Bird",
        "description": "Secure an internship before junior year",
        "difficulty": "hard",
        "reward_points": 500,
        "reward_description": "Career head start bonus"
    },
    "research_pioneer": {
        "id": "research_pioneer",
        "name": "The Research Pioneer",
        "description": "Get published or present at a conference",
        "difficulty": "very_hard",
        "reward_points": 1000,
        "reward_description": "Academic prestige and graduate school boost"
    },
    "networking_master": {
        "id": "networking_master",
        "name": "The Networking Master",
        "description": "Build connections with 10+ industry professionals",
        "difficulty": "medium",
        "reward_points": 400,
        "reward_description": "Professional network bonus and job leads"
    },
    "entrepreneur": {
        "id": "entrepreneur",
        "name": "The Entrepreneur",
        "description": "Start a student venture or side business",
        "difficulty": "very_hard",
        "reward_points": 1200,
        "reward_description": "Entrepreneurial spirit badge and investor connections"
    }
}
