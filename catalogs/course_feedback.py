# Course feedback and rating system
# Students can provide feedback on courses to help others

from typing import Dict, List
from pydantic import BaseModel, Field


class CourseFeedback(BaseModel):
    """Model for course feedback"""
    course_id: str
    semester: int
    rating: int = Field(ge=1, le=5, description="Rating from 1-5 stars")
    difficulty_rating: int = Field(ge=1, le=5, description="Difficulty from 1 (easy) to 5 (very hard)")
    time_commitment: str = Field(description="Hours per week: light (<5), moderate (5-10), heavy (10-15), extreme (15+)")
    would_recommend: bool
    pros: List[str] = Field(default_factory=list, description="What you liked about the course")
    cons: List[str] = Field(default_factory=list, description="What could be improved")
    tips: str = Field(default="", description="Advice for future students")
    professor_quality: int = Field(ge=1, le=5, description="Professor effectiveness 1-5")
    real_world_relevance: int = Field(ge=1, le=5, description="How applicable to real world 1-5")
    
    
class CourseFeedbackSummary(BaseModel):
    """Aggregated feedback for a course"""
    course_id: str
    course_name: str
    total_reviews: int
    average_rating: float
    average_difficulty: float
    average_time_commitment: str
    recommendation_percentage: float
    common_pros: List[str]
    common_cons: List[str]
    top_tips: List[str]


# Sample feedback data (in a real app, this would be in a database)
SAMPLE_COURSE_FEEDBACK = {
    "CS101": [
        {
            "course_id": "CS101",
            "semester": 1,
            "rating": 5,
            "difficulty_rating": 3,
            "time_commitment": "moderate",
            "would_recommend": True,
            "pros": ["Great introduction to programming", "Supportive professor", "Fun projects"],
            "cons": ["Pacing could be faster for experienced programmers"],
            "tips": "Start projects early and don't be afraid to ask questions in office hours!",
            "professor_quality": 5,
            "real_world_relevance": 5
        },
        {
            "course_id": "CS101",
            "semester": 1,
            "rating": 4,
            "difficulty_rating": 4,
            "time_commitment": "heavy",
            "would_recommend": True,
            "pros": ["Solid foundation", "Good resources"],
            "cons": ["Challenging for complete beginners", "Heavy workload"],
            "tips": "Form a study group - debugging with peers helps a lot.",
            "professor_quality": 4,
            "real_world_relevance": 5
        }
    ],
    "CS102": [
        {
            "course_id": "CS102",
            "semester": 2,
            "rating": 4,
            "difficulty_rating": 5,
            "time_commitment": "extreme",
            "would_recommend": True,
            "pros": ["Essential for interviews", "Challenging but rewarding"],
            "cons": ["Very difficult", "Time-consuming assignments"],
            "tips": "Practice implementing data structures from scratch. Don't just memorize.",
            "professor_quality": 4,
            "real_world_relevance": 5
        }
    ],
    "BUS101": [
        {
            "course_id": "BUS101",
            "semester": 1,
            "rating": 4,
            "difficulty_rating": 2,
            "time_commitment": "light",
            "would_recommend": True,
            "pros": ["Easy to understand", "Real-world examples", "Engaging lectures"],
            "cons": ["Sometimes feels too basic"],
            "tips": "Participate in class discussions - it's an easy way to boost your grade.",
            "professor_quality": 4,
            "real_world_relevance": 4
        }
    ],
    "MATH141": [
        {
            "course_id": "MATH141",
            "semester": 1,
            "rating": 3,
            "difficulty_rating": 5,
            "time_commitment": "heavy",
            "would_recommend": True,
            "pros": ["Fundamental math skills", "Prepares you for advanced courses"],
            "cons": ["Very challenging", "Fast-paced", "Homework is time-consuming"],
            "tips": "Use Khan Academy or YouTube for extra help. Go to tutoring sessions!",
            "professor_quality": 3,
            "real_world_relevance": 4
        },
        {
            "course_id": "MATH141",
            "semester": 1,
            "rating": 4,
            "difficulty_rating": 4,
            "time_commitment": "heavy",
            "would_recommend": True,
            "pros": ["Good professor", "Important material"],
            "cons": ["Tough exams"],
            "tips": "Do all the practice problems. Exams are similar to homework.",
            "professor_quality": 4,
            "real_world_relevance": 4
        }
    ]
}


