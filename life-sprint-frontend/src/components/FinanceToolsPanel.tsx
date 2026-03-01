import React from 'react'
import {
    Player,
    financeBorrow,
    financeAccrueInSchoolInterest,
    financeStartRepayment,
    financeSetRepaymentProfile,
    financeRepayMonths,
    getPlayer,
    FinanceLoanRecord,
} from '../utils/api'
import { UIButton, UICard } from './ui/UIPrimitives'
import './FinanceToolsPanel.css'

interface FinanceToolsPanelProps {
    player: Player
    onPlayerUpdate?: (player: Player) => void
    onRefreshPlayer?: (playerId: string) => Promise<Player | null>
}

interface FinanceSnapshot {
    balance: number
    monthlyExpenses: number
    tuitionPerSemester: number
    scholarshipPerSemester: number
    loans: FinanceLoanRecord[]
    planType: 'standard' | 'idr'
    annualIncome: number
    familySize: number
}

interface ProjectionResult {
    months: number
    endingBalance: number
    endingDebt: number
    totalPaid: number
    totalInterest: number
    projectedMonthlyPayment: number
}

interface StrategyProjection {
    strategy: 'avalanche' | 'snowball'
    payoffMonths: number
    interestPaid: number
}

interface GoalState {
    emergencyFundTarget: number
    debtReductionTarget: number
}

interface FinanceActivity {
    id: string
    at: string
    action: string
    details: string
}

const DEFAULT_GOALS: GoalState = {
    emergencyFundTarget: 10000,
    debtReductionTarget: 0.2,
}

function toCurrency(value: number): string {
    return `$${Number(value || 0).toFixed(2)}`
}

function clampNonNegative(value: number): number {
    return Number.isFinite(value) ? Math.max(0, value) : 0
}

function computeMonthlyRate(loans: FinanceLoanRecord[]): number {
    const principal = loans.reduce((sum, loan) => sum + Number(loan.principal || 0), 0)
    if (principal <= 0) return 0
    const weightedAnnual = loans.reduce(
        (sum, loan) => sum + Number(loan.principal || 0) * Number(loan.annual_interest_rate || 0),
        0,
    ) / principal
    return weightedAnnual / 12
}

function computeStandardMonthlyPayment(loans: FinanceLoanRecord[]): number {
    const knownMin = loans.reduce((sum, loan) => sum + Number(loan.minimum_payment || 0), 0)
    if (knownMin > 0) return knownMin

    const fallback = loans.reduce((sum, loan) => {
        const principal = Number(loan.principal || 0)
        if (principal <= 0) return sum
        const months = Math.max(1, Number(loan.repayment_months_remaining || 120))
        const monthlyRate = Number(loan.annual_interest_rate || 0) / 12
        if (monthlyRate <= 0) return sum + principal / months
        const denominator = 1 - Math.pow(1 + monthlyRate, -months)
        if (denominator <= 0) return sum + principal / months
        return sum + (principal * monthlyRate) / denominator
    }, 0)

    return fallback
}

function estimateIdrMonthlyPayment(annualIncome: number, familySize: number): number {
    const povertyBase = 15100
    const povertyPerPerson = 5400
    const povertyLine = povertyBase + Math.max(0, familySize - 1) * povertyPerPerson
    const discretionary = Math.max(0, annualIncome - povertyLine * 1.5)
    const annualPayment = discretionary * 0.1
    return annualPayment / 12
}

