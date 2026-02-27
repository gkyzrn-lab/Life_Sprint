import '../styles/BadgesPanel.css'

export interface Badge {
    id: string
    title: string
    description: string
    icon: string
    rarity?: 'common' | 'rare' | 'epic' | 'legendary'
    earned: boolean
    earnedAt?: string
    progress?: number
    goal?: number
}

export interface BadgesPanelProps {
    badges: Badge[]
}

const formatValue = (value: number) => {
    if (Math.abs(value) >= 1000) {
        return value.toLocaleString()
    }
    return Math.round(value).toString()
}

export function BadgesPanel({ badges }: BadgesPanelProps) {
    const earnedCount = badges.filter((badge) => badge.earned).length
    const sortedBadges = [...badges].sort((a, b) => Number(b.earned) - Number(a.earned))

    return (
        <div className="badges-panel">
            <div className="panel-header">
                <h3>Badges</h3>
                <span>{earnedCount}/{badges.length} unlocked</span>
            </div>
            <div className="badge-grid">
                {sortedBadges.map((badge) => {
                    const progressPercent = badge.goal && badge.progress !== undefined
                        ? Math.min(100, Math.max(0, (badge.progress / badge.goal) * 100))
                        : 0

                    return (
                        <div
                            key={badge.id}
                            className={`badge-card ${badge.earned ? 'earned' : 'locked'} ${badge.rarity ? `rarity-${badge.rarity}` : ''}`}
                        >
                            <div className="badge-icon">{badge.icon}</div>
                            <div className="badge-content">
                                <div className="badge-title-row">
                                    <h4>{badge.title}</h4>
                                    <span className={`badge-tag ${badge.earned ? '' : 'muted'}`}>
                                        {badge.earned ? 'Earned' : 'Locked'}
                                    </span>
                                </div>
                                <p>{badge.description}</p>
                                {!badge.earned && badge.goal !== undefined && badge.progress !== undefined && (
                                    <div className="badge-progress">
                                        <div className="badge-progress-bar">
                                            <div className="badge-progress-fill" style={{ width: `${progressPercent}%` }} />
                                        </div>
                                        <span>{formatValue(badge.progress)} / {formatValue(badge.goal)}</span>
                                    </div>
                                )}
                                {badge.earned && badge.earnedAt && (
                                    <span className="badge-earned-at">Unlocked {badge.earnedAt}</span>
                                )}
                            </div>
                        </div>
                    )
                })}
            </div>
        </div>
    )
}
