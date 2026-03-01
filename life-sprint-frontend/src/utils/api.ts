const API_BASE = import.meta.env.DEV ? 'http://localhost:8000' : '/api'

export interface Player {
    id: string
    name: string
    age: number
    hs_gpa: number
    parent_income: number
    major_id: string
    college_id: string
    semester: number
    year_in_school: number
    stats: any
    finance: any
    housing: any
    job: any
    plan: any
    history: any[]
    tutorial_state: {
        completed_steps: string[]
        dismissed_tooltips: string[]
        tutorials_enabled: boolean
        current_focus: string | null
    }
}

export interface TutorialStep {
    step_id: string
    title: string
    description: string
    context: string
    priority: number
    action_hint?: string
}

export interface Tooltip {
    tooltip_id: string
    label: string
    content: string
    related_concept: string
}

export interface MiniGameSummary {
    id: string
    title: string
    description: string
    topic: string
    game_type: string
    estimated_duration_minutes: number
    question_count: number
    points_per_correct: number
    min_passing_score: number
    average_question_difficulty?: number
    seen?: boolean
    completed?: boolean
    best_score_percent?: number | null
}

export interface MiniGameQuestion {
    id: string
    prompt: string
    options: string[]
    difficulty: number
}

export interface MiniGameDetails {
    id: string
    course_id: string
    title: string
    description: string
    topic: string
    game_type: string
    estimated_duration_minutes: number
    points_per_correct: number
    points_per_incorrect: number
    min_passing_score: number
    questions: MiniGameQuestion[]
    message: string
}

export interface MiniGameSubmissionAnswer {
    question_id: string
    selected_option_index: number
}

export interface MiniGameSubmissionResult {
    game_id: string
    course_id: string
    score_percent: number
    points_earned: number
    correct_answers: number
    total_questions: number
    passed: boolean
    time_spent_minutes: number
    feedback: Array<{
        question_id: string
        is_correct: boolean
        learning_point: string
        correct_answer?: string
        explanation?: string
    }>
    key_learnings: string[]
    total_game_points: number
    life_impact?: {
        balance: number
        stress: number
        happiness: number
        burnout: number
        gpa: number
        technical_skills: number
        business_acumen: number
        communication_skills: number
        time_management: number
        energy_level: number
    }
    updated_stats?: {
        stress: number
        happiness: number
        burnout: number
        gpa: number
        technical_skills: number
        business_acumen: number
        communication_skills: number
        time_management: number
        energy_level: number
        balance: number
    }
    career_consequences?: {
        unlocked_now: string[]
        blocked_now: string[]
        salary_multiplier: number
        total_unlocked: number
        total_blocked: number
    }
    message: string
}

export interface LessonGameQuestion {
    id: string
    prompt: string
    options: string[]
    correct_option_index: number
    explanation: string
    learning_point: string
}

export interface LessonGameDetails {
    game_id: string
    lesson_id: string
    title: string
    game_type: string
    description: string
    objectives: string[]
    difficulty: string
    estimated_duration_minutes: number
    content?: any
    questions?: LessonGameQuestion[]
}

export interface DomainReadiness {
    domain: string
    score: number  // 0-100
    games_completed: number
    recent_performance: number
    trend: string  // "improving" | "stable" | "declining"
}

export interface GameRecommendation {
    game_id: string
    title: string
    course_id: string
    reason: string
}

export interface Badge {
    id: string
    name: string
    description: string
    icon: string
    category: string
    tier: number
}

export interface LifeReadinessAnalytics {
    overall_score: number  // 0-100
    domains: DomainReadiness[]
    total_games_completed: number
    average_game_score: number
    readiness_level: string  // "beginner" | "developing" | "proficient" | "expert"
    strengths: string[]
    areas_for_growth: string[]
    career_ready: boolean
    career_salary_impact: number
    score_change_since_last_snapshot: number
    momentum: 'up' | 'flat' | 'down'
    next_readiness_target: number
    points_to_next_target: number
    coaching_tip: string
    recommended_next_games: GameRecommendation[]
    achievement_badges: string[]  // Badge IDs
    newly_earned_badges: string[]  // NEW badges since last check
}