function projectScenario(
    snapshot: FinanceSnapshot,
    months: number,
    options?: {
        annualIncome?: number
        planType?: 'standard' | 'idr'
        monthlyExpensesDelta?: number
        monthlyExtraPayment?: number
    },
): ProjectionResult {
    const m = Math.max(1, Math.floor(months))
    const annualIncome = clampNonNegative(options?.annualIncome ?? snapshot.annualIncome)
    const planType = options?.planType ?? snapshot.planType
    const monthlyExpenses = clampNonNegative(snapshot.monthlyExpenses + Number(options?.monthlyExpensesDelta || 0))
    const monthlyIncome = annualIncome / 12
    const extraPayment = clampNonNegative(Number(options?.monthlyExtraPayment || 0))

    let balance = clampNonNegative(snapshot.balance)
    let debt = snapshot.loans.reduce((sum, loan) => sum + Number(loan.principal || 0) + Number(loan.accrued_interest || 0), 0)
    let totalPaid = 0
    let totalInterest = 0
    const monthlyRate = computeMonthlyRate(snapshot.loans)

    const standardPayment = computeStandardMonthlyPayment(snapshot.loans)
    const idrPayment = estimateIdrMonthlyPayment(annualIncome, snapshot.familySize)
    const projectedMonthlyPayment = (planType === 'idr' ? Math.min(standardPayment, idrPayment) : standardPayment) + extraPayment

    for (let i = 0; i < m; i += 1) {
        const interest = debt * monthlyRate
        debt += interest
        totalInterest += interest

        balance += monthlyIncome - monthlyExpenses
        if (balance < 0) balance = 0

        const payment = Math.min(balance, debt, projectedMonthlyPayment)
        balance -= payment
        debt -= payment
        totalPaid += payment

        if (debt <= 0.01) {
            debt = 0
            break
        }
    }

    return {
        months: m,
        endingBalance: clampNonNegative(balance),
        endingDebt: clampNonNegative(debt),
        totalPaid,
        totalInterest,
        projectedMonthlyPayment,
    }
}

function projectLoanPayoff(
    loans: FinanceLoanRecord[],
    strategy: 'avalanche' | 'snowball',
    monthlyBudget: number,
): StrategyProjection {
    const working = loans
        .filter((loan) => Number(loan.principal || 0) > 0)
        .map((loan) => ({
            principal: Number(loan.principal || 0),
            annualRate: Number(loan.annual_interest_rate || 0),
        }))

    if (working.length === 0 || monthlyBudget <= 0) {
        return {
            strategy,
            payoffMonths: 0,
            interestPaid: 0,
        }
    }

    let months = 0
    let interestPaid = 0
    const maxMonths = 720

    while (months < maxMonths) {
        const totalRemaining = working.reduce((sum, loan) => sum + loan.principal, 0)
        if (totalRemaining <= 0.01) break

        for (let i = 0; i < working.length; i += 1) {
            const interest = working[i].principal * (working[i].annualRate / 12)
            working[i].principal += interest
            interestPaid += interest
        }

        let remainingBudget = monthlyBudget
        const order = [...working]
        order.sort((a, b) => {
            if (strategy === 'avalanche') return b.annualRate - a.annualRate
            return a.principal - b.principal
        })

        for (let i = 0; i < order.length; i += 1) {
            if (remainingBudget <= 0) break
            const target = order[i]
            const pay = Math.min(remainingBudget, target.principal)
            target.principal -= pay
            remainingBudget -= pay
        }

        months += 1
    }

    return {
        strategy,
        payoffMonths: months,
        interestPaid,
    }
}

