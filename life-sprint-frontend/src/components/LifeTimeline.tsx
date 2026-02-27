import '../styles/LifeTimeline.css'

export interface LifeEvent {
    age: number
    year: number
    title: string
    description: string
    type: 'achievement' | 'career' | 'education' | 'relationship' | 'financial' | 'health'
    icon: string
}

export interface LifeTimelineProps {
    currentAge: number
    events: LifeEvent[]
}

const typeColors = {
    achievement: '#FFD700',
    career: '#4A90E2',
    education: '#7ED321',
    relationship: '#FF6B6B',
    financial: '#50E3C2',
    health: '#B8E986'
}

const typeIcons = {
    achievement: '🏆',
    career: '💼',
    education: '📚',
    relationship: '❤️',
    financial: '💰',
    health: '❤️'
}

export function LifeTimeline({ currentAge, events }: LifeTimelineProps) {
    return (
        <div className="life-timeline">
            <div className="timeline-header">
                <h2>Life Timeline</h2>
                <span className="current-age">Age {currentAge}</span>
            </div>

            <div className="timeline-container">
                {events.map((event, index) => (
                    <div
                        key={index}
                        className={`timeline-item ${event.type}`}
                        style={{ borderLeftColor: typeColors[event.type], animationDelay: `${index * 60}ms` }}
                    >
                        <div className="timeline-marker" style={{ backgroundColor: typeColors[event.type] }}>
                            <span>{typeIcons[event.type]}</span>
                        </div>
                        <div className="timeline-content">
                            <div className="timeline-age">Age {event.age}</div>
                            <h3 className="timeline-title">{event.title}</h3>
                            <p className="timeline-description">{event.description}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}
