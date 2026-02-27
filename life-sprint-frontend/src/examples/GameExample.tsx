/**
 * Complete Example: Integrating BitLife-Style Components with Backend
 * 
 * This example shows how to connect all the visual components with your
 * Python backend API to create a fully functional financial education game.
 */

import { useState, useEffect } from 'react'
import {
    GameLayout,
    CharacterCard,
    AgeProgression,
    FinancialDashboard,
    LifeTimeline,
    DecisionCard,
} from '../components'
import { Player, api } from '../utils/api'

/**
 * FullGameExample - Complete integration of all visual components
 * Shows how to fetch data from the Python backend and manage game state
 */
export function FullGameExample() {
    const [player, setPlayer] = useState<Player | null>(null)
    const [events, setEvents] = useState<any[]>([])
    const [currentDecision, setCurrentDecision] = useState<any>(null)
    const [loading, setLoading] = useState(true)

    // 1. INITIAL DATA FETCH
    useEffect(() => {
        const loadPlayer = async () => {
            try {
                // Fetch player from backend
                const response = await api.get('/api/players/me')
                const playerData = response.data
                setPlayer(playerData)

                // Fetch player events/history
                const eventsResponse = await api.get(`/api/players/${playerData.id}/history`)
                setEvents(eventsResponse.data)

                // Fetch current decision/choice scenario
                const decisionResponse = await api.get(`/api/players/${playerData.id}/current-decision`)
                if (decisionResponse.status === 200) {
                    setCurrentDecision(decisionResponse.data)
                }
            } catch (error) {
                console.error('Failed to load player:', error)
            } finally {
                setLoading(false)
            }
        }

        loadPlayer()
    }, [])

    if (loading) {
        return <div>Loading game...</div>
    }

    if (!player) {
        return <div>Error loading player data</div>
    }

    // 2. TRANSFORM BACKEND DATA FOR COMPONENTS

    // Character stats from player.stats model
    const characterStats = {
        health: player.stats?.health || 50,
        happiness: 75, // Could come from player.stats.happiness
        intelligence: (player.stats?.gpa || 3.0) / 4.0 * 100,
        attractiveness: 60,
        age: player.age,
        net_worth: player.finance?.balance || 0,
    }

    // Financial data from player.finance model
    const financialData = {
        cash: player.finance?.balance || 0,
        savings: Math.max(0, (player.finance?.balance || 0) * 0.3),
        investments: Math.max(0, (player.finance?.balance || 0) * 0.2),
        loans: player.finance?.loan_balance || 0,
        netWorth: (player.finance?.balance || 0) - (player.finance?.loan_balance || 0),
        salary: 0, // Could be derived from player.career
    }

    // Transform events to match LifeTimeline format
    const timelineEvents = events.map((event: any) => ({
        age: event.player_age,
        year: event.year,
        title: event.title,
        description: event.description,
        type: mapEventType(event.event_type),
        icon: getEventIcon(event.event_type),
    }))

    // Decision options with calculated consequences
    const decisionOptions = currentDecision?.options?.map((option: any) => ({
        id: option.id,
        text: option.text,
        outcome: formatOutcome(option.effects),
        consequences: option.effects || {},
    })) || []

    // 3. EVENT HANDLERS

    const handleDecisionSelect = async (optionId: string) => {
        try {
            // Submit decision to backend
            const result = await api.post(
                `/api/players/${player.id}/decisions`,
                {
                    decision_id: currentDecision.id,
                    option_id: optionId,
                }
            )

            // Update local player state with changes
            setPlayer(result.data.player)

            // Record the event
            if (result.data.event) {
                setEvents([...events, result.data.event])
            }

            // Load next decision
            const nextDecisionResponse = await api.get(
                `/api/players/${player.id}/current-decision`
            )
            if (nextDecisionResponse.status === 200) {
                setCurrentDecision(nextDecisionResponse.data)
            } else {
                setCurrentDecision(null)
            }
        } catch (error) {
            console.error('Failed to submit decision:', error)
        }
    }

    const handleProgressAge = async () => {
        try {
            // Advance to next semester/year
            const result = await api.post(`/api/players/${player.id}/progress`)
            setPlayer(result.data.player)

            if (result.data.events) {
                setEvents([...events, ...result.data.events])
            }
        } catch (error) {
            console.error('Failed to progress:', error)
        }
    }

    // 4. RENDER WITH GAME LAYOUT

    return (
        <div>
            <GameLayout
                playerName={player.name}
                age={player.age}
                year={new Date().getFullYear()}
                stats={{
                    health: characterStats.health,
                    happiness: characterStats.happiness,
                    intelligence: characterStats.intelligence,
                    attractiveness: characterStats.attractiveness,
                }}
                finance={{
                    cash: financialData.cash,
                    savings: financialData.savings,
                    investments: financialData.investments,
                    loans: financialData.loans,
                    netWorth: financialData.netWorth,
                }}
            />

            {/* Modal or overlay for current decision */}
            {currentDecision && (
                <DecisionModal
                    decision={currentDecision}
                    options={decisionOptions}
                    onSelect={handleDecisionSelect}
                />
            )}

            {/* Timeline preview using mapped events */}
            {timelineEvents.length > 0 && (
                <div className="timeline-preview">
                    <LifeTimeline currentAge={player.age} events={timelineEvents} />
                </div>
            )}

            {/* Optional: Progress button */}
            <button onClick={handleProgressAge} className="progress-btn">
                Next Semester →
            </button>
        </div>
    )
}

