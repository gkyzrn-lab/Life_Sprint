import React from 'react'
import './SemesterSummaryScreen.css'

interface SemesterSummary {
    previous_semester: number
    new_semester: number
    year_in_school: number
    year_label: string
    graduated: boolean
    semester_summary: {
        courses_completed: string[]
        scholarship_awarded: number
        tuition_paid: number
        borrowed: number
        living_expenses: number
        gpa: number
        burnout_level: string
        sleep_delta?: number
        health_delta?: number
        network_delta?: number
        burnout_consequence?: any
    }
    warnings: string[]
}

interface SemesterSummaryScreenProps {
    summary: SemesterSummary
    onContinue: () => void
    isLoading: boolean
}

export const SemesterSummaryScreen: React.FC<SemesterSummaryScreenProps> = ({
    summary,
    onContinue,
    isLoading,
}) => {
    const {
        previous_semester,
        new_semester,
        year_in_school,
        year_label,
        graduated,
        semester_summary,
        warnings,
    } = summary

    const formatCurrency = (amount: number) => `$${amount.toLocaleString('en-US', { maximumFractionDigits: 0 })}`
    const formatGPA = (gpa: number) => gpa.toFixed(2)

    return (
        <div className="semester-summary-overlay">
            <div className="semester-summary-card">
                <div className="summary-header">
                    {graduated ? (
                        <>
                            <h1 className="summary-title">🎓 GRADUATION!</h1>
                            <p className="summary-subtitle">You've completed your degree journey!</p>
                        </>
                    ) : (
                        <>
                            <h1 className="summary-title">✅ Semester Complete!</h1>
                            <p className="summary-subtitle">
                                {year_label} | Moving from Semester {previous_semester} → Semester {new_semester}
                            </p>
                        </>
                    )}
                </div>

                <div className="summary-content">
                    {/* Academic Results */}
                    <section className="summary-section">
                        <h2>📚 Academic</h2>
                        <div className="stat-grid">
                            <div className="stat-item">
                                <label>GPA</label>
                                <value className="gpa-badge">{formatGPA(semester_summary.gpa)}</value>
                            </div>
                            <div className="stat-item">
                                <label>Burnout Level</label>
                                <value className={`burnout-${semester_summary.burnout_level.toLowerCase()}`}>
                                    {semester_summary.burnout_level}
                                </value>
                            </div>
                            {semester_summary.courses_completed.length > 0 && (
                                <div className="stat-item full-width">
                                    <label>Courses Completed</label>
                                    <div className="course-list">
                                        {semester_summary.courses_completed.map((course) => (
                                            <span key={course} className="course-badge">
                                                {course}
                                            </span>
                                        ))}
                                    </div>
                                </div>
                            )}
                        </div>
                    </section>

                    {/* Financial Summary */}
                    <section className="summary-section">
                        <h2>💰 Finances</h2>
                        <div className="stat-grid">
                            <div className="stat-item">
                                <label>Tuition Paid</label>
                                <value className="expense">{formatCurrency(semester_summary.tuition_paid)}</value>
                            </div>
                            <div className="stat-item">
                                <label>Living Expenses</label>
                                <value className="expense">
                                    {formatCurrency(semester_summary.living_expenses)}
                                </value>
                            </div>
                            <div className="stat-item">
                                <label>New Loans</label>
                                <value className="borrowed">{formatCurrency(semester_summary.borrowed)}</value>
                            </div>
                            {semester_summary.scholarship_awarded > 0 && (
                                <div className="stat-item">
                                    <label>Scholarships</label>
                                    <value className="scholarship">
                                        +{formatCurrency(semester_summary.scholarship_awarded)}
                                    </value>
                                </div>
                            )}
                        </div>
                    </section>

                    {/* Wellbeing Effects */}
                    {(semester_summary.sleep_delta !== undefined ||
                        semester_summary.health_delta !== undefined ||
                        semester_summary.network_delta !== undefined) && (
                            <section className="summary-section">
                                <h2>❤️ Wellbeing</h2>
                                <div className="stat-grid">
                                    {semester_summary.sleep_delta !== undefined && (
                                        <div className="stat-item">
                                            <label>Sleep Quality</label>
                                            <value className={semester_summary.sleep_delta < 0 ? 'negative' : 'positive'}>
                                                {semester_summary.sleep_delta > 0 ? '+' : ''}
                                                {semester_summary.sleep_delta.toFixed(1)}
                                            </value>
                                        </div>
                                    )}
                                    {semester_summary.health_delta !== undefined && (
                                        <div className="stat-item">
                                            <label>Health</label>
                                            <value className={semester_summary.health_delta < 0 ? 'negative' : 'positive'}>
                                                {semester_summary.health_delta > 0 ? '+' : ''}
                                                {semester_summary.health_delta.toFixed(1)}
                                            </value>
                                        </div>
                                    )}
                                    {semester_summary.network_delta !== undefined && (
                                        <div className="stat-item">
                                            <label>Network Score</label>
                                            <value className={semester_summary.network_delta < 0 ? 'negative' : 'positive'}>
                                                {semester_summary.network_delta > 0 ? '+' : ''}
                                                {semester_summary.network_delta.toFixed(1)}
                                            </value>
                                        </div>
                                    )}
                                </div>
                            </section>
                        )}

                    {/* Warnings */}
                    {warnings.length > 0 && (
                        <section className="summary-section warnings-section">
                            <h2>⚠️ Heads Up</h2>
                            <ul className="warnings-list">
                                {warnings.map((warning, idx) => (
                                    <li key={idx}>{warning}</li>
                                ))}
                            </ul>
                        </section>
                    )}

                    {/* Burnout Consequence */}
                    {semester_summary.burnout_consequence && (
                        <section className="summary-section consequence-section">
                            <h2>⚡ Emergency Action</h2>
                            <div className="consequence-alert">
                                <p>{semester_summary.burnout_consequence.message}</p>
                                <p className="consequence-detail">
                                    Dropped: {semester_summary.burnout_consequence.course_name} (
                                    {semester_summary.burnout_consequence.credits_lost} credits)
                                </p>
                            </div>
                        </section>
                    )}
                </div>

                <div className="summary-footer">
                    <button
                        className="btn-continue"
                        onClick={onContinue}
                        disabled={isLoading}
                    >
                        {isLoading ? (
                            <>⏳ Loading next semester...</>
                        ) : graduated ? (
                            <>🎉 View Graduation Report</>
                        ) : (
                            <>➡️ Continue to Semester {new_semester}</>
                        )}
                    </button>
                </div>
            </div>
        </div>
    )
}

export default SemesterSummaryScreen
