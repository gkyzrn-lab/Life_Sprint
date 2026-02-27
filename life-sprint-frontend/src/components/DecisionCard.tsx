import '../styles/DecisionCard.css'

export interface DecisionOption {
    id: string
    text: string
    outcome?: string
    consequences?: {
        health?: number
        happiness?: number
        intelligence?: number
        attractiveness?: number
        money?: number
    }
}

export interface DecisionCardProps {
    title: string
    description: string
    image?: string
    options: DecisionOption[]
    onSelect: (optionId: string) => void
}

export function DecisionCard({ title, description, image, options, onSelect }: DecisionCardProps) {
    return (
        <div className="decision-card">
            <div className="decision-header">
                {image && <img src={image} alt={title} className="decision-image" />}
                <h3>{title}</h3>
            </div>

            <p className="decision-description">{description}</p>

            <div className="decision-options">
                {options.map(option => (
                    <button
                        key={option.id}
                        className="decision-button"
                        onClick={() => onSelect(option.id)}
                    >
                        <span className="option-text">{option.text}</span>
                        {option.outcome && <span className="option-outcome">{option.outcome}</span>}
                    </button>
                ))}
            </div>
        </div>
    )
}
