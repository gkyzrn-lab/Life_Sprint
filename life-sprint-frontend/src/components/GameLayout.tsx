import { useState } from 'react'
import '../styles/GameLayout.css'
import { CharacterCard } from './CharacterCard'
import { AgeProgression } from './AgeProgression'
import { FinancialDashboard } from './FinancialDashboard'
import { LifeTimeline, LifeEvent } from './LifeTimeline'
import { DecisionCard } from './DecisionCard'
import { BadgesPanel, Badge } from './BadgesPanel'
import { QuestsPanel, Quest } from './QuestsPanel'

interface DecisionOptionData {
    id: string
    text: string
    outcome?: string
}

interface DecisionData {
    title: string
    description: string
    image?: string
    options: DecisionOptionData[]
}

export interface GameLayoutProps {
    playerName: string
    age: number
    year: number
    stats: {
        health: number
        happiness: number
        intelligence: number
        attractiveness: number
    }
    finance: {
        cash: number
        savings: number
        investments: number
        loans: number
        netWorth: number
    }
    events?: LifeEvent[]
    decision?: DecisionData
    badges?: Badge[]
    quests?: Quest[]
    onDecisionSelect?: (optionId: string) => void
    onLogout?: () => void
}

export function GameLayout({
    playerName,
    age,
    year,
    stats,
    finance,
    events,
    decision,
    badges,
    quests,
    onDecisionSelect,
    onLogout,
}: GameLayoutProps) {
    const [activePanel, setActivePanel] = useState<'overview' | 'life' | 'finances' | 'decisions' | 'badges' | 'quests'>('overview')
    const timelineEvents: LifeEvent[] = events && events.length > 0 ? events : [
        { age: 18, year: 2020, title: 'College Start', description: 'Began your college journey', type: 'education', icon: '🎓' },
        { age: 20, year: 2022, title: 'First Job', description: 'Landed your first internship', type: 'career', icon: '💼' },
        { age: 22, year: 2024, title: 'Graduation', description: 'Completed your degree', type: 'achievement', icon: '🏆' },
    ]
    const badgeList: Badge[] = badges && badges.length > 0 ? badges : [
        { id: 'starter', title: 'Getting Started', description: 'Begin your journey.', icon: '✨', earned: true, rarity: 'common' },
        { id: 'future', title: 'Future Planner', description: 'Set your first goal.', icon: '🗺️', earned: false, rarity: 'rare', progress: 1, goal: 3 },
    ]
    const questList: Quest[] = quests && quests.length > 0 ? quests : [
        { id: 'quest-1', title: 'Build Momentum', description: 'Make 3 life decisions.', icon: '🎯', progress: 1, goal: 3, reward: '+5 Happiness' },
        { id: 'quest-2', title: 'Save $500', description: 'Grow your savings.', icon: '💰', progress: 200, goal: 500, reward: '+$50 Bonus', unit: 'money' },
    ]
    const decisionData = decision || {
        title: 'Life Decision',
        description: 'Choose your next path carefully. Each decision shapes your future.',
        options: [
            { id: '1', text: 'Pursue Higher Education', outcome: '+Intelligence, -Cash' },
            { id: '2', text: 'Start Working', outcome: '+Cash, -Health' },
            { id: '3', text: 'Take a Gap Year', outcome: '+Happiness, -Career Growth' },
        ],
    }

    return (
        <div className="bitlife-layout">
            {/* Top Info Bar */}
            <div className="info-bar">
                <div className="info-title">
                    <span className="game-name">Life Sprint</span>
                    {onLogout && (
                        <button className="logout-btn" onClick={onLogout}>Logout</button>
                    )}
                </div>
                <div className="info-section">
                    <span className="info-label">Age</span>
                    <span className="info-value">{age}</span>
                </div>
                <div className="info-section">
                    <span className="info-label">Year</span>
                    <span className="info-value">{year}</span>
                </div>
                <div className="info-section">
                    <span className="info-label">Net Worth</span>
                    <span className="info-value accent">${(finance.netWorth / 1000000).toFixed(1)}M</span>
                </div>
                <div className="info-section">
                    <span className="info-label">Health</span>
                    <div className="mini-stat-bar">
                        <div className="mini-bar-fill" style={{ width: `${stats.health}%`, backgroundColor: '#7ED321' }} />
                    </div>
                </div>
                <div className="info-section">
                    <span className="info-label">Happiness</span>
                    <div className="mini-stat-bar">
                        <div className="mini-bar-fill" style={{ width: `${stats.happiness}%`, backgroundColor: '#FFD700' }} />
                    </div>
                </div>
            </div>

            {/* Main Content */}
            <div className="main-layout">
                {/* Left Sidebar - Character & Timeline */}
                <aside className="sidebar-left">
                    {activePanel === 'overview' && (
                        <CharacterCard
                            name={playerName}
                            stats={{
                                health: stats.health,
                                happiness: stats.happiness,
                                intelligence: stats.intelligence,
                                attractiveness: stats.attractiveness,
                                age: age,
                                net_worth: finance.netWorth
                            }}
                        />
                    )}

                    {activePanel === 'life' && (
                        <LifeTimeline
                            currentAge={age}
                            events={timelineEvents}
                        />
                    )}

                    {activePanel === 'finances' && (
                        <FinancialDashboard
                            data={{
                                cash: finance.cash,
                                savings: finance.savings,
                                investments: finance.investments,
                                loans: finance.loans,
                                netWorth: finance.netWorth,
                            }}
                        />
                    )}

                    {activePanel === 'decisions' && (
                        <DecisionCard
                            title={decisionData.title}
                            description={decisionData.description}
                            image={decisionData.image}
                            options={decisionData.options}
                            onSelect={(id) => (onDecisionSelect ? onDecisionSelect(id) : console.log('Selected:', id))}
                        />
                    )}

                    {activePanel === 'badges' && (
                        <BadgesPanel badges={badgeList} />
                    )}

                    {activePanel === 'quests' && (
                        <QuestsPanel quests={questList} />
                    )}
                </aside>

                {/* Center - Age & Progression */}
                <main className="main-content">
                    <AgeProgression currentAge={age} currentYear={year} />
                </main>

                {/* Right Sidebar - Navigation */}
                <aside className="sidebar-right">
                    <nav className="panel-nav">
                        <button
                            className={`panel-btn ${activePanel === 'overview' ? 'active' : ''}`}
                            onClick={() => setActivePanel('overview')}
                        >
                            <span className="btn-icon">👤</span>
                            <span className="btn-label">Profile</span>
                        </button>
                        <button
                            className={`panel-btn ${activePanel === 'life' ? 'active' : ''}`}
                            onClick={() => setActivePanel('life')}
                        >
                            <span className="btn-icon">📜</span>
                            <span className="btn-label">History</span>
                        </button>
                        <button
                            className={`panel-btn ${activePanel === 'finances' ? 'active' : ''}`}
                            onClick={() => setActivePanel('finances')}
                        >
                            <span className="btn-icon">💰</span>
                            <span className="btn-label">Finance</span>
                        </button>
                        <button
                            className={`panel-btn ${activePanel === 'decisions' ? 'active' : ''}`}
                            onClick={() => setActivePanel('decisions')}
                        >
                            <span className="btn-icon">🎯</span>
                            <span className="btn-label">Options</span>
                        </button>
                        <button
                            className={`panel-btn ${activePanel === 'badges' ? 'active' : ''}`}
                            onClick={() => setActivePanel('badges')}
                        >
                            <span className="btn-icon">🏅</span>
                            <span className="btn-label">Badges</span>
                        </button>
                        <button
                            className={`panel-btn ${activePanel === 'quests' ? 'active' : ''}`}
                            onClick={() => setActivePanel('quests')}
                        >
                            <span className="btn-icon">🗺️</span>
                            <span className="btn-label">Quests</span>
                        </button>
                    </nav>

                    <div className="quick-stats">
                        <div className="quick-stat">
                            <span>💪</span>
                            <div>
                                <p>Strength</p>
                                <p className="value">{Math.round(stats.intelligence)}</p>
                            </div>
                        </div>
                        <div className="quick-stat">
                            <span>🧠</span>
                            <div>
                                <p>Mind</p>
                                <p className="value">{Math.round(stats.intelligence)}</p>
                            </div>
                        </div>
                        <div className="quick-stat">
                            <span>❤️</span>
                            <div>
                                <p>Charm</p>
                                <p className="value">{Math.round(stats.attractiveness)}</p>
                            </div>
                        </div>
                    </div>
                </aside>
            </div>
        </div>
    )
}
