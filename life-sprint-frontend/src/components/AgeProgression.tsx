import '../styles/AgeProgression.css'

export interface AgeProgressionProps {
    currentAge: number
    currentYear: number
    lifeExpectancy?: number
}

export function AgeProgression({ currentAge, currentYear, lifeExpectancy = 80 }: AgeProgressionProps) {
    const progressPercent = (currentAge / lifeExpectancy) * 100

    const getLifeStage = (age: number) => {
        if (age < 13) return 'Childhood'
        if (age < 20) return 'Teenage Years'
        if (age < 30) return 'Young Adult'
        if (age < 45) return 'Adult'
        if (age < 65) return 'Middle Age'
        return 'Senior'
    }

    return (
        <div className="age-progression">
            <div className="age-display">
                <div className="age-number">
                    <span className="age">{currentAge}</span>
                    <span className="label">Age</span>
                </div>
                <div className="year-display">
                    <span className="year">{currentYear}</span>
                    <span className="label">Year</span>
                </div>
            </div>

            <div className="life-stage">
                <p>{getLifeStage(currentAge)}</p>
            </div>

            <div className="life-bar-container">
                <div className="life-bar">
                    <div
                        className="life-bar-fill"
                        style={{ width: `${Math.min(progressPercent, 100)}%` }}
                    />
                </div>
                <div className="life-milestones">
                    {[0, 13, 20, 30, 45, 65, 80].map(age => (
                        <div
                            key={age}
                            className={`milestone ${age === currentAge ? 'active' : ''}`}
                            style={{ left: `${(age / 80) * 100}%` }}
                            title={`Age ${age}`}
                        >
                            {age === 0 ? '👶' : age === 13 ? '👧' : age === 20 ? '👨' : age === 45 ? '👴' : age === 65 ? '🧓' : '⚪'}
                        </div>
                    ))}
                </div>
            </div>

            <div className="life-stats">
                <div className="stat">
                    <span className="stat-label">Years Lived</span>
                    <span className="stat-value">{currentAge}</span>
                </div>
                <div className="stat">
                    <span className="stat-label">Years Remaining</span>
                    <span className="stat-value">{Math.max(0, lifeExpectancy - currentAge)}</span>
                </div>
                <div className="stat">
                    <span className="stat-label">Life Progress</span>
                    <span className="stat-value">{Math.round(progressPercent)}%</span>
                </div>
            </div>
        </div>
    )
}
