"""Mock interview system for Life Sprint.

Teaches students:
- How to prepare for interviews
- Common interview questions by role/level
- STAR method for behavioral questions
- Technical vs behavioral questions
- Red flags to avoid
- How to handle difficult questions
- Post-interview follow-up
"""

from typing import Dict, List, Optional, Literal
from pydantic import BaseModel, Field
import random


class InterviewQuestion(BaseModel):
    """A single interview question."""
    question_id: str
    question_text: str
    question_type: Literal["behavioral", "technical", "situational", "culture_fit", "tricky"]
    difficulty: Literal["easy", "medium", "hard"]
    
    # What interviewers are looking for
    key_criteria: List[str] = Field(default_factory=list)
    
    # Example good answer framework
    good_answer_framework: str = ""
    
    # Red flags to avoid
    red_flags: List[str] = Field(default_factory=list)


class InterviewResponse(BaseModel):
    """Player's response to an interview question."""
    response_type: Literal["detailed_star", "brief_answer", "nervous_ramble", "dodge", "honest"]
    response_text: str
    
    # Quality indicators
    used_star_method: bool = False
    used_specific_examples: bool = False
    demonstrated_skill: bool = False
    showed_enthusiasm: bool = False
    avoided_red_flags: bool = False


class InterviewScenario(BaseModel):
    """A complete interview scenario."""
    scenario_id: str
    job_title: str
    company_name: str
    company_tier: Literal["startup", "small", "medium", "large", "fortune_500"]
    interview_round: Literal["phone_screen", "first_round", "technical", "final_round"]
    
    # Interview structure
    questions: List[InterviewQuestion] = Field(default_factory=list)
    time_limit_minutes: int = 45
    
    # Context
    interviewer_personality: Literal["friendly", "neutral", "intimidating", "technical"]
    interview_format: Literal["one_on_one", "panel", "group", "peer"]


class InterviewOutcome(BaseModel):
    """Result of an interview."""
    success: bool
    overall_score: int  # 0-100
    
    # Breakdown by category
    behavioral_score: int = 0
    technical_score: int = 0
    communication_score: int = 0
    culture_fit_score: int = 0
    
    # Feedback
    strengths: List[str] = Field(default_factory=list)
    areas_for_improvement: List[str] = Field(default_factory=list)
    interviewer_feedback: str = ""
    
    # Outcome
    next_step: Literal["rejected", "phone_screen", "first_round", "technical", "final_round", "offer"]
    rejection_reason: Optional[str] = None


class InterviewPrep(BaseModel):
    """Interview preparation tips."""
    tip_id: str
    category: Literal["research", "star_method", "common_questions", "body_language", "follow_up", "red_flags"]
    title: str
    description: str
    example: str
    impact: Literal["low", "medium", "high", "critical"]


