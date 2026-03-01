const API_BASE = import.meta.env.DEV ? 'http://localhost:8000' : '/api'

type CacheEntry<T> = {
    data: T
    expiresAt: number
}

const responseCache = new Map<string, CacheEntry<unknown>>()
const inflightRequests = new Map<string, Promise<unknown>>()
const DEFAULT_CACHE_TTL_MS = 15000

function getCached<T>(key: string): CacheEntry<T> | null {
    const entry = responseCache.get(key)
    if (!entry) return null
    return entry as CacheEntry<T>
}

function setCached<T>(key: string, data: T, ttlMs: number = DEFAULT_CACHE_TTL_MS): void {
    responseCache.set(key, {
        data,
        expiresAt: Date.now() + ttlMs,
    })
}

async function fetchJsonWithCache<T>(
    key: string,
    url: string,
    options?: {
        ttlMs?: number
        forceRefresh?: boolean
        staleWhileRevalidate?: boolean
    },
): Promise<T> {
    const ttlMs = options?.ttlMs ?? DEFAULT_CACHE_TTL_MS
    const staleWhileRevalidate = options?.staleWhileRevalidate ?? true
    const now = Date.now()
    const cached = getCached<T>(key)

    if (!options?.forceRefresh && cached && cached.expiresAt > now) {
        return cached.data
    }

    const existingInflight = inflightRequests.get(key) as Promise<T> | undefined
    if (existingInflight) {
        if (cached && staleWhileRevalidate && !options?.forceRefresh) {
            return cached.data
        }
        return existingInflight
    }

    const networkPromise = (async () => {
        const response = await fetch(url)
        if (!response.ok) throw new Error(`Request failed: ${response.statusText}`)
        const data = await response.json() as T
        setCached(key, data, ttlMs)
        return data
    })().finally(() => {
        inflightRequests.delete(key)
    })

    inflightRequests.set(key, networkPromise)

    if (cached && staleWhileRevalidate && !options?.forceRefresh) {
        return cached.data
    }

    return networkPromise
}

export function getApiBase(): string {
    return API_BASE
}

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

export interface FinanceLoanRecord {
    id: string
    loan_type: 'subsidized' | 'unsubsidized' | 'private' | string
    principal: number
    annual_interest_rate: number
    accrued_interest: number
    in_school: boolean
    grace_months_remaining: number
    repayment_months_remaining: number
    minimum_payment: number
}

export interface FinanceBorrowResponse {
    player_id: string
    borrowed_total: number
    remaining_uncovered: number
    new_balance: number
    loans: FinanceLoanRecord[]
}

export interface FinanceProfileResponse {
    player_id: string
    repayment_profile: {
        plan_type: 'standard' | 'idr' | string
        annual_income: number
        family_size: number
        poverty_line_annual: number
        discretionary_multiplier: number
        idr_percent: number
        payment_cap_to_standard: boolean
    }
}

export interface FinanceRepayResponse {
    player_id: string
    months: number
    total_paid: number
    ending_balance: number
    total_principal_remaining: number
    loans: FinanceLoanRecord[]
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

export async function getPlayer(playerId: string, options?: { forceRefresh?: boolean }): Promise<Player> {
    return fetchJsonWithCache<Player>(
        `player:${playerId}`,
        `${API_BASE}/player/${playerId}`,
        {
            ttlMs: 8000,
            forceRefresh: options?.forceRefresh,
            staleWhileRevalidate: true,
        },
    )
}

// Finance Tools
export async function financeBorrow(playerId: string, neededAmount: number): Promise<FinanceBorrowResponse> {
    const response = await fetch(`${API_BASE}/finance/borrow`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ player_id: playerId, needed_amount: neededAmount }),
    })
    if (!response.ok) throw new Error(`Failed to borrow funds: ${response.statusText}`)
    return response.json()
}

export async function financeAccrueInSchoolInterest(playerId: string, months = 4): Promise<{ player_id: string; months: number; loans: FinanceLoanRecord[] }> {
    const response = await fetch(`${API_BASE}/finance/accrue-in-school-interest?player_id=${encodeURIComponent(playerId)}&months=${encodeURIComponent(String(months))}`, {
        method: 'POST',
    })
    if (!response.ok) throw new Error(`Failed to accrue in-school interest: ${response.statusText}`)
    return response.json()
}

