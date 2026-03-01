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

    const refreshFromServer = async () => {
        const fresh = await getPlayer(player.id)
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
    }

    const runAction = async (fn: () => Promise<void>) => {
        try {
            setWorking(true)
            setError(null)
            setMessage(null)
            await fn()
            await refreshFromServer()
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
                    <p>${snapshot.balance.toFixed(2)}</p>
                </UICard>
                <UICard className="finance-summary-card">
                    <label>Monthly Expenses</label>
                    <p>${snapshot.monthlyExpenses.toFixed(2)}</p>
                </UICard>
                <UICard className="finance-summary-card">
                    <label>Semester Tuition</label>
                    <p>${snapshot.tuitionPerSemester.toFixed(2)}</p>
                </UICard>
                <UICard className="finance-summary-card">
                    <label>Scholarship</label>
                    <p>${snapshot.scholarshipPerSemester.toFixed(2)}</p>
                </UICard>
            </div>

            <div className="finance-debt-summary">
                <UICard className="finance-debt-card">
                    <h3>Loan Portfolio</h3>
                    <div className="debt-metrics">
                        <div><span>Principal</span><strong>${totals.principal.toFixed(2)}</strong></div>
                        <div><span>Accrued Interest</span><strong>${totals.accrued.toFixed(2)}</strong></div>
                        <div><span>Total Debt</span><strong>${totals.totalDebt.toFixed(2)}</strong></div>
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
                        })}
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
                        })}
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
                        })}
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
                            })}
                        >
                            {working ? 'Working...' : 'Start Repayment'}
                        </UIButton>
                        <UIButton
                            disabled={working}
                            onClick={() => runAction(async () => {
                                const result = await financeRepayMonths(player.id, repayMonths)
                                setMessage(`Paid $${result.total_paid.toFixed(2)} over ${result.months} month(s).`)
                            })}
                        >
                            {working ? 'Working...' : 'Repay Months'}
                        </UIButton>
                    </div>
                </UICard>
            </div>

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
                                        <td>${Number(loan.principal || 0).toFixed(2)}</td>
                                        <td>${Number(loan.accrued_interest || 0).toFixed(2)}</td>
                                        <td>{(Number(loan.annual_interest_rate || 0) * 100).toFixed(2)}%</td>
                                        <td>{loan.in_school ? 'In School' : 'Repayment'}</td>
                                        <td>{loan.grace_months_remaining}</td>
                                        <td>${Number(loan.minimum_payment || 0).toFixed(2)}</td>
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
