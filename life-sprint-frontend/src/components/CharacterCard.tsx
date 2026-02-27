import type { FC } from 'react'
import { useEffect, useRef, useState } from 'react'
import '../styles/CharacterCard.css'

export interface CharacterStats {
    health: number
    happiness: number
    intelligence: number
    attractiveness: number
    age: number
    net_worth: number
}

export interface CharacterCardProps {
    name: string
    stats: CharacterStats
    avatar?: string
}

export const CharacterCard: FC<CharacterCardProps> = ({ name, stats, avatar }) => {
    const [pulseKey, setPulseKey] = useState(0)
    const prevStatsRef = useRef<CharacterStats | null>(null)

    const prevStats = prevStatsRef.current
    const statChanges = {
        health: prevStats ? prevStats.health !== stats.health : false,
        happiness: prevStats ? prevStats.happiness !== stats.happiness : false,
        intelligence: prevStats ? prevStats.intelligence !== stats.intelligence : false,
        attractiveness: prevStats ? prevStats.attractiveness !== stats.attractiveness : false,
    }

    const statDeltas = {
        health: prevStats ? stats.health - prevStats.health : 0,
        happiness: prevStats ? stats.happiness - prevStats.happiness : 0,
        intelligence: prevStats ? stats.intelligence - prevStats.intelligence : 0,
        attractiveness: prevStats ? stats.attractiveness - prevStats.attractiveness : 0,
    }

    useEffect(() => {
        if (prevStatsRef.current) {
            const prev = prevStatsRef.current
            const changed =
                prev.health !== stats.health ||
                prev.happiness !== stats.happiness ||
                prev.intelligence !== stats.intelligence ||
                prev.attractiveness !== stats.attractiveness

            if (changed) {
                setPulseKey((value: number) => value + 1)
            }
        }
        prevStatsRef.current = stats
    }, [stats])
    const getStatColor = (value: number) => {
        if (value >= 80) return '#7ED321'  // Green
        if (value >= 60) return '#50E3C2'  // Cyan
        if (value >= 40) return '#FFD700'  // Gold
        return '#FF6B6B'  // Red
    }

    const StatBar: FC<{ label: string; value: number; changed: boolean; delta: number }> = ({ label, value, changed, delta }) => (
        <div className="stat-item" data-changed={changed ? 'true' : 'false'}>
            <div className="stat-label">
                <span>{label}</span>
                <span className="stat-value">
                    {Math.round(value)}
                    {delta !== 0 && (
                        <span className={`stat-delta ${delta > 0 ? 'positive' : 'negative'}`}>
                            {delta > 0 ? `+${Math.round(delta)}` : Math.round(delta)}
                        </span>
                    )}
                </span>
            </div>
            <div className="stat-bar-container">
                <div
                    className="stat-bar-fill"
                    style={{
                        width: `${Math.max(0, Math.min(100, value))}%`,
                        backgroundColor: getStatColor(value)
                    }}
                />
            </div>
        </div>
    )

    return (
        <div className="character-card" data-pulse-key={pulseKey}>
            <div className="character-header">
                <div className="character-avatar">
                    {avatar ? (
                        <img src={avatar} alt={name} />
                    ) : (
                        <div className="avatar-placeholder">👤</div>
                    )}
                </div>
                <div className="character-info">
                    <h2>{name}</h2>
                    <p className="character-age">Age {stats.age}</p>
                    <p className="character-net-worth">Net Worth: ${(stats.net_worth / 1000000).toFixed(1)}M</p>
                </div>
            </div>

            <div className="stats-grid">
                <StatBar label="Health" value={stats.health} changed={statChanges.health} delta={statDeltas.health} />
                <StatBar label="Happiness" value={stats.happiness} changed={statChanges.happiness} delta={statDeltas.happiness} />
                <StatBar label="Intelligence" value={stats.intelligence} changed={statChanges.intelligence} delta={statDeltas.intelligence} />
                <StatBar label="Attractiveness" value={stats.attractiveness} changed={statChanges.attractiveness} delta={statDeltas.attractiveness} />
            </div>
        </div>
    )
}
