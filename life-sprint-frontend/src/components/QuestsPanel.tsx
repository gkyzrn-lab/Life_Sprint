import '../styles/QuestsPanel.css'

export interface Quest {
    id: string
    title: string
    description: string
    icon: string
    progress: number
    goal: number
    reward: string
    unit?: 'money' | 'points'
}

export interface QuestsPanelProps {
    quests: Quest[]
}

const formatValue = (value: number, unit?: Quest['unit']) => {
    if (unit === 'money') {
        return `$${Math.round(value).toLocaleString()}`
    }
    return Math.round(value).toString()
}

export function QuestsPanel({ quests }: QuestsPanelProps) {
    return (
        <div className="quests-panel">
            <div className="panel-header">
                <h3>Quests</h3>
                <span>{quests.filter((quest) => quest.progress >= quest.goal).length}/{quests.length} completed</span>
            </div>
            <div className="quest-list">
                {quests.map((quest) => {
                    const progressPercent = Math.min(100, Math.max(0, (quest.progress / quest.goal) * 100))
                    const isComplete = quest.progress >= quest.goal

                    return (
                        <div key={quest.id} className="quest-card">
                            <div className="quest-header">
                                <div className="quest-title">
                                    <span className="quest-icon">{quest.icon}</span>
                                    <h4>{quest.title}</h4>
                                </div>
                                <span className={`quest-status ${isComplete ? 'complete' : 'pending'}`}>
                                    {isComplete ? 'Complete' : 'In progress'}
                                </span>
                            </div>
                            <p className="quest-desc">{quest.description}</p>
                            <div className="quest-progress">
                                <div className="quest-progress-bar">
                                    <div className="quest-progress-fill" style={{ width: `${progressPercent}%` }} />
                                </div>
                                <span>{formatValue(quest.progress, quest.unit)} / {formatValue(quest.goal, quest.unit)}</span>
                            </div>
                            <div className="quest-reward">Reward: {quest.reward}</div>
                        </div>
                    )
                })}
            </div>
        </div>
    )
}