export default function FinanceToolsPanel({ player }: FinanceToolsPanelProps) {
    const [snapshot, setSnapshot] = React.useState<FinanceSnapshot>(() => ({
        balance: Number(player.finance?.balance ?? 0),
        monthlyExpenses: Number(player.finance?.monthly_expenses ?? 0),
        tuitionPerSemester: Number(player.finance?.tuition_per_semester ?? 0),
        scholarshipPerSemester: Number(player.finance?.scholarship_per_semester ?? 0),
        loans: Array.isArray(player.finance?.loan_portfolio?.loans) ? player.finance.loan_portfolio.loans : [],
        planType: (player.finance?.repayment_profile?.plan_type ?? 'standard') as 'standard' | 'idr',
        annualIncome: Number(player.finance?.repayment_profile?.annual_income ?? 0),
        familySize: Number(player.finance?.repayment_profile?.family_size ?? 1),
    }))

    const [borrowAmount, setBorrowAmount] = React.useState(2000)
    const [accrueMonths, setAccrueMonths] = React.useState(4)
    const [repayMonths, setRepayMonths] = React.useState(1)
    const [annualIncomeInput, setAnnualIncomeInput] = React.useState(snapshot.annualIncome || 60000)
    const [familySizeInput, setFamilySizeInput] = React.useState(snapshot.familySize || 1)
    const [planTypeInput, setPlanTypeInput] = React.useState<'standard' | 'idr'>(snapshot.planType)

    const [scenarioMonths, setScenarioMonths] = React.useState(12)
    const [scenarioIncome, setScenarioIncome] = React.useState(snapshot.annualIncome || 60000)
    const [scenarioPlanType, setScenarioPlanType] = React.useState<'standard' | 'idr'>(snapshot.planType)
    const [scenarioExpenseDelta, setScenarioExpenseDelta] = React.useState(0)
    const [scenarioExtraPayment, setScenarioExtraPayment] = React.useState(0)

    const [goals, setGoals] = React.useState<GoalState>(DEFAULT_GOALS)
    const [activityLog, setActivityLog] = React.useState<FinanceActivity[]>([])

    const [working, setWorking] = React.useState(false)
    const [message, setMessage] = React.useState<string | null>(null)
    const [error, setError] = React.useState<string | null>(null)

    const principal = snapshot.loans.reduce((sum, loan) => sum + Number(loan.principal || 0), 0)
    const accrued = snapshot.loans.reduce((sum, loan) => sum + Number(loan.accrued_interest || 0), 0)
    const totals = {
        principal,
        accrued,
        totalDebt: principal + accrued,
    }

    const standardMonthlyPayment = computeStandardMonthlyPayment(snapshot.loans)
    const estimatedIdrPayment = estimateIdrMonthlyPayment(snapshot.annualIncome, snapshot.familySize)
    const projectedCurrentPayment = snapshot.planType === 'idr'
        ? Math.min(standardMonthlyPayment, estimatedIdrPayment)
        : standardMonthlyPayment
    const monthlyIncome = Math.max(0, snapshot.annualIncome / 12)
    const debtToIncome = snapshot.annualIncome > 0 ? totals.totalDebt / snapshot.annualIncome : 0
    const paymentToIncome = monthlyIncome > 0 ? projectedCurrentPayment / monthlyIncome : 0
    const cashRunwayMonths = snapshot.monthlyExpenses > 0 ? snapshot.balance / snapshot.monthlyExpenses : 0
    const riskLevel = cashRunwayMonths < 1 || paymentToIncome > 0.35
        ? 'High'
        : (cashRunwayMonths < 3 || paymentToIncome > 0.2 ? 'Moderate' : 'Healthy')

    const projection6 = projectScenario(snapshot, 6)
    const projection12 = projectScenario(snapshot, 12)
    const projection24 = projectScenario(snapshot, 24)
    const scenarioProjection = projectScenario(snapshot, scenarioMonths, {
        annualIncome: scenarioIncome,
        planType: scenarioPlanType,
        monthlyExpensesDelta: scenarioExpenseDelta,
        monthlyExtraPayment: scenarioExtraPayment,
    })

    const strategyMonthlyBudget = Math.max(0, projectedCurrentPayment + scenarioExtraPayment)
    const avalanche = projectLoanPayoff(snapshot.loans, 'avalanche', strategyMonthlyBudget)
    const snowball = projectLoanPayoff(snapshot.loans, 'snowball', strategyMonthlyBudget)

    const emergencyFundProgress = goals.emergencyFundTarget > 0
        ? Math.min(1, snapshot.balance / goals.emergencyFundTarget)
        : 1
    const debtReductionProgress = totals.totalDebt > 0
        ? Math.min(1, Math.max(0, goals.debtReductionTarget))
        : 1

    React.useEffect(() => {
        const goalsRaw = localStorage.getItem(`finance_goals_${player.id}`)
        const logRaw = localStorage.getItem(`finance_activity_${player.id}`)

        if (goalsRaw) {
            try {
                const parsed = JSON.parse(goalsRaw)
                setGoals({
                    emergencyFundTarget: clampNonNegative(Number(parsed.emergencyFundTarget ?? DEFAULT_GOALS.emergencyFundTarget)),
                    debtReductionTarget: clampNonNegative(Number(parsed.debtReductionTarget ?? DEFAULT_GOALS.debtReductionTarget)),
                })
            } catch {
                setGoals(DEFAULT_GOALS)
            }
        }

        if (logRaw) {
            try {
                const parsed = JSON.parse(logRaw)
                if (Array.isArray(parsed)) {
                    setActivityLog(parsed)
                }
            } catch {
                setActivityLog([])
            }
        }
    }, [player.id])

    React.useEffect(() => {
        localStorage.setItem(`finance_goals_${player.id}`, JSON.stringify(goals))
    }, [goals, player.id])

    React.useEffect(() => {
        localStorage.setItem(`finance_activity_${player.id}`, JSON.stringify(activityLog.slice(0, 25)))
    }, [activityLog, player.id])

    const addActivity = (action: string, details: string) => {
        setActivityLog((prev) => [
            {
                id: `${Date.now()}_${Math.random().toString(16).slice(2)}`,
                at: new Date().toISOString(),
                action,
                details,
            },
            ...prev,
        ].slice(0, 25))
    }

    const refreshFromServer = async (forceRefresh: boolean = true) => {
        const fresh = await getPlayer(player.id, { forceRefresh })
        setSnapshot({
            balance: Number(fresh.finance?.balance ?? 0),
            monthlyExpenses: Number(fresh.finance?.monthly_expenses ?? 0),
            tuitionPerSemester: Number(fresh.finance?.tuition_per_semester ?? 0),
            scholarshipPerSemester: Number(fresh.finance?.scholarship_per_semester ?? 0),
            loans: Array.isArray(fresh.finance?.loan_portfolio?.loans) ? fresh.finance.loan_portfolio.loans : [],
            planType: (fresh.finance?.repayment_profile?.plan_type ?? 'standard') as 'standard' | 'idr',
            annualIncome: Number(fresh.finance?.repayment_profile?.annual_income ?? 0),
            familySize: Number(fresh.finance?.repayment_profile?.family_size ?? 1),
        })

        // Update parent player state
        if (onPlayerUpdate) {
            onPlayerUpdate(fresh)
        }
        return fresh
    }

    const runAction = async (fn: () => Promise<void>, actionLabel?: string, actionDetails?: string) => {
        try {
            setWorking(true)
            setError(null)
            setMessage(null)
            await fn()
            await refreshFromServer()
            if (actionLabel && actionDetails) {
                addActivity(actionLabel, actionDetails)
            }
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Finance action failed')
        } finally {
            setWorking(false)
        }
    }

    return (
        <section className="finance-tools-wrap">
            <h2>💰 Financial Tools</h2>

            {error && <div className="finance-alert finance-error">{error}</div>}
            {message && <div className="finance-alert finance-success">{message}</div>}

            <div className="finance-summary-grid">
                <UICard className="finance-summary-card">
                    <label>Cash Balance</label>
                    <p>{toCurrency(snapshot.balance)}</p>
                </UICard>
                <UICard className="finance-summary-card">
                    <label>Monthly Expenses</label>
                    <p>{toCurrency(snapshot.monthlyExpenses)}</p>
                </UICard>
                <UICard className="finance-summary-card">
                    <label>Semester Tuition</label>
                    <p>{toCurrency(snapshot.tuitionPerSemester)}</p>
                </UICard>
                <UICard className="finance-summary-card">
                    <label>Scholarship</label>
                    <p>{toCurrency(snapshot.scholarshipPerSemester)}</p>
                </UICard>
            </div>

            <UICard className="finance-health-card">
                <h3>Financial Health Snapshot</h3>
                <div className="health-metrics-grid">
                    <div>
                        <span>Debt-to-Income</span>
                        <strong>{(debtToIncome * 100).toFixed(1)}%</strong>
                    </div>
                    <div>
                        <span>Payment Burden</span>
                        <strong>{(paymentToIncome * 100).toFixed(1)}%</strong>
                    </div>
                    <div>
                        <span>Cash Runway</span>
                        <strong>{cashRunwayMonths.toFixed(1)} months</strong>
                    </div>
                    <div>
                        <span>Risk Level</span>
                        <strong className={`risk-${riskLevel.toLowerCase()}`}>{riskLevel}</strong>
                    </div>
                </div>
            </UICard>

            <div className="finance-debt-summary">
                <UICard className="finance-debt-card">
                    <h3>Loan Portfolio</h3>
                    <div className="debt-metrics">
                        <div><span>Principal</span><strong>{toCurrency(totals.principal)}</strong></div>
                        <div><span>Accrued Interest</span><strong>{toCurrency(totals.accrued)}</strong></div>
                        <div><span>Total Debt</span><strong>{toCurrency(totals.totalDebt)}</strong></div>
                        <div><span>Current Plan</span><strong>{snapshot.planType.toUpperCase()}</strong></div>
                        <div><span>Projected Monthly Payment</span><strong>{toCurrency(projectedCurrentPayment)}</strong></div>
                        <div><span>Estimated IDR Payment</span><strong>{toCurrency(estimatedIdrPayment)}</strong></div>
                    </div>
                </UICard>
            </div>

            <div className="finance-tools-grid">
                <UICard className="finance-tool-card">
                    <h3>Borrow for Semester</h3>
                    <div className="tool-row">
                        <label>Needed Amount ($)</label>
                        <input
                            type="number"
                            min={0}
                            step={100}
                            value={borrowAmount}
                            onChange={(e) => setBorrowAmount(Number(e.target.value || 0))}
                        />
                    </div>
                    <UIButton
                        disabled={working}
                        onClick={() => runAction(async () => {
                            const res = await financeBorrow(player.id, borrowAmount)
                            setMessage(`Borrowed $${res.borrowed_total.toFixed(2)}. Remaining uncovered: $${res.remaining_uncovered.toFixed(2)}.`)
                        }, 'Borrow Funds', `Borrowed ${toCurrency(borrowAmount)}`)}
                    >
                        {working ? 'Processing...' : 'Borrow Funds'}
                    </UIButton>
                </UICard>

                <UICard className="finance-tool-card">
                    <h3>Accrue In-School Interest</h3>
                    <div className="tool-row">
                        <label>Months</label>
                        <input
                            type="number"
                            min={1}
                            max={24}
                            value={accrueMonths}
                            onChange={(e) => setAccrueMonths(Number(e.target.value || 1))}
                        />
                    </div>
                    <UIButton
                        variant="secondary"
                        disabled={working}
                        onClick={() => runAction(async () => {
                            const res = await financeAccrueInSchoolInterest(player.id, accrueMonths)
                            setMessage(`Applied in-school interest for ${res.months} months.`)
                        }, 'Accrue Interest', `Applied in-school interest for ${accrueMonths} month(s)`)}
                    >
                        {working ? 'Processing...' : 'Accrue Interest'}
                    </UIButton>
                </UICard>

                <UICard className="finance-tool-card">
                    <h3>Repayment Profile</h3>
                    <div className="tool-row">
                        <label>Plan</label>
                        <select value={planTypeInput} onChange={(e) => setPlanTypeInput(e.target.value as 'standard' | 'idr')}>
                            <option value="standard">Standard</option>
                            <option value="idr">IDR</option>
                        </select>
                    </div>
                    <div className="tool-row">
                        <label>Annual Income ($)</label>
                        <input
                            type="number"
                            min={0}
                            step={1000}
                            value={annualIncomeInput}
                            onChange={(e) => setAnnualIncomeInput(Number(e.target.value || 0))}
                        />
                    </div>
                    <div className="tool-row">
                        <label>Family Size</label>
                        <input
                            type="number"
                            min={1}
                            max={10}
                            value={familySizeInput}
                            onChange={(e) => setFamilySizeInput(Number(e.target.value || 1))}
                        />
                    </div>
                    <UIButton
                        variant="secondary"
                        disabled={working}
                        onClick={() => runAction(async () => {
                            await financeSetRepaymentProfile(player.id, planTypeInput, annualIncomeInput, familySizeInput)
                            setMessage(`Repayment profile set to ${planTypeInput.toUpperCase()}.`)
                        }, 'Update Repayment Profile', `${planTypeInput.toUpperCase()}, income ${toCurrency(annualIncomeInput)}`)}
                    >
                        {working ? 'Saving...' : 'Save Repayment Profile'}
                    </UIButton>
                </UICard>

                <UICard className="finance-tool-card">
                    <h3>Start / Simulate Repayment</h3>
                    <div className="tool-row">
                        <label>Repay Months</label>
                        <input
                            type="number"
                            min={1}
                            max={60}
                            value={repayMonths}
                            onChange={(e) => setRepayMonths(Number(e.target.value || 1))}
                        />
                    </div>
                    <div className="tool-actions">
                        <UIButton
                            variant="secondary"
                            disabled={working}
                            onClick={() => runAction(async () => {
                                await financeStartRepayment(player.id)
                                setMessage('Loans moved to repayment mode.')
                            }, 'Start Repayment', 'Transitioned loans to repayment')}
                        >
                            {working ? 'Working...' : 'Start Repayment'}
                        </UIButton>
                        <UIButton
                            disabled={working}
                            onClick={() => runAction(async () => {
                                const result = await financeRepayMonths(player.id, repayMonths)
                                setMessage(`Paid $${result.total_paid.toFixed(2)} over ${result.months} month(s).`)
                            }, 'Repay Months', `Repayment simulation for ${repayMonths} month(s)`)}
                        >
                            {working ? 'Working...' : 'Repay Months'}
                        </UIButton>
                    </div>
                </UICard>
            </div>

            <UICard className="projection-card">
                <h3>Forecast Dashboard</h3>
                <div className="projection-grid">
                    {[projection6, projection12, projection24].map((p) => (
                        <div key={p.months} className="projection-tile">
                            <h4>{p.months}-Month Outlook</h4>
                            <p><span>Ending Cash</span><strong>{toCurrency(p.endingBalance)}</strong></p>
                            <p><span>Ending Debt</span><strong>{toCurrency(p.endingDebt)}</strong></p>
                            <p><span>Total Paid</span><strong>{toCurrency(p.totalPaid)}</strong></p>
                            <p><span>Interest Cost</span><strong>{toCurrency(p.totalInterest)}</strong></p>
                        </div>
                    ))}
                </div>
            </UICard>

            <UICard className="whatif-card">
                <h3>What-If Simulator</h3>
                <div className="whatif-controls">
                    <div className="tool-row">
                        <label>Projection Months</label>
                        <input
                            type="number"
                            min={1}
                            max={60}
                            value={scenarioMonths}
                            onChange={(e) => setScenarioMonths(Number(e.target.value || 1))}
                        />
                    </div>
                    <div className="tool-row">
                        <label>Scenario Annual Income ($)</label>
                        <input
                            type="number"
                            min={0}
                            step={1000}
                            value={scenarioIncome}
                            onChange={(e) => setScenarioIncome(Number(e.target.value || 0))}
                        />
                    </div>
                    <div className="tool-row">
                        <label>Plan Type</label>
                        <select value={scenarioPlanType} onChange={(e) => setScenarioPlanType(e.target.value as 'standard' | 'idr')}>
                            <option value="standard">Standard</option>
                            <option value="idr">IDR</option>
                        </select>
                    </div>
                    <div className="tool-row">
                        <label>Monthly Expense Delta ($)</label>
                        <input
                            type="number"
                            step={50}
                            value={scenarioExpenseDelta}
                            onChange={(e) => setScenarioExpenseDelta(Number(e.target.value || 0))}
                        />
                    </div>
                    <div className="tool-row">
                        <label>Extra Monthly Payment ($)</label>
                        <input
                            type="number"
                            min={0}
                            step={25}
                            value={scenarioExtraPayment}
                            onChange={(e) => setScenarioExtraPayment(Number(e.target.value || 0))}
                        />
                    </div>
                </div>
                <div className="scenario-result">
                    <p><span>Projected Payment / Month</span><strong>{toCurrency(scenarioProjection.projectedMonthlyPayment)}</strong></p>
                    <p><span>Ending Cash</span><strong>{toCurrency(scenarioProjection.endingBalance)}</strong></p>
                    <p><span>Ending Debt</span><strong>{toCurrency(scenarioProjection.endingDebt)}</strong></p>
                    <p><span>Total Interest</span><strong>{toCurrency(scenarioProjection.totalInterest)}</strong></p>
                </div>
            </UICard>

            <UICard className="strategy-card">
                <h3>Repayment Strategy Optimizer</h3>
                <div className="strategy-grid">
                    <div className="strategy-tile">
                        <h4>Avalanche (Highest APR First)</h4>
                        <p><span>Debt-Free ETA</span><strong>{avalanche.payoffMonths} months</strong></p>
                        <p><span>Total Interest</span><strong>{toCurrency(avalanche.interestPaid)}</strong></p>
                    </div>
                    <div className="strategy-tile">
                        <h4>Snowball (Smallest Balance First)</h4>
                        <p><span>Debt-Free ETA</span><strong>{snowball.payoffMonths} months</strong></p>
                        <p><span>Total Interest</span><strong>{toCurrency(snowball.interestPaid)}</strong></p>
                    </div>
                </div>
                <p className="muted">
                    Recommendation: <strong>{avalanche.interestPaid <= snowball.interestPaid ? 'Avalanche' : 'Snowball'}</strong>
                    {' '}saves about {toCurrency(Math.abs(snowball.interestPaid - avalanche.interestPaid))} in projected interest.
                </p>
            </UICard>

            <UICard className="goals-card">
                <h3>Goals & Milestones</h3>
                <div className="goals-controls">
                    <div className="tool-row">
                        <label>Emergency Fund Goal ($)</label>
                        <input
                            type="number"
                            min={0}
                            step={250}
                            value={goals.emergencyFundTarget}
                            onChange={(e) => setGoals((prev) => ({ ...prev, emergencyFundTarget: Number(e.target.value || 0) }))}
                        />
                    </div>
                    <div className="tool-row">
                        <label>Debt Reduction Goal (%)</label>
                        <input
                            type="number"
                            min={0}
                            max={100}
                            step={5}
                            value={goals.debtReductionTarget * 100}
                            onChange={(e) => setGoals((prev) => ({ ...prev, debtReductionTarget: Number(e.target.value || 0) / 100 }))}
                        />
                    </div>
                </div>
                <div className="goal-progress-list">
                    <div>
                        <span>Emergency Fund Progress</span>
                        <progress max={1} value={emergencyFundProgress} />
                        <small>{(emergencyFundProgress * 100).toFixed(1)}% ({toCurrency(snapshot.balance)} / {toCurrency(goals.emergencyFundTarget)})</small>
                    </div>
                    <div>
                        <span>Debt Reduction Target</span>
                        <progress max={1} value={debtReductionProgress} />
                        <small>{(debtReductionProgress * 100).toFixed(1)}% target configured</small>
                    </div>
                </div>
            </UICard>

            <UICard className="activity-card">
                <div className="activity-header-row">
                    <h3>Finance Activity Ledger</h3>
                    <UIButton
                        variant="secondary"
                        disabled={activityLog.length === 0}
                        onClick={() => setActivityLog([])}
                    >
                        Clear Log
                    </UIButton>
                </div>
                {activityLog.length === 0 ? (
                    <p className="muted">No finance actions logged yet.</p>
                ) : (
                    <ul className="activity-list">
                        {activityLog.map((item) => (
                            <li key={item.id}>
                                <div>
                                    <strong>{item.action}</strong>
                                    <p>{item.details}</p>
                                </div>
                                <time>{new Date(item.at).toLocaleString()}</time>
                            </li>
                        ))}
                    </ul>
                )}
            </UICard>

            <UICard className="loan-table-card">
                <h3>Active Loans</h3>
                {snapshot.loans.length === 0 ? (
                    <p className="muted">No loans yet.</p>
                ) : (
                    <div className="loan-table-wrap">
                        <table className="loan-table">
                            <thead>
                                <tr>
                                    <th>Type</th>
                                    <th>Principal</th>
                                    <th>Accrued</th>
                                    <th>APR</th>
                                    <th>Phase</th>
                                    <th>Grace</th>
                                    <th>Min Payment</th>
                                </tr>
                            </thead>
                            <tbody>
                                {snapshot.loans.map((loan) => (
                                    <tr key={loan.id}>
                                        <td>{loan.loan_type}</td>
                                        <td>{toCurrency(Number(loan.principal || 0))}</td>
                                        <td>{toCurrency(Number(loan.accrued_interest || 0))}</td>
                                        <td>{(Number(loan.annual_interest_rate || 0) * 100).toFixed(2)}%</td>
                                        <td>{loan.in_school ? 'In School' : 'Repayment'}</td>
                                        <td>{loan.grace_months_remaining}</td>
                                        <td>{toCurrency(Number(loan.minimum_payment || 0))}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                )}
            </UICard>
        </section>
    )
}