/**
 * Example component showing individual component usage
 */
export function ComponentShowcase() {
    const samplePlayer = {
        name: 'Alex Chen',
        age: 22,
        year: 2024,
    }

    const sampleStats = {
        health: 75,
        happiness: 82,
        intelligence: 88,
        attractiveness: 72,
        age: 22,
        net_worth: 36000,
    }

    const sampleFinance = {
        cash: 45000,
        savings: 15000,
        investments: 8000,
        loans: 32000,
        netWorth: 36000,
    }

    const sampleEvents = [
        {
            age: 18,
            year: 2020,
            title: 'Started College',
            description: 'Enrolled in Computer Science program',
            type: 'education' as const,
            icon: '🎓',
        },
        {
            age: 20,
            year: 2022,
            title: 'First Internship',
            description: 'Completed internship at TechCorp',
            type: 'career' as const,
            icon: '💼',
        },
        {
            age: 21,
            year: 2023,
            title: 'Emergency Fund Started',
            description: 'Saved $3,000 emergency fund',
            type: 'financial' as const,
            icon: '💰',
        },
        {
            age: 22,
            year: 2024,
            title: 'Got Full-Time Offer',
            description: 'Accepted job at Google with $150k salary',
            type: 'achievement' as const,
            icon: '🏆',
        },
    ]

    const sampleDecision = {
        title: 'Post-Graduation Career Decision',
        description: 'You received multiple job offers. Which one do you choose?',
        options: [
            {
                id: '1',
                text: 'Join FAANG company: $150k salary, high stress',
                outcome: '+$120k/year, -Health',
            },
            {
                id: '2',
                text: 'Startup position: $80k + equity, low stress',
                outcome: '+Happiness, +Growth potential',
            },
            {
                id: '3',
                text: 'Non-profit role: $60k, meaningful work',
                outcome: '+Happiness, +Intelligence',
            },
        ],
    }

    return (
        <div className="showcase">
            {/* Row 1: Character Card & Age Progression */}
            <div className="row">
                <CharacterCard name={samplePlayer.name} stats={sampleStats} />
                <AgeProgression currentAge={samplePlayer.age} currentYear={samplePlayer.year} />
            </div>

            {/* Row 2: Financial Dashboard */}
            <div className="row">
                <FinancialDashboard data={sampleFinance} income={7000} expenses={2000} />
            </div>

            {/* Row 3: Timeline */}
            <div className="row">
                <LifeTimeline currentAge={samplePlayer.age} events={sampleEvents} />
            </div>

            {/* Row 4: Decision Card */}
            <div className="row">
                <DecisionCard
                    title={sampleDecision.title}
                    description={sampleDecision.description}
                    options={sampleDecision.options}
                    onSelect={(id: string) => console.log('Selected:', id)}
                />
            </div>
        </div>
    )
}

/**
 * Helper Functions
 */

/**
 * Map backend event types to component event types
 */
function mapEventType(
    backendType: string
): 'achievement' | 'career' | 'education' | 'relationship' | 'financial' | 'health' {
    const typeMap: Record<
        string,
        'achievement' | 'career' | 'education' | 'relationship' | 'financial' | 'health'
    > = {
        graduation: 'achievement',
        job_offer: 'career',
        internship: 'career',
        admission: 'education',
        course_completed: 'education',
        scholarship_awarded: 'financial',
        loan_taken: 'financial',
        promotion: 'career',
        relationship_start: 'relationship',
        relationship_end: 'relationship',
        health_incident: 'health',
        fitness_milestone: 'health',
    }

    return typeMap[backendType] || 'achievement'
}

/**
 * Get emoji icon for event type
 */
function getEventIcon(eventType: string): string {
    const iconMap: Record<string, string> = {
        graduation: '🎓',
        job_offer: '💼',
        internship: '💼',
        admission: '📚',
        course_completed: '✅',
        scholarship_awarded: '🏆',
        loan_taken: '💳',
        promotion: '📈',
        relationship_start: '💕',
        relationship_end: '💔',
        health_incident: '🏥',
        fitness_milestone: '💪',
    }

    return iconMap[eventType] || '📌'
}

/**
 * Format stat changes as human-readable outcome
 */
function formatOutcome(effects: Record<string, number>): string {
    const parts: string[] = []

    Object.entries(effects).forEach(([stat, change]) => {
        if (change > 0) {
            parts.push(`+${stat}`)
        } else if (change < 0) {
            parts.push(`${stat}`)
        }
    })

    return parts.join(', ') || 'No immediate effects'
}

/**
 * Decision Modal Component
 */
interface DecisionModalProps {
    decision: any
    options: any[]
    onSelect: (optionId: string) => void
}

function DecisionModal({ decision, options, onSelect }: DecisionModalProps) {
    return (
        <div className="decision-modal-overlay">
            <DecisionCard
                title={decision.title}
                description={decision.description}
                image={decision.image}
                options={options}
                onSelect={onSelect}
            />
        </div>
    )
}

/**
 * Dashboard Component - Shows all components in a grid
 */
export function FullDashboard() {
    return (
        <div className="dashboard-grid">
            <section className="dashboard-section">
                <h2>👤 Your Profile</h2>
                <ComponentShowcase />
            </section>
        </div>
    )
}

export default FullGameExample
