import { useMemo, useState } from 'react'
import { Player, MiniGameSummary } from '../utils/api'
import './VisualExperiencePanel.css'

interface CourseLite {
    id: string
    title: string
    credits: number
    weekly_hours: number
}

interface VisualExperiencePanelProps {
    player: Player
    currentCourses: CourseLite[]
    miniGames: MiniGameSummary[]
    onJumpToAcademics: () => void
}

const clamp = (value: number, min: number, max: number) => Math.max(min, Math.min(max, value))

export default function VisualExperiencePanel({
    player,
    currentCourses,
    miniGames,
    onJumpToAcademics,
}: VisualExperiencePanelProps) {
    const [theme, setTheme] = useState<'aurora' | 'midnight'>('aurora')

    const metrics = useMemo(() => {
        const gpa = Number(player.stats?.gpa ?? 0)
        const stress = Number(player.stats?.stress ?? 0)
        const health = Number(player.stats?.health ?? 0)
        const network = Number(player.stats?.network ?? 0)
        const balance = Number(player.finance?.balance ?? 0)
        const expenses = Number(player.finance?.monthly_expenses ?? 0)

        const normalizedGpa = clamp((gpa / 4) * 100, 0, 100)
        const normalizedStress = clamp(stress, 0, 100)
        const normalizedHealth = clamp(health, 0, 100)
        const normalizedNetwork = clamp(network, 0, 100)
        const savingsRunway = expenses > 0 ? clamp((balance / expenses) * 10, 0, 100) : 100

        const readiness = clamp(
            normalizedGpa * 0.3 +
            normalizedHealth * 0.25 +
            normalizedNetwork * 0.2 +
            savingsRunway * 0.15 +
            (100 - normalizedStress) * 0.1,
            0,
            100,
        )

        return {
            gpa,
            stress,
            health,
            network,
            balance,
            expenses,
            normalizedGpa,
            normalizedStress,
            normalizedHealth,
            normalizedNetwork,
            savingsRunway,
            readiness,
        }
    }, [player])

    const achievements = useMemo(() => {
        const list = [] as Array<{ icon: string; label: string; unlocked: boolean }>
        list.push({ icon: '🎯', label: 'GPA 3.5+', unlocked: metrics.gpa >= 3.5 })
        list.push({ icon: '🧘', label: 'Stress < 40', unlocked: metrics.stress < 40 })
        list.push({ icon: '🤝', label: 'Network 60+', unlocked: metrics.network >= 60 })
        list.push({ icon: '🏦', label: '$5k Balance', unlocked: metrics.balance >= 5000 })
        list.push({ icon: '📚', label: '3+ Courses', unlocked: currentCourses.length >= 3 })
        return list
    }, [currentCourses.length, metrics])

    const gameSpotlight = useMemo(() => {
        return [...miniGames]
            .sort((a, b) => {
                const aScore = Number(a.best_score_percent ?? 0)
                const bScore = Number(b.best_score_percent ?? 0)
                return bScore - aScore
            })
            .slice(0, 3)
    }, [miniGames])

    return (
        <section className={`visual-panel visual-${theme}`}>
            <div className="visual-topbar">
                <div>
                    <h2>✨ Visual Command Center</h2>
                    <p>Dashboard, progress, achievements, mini-game highlights, and trend visuals in one place.</p>
                </div>
                <button
                    type="button"
                    className="theme-toggle"
                    onClick={() => setTheme(prev => (prev === 'aurora' ? 'midnight' : 'aurora'))}
                >
                    {theme === 'aurora' ? '🌙 Midnight Theme' : '🌈 Aurora Theme'}
                </button>
            </div>

            <div className="visual-kpis">
                <article className="vk-card">
                    <span className="vk-label">Life Readiness</span>
                    <strong>{metrics.readiness.toFixed(0)}%</strong>
                    <div className="meter"><div style={{ width: `${metrics.readiness}%` }} /></div>
                </article>
                <article className="vk-card">
                    <span className="vk-label">Academic Power</span>
                    <strong>{metrics.gpa.toFixed(2)} GPA</strong>
                    <div className="meter"><div style={{ width: `${metrics.normalizedGpa}%` }} /></div>
                </article>
                <article className="vk-card">
                    <span className="vk-label">Wellness Index</span>
                    <strong>{metrics.health.toFixed(0)}%</strong>
                    <div className="meter"><div style={{ width: `${metrics.normalizedHealth}%` }} /></div>
                </article>
                <article className="vk-card">
                    <span className="vk-label">Runway</span>
                    <strong>{metrics.savingsRunway.toFixed(0)}%</strong>
                    <div className="meter"><div style={{ width: `${metrics.savingsRunway}%` }} /></div>
                </article>
            </div>

            <div className="visual-grid">
                <article className="visual-card">
                    <h3>📈 Stat Trends</h3>
                    <div className="trend-rows">
                        <div><span>Stress</span><div className="meter negative"><div style={{ width: `${metrics.normalizedStress}%` }} /></div></div>
                        <div><span>Network</span><div className="meter"><div style={{ width: `${metrics.normalizedNetwork}%` }} /></div></div>
                        <div><span>Health</span><div className="meter"><div style={{ width: `${metrics.normalizedHealth}%` }} /></div></div>
                    </div>
                    <svg viewBox="0 0 240 80" className="sparkline" role="img" aria-label="Readiness trend">
                        <polyline
                            fill="none"
                            stroke="currentColor"
                            strokeWidth="4"
                            points={`0,60 40,${70 - metrics.normalizedGpa * 0.3} 90,${70 - metrics.normalizedHealth * 0.35} 140,${70 - metrics.normalizedNetwork * 0.35} 190,${70 - metrics.readiness * 0.45} 240,${70 - metrics.savingsRunway * 0.3}`}
                        />
                    </svg>
                </article>

                <article className="visual-card">
                    <h3>🏅 Achievement Badges</h3>
                    <div className="badge-grid">
                        {achievements.map(a => (
                            <div key={a.label} className={`badge-chip ${a.unlocked ? 'on' : 'off'}`}>
                                <span>{a.icon}</span>
                                <small>{a.label}</small>
                            </div>
                        ))}
                    </div>
                </article>

                <article className="visual-card">
                    <h3>🧠 Course Progress View</h3>
                    <div className="course-list">
                        {currentCourses.length === 0 ? (
                            <p className="muted">No active courses yet.</p>
                        ) : (
                            currentCourses.slice(0, 4).map((course, index) => {
                                const progress = clamp(22 + index * 15 + player.semester * 4, 0, 100)
                                return (
                                    <div key={course.id} className="course-item">
                                        <div className="course-row">
                                            <strong>{course.title}</strong>
                                            <span>{progress}%</span>
                                        </div>
                                        <div className="meter"><div style={{ width: `${progress}%` }} /></div>
                                    </div>
                                )
                            })
                        )}
                    </div>
                </article>

                <article className="visual-card">
                    <h3>🎮 Mini-Game Spotlight</h3>
                    {gameSpotlight.length === 0 ? (
                        <>
                            <p className="muted">No mini-games loaded yet for this course selection.</p>
                            <button type="button" className="jump-btn" onClick={onJumpToAcademics}>Go to Academics</button>
                        </>
                    ) : (
                        <div className="spotlight-list">
                            {gameSpotlight.map(game => (
                                <div key={game.id} className="spotlight-item">
                                    <div>
                                        <strong>{game.title}</strong>
                                        <p>{game.topic} · {game.question_count} questions</p>
                                    </div>
                                    <div className="spotlight-meta">
                                        <span>{Number(game.best_score_percent ?? 0).toFixed(0)}%</span>
                                        <small>{game.completed ? 'Completed' : 'Fresh'}</small>
                                    </div>
                                </div>
                            ))}
                            <button type="button" className="jump-btn" onClick={onJumpToAcademics}>Open Mini-Games</button>
                        </div>
                    )}
                </article>
            </div>
        </section>
    )
}
