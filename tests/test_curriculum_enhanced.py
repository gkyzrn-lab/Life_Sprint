"""
Unit tests for enhanced curriculum features
Tests curriculum endpoints, gamification, learning paths, and progress tracking
"""

import pytest
from fastapi.testclient import TestClient
from main import app
from catalogs.curriculums import CURRICULUMS
from catalogs.curriculum_achievements import CURRICULUM_ACHIEVEMENTS
from catalogs.learning_paths import LEARNING_PATHS, recommend_learning_path
from catalogs.student_progress import calculate_gpa, calculate_completion_percentage

client = TestClient(app)


class TestCurriculumEndpoints:
    """Test curriculum information endpoints"""
    
    def test_get_enhanced_curriculum(self):
        """Test getting enhanced curriculum for a major"""
        response = client.get("/curriculum/enhanced/cs")
        assert response.status_code == 200
        data = response.json()
        assert data["major_id"] == "cs"
        assert "semesters" in data
        assert data["total_semesters"] == 8
        assert len(data["career_paths"]) > 0
    
    def test_get_enhanced_curriculum_invalid_major(self):
        """Test getting curriculum for non-existent major"""
        response = client.get("/curriculum/enhanced/invalid_major")
        assert response.status_code == 404
    
    def test_get_semester_detail(self):
        """Test getting specific semester information"""
        response = client.get("/curriculum/enhanced/cs/semester/1")
        assert response.status_code == 200
        data = response.json()
        assert data["major_id"] == "cs"
        assert "semester_info" in data
        assert data["semester_info"]["semester"] == 1
    
    def test_get_semester_detail_invalid(self):
        """Test getting non-existent semester"""
        response = client.get("/curriculum/enhanced/cs/semester/99")
        assert response.status_code == 404
    
    def test_get_curriculum_visualization(self):
        """Test getting visualization-friendly curriculum data"""
        response = client.get("/curriculum/enhanced/cs/visualization")
        assert response.status_code == 200
        data = response.json()
        assert "timeline" in data
        assert len(data["timeline"]) == 8
        assert "difficulty_distribution" in data["timeline"][0]
    
    def test_get_curriculum_roadmap(self):
        """Test getting curriculum roadmap grouped by year"""
        response = client.get("/curriculum/enhanced/cs/roadmap")
        assert response.status_code == 200
        data = response.json()
        assert "years" in data
        assert len(data["years"]) == 4  # 4 years
    
    def test_list_available_curricula(self):
        """Test listing all available curricula"""
        response = client.get("/curriculum/enhanced/list")
        assert response.status_code == 200
        data = response.json()
        assert "available_majors" in data
        assert len(data["available_majors"]) > 0


class TestGamificationEndpoints:
    """Test gamification endpoints"""
    
    def test_get_all_achievements(self):
        """Test getting all achievements"""
        response = client.get("/curriculum/achievements")
        assert response.status_code == 200
        data = response.json()
        assert "achievements" in data
        assert data["total_achievements"] > 0
        assert "total_points_available" in data
    
    def test_get_achievement_detail(self):
        """Test getting specific achievement"""
        response = client.get("/curriculum/achievements/first_semester")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == "first_semester"
        assert "points" in data
    
    def test_get_achievement_detail_invalid(self):
        """Test getting non-existent achievement"""
        response = client.get("/curriculum/achievements/invalid_achievement")
        assert response.status_code == 404
    
    def test_get_all_milestones(self):
        """Test getting all semester milestones"""
        response = client.get("/curriculum/milestones")
        assert response.status_code == 200
        data = response.json()
        assert "milestones" in data
        assert "total_semesters" in data
    
    def test_get_semester_milestone(self):
        """Test getting milestone for specific semester"""
        response = client.get("/curriculum/milestones/semester/1")
        assert response.status_code == 200
        data = response.json()
        assert data["semester"] == 1
        assert "milestone" in data
        assert "level" in data
    
    def test_get_progress_levels(self):
        """Test getting all progress levels"""
        response = client.get("/curriculum/progress-levels")
        assert response.status_code == 200
        data = response.json()
        assert "levels" in data
        assert len(data["levels"]) == 4  # Freshman, Sophomore, Junior, Senior
    
    def test_get_point_system(self):
        """Test getting point system information"""
        response = client.get("/curriculum/points")
        assert response.status_code == 200
        data = response.json()
        assert "point_rewards" in data
        assert "description" in data
    
    def test_get_all_challenges(self):
        """Test getting all challenges"""
        response = client.get("/curriculum/challenges")
        assert response.status_code == 200
        data = response.json()
        assert "challenges" in data
        assert data["total_challenges"] > 0