# Interview questions by job tier and type
INTERVIEW_QUESTIONS: Dict[str, InterviewQuestion] = {
    # Entry-level behavioral
    "tell_me_about_yourself": InterviewQuestion(
        question_id="tell_me_about_yourself",
        question_text="Tell me about yourself.",
        question_type="behavioral",
        difficulty="easy",
        key_criteria=["concise", "relevant", "structured", "professional"],
        good_answer_framework="Use present-past-future structure: 'I'm currently a [year] student at [school] studying [major]. Previously, I [relevant experience]. I'm interested in this role because [connection to future goals].' Keep to 60-90 seconds.",
        red_flags=[
            "Rambling for 5+ minutes about your whole life story",
            "Talking about irrelevant personal details",
            "Reading your resume word-for-word",
            "Starting with 'Umm, I don't know where to start'"
        ]
    ),
    
    "why_this_company": InterviewQuestion(
        question_id="why_this_company",
        question_text="Why do you want to work here?",
        question_type="culture_fit",
        difficulty="medium",
        key_criteria=["researched_company", "genuine_interest", "specific_reasons", "aligned_values"],
        good_answer_framework="Show you researched the company: 'I'm impressed by [specific company achievement]. Your focus on [company value] aligns with my interest in [your goal]. I'm particularly excited about [specific project/team/technology].'",
        red_flags=[
            "'I need a job and you're hiring'",
            "Generic answer that could apply to any company",
            "Only mentioning salary/benefits",
            "Mispronouncing company name or getting facts wrong"
        ]
    ),
    
    "greatest_weakness": InterviewQuestion(
        question_id="greatest_weakness",
        question_text="What's your greatest weakness?",
        question_type="tricky",
        difficulty="hard",
        key_criteria=["self_aware", "honest_but_strategic", "shows_growth", "not_red_flag"],
        good_answer_framework="Use this formula: 1) Name a real weakness (not 'I'm a perfectionist'). 2) Explain how you're actively working on it. 3) Give a recent example of improvement. Example: 'I used to struggle with public speaking. I joined Toastmasters last year and have given 5 presentations. I'm still nervous but much more confident.'",
        red_flags=[
            "'I don't have any weaknesses' (arrogant)",
            "'I'm a perfectionist' (cliché non-answer)",
            "Naming something critical to the job",
            "'I'm always late' (actual red flag)"
        ]
    ),
    
    "conflict_with_coworker": InterviewQuestion(
        question_id="conflict_with_coworker",
        question_text="Tell me about a time you had a conflict with a coworker or teammate. How did you handle it?",
        question_type="behavioral",
        difficulty="medium",
        key_criteria=["used_star", "took_responsibility", "focused_on_resolution", "professional"],
        good_answer_framework="STAR method: Situation (brief context), Task (your role), Action (specific steps you took to resolve), Result (outcome + what you learned). Focus on YOUR actions, not blaming the other person.",
        red_flags=[
            "Blaming the other person entirely",
            "Getting angry/emotional while telling the story",
            "No resolution or lesson learned",
            "'I've never had a conflict' (unbelievable)"
        ]
    ),
    
    "why_should_we_hire_you": InterviewQuestion(
        question_id="why_should_we_hire_you",
        question_text="Why should we hire you over other candidates?",
        question_type="situational",
        difficulty="hard",
        key_criteria=["confident", "specific_skills", "value_proposition", "differentiated"],
        good_answer_framework="Connect your strengths to their needs. Structure: 'Based on our conversation, you need someone who [key requirement]. My experience with [specific skill/project] positions me well to [solve their problem]. What makes me unique is [differentiator].'",
        red_flags=[
            "Arrogance ('I'm the best')",
            "Putting down other candidates",
            "Vague generalities with no specifics",
            "Desperation ('I really need this job')"
        ]
    ),
    
    # Technical questions (varies by role)
    "technical_problem_solving": InterviewQuestion(
        question_id="technical_problem_solving",
        question_text="Walk me through how you would approach [technical problem relevant to role].",
        question_type="technical",
        difficulty="hard",
        key_criteria=["structured_thinking", "asks_clarifying_questions", "explains_reasoning", "handles_uncertainty"],
        good_answer_framework="1) Ask clarifying questions first. 2) Explain your thought process out loud. 3) Break problem into steps. 4) Consider edge cases. 5) Admit when you don't know something.",
        red_flags=[
            "Jumping to solution without understanding problem",
            "Silent for minutes without explaining thinking",
            "Making up answers when you don't know",
            "Getting defensive when challenged"
        ]
    ),
    
    "describe_project": InterviewQuestion(
        question_id="describe_project",
        question_text="Describe a project you're proud of. What was your role and what was the outcome?",
        question_type="behavioral",
        difficulty="medium",
        key_criteria=["clear_communication", "quantifiable_impact", "team_contribution", "lessons_learned"],
        good_answer_framework="Use STAR method: Describe the project, your specific contributions (not just 'we'), challenges you overcame, measurable results. Focus on quantifiable impact and end with what you learned.",
        red_flags=[
            "Taking credit for team's work ('I did everything')",
            "No clear outcome or impact",
            "Overly technical jargon without explanation",
            "Couldn't explain your actual role"
        ]
    ),
    
    "handle_failure": InterviewQuestion(
        question_id="handle_failure",
        question_text="Tell me about a time you failed. What happened and what did you learn?",
        question_type="behavioral",
        difficulty="hard",
        key_criteria=["vulnerability", "ownership", "growth_mindset", "specific_lesson"],
        good_answer_framework="Choose a real failure (not humble-brag). Take ownership. Focus heavily on what you learned and how you've applied that lesson since. Show growth.",
        red_flags=[
            "Blaming others for the failure",
            "No real failure ('I once got a B+')",
            "No lesson learned",
            "Choosing something too severe (got fired for theft)"
        ]
    ),
    
    "questions_for_us": InterviewQuestion(
        question_id="questions_for_us",
        question_text="Do you have any questions for us?",
        question_type="culture_fit",
        difficulty="easy",
        key_criteria=["prepared_questions", "genuine_interest", "insightful", "not_about_salary"],
        good_answer_framework="Always have 2-3 questions ready. Ask about: team dynamics, growth opportunities, company challenges, day-to-day work. Avoid: salary/benefits in first interview.",
        red_flags=[
            "'No, I'm good' (shows no interest)",
            "Only asking about vacation days",
            "Asking something answered on company website",
            "Asking when you'll get a raise"
        ]
    ),
}


