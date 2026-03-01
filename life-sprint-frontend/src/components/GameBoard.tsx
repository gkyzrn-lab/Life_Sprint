import { useState, useEffect, useRef } from 'react'
import {
    Player,
    attendClass,
    getMiniGamesForCourse,
    getMiniGameDetails,
    getLessonGame,
    markMiniGameSeen,
    submitLessonGame,
    submitMiniGame,
    prefetchAnalyticsData,
    prefetchFinanceData,
    prefetchStoreData,
    MiniGameSummary,
    MiniGameDetails,
    LessonGameDetails,
    LessonGameQuestion,
    MiniGameSubmissionResult,
    GameRecommendation,
    getSemesterExamStatus,
    generateSemesterExam,
    submitSemesterExam,
    advanceSemester,
} from '../utils/api'
import { getSemesterInfo, getCurrentPhase } from '../utils/semesterUtils'
import LifeReadinessPanel from './LifeReadinessPanel'
import VisualExperiencePanel from './VisualExperiencePanel'
import FinanceToolsPanel from './FinanceToolsPanel'
import { StorePanel } from './StorePanel'
import SemesterSummaryScreen from './SemesterSummaryScreen'
import './GameBoard.css'

interface GameBoardProps {
    player: Player
    onLogout: () => void
    onPlayerUpdate: (player: Player) => void
    onRefreshPlayer: (playerId: string) => Promise<Player | null>
}

type GameTab = 'stats' | 'finance' | 'planning' | 'academics' | 'visual' | 'analytics' | 'store'

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

interface LessonConceptGameResult {
    scorePercent: number
    passed: boolean
    correctCount: number
    totalQuestions: number
}