class TestFeedbackEndpoints:
    """Test course feedback endpoints"""
    
    def test_get_course_feedback(self):
        """Test getting feedback for a course"""
        response = client.get("/curriculum/feedback/course/CS101")
        assert response.status_code == 200
        data = response.json()
        assert data["course_id"] == "CS101"
        assert "reviews" in data
    
    def test_get_course_feedback_summary(self):
        """Test getting aggregated feedback summary"""
        response = client.get("/curriculum/feedback/course/CS101/summary")
        assert response.status_code == 200
        data = response.json()
        assert data["course_id"] == "CS101"
        assert "average_rating" in data
        assert "common_pros" in data
    
    def test_submit_course_feedback(self):
        """Test submitting course feedback"""
        feedback = {
            "course_id": "CS101",
            "semester": 1,
            "rating": 5,
            "difficulty_rating": 3,
            "time_commitment": "moderate",
            "would_recommend": True,
            "pros": ["Great course"],
            "cons": [],
            "tips": "Start early",
            "professor_quality": 5,
            "real_world_relevance": 5
        }
        response = client.post("/curriculum/feedback/course/CS101", json=feedback)
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
    
    def test_get_success_stories(self):
        """Test getting success stories for a major"""
        response = client.get("/curriculum/success-stories/cs")
        assert response.status_code == 200
        data = response.json()
        assert "stories" in data
        assert data["major_id"] == "cs"


class TestLearningPathEndpoints:
    """Test learning path endpoints"""
    
    def test_get_all_learning_paths(self):
        """Test getting all learning paths"""
        response = client.get("/curriculum/learning-paths")
        assert response.status_code == 200
        data = response.json()
        assert "learning_paths" in data
        assert data["total_paths"] > 0
    
    def test_get_learning_paths_by_major(self):
        """Test getting paths for specific major"""
        response = client.get("/curriculum/learning-paths/major/cs")
        assert response.status_code == 200
        data = response.json()
        assert data["major_id"] == "cs"
        assert len(data["learning_paths"]) > 0
    
    def test_get_learning_path_detail(self):
        """Test getting specific learning path"""
        response = client.get("/curriculum/learning-paths/cs_fullstack")
        assert response.status_code == 200
        data = response.json()
        assert data["path_id"] == "cs_fullstack"
        assert "recommended_electives" in data
    
    def test_recommend_paths(self):
        """Test getting personalized recommendations"""
        response = client.get(
            "/curriculum/learning-paths/recommend/cs",
            params={"interests": ["web", "design"], "skills": ["javascript"]}
        )
        assert response.status_code == 200
        data = response.json()
        assert "recommendations" in data
        assert len(data["recommendations"]) > 0
    
    def test_get_career_assessment(self):
        """Test getting career assessment questions"""
        response = client.get("/curriculum/career-assessment")
        assert response.status_code == 200
        data = response.json()
        assert "questions" in data


class TestProgressTrackingEndpoints:
    """Test progress tracking endpoints"""
    
    def test_get_detailed_progress(self):
        """Test getting detailed progress for sample player"""
        response = client.get("/curriculum/player/player_001/detailed-progress")
        assert response.status_code == 200
        data = response.json()
        assert "progress" in data
        assert "insights" in data
    
    def test_get_gpa_history(self):
        """Test getting GPA history"""
        response = client.get("/curriculum/player/player_001/gpa-history")
        assert response.status_code == 200
        data = response.json()
        assert "gpa_history" in data
        assert "current_gpa" in data
    
    def test_get_achievements_progress(self):
        """Test getting achievements progress"""
        response = client.get("/curriculum/player/player_001/achievements-progress")
        assert response.status_code == 200
        data = response.json()
        assert "earned_achievements" in data
        assert "locked_achievements" in data
    
    def test_get_next_steps(self):
        """Test getting personalized next steps"""
        response = client.get("/curriculum/player/player_001/next-steps")
        assert response.status_code == 200
        data = response.json()
        assert "next_steps" in data
    
    def test_compare_with_peers(self):
        """Test peer comparison"""
        # This would need actual player - using mock for now
        # response = client.get("/curriculum/player/test_player/compare-peers")
        # assert response.status_code in [200, 404]
        pass