# Interview prep tips
INTERVIEW_PREP_TIPS: Dict[str, InterviewPrep] = {
    "star_method": InterviewPrep(
        tip_id="star_method",
        category="star_method",
        title="Master the STAR Method for Behavioral Questions",
        description="STAR = Situation, Task, Action, Result. Use this framework for 'Tell me about a time...' questions. Spend 10% on S, 10% on T, 60% on A, 20% on R. Focus on YOUR actions, not team's.",
        example="Q: 'Tell me about a time you showed leadership.'\nBad: 'I'm a natural leader.'\nGood: 'Situation: My team was behind on a group project. Task: As lead, I needed to get us back on track. Action: I scheduled a meeting, reassigned tasks based on strengths, and checked in daily. Result: We submitted 2 days early and got an A. I learned that clear communication prevents panic.'",
        impact="critical"
    ),
    
    "research_company": InterviewPrep(
        tip_id="research_company",
        category="research",
        title="Research the Company Thoroughly",
        description="Spend 30+ minutes before interview: read company website, recent news, Glassdoor reviews, LinkedIn employees, competitors. Be able to name: recent product launches, company values, key executives, company size/growth.",
        example="Don't just say 'I want to work here.' Say: 'I saw you just launched [product]. As someone interested in [area], I'm excited about [specific aspect]. I noticed on LinkedIn that [employee] worked on this - what's the team dynamic like?'",
        impact="high"
    ),
    
    "prepare_stories": InterviewPrep(
        tip_id="prepare_stories",
        category="common_questions",
        title="Prepare 5-7 Stories Using STAR Method",
        description="Have ready: 1) Leadership example, 2) Failure/learning, 3) Conflict resolution, 4) Technical challenge, 5) Time management, 6) Going above and beyond, 7) Teamwork. Adapt these to different questions.",
        example="If they ask 'Tell me about teamwork' but you prepared a 'leadership' story, you can adapt: focus on how you collaborated, listened to team input, etc. Same story, different angle.",
        impact="critical"
    ),
    
    "body_language": InterviewPrep(
        tip_id="body_language",
        category="body_language",
        title="Nonverbal Communication Matters",
        description="Make eye contact, smile, sit up straight, lean forward slightly (shows interest), don't fidget. For video interviews: look at camera (not screen), ensure good lighting, professional background.",
        example="Studies show interviewers decide in first 7 seconds. Strong handshake, smile, confident posture, and 'Nice to meet you, thanks for your time' sets positive tone.",
        impact="medium"
    ),
    
    "follow_up": InterviewPrep(
        tip_id="follow_up",
        category="follow_up",
        title="Send Thank You Email Within 24 Hours",
        description="Email each interviewer individually if possible. Structure: 1) Thank them, 2) Reference specific conversation point, 3) Reiterate interest, 4) Add any follow-up info you mentioned. Keep it brief (3-4 sentences).",
        example="'Thanks for taking time to discuss the Product Manager role. I enjoyed learning about your approach to user research. Our conversation reinforced my excitement about contributing to [specific project]. Please let me know if you need anything else. Looking forward to next steps.'",
        impact="medium"
    ),
    
    "avoid_red_flags": InterviewPrep(
        tip_id="avoid_red_flags",
        category="red_flags",
        title="Common Interview Red Flags to Avoid",
        description="Never: arrive late without notice, bad-mouth previous employer, lie about experience, be arrogant, appear desperate, check phone, ask about salary in first interview, say 'I don't know' without elaborating.",
        example="Bad: 'My last boss was terrible.'\nGood: 'I'm looking for a more collaborative environment where I can [positive goal].'\n\nBad: 'I don't know.'\nGood: 'I haven't encountered that specific situation, but here's how I'd approach it based on [related experience].'",
        impact="critical"
    ),
}


