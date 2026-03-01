import React, { useState, useEffect } from 'react';
import './TutorialQuestModal.css';

interface TutorialQuestion {
    id: string;
    text: string;
    choices: Array<{
        id: string;
        text: string;
        correct: boolean;
        explanation: string;
    }>;
    hint: string;
    learning_objective: string;
}

interface TutorialGame {
    id: string;
    title: string;
    description: string;
    mascot_dialogue: string;
    game_type: string;
    questions: TutorialQuestion[];
    points_reward: number;
    estimated_duration_seconds: number;
}

interface QuestStep {
    id: string;
    title: string;
    description: string;
    game_id: string;
    required_score: number;
    rewards: Record<string, any>;
    next_step_id: string | null;
}

interface QuestProgress {
    quest_id: string;
    quest_title: string;
    total_steps: number;
    completed_steps: number;
    progress_percent: number;
    current_step: QuestStep | null;
    is_complete: boolean;
    total_points_earned: number;
}

interface Props {
    playerId: string;
    onComplete: () => void;
    onSkip: () => void;
}

export function TutorialQuestModal({ playerId, onComplete, onSkip }: Props) {
    const [loading, setLoading] = useState(true);
    const [questProgress, setQuestProgress] = useState<QuestProgress | null>(null);
    const [currentGame, setCurrentGame] = useState<TutorialGame | null>(null);
    const [mascotDialogue, setMascotDialogue] = useState<string>('');
    const [showMascot, setShowMascot] = useState(true);

    // Game state
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
    const [selectedAnswers, setSelectedAnswers] = useState<Record<string, string>>({});
    const [showHint, setShowHint] = useState(false);
    const [submitting, setSubmitting] = useState(false);
    const [gameResult, setGameResult] = useState<any>(null);

    useEffect(() => {
        startQuest();
    }, []);

    const startQuest = async () => {
        try {
            const response = await fetch(`http://localhost:8000/tutorial/${playerId}/start`, {
                method: 'POST',
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.detail || 'Failed to start tutorial');
            }

            const data = await response.json();
            setQuestProgress(data.progress);
            setCurrentGame(data.first_game);
            setMascotDialogue(data.mascot_dialogue);
            setLoading(false);
        } catch (error) {
            console.error('Failed to start tutorial quest:', error);
            alert('Failed to start tutorial. Please try again.');
        }
    };

    const handleSelectAnswer = (questionId: string, choiceId: string) => {
        setSelectedAnswers(prev => ({
            ...prev,
            [questionId]: choiceId,
        }));
    };

    const handleNextQuestion = () => {
        if (currentGame && currentQuestionIndex < currentGame.questions.length - 1) {
            setCurrentQuestionIndex(prev => prev + 1);
            setShowHint(false);
        }
    };

    const handlePreviousQuestion = () => {
        if (currentQuestionIndex > 0) {
            setCurrentQuestionIndex(prev => prev - 1);
            setShowHint(false);
        }
    };

    const handleSubmitGame = async () => {
        if (!currentGame) return;

        // Validate all questions answered
        const unansweredQuestions = currentGame.questions.filter(
            q => !selectedAnswers[q.id]
        );

        if (unansweredQuestions.length > 0) {
            alert(`Please answer all questions before submitting. (${unansweredQuestions.length} remaining)`);
            return;
        }

        setSubmitting(true);

        try {
            const answers = Object.entries(selectedAnswers).map(([qId, cId]) => ({
                question_id: qId,
                choice_id: cId,
            }));

            const response = await fetch('http://localhost:8000/tutorial/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    player_id: playerId,
                    game_id: currentGame.id,
                    answers: answers,
                }),
            });

            const result = await response.json();
            setGameResult(result);
            setMascotDialogue(result.mascot_dialogue);

        } catch (error) {
            console.error('Failed to submit tutorial game:', error);
            alert('Failed to submit. Please try again.');
        } finally {
            setSubmitting(false);
        }
    };

    const handleContinueAfterResult = () => {
        if (!gameResult) return;

        if (gameResult.quest_complete) {
            // Tutorial fully complete!
            onComplete();
            return;
        }

        if (gameResult.passed && gameResult.next_step) {
            // Load next game
            setCurrentGame(gameResult.next_step.game);
            setCurrentQuestionIndex(0);
            setSelectedAnswers({});
            setShowHint(false);
            setGameResult(null);

            // Update progress
            setQuestProgress(prev => prev ? {
                ...prev,
                completed_steps: prev.completed_steps + 1,
                progress_percent: ((prev.completed_steps + 1) / prev.total_steps) * 100,
            } : null);

        } else if (!gameResult.passed) {
            // Failed, restart current game
            setCurrentQuestionIndex(0);
            setSelectedAnswers({});
            setShowHint(false);
            setGameResult(null);
        }
    };

    const handleSkipTutorial = async () => {
        if (!confirm('Are you sure you want to skip the tutorial? You can always come back later.')) {
            return;
        }

        try {
            await fetch(`http://localhost:8000/tutorial/${playerId}/skip`, {
                method: 'POST',
            });
            onSkip();
        } catch (error) {
            console.error('Failed to skip tutorial:', error);
        }
    };

    if (loading) {
        return (
            <div className="tutorial-quest-modal">
                <div className="tutorial-content">
                    <div className="loading-spinner">Loading tutorial...</div>
                </div>
            </div>
        );
    }

    if (gameResult) {
        return (
            <div className="tutorial-quest-modal">
                <div className="tutorial-content">
                    {/* Result Screen */}
                    <div className="tutorial-result">
                        <div className="mascot-section">
                            <div className="mascot-avatar">🏃</div>
                            <div className="mascot-bubble">{mascotDialogue}</div>
                        </div>

                        <div className="result-summary">
                            <h2>{gameResult.passed ? '✅ Nice Work!' : '❌ Not Quite'}</h2>
                            <div className="score-display">
                                <div className="score-circle">
                                    <span className="score-number">{Math.round(gameResult.score_percent)}</span>
                                    <span className="score-label">%</span>
                                </div>
                                <div className="score-details">
                                    <p>{gameResult.correct_count} / {gameResult.total_questions} correct</p>
                                    {gameResult.passed && (
                                        <p className="points-earned">+{gameResult.points_earned} points!</p>
                                    )}
                                </div>
                            </div>
                        </div>

                        {/* Feedback */}
                        <div className="feedback-section">
                            <h3>Review Your Answers</h3>
                            {gameResult.feedback.map((fb: any, idx: number) => (
                                <div key={idx} className={`feedback-item ${fb.is_correct ? 'correct' : 'incorrect'}`}>
                                    <div className="feedback-question">{fb.question_text}</div>
                                    <div className="feedback-answer">
                                        <strong>Your answer:</strong> {fb.your_answer}
                                        {fb.is_correct ? ' ✓' : ' ✗'}
                                    </div>
                                    <div className="feedback-explanation">{fb.explanation}</div>
                                </div>
                            ))}
                        </div>

                        {/* Progress Bar */}
                        {questProgress && (
                            <div className="quest-progress-bar">
                                <div className="progress-label">
                                    Tutorial Progress: {questProgress.completed_steps} / {questProgress.total_steps}
                                </div>
                                <div className="progress-bar">
                                    <div
                                        className="progress-fill"
                                        style={{ width: `${questProgress.progress_percent}%` }}
                                    />
                                </div>
                            </div>
                        )}

                        <div className="result-actions">
                            {gameResult.passed ? (
                                <button onClick={handleContinueAfterResult} className="btn-primary">
                                    {gameResult.quest_complete ? 'Start Playing! 🎮' : 'Next Challenge →'}
                                </button>
                            ) : (
                                <button onClick={handleContinueAfterResult} className="btn-warning">
                                    Try Again
                                </button>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    if (!currentGame) {
        return null;
    }

    const currentQuestion = currentGame.questions[currentQuestionIndex];
    const isLastQuestion = currentQuestionIndex === currentGame.questions.length - 1;
    const allQuestionsAnswered = currentGame.questions.every(q => selectedAnswers[q.id]);

    return (
        <div className="tutorial-quest-modal">
            <div className="tutorial-content">
                {/* Header with progress */}
                <div className="tutorial-header">
                    <div className="quest-title">
                        <h2>{currentGame.title}</h2>
                        <p className="quest-subtitle">{currentGame.description}</p>
                    </div>

                    {questProgress && (
                        <div className="header-progress">
                            <span>Step {questProgress.completed_steps + 1} of {questProgress.total_steps}</span>
                            <div className="mini-progress-bar">
                                <div
                                    className="mini-progress-fill"
                                    style={{ width: `${questProgress.progress_percent}%` }}
                                />
                            </div>
                        </div>
                    )}

                    <button onClick={handleSkipTutorial} className="btn-skip">
                        Skip Tutorial
                    </button>
                </div>

                {/* Mascot dialogue */}
                {showMascot && (
                    <div className="mascot-section">
                        <div className="mascot-avatar bounce">🏃</div>
                        <div className="mascot-bubble">
                            {mascotDialogue}
                            <button
                                onClick={() => setShowMascot(false)}
                                className="mascot-close"
                                title="Hide mascot"
                            >
                                ×
                            </button>
                        </div>
                    </div>
                )}

                {/* Question */}
                <div className="question-section">
                    <div className="question-header">
                        <span className="question-number">
                            Question {currentQuestionIndex + 1} of {currentGame.questions.length}
                        </span>
                        <button
                            onClick={() => setShowHint(!showHint)}
                            className="btn-hint"
                        >
                            {showHint ? '🔒 Hide Hint' : '💡 Show Hint'}
                        </button>
                    </div>

                    <div className="question-text">{currentQuestion.text}</div>

                    {showHint && (
                        <div className="hint-box">
                            <strong>💡 Hint:</strong> {currentQuestion.hint}
                        </div>
                    )}

                    {/* Choices */}
                    <div className="choices-list">
                        {currentQuestion.choices.map((choice) => (
                            <button
                                key={choice.id}
                                onClick={() => handleSelectAnswer(currentQuestion.id, choice.id)}
                                className={`choice-button ${selectedAnswers[currentQuestion.id] === choice.id ? 'selected' : ''
                                    }`}
                            >
                                <span className="choice-letter">{choice.id.toUpperCase()}</span>
                                <span className="choice-text">{choice.text}</span>
                                {selectedAnswers[currentQuestion.id] === choice.id && (
                                    <span className="choice-checkmark">✓</span>
                                )}
                            </button>
                        ))}
                    </div>
                </div>

                {/* Navigation */}
                <div className="tutorial-navigation">
                    <button
                        onClick={handlePreviousQuestion}
                        disabled={currentQuestionIndex === 0}
                        className="btn-secondary"
                    >
                        ← Previous
                    </button>

                    {!isLastQuestion ? (
                        <button
                            onClick={handleNextQuestion}
                            disabled={!selectedAnswers[currentQuestion.id]}
                            className="btn-primary"
                        >
                            Next →
                        </button>
                    ) : (
                        <button
                            onClick={handleSubmitGame}
                            disabled={!allQuestionsAnswered || submitting}
                            className="btn-success"
                        >
                            {submitting ? 'Submitting...' : `Submit (${currentGame.points_reward} pts)`}
                        </button>
                    )}
                </div>

                {/* Learning Objective Footer */}
                <div className="learning-objective">
                    <strong>🎯 You'll learn:</strong> {currentQuestion.learning_objective}
                </div>
            </div>
        </div>
    );
}