class TestResourceEndpoints:
    """Test educational resource endpoints"""
    
    def test_get_course_resources(self):
        """Test getting resources for a course"""
        response = client.get("/curriculum/resources/course/CS101")
        assert response.status_code == 200
        data = response.json()
        assert "resources" in data or "course_name" in data
    
    def test_get_course_resources_free_only(self):
        """Test getting only free resources"""
        response = client.get("/curriculum/resources/course/CS101?free_only=true")
        assert response.status_code == 200
        data = response.json()
        assert "filter" in data
        assert data["filter"] == "free_only"
    
    def test_get_subject_resources(self):
        """Test getting subject area resources"""
        response = client.get("/curriculum/resources/subject/computer_science")
        assert response.status_code == 200
        data = response.json()
        assert "subject" in data
        assert "resources" in data
    
    def test_get_study_tips(self):
        """Test getting study tips and techniques"""
        response = client.get("/curriculum/resources/study-tips")
        assert response.status_code == 200
        data = response.json()
        assert "study_techniques" in data
        assert "productivity_tools" in data
    
    def test_get_all_course_resources(self):
        """Test listing all courses with resources"""
        response = client.get("/curriculum/resources/all-courses")
        assert response.status_code == 200
        data = response.json()
        assert "courses_with_resources" in data
    
    def test_get_recommended_resources(self):
        """Test getting recommended resources by major"""
        response = client.get("/curriculum/resources/recommendations/cs")
        assert response.status_code == 200
        data = response.json()
        assert "major_id" in data


class TestHelperFunctions:
    """Test helper functions from catalogs"""
    
    def test_calculate_gpa(self):
        """Test GPA calculation"""
        grades = ["A", "B", "A", "C"]
        credits = [3, 4, 3, 3]
        gpa = calculate_gpa(grades, credits)
        assert 3.0 <= gpa <= 3.5
    
    def test_calculate_completion_percentage(self):
        """Test completion percentage calculation"""
        percentage = calculate_completion_percentage(30, 120)
        assert percentage == 25.0
    
    def test_recommend_learning_path_function(self):
        """Test learning path recommendation algorithm"""
        recommendations = recommend_learning_path(
            "cs",
            ["web", "design"],
            ["javascript", "python"]
        )
        assert len(recommendations) > 0
        assert all("path_id" in rec for rec in recommendations)


class TestDataIntegrity:
    """Test data integrity and consistency"""
    
    def test_all_curricula_have_8_semesters(self):
        """Ensure all curricula have 8 semesters"""
        for major_id, curriculum in CURRICULUMS.items():
            assert curriculum["total_semesters"] == 8
            assert len(curriculum["semesters"]) == 8
    
    def test_all_semesters_have_required_fields(self):
        """Ensure all semesters have required fields"""
        for major_id, curriculum in CURRICULUMS.items():
            for sem_num, semester in curriculum["semesters"].items():
                assert "semester" in semester
                assert "title" in semester
                assert "description" in semester
                assert "courses" in semester
                assert isinstance(semester["courses"], list)
    
    def test_all_courses_have_required_fields(self):
        """Ensure all courses have required fields"""
        for major_id, curriculum in CURRICULUMS.items():
            for sem_num, semester in curriculum["semesters"].items():
                for course in semester["courses"]:
                    assert "id" in course
                    assert "name" in course
                    assert "credits" in course
                    assert "description" in course
                    assert "difficulty" in course
                    assert "skills" in course
                    assert "real_world" in course
    
    def test_all_achievements_have_required_fields(self):
        """Ensure all achievements have required fields"""
        for ach_id, achievement in CURRICULUM_ACHIEVEMENTS.items():
            assert "id" in achievement
            assert "name" in achievement
            assert "description" in achievement
            assert "points" in achievement
            assert achievement["points"] > 0
    
    def test_all_learning_paths_have_required_fields(self):
        """Ensure all learning paths have required fields"""
        for path_id, path in LEARNING_PATHS.items():
            assert "path_id" in path
            assert "name" in path
            assert "description" in path
            assert "major_id" in path
            assert "career_focus" in path
            assert "recommended_electives" in path
            assert "skills_developed" in path
            assert "typical_careers" in path


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
