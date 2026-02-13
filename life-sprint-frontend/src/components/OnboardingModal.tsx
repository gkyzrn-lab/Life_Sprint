import React, { useState, useEffect } from 'react'
import { TutorialStep, getTutorialSequence, completeTutorial, disableTutorials, createPlayer } from '../utils/api'
import './OnboardingModal.css'

interface OnboardingModalProps {
    playerName: string
    onComplete: (player: any) => void
}

export function OnboardingModal({ playerName, onComplete }: OnboardingModalProps) {
    const [currentStep, setCurrentStep] = useState(0)
    const [tutorials, setTutorials] = useState<TutorialStep[]>([])
    const [playerId, setPlayerId] = useState<string | null>(null)
    const [progress, setProgress] = useState(0)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {
        const initGame = async () => {
            try {
                setLoading(true)
                // 1. Create player
                const player = await createPlayer(playerName, 'nyc_public', 'cs')
                setPlayerId(player.id)

                // 2. Fetch tutorial sequence
                const { sequence } = await getTutorialSequence()
                setTutorials(sequence)
                setLoading(false)
            } catch (err) {
                setError(err instanceof Error ? err.message : 'Failed to initialize game')
                setLoading(false)
            }
        }

        initGame()
    }, [playerName])

    const handleNext = async () => {
        if (!playerId) return

        try {
            setLoading(true)
            // Mark current tutorial as complete
            const response = await completeTutorial(playerId, tutorials[currentStep].step_id)
            setProgress(response.completion_percentage)

            if (currentStep < tutorials.length - 1) {
                setCurrentStep(currentStep + 1)
            } else {
                // Onboarding complete!
                const playerResponse = await fetch(`http://localhost:8000/player/${playerId}`)
                const finalPlayer = await playerResponse.json()
                onComplete(finalPlayer)
            }
            setLoading(false)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to complete tutorial')
            setLoading(false)
        }
    }

    const handleSkip = async () => {
        if (!playerId) return

        try {
            setLoading(true)
            // Disable tutorials and proceed
            await disableTutorials(playerId)
            const playerResponse = await fetch(`http://localhost:8000/player/${playerId}`)
            const finalPlayer = await playerResponse.json()
            onComplete(finalPlayer)
            setLoading(false)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to skip tutorials')
            setLoading(false)
        }
    }

    if (error) {
        return (
            <div className="onboarding-container">
                <div className="onboarding-modal">
                    <div className="error-message">
                        <h2>Error</h2>
                        <p>{error}</p>
                        <p>Make sure the backend is running at http://localhost:8000</p>
                    </div>
                </div>
            </div>
        )
    }

    if (loading || tutorials.length === 0) {
        return (
            <div className="onboarding-container">
                <div className="onboarding-modal">
                    <div className="loading">
                        <div className="spinner"></div>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
        )
    }

    const tutorial = tutorials[currentStep]

    return (
        <div className="onboarding-container">
            <div className="onboarding-modal">
                <div className="tutorial-content">
                    <h1>{tutorial.title}</h1>
                    <p className="description">{tutorial.description}</p>
                    {tutorial.action_hint && <p className="hint">{tutorial.action_hint}</p>}
                </div>

                <div className="progress-section">
                    <div className="progress-bar">
                        <div className="progress-fill" style={{ width: `${progress}%` }}></div>
                    </div>
                    <p className="progress-text">
                        {currentStep + 1} of {tutorials.length}
                    </p>
                </div>

                <div className="button-group">
                    <button onClick={handleNext} className="btn btn-primary" disabled={loading}>
                        {loading ? 'Loading...' : currentStep < tutorials.length - 1 ? 'Next' : 'Start Playing'}
                    </button>
                    <button onClick={handleSkip} className="btn btn-secondary" disabled={loading}>
                        Skip Tutorial
                    </button>
                </div>
            </div>
        </div>
    )
}
