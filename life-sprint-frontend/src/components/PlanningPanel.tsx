import { useState, useEffect } from 'react'
import { Player, savePlan, lockPlan, forecastPlan, ForecastResult } from '../utils/api'
import './PlanningPanel.css'

interface PlanningPanelProps {
    player: Player
    onPlayerUpdate: (player: Player) => void
    onRefreshPlayer: (playerId: string) => Promise<Player | null>
    allHousingOptions: { [key: string]: any }
    allJobOptions: { [key: string]: any }
    allActivities: { [key: string]: any }
}

export default function PlanningPanel({
    player,
    onPlayerUpdate,
    onRefreshPlayer,
    allHousingOptions,
    allJobOptions,
    allActivities,
}: PlanningPanelProps) {
    const [selectedHousing, setSelectedHousing] = useState(player.plan?.housing_option_id || 'dorm')
    const [selectedJob, setSelectedJob] = useState(player.plan?.job_id || '')
    const [selectedActivities, setSelectedActivities] = useState<string[]>(player.plan?.activities || [])
    const [saving, setSaving] = useState(false)
    const [locking, setLocking] = useState(false)
    const [forecast, setForecast] = useState<ForecastResult | null>(null)
    const [forecastLoading, setForecastLoading] = useState(false)
    const [forecastError, setForecastError] = useState<string | null>(null)

    const isLocked = player.plan?.locked === true
    const housingObj = allHousingOptions[selectedHousing]
    const jobObj = selectedJob ? allJobOptions[selectedJob] : null

    const handleActivityToggle = (activityId: string) => {
        setSelectedActivities((prev) =>
            prev.includes(activityId) ? prev.filter((a) => a !== activityId) : [...prev, activityId]
        )
    }

    const handleForecast = async () => {
        setForecastLoading(true)
        setForecastError(null)
        try {
            const result = await forecastPlan(player.id, selectedHousing, selectedJob || null, selectedActivities)
            setForecast(result)
        } catch (err) {
            setForecastError(err instanceof Error ? err.message : 'Failed to forecast plan')
        } finally {
            setForecastLoading(false)
        }
    }

    const handleSave = async () => {
        setSaving(true)
        try {
            await savePlan(player.id, player.semester, selectedHousing, selectedJob || null, selectedActivities)
            const updated = await onRefreshPlayer(player.id)
            if (updated) onPlayerUpdate(updated)
        } catch (err) {
            alert(err instanceof Error ? err.message : 'Failed to save plan')
        } finally {
            setSaving(false)
        }
    }

    const handleLock = async () => {
        if (!player.plan) {
            alert('Save your plan first!')
            return
        }
        setLocking(true)
        try {
            await lockPlan(player.id, player.semester)
            const updated = await onRefreshPlayer(player.id)
            if (updated) onPlayerUpdate(updated)
        } catch (err) {
            alert(err instanceof Error ? err.message : 'Failed to lock plan')
        } finally {
            setLocking(false)
        }
    }

    return (
        <div className="planning-panel">
            {isLocked ? (
                <div className="plan-locked-banner">
                    <p className="locked-title">✅ Plan Locked</p>
                    <p className="locked-desc">Your semester plan is locked in. You can proceed to take your exam!</p>
                </div>
            ) : (
                <div className="plan-draft-banner">
                    <p className="draft-title">📋 Create Your Semester Plan</p>
                    <p className="draft-desc">Choose your housing, job, and activities. Then lock it in to proceed.</p>
                </div>
            )}

            <div className="planning-grid">
                {/* Housing Selection */}
                <div className="planning-section">
                    <h3>🏠 Housing</h3>
                    <select
                        value={selectedHousing}
                        onChange={(e) => setSelectedHousing(e.target.value)}
                        disabled={isLocked}
                        className="planning-select"
                    >
                        {Object.entries(allHousingOptions).map(([id, housing]) => (
                            <option key={id} value={id}>
                                {housing.name || id} (${housing.monthly_cost}/mo)
                            </option>
                        ))}
                    </select>
                    {housingObj && (
                        <div className="option-details">
                            <p className="detail-line">
                                💰 Cost: <strong>${housingObj.monthly_cost}/month</strong>
                            </p>
                            <p className="detail-line">
                                ⏱️ Commute: <strong>{housingObj.commute_minutes} min</strong>
                            </p>
                            <p className="detail-line">
                                😊 Stress Impact: <strong>{housingObj.stress_level}</strong>
                            </p>
                        </div>
                    )}
                </div>

                {/* Job Selection */}
                <div className="planning-section">
                    <h3>💼 Work</h3>
                    <select
                        value={selectedJob}
                        onChange={(e) => setSelectedJob(e.target.value)}
                        disabled={isLocked}
                        className="planning-select"
                    >
                        <option value="">No job</option>
                        {Object.entries(allJobOptions).map(([id, job]) => (
                            <option key={id} value={id}>
                                {job.title || id} ({job.hours_per_week}h/week @ ${job.hourly_wage}/hr)
                            </option>
                        ))}
                    </select>
                    {jobObj && (
                        <div className="option-details">
                            <p className="detail-line">
                                ⏰ Hours: <strong>{jobObj.hours_per_week}/week</strong>
                            </p>
                            <p className="detail-line">
                                💵 Hourly: <strong>${jobObj.hourly_wage}/hr</strong>
                            </p>
                            <p className="detail-line">
                                Monthly Income: <strong>${(jobObj.hourly_wage * jobObj.hours_per_week * 4.33).toFixed(0)}</strong>
                            </p>
                            <p className="detail-line">
                                😰 Stress: <strong>+{jobObj.stress_per_semester}</strong>
                            </p>
                        </div>
                    )}
                </div>

                {/* Activities Selection */}
                <div className="planning-section">
                    <h3>🎯 Activities</h3>
                    <div className="activities-list">
                        {Object.entries(allActivities).map(([id, activity]) => (
                            <label key={id} className="activity-checkbox">
                                <input
                                    type="checkbox"
                                    checked={selectedActivities.includes(id)}
                                    onChange={() => handleActivityToggle(id)}
                                    disabled={isLocked}
                                />
                                <span className="activity-name">{activity.name}</span>
                                <span className="activity-meta">
                                    {activity.hours_per_week}h/week • ${activity.cost_per_semester}/sem
                                </span>
                            </label>
                        ))}
                    </div>
                </div>
            </div>

            {/* Forecast Section */}
            <div className="forecast-section">
                <div className="forecast-header">
                    <h3>📊 Forecast Your Week</h3>
                    <button
                        onClick={handleForecast}
                        disabled={isLocked || forecastLoading}
                        className="forecast-btn"
                    >
                        {forecastLoading ? 'Calculating...' : 'Calculate'}
                    </button>
                </div>

                {forecastError && <div className="forecast-error">{forecastError}</div>}

                {forecast && (
                    <div className="forecast-card">
                        <div className="forecast-grid">
                            <div className="forecast-stat">
                                <label>Course Hours</label>
                                <strong>{forecast.weekly_load.course_hours}</strong>
                            </div>
                            <div className="forecast-stat">
                                <label>Work Hours</label>
                                <strong>{forecast.weekly_load.work_hours}</strong>
                            </div>
                            <div className="forecast-stat">
                                <label>Activity Hours</label>
                                <strong>{forecast.weekly_load.activity_hours}</strong>
                            </div>
                            <div className="forecast-stat">
                                <label>Total Hours</label>
                                <strong className={forecast.weekly_load.total_hours > 60 ? 'warn' : ''}>
                                    {forecast.weekly_load.total_hours}
                                </strong>
                            </div>
                        </div>

                        {forecast.weekly_load.overload > 0 && (
                            <div className={`overload-warning overload-${Math.min(3, Math.ceil(forecast.weekly_load.overload / 8))}`}>
                                <strong>⚠️ Overload: {forecast.weekly_load.overload} hours</strong>
                                <p>This will impact your stress and GPA. Consider reducing work or courses.</p>
                            </div>
                        )}

                        {forecast.warnings.length > 0 && (
                            <div className="warnings-list">
                                {forecast.warnings.map((warning, idx) => (
                                    <div key={idx} className="warning-item">
                                        {warning}
                                    </div>
                                ))}
                            </div>
                        )}
                    </div>
                )}
            </div>

            {/* Action Buttons */}
            <div className="planning-actions">
                {!isLocked ? (
                    <>
                        <button onClick={handleSave} disabled={saving} className="btn-primary">
                            {saving ? 'Saving...' : '💾 Save Draft'}
                        </button>
                        <button onClick={handleLock} disabled={locking || !player.plan} className="btn-success">
                            {locking ? 'Locking...' : '🔒 Lock Plan'}
                        </button>
                    </>
                ) : (
                    <div className="locked-notice">
                        <p>✅ Your plan is locked. Ready to take your exam!</p>
                    </div>
                )}
            </div>
        </div>
    )
}