def generate_interview(
    job_title: str,
    job_tier: Literal["low", "mid", "high", "startup"],
    interview_round: Literal["phone_screen", "first_round", "technical", "final_round"]
) -> InterviewScenario:
    """Generate a mock interview scenario based on job and round."""
    
    # Select questions based on job tier and round
    selected_questions = []
    
    if interview_round == "phone_screen":
        # Phone screens are usually 30 min, 3-4 questions, basic screening
        selected_questions = [
            INTERVIEW_QUESTIONS["tell_me_about_yourself"],
            INTERVIEW_QUESTIONS["why_this_company"],
            INTERVIEW_QUESTIONS["questions_for_us"]
        ]
        time_limit = 30
        format_type = "one_on_one"
        personality = "friendly"
    
    elif interview_round == "first_round":
        # First round: 45-60 min, mix of behavioral and culture fit
        selected_questions = [
            INTERVIEW_QUESTIONS["tell_me_about_yourself"],
            INTERVIEW_QUESTIONS["why_this_company"],
            INTERVIEW_QUESTIONS["describe_project"],
            INTERVIEW_QUESTIONS["conflict_with_coworker"],
            INTERVIEW_QUESTIONS["questions_for_us"]
        ]
        time_limit = 60
        format_type = "one_on_one"
        personality = "neutral"
    
    elif interview_round == "technical":
        # Technical round: heavily focused on skills
        selected_questions = [
            INTERVIEW_QUESTIONS["technical_problem_solving"],
            INTERVIEW_QUESTIONS["describe_project"],
            INTERVIEW_QUESTIONS["handle_failure"],
            INTERVIEW_QUESTIONS["questions_for_us"]
        ]
        time_limit = 60
        format_type = "one_on_one"
        personality = "technical"
    
    else:  # final_round
        # Final round: hardest questions, culture fit, panel interview
        selected_questions = [
            INTERVIEW_QUESTIONS["why_should_we_hire_you"],
            INTERVIEW_QUESTIONS["greatest_weakness"],
            INTERVIEW_QUESTIONS["handle_failure"],
            INTERVIEW_QUESTIONS["conflict_with_coworker"],
            INTERVIEW_QUESTIONS["questions_for_us"]
        ]
        time_limit = 90
        format_type = "panel"
        personality = "intimidating"
    
    # Map tier to company type
    tier_to_company = {
        "low": "small",
        "mid": "medium",
        "high": "large",
        "startup": "startup"
    }
    
    return InterviewScenario(
        scenario_id=f"{job_tier}_{interview_round}",
        job_title=job_title,
        company_name="TechCorp",  # Could randomize
        company_tier=tier_to_company[job_tier],
        interview_round=interview_round,
        questions=selected_questions,
        time_limit_minutes=time_limit,
        interviewer_personality=personality,
        interview_format=format_type
    )


def evaluate_interview_response(
    question: InterviewQuestion,
    response: InterviewResponse,
    player_communication_skills: int = 50,
    player_confidence: int = 50
) -> Dict[str, any]:
    """Evaluate a single interview response.
    
    Returns score and feedback for the response.
    """
    
    base_score = 50
    
    # Evaluate based on response type
    type_scores = {
        "detailed_star": 90,
        "brief_answer": 60,
        "nervous_ramble": 30,
        "dodge": 20,
        "honest": 70
    }
    base_score = type_scores[response.response_type]
    
    # Bonuses for good practices
    if response.used_star_method and question.question_type == "behavioral":
        base_score += 10
    
    if response.used_specific_examples:
        base_score += 10
    
    if response.demonstrated_skill:
        base_score += 10
    
    if response.showed_enthusiasm:
        base_score += 5
    
    if response.avoided_red_flags:
        base_score += 10
    else:
        base_score -= 20  # Red flags are very bad
    
    # Adjust for player skills
    skill_modifier = (player_communication_skills + player_confidence) / 100
    final_score = int(base_score * skill_modifier)
    final_score = max(0, min(100, final_score))
    
    # Generate feedback
    feedback_points = []
    if response.used_star_method:
        feedback_points.append("Great use of STAR method!")
    elif question.question_type == "behavioral":
        feedback_points.append("Consider using STAR method for behavioral questions")
    
    if response.used_specific_examples:
        feedback_points.append("Specific examples strengthen your answer")
    else:
        feedback_points.append("Add specific examples to make your answer more compelling")
    
    if not response.avoided_red_flags:
        feedback_points.append(f"Watch out for red flag issues: {', '.join(question.red_flags)}")
    
    return {
        "score": final_score,
        "feedback": feedback_points,
        "key_criteria_met": sum([
            response.used_star_method,
            response.used_specific_examples,
            response.demonstrated_skill,
            response.avoided_red_flags
        ])
    }


