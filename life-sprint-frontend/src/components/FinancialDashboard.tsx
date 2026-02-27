import '../styles/FinancialDashboard.css'

export interface FinancialData {
    cash: number
    savings: number
    investments: number
    loans: number
    netWorth: number
    salary?: number
}

export interface FinancialDashboardProps {
    data: FinancialData
    income?: number
    expenses?: number
}

export function FinancialDashboard({ data, income = 0, expenses = 0 }: FinancialDashboardProps) {
    const formatMoney = (amount: number) => {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 0,
            maximumFractionDigits: 0
        }).format(amount)
    }

    const getAssetColor = (value: number) => {
        return value > 0 ? '#7ED321' : value < 0 ? '#FF6B6B' : '#999'
    }

    const FinancialItem = ({ label, amount, icon }: { label: string; amount: number; icon: string }) => (
        <div className="financial-item">
            <span className="item-icon">{icon}</span>
            <span className="item-label">{label}</span>
            <span className="item-amount" style={{ color: getAssetColor(amount) }}>
                {formatMoney(amount)}
            </span>
        </div>
    )

    return (
        <div className="financial-dashboard">
            <div className="dashboard-header">
                <h3>💰 Financial Overview</h3>
                <div className="net-worth-display">
                    <span className="label">Net Worth</span>
                    <span className="value" style={{ color: getAssetColor(data.netWorth) }}>
                        {formatMoney(data.netWorth)}
                    </span>
                </div>
            </div>

            <div className="financial-grid">
                <div className="grid-section assets">
                    <h4>Assets</h4>
                    <FinancialItem label="Cash" amount={data.cash} icon="💵" />
                    <FinancialItem label="Savings" amount={data.savings} icon="🏦" />
                    <FinancialItem label="Investments" amount={data.investments} icon="📈" />
                </div>

                <div className="grid-section liabilities">
                    <h4>Liabilities</h4>
                    <FinancialItem label="Loans" amount={-data.loans} icon="📊" />
                </div>

                <div className="grid-section income-expenses">
                    <h4>Cash Flow</h4>
                    {data.salary && <FinancialItem label="Salary" amount={data.salary} icon="💼" />}
                    {income > 0 && <FinancialItem label="Monthly Income" amount={income} icon="📥" />}
                    {expenses > 0 && <FinancialItem label="Monthly Expenses" amount={-expenses} icon="📤" />}
                    {(income > 0 || expenses > 0) && (
                        <FinancialItem
                            label="Monthly Balance"
                            amount={income - expenses}
                            icon={income - expenses > 0 ? '📈' : '📉'}
                        />
                    )}
                </div>
            </div>

            <div className="financial-breakdown">
                <div className="breakdown-item">
                    <span>Assets:</span>
                    <span>{formatMoney(data.cash + data.savings + data.investments)}</span>
                </div>
                <div className="breakdown-item">
                    <span>Liabilities:</span>
                    <span>{formatMoney(data.loans)}</span>
                </div>
            </div>
        </div>
    )
}