# Pre-computed summaries (in real app, compute dynamically)
COURSE_FEEDBACK_SUMMARIES = {
    "CS101": {
        "course_id": "CS101",
        "course_name": "Introduction to Programming",
        "total_reviews": 2,
        "average_rating": 4.5,
        "average_difficulty": 3.5,
        "average_time_commitment": "moderate-heavy",
        "recommendation_percentage": 100.0,
        "common_pros": [
            "Great introduction to programming",
            "Supportive professors",
            "Fun and engaging projects",
            "Solid foundation for future courses"
        ],
        "common_cons": [
            "Can be slow for those with prior experience",
            "Challenging for complete beginners",
            "Heavy workload"
        ],
        "top_tips": [
            "Start projects early!",
            "Form study groups for debugging",
            "Use office hours - professors are helpful",
            "Practice coding every day"
        ]
    },
    "CS102": {
        "course_id": "CS102",
        "course_name": "Data Structures",
        "total_reviews": 1,
        "average_rating": 4.0,
        "average_difficulty": 5.0,
        "average_time_commitment": "extreme",
        "recommendation_percentage": 100.0,
        "common_pros": [
            "Essential knowledge for tech interviews",
            "Challenging but very rewarding",
            "Teaches you to think like a computer scientist"
        ],
        "common_cons": [
            "Extremely difficult",
            "Very time-consuming assignments",
            "Steep learning curve"
        ],
        "top_tips": [
            "Implement every data structure from scratch",
            "Start LeetCode practice early",
            "Don't fall behind - material builds quickly",
            "Form study groups"
        ]
    },
    "BUS101": {
        "course_id": "BUS101",
        "course_name": "Introduction to Business",
        "total_reviews": 1,
        "average_rating": 4.0,
        "average_difficulty": 2.0,
        "average_time_commitment": "light",
        "recommendation_percentage": 100.0,
        "common_pros": [
            "Easy to understand concepts",
            "Lots of real-world examples",
            "Engaging professor"
        ],
        "common_cons": [
            "Material can feel basic at times"
        ],
        "top_tips": [
            "Participate actively in discussions",
            "Connect concepts to current business news",
            "Network with classmates"
        ]
    },
    "MATH141": {
        "course_id": "MATH141",
        "course_name": "Calculus I",
        "total_reviews": 2,
        "average_rating": 3.5,
        "average_difficulty": 4.5,
        "average_time_commitment": "heavy",
        "recommendation_percentage": 100.0,
        "common_pros": [
            "Builds fundamental math skills",
            "Prepares you for advanced courses",
            "Important for STEM careers"
        ],
        "common_cons": [
            "Very challenging material",
            "Fast-paced lectures",
            "Difficult exams",
            "Time-consuming homework"
        ],
        "top_tips": [
            "Use online resources like Khan Academy",
            "Go to ALL tutoring sessions",
            "Do every practice problem",
            "Form study groups early",
            "Don't fall behind - material compounds"
        ]
    }
}


# Student success stories for motivation
STUDENT_SUCCESS_STORIES = {
    "cs": [
        {
            "name": "Alex T.",
            "story": "I struggled with CS101 at first, but by forming a study group and going to office hours, I ended up with an A. Now I'm a software engineer at Google!",
            "course": "CS101",
            "tip": "Don't be afraid to ask for help. Everyone struggles at first."
        },
        {
            "name": "Sarah M.",
            "story": "Data Structures was the hardest course I've ever taken. But it prepared me so well for technical interviews. I got offers from 3 FAANG companies!",
            "course": "CS102",
            "tip": "The struggle is worth it. Push through and you'll be amazed at what you can do."
        },
        {
            "name": "Mike L.",
            "story": "I failed Algorithms the first time. Retook it, worked harder, and got an A-. Now I'm a machine learning engineer. Failure isn't final!",
            "course": "CS203",
            "tip": "Persistence beats talent. Keep going even when it's hard."
        }
    ],
    "business": [
        {
            "name": "Jessica R.",
            "story": "Business classes taught me more than just theory - I learned to network. My connections from college landed me my first consulting job.",
            "course": "BUS101",
            "tip": "Build relationships with everyone - your classmates are future colleagues and clients."
        },
        {
            "name": "David K.",
            "story": "The capstone project was intense, but working with a real company taught me so much. They hired me full-time after graduation!",
            "course": "BUS490",
            "tip": "Treat every project like a job interview. You never know where it might lead."
        }
    ],
    "engineering": [
        {
            "name": "Emily C.",
            "story": "Engineering was brutal, especially the math. But I graduated and now I design bridges. My work will be around for 100 years!",
            "course": "ENGR201",
            "tip": "Remember why you started. Engineers build the future."
        },
        {
            "name": "James P.",
            "story": "Capstone project was stressful but amazing. We built a working prototype that's now a startup. Sometimes the best opportunities come from class projects.",
            "course": "ENGR401",
            "tip": "Take capstone seriously - it could launch your career."
        }
    ]
}
