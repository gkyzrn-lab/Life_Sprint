import { useEffect, useState } from 'react'
import { getLifeReadinessAnalytics, type LifeReadinessResponse, type DomainReadiness, type GameRecommendation } from '../utils/api'

interface LifeReadinessPanelProps {
    playerId: string
    onClose?: () => void
    onPlayRecommendation?: (rec: GameRecommendation) => void | Promise<void>
}

export default function LifeReadinessPanel({ playerId, onClose, onPlayRecommendation }: LifeReadinessPanelProps) {
    const [analytics, setAnalytics] = useState<LifeReadinessResponse | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)
    const [launchingGameId, setLaunchingGameId] = useState<string | null>(null)

    useEffect(() => {
        loadAnalytics()
    }, [playerId])

    async function loadAnalytics() {
        try {
            setLoading(true)
            setError(null)
            const data = await getLifeReadinessAnalytics(playerId)
            setAnalytics(data)
        } catch (err: any) {
            setError(err.message || 'Failed to load analytics')
        } finally {
            setLoading(false)
        }
    }

    async function handlePlayRecommendation(rec: GameRecommendation) {
        if (!onPlayRecommendation) return
        try {
            setLaunchingGameId(rec.game_id)
            await onPlayRecommendation(rec)
        } catch (err: any) {
            setError(err?.message || 'Failed to open recommended game')
        } finally {
            setLaunchingGameId(null)
        }
    }

    if (loading) {
        return (
            <div className="life-readiness-panel">
                <div className="panel-header">
                    <h2>📊 Life Readiness Score</h2>
                    {onClose && <button onClick={onClose} className="close-btn">×</button>}
                </div>
                <div className="loading-state">Loading analytics...</div>
            </div>
        )
    }

    if (error) {
        return (
            <div className="life-readiness-panel">
                <div className="panel-header">
                    <h2>📊 Life Readiness Score</h2>
                    {onClose && <button onClick={onClose} className="close-btn">×</button>}
                </div>
                <div className="error-state">
                    <p>❌ {error}</p>
                    <button onClick={loadAnalytics}>Retry</button>
                </div>
            </div>
        )
    }

    if (!analytics || !analytics.analytics) {
        return (
            <div className="life-readiness-panel">
                <div className="panel-header">
                    <h2>📊 Life Readiness Score</h2>
                    {onClose && <button onClick={onClose} className="close-btn">×</button>}
                </div>
                <div className="empty-state">
                    <p>🎮 Play mini-games to build your Life Readiness Score!</p>
                    <p>Complete challenges in Finance, Leadership, Technical skills, and more.</p>
                </div>
            </div>
        )
    }

    const a = analytics.analytics

    // Helper for score color
    function getScoreColor(score: number): string {
        if (score >= 85) return '#22c55e'  // green
        if (score >= 70) return '#3b82f6'  // blue
        if (score >= 50) return '#f59e0b'  // orange
        return '#ef4444'  // red
    }

    // Helper for readiness level label
    function getReadinessEmoji(level: string): string {
        const map: Record<string, string> = {
            'expert': '🏆',
            'proficient': '✅',
            'developing': '📈',
            'beginner': '🌱'
        }
        return map[level] || '📊'
    }

    // Helper for trend emoji
    function getTrendEmoji(trend: string): string {
        const map: Record<string, string> = {
            'improving': '📈',
            'stable': '➡️',
            'declining': '📉',
            'unknown': '❓'
        }
        return map[trend] || '➡️'
    }

    function getMomentumEmoji(momentum: string): string {
        if (momentum === 'up') return '🚀'
        if (momentum === 'down') return '🧯'
        return '🧭'
    }

    // Domain display names
    const domainLabels: Record<string, string> = {
        'finance': '💰 Finance',
        'leadership': '👥 Leadership',
        'technical': '⚙️ Technical',
        'critical_thinking': '🧠 Critical Thinking',
        'ethics': '⚖️ Ethics'
    }

    // Badge icon mapping (simple emoji lookup by category/name)
    function getBadgeIcon(badgeId: string): string {
        // Map badge IDs to emojis
        const iconMap: Record<string, string> = {
            'finance_guru_bronze': '💰',
            'finance_guru_silver': '💎',
            'tech_master_bronze': '💻',
            'tech_master_silver': '⚡',
            'leader_bronze': '👥',
            'leader_silver': '🌟',
            'critical_thinker_bronze': '🧠',
            'ethical_bronze': '⚖️',
            'game_explorer': '🎮',
            'game_veteran': '🏆',
            'game_legend': '👑',
            'consistent_performer': '📈',
            'unstoppable': '🔥',
            'perfectionist': '✨',
            'high_achiever': '🎯',
            'domain_expert': '🌟',
            'domain_master': '💫',
            'career_ready': '🚀',
            'industry_ready': '💼',
            'elite_candidate': '🏅',
            'well_rounded': '🌈',
            'renaissance_student': '🎨',
        }
        return iconMap[badgeId] || '🏅'
    }

    return (
        <div className="life-readiness-panel">
            <div className="panel-header">
                <div>
                    <h2>📊 Life Readiness Score</h2>
                    <p className="player-info">{analytics.player_name} • Semester {analytics.semester}</p>
                </div>
                {onClose && <button onClick={onClose} className="close-btn">×</button>}
            </div>

            {/* Overall Score */}
            <div className="overall-score-card">
                <div className="score-circle" style={{ borderColor: getScoreColor(a.overall_score) }}>
                    <div className="score-number" style={{ color: getScoreColor(a.overall_score) }}>
                        {a.overall_score.toFixed(1)}
                    </div>
                    <div className="score-label">Overall</div>
                </div>
                <div className="readiness-details">
                    <div className="readiness-level">
                        {getReadinessEmoji(a.readiness_level)} <strong>{a.readiness_level.toUpperCase()}</strong>
                    </div>
                    <div className="games-completed">
                        {a.total_games_completed} games completed • {a.average_game_score.toFixed(1)}% avg score
                    </div>
                    <div className={`career-status ${a.career_ready ? 'ready' : 'not-ready'}`}>
                        {a.career_ready ? '✅ Career Ready' : '⚠️ Build Skills for Career Readiness (70+ needed)'}
                    </div>
                    {a.career_salary_impact !== 1.0 && (
                        <div className="salary-impact">
                            💵 Salary Impact: <strong>{(a.career_salary_impact * 100).toFixed(0)}%</strong>
                            <span className="impact-hint">
                                {a.career_salary_impact >= 1.1
                                    ? ' (Strong skills = higher starting salary!)'
                                    : ' (Improve skills for better career prospects)'}
                            </span>
                        </div>
                    )}
                </div>
            </div>

            {/* Momentum + Coaching */}
            <div className={`coach-section momentum-${a.momentum}`}>
                <div className="coach-header">
                    <span className="coach-emoji">{getMomentumEmoji(a.momentum)}</span>
                    <h3>Momentum Coach</h3>
                    <span className="coach-delta">
                        {a.score_change_since_last_snapshot > 0 ? '+' : ''}
                        {a.score_change_since_last_snapshot.toFixed(1)}
                    </span>
                </div>
                <p className="coach-tip">{a.coaching_tip}</p>
                {a.points_to_next_target > 0 && (
                    <p className="coach-target">
                        Next target: <strong>{a.next_readiness_target.toFixed(0)}</strong> (
                        {a.points_to_next_target.toFixed(1)} points to go)
                    </p>
                )}
            </div>

            {/* Historical Trend */}
            {analytics.readiness_history && analytics.readiness_history.length > 1 && (
                <div className="history-section">
                    <h3>📈 Readiness Trend</h3>
                    <div className="history-bars">
                        {analytics.readiness_history.slice(-8).map((snap, idx) => (
                            <div key={`${snap.semester}-${snap.total_games}-${idx}`} className="history-point">
                                <div
                                    className="history-bar"
                                    style={{ height: `${Math.max(10, snap.overall_score)}%` }}
                                    title={`Semester ${snap.semester}: ${snap.overall_score.toFixed(1)}`}
                                />
                                <span className="history-label">S{snap.semester}</span>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Domain Breakdown */}
            <div className="domains-section">
                <h3>Skill Domain Breakdown</h3>
                {a.domains.length === 0 ? (
                    <p className="no-domains">Play mini-games to see your skill breakdown!</p>
                ) : (
                    <div className="domain-list">
                        {a.domains.map((domain: DomainReadiness) => (
                            <div key={domain.domain} className="domain-card">
                                <div className="domain-header">
                                    <span className="domain-name">{domainLabels[domain.domain] || domain.domain}</span>
                                    <span className="domain-trend">{getTrendEmoji(domain.trend)}</span>
                                </div>
                                <div className="domain-score-bar">
                                    <div
                                        className="score-fill"
                                        style={{
                                            width: `${domain.score}%`,
                                            backgroundColor: getScoreColor(domain.score)
                                        }}
                                    />
                                </div>
                                <div className="domain-stats">
                                    <span className="score-value" style={{ color: getScoreColor(domain.score) }}>
                                        {domain.score.toFixed(1)}
                                    </span>
                                    <span className="games-count">
                                        {domain.games_completed} game{domain.games_completed !== 1 ? 's' : ''}
                                    </span>
                                    <span className="trend-text">
                                        {domain.trend}
                                    </span>
                                </div>
                            </div>
                        ))}
                    </div>
                )}
            </div>

            {/* Strengths & Growth Areas */}
            <div className="insights-section">
                <div className="insight-card strengths">
                    <h4>💪 Your Strengths</h4>
                    {a.strengths.length === 0 ? (
                        <p>Complete more games to identify strengths</p>
                    ) : (
                        <ul>
                            {a.strengths.map((s: string) => (
                                <li key={s}>{domainLabels[s] || s}</li>
                            ))}
                        </ul>
                    )}
                </div>
                <div className="insight-card growth-areas">
                    <h4>🎯 Areas for Growth</h4>
                    {a.areas_for_growth.length === 0 ? (
                        <p>Keep up the great work!</p>
                    ) : (
                        <ul>
                            {a.areas_for_growth.map((area: string) => (
                                <li key={area}>{domainLabels[area] || area}</li>
                            ))}
                        </ul>
                    )}
                </div>
            </div>

            {/* Recommended Next Steps */}
            {a.recommended_next_games.length > 0 && (
                <div className="recommendations-section">
                    <h4>🎯 Recommended Practice</h4>
                    <div className="game-recommendations">
                        {a.recommended_next_games.map((rec: GameRecommendation) => (
                            <div key={rec.game_id} className="game-rec-card">
                                <div className="game-rec-title">📚 {rec.title}</div>
                                <div className="game-rec-course">Course: {rec.course_id.toUpperCase()}</div>
                                <div className="game-rec-reason">{rec.reason}</div>
                                {onPlayRecommendation && (
                                    <button
                                        className="game-rec-play-btn"
                                        onClick={() => handlePlayRecommendation(rec)}
                                        disabled={launchingGameId === rec.game_id}
                                    >
                                        {launchingGameId === rec.game_id ? 'Opening...' : 'Play now'}
                                    </button>
                                )}
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Achievement Badges */}
            {a.achievement_badges && a.achievement_badges.length > 0 && (
                <div className="badges-section">
                    <h4>🏆 Achievement Badges ({a.achievement_badges.length})</h4>
                    {a.newly_earned_badges && a.newly_earned_badges.length > 0 && (
                        <div className="new-badges-alert">
                            🎉 {a.newly_earned_badges.length} new badge{a.newly_earned_badges.length !== 1 ? 's' : ''} earned!
                        </div>
                    )}
                    <div className="badge-grid">
                        {a.achievement_badges.slice(0, 12).map((badgeId: string) => (
                            <div
                                key={badgeId}
                                className={`badge-item ${a.newly_earned_badges?.includes(badgeId) ? 'new-badge' : ''}`}
                                title={badgeId}
                            >
                                {getBadgeIcon(badgeId)}
                            </div>
                        ))}
                    </div>
                    {a.achievement_badges.length > 12 && (
                        <div className="more-badges">
                            +{a.achievement_badges.length - 12} more badges
                        </div>
                    )}
                </div>
            )}

            <style>{`
                .life-readiness-panel {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 16px;
                    padding: 24px;
                    color: white;
                    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                    max-width: 900px;
                    margin: 0 auto;
                }

                .panel-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: start;
                    margin-bottom: 24px;
                }

                .panel-header h2 {
                    margin: 0 0 4px 0;
                    font-size: 28px;
                    font-weight: bold;
                }

                .player-info {
                    margin: 0;
                    opacity: 0.9;
                    font-size: 14px;
                }

                .close-btn {
                    background: rgba(255,255,255,0.2);
                    border: none;
                    color: white;
                    font-size: 32px;
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    cursor: pointer;
                    transition: all 0.2s;
                    line-height: 1;
                    padding: 0;
                }

                .close-btn:hover {
                    background: rgba(255,255,255,0.3);
                    transform: rotate(90deg);
                }

                .loading-state, .error-state, .empty-state {
                    text-align: center;
                    padding: 60px 20px;
                    background: rgba(255,255,255,0.1);
                    border-radius: 12px;
                }

                .error-state button {
                    margin-top: 16px;
                    padding: 10px 24px;
                    background: white;
                    color: #667eea;
                    border: none;
                    border-radius: 8px;
                    cursor: pointer;
                    font-weight: 600;
                }

                .overall-score-card {
                    display: flex;
                    gap: 32px;
                    background: rgba(255,255,255,0.15);
                    padding: 32px;
                    border-radius: 12px;
                    margin-bottom: 24px;
                    backdrop-filter: blur(10px);
                    align-items: center;
                }

                .score-circle {
                    width: 140px;
                    height: 140px;
                    border-radius: 50%;
                    border: 8px solid white;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    background: rgba(255,255,255,0.1);
                    flex-shrink: 0;
                }

                .score-number {
                    font-size: 42px;
                    font-weight: bold;
                    line-height: 1;
                }

                .score-label {
                    font-size: 14px;
                    opacity: 0.9;
                    margin-top: 4px;
                }

                .readiness-details {
                    flex: 1;
                    display: flex;
                    flex-direction: column;
                    gap: 12px;
                }

                .readiness-level {
                    font-size: 24px;
                    font-weight: 600;
                }

                .games-completed {
                    font-size: 16px;
                    opacity: 0.9;
                }

                .career-status {
                    padding: 12px 16px;
                    border-radius: 8px;
                    font-weight: 600;
                    font-size: 15px;
                }

                .career-status.ready {
                    background: rgba(34, 197, 94, 0.3);
                    border: 2px solid rgba(34, 197, 94, 0.6);
                }

                .career-status.not-ready {
                    background: rgba(251, 191, 36, 0.3);
                    border: 2px solid rgba(251, 191, 36, 0.6);
                }

                .salary-impact {
                    font-size: 15px;
                }

                .salary-impact strong {
                    font-size: 18px;
                }

                .impact-hint {
                    font-size: 13px;
                    opacity: 0.8;
                }

                .domains-section {
                    margin-bottom: 24px;
                }

                .coach-section {
                    background: rgba(255,255,255,0.15);
                    padding: 18px;
                    border-radius: 10px;
                    backdrop-filter: blur(5px);
                    margin-bottom: 24px;
                    border-left: 4px solid rgba(255,255,255,0.35);
                }

                .coach-section.momentum-up {
                    border-left-color: rgba(34, 197, 94, 0.8);
                }

                .coach-section.momentum-down {
                    border-left-color: rgba(239, 68, 68, 0.8);
                }

                .coach-section.momentum-flat {
                    border-left-color: rgba(59, 130, 246, 0.8);
                }

                .coach-header {
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    margin-bottom: 8px;
                }

                .coach-header h3 {
                    margin: 0;
                    font-size: 18px;
                    flex: 1;
                }

                .coach-emoji {
                    font-size: 22px;
                }

                .coach-delta {
                    font-weight: 700;
                    background: rgba(255,255,255,0.2);
                    padding: 4px 10px;
                    border-radius: 999px;
                }

                .coach-tip {
                    margin: 0 0 8px 0;
                    font-size: 15px;
                    opacity: 0.95;
                }

                .coach-target {
                    margin: 0;
                    font-size: 14px;
                    opacity: 0.9;
                }

                .history-section {
                    background: rgba(255,255,255,0.15);
                    padding: 20px;
                    border-radius: 10px;
                    backdrop-filter: blur(5px);
                    margin-bottom: 24px;
                }

                .history-section h3 {
                    margin: 0 0 14px 0;
                    font-size: 20px;
                }

                .history-bars {
                    display: flex;
                    align-items: end;
                    gap: 10px;
                    height: 130px;
                }

                .history-point {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: end;
                    flex: 1;
                    min-width: 24px;
                    height: 100%;
                }

                .history-bar {
                    width: 100%;
                    border-radius: 8px 8px 4px 4px;
                    background: linear-gradient(180deg, rgba(255,255,255,0.95), rgba(255,255,255,0.45));
                    transition: transform 0.2s ease;
                }

                .history-bar:hover {
                    transform: translateY(-3px);
                }

                .history-label {
                    margin-top: 6px;
                    font-size: 11px;
                    opacity: 0.85;
                }

                .domains-section h3 {
                    margin: 0 0 16px 0;
                    font-size: 20px;
                }

                .no-domains {
                    text-align: center;
                    padding: 20px;
                    opacity: 0.8;
                }

                .domain-list {
                    display: flex;
                    flex-direction: column;
                    gap: 16px;
                }

                .domain-card {
                    background: rgba(255,255,255,0.15);
                    padding: 20px;
                    border-radius: 10px;
                    backdrop-filter: blur(5px);
                }

                .domain-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 12px;
                }

                .domain-name {
                    font-size: 18px;
                    font-weight: 600;
                }

                .domain-trend {
                    font-size: 20px;
                }

                .domain-score-bar {
                    height: 24px;
                    background: rgba(0,0,0,0.2);
                    border-radius: 12px;
                    overflow: hidden;
                    margin-bottom: 8px;
                }

                .score-fill {
                    height: 100%;
                    transition: width 0.5s ease;
                    display: flex;
                    align-items: center;
                    justify-content: flex-end;
                    padding-right: 8px;
                    font-weight: 600;
                    font-size: 13px;
                }

                .domain-stats {
                    display: flex;
                    justify-content: space-between;
                    font-size: 14px;
                }

                .score-value {
                    font-weight: bold;
                    font-size: 16px;
                }

                .games-count {
                    opacity: 0.8;
                }

                .trend-text {
                    opacity: 0.9;
                    font-style: italic;
                }

                .insights-section {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 16px;
                    margin-bottom: 24px;
                }

                .insight-card {
                    background: rgba(255,255,255,0.15);
                    padding: 20px;
                    border-radius: 10px;
                    backdrop-filter: blur(5px);
                }

                .insight-card h4 {
                    margin: 0 0 12px 0;
                    font-size: 16px;
                }

                .insight-card ul {
                    margin: 0;
                    padding-left: 20px;
                }

                .insight-card li {
                    margin: 6px 0;
                    font-size: 15px;
                }

                .insight-card p {
                    margin: 0;
                    opacity: 0.8;
                    font-style: italic;
                }

                .recommendations-section {
                    background: rgba(255,255,255,0.15);
                    padding: 20px;
                    border-radius: 10px;
                    backdrop-filter: blur(5px);
                    margin-bottom: 16px;
                }

                .recommendations-section h4 {
                    margin: 0 0 16px 0;
                    font-size: 16px;
                }

                .game-recommendations {
                    display: flex;
                    flex-direction: column;
                    gap: 12px;
                }

                .game-rec-card {
                    background: rgba(255,255,255,0.1);
                    padding: 14px;
                    border-radius: 8px;
                    border-left: 4px solid rgba(255,255,255,0.5);
                }

                .game-rec-title {
                    font-weight: 600;
                    font-size: 15px;
                    margin-bottom: 4px;
                }

                .game-rec-course {
                    font-size: 12px;
                    opacity: 0.8;
                    margin-bottom: 6px;
                }

                .game-rec-reason {
                    font-size: 14px;
                    opacity: 0.9;
                    font-style: italic;
                }

                .game-rec-play-btn {
                    margin-top: 10px;
                    background: rgba(255,255,255,0.22);
                    border: 1px solid rgba(255,255,255,0.45);
                    color: white;
                    border-radius: 8px;
                    padding: 7px 12px;
                    cursor: pointer;
                    font-weight: 600;
                    transition: all 0.2s;
                }

                .game-rec-play-btn:hover:not(:disabled) {
                    background: rgba(255,255,255,0.34);
                    transform: translateY(-1px);
                }

                .game-rec-play-btn:disabled {
                    opacity: 0.7;
                    cursor: default;
                }

                .badges-section {
                    background: rgba(255,255,255,0.15);
                    padding: 20px;
                    border-radius: 10px;
                    backdrop-filter: blur(5px);
                    margin-bottom: 16px;
                }

                .badges-section h4 {
                    margin: 0 0 12px 0;
                    font-size: 16px;
                }

                .new-badges-alert {
                    background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
                    padding: 10px 16px;
                    border-radius: 8px;
                    margin-bottom: 16px;
                    font-weight: 600;
                    text-align: center;
                    animation: pulse 2s ease-in-out infinite;
                }

                @keyframes pulse {
                    0%, 100% { transform: scale(1); }
                    50% { transform: scale(1.02); }
                }

                .badge-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(70px, 1fr));
                    gap: 12px;
                }

                .badge-item {
                    background: rgba(255,255,255,0.2);
                    padding: 16px;
                    border-radius: 10px;
                    text-align: center;
                    font-size: 32px;
                    transition: transform 0.2s, background 0.2s;
                    cursor: help;
                }

                .badge-item:hover {
                    transform: translateY(-4px) scale(1.1);
                    background: rgba(255,255,255,0.3);
                }

                .badge-item.new-badge {
                    background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
                    animation: badgeBounce 0.6s ease-out;
                }

                @keyframes badgeBounce {
                    0% { transform: scale(0); }
                    50% { transform: scale(1.2); }
                    100% { transform: scale(1); }
                }

                .more-badges {
                    margin-top: 12px;
                    text-align: center;
                    opacity: 0.8;
                    font-size: 14px;
                }

                @media (max-width: 768px) {
                    .overall-score-card {
                        flex-direction: column;
                        align-items: center;
                        text-align: center;
                    }

                    .insights-section {
                        grid-template-columns: 1fr;
                    }
                }
            `}</style>
        </div>
    )
}
