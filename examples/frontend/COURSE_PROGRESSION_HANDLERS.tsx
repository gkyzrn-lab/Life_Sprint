// File: life-sprint-frontend/src/components/GameBoard.tsx
// Add these handler functions after the existing handlers

// ==================== COURSE INFO HANDLERS ====================

const [courseInfoLoading, setCourseInfoLoading] = useState(false)

const handleCourseInfo = async (courseId: string) => {
    try {
        setCourseInfoLoading(true)
        const response = await fetch(`/api/exams/course-info/${courseId}`)
        if (!response.ok) throw new Error('Failed to fetch course info')
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

// ==================== SEMESTER EXAM HANDLERS ====================

const handleLoadSemesterExamStatus = async () => {
    try {
        setLoading(true)
        const response = await fetch(`/api/exams/semester-exam-status?player_id=${player.id}`)
        if (!response.ok) throw new Error('Failed to load exam status')
        const data = await response.json()
        setExamStatus(data)
    } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load exam status')
    } finally {
        setLoading(false)
    }
}

const handleStartSemesterExam = async () => {
    try {
        setLoading(true)
        const response = await fetch(`/api/exams/semester-exam/generate?player_id=${player.id}&num_questions=5`, {
            method: 'POST'
        })
        if (!response.ok) throw new Error('Failed to generate exam')
        const data = await response.json()
        setActiveExam(data)
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
        setLoading(true)

        // Convert answers to exam format
        const answers = activeExam.questions.map((q: any, idx: number) => ({
            question_id: q.id,
            chosen_choice_id: examAnswers[idx]
        }))

        const response = await fetch('/api/exams/semester-exam/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                player_id: player.id,
                answers: answers
            })
        })

        if (!response.ok) throw new Error('Failed to submit exam')
        const data = await response.json()

        // Calculate score
        const score = Math.round(data.exam_result.score_percent)
        setExamScore(score)
        setExamSubmitted(true)

        // Update player stats if passed
        if (data.passed && data.updated_player) {
            // Parent component should update player state here
        }
    } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to submit exam')
    } finally {
        setLoading(false)
    }
}

const handleProgressSemester = async () => {
    try {
        setLoading(true)
        const response = await fetch(`/api/exams/progress-semester?player_id=${player.id}`, {
            method: 'POST'
        })

        if (!response.ok) throw new Error('Failed to progress semester')
        const data = await response.json()

        // Close modals
        setShowSemesterExam(false)
        setActiveExam(null)
        setExamStatus(null)

        // Parent component should update player state here
        // This typically triggers a page refresh or state update
    } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to progress to next semester')
    } finally {
        setLoading(false)
    }
}