export interface ReadinessSnapshot {
    semester: number
    overall_score: number
    domains: Record<string, number>
    total_games: number
    timestamp: number | null
}

export interface LifeReadinessResponse {
    player_id: string
    player_name: string
    semester: number
    analytics: LifeReadinessAnalytics
    readiness_history: ReadinessSnapshot[]  // Historical trend data
}

// Player Management
export async function createPlayer(
    name: string,
    collegeId: string,
    majorId: string,
    hsGpa: number = 3.0,
    startingBalance: number = 5000,
    age: number = 18,
    housingOptionId: string = 'dorm_standard'
): Promise<Player> {
    const response = await fetch(`${API_BASE}/player/start`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            name,
            college_id: collegeId,
            major_id: majorId,
            age,
            hs_gpa: hsGpa,
            parent_income: 60000,
            starting_balance: startingBalance,
            housing_option_id: housingOptionId,
            job_id: null,
        }),
    })
    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}))
        throw new Error(`Failed to create player: ${response.statusText} - ${JSON.stringify(errorData)}`)
    }
    return response.json()
}

export async function getPlayer(playerId: string): Promise<Player> {
    const response = await fetch(`${API_BASE}/player/${playerId}`)
    if (!response.ok) throw new Error(`Failed to fetch player: ${response.statusText}`)
    return response.json()
}

// Tutorial Management
export async function getTutorialSequence(): Promise<{ sequence: TutorialStep[]; total_steps: number }> {
    // Note: getTutorialSequence is deprecated. Use startTutorial instead.
    // This is kept for backward compatibility but may not return expected data.
    return {
        sequence: [],
        total_steps: 0
    }
}

export async function startTutorial(playerId: string): Promise<any> {
    const response = await fetch(`${API_BASE}/tutorial/${playerId}/start`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    })
    if (!response.ok) throw new Error(`Failed to start tutorial: ${response.statusText}`)
    return response.json()
}

export async function getTutorial(stepId: string): Promise<TutorialStep> {
    // Deprecated: tutorial system now uses quest-based progression via /tutorial/{player_id}/start
    // This function is kept for backward compatibility only
    return {
        step_id: stepId,
        title: 'Tutorial Step',
        description: 'This endpoint is deprecated',
        context: 'deprecated',
        priority: 0
    }
}

export async function getContextTutorials(_context: string): Promise<{ tutorials: TutorialStep[]; count: number }> {
    // Deprecated: tutorial system now uses quest-based progression
    return {
        tutorials: [],
        count: 0
    }
}

export async function completeTutorial(_playerId: string, _stepId: string): Promise<any> {
    // Deprecated: use submitTutorialGame instead for the new quest system
    return { status: 'deprecated' }
}

export async function getTutorialProgress(playerId: string): Promise<any> {
    const response = await fetch(`${API_BASE}/tutorial/${playerId}/progress`)
    if (!response.ok) throw new Error(`Failed to fetch progress: ${response.statusText}`)
    return response.json()
}

export async function submitTutorialGame(playerId: string, gameId: string, answers: any[]): Promise<any> {
    const response = await fetch(`${API_BASE}/tutorial/submit`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ player_id: playerId, game_id: gameId, answers }),
    })
    if (!response.ok) throw new Error(`Failed to submit tutorial game: ${response.statusText}`)
    return response.json()
}

export async function skipTutorial(playerId: string): Promise<any> {
    const response = await fetch(`${API_BASE}/tutorial/${playerId}/skip`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    })
    if (!response.ok) throw new Error(`Failed to skip tutorial: ${response.statusText}`)
    return response.json()
}

// Tooltip Management (Deprecated - onboarding endpoints no longer exist)
export async function getAllTooltips(): Promise<{ [key: string]: Tooltip }> {
    // Note: Tooltip endpoints have been removed in favor of quest-based tutorial system
    return {}
}

export async function getTooltip(tooltipId: string): Promise<Tooltip> {
    // Note: Tooltip endpoints have been removed in favor of quest-based tutorial system
    return {
        tooltip_id: tooltipId,
        label: 'Deprecated',
        content: 'This endpoint no longer exists',
        related_concept: 'tutorial-quests'
    }
}

