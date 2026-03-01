import { useState, useEffect } from 'react'
import { Player } from '../utils/api'
import './StorePanel.css'

interface Purchase {
    purchase_id: string
    name: string
    emoji: string
    description: string
    cost: number
    category: string
    one_time: boolean
    max_per_semester?: number
    effects: { stat: string; change: number }[]
    is_affordable: boolean
    current_balance: number
}

interface PurchaseSuggestion {
    purchase_id: string
    name: string
    emoji: string
    cost: number
    reason: string
    is_affordable: boolean
}

interface StorePanelProps {
    player: Player
}

export function StorePanel({ player }: StorePanelProps) {
    const [purchases, setPurchases] = useState<Purchase[]>([])
    const [suggestions, setSuggestions] = useState<PurchaseSuggestion[]>([])
    const [history, setHistory] = useState<any[]>([])
    const [loading, setLoading] = useState(true)
    const [isPurchasing, setIsPurchasing] = useState(false)
    const [error, setError] = useState<string | null>(null)
    const [activeTab, setActiveTab] = useState<'available' | 'suggestions' | 'history'>('available')
    const [selectedCategory, setSelectedCategory] = useState<string | null>(null)
    const [purchaseMessage, setPurchaseMessage] = useState<string | null>(null)
    const [purchaseSuccess, setPurchaseSuccess] = useState(false)

    const fetchPurchases = async () => {
        const response = await fetch(
            `http://localhost:8000/api/store/available?player_id=${player.id}`
        )
        if (!response.ok) {
            throw new Error('Failed to load purchases')
        }
        const data = await response.json()
        setPurchases(data.purchases || [])
    }

    const fetchSuggestions = async () => {
        const response = await fetch(
            `http://localhost:8000/api/store/suggestions?player_id=${player.id}`
        )
        if (!response.ok) {
            throw new Error('Failed to load suggestions')
        }
        const data = await response.json()
        setSuggestions(data.suggestions || [])
    }

    const fetchHistory = async () => {
        const response = await fetch(
            `http://localhost:8000/api/store/history?player_id=${player.id}`
        )
        if (!response.ok) {
            throw new Error('Failed to load history')
        }
        const data = await response.json()
        setHistory(data.history || [])
    }

    const refreshStoreData = async () => {
        await Promise.allSettled([fetchPurchases(), fetchSuggestions(), fetchHistory()])
    }

    // Fetch available purchases
    useEffect(() => {
        const initStoreData = async () => {
            try {
                setLoading(true)
                setError(null)
                await refreshStoreData()
            } catch (err) {
                setError('Error connecting to store')
                console.error(err)
            } finally {
                setLoading(false)
            }
        }

        initStoreData()
    }, [player.id])

    const handlePurchase = async (purchaseId: string) => {
        try {
            setIsPurchasing(true)
            setPurchaseMessage(null)
            const response = await fetch(
                `http://localhost:8000/api/store/purchase/${purchaseId}?player_id=${player.id}`,
                { method: 'POST' }
            )

            const data = await response.json()

            if (response.ok) {
                setPurchaseSuccess(true)
                setPurchaseMessage(`✅ ${data.message}`)
                await refreshStoreData()
            } else {
                setPurchaseSuccess(false)
                setPurchaseMessage(`❌ ${data.detail || 'Purchase failed'}`)
            }
        } catch (err) {
            setPurchaseSuccess(false)
            setPurchaseMessage('❌ Error processing purchase')
            console.error(err)
        } finally {
            setIsPurchasing(false)
        }
    }

    const filteredPurchases = selectedCategory
        ? purchases.filter((p) => p.category === selectedCategory)
        : purchases

    const categories = Array.from(new Set(purchases.map((p) => p.category)))

    if (loading) {
        return (
            <div className="store-panel">
                <div className="store-loading">Loading store...</div>
            </div>
        )
    }

    return (
        <div className="store-panel">
            <div className="store-header">
                <h2>🛍️ Life Store</h2>
                <div className="store-balance">Balance: ${player.finance?.balance.toFixed(2) || '0.00'}</div>
            </div>

            {purchaseMessage && (
                <div className={`purchase-message ${purchaseSuccess ? 'success' : 'error'}`}>
                    {purchaseMessage}
                </div>
            )}

            {error && <div className="store-error">{error}</div>}

            <div className="store-tabs">
                <button
                    className={`store-tab ${activeTab === 'available' ? 'active' : ''}`}
                    onClick={() => setActiveTab('available')}
                >
                    Available ({purchases.length})
                </button>
                <button
                    className={`store-tab ${activeTab === 'suggestions' ? 'active' : ''}`}
                    onClick={() => setActiveTab('suggestions')}
                >
                    Suggestions ({suggestions.length})
                </button>
                <button
                    className={`store-tab ${activeTab === 'history' ? 'active' : ''}`}
                    onClick={() => setActiveTab('history')}
                >
                    History ({history.length})
                </button>
            </div>

            {/* Available Purchases Tab */}
            {activeTab === 'available' && (
                <div className="store-content">
                    <div className="category-filter">
                        <button
                            className={`category-btn ${selectedCategory === null ? 'active' : ''}`}
                            onClick={() => setSelectedCategory(null)}
                        >
                            All
                        </button>
                        {categories.map((cat) => (
                            <button
                                key={cat}
                                className={`category-btn ${selectedCategory === cat ? 'active' : ''}`}
                                onClick={() => setSelectedCategory(cat)}
                            >
                                {cat}
                            </button>
                        ))}
                    </div>

                    <div className="purchases-grid">
                        {filteredPurchases.map((purchase) => (
                            <div
                                key={purchase.purchase_id}
                                className={`purchase-card ${!purchase.is_affordable ? 'unaffordable' : ''}`}
                            >
                                <div className="purchase-emoji">{purchase.emoji}</div>
                                <h3>{purchase.name}</h3>
                                <p className="purchase-description">{purchase.description}</p>
                                <div className="purchase-cost">${purchase.cost.toFixed(2)}</div>

                                <div className="purchase-effects">
                                    {purchase.effects.slice(0, 3).map((effect, idx) => (
                                        <div key={idx} className="effect-badge">
                                            {effect.stat}: {effect.change > 0 ? '+' : ''}{effect.change.toFixed(0)}
                                        </div>
                                    ))}
                                    {purchase.effects.length > 3 && (
                                        <div className="effect-badge">+{purchase.effects.length - 3} more</div>
                                    )}
                                </div>

                                <button
                                    className={`purchase-btn ${!purchase.is_affordable ? 'disabled' : ''}`}
                                    onClick={() => handlePurchase(purchase.purchase_id)}
                                    disabled={!purchase.is_affordable || isPurchasing}
                                >
                                    {isPurchasing ? 'Processing...' : (purchase.is_affordable ? 'Buy Now' : 'Too Expensive')}
                                </button>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Suggestions Tab */}
            {activeTab === 'suggestions' && (
                <div className="store-content">
                    {suggestions.length === 0 ? (
                        <div className="empty-state">No suggestions at the moment</div>
                    ) : (
                        <div className="suggestions-list">
                            {suggestions.map((suggestion) => (
                                <div
                                    key={suggestion.purchase_id}
                                    className={`suggestion-card ${!suggestion.is_affordable ? 'unaffordable' : ''}`}
                                >
                                    <div className="suggestion-header">
                                        <div className="suggestion-title">
                                            <span className="suggestion-emoji">{suggestion.emoji}</span>
                                            <h3>{suggestion.name}</h3>
                                        </div>
                                        <div className="suggestion-cost">${suggestion.cost.toFixed(2)}</div>
                                    </div>
                                    <p className="suggestion-reason">💡 {suggestion.reason}</p>
                                    <button
                                        className={`purchase-btn ${!suggestion.is_affordable ? 'disabled' : ''}`}
                                        onClick={() => handlePurchase(suggestion.purchase_id)}
                                        disabled={!suggestion.is_affordable || isPurchasing}
                                    >
                                        {isPurchasing ? 'Processing...' : (suggestion.is_affordable ? 'Buy Now' : 'Too Expensive')}
                                    </button>
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            )}

            {/* Purchase History Tab */}
            {activeTab === 'history' && (
                <div className="store-content">
                    {history.length === 0 ? (
                        <div className="empty-state">No purchases yet</div>
                    ) : (
                        <div className="history-list">
                            {history.map((item, idx) => (
                                <div key={idx} className="history-item">
                                    <div className="history-header">
                                        <h4>{item.purchase_name}</h4>
                                        <span className="history-cost">-${item.cost.toFixed(2)}</span>
                                    </div>
                                    <div className="history-details">
                                        <small>Semester {item.semester}</small>
                                        <div className="history-effects">
                                            {Object.entries(item.effects).map(([stat, change]: [string, any]) => (
                                                <span key={stat} className="history-effect">
                                                    {stat}: {change > 0 ? '+' : ''}{change.toFixed(0)}
                                                </span>
                                            ))}
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            )}
        </div>
    )
}