def simulate_full_interview(
    scenario: InterviewScenario,
    player_communication_skills: int = 50,
    player_confidence: int = 50,
    player_preparation: Literal["none", "basic", "thorough"] = "basic"
) -> InterviewOutcome:
    """Simulate a complete interview.
    
    Returns outcome with detailed feedback.
    """
    
    # Simulate responses to each question
    question_scores = []
    behavioral_scores = []
    technical_scores = []
    
    for question in scenario.questions:
        # Simulate response quality based on player stats and prep
        prep_bonus = {"none": 0, "basic": 20, "thorough": 40}[player_preparation]
        
        # Simplified response generation
        base_quality = player_communication_skills + prep_bonus
        
        if base_quality >= 80:
            response_type = "detailed_star"
        elif base_quality >= 60:
            response_type = "honest"
        elif base_quality >= 40:
            response_type = "brief_answer"
        else:
            response_type = "nervous_ramble"
        
        response = InterviewResponse(
            response_type=response_type,
            response_text="[Player response]",
            used_star_method=base_quality >= 70 and question.question_type == "behavioral",
            used_specific_examples=base_quality >= 60,
            demonstrated_skill=base_quality >= 70,
            showed_enthusiasm=player_confidence >= 60,
            avoided_red_flags=base_quality >= 50
        )
        
        evaluation = evaluate_interview_response(question, response, player_communication_skills, player_confidence)
        question_scores.append(evaluation["score"])
        
        if question.question_type in ["behavioral", "situational"]:
            behavioral_scores.append(evaluation["score"])
        elif question.question_type == "technical":
            technical_scores.append(evaluation["score"])
    
    # Calculate overall score
    overall_score = int(sum(question_scores) / len(question_scores))
    behavioral_score = int(sum(behavioral_scores) / len(behavioral_scores)) if behavioral_scores else 0
    technical_score = int(sum(technical_scores) / len(technical_scores)) if technical_scores else 0
    communication_score = player_communication_skills
    culture_fit_score = player_confidence
    
    # Determine outcome
    success = overall_score >= 60
    
    if scenario.interview_round == "phone_screen":
        next_step = "first_round" if success else "rejected"
    elif scenario.interview_round == "first_round":
        next_step = "technical" if success else "rejected"
    elif scenario.interview_round == "technical":
        next_step = "final_round" if success else "rejected"
    else:  # final_round
        next_step = "offer" if success else "rejected"
    
    # Generate feedback
    strengths = []
    improvements = []
    
    if behavioral_score >= 70:
        strengths.append("Strong storytelling with STAR method")
    elif behavioral_score < 50:
        improvements.append("Practice STAR method for behavioral questions")
    
    if technical_score >= 70:
        strengths.append("Solid technical problem-solving approach")
    elif technical_score < 50:
        improvements.append("Brush up on technical fundamentals")
    
    if communication_score >= 70:
        strengths.append("Clear and confident communication")
    else:
        improvements.append("Work on communication skills and practice answering out loud")
    
    if player_confidence >= 70:
        strengths.append("Confident demeanor")
    else:
        improvements.append("Build confidence through mock interviews")
    
    if player_preparation == "thorough":
        strengths.append("Well-prepared with research on company")
    else:
        improvements.append("Research company more thoroughly before interview")
    
    if success:
        interviewer_feedback = f"We enjoyed speaking with you and think you'd be a good fit. We'd like to invite you to the {next_step.replace('_', ' ')}."
    else:
        rejection_reasons = {
            "phone_screen": "Didn't demonstrate enough interest in the company or role.",
            "first_round": "Behavioral responses lacked specific examples and impact.",
            "technical": "Struggled with technical problem-solving and explaining thought process.",
            "final_round": "While technically strong, we had concerns about culture fit and communication style."
        }
        interviewer_feedback = "Thank you for your time. Unfortunately, we've decided to move forward with other candidates."
        rejection_reason = rejection_reasons[scenario.interview_round]
    
    return InterviewOutcome(
        success=success,
        overall_score=overall_score,
        behavioral_score=behavioral_score,
        technical_score=technical_score,
        communication_score=communication_score,
        culture_fit_score=culture_fit_score,
        strengths=strengths,
        areas_for_improvement=improvements,
        interviewer_feedback=interviewer_feedback,
        next_step=next_step,
        rejection_reason=rejection_reason if not success else None
    )


def get_interview_prep_tip(tip_id: str) -> Optional[InterviewPrep]:
    """Get a specific interview prep tip."""
    return INTERVIEW_PREP_TIPS.get(tip_id)


def get_tips_by_category(category: str) -> List[InterviewPrep]:
    """Get all tips for a category."""
    return [tip for tip in INTERVIEW_PREP_TIPS.values() if tip.category == category]
