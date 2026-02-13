import React, { useState } from 'react'
import { Player } from '../utils/api'
import './GameBoard.css'

interface GameBoardProps {
    player: Player
    onLogout: () => void
}

export function GameBoard({ player, onLogout }: GameBoardProps) {
    const [activeTab, setActiveTab] = useState<'stats' | 'finance' | 'planning'>('stats')

    return (
        <div className="game-container">
            <header className="game-header">
                <div className="header-content">
                    <h1>🎮 Life Sprint</h1>
                    <div className="player-info">
                        <span className="player-name">{player.name}</span>
                        <span className="player-semester">Semester {player.semester}</span>
                    </div>
                </div>
                <button onClick={onLogout} className="logout-btn">Logout</button>
            </header>

            <div className="game-content">
                <nav className="game-nav">
                    <button
                        className={`nav-btn ${activeTab === 'stats' ? 'active' : ''}`}
                        onClick={() => setActiveTab('stats')}
                    >
                        📊 Stats
                    </button>
                    <button
                        className={`nav-btn ${activeTab === 'finance' ? 'active' : ''}`}
                        onClick={() => setActiveTab('finance')}
                    >
                        💰 Finance
                    </button>
                    <button
                        className={`nav-btn ${activeTab === 'planning' ? 'active' : ''}`}
                        onClick={() => setActiveTab('planning')}
                    >
                        📅 Planning
                    </button>
                </nav>

                <main className="game-main">
                    {activeTab === 'stats' && (
                        <section className="tab-content">
                            <h2>Your Stats</h2>
                            <div className="stats-grid">
                                <div className="stat-card">
                                    <h3>GPA</h3>
                                    <p className="stat-value">{player.stats?.gpa?.toFixed(2) || 'N/A'}</p>
                                </div>
                                <div className="stat-card">
                                    <h3>Stress</h3>
                                    <p className="stat-value">{player.stats?.stress?.toFixed(0) || 'N/A'}%</p>
                                </div>
                                <div className="stat-card">
                                    <h3>Network</h3>
                                    <p className="stat-value">{player.stats?.network?.toFixed(0) || 'N/A'}</p>
                                </div>
                                <div className="stat-card">
                                    <h3>Health</h3>
                                    <p className="stat-value">{player.stats?.health?.toFixed(0) || 'N/A'}%</p>
                                </div>
                            </div>
                        </section>
                    )}

                    {activeTab === 'finance' && (
                        <section className="tab-content">
                            <h2>Financial Status</h2>
                            <div className="finance-info">
                                <div className="info-card">
                                    <label>Cash Balance</label>
                                    <p className="amount">${player.finance?.balance?.toFixed(2) || '0.00'}</p>
                                </div>
                                <div className="info-card">
                                    <label>Monthly Expenses</label>
                                    <p className="amount">${player.finance?.monthly_expenses?.toFixed(2) || '0.00'}</p>
                                </div>
                                <div className="info-card">
                                    <label>Tuition (Per Semester)</label>
                                    <p className="amount">${player.finance?.tuition_per_semester?.toFixed(2) || '0.00'}</p>
                                </div>
                                <div className="info-card">
                                    <label>Scholarship</label>
                                    <p className="amount">${player.finance?.scholarship_per_semester?.toFixed(2) || '0.00'}</p>
                                </div>
                            </div>
                        </section>
                    )}

                    {activeTab === 'planning' && (
                        <section className="tab-content">
                            <h2>Semester Planning</h2>
                            <div className="planning-info">
                                <p>Plan your semester activities and time allocation.</p>
                                {player.plan ? (
                                    <div className="plan-details">
                                        <p>Current plan is active</p>
                                    </div>
                                ) : (
                                    <div className="no-plan">
                                        <p>No plan created yet. Create one to get started!</p>
                                    </div>
                                )}
                            </div>
                        </section>
                    )}
                </main>
            </div>

            <footer className="game-footer">
                <p>College: {player.college_id} | Major: {player.major_id} | Age: {player.age}</p>
            </footer>
        </div>
    )
}
