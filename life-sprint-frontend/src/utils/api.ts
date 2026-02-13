const API_BASE = import.meta.env.DEV ? 'http://localhost:8000' : '/api'

export interface Player {
    id: string
    name: string
    age: number
    hs_gpa: float
    parent_income: float
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

// Player Management
export async function createPlayer(name: string, collegeId: string, majorId: string): Promise<Player> {
    const response = await fetch(`${API_BASE}/player/start`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            name,
            college_id: collegeId,
            major_id: majorId,
            housing_option_id: 'dorm',
            job_id: null,
        }),
    })
    if (!response.ok) throw new Error(`Failed to create player: ${response.statusText}`)
    return response.json()
}

export async function getPlayer(playerId: string): Promise<Player> {
    const response = await fetch(`${API_BASE}/player/${playerId}`)
    if (!response.ok) throw new Error(`Failed to fetch player: ${response.statusText}`)
    return response.json()
}

// Tutorial Management
export async function getTutorialSequence(): Promise<{ sequence: TutorialStep[]; total_steps: number }> {
    const response = await fetch(`${API_BASE}/onboarding/tutorial-sequence`)
    if (!response.ok) throw new Error(`Failed to fetch tutorials: ${response.statusText}`)
    return response.json()
}

export async function getTutorial(stepId: string): Promise<TutorialStep> {
    const response = await fetch(`${API_BASE}/onboarding/tutorial/${stepId}`)
    if (!response.ok) throw new Error(`Failed to fetch tutorial: ${response.statusText}`)
    return response.json()
}

export async function getContextTutorials(context: string): Promise<{ tutorials: TutorialStep[]; count: number }> {
    const response = await fetch(`${API_BASE}/onboarding/tutorials/context/${context}`)
    if (!response.ok) throw new Error(`Failed to fetch context tutorials: ${response.statusText}`)
    return response.json()
}

export async function completeTutorial(playerId: string, stepId: string): Promise<any> {
    const response = await fetch(`${API_BASE}/onboarding/tutorial/complete`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ player_id: playerId, step_id: stepId }),
    })
    if (!response.ok) throw new Error(`Failed to complete tutorial: ${response.statusText}`)
    return response.json()
}

export async function getTutorialProgress(playerId: string): Promise<any> {
    const response = await fetch(`${API_BASE}/onboarding/${playerId}/progress`)
    if (!response.ok) throw new Error(`Failed to fetch progress: ${response.statusText}`)
    return response.json()
}

// Tooltip Management
export async function getAllTooltips(): Promise<{ [key: string]: Tooltip }> {
    const response = await fetch(`${API_BASE}/onboarding/tooltips`)
    if (!response.ok) throw new Error(`Failed to fetch tooltips: ${response.statusText}`)
    return response.json()
}

export async function getTooltip(tooltipId: string): Promise<Tooltip> {
    const response = await fetch(`${API_BASE}/onboarding/tooltip/${tooltipId}`)
    if (!response.ok) throw new Error(`Failed to fetch tooltip: ${response.statusText}`)
    return response.json()
}

export async function dismissTooltip(playerId: string, tooltipId: string): Promise<any> {
    const response = await fetch(`${API_BASE}/onboarding/tooltip/dismiss`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ player_id: playerId, tooltip_id: tooltipId }),
    })
    if (!response.ok) throw new Error(`Failed to dismiss tooltip: ${response.statusText}`)
    return response.json()
}

export async function enableTutorials(playerId: string): Promise<any> {
    const response = await fetch(`${API_BASE}/onboarding/${playerId}/enable-tutorials`, {
        method: 'POST',
    })
    if (!response.ok) throw new Error(`Failed to enable tutorials: ${response.statusText}`)
    return response.json()
}

export async function disableTutorials(playerId: string): Promise<any> {
    const response = await fetch(`${API_BASE}/onboarding/${playerId}/disable-tutorials`, {
        method: 'POST',
    })
    if (!response.ok) throw new Error(`Failed to disable tutorials: ${response.statusText}`)
    return response.json()
}
