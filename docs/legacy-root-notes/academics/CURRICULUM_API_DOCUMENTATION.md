# Curriculum API Documentation

## Overview

The Enhanced Curriculum API provides comprehensive endpoints for managing university education with a game-like experience. Students can explore their major semester-by-semester, track progress, earn achievements, get personalized recommendations, and access learning resources.

**Base URL**: `/curriculum`

## Key Features

1. **Semester-by-Semester Curricula**: Detailed, game-friendly breakdowns of real-world degree paths.
2. **Gamification Elements**: Achievements, badges, and points for completing courses and milestones to boost engagement.

---

## Table of Contents

1. [Key Features](#key-features)
2. [Curriculum Information](#curriculum-information)
3. [Visualization & Roadmaps](#visualization--roadmaps)
4. [Gamification](#gamification)
5. [Course Feedback](#course-feedback)
6. [Learning Paths](#learning-paths)
7. [Progress Tracking](#progress-tracking)
8. [Educational Resources](#educational-resources)

---

## Curriculum Information

### GET `/enhanced/{major_id}`

Get comprehensive curriculum information for a major with detailed semester breakdowns.

**Parameters:**
- `major_id` (path): Major identifier (e.g., "cs", "business", "engineering")

**Response Example:**
```json
{
  "major_id": "cs",
  "major_name": "Computer Science",
  "total_semesters": 8,
  "semesters": {
    "1": {
      "semester": 1,
      "title": "Foundation Year - Fall",
      "description": "Build your programming foundation",
      "courses": [
        {
          "id": "CS101",
          "name": "Introduction to Programming",
          "credits": 4,
          "description": "Master the basics of coding with Python",
          "difficulty": "medium",
          "skills": ["Python basics", "Problem solving"],
          "real_world": "Foundation for all software development roles",
          "real_world_scenarios": [
            {
              "title": "Campus Event Registration App",
              "summary": "Build a simple registration app to track attendees, waitlists, and email confirmations."
            }
          ]
        }
      ],
      "tips": "Focus on understanding concepts, not just syntax"
    }
  },
  "career_paths": ["Software Engineer", "Data Scientist"],
  "skills_gained": ["Programming", "Algorithm design"]
}
```

### GET `/enhanced/{major_id}/semester/{semester_num}`

Get detailed information about a specific semester.

**Parameters:**
- `major_id` (path): Major identifier
- `semester_num` (path): Semester number (1-8)

---

## Visualization & Roadmaps

### GET `/enhanced/{major_id}/visualization`

Get visualization-friendly curriculum data optimized for timeline or flowchart displays.

**Response Includes:**
- Timeline of all semesters
- Course counts per semester
- Credit distribution
- Difficulty distribution
- Key course highlights

### GET `/enhanced/{major_id}/roadmap`

Get a high-level roadmap grouped by academic year with milestones.

**Response Example:**
```json
{
  "major_id": "cs",
  "major_name": "Computer Science",
  "years": [
    {
      "year": 1,
      "name": "Year 1",
      "semesters": [
        {
          "semester": 1,
          "title": "Foundation Year - Fall",
          "description": "Build your programming foundation",
          "tips": "Attend every class - attendance matters"
        }
      ]
    }
  ]
}
```

### GET `/enhanced/list`

List all available enhanced curricula.

---

## Gamification

### GET `/achievements`

Get all available curriculum achievements students can earn.

**Response:**
- List of all achievements with points, icons, and unlock conditions
- Total achievements available
- Total points possible

### GET `/achievements/{achievement_id}`

Get detailed information about a specific achievement.

### GET `/badges`

Get all available curriculum badges students can earn.

**Response Includes:**
- Badge name, tier (bronze/silver/gold/platinum), points, and unlock condition
- Total badges available

### GET `/badges/{badge_id}`

Get detailed information about a specific badge.

### GET `/milestones`

Get all semester milestones with tips and descriptions.

### GET `/milestones/semester/{semester_num}`

Get milestone information for a specific semester including:
- Tips for success
- What to focus on
- Progress level (Freshman, Sophomore, Junior, Senior)

### GET `/progress-levels`

Get all progress levels (Freshman, Sophomore, Junior, Senior) with icons and descriptions.

### GET `/points`

Get information about the gamification point system.

**Points Earned For:**
- Completing courses (50-150 points based on difficulty)
- Good grades (25-100 points)
- Completing semesters (200 points)
- Joining study groups (25 points)
- Getting internships (500 points)
- And more!

### GET `/challenges`

Get all available curriculum challenges.

**Challenge Types:**
- The Perfectionist: All A's in a semester
- The Overachiever: 18+ credits with 3.5+ GPA
- The Comeback Story: Improve GPA significantly
- And more!

### GET `/challenges/{challenge_id}`

Get detailed information about a specific challenge.

---

## Course Feedback

### GET `/feedback/course/{course_id}`

Get student reviews and feedback for a specific course.

**Response Includes:**
- Individual reviews with ratings
- Difficulty ratings
- Time commitment estimates
- Pros and cons
- Tips from previous students

### GET `/feedback/course/{course_id}/summary`

Get aggregated feedback summary for a course.

**Response Example:**
```json
{
  "course_id": "CS101",
  "course_name": "Introduction to Programming",
  "total_reviews": 2,
  "average_rating": 4.5,
  "average_difficulty": 3.5,
  "average_time_commitment": "moderate-heavy",
  "recommendation_percentage": 100.0,
  "common_pros": ["Great introduction", "Supportive professor"],
  "common_cons": ["Can be slow for experienced programmers"],
  "top_tips": ["Start projects early!", "Form study groups"]
}
```

### POST `/feedback/course/{course_id}`

Submit feedback for a course.

**Request Body:**
```json
{
  "course_id": "CS101",
  "semester": 1,
  "rating": 5,
  "difficulty_rating": 3,
  "time_commitment": "moderate",
  "would_recommend": true,
  "pros": ["Great course!"],
  "cons": [],
  "tips": "Start early",
  "professor_quality": 5,
  "real_world_relevance": 5
}
```

### GET `/success-stories/{major_id}`

Get inspirational success stories from students in a specific major.

### GET `/success-stories`

Get all student success stories across all majors.

---

## Learning Paths

### GET `/learning-paths`

Get all available learning paths across all majors.

### GET `/learning-paths/major/{major_id}`

Get learning paths available for a specific major.

**Example Paths:**
- **Computer Science**: Full-Stack Web Dev, ML/AI, Cybersecurity
- **Business**: Finance, Marketing, Consulting
- **Engineering**: Software, Mechanical, Renewable Energy

### GET `/learning-paths/{path_id}`

Get detailed information about a specific learning path.

**Response Includes:**
- Description and career focus
- Recommended electives
- Recommended activities
- Skills developed
- Typical careers

### GET `/learning-paths/recommend/{major_id}`

Get personalized learning path recommendations.

**Query Parameters:**
- `interests`: List of interests (e.g., "web", "design")
- `skills`: List of existing skills (e.g., "javascript", "python")

**Example Request:**
```
GET /learning-paths/recommend/cs?interests=web&interests=design&skills=javascript
```

### GET `/career-assessment`

Get career interest assessment questions to help students choose a path.

### POST `/career-assessment/submit`

Submit career assessment answers and get recommendations.

---

## Progress Tracking

### GET `/player/{player_id}/progress`

Get basic player progress (existing endpoint).

### GET `/player/{player_id}/detailed-progress`

Get comprehensive progress tracking including:
- Overall GPA and credits
- Semester-by-semester progress
- Achievements earned
- Courses completed/in-progress/remaining
- Learning path progress
- Career readiness metrics
- Personalized insights

**Insights Include:**
- Strengths
- Areas for improvement
- Recommendations
- Motivational messages

### GET `/player/{player_id}/gpa-history`

Get semester-by-semester GPA history for visualization.

**Response:**
```json
{
  "player_id": "123",
  "gpa_history": [
    {"semester": 1, "gpa": 3.3, "credits": 15},
    {"semester": 2, "gpa": 3.8, "credits": 16}
  ],
  "current_gpa": 3.6,
  "trend": "improving"
}
```

### GET `/player/{player_id}/achievements-progress`

Get achievements earned and progress toward locked achievements.

### POST `/player/{player_id}/update-progress`

Update student progress (complete a course, assign grade, etc.).

**Request Body:**
```json
{
  "course_id": "CS101",
  "new_status": "completed",
  "grade": "A",
  "notes": "Great course!"
}
```

### GET `/player/{player_id}/next-steps`

Get personalized recommendations for what the student should do next.

**Response Includes:**
- High-priority academic recommendations
- Semester-specific tips
- Learning path suggestions
- Career preparation actions

### GET `/player/{player_id}/compare-peers`

Compare student's progress with peers in the same major (anonymized).

**Metrics:**
- GPA comparison
- Credit pace
- Achievement comparison
- Percentile ranking

---

## Educational Resources

### GET `/resources/course/{course_id}`

Get learning resources for a specific course (videos, articles, books, tools).

**Query Parameters:**
- `free_only` (boolean): If true, return only free resources

**Resource Types:**
- 📺 Video Tutorials
- 📄 Articles
- 📚 Books
- 🎓 Online Courses
- 🛠️ Tools/Software
- 💪 Practice Platforms
- 📖 Documentation
- 👥 Communities
- 🎙️ Podcasts

**Example Response:**
```json
{
  "course_id": "CS101",
  "course_name": "Introduction to Programming",
  "resources": [
    {
      "type": "video",
      "title": "Python for Beginners - Full Course",
      "provider": "freeCodeCamp",
      "url": "https://www.youtube.com/...",
      "description": "Comprehensive Python tutorial",
      "free": true
    }
  ]
}
```

### GET `/resources/subject/{subject}`

Get general resources for a subject area.

**Subjects:**
- `computer_science`
- `business`
- `mathematics`

### GET `/resources/study-tips`

Get study techniques and productivity tools.

**Includes:**
- Study techniques (Pomodoro, Active Recall, Spaced Repetition, Feynman)
- Productivity tools (Notion, Todoist, Forest, Anki)
- Best practices for each technique

### GET `/resources/all-courses`

Get a list of all courses that have resources available.

### GET `/resources/recommendations/{major_id}`

Get recommended resources based on major.

---

## Common Response Codes

- `200 OK`: Successful request
- `404 Not Found`: Resource not found (invalid major_id, course_id, etc.)
- `422 Unprocessable Entity`: Invalid request parameters

---

## Usage Tips

1. **Getting Started**: Start with `/enhanced/{major_id}` to see the full curriculum
2. **Visualization**: Use `/enhanced/{major_id}/visualization` or `/roadmap` for frontend displays
3. **Student Engagement**: Combine progress tracking with achievements and feedback
4. **Learning Resources**: Link course pages to `/resources/course/{course_id}`
5. **Personalization**: Use learning paths to help students specialize

---

## Example User Flow

1. Student views major curriculum: `GET /enhanced/cs`
2. Student checks semester 1 details: `GET /enhanced/cs/semester/1`
3. Student views course resources: `GET /resources/course/CS101`
4. Student reads course feedback: `GET /feedback/course/CS101/summary`
5. Student completes course: `POST /player/{id}/update-progress`
6. Student checks achievements: `GET /player/{id}/achievements-progress`
7. Student explores learning paths: `GET /learning-paths/major/cs`
8. Student gets next steps: `GET /player/{id}/next-steps`

---

## Future Enhancements

- Integration with actual Player model for real-time progress
- Machine learning for personalized recommendations
- Social features (compare with friends, study groups)
- Integration with external learning platforms
- Mobile app optimizations
- Real-time notifications for achievements
- Gamified leaderboards

---

## Support

For questions or issues, contact the development team or check the project README.
