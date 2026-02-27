import React, { useState, useEffect } from 'react'
import { Player, attendClass } from '../utils/api'
import { getSemesterInfo, getCurrentPhase, formatSemesterDisplay } from '../utils/semesterUtils'
import { StorePanel } from './StorePanel'
import './GameBoard.css'

interface GameBoardProps {
    player: Player
    onLogout: () => void
}

interface Course {
    id: string
    title: string
    credits: number
    weekly_hours: number
}

interface ClassContent {
    course_id: string
    course_title: string
    topics: string[]
    lessons: any[]
    quizzes: any[]
    learning_outcomes: string[]
}

export function GameBoard({ player, onLogout }: GameBoardProps) {
    const [activeTab, setActiveTab] = useState<'stats' | 'finance' | 'planning' | 'academics' | 'store'>('stats')
    const [classContent, setClassContent] = useState<ClassContent | null>(null)
    const [selectedCourse, setSelectedCourse] = useState<string | null>(null)
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState<string | null>(null)

    // Course info modal state
    const [courseInfoModal, setCourseInfoModal] = useState<any | null>(null)
    const [courseInfoLoading, setCourseInfoLoading] = useState(false)

    // Semester exam state
    const [showSemesterExam, setShowSemesterExam] = useState(false)
    const [examStatus, setExamStatus] = useState<any | null>(null)
    const [activeExam, setActiveExam] = useState<any | null>(null)
    const [examQuestionIndex, setExamQuestionIndex] = useState(0)
    const [examAnswers, setExamAnswers] = useState<Record<number, string>>({})
    const [examSubmitted, setExamSubmitted] = useState(false)
    const [examScore, setExamScore] = useState<number | null>(null)

    // Quiz state
    const [activeQuiz, setActiveQuiz] = useState<any | null>(null)
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0)
    const [userAnswers, setUserAnswers] = useState<Record<number, string>>({})
    const [quizSubmitted, setQuizSubmitted] = useState(false)
    const [quizScore, setQuizScore] = useState<number | null>(null)

    // Sample courses for this semester (in a real app, this would come from the player's curriculum)
    const currentCourses: Course[] = [
        { id: 'cs101', title: 'Intro Programming', credits: 4, weekly_hours: 10 },
        { id: 'cs102', title: 'Data Structures', credits: 4, weekly_hours: 12 },
        { id: 'ba101', title: 'Intro Business', credits: 3, weekly_hours: 8 }
    ]

    const handleCourseInfo = async (courseId: string) => {
        try {
            setCourseInfoLoading(true)
            const response = await fetch(`/api/exams/course-info/${courseId}`)
            if (!response.ok) throw new Error('Failed to load course info')
            const data = await response.json()
            setCourseInfoModal(data)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to load course info')
        } finally {
            setCourseInfoLoading(false)
        }
    }

    const handleCloseCourseInfo = () => {
        setCourseInfoModal(null)
    }

    const handleLoadSemesterExamStatus = async () => {
        try {
            const response = await fetch(`/api/exams/semester-exam-status?player_id=${player.id}`)
            if (!response.ok) throw new Error('Failed to load exam status')
            const data = await response.json()
            setExamStatus(data)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to load exam status')
        }
    }

    const handleStartSemesterExam = async () => {
        try {
            setLoading(true)
            const response = await fetch(`/api/exams/semester-exam/generate?player_id=${player.id}&num_questions=5`, {
                method: 'POST'
            })
            if (!response.ok) {
                const errorData = await response.json()
                throw new Error(errorData.detail || 'Failed to generate exam')
            }
            const exam = await response.json()
            setActiveExam(exam)
            setExamQuestionIndex(0)
            setExamAnswers({})
            setExamSubmitted(false)
            setExamScore(null)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to start exam')
        } finally {
            setLoading(false)
        }
    }

    const handleExamAnswerSelect = (choiceId: string) => {
        setExamAnswers(prev => ({
            ...prev,
            [examQuestionIndex]: choiceId
        }))
    }

    const handleExamNextQuestion = () => {
        if (examQuestionIndex < activeExam.questions.length - 1) {
            setExamQuestionIndex(examQuestionIndex + 1)
        }
    }

    const handleExamPreviousQuestion = () => {
        if (examQuestionIndex > 0) {
            setExamQuestionIndex(examQuestionIndex - 1)
        }
    }

    const handleSubmitSemesterExam = async () => {
        try {
            const answers = activeExam.questions.map((q: any, idx: number) => ({
                question_id: q.id,
                chosen_choice_id: examAnswers[idx]
            }))

            const response = await fetch(`/api/exams/semester-exam/submit`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    player_id: player.id,
                    answers: answers
                })
            })

            if (!response.ok) throw new Error('Failed to submit exam')
            const result = await response.json()

            setExamSubmitted(true)
            setExamScore(result.exam_result.score_percent)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to submit exam')
        }
    }

    const handleProgressSemester = async () => {
        try {
            setLoading(true)
            const response = await fetch(`/api/exams/progress-semester?player_id=${player.id}`, {
                method: 'POST'
            })
            if (!response.ok) throw new Error('Failed to progress semester')

            setShowSemesterExam(false)
            setActiveExam(null)
            // Note: In a real app, you'd reload the player data here
            window.location.reload()
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to progress semester')
        } finally {
            setLoading(false)
        }
    }

    const handleAttendClass = async (courseId: string) => {
        try {
            setLoading(true)
            setError(null)
            const content = await attendClass(courseId)
            setClassContent(content)
            setSelectedCourse(courseId)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to attend class')
        } finally {
            setLoading(false)
        }
    }

    const handleStartQuiz = (quiz: any) => {
        setActiveQuiz(quiz)
        setCurrentQuestionIndex(0)
        setUserAnswers({})
        setQuizSubmitted(false)
        setQuizScore(null)
    }

    const handleAnswerSelect = (answer: string) => {
        setUserAnswers(prev => ({
            ...prev,
            [currentQuestionIndex]: answer
        }))
    }

    const handleNextQuestion = () => {
        if (currentQuestionIndex < activeQuiz.questions.length - 1) {
            setCurrentQuestionIndex(currentQuestionIndex + 1)
        }
    }

    const handlePreviousQuestion = () => {
        if (currentQuestionIndex > 0) {
            setCurrentQuestionIndex(currentQuestionIndex - 1)
        }
    }

    const handleSubmitQuiz = async () => {
        let correctCount = 0
        activeQuiz.questions.forEach((question: any, index: number) => {
            if (userAnswers[index] === question.correct_answer) {
                correctCount++
            }
        })
        const score = Math.round((correctCount / activeQuiz.questions.length) * 100)
        setQuizScore(score)
        setQuizSubmitted(true)

        // If passed, mark course as completed
        if (score >= 70) {
            try {
                const response = await fetch(`/api/exams/course-complete`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        player_id: player.id,
                        course_id: activeQuiz.course_id || selectedCourse
                    })
                })
                if (!response.ok) throw new Error('Failed to mark course complete')
            } catch (err) {
                console.warn('Failed to mark course complete:', err)
            }
        }
    }

    const handleCloseQuiz = () => {
        setActiveQuiz(null)
        setCurrentQuestionIndex(0)
        setUserAnswers({})
        setQuizSubmitted(false)
        setQuizScore(null)
    }

    const semesterInfo = getSemesterInfo(player.semester)
    const phaseInfo = getCurrentPhase(player.semester)

    return (
        <div className="game-container">
            <header className="game-header">
                <div className="header-content">
                    <h1>🎮 Life Sprint</h1>
                    <div className="player-info">
                        <span className="player-name">{player.name}</span>
                        <div className="semester-info">
                            <span className="player-semester">{semesterInfo.displayName}</span>
                            <span className="semester-dates">{semesterInfo.monthRange}</span>
                            <span className={`phase-badge ${phaseInfo.phase}`}>{phaseInfo.description}</span>
                        </div>
                    </div>
                </div>
                <button onClick={onLogout} className="logout-btn">Logout</button>
            </header>

            <div className="game-content">
                <nav className="game-nav">
                    <button
                        className={`nav-btn ${activeTab === 'stats' ? 'active' : ''}`}
                        onClick={() => setActiveTab('stats')}
                    >
                        📊 Stats
                    </button>
                    <button
                        className={`nav-btn ${activeTab === 'finance' ? 'active' : ''}`}
                        onClick={() => setActiveTab('finance')}
                    >
                        💰 Finance
                    </button>
                    <button
                        className={`nav-btn ${activeTab === 'planning' ? 'active' : ''}`}
                        onClick={() => setActiveTab('planning')}
                    >
                        📅 Planning
                    </button>
                    <button
                        className={`nav-btn ${activeTab === 'academics' ? 'active' : ''}`}
                        onClick={() => setActiveTab('academics')}
                    >
                        🎓 Academics
                    </button>
                    <button
                        className={`nav-btn ${activeTab === 'store' ? 'active' : ''}`}
                        onClick={() => setActiveTab('store')}
                    >
                        🛍️ Store
                    </button>
                </nav>

                <main className="game-main">
                    {activeTab === 'stats' && (
                        <section className="tab-content">
                            <h2>Your Stats</h2>
                            <div className="stats-grid">
                                <div className="stat-card">
                                    <h3>GPA</h3>
                                    <p className="stat-value">{player.stats?.gpa?.toFixed(2) || 'N/A'}</p>
                                </div>
                                <div className="stat-card">
                                    <h3>Stress</h3>
                                    <p className="stat-value">{player.stats?.stress?.toFixed(0) || 'N/A'}%</p>
                                </div>
                                <div className="stat-card">
                                    <h3>Network</h3>
                                    <p className="stat-value">{player.stats?.network?.toFixed(0) || 'N/A'}</p>
                                </div>
                                <div className="stat-card">
                                    <h3>Health</h3>
                                    <p className="stat-value">{player.stats?.health?.toFixed(0) || 'N/A'}%</p>
                                </div>
                            </div>
                        </section>
                    )}

                    {activeTab === 'finance' && (
                        <section className="tab-content">
                            <h2>Financial Status</h2>
                            <div className="finance-info">
                                <div className="info-card">
                                    <label>Cash Balance</label>
                                    <p className="amount">${player.finance?.balance?.toFixed(2) || '0.00'}</p>
                                </div>
                                <div className="info-card">
                                    <label>Monthly Expenses</label>
                                    <p className="amount">${player.finance?.monthly_expenses?.toFixed(2) || '0.00'}</p>
                                </div>
                                <div className="info-card">
                                    <label>Tuition (Per Semester)</label>
                                    <p className="amount">${player.finance?.tuition_per_semester?.toFixed(2) || '0.00'}</p>
                                </div>
                                <div className="info-card">
                                    <label>Scholarship</label>
                                    <p className="amount">${player.finance?.scholarship_per_semester?.toFixed(2) || '0.00'}</p>
                                </div>
                            </div>
                        </section>
                    )}

                    {activeTab === 'planning' && (
                        <section className="tab-content">
                            <h2>Semester Planning</h2>
                            <div className="planning-info">
                                <p>Plan your semester activities and time allocation.</p>
                                {player.plan ? (
                                    <div className="plan-details">
                                        <p>Current plan is active</p>
                                    </div>
                                ) : (
                                    <div className="no-plan">
                                        <p>No plan created yet. Create one to get started!</p>
                                    </div>
                                )}
                            </div>
                        </section>
                    )}

                    {activeTab === 'academics' && (
                        <section className="tab-content">
                            <h2>🎓 Academics</h2>

                            {error && (
                                <div className="error-message" style={{ marginBottom: '20px' }}>
                                    {error}
                                </div>
                            )}

                            <div className="academics-container">
                                <div className="academics-sidebar">
                                    <h3>Your Info</h3>
                                    <div className="info-card">
                                        <label>College</label>
                                        <p className="detail-value">{player.college_id || 'Not selected'}</p>
                                    </div>
                                    <div className="info-card">
                                        <label>Major</label>
                                        <p className="detail-value">{player.major_id || 'Not selected'}</p>
                                    </div>
                                    <div className="info-card">
                                        <label>Semester</label>
                                        <p className="detail-value">{semesterInfo.displayName}</p>
                                    </div>
                                    <div className="info-card">
                                        <label>Period</label>
                                        <p className="detail-value">{semesterInfo.monthRange}</p>
                                    </div>
                                    <div className="info-card">
                                        <label>GPA</label>
                                        <p className="detail-value">{player.stats?.gpa?.toFixed(2) || 'N/A'}</p>
                                    </div>
                                </div>

                                <div className="academics-main">
                                    {!classContent ? (
                                        <div>
                                            <h3>{semesterInfo.displayName} Courses</h3>
                                            {!phaseInfo.canAttendClasses && (
                                                <div className="phase-notice">
                                                    <p>⏱️ {phaseInfo.description}</p>
                                                    <p className="notice-sub">Classes are not in session. Use this time for work, internships, or skill development!</p>
                                                </div>
                                            )}
                                            <div className="courses-grid">
                                                {currentCourses.map(course => (
                                                    <div
                                                        key={course.id}
                                                        className={`course-card ${selectedCourse === course.id ? 'selected' : ''} ${!phaseInfo.canAttendClasses ? 'disabled' : ''}`}
                                                        onClick={() => phaseInfo.canAttendClasses && handleAttendClass(course.id)}
                                                    >
                                                        <div className="course-header">
                                                            <h4>{course.title}</h4>
                                                            <span className="course-id">{course.id}</span>
                                                        </div>
                                                        <p className="course-info">
                                                            {course.credits} credits | {course.weekly_hours} hrs/week
                                                        </p>
                                                        <div className="course-buttons">
                                                            <button
                                                                className="btn-attend"
                                                                disabled={loading || !phaseInfo.canAttendClasses}
                                                                title={!phaseInfo.canAttendClasses ? 'Classes not in session' : 'Click to attend class'}
                                                            >
                                                                {loading && selectedCourse === course.id ? 'Loading...' : !phaseInfo.canAttendClasses ? 'Break Period' : 'Attend Class'}
                                                            </button>
                                                            <button
                                                                className="btn-course-info"
                                                                onClick={(e) => {
                                                                    e.stopPropagation()
                                                                    handleCourseInfo(course.id)
                                                                }}
                                                                title="View course information"
                                                            >
                                                                ℹ️ Info
                                                            </button>
                                                        </div>
                                                    </div>
                                                ))}
                                            </div>

                                            {/* Semester Exam Button */}
                                            <div className="semester-exam-section" style={{ marginTop: '30px', paddingTop: '20px', borderTop: '1px solid #ddd' }}>
                                                <h3>End of Semester Exam</h3>
                                                <button
                                                    className="btn-nav btn-exam"
                                                    onClick={() => {
                                                        setShowSemesterExam(true)
                                                        handleLoadSemesterExamStatus()
                                                    }}
                                                    style={{ marginTop: '10px' }}
                                                >
                                                    📝 View Exam Status
                                                </button>
                                            </div>
                                        </div>
                                    ) : (
                                        <div className="class-content">
                                            <div className="class-header">
                                                <button
                                                    className="btn-back"
                                                    onClick={() => {
                                                        setClassContent(null)
                                                        setSelectedCourse(null)
                                                    }}
                                                >
                                                    ← Back to Courses
                                                </button>
                                                <h3>{classContent.course_title}</h3>
                                            </div>

                                            <div className="class-sections">
                                                {/* Topics */}
                                                <section className="class-section">
                                                    <h4>📚 Topics Covered</h4>
                                                    <ul className="topics-list">
                                                        {classContent.topics.map((topic, idx) => (
                                                            <li key={idx}>{topic}</li>
                                                        ))}
                                                    </ul>
                                                </section>

                                                {/* Learning Outcomes */}
                                                <section className="class-section">
                                                    <h4>🎯 Learning Outcomes</h4>
                                                    <ul className="outcomes-list">
                                                        {classContent.learning_outcomes.map((outcome, idx) => (
                                                            <li key={idx}>{outcome}</li>
                                                        ))}
                                                    </ul>
                                                </section>

                                                {/* Lessons */}
                                                <section className="class-section">
                                                    <h4>📖 Lessons ({classContent.lessons.length})</h4>
                                                    <div className="lessons-list">
                                                        {classContent.lessons.map(lesson => (
                                                            <div key={lesson.id} className="lesson-item">
                                                                <div className="lesson-header">
                                                                    <span className="lesson-title">{lesson.title}</span>
                                                                    <span className="lesson-time">{lesson.duration_minutes} min</span>
                                                                </div>
                                                                <p className="lesson-description">{lesson.content}</p>
                                                                <p className="lesson-topic">Topic: {lesson.topic}</p>
                                                            </div>
                                                        ))}
                                                    </div>
                                                </section>

                                                {/* Quizzes */}
                                                <section className="class-section">
                                                    <h4>✏️ Quizzes ({classContent.quizzes.length})</h4>
                                                    <div className="quizzes-list">
                                                        {classContent.quizzes.map(quiz => (
                                                            <div key={quiz.id} className="quiz-item">
                                                                <div className="quiz-header">
                                                                    <span className="quiz-title">{quiz.title}</span>
                                                                    <span className="quiz-score">Pass: {quiz.passing_score}%</span>
                                                                </div>
                                                                <p className="quiz-topic">Topic: {quiz.topic}</p>
                                                                <p className="quiz-count">{quiz.questions.length} questions</p>
                                                                <button
                                                                    className="btn-quiz"
                                                                    onClick={() => handleStartQuiz(quiz)}
                                                                >
                                                                    Start Quiz
                                                                </button>
                                                            </div>
                                                        ))}
                                                    </div>
                                                </section>
                                            </div>
                                        </div>
                                    )}
                                </div>
                            </div>
                        </section>
                    )}
                </main>
            </div>

            <footer className="game-footer">
                <p>College: {player.college_id} | Major: {player.major_id} | Age: {player.age}</p>
            </footer>

            {/* Quiz Modal */}
            {activeQuiz && (
                <div className="quiz-modal-overlay">
                    <div className="quiz-modal">
                        <div className="quiz-modal-header">
                            <h2>{activeQuiz.title}</h2>
                            <button className="close-quiz" onClick={handleCloseQuiz}>✕</button>
                        </div>

                        {!quizSubmitted ? (
                            <>
                                <div className="quiz-progress">
                                    <span>Question {currentQuestionIndex + 1} of {activeQuiz.questions.length}</span>
                                    <div className="progress-bar">
                                        <div
                                            className="progress-fill"
                                            style={{ width: `${((currentQuestionIndex + 1) / activeQuiz.questions.length) * 100}%` }}
                                        />
                                    </div>
                                </div>

                                <div className="quiz-question">
                                    <h3>{activeQuiz.questions[currentQuestionIndex].question}</h3>
                                    <div className="quiz-options">
                                        {activeQuiz.questions[currentQuestionIndex].options.map((option: string, idx: number) => (
                                            <button
                                                key={idx}
                                                className={`quiz-option ${userAnswers[currentQuestionIndex] === option ? 'selected' : ''}`}
                                                onClick={() => handleAnswerSelect(option)}
                                            >
                                                {option}
                                            </button>
                                        ))}
                                    </div>
                                </div>

                                <div className="quiz-navigation">
                                    <button
                                        onClick={handlePreviousQuestion}
                                        disabled={currentQuestionIndex === 0}
                                        className="btn-nav"
                                    >
                                        Previous
                                    </button>

                                    {currentQuestionIndex < activeQuiz.questions.length - 1 ? (
                                        <button
                                            onClick={handleNextQuestion}
                                            disabled={!userAnswers[currentQuestionIndex]}
                                            className="btn-nav btn-primary"
                                        >
                                            Next
                                        </button>
                                    ) : (
                                        <button
                                            onClick={handleSubmitQuiz}
                                            disabled={Object.keys(userAnswers).length !== activeQuiz.questions.length}
                                            className="btn-nav btn-submit"
                                        >
                                            Submit Quiz
                                        </button>
                                    )}
                                </div>
                            </>
                        ) : (
                            <div className="quiz-results">
                                <h3>Quiz Complete!</h3>
                                <div className={`score-display ${quizScore! >= activeQuiz.passing_score ? 'passed' : 'failed'}`}>
                                    <span className="score-number">{quizScore}%</span>
                                    <span className="score-label">
                                        {quizScore! >= activeQuiz.passing_score ? '✅ Passed!' : '❌ Failed'}
                                    </span>
                                </div>
                                <p className="passing-score">Passing score: {activeQuiz.passing_score}%</p>

                                <div className="quiz-review">
                                    <h4>Review Your Answers</h4>
                                    {activeQuiz.questions.map((question: any, idx: number) => (
                                        <div key={idx} className="review-item">
                                            <p className="review-question">
                                                <strong>Q{idx + 1}:</strong> {question.question}
                                            </p>
                                            <p className={`review-answer ${userAnswers[idx] === question.correct_answer ? 'correct' : 'incorrect'}`}>
                                                Your answer: {userAnswers[idx]}
                                                {userAnswers[idx] === question.correct_answer ? ' ✅' : ' ❌'}
                                            </p>
                                            {userAnswers[idx] !== question.correct_answer && (
                                                <p className="review-correct">
                                                    Correct answer: {question.correct_answer}
                                                </p>
                                            )}
                                        </div>
                                    ))}
                                </div>

                                <button className="btn-close-results" onClick={handleCloseQuiz}>
                                    Close
                                </button>
                            </div>
                        )}
                    </div>
                </div>
            )}

            {/* Course Info Modal */}
            {courseInfoModal && (
                <div className="modal-overlay" onClick={handleCloseCourseInfo}>
                    <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                        <div className="modal-header">
                            <h2>{courseInfoModal.title}</h2>
                            <button className="close-btn" onClick={handleCloseCourseInfo}>✕</button>
                        </div>

                        <div className="modal-body">
                            <div className="course-info-grid">
                                <div className="info-item">
                                    <label>Credits</label>
                                    <p>{courseInfoModal.credits}</p>
                                </div>
                                <div className="info-item">
                                    <label>Difficulty</label>
                                    <p>{'⭐'.repeat(courseInfoModal.difficulty / 2)}</p>
                                </div>
                                <div className="info-item">
                                    <label>Weekly Hours</label>
                                    <p>{courseInfoModal.weekly_hours} hours</p>
                                </div>
                                <div className="info-item">
                                    <label>Lessons</label>
                                    <p>{courseInfoModal.lessons_count || 'N/A'}</p>
                                </div>
                            </div>

                            <div className="info-section">
                                <h3>About This Course</h3>
                                <p>{courseInfoModal.description || 'No description available'}</p>
                            </div>

                            {courseInfoModal.skills && courseInfoModal.skills.length > 0 && (
                                <div className="info-section">
                                    <h3>Skills You'll Learn</h3>
                                    <div className="skills-list">
                                        {courseInfoModal.skills.map((skill: string, idx: number) => (
                                            <span key={idx} className="skill-badge">{skill}</span>
                                        ))}
                                    </div>
                                </div>
                            )}

                            {courseInfoModal.topics && courseInfoModal.topics.length > 0 && (
                                <div className="info-section">
                                    <h3>Topics Covered</h3>
                                    <ul>
                                        {courseInfoModal.topics.map((topic: string, idx: number) => (
                                            <li key={idx}>{topic}</li>
                                        ))}
                                    </ul>
                                </div>
                            )}
                        </div>

                        <div className="modal-footer">
                            <button className="btn-nav" onClick={handleCloseCourseInfo}>Close</button>
                        </div>
                    </div>
                </div>
            )}

            {/* Semester Exam Modal */}
            {showSemesterExam && (
                <div className="modal-overlay" onClick={() => setShowSemesterExam(false)}>
                    <div className="modal-content large" onClick={(e) => e.stopPropagation()}>
                        <div className="modal-header">
                            <h2>📝 Semester Exam</h2>
                            <button className="close-btn" onClick={() => setShowSemesterExam(false)}>✕</button>
                        </div>

                        <div className="modal-body">
                            {!activeExam ? (
                                <div className="exam-status">
                                    {examStatus ? (
                                        <>
                                            <div className="status-info">
                                                <h3>Exam Requirements</h3>
                                                <div className="progress-item">
                                                    <label>Courses Completed</label>
                                                    <div className="progress-bar">
                                                        <div
                                                            className="progress-fill"
                                                            style={{ width: `${(examStatus.completed_courses / examStatus.total_courses) * 100}%` }}
                                                        />
                                                    </div>
                                                    <p className="progress-text">
                                                        {examStatus.completed_courses}/{examStatus.total_courses} courses
                                                    </p>
                                                </div>
                                            </div>

                                            {examStatus.can_take_exam ? (
                                                <div className="exam-ready">
                                                    <p className="success-message">✅ You're ready to take the semester exam!</p>
                                                    <p>The exam will have 5 questions covering all courses from this semester.</p>
                                                    <button
                                                        className="btn-nav btn-primary"
                                                        onClick={handleStartSemesterExam}
                                                        disabled={loading}
                                                    >
                                                        {loading ? 'Generating Exam...' : 'Start Exam'}
                                                    </button>
                                                </div>
                                            ) : (
                                                <div className="exam-blocked">
                                                    <p className="warning-message">⏳ Complete all courses first</p>
                                                    <p>You need to complete {examStatus.total_courses - examStatus.completed_courses} more course(s) to take the exam.</p>
                                                </div>
                                            )}
                                        </>
                                    ) : (
                                        <p>Loading exam status...</p>
                                    )}
                                </div>
                            ) : !examSubmitted ? (
                                <>
                                    <div className="exam-progress">
                                        <span>Question {examQuestionIndex + 1} of {activeExam.questions.length}</span>
                                        <div className="progress-bar">
                                            <div
                                                className="progress-fill"
                                                style={{ width: `${((examQuestionIndex + 1) / activeExam.questions.length) * 100}%` }}
                                            />
                                        </div>
                                    </div>

                                    {activeExam.questions[examQuestionIndex] && (
                                        <div className="exam-question">
                                            <h4>{activeExam.questions[examQuestionIndex].text}</h4>
                                            <div className="exam-choices">
                                                {activeExam.questions[examQuestionIndex].choices.map((choice: any) => (
                                                    <label key={choice.id} className="exam-choice">
                                                        <input
                                                            type="radio"
                                                            name="exam-choice"
                                                            value={choice.id}
                                                            checked={examAnswers[examQuestionIndex] === choice.id}
                                                            onChange={() => handleExamAnswerSelect(choice.id)}
                                                        />
                                                        <span>{choice.text}</span>
                                                    </label>
                                                ))}
                                            </div>
                                        </div>
                                    )}

                                    <div className="exam-navigation">
                                        <button
                                            onClick={handleExamPreviousQuestion}
                                            disabled={examQuestionIndex === 0}
                                            className="btn-nav"
                                        >
                                            Previous
                                        </button>

                                        {examQuestionIndex < activeExam.questions.length - 1 ? (
                                            <button
                                                onClick={handleExamNextQuestion}
                                                disabled={!examAnswers[examQuestionIndex]}
                                                className="btn-nav btn-primary"
                                            >
                                                Next
                                            </button>
                                        ) : (
                                            <button
                                                onClick={handleSubmitSemesterExam}
                                                disabled={Object.keys(examAnswers).length !== activeExam.questions.length}
                                                className="btn-nav btn-submit"
                                            >
                                                Submit Exam
                                            </button>
                                        )}
                                    </div>
                                </>
                            ) : (
                                <div className="exam-results">
                                    <h3>Exam Results</h3>
                                    <div className={`score-display ${examScore! >= 70 ? 'passed' : 'failed'}`}>
                                        <span className="score-number">{examScore}%</span>
                                        <span className="score-label">
                                            {examScore! >= 70 ? '✅ Passed!' : '❌ Failed'}
                                        </span>
                                    </div>
                                    <p className="passing-score">Passing score: 70%</p>

                                    {examScore! >= 70 && (
                                        <div className="progress-section">
                                            <p className="success-message">Congratulations! You may now progress to the next semester.</p>
                                            <button
                                                className="btn-nav btn-primary"
                                                onClick={handleProgressSemester}
                                                disabled={loading}
                                            >
                                                {loading ? 'Progressing...' : '➡️ Go to Next Semester'}
                                            </button>
                                        </div>
                                    )}
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            )}
        </div>
    )
}