export async function financeStartRepayment(playerId: string): Promise<{ player_id: string; status: string; loans: FinanceLoanRecord[] }> {
    const response = await fetch(`${API_BASE}/finance/start-repayment?player_id=${encodeURIComponent(playerId)}`, {
        method: 'POST',
    })
    if (!response.ok) throw new Error(`Failed to start repayment: ${response.statusText}`)
    return response.json()
}

export async function financeSetRepaymentProfile(
    playerId: string,
    planType: 'standard' | 'idr',
    annualIncome: number,
    familySize = 1,
): Promise<FinanceProfileResponse> {
    const response = await fetch(`${API_BASE}/finance/set-repayment-profile`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            player_id: playerId,
            plan_type: planType,
            annual_income: annualIncome,
            family_size: familySize,
        }),
    })
    if (!response.ok) throw new Error(`Failed to set repayment profile: ${response.statusText}`)
    return response.json()
}

export async function financeRepayMonths(playerId: string, months: number): Promise<FinanceRepayResponse> {
    const response = await fetch(`${API_BASE}/finance/repay-months`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ player_id: playerId, months }),
    })
    if (!response.ok) throw new Error(`Failed to process repayment: ${response.statusText}`)
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
    return fetchJsonWithCache<LifeReadinessResponse>(
        `analytics:${playerId}`,
        `${API_BASE}/curriculum/analytics/${playerId}`,
        {
            ttlMs: 12000,
            staleWhileRevalidate: true,
        },
    )
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

// Exams & Progression
export async function getSemesterExamStatus(playerId: string): Promise<any> {
    const response = await fetch(`${API_BASE}/exams/semester-exam-status?player_id=${encodeURIComponent(playerId)}`)
    if (!response.ok) throw new Error(`Failed to load exam status: ${response.statusText}`)
    return response.json()
}

export async function generateSemesterExam(playerId: string, numQuestions: number = 5): Promise<any> {
    const response = await fetch(`${API_BASE}/exams/semester-exam/generate?player_id=${encodeURIComponent(playerId)}&num_questions=${numQuestions}`, {
        method: 'POST',
    })
    if (!response.ok) throw new Error(`Failed to generate exam: ${response.statusText}`)
    return response.json()
}

export interface SemesterExamSubmission {
    player_id: string
    answers: Array<{
        question_id: string
        chosen_choice_id: string
    }>
}

export async function submitSemesterExam(payload: SemesterExamSubmission): Promise<any> {
    const response = await fetch(`${API_BASE}/exams/semester-exam/submit`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
    })
    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}))
        throw new Error(errorData.detail || `Failed to submit exam: ${response.statusText}`)
    }
    return response.json()
}

export async function canProgressSemester(playerId: string): Promise<any> {
    const response = await fetch(`${API_BASE}/exams/can-progress-semester?player_id=${encodeURIComponent(playerId)}`)
    if (!response.ok) throw new Error(`Failed to check progression: ${response.statusText}`)
    return response.json()
}

export async function advanceSemester(playerId: string): Promise<any> {
    const response = await fetch(`${API_BASE}/progress/advance`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ player_id: playerId }),
    })
    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}))
        throw new Error(errorData.detail || `Failed to advance semester: ${response.statusText}`)
    }
    return response.json()
}

export async function prefetchFinanceData(playerId: string): Promise<void> {
    try {
        await getPlayer(playerId)
    } catch {
        // silent prefetch
    }
}

export async function prefetchAnalyticsData(playerId: string): Promise<void> {
    try {
        await getLifeReadinessAnalytics(playerId)
    } catch {
        // silent prefetch
    }
}

export async function prefetchStoreData(playerId: string): Promise<void> {
    try {
        await Promise.allSettled([
            fetch(`${API_BASE}/api/store/available?player_id=${encodeURIComponent(playerId)}`),
            fetch(`${API_BASE}/api/store/suggestions?player_id=${encodeURIComponent(playerId)}`),
            fetch(`${API_BASE}/api/store/history?player_id=${encodeURIComponent(playerId)}`),
        ])
    } catch {
        // silent prefetch
    }
}