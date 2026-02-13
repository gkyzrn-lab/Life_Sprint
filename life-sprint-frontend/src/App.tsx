import React, { useState } from 'react'
import { OnboardingModal } from './components/OnboardingModal'
import { GameBoard } from './components/GameBoard'
import { Player } from './utils/api'
import './App.css'

export function App() {
    const [playerName, setPlayerName] = useState('')
    const [player, setPlayer] = useState<Player | null>(null)
    const [showNameInput, setShowNameInput] = useState(true)

    const handleStartGame = () => {
        if (playerName.trim().length > 0) {
            setShowNameInput(false)
        }
    }

    const handleOnboardingComplete = (completedPlayer: Player) => {
        setPlayer(completedPlayer)
    }

    const handleLogout = () => {
        setPlayer(null)
        setPlayerName('')
        setShowNameInput(true)
    }

    // Show name input screen
    if (showNameInput) {
        return (
            <div className="splash-container">
                <div className="splash-content">
                    <h1 className="splash-title">🎮 Life Sprint</h1>
                    <p className="splash-subtitle">Navigate college life, one semester at a time</p>

                    <div className="name-input-section">
                        <input
                            type="text"
                            value={playerName}
                            onChange={(e) => setPlayerName(e.target.value)}
                            onKeyPress={(e) => e.key === 'Enter' && handleStartGame()}
                            placeholder="Enter your name"
                            className="name-input"
                            autoFocus
                        />
                        <button onClick={handleStartGame} className="start-btn">
                            Start Playing
                        </button>
                    </div>

                    <div className="splash-footer">
                        <p>Learn to balance academics, finances, and well-being</p>
                    </div>
                </div>
            </div>
        )
    }

    // Show onboarding if player is being created
    if (!player) {
        return <OnboardingModal playerName={playerName} onComplete={handleOnboardingComplete} />
    }

    // Show game board
    return <GameBoard player={player} onLogout={handleLogout} />
}

export default App