export function GameBoard({ player, onLogout, onPlayerUpdate, onRefreshPlayer }: GameBoardProps) {
    const [activeTab, setActiveTab] = useState<GameTab>('stats')
    const [tabTransitioning, setTabTransitioning] = useState(false)
    const [classContent, setClassContent] = useState<ClassContent | null>(null)
    const [selectedCourse, setSelectedCourse] = useState<string | null>(null)
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState<string | null>(null)
    const [currentCourses, setCurrentCourses] = useState<Course[]>([])
    const [coursesLoading, setCoursesLoading] = useState(false)

    // Course info modal state
    const [courseInfoModal, setCourseInfoModal] = useState<any | null>(null)
    const [, setCourseInfoLoading] = useState(false)

    // Semester exam state
    const [showSemesterExam, setShowSemesterExam] = useState(false)
    const [examStatus, setExamStatus] = useState<any | null>(null)
    const [activeExam, setActiveExam] = useState<any | null>(null)
    const [examQuestionIndex, setExamQuestionIndex] = useState(0)
    const [examAnswers, setExamAnswers] = useState<Record<number, string>>({})
    const [examSubmitted, setExamSubmitted] = useState(false)
    const [examScore, setExamScore] = useState<number | null>(null)
    const [semesterSummary, setSemesterSummary] = useState<any | null>(null)
    const [showSemesterSummary, setShowSemesterSummary] = useState(false)

    // Quiz state
    const [activeQuiz, setActiveQuiz] = useState<any | null>(null)
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0)
    const [userAnswers, setUserAnswers] = useState<Record<number, string>>({})
    const [quizSubmitted, setQuizSubmitted] = useState(false)
    const [quizScore, setQuizScore] = useState<number | null>(null)

    // Mini-game state
    const [courseMiniGames, setCourseMiniGames] = useState<MiniGameSummary[]>([])
    const [miniGamesLoading, setMiniGamesLoading] = useState(false)
    const [activeMiniGame, setActiveMiniGame] = useState<MiniGameDetails | null>(null)
    const [miniGameQuestionIndex, setMiniGameQuestionIndex] = useState(0)
    const [miniGameAnswers, setMiniGameAnswers] = useState<Record<number, number>>({})
    const [miniGameSubmitted, setMiniGameSubmitted] = useState(false)
    const [miniGameResult, setMiniGameResult] = useState<MiniGameSubmissionResult | null>(null)
    const [miniGameStartTime, setMiniGameStartTime] = useState<number | null>(null)
    const [activeLesson, setActiveLesson] = useState<any | null>(null)
    const [activeLessonGame, setActiveLessonGame] = useState<LessonGameDetails | null>(null)
    const [lessonGameLoading, setLessonGameLoading] = useState(false)
    const [lessonGameError, setLessonGameError] = useState<string | null>(null)
    const [lessonGameQuestionIndex, setLessonGameQuestionIndex] = useState(0)
    const [lessonGameAnswers, setLessonGameAnswers] = useState<Record<number, number>>({})
    const [lessonGameSubmitted, setLessonGameSubmitted] = useState(false)
    const [lessonGameResult, setLessonGameResult] = useState<LessonConceptGameResult | null>(null)
    const [pendingRecommendedGameId, setPendingRecommendedGameId] = useState<string | null>(null)
    const [lifeMomentNotice, setLifeMomentNotice] = useState<string | null>(null)
    const [pendingLifeMoment, setPendingLifeMoment] = useState<{
        headline: string
        scenario: string
        stakes: string
        game: MiniGameDetails
    } | null>(null)
    const [planningDraft, setPlanningDraft] = useState('')
    const [planningDraftStatus, setPlanningDraftStatus] = useState<'idle' | 'saving' | 'saved'>('idle')
    const [debouncedSelectedCourse, setDebouncedSelectedCourse] = useState<string | null>(null)
    const [sortedMiniGames, setSortedMiniGames] = useState<MiniGameSummary[]>([])
    const randomMiniGameTimerRef = useRef<number | null>(null)
    const recommendedLaunchTimerRef = useRef<number | null>(null)
    const randomMomentsByCourseRef = useRef<Record<string, number>>({})
    const seenMiniGamesByCourseRef = useRef<Record<string, Set<string>>>({})
    const randomTriggerAttemptsByCourseRef = useRef<Record<string, number>>({})
    const miniGameOutcomesByCourseRef = useRef<Record<string, { passed: number; failed: number }>>({})
    const lastRandomTriggerAtRef = useRef<number>(0)
    const classSessionStartedAtRef = useRef<number>(0)
    const lastMiniGameClosedAtRef = useRef<number>(0)
    const MAX_RANDOM_MOMENTS_PER_COURSE = 2
    const prefetchedTabsRef = useRef<Set<GameTab>>(new Set())

    const clampNumber = (value: number, min: number, max: number): number => {
        return Math.max(min, Math.min(max, value))
    }

    const generateFallbackLessonQuestions = (lesson: any): LessonGameQuestion[] => {
        const topic = lesson?.topic || 'this concept'
        const title = lesson?.title || 'the lesson'
        const content = (lesson?.content || '').toString()
        const summary = content.length > 90 ? `${content.slice(0, 90)}...` : content

        return [
            {
                id: `${lesson?.id || 'lesson'}-q1`,
                prompt: `What is the main focus of "${title}"?`,
                options: [
                    `Understanding ${topic} through examples and practical reasoning`,
                    'Memorizing facts without application',
                    'Skipping fundamentals and jumping to advanced topics',
                    'Avoiding feedback and concept checks',
                ],
                correct_option_index: 0,
                explanation: `This lesson emphasizes applying ${topic} clearly, not just memorizing terms.`,
                learning_point: `Core concept clarity in ${topic}`,
            },
            {
                id: `${lesson?.id || 'lesson'}-q2`,
                prompt: `Which approach best helps you retain this lesson concept?`,
                options: [
                    'Connect the concept to a real scenario and explain it in your own words',
                    'Read once and move on quickly',
                    'Ignore examples and only look at headings',
                    'Wait until exam week to review',
                ],
                correct_option_index: 0,
                explanation: 'Active recall + real-world connection improves learning and transfer.',
                learning_point: 'Active learning beats passive exposure.',
            },
            {
                id: `${lesson?.id || 'lesson'}-q3`,
                prompt: `Based on this lesson summary: "${summary || topic}", what should you do next?`,
                options: [
                    `Practice one short application task related to ${topic}`,
                    'Skip practice and rely on intuition',
                    'Avoid reviewing mistakes',
                    'Only focus on unrelated topics',
                ],
                correct_option_index: 0,
                explanation: 'Immediate small practice cements concept understanding.',
                learning_point: 'Short practice loops build long-term mastery.',
            },
        ]
    }

    const normalizeLessonGame = (lesson: any, payload: LessonGameDetails | null): LessonGameDetails => {
        const contentQuestions = Array.isArray(payload?.content?.questions)
            ? payload?.content?.questions
            : []

        const normalizedQuestions: LessonGameQuestion[] = contentQuestions
            .filter((q: any) => q && Array.isArray(q.options) && q.options.length > 1)
            .map((q: any, idx: number) => ({
                id: q.id || `${lesson?.id || 'lesson'}-api-q${idx + 1}`,
                prompt: q.prompt || q.question || `Concept Check ${idx + 1}`,
                options: q.options,
                correct_option_index: Number.isInteger(q.correct_option_index) ? q.correct_option_index : 0,
                explanation: q.explanation || 'Review the concept and try applying it to a practical case.',
                learning_point: q.learning_point || 'Concept reinforcement',
            }))

        const questions = normalizedQuestions.length >= 2
            ? normalizedQuestions
            : generateFallbackLessonQuestions(lesson)

        return {
            game_id: payload?.game_id || `lesson_${lesson?.id || 'concept'}_challenge`,
            lesson_id: lesson?.id || payload?.lesson_id || 'lesson',
            title: payload?.title || `Concept Challenge: ${lesson?.title || 'Lesson'}`,
            game_type: payload?.game_type || 'concept_check',
            description: payload?.description || `Interactive checks to help you understand ${lesson?.topic || 'the lesson'} better.`,
            objectives: payload?.objectives || [
                `Understand the core idea of ${lesson?.topic || 'the lesson'}`,
                'Apply the concept in realistic scenarios',
                'Build confidence before moving to quizzes',
            ],
            difficulty: payload?.difficulty || 'beginner',
            estimated_duration_minutes: payload?.estimated_duration_minutes || 4,
            content: payload?.content,
            questions,
        }
    }

    const getSessionStage = (courseId: string): 'early' | 'mid' | 'finals' => {
        const startedAt = classSessionStartedAtRef.current || Date.now()
        const elapsedMs = Date.now() - startedAt
        const momentsSeen = randomMomentsByCourseRef.current[courseId] || 0

        if (elapsedMs < 90_000 && momentsSeen === 0) return 'early'
        if (elapsedMs < 5 * 60_000) return 'mid'
        return 'finals'
    }

    const getPacingConfig = (stage: 'early' | 'mid' | 'finals') => {
        const phase = getCurrentPhase(player.semester).phase

        const byStage = {
            early: { maxMoments: 1, cooldownMs: 55_000, triggerMultiplier: 0.85, minDelayMs: 10_000, maxDelayMs: 24_000 },
            mid: { maxMoments: 2, cooldownMs: 45_000, triggerMultiplier: 1.0, minDelayMs: 9_000, maxDelayMs: 21_000 },
            finals: { maxMoments: 3, cooldownMs: 35_000, triggerMultiplier: 1.2, minDelayMs: 7_000, maxDelayMs: 16_000 },
        }[stage]

        if (phase === 'winter-break' || phase === 'summer-break') {
            return { ...byStage, maxMoments: Math.max(0, byStage.maxMoments - 2), triggerMultiplier: byStage.triggerMultiplier * 0.5 }
        }

        if (phase === 'internship-period') {
            return { ...byStage, maxMoments: Math.max(1, byStage.maxMoments - 1), triggerMultiplier: byStage.triggerMultiplier * 0.8 }
        }

        return byStage
    }

    const computeWeightedTriggerChance = (courseId: string, cooldownMs: number, triggerMultiplier: number): number => {
        const stress = Number(player.stats?.stress ?? 0)
        const burnout = Number(player.stats?.burnout ?? 0)
        const gpa = Number(player.stats?.gpa ?? 0)

        const courseInfo = currentCourses.find(c => c.id === courseId)
        const weeklyHours = Number(courseInfo?.weekly_hours ?? 0)

        const outcomes = miniGameOutcomesByCourseRef.current[courseId] || { passed: 0, failed: 0 }
        const totalOutcomes = outcomes.passed + outcomes.failed
        const failRate = totalOutcomes > 0 ? outcomes.failed / totalOutcomes : 0

        const attempts = randomTriggerAttemptsByCourseRef.current[courseId] || 0
        const phase = getCurrentPhase(player.semester).phase

        let chance = 0.28
        chance += (stress / 100) * 0.22
        chance += (burnout / 100) * 0.14
        chance += clampNumber((3.0 - gpa) / 3.0, 0, 1) * 0.12
        chance += clampNumber(weeklyHours / 16, 0, 1) * 0.12
        chance += failRate * 0.15
        chance += clampNumber(attempts / 4, 0, 1) * 0.08

        if (phase === 'internship-period') {
            chance += 0.08
        } else if (phase === 'winter-break' || phase === 'summer-break') {
            chance -= 0.12
        }

        const sinceRandomTriggerMs = Date.now() - lastRandomTriggerAtRef.current
        const sinceMiniGameCloseMs = Date.now() - lastMiniGameClosedAtRef.current
        if (sinceRandomTriggerMs < cooldownMs || sinceMiniGameCloseMs < cooldownMs) {
            chance -= 0.2
        }

        chance *= triggerMultiplier

        return clampNumber(chance, 0.08, 0.9)
    }

    const getGameChallengeScore = (game: MiniGameSummary): number => {
        const passComponent = (game.min_passing_score || 70) / 100
        const lengthComponent = Math.min(1.0, (game.question_count || 1) / 10)
        const difficultyComponent = Math.min(1.0, (game.average_question_difficulty || 2.5) / 5)
        return passComponent * 0.35 + lengthComponent * 0.25 + difficultyComponent * 0.4
    }

    const getAdaptiveMode = (courseId: string): 'recovery' | 'balanced' | 'challenge' => {
        const outcomes = miniGameOutcomesByCourseRef.current[courseId] || { passed: 0, failed: 0 }
        const totalOutcomes = outcomes.passed + outcomes.failed
        const failRate = totalOutcomes > 0 ? outcomes.failed / totalOutcomes : 0

        const completedGames = courseMiniGames.filter(g => g.completed)
        const avgBestScore = completedGames.length > 0
            ? completedGames.reduce((sum, g) => sum + Number(g.best_score_percent || 0), 0) / completedGames.length
            : 0

        if (failRate >= 0.45 || (completedGames.length > 0 && avgBestScore < 70)) {
            return 'recovery'
        }
        if ((outcomes.passed >= outcomes.failed + 2) || avgBestScore >= 88) {
            return 'challenge'
        }
        return 'balanced'
    }

    const buildLifeMomentNarration = (courseId: string, game: MiniGameSummary): { headline: string; scenario: string; stakes: string } => {
        const cid = courseId.toLowerCase()

        if (cid.startsWith('ba') || cid.startsWith('econ')) {
            return {
                headline: `Boardroom ping: ${game.title}`,
                scenario: `A stakeholder asks for an immediate decision related to ${game.topic.toLowerCase()}. You have one shot to respond clearly and confidently.`,
                stakes: 'Good call: stronger reputation and opportunity momentum. Bad call: trust drops and pressure rises.',
            }
        }

        if (cid.startsWith('cs')) {
            return {
                headline: `Production alert: ${game.title}`,
                scenario: `A live system issue just hit your queue. The challenge maps to ${game.topic.toLowerCase()} and your team expects fast, correct reasoning.`,
                stakes: 'Strong response: technical credibility grows. Weak response: interview readiness and confidence take a hit.',
            }
        }

        if (cid.startsWith('eng') || cid.startsWith('phys')) {
            return {
                headline: `Design review emergency: ${game.title}`,
                scenario: `A real-world constraint changed minutes before review. You must apply ${game.topic.toLowerCase()} under time pressure.`,
                stakes: 'Solid solution: project trust and leadership rise. Mistakes: safety/risk concerns and extra scrutiny.',
            }
        }

        return {
            headline: `Life moment triggered: ${game.title}`,
            scenario: `A course-related situation appeared unexpectedly. Apply what you learned about ${game.topic.toLowerCase()}.`,
            stakes: 'Your choice affects stress, confidence, and future opportunities.',
        }
    }

    const pickWeightedMiniGame = (courseId: string, pool: MiniGameSummary[]): MiniGameSummary | null => {
        if (pool.length === 0) return null

        const adaptiveMode = getAdaptiveMode(courseId)

        const weightedPool = pool.map(game => {
            const challengeScore = getGameChallengeScore(game)
            let weight = 1

            if (adaptiveMode === 'recovery') {
                weight += Math.max(0.3, 1.7 - challengeScore)
            } else if (adaptiveMode === 'challenge') {
                weight += challengeScore * 1.8
            } else {
                weight += 0.6
            }

            return { game, weight: Math.max(0.1, weight) }
        })

        const totalWeight = weightedPool.reduce((sum, item) => sum + item.weight, 0)
        let pick = Math.random() * totalWeight

        for (const item of weightedPool) {
            pick -= item.weight
            if (pick <= 0) {
                return item.game
            }
        }

        return weightedPool[weightedPool.length - 1].game
    }

    useEffect(() => {
        const loadSemesterCourses = async () => {
            try {
                setCoursesLoading(true)
                const response = await fetch(`/api/exams/semester-courses?player_id=${player.id}`)
                if (!response.ok) throw new Error('Failed to load semester courses')

                const data = await response.json()
                setCurrentCourses(data.courses || [])
            } catch (err) {
                setError(err instanceof Error ? err.message : 'Failed to load semester courses')
                setCurrentCourses([])
            } finally {
                setCoursesLoading(false)
            }
        }

        if (player?.id) {
            loadSemesterCourses()
        }
    }, [player?.id, player?.semester])

    useEffect(() => {
        if (!pendingRecommendedGameId || activeTab !== 'academics' || !classContent) return

        const card = document.querySelector(`[data-game-id="${pendingRecommendedGameId}"]`) as HTMLElement | null
        if (!card) return

        card.scrollIntoView({ behavior: 'smooth', block: 'center' })
    }, [pendingRecommendedGameId, activeTab, classContent, courseMiniGames])

    useEffect(() => {
        return () => {
            if (recommendedLaunchTimerRef.current) {
                window.clearTimeout(recommendedLaunchTimerRef.current)
                recommendedLaunchTimerRef.current = null
            }
        }
    }, [])

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
            setLoading(true)
            const answers = activeExam.questions.map((q: any, idx: number) => ({
                question_id: q.id,
                chosen_choice_id: examAnswers[idx]
            }))

            const result = await submitSemesterExam({
                player_id: player.id,
                answers: answers
            })

            setExamSubmitted(true)
            setExamScore(result.exam_result.score_percent)

            // If exam passed, show "progress to next semester" button
            // (The summary will show after they click it)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to submit exam')
        } finally {
            setLoading(false)
        }
    }

    const handleProgressSemester = async () => {
        try {
            setLoading(true)

            // Call the progression API
            const summary = await advanceSemester(player.id)

            // Show the summary screen
            setSemesterSummary(summary)
            setShowSemesterSummary(true)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to progress semester')
        } finally {
            setLoading(false)
        }
    }

    const handleContinueAfterSummary = async () => {
        try {
            setLoading(true)

            // Refresh player data from server
            if (onRefreshPlayer) {
                const updated = await onRefreshPlayer(player.id)
                if (updated && onPlayerUpdate) {
                    onPlayerUpdate(updated)
                }
            }

            // Close all exam/summary modals
            setShowSemesterExam(false)
            setShowSemesterSummary(false)
            setActiveExam(null)
            setSemesterSummary(null)
            setExamSubmitted(false)
            setExamScore(null)
            setExamAnswers({})
            setExamQuestionIndex(0)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to continue')
        } finally {
            setLoading(false)
        }
    }

    const handleAttendClass = async (courseId: string) => {
        try {
            setLoading(true)
            setError(null)
            classSessionStartedAtRef.current = Date.now()
            randomMomentsByCourseRef.current[courseId] = 0
            randomTriggerAttemptsByCourseRef.current[courseId] = 0

            const [content, gamesResponse] = await Promise.all([
                attendClass(courseId),
                getMiniGamesForCourse(courseId, player.id),
            ])
            setClassContent(content)
            setSelectedCourse(courseId)
            setCourseMiniGames(gamesResponse.games || [])

            const persistedSeen = new Set<string>(
                (gamesResponse.games || [])
                    .filter(g => g.seen || g.completed)
                    .map(g => g.id)
            )
            seenMiniGamesByCourseRef.current[courseId] = persistedSeen
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to attend class')
            setCourseMiniGames([])
        } finally {
            setLoading(false)
        }
    }

    const handleStartMiniGame = async (gameId: string) => {
        try {
            setMiniGamesLoading(true)
            setError(null)

            const game = await getMiniGameDetails(gameId)

            try {
                await markMiniGameSeen(player.id, game.id, game.course_id)
            } catch {
                // non-blocking: gameplay should continue even if seen tracking fails
            }

            if (!seenMiniGamesByCourseRef.current[game.course_id]) {
                seenMiniGamesByCourseRef.current[game.course_id] = new Set<string>()
            }
            seenMiniGamesByCourseRef.current[game.course_id].add(game.id)
            setCourseMiniGames(prev => prev.map(g => (g.id === game.id ? { ...g, seen: true } : g)))

            setActiveMiniGame(game)
            setMiniGameQuestionIndex(0)
            setMiniGameAnswers({})
            setMiniGameSubmitted(false)
            setMiniGameResult(null)
            setMiniGameStartTime(Date.now())
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to start mini-game')
        } finally {
            setMiniGamesLoading(false)
        }
    }

    const handleMiniGameAnswerSelect = (optionIndex: number) => {
        setMiniGameAnswers(prev => ({
            ...prev,
            [miniGameQuestionIndex]: optionIndex,
        }))
    }

    const handleMiniGameNextQuestion = () => {
        if (!activeMiniGame) return
        if (miniGameQuestionIndex < activeMiniGame.questions.length - 1) {
            setMiniGameQuestionIndex(miniGameQuestionIndex + 1)
        }
    }

    const handleMiniGamePreviousQuestion = () => {
        if (miniGameQuestionIndex > 0) {
            setMiniGameQuestionIndex(miniGameQuestionIndex - 1)
        }
    }

    const handleSubmitMiniGame = async () => {
        if (!activeMiniGame) return

        try {
            setMiniGamesLoading(true)

            const answers = activeMiniGame.questions.map((q, idx) => ({
                question_id: q.id,
                selected_option_index: miniGameAnswers[idx],
            }))

            const elapsedMs = miniGameStartTime ? Date.now() - miniGameStartTime : 0
            const timeSpentMinutes = Math.max(1, Math.round(elapsedMs / 60000))

            const result = await submitMiniGame(player.id, {
                game_id: activeMiniGame.id,
                course_id: activeMiniGame.course_id,
                answers,
                time_spent_minutes: timeSpentMinutes,
            })

            if (!miniGameOutcomesByCourseRef.current[activeMiniGame.course_id]) {
                miniGameOutcomesByCourseRef.current[activeMiniGame.course_id] = { passed: 0, failed: 0 }
            }
            if (result.passed) {
                miniGameOutcomesByCourseRef.current[activeMiniGame.course_id].passed += 1
            } else {
                miniGameOutcomesByCourseRef.current[activeMiniGame.course_id].failed += 1
            }

            setCourseMiniGames(prev => prev.map(g => (
                g.id === activeMiniGame.id
                    ? {
                        ...g,
                        seen: true,
                        completed: result.passed ? true : (g.completed || false),
                        best_score_percent: Math.max(g.best_score_percent ?? 0, result.score_percent),
                    }
                    : g
            )))

            setMiniGameResult(result)
            setMiniGameSubmitted(true)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to submit mini-game')
        } finally {
            setMiniGamesLoading(false)
        }
    }

    const handleCloseMiniGame = () => {
        lastMiniGameClosedAtRef.current = Date.now()
        setActiveMiniGame(null)
        setMiniGameQuestionIndex(0)
        setMiniGameAnswers({})
        setMiniGameSubmitted(false)
        setMiniGameResult(null)
        setMiniGameStartTime(null)
    }

    const handleOpenLessonGame = async (lesson: any) => {
        try {
            setLessonGameLoading(true)
            setLessonGameError(null)
            setActiveLesson(lesson)
            setLessonGameQuestionIndex(0)
            setLessonGameAnswers({})
            setLessonGameSubmitted(false)
            setLessonGameResult(null)

            let payload: LessonGameDetails | null = null
            try {
                payload = await getLessonGame(lesson.id)
            } catch {
                payload = null
            }

            setActiveLessonGame(normalizeLessonGame(lesson, payload))
        } catch (err) {
            setLessonGameError(err instanceof Error ? err.message : 'Failed to open lesson mini-game')
        } finally {
            setLessonGameLoading(false)
        }
    }

    const handleCloseLessonGame = () => {
        setActiveLesson(null)
        setActiveLessonGame(null)
        setLessonGameError(null)
        setLessonGameQuestionIndex(0)
        setLessonGameAnswers({})
        setLessonGameSubmitted(false)
        setLessonGameResult(null)
    }

    const handleLessonAnswerSelect = (optionIndex: number) => {
        setLessonGameAnswers(prev => ({
            ...prev,
            [lessonGameQuestionIndex]: optionIndex,
        }))
    }

    const handleLessonNextQuestion = () => {
        if (!activeLessonGame?.questions) return
        if (lessonGameQuestionIndex < activeLessonGame.questions.length - 1) {
            setLessonGameQuestionIndex(lessonGameQuestionIndex + 1)
        }
    }

    const handleLessonPreviousQuestion = () => {
        if (lessonGameQuestionIndex > 0) {
            setLessonGameQuestionIndex(lessonGameQuestionIndex - 1)
        }
    }

    const handleSubmitLessonConceptGame = async () => {
        if (!activeLessonGame?.questions || !activeLesson) return

        const total = activeLessonGame.questions.length
        let correct = 0
        activeLessonGame.questions.forEach((q, idx) => {
            if (lessonGameAnswers[idx] === q.correct_option_index) {
                correct += 1
            }
        })

        const scorePercent = Math.round((correct / total) * 100)
        const passed = scorePercent >= 70

        setLessonGameResult({
            scorePercent,
            passed,
            correctCount: correct,
            totalQuestions: total,
        })
        setLessonGameSubmitted(true)

        try {
            await submitLessonGame(activeLesson.id, { score: correct, max_score: total })
        } catch {
            // non-blocking: local learning flow should continue
        }
    }

    const handlePlayRecommendedGame = async (rec: GameRecommendation) => {
        const phase = getCurrentPhase(player.semester)
        if (!phase.canAttendClasses) {
            throw new Error('Classes are not in session right now. Recommended games open during class periods.')
        }

        setActiveTab('academics')
        setPendingRecommendedGameId(rec.game_id)

        if (!classContent || selectedCourse !== rec.course_id) {
            await handleAttendClass(rec.course_id)
        }

        await new Promise(resolve => window.setTimeout(resolve, 260))
        await handleStartMiniGame(rec.game_id)

        if (recommendedLaunchTimerRef.current) {
            window.clearTimeout(recommendedLaunchTimerRef.current)
        }
        recommendedLaunchTimerRef.current = window.setTimeout(() => {
            setPendingRecommendedGameId(null)
            recommendedLaunchTimerRef.current = null
        }, 2200)
    }

    const handleStartPendingLifeMoment = () => {
        if (!pendingLifeMoment) return
        setActiveMiniGame(pendingLifeMoment.game)
        setMiniGameQuestionIndex(0)
        setMiniGameAnswers({})
        setMiniGameSubmitted(false)
        setMiniGameResult(null)
        setMiniGameStartTime(Date.now())
        setPendingLifeMoment(null)
    }

    useEffect(() => {
        if (randomMiniGameTimerRef.current !== null) {
            window.clearTimeout(randomMiniGameTimerRef.current)
            randomMiniGameTimerRef.current = null
        }

        if (!classContent || !selectedCourse || courseMiniGames.length === 0) {
            return
        }

        const sessionStage = getSessionStage(selectedCourse)
        const pacing = getPacingConfig(sessionStage)

        const randomCount = randomMomentsByCourseRef.current[selectedCourse] || 0
        const maxAllowedMoments = Math.min(MAX_RANDOM_MOMENTS_PER_COURSE, pacing.maxMoments)
        if (randomCount >= maxAllowedMoments) {
            return
        }

        if (activeMiniGame || activeQuiz || showSemesterExam || pendingLifeMoment) {
            return
        }

        if (!seenMiniGamesByCourseRef.current[selectedCourse]) {
            seenMiniGamesByCourseRef.current[selectedCourse] = new Set<string>()
        }

        const unseenGames = courseMiniGames.filter(g => !seenMiniGamesByCourseRef.current[selectedCourse].has(g.id))
        if (unseenGames.length === 0) {
            return
        }

        const weightedChance = computeWeightedTriggerChance(selectedCourse, pacing.cooldownMs, pacing.triggerMultiplier)
        const pressureFactor = clampNumber((Number(player.stats?.stress ?? 0) + Number(player.stats?.burnout ?? 0)) / 200, 0, 1)
        const range = Math.max(1, pacing.maxDelayMs - pacing.minDelayMs)
        const pacedDelay = pacing.minDelayMs + Math.floor(Math.random() * range)
        const delayMs = Math.max(5000, pacedDelay - Math.floor(5000 * pressureFactor))

        randomMiniGameTimerRef.current = window.setTimeout(async () => {
            try {
                randomTriggerAttemptsByCourseRef.current[selectedCourse] = (randomTriggerAttemptsByCourseRef.current[selectedCourse] || 0) + 1

                if (Math.random() > weightedChance) {
                    setLifeMomentNotice(`🧭 ${selectedCourse.toUpperCase()} stayed stable this time (phase ${sessionStage}, trigger chance ${(weightedChance * 100).toFixed(0)}%).`)
                    return
                }

                const pool = courseMiniGames.filter(g => !seenMiniGamesByCourseRef.current[selectedCourse].has(g.id))
                if (pool.length === 0) {
                    return
                }

                const randomGame = pickWeightedMiniGame(selectedCourse, pool)

                if (!randomGame) {
                    return
                }

                seenMiniGamesByCourseRef.current[selectedCourse].add(randomGame.id)
                randomMomentsByCourseRef.current[selectedCourse] = (randomMomentsByCourseRef.current[selectedCourse] || 0) + 1
                lastRandomTriggerAtRef.current = Date.now()

                const momentsLeft = Math.max(0, maxAllowedMoments - randomMomentsByCourseRef.current[selectedCourse])
                setLifeMomentNotice(`⚡ ${sessionStage.toUpperCase()} phase moment in ${selectedCourse.toUpperCase()}: ${randomGame.title}${momentsLeft > 0 ? ` • ${momentsLeft} event(s) left this phase` : ''} • trigger ${(weightedChance * 100).toFixed(0)}%`)
                setMiniGamesLoading(true)

                const game = await getMiniGameDetails(randomGame.id)
                const narration = buildLifeMomentNarration(selectedCourse, randomGame)
                setPendingLifeMoment({
                    ...narration,
                    game,
                })
            } catch (err) {
                setError(err instanceof Error ? err.message : 'Failed to launch random mini-game')
            } finally {
                setMiniGamesLoading(false)
                randomMiniGameTimerRef.current = null
            }
        }, delayMs)

        return () => {
            if (randomMiniGameTimerRef.current !== null) {
                window.clearTimeout(randomMiniGameTimerRef.current)
                randomMiniGameTimerRef.current = null
            }
        }
    }, [classContent, selectedCourse, courseMiniGames, activeMiniGame, activeQuiz, showSemesterExam, pendingLifeMoment])

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

    useEffect(() => {
        const timer = window.setTimeout(() => {
            setDebouncedSelectedCourse(selectedCourse)
        }, 120)
        return () => window.clearTimeout(timer)
    }, [selectedCourse])

    useEffect(() => {
        const timer = window.setTimeout(() => {
            setTabTransitioning(false)
        }, 140)
        setTabTransitioning(true)
        return () => window.clearTimeout(timer)
    }, [activeTab])

    useEffect(() => {
        const key = `planning_draft_${player.id}`
        const existing = localStorage.getItem(key)
        if (existing) {
            setPlanningDraft(existing)
        } else {
            setPlanningDraft('')
        }
        setPlanningDraftStatus('idle')
    }, [player.id])

    useEffect(() => {
        if (!player.id) return
        setPlanningDraftStatus('saving')
        const timer = window.setTimeout(() => {
            localStorage.setItem(`planning_draft_${player.id}`, planningDraft)
            setPlanningDraftStatus('saved')
            window.setTimeout(() => setPlanningDraftStatus('idle'), 900)
        }, 280)
        return () => window.clearTimeout(timer)
    }, [planningDraft, player.id])

    const semesterInfo = getSemesterInfo(player.semester)
    const phaseInfo = getCurrentPhase(player.semester)
    const adaptiveMode = debouncedSelectedCourse ? getAdaptiveMode(debouncedSelectedCourse) : 'balanced'
    const adaptiveModeLabel = adaptiveMode === 'recovery'
        ? 'Recovery Mode: easier moments prioritized'
        : adaptiveMode === 'challenge'
            ? 'Challenge Mode: harder moments prioritized'
            : 'Balanced Mode: mixed difficulty'

    useEffect(() => {
        const timer = window.setTimeout(() => {
            const next = [...courseMiniGames].sort((a, b) => {
                const target = adaptiveMode === 'recovery' ? 0.35 : adaptiveMode === 'challenge' ? 0.8 : 0.55
                const da = Math.abs(getGameChallengeScore(a) - target)
                const db = Math.abs(getGameChallengeScore(b) - target)
                return da - db
            })
            setSortedMiniGames(next)
        }, 90)

        return () => window.clearTimeout(timer)
    }, [courseMiniGames, adaptiveMode])

    const gpaValue = Number(player.stats?.gpa ?? 0)
    const stressValue = Number(player.stats?.stress ?? 0)
    const networkValue = Number(player.stats?.network ?? 0)
    const healthValue = Number(player.stats?.health ?? 0)
    const balanceValue = Number(player.finance?.balance ?? 0)

    const momentumScore = Math.round(
        clampNumber(
            (gpaValue / 4) * 40 + ((100 - stressValue) * 0.22) + (networkValue * 0.18) + (healthValue * 0.2),
            0,
            100,
        ),
    )

    const momentumLabel = momentumScore >= 80
        ? 'On Fire'
        : momentumScore >= 60
            ? 'Stable Climb'
            : momentumScore >= 40
                ? 'Needs Attention'
                : 'Critical Recovery'

    const coachTips: Array<{
        id: string
        title: string
        detail: string
        tab: GameTab
        cta: string
    }> = []

    if (stressValue >= 70) {
        coachTips.push({
            id: 'stress-high',
            title: 'Stress is very high',
            detail: 'Shift your schedule, reduce overload, and make one recovery purchase this term.',
            tab: 'planning',
            cta: 'Adjust Plan',
        })
    }

    if (balanceValue < 500) {
        coachTips.push({
            id: 'cash-low',
            title: 'Cash buffer is low',
            detail: 'Review debt and repayment profile to protect cash runway.',
            tab: 'finance',
            cta: 'Open Finance',
        })
    }

    if (!player.plan) {
        coachTips.push({
            id: 'no-plan',
            title: 'No active semester plan',
            detail: 'Create and lock a plan to stabilize outcomes before advancing.',
            tab: 'planning',
            cta: 'Create Plan',
        })
    }

    if (gpaValue < 2.8) {
        coachTips.push({
            id: 'gpa-risk',
            title: 'GPA recovery opportunity',
            detail: 'Focus on classes and complete mini-games to recover performance quickly.',
            tab: 'academics',
            cta: 'Study Now',
        })
    }

    if (networkValue < 40) {
        coachTips.push({
            id: 'network-low',
            title: 'Network score can grow faster',
            detail: 'Pick social or mentorship activities and strategic store items.',
            tab: 'store',
            cta: 'Open Store',
        })
    }

    if (coachTips.length === 0) {
        coachTips.push({
            id: 'all-good',
            title: 'Great momentum',
            detail: 'You are balanced. Push for higher GPA and maintain low stress.',
            tab: 'academics',
            cta: 'Chase Excellence',
        })
    }

    const prefetchTab = (tab: GameTab) => {
        if (prefetchedTabsRef.current.has(tab)) return
        prefetchedTabsRef.current.add(tab)

        if (tab === 'finance') {
            prefetchFinanceData(player.id)
            return
        }

        if (tab === 'analytics') {
            prefetchAnalyticsData(player.id)
            return
        }

        if (tab === 'store') {
            prefetchStoreData(player.id)
        }
    }

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
                <nav className="game-nav" aria-label="Primary game navigation">
                    <button
                        className={`nav-btn ${activeTab === 'stats' ? 'active' : ''}`}
                        onClick={() => setActiveTab('stats')}
                        onMouseEnter={() => prefetchTab('stats')}
                        onFocus={() => prefetchTab('stats')}
                        aria-label="Open stats tab"
                    >
                        📊 Stats
                    </button>
                    <button
                        className={`nav-btn ${activeTab === 'finance' ? 'active' : ''}`}
                        onClick={() => setActiveTab('finance')}
                        onMouseEnter={() => prefetchTab('finance')}
                        onFocus={() => prefetchTab('finance')}
                        aria-label="Open finance tab"
                    >
                        💰 Finance
                    </button>
                    <button
                        className={`nav-btn ${activeTab === 'planning' ? 'active' : ''}`}
                        onClick={() => setActiveTab('planning')}
                        onMouseEnter={() => prefetchTab('planning')}
                        onFocus={() => prefetchTab('planning')}
                        aria-label="Open planning tab"
                    >
                        📅 Planning
                    </button>
                    <button
                        className={`nav-btn ${activeTab === 'academics' ? 'active' : ''}`}
                        onClick={() => setActiveTab('academics')}
                        onMouseEnter={() => prefetchTab('academics')}
                        onFocus={() => prefetchTab('academics')}
                        aria-label="Open academics tab"
                    >
                        🎓 Academics
                    </button>
                    <button
                        className={`nav-btn ${activeTab === 'visual' ? 'active' : ''}`}
                        onClick={() => setActiveTab('visual')}
                        onMouseEnter={() => prefetchTab('visual')}
                        onFocus={() => prefetchTab('visual')}
                        aria-label="Open visual dashboard tab"
                    >
                        ✨ Visual
                    </button>
                    <button
                        className={`nav-btn ${activeTab === 'analytics' ? 'active' : ''}`}
                        onClick={() => setActiveTab('analytics')}
                        onMouseEnter={() => prefetchTab('analytics')}
                        onFocus={() => prefetchTab('analytics')}
                        aria-label="Open analytics tab"
                    >
                        📊 Analytics
                    </button>
                    <button
                        className={`nav-btn ${activeTab === 'store' ? 'active' : ''}`}
                        onClick={() => setActiveTab('store')}
                        onMouseEnter={() => prefetchTab('store')}
                        onFocus={() => prefetchTab('store')}
                        aria-label="Open store tab"
                    >
                        🛍️ Store
                    </button>
                </nav>

                <main className="game-main">
                    {tabTransitioning && (
                        <div className="tab-switch-skeleton" aria-label="Loading tab content">
                            <div className="skeleton-line long" />
                            <div className="skeleton-grid">
                                <div className="skeleton-card" />
                                <div className="skeleton-card" />
                                <div className="skeleton-card" />
                            </div>
                        </div>
                    )}
                    {activeTab === 'stats' && (
                        <section className="tab-content">
                            <h2>Your Stats</h2>
                            <div className="stats-grid">
                                <div className="stat-card">
                                    <h3>GPA</h3>
                                    <p className="stat-value">{gpaValue.toFixed(2)}</p>
                                </div>
                                <div className="stat-card">
                                    <h3>Stress</h3>
                                    <p className="stat-value">{stressValue.toFixed(0)}%</p>
                                </div>
                                <div className="stat-card">
                                    <h3>Network</h3>
                                    <p className="stat-value">{networkValue.toFixed(0)}</p>
                                </div>
                                <div className="stat-card">
                                    <h3>Health</h3>
                                    <p className="stat-value">{healthValue.toFixed(0)}%</p>
                                </div>
                                <div className="stat-card momentum-card">
                                    <h3>Momentum</h3>
                                    <p className="stat-value">{momentumScore}</p>
                                    <span className="momentum-label">{momentumLabel}</span>
                                </div>
                            </div>

                            <div className="stats-progress-grid">
                                <div className="progress-card">
                                    <div className="progress-head">
                                        <span>Academic Progress</span>
                                        <strong>{((gpaValue / 4) * 100).toFixed(0)}%</strong>
                                    </div>
                                    <progress max={100} value={clampNumber((gpaValue / 4) * 100, 0, 100)} />
                                </div>
                                <div className="progress-card">
                                    <div className="progress-head">
                                        <span>Wellbeing Stability</span>
                                        <strong>{clampNumber((healthValue + (100 - stressValue)) / 2, 0, 100).toFixed(0)}%</strong>
                                    </div>
                                    <progress max={100} value={clampNumber((healthValue + (100 - stressValue)) / 2, 0, 100)} />
                                </div>
                                <div className="progress-card">
                                    <div className="progress-head">
                                        <span>Career Network Growth</span>
                                        <strong>{clampNumber(networkValue, 0, 100).toFixed(0)}%</strong>
                                    </div>
                                    <progress max={100} value={clampNumber(networkValue, 0, 100)} />
                                </div>
                            </div>

                            <div className="coach-panel">
                                <div className="coach-header">
                                    <h3>🎯 Life Coach Recommendations</h3>
                                    <p>Top actions to improve your next semester outcome.</p>
                                </div>
                                <div className="coach-list">
                                    {coachTips.slice(0, 3).map((tip) => (
                                        <div key={tip.id} className="coach-item">
                                            <div>
                                                <h4>{tip.title}</h4>
                                                <p>{tip.detail}</p>
                                            </div>
                                            <button className="coach-action-btn" onClick={() => setActiveTab(tip.tab)}>
                                                {tip.cta}
                                            </button>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </section>
                    )}

                    {activeTab === 'finance' && (
                        <section className="tab-content">
                            <FinanceToolsPanel player={player} onPlayerUpdate={onPlayerUpdate} onRefreshPlayer={onRefreshPlayer} />
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
                                        <div className="plan-summary-grid">
                                            <div>
                                                <label>Housing</label>
                                                <strong>{player.plan.housing_option_id || 'Not set'}</strong>
                                            </div>
                                            <div>
                                                <label>Job</label>
                                                <strong>{player.plan.job_id || 'No job selected'}</strong>
                                            </div>
                                            <div>
                                                <label>Activities</label>
                                                <strong>{Array.isArray(player.plan.activities) ? player.plan.activities.length : 0}</strong>
                                            </div>
                                            <div>
                                                <label>Status</label>
                                                <strong>{player.plan.locked ? 'Locked' : 'Draft'}</strong>
                                            </div>
                                        </div>
                                        <div className="planning-quick-actions">
                                            <button className="plan-jump-btn" onClick={() => setActiveTab('academics')}>
                                                Improve Academic Mix
                                            </button>
                                            <button className="plan-jump-btn" onClick={() => setActiveTab('finance')}>
                                                Check Budget Fit
                                            </button>
                                            <button className="plan-jump-btn" onClick={() => setActiveTab('store')}>
                                                Add Recovery Items
                                            </button>
                                        </div>
                                    </div>
                                ) : (
                                    <div className="no-plan">
                                        <p>No plan created yet. Create one to get started!</p>
                                        <div className="planning-quick-actions">
                                            <button className="plan-jump-btn" onClick={() => setActiveTab('academics')}>
                                                Pick Courses First
                                            </button>
                                            <button className="plan-jump-btn" onClick={() => setActiveTab('finance')}>
                                                Prepare Finances
                                            </button>
                                        </div>
                                    </div>
                                )}

                                <div className="planning-draft-card">
                                    <div className="planning-draft-head">
                                        <h3>Quick Plan Draft</h3>
                                        <span className={`draft-status ${planningDraftStatus}`}>{planningDraftStatus === 'saving' ? 'Saving…' : planningDraftStatus === 'saved' ? 'Saved' : 'Idle'}</span>
                                    </div>
                                    <textarea
                                        value={planningDraft}
                                        onChange={(e) => setPlanningDraft(e.target.value)}
                                        placeholder="Write your semester intention, risk notes, or weekly action plan..."
                                        rows={4}
                                    />
                                </div>
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
                                            {coursesLoading && (
                                                <div className="courses-loading-skeleton" aria-label="Loading courses">
                                                    <div className="course-skeleton" />
                                                    <div className="course-skeleton" />
                                                    <div className="course-skeleton" />
                                                </div>
                                            )}
                                            {!coursesLoading && currentCourses.length === 0 && (
                                                <div className="phase-notice">
                                                    <p>No courses found for your current major and semester.</p>
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
                                                        setCourseMiniGames([])
                                                        setLifeMomentNotice(null)
                                                    }}
                                                >
                                                    ← Back to Courses
                                                </button>
                                                <h3>{classContent.course_title}</h3>
                                            </div>

                                            <div className="class-sections">
                                                {lifeMomentNotice && (
                                                    <div className="phase-notice" style={{ marginBottom: '12px' }}>
                                                        <p>{lifeMomentNotice}</p>
                                                        <p className="notice-sub">Life Sprint triggers course-related challenges at random moments, just like real life.</p>
                                                    </div>
                                                )}

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
                                                                <button
                                                                    className="btn-lesson-game"
                                                                    onClick={() => handleOpenLessonGame(lesson)}
                                                                    disabled={lessonGameLoading}
                                                                >
                                                                    🧠 Understand Concept
                                                                </button>
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

                                                {/* Mini-Games */}
                                                <section className="class-section">
                                                    <h4>🎮 Mini-Games ({courseMiniGames.length})</h4>
                                                    <p className="notice-sub">Life Sprint can trigger these at random moments during class.</p>
                                                    <p className="notice-sub">🧠 Adaptive difficulty: {adaptiveModeLabel}</p>
                                                    {miniGamesLoading && <p>Loading mini-games...</p>}
                                                    {!miniGamesLoading && courseMiniGames.length === 0 && (
                                                        <p>No mini-games available for this course yet.</p>
                                                    )}

                                                    {!miniGamesLoading && courseMiniGames.length > 0 && (
                                                        <div className="quizzes-list">
                                                            {sortedMiniGames.map((game, idx) => (
                                                                <div
                                                                    key={game.id}
                                                                    data-game-id={game.id}
                                                                    className={`quiz-item ${pendingRecommendedGameId === game.id ? 'recommended-focus' : ''}`}
                                                                >
                                                                    <div className="quiz-header">
                                                                        <span className="quiz-title">{game.title}{idx === 0 ? ' ⭐ Recommended now' : ''}</span>
                                                                        <span className="quiz-score">Pass: {game.min_passing_score}%</span>
                                                                    </div>
                                                                    <p className="quiz-topic">{game.topic}</p>
                                                                    <p className="quiz-count">{game.question_count} questions • ~{game.estimated_duration_minutes} min</p>
                                                                    <button
                                                                        className="btn-quiz"
                                                                        onClick={() => handleStartMiniGame(game.id)}
                                                                        disabled={miniGamesLoading}
                                                                    >
                                                                        Play Mini-Game
                                                                    </button>
                                                                </div>
                                                            ))}
                                                        </div>
                                                    )}
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

            {/* Mini-Game Modal */}
            {activeMiniGame && (
                <div className="quiz-modal-overlay">
                    <div className="quiz-modal">
                        <div className="quiz-modal-header">
                            <h2>{activeMiniGame.title}</h2>
                            <button className="close-quiz" onClick={handleCloseMiniGame}>✕</button>
                        </div>

                        {!miniGameSubmitted ? (
                            <>
                                <div className="quiz-progress">
                                    <span>Question {miniGameQuestionIndex + 1} of {activeMiniGame.questions.length}</span>
                                    <div className="progress-bar">
                                        <div
                                            className="progress-fill"
                                            style={{ width: `${((miniGameQuestionIndex + 1) / activeMiniGame.questions.length) * 100}%` }}
                                        />
                                    </div>
                                </div>

                                <div className="quiz-question">
                                    <h3>{activeMiniGame.questions[miniGameQuestionIndex].prompt}</h3>
                                    <div className="quiz-options">
                                        {activeMiniGame.questions[miniGameQuestionIndex].options.map((option: string, idx: number) => (
                                            <button
                                                key={idx}
                                                className={`quiz-option ${miniGameAnswers[miniGameQuestionIndex] === idx ? 'selected' : ''}`}
                                                onClick={() => handleMiniGameAnswerSelect(idx)}
                                            >
                                                {option}
                                            </button>
                                        ))}
                                    </div>
                                </div>

                                <div className="quiz-navigation">
                                    <button
                                        onClick={handleMiniGamePreviousQuestion}
                                        disabled={miniGameQuestionIndex === 0}
                                        className="btn-nav"
                                    >
                                        Previous
                                    </button>

                                    {miniGameQuestionIndex < activeMiniGame.questions.length - 1 ? (
                                        <button
                                            onClick={handleMiniGameNextQuestion}
                                            disabled={miniGameAnswers[miniGameQuestionIndex] === undefined || miniGamesLoading}
                                            className="btn-nav btn-primary"
                                        >
                                            Next
                                        </button>
                                    ) : (
                                        <button
                                            onClick={handleSubmitMiniGame}
                                            disabled={Object.keys(miniGameAnswers).length !== activeMiniGame.questions.length || miniGamesLoading}
                                            className="btn-nav btn-submit"
                                        >
                                            {miniGamesLoading ? 'Submitting...' : 'Submit Mini-Game'}
                                        </button>
                                    )}
                                </div>
                            </>
                        ) : (
                            <div className="quiz-results">
                                <h3>Mini-Game Complete!</h3>
                                <div className={`score-display ${miniGameResult?.passed ? 'passed' : 'failed'}`}>
                                    <span className="score-number">{miniGameResult?.score_percent.toFixed(1)}%</span>
                                    <span className="score-label">
                                        {miniGameResult?.passed ? '✅ Passed!' : '❌ Try Again'}
                                    </span>
                                </div>
                                <p className="passing-score">Passing score: {activeMiniGame.min_passing_score}%</p>
                                <p className="passing-score">Points earned: {miniGameResult?.points_earned ?? 0}</p>

                                {miniGameResult?.life_impact && (
                                    <div className="quiz-review">
                                        <h4>Life Impact</h4>
                                        <div className="review-item">
                                            <p className="review-correct">💵 Balance: {miniGameResult.life_impact.balance >= 0 ? '+' : ''}{miniGameResult.life_impact.balance.toFixed(2)}</p>
                                            <p className="review-correct">😰 Stress: {miniGameResult.life_impact.stress >= 0 ? '+' : ''}{miniGameResult.life_impact.stress.toFixed(2)}</p>
                                            <p className="review-correct">😊 Happiness: {miniGameResult.life_impact.happiness >= 0 ? '+' : ''}{miniGameResult.life_impact.happiness.toFixed(2)}</p>
                                            <p className="review-correct">🔥 Burnout: {miniGameResult.life_impact.burnout >= 0 ? '+' : ''}{miniGameResult.life_impact.burnout.toFixed(2)}</p>
                                            <p className="review-correct">🎓 GPA: {miniGameResult.life_impact.gpa >= 0 ? '+' : ''}{miniGameResult.life_impact.gpa.toFixed(3)}</p>
                                        </div>
                                    </div>
                                )}

                                {miniGameResult?.career_consequences && (
                                    <div className="quiz-review">
                                        <h4>Career Consequences</h4>
                                        <div className="review-item">
                                            <p className="review-correct">💼 Salary Multiplier: x{miniGameResult.career_consequences.salary_multiplier.toFixed(3)}</p>
                                            <p className="review-correct">🔓 Newly Unlocked: {miniGameResult.career_consequences.unlocked_now.length > 0 ? miniGameResult.career_consequences.unlocked_now.join(', ') : 'None'}</p>
                                            <p className="review-correct">🚫 Newly Blocked: {miniGameResult.career_consequences.blocked_now.length > 0 ? miniGameResult.career_consequences.blocked_now.join(', ') : 'None'}</p>
                                        </div>
                                    </div>
                                )}

                                <div className="quiz-review">
                                    <h4>Feedback</h4>
                                    {miniGameResult?.feedback.map((item, idx) => (
                                        <div key={`${item.question_id}-${idx}`} className="review-item">
                                            <p className={`review-answer ${item.is_correct ? 'correct' : 'incorrect'}`}>
                                                Q{idx + 1}: {item.is_correct ? 'Correct ✅' : 'Incorrect ❌'}
                                            </p>
                                            {!item.is_correct && item.correct_answer && (
                                                <p className="review-correct">Correct answer: {item.correct_answer}</p>
                                            )}
                                            {!item.is_correct && item.explanation && (
                                                <p className="review-correct">Why: {item.explanation}</p>
                                            )}
                                            <p className="review-correct">Learning: {item.learning_point}</p>
                                        </div>
                                    ))}
                                </div>

                                <button className="btn-close-results" onClick={handleCloseMiniGame}>
                                    Close
                                </button>
                            </div>
                        )}
                    </div>
                </div>
            )}

            {/* Lesson Concept Mini-Game Modal */}
            {activeLesson && (
                <div className="quiz-modal-overlay">
                    <div className="quiz-modal">
                        <div className="quiz-modal-header">
                            <h2>🧠 {activeLessonGame?.title || `Concept: ${activeLesson.title}`}</h2>
                            <button className="close-quiz" onClick={handleCloseLessonGame}>✕</button>
                        </div>

                        {lessonGameLoading ? (
                            <div className="quiz-results">
                                <p>Loading interactive concept challenge...</p>
                            </div>
                        ) : lessonGameError ? (
                            <div className="quiz-results">
                                <p className="error-message">{lessonGameError}</p>
                                <button className="btn-close-results" onClick={handleCloseLessonGame}>Close</button>
                            </div>
                        ) : activeLessonGame && activeLessonGame.questions && activeLessonGame.questions.length > 0 ? (
                            !lessonGameSubmitted ? (
                                <>
                                    <div className="quiz-progress">
                                        <span>Question {lessonGameQuestionIndex + 1} of {activeLessonGame.questions.length}</span>
                                        <div className="progress-bar">
                                            <div
                                                className="progress-fill"
                                                style={{ width: `${((lessonGameQuestionIndex + 1) / activeLessonGame.questions.length) * 100}%` }}
                                            />
                                        </div>
                                    </div>

                                    <div className="quiz-question">
                                        <p className="lesson-game-description">{activeLessonGame.description}</p>
                                        {activeLessonGame.objectives?.length > 0 && (
                                            <ul className="lesson-game-objectives">
                                                {activeLessonGame.objectives.map((obj, idx) => (
                                                    <li key={`${obj}-${idx}`}>{obj}</li>
                                                ))}
                                            </ul>
                                        )}

                                        <h3>{activeLessonGame.questions[lessonGameQuestionIndex].prompt}</h3>
                                        <div className="quiz-options">
                                            {activeLessonGame.questions[lessonGameQuestionIndex].options.map((option: string, idx: number) => (
                                                <button
                                                    key={idx}
                                                    className={`quiz-option ${lessonGameAnswers[lessonGameQuestionIndex] === idx ? 'selected' : ''}`}
                                                    onClick={() => handleLessonAnswerSelect(idx)}
                                                >
                                                    {option}
                                                </button>
                                            ))}
                                        </div>
                                    </div>

                                    <div className="quiz-navigation">
                                        <button
                                            onClick={handleLessonPreviousQuestion}
                                            disabled={lessonGameQuestionIndex === 0}
                                            className="btn-nav"
                                        >
                                            Previous
                                        </button>

                                        {lessonGameQuestionIndex < activeLessonGame.questions.length - 1 ? (
                                            <button
                                                onClick={handleLessonNextQuestion}
                                                disabled={lessonGameAnswers[lessonGameQuestionIndex] === undefined}
                                                className="btn-nav btn-primary"
                                            >
                                                Next
                                            </button>
                                        ) : (
                                            <button
                                                onClick={handleSubmitLessonConceptGame}
                                                disabled={Object.keys(lessonGameAnswers).length !== activeLessonGame.questions.length}
                                                className="btn-nav btn-submit"
                                            >
                                                Submit Concept Check
                                            </button>
                                        )}
                                    </div>
                                </>
                            ) : (
                                <div className="quiz-results">
                                    <h3>Concept Check Complete!</h3>
                                    <div className={`score-display ${lessonGameResult?.passed ? 'passed' : 'failed'}`}>
                                        <span className="score-number">{lessonGameResult?.scorePercent}%</span>
                                        <span className="score-label">
                                            {lessonGameResult?.passed ? '✅ Concept Understood' : '📘 Review and Retry'}
                                        </span>
                                    </div>
                                    <p className="passing-score">
                                        Correct: {lessonGameResult?.correctCount}/{lessonGameResult?.totalQuestions} (Pass: 70%)
                                    </p>

                                    <div className="quiz-review">
                                        <h4>Concept Feedback</h4>
                                        {activeLessonGame.questions.map((q, idx) => {
                                            const isCorrect = lessonGameAnswers[idx] === q.correct_option_index
                                            return (
                                                <div key={q.id} className="review-item">
                                                    <p className={`review-answer ${isCorrect ? 'correct' : 'incorrect'}`}>
                                                        Q{idx + 1}: {isCorrect ? 'Correct ✅' : 'Incorrect ❌'}
                                                    </p>
                                                    {!isCorrect && (
                                                        <p className="review-correct">Correct answer: {q.options[q.correct_option_index]}</p>
                                                    )}
                                                    <p className="review-correct">Why: {q.explanation}</p>
                                                    <p className="review-correct">Learning: {q.learning_point}</p>
                                                </div>
                                            )
                                        })}
                                    </div>

                                    <button className="btn-close-results" onClick={handleCloseLessonGame}>
                                        Continue Learning
                                    </button>
                                </div>
                            )
                        ) : (
                            <div className="quiz-results">
                                <p>No concept challenge available for this lesson yet.</p>
                                <button className="btn-close-results" onClick={handleCloseLessonGame}>Close</button>
                            </div>
                        )}
                    </div>
                </div>
            )}

            {/* Life Moment Narrative Card */}
            {pendingLifeMoment && (
                <div className="modal-overlay" onClick={() => setPendingLifeMoment(null)}>
                    <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                        <div className="modal-header">
                            <h2>🎬 {pendingLifeMoment.headline}</h2>
                            <button className="close-btn" onClick={() => setPendingLifeMoment(null)}>✕</button>
                        </div>
                        <div className="modal-body">
                            <div className="info-section">
                                <h3>Scenario</h3>
                                <p>{pendingLifeMoment.scenario}</p>
                            </div>
                            <div className="info-section">
                                <h3>Stakes</h3>
                                <p>{pendingLifeMoment.stakes}</p>
                            </div>
                        </div>
                        <div className="modal-footer">
                            <button className="btn-nav" onClick={() => setPendingLifeMoment(null)}>Skip for now</button>
                            <button className="btn-nav btn-primary" onClick={handleStartPendingLifeMoment}>Face the Moment</button>
                        </div>
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

            {activeTab === 'visual' && (
                <section className="tab-content">
                    <VisualExperiencePanel
                        player={player}
                        currentCourses={currentCourses}
                        miniGames={courseMiniGames}
                        onJumpToAcademics={() => setActiveTab('academics')}
                    />
                </section>
            )}

            {activeTab === 'analytics' && (
                <section className="tab-content">
                    <LifeReadinessPanel
                        playerId={player.id}
                        onPlayRecommendation={handlePlayRecommendedGame}
                    />
                </section>
            )}

            {activeTab === 'store' && (
                <section className="tab-content">
                    <StorePanel player={player} onPlayerUpdate={onPlayerUpdate} onRefreshPlayer={onRefreshPlayer} />
                </section>
            )}

            {/* Semester Summary Screen */}
            {showSemesterSummary && semesterSummary && (
                <SemesterSummaryScreen
                    summary={semesterSummary}
                    onContinue={handleContinueAfterSummary}
                    isLoading={loading}
                />
            )}
        </div>
    )
}
