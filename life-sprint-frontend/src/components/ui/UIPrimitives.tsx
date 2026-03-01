import './UIPrimitives.css'

type BaseProps = {
    children?: any
    className?: string
}

type ButtonProps = BaseProps & {
    variant?: 'primary' | 'secondary' | 'ghost'
    [key: string]: any
}

export function UICard({ children, className = '' }: BaseProps) {
    return <article className={`ui-card ${className}`.trim()}>{children}</article>
}

export function UIButton({
    children,
    className = '',
    variant = 'primary',
    ...props
}: ButtonProps) {
    return (
        <button {...props} className={`ui-btn ui-btn-${variant} ${className}`.trim()}>
            {children}
        </button>
    )
}

export function UIBadge({
    children,
    tone = 'neutral',
    className = '',
}: BaseProps & { tone?: 'neutral' | 'success' | 'warning' | 'danger' }) {
    return <span className={`ui-badge ui-badge-${tone} ${className}`.trim()}>{children}</span>
}

export function UIProgressBar({
    value,
    className = '',
    danger = false,
    style,
}: {
    value: number
    className?: string
    danger?: boolean
    style?: any
}) {
    const clamped = Math.max(0, Math.min(100, value))
    return (
        <div className={`ui-progress ${danger ? 'danger' : ''} ${className}`.trim()} style={style} aria-hidden="true">
            <div style={{ width: `${clamped}%` }} />
        </div>
    )
}

export function UISkeleton({ className = '' }: { className?: string }) {
    return <div className={`ui-skeleton ${className}`.trim()} aria-hidden="true" />
}