export async function dismissTooltip(_playerId: string, _tooltipId: string): Promise<any> {
    // Note: Tooltip endpoints have been removed in favor of quest-based tutorial system
    return { status: 'deprecated' }
}

export async function enableTutorials(playerId: string): Promise<any> {
    // Enable tutorials - in new system, call startTutorial instead
    return startTutorial(playerId)
}

export async function disableTutorials(playerId: string): Promise<any> {
    // Now use skipTutorial instead - this is kept for backward compatibility
    return skipTutorial(playerId)
}

// Catalog Functions
export async function getColleges(): Promise<any> {
    const response = await fetch(`${API_BASE}/catalogs/colleges`)
    if (!response.ok) throw new Error(`Failed to fetch colleges: ${response.statusText}`)
    return response.json()
}

export async function getMajors(): Promise<any> {
    const response = await fetch(`${API_BASE}/catalogs/majors`)
    if (!response.ok) throw new Error(`Failed to fetch majors: ${response.statusText}`)
    return response.json()
}

// Academic Functions
export async function attendClass(courseId: string): Promise<any> {
    const response = await fetch(`${API_BASE}/curriculum/attend-class`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ course_id: courseId }),
    })
    if (!response.ok) throw new Error(`Failed to attend class: ${response.statusText}`)
    return response.json()
}

export async function getCourseContent(courseId: string): Promise<any> {
    const response = await fetch(`${API_BASE}/curriculum/courses/${courseId}`)
    if (!response.ok) throw new Error(`Failed to fetch course content: ${response.statusText}`)
    return response.json()
}

export async function getMiniGamesForCourse(courseId: string, playerId?: string): Promise<{ course_id: string; games: MiniGameSummary[]; total_games?: number; message: string }> {
    const query = playerId ? `?player_id=${encodeURIComponent(playerId)}` : ''
    const response = await fetch(`${API_BASE}/curriculum/games/course/${courseId}${query}`)
    if (!response.ok) throw new Error(`Failed to fetch mini-games: ${response.statusText}`)
    return response.json()
}

export async function getMiniGameDetails(gameId: string): Promise<MiniGameDetails> {
    const response = await fetch(`${API_BASE}/curriculum/games/${gameId}`)
    if (!response.ok) throw new Error(`Failed to fetch mini-game details: ${response.statusText}`)
    return response.json()
}

export async function markMiniGameSeen(playerId: string, gameId: string, courseId: string): Promise<any> {
    const response = await fetch(`${API_BASE}/curriculum/games/seen?player_id=${encodeURIComponent(playerId)}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ game_id: gameId, course_id: courseId }),
    })
    if (!response.ok) throw new Error(`Failed to mark game as seen: ${response.statusText}`)
    return response.json()
}

export async function getLifeReadinessAnalytics(playerId: string): Promise<LifeReadinessResponse> {
    const response = await fetch(`${API_BASE}/curriculum/analytics/${playerId}`)
    if (!response.ok) throw new Error(`Failed to fetch life readiness analytics: ${response.statusText}`)
    return response.json()
}

export async function submitMiniGame(
    playerId: string,
    payload: {
        game_id: string
        course_id: string
        answers: MiniGameSubmissionAnswer[]
        time_spent_minutes: number
    }
): Promise<MiniGameSubmissionResult> {
    const response = await fetch(`${API_BASE}/curriculum/games/submit?player_id=${encodeURIComponent(playerId)}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
    })
    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}))
        throw new Error(errorData.detail || `Failed to submit mini-game: ${response.statusText}`)
    }
    return response.json()
}

export async function getLessonGame(lessonId: string): Promise<LessonGameDetails> {
    const response = await fetch(`${API_BASE}/curriculum/lessons/${encodeURIComponent(lessonId)}/game`)
    if (!response.ok) throw new Error(`Failed to fetch lesson game: ${response.statusText}`)
    return response.json()
}

export async function submitLessonGame(
    lessonId: string,
    payload: { score: number; max_score: number }
): Promise<any> {
    const response = await fetch(`${API_BASE}/curriculum/lessons/${encodeURIComponent(lessonId)}/game/submit`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
    })
    if (!response.ok) throw new Error(`Failed to submit lesson game: ${response.statusText}`)
    return response.json()
}