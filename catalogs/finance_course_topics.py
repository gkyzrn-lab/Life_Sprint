"""
Enhanced Finance/Accounting Course Topics.
Provides detailed topic descriptions for finance and accounting course IDs.
"""

from typing import Dict, Any

FINANCE_ACCOUNTING_TOPICS: Dict[str, Dict[str, Any]] = {
    "fin101": {
        "title": "Intro to Finance",
        "description": "Core financial concepts for personal and corporate decision-making.",
        "key_topics": [
            {
                "name": "Time Value of Money",
                "description": "Present value, future value, and discounting cash flows.",
                "real_world": "Why is $1,000 today worth more than $1,000 five years from now?"
            },
            {
                "name": "Risk and Return",
                "description": "Understanding risk premiums and expected return tradeoffs.",
                "real_world": "Why do investors demand higher returns from volatile assets?"
            },
            {
                "name": "Interest Rates",
                "description": "Nominal vs real rates and the role of inflation.",
                "real_world": "How do rising rates impact borrowing for students and businesses?"
            },
            {
                "name": "Financial Markets",
                "description": "Primary vs secondary markets, stocks, bonds, and intermediaries.",
                "real_world": "How do companies raise money through debt and equity markets?"
            },
            {
                "name": "Basic Valuation",
                "description": "Valuing cash-flow streams and simple securities.",
                "real_world": "How do analysts estimate what a stock is worth?"
            },
        ],
    },
    "fin201": {
        "title": "Financial Markets",
        "description": "Market structure, instruments, and pricing behavior in modern capital markets.",
        "key_topics": [
            {
                "name": "Market Microstructure",
                "description": "Order books, liquidity, spreads, and trade execution.",
                "real_world": "Why can two investors get different prices seconds apart?"
            },
            {
                "name": "Bond Markets",
                "description": "Yield, duration, and credit risk across debt instruments.",
                "real_world": "How does a credit downgrade increase borrowing costs?"
            },
            {
                "name": "Equity Markets",
                "description": "Market capitalization, indices, and sector behavior.",
                "real_world": "Why do tech indices move differently than utilities?"
            },
            {
                "name": "Derivatives Basics",
                "description": "Forwards, futures, options, and hedging concepts.",
                "real_world": "How can airlines hedge fuel-price risk using derivatives?"
            },
            {
                "name": "Regulation and Stability",
                "description": "Roles of regulators and systemic-risk controls.",
                "real_world": "How do circuit breakers reduce panic selling?"
            },
        ],
    },
    "acc101": {
        "title": "Principles of Accounting I",
        "description": "Foundational accounting systems and financial statement preparation.",
        "key_topics": [
            {
                "name": "Accounting Equation",
                "description": "Assets = Liabilities + Equity as the base model.",
                "real_world": "How does a startup investment affect both cash and equity?"
            },
            {
                "name": "Debits and Credits",
                "description": "Double-entry logic and account normal balances.",
                "real_world": "Why does cash increase with a debit while revenue increases with a credit?"
            },
            {
                "name": "Adjusting Entries",
                "description": "Accruals, deferrals, and period-end adjustments.",
                "real_world": "How are prepaid subscriptions recognized month by month?"
            },
            {
                "name": "Trial Balance",
                "description": "Checking ledger integrity before preparing statements.",
                "real_world": "How do accountants detect posting mistakes quickly?"
            },
            {
                "name": "Financial Statement Flow",
                "description": "Connecting income statement, balance sheet, and cash flow.",
                "real_world": "How can profitable firms still show weak operating cash flow?"
            },
        ],
    },
    "acc301": {
        "title": "Intermediate Accounting I",
        "description": "Advanced reporting standards and asset recognition/measurement.",
        "key_topics": [
            {
                "name": "Revenue Recognition",
                "description": "Performance obligations and timing under GAAP/IFRS.",
                "real_world": "When should a SaaS company recognize annual contract revenue?"
            },
            {
                "name": "Inventory Accounting",
                "description": "FIFO/LIFO/weighted-average effects on statements.",
                "real_world": "How does inflation change gross margin under different methods?"
            },
            {
                "name": "Long-Lived Assets",
                "description": "Depreciation, impairment, and asset disposal.",
                "real_world": "How does impairment alter earnings quality signals?"
            },
            {
                "name": "Earnings Quality",
                "description": "Distinguishing recurring operations from one-off items.",
                "real_world": "Why do analysts adjust EBITDA and normalized earnings?"
            },
            {
                "name": "Disclosure and Notes",
                "description": "Footnotes, contingencies, and risk communication.",
                "real_world": "How do note disclosures reveal hidden liabilities?"
            },
        ],
    },
}


def get_finance_accounting_topics(course_id: str) -> Dict[str, Any]:
    """Get detailed topics for finance/accounting course."""
    return FINANCE_ACCOUNTING_TOPICS.get(course_id, {})


def _topic_icon(topic_name: str) -> str:
    """Topic icon for finance/accounting themes."""
    icon_map = {
        "time value": "⏳",
        "risk": "⚠️",
        "return": "📈",
        "interest": "💹",
        "market": "🏦",
        "valuation": "💎",
        "bond": "🧾",
        "equity": "📊",
        "derivatives": "🧮",
        "regulation": "⚖️",
        "accounting": "📘",
        "debits": "📝",
        "credits": "🧮",
        "adjusting": "🔧",
        "trial balance": "✅",
        "statement": "📋",
        "revenue": "💵",
        "inventory": "📦",
        "assets": "🏢",
        "earnings": "🎯",
        "disclosure": "🔍",
    }
    name = topic_name.lower()
    for key, icon in icon_map.items():
        if key in name:
            return icon
    return "💼"


def format_finance_accounting_topics(course_id: str) -> Dict[str, Any]:
    """Format finance/accounting topics for frontend display."""
    course_data = get_finance_accounting_topics(course_id)
    if not course_data:
        return {
            "course_id": course_id,
            "found": False,
            "message": f"Topics not yet available for {course_id}",
        }

    return {
        "course_id": course_id,
        "title": course_data.get("title", ""),
        "description": course_data.get("description", ""),
        "found": True,
        "topics": [
            {
                "name": topic["name"],
                "description": topic["description"],
                "real_world": topic["real_world"],
                "icon": _topic_icon(topic["name"]),
            }
            for topic in course_data.get("key_topics", [])
        ],
        "learning_outcomes": [
            f"Analyze: {topic['name']}" if i % 2 == 0 else f"Apply: {topic['description']}"
            for i, topic in enumerate(course_data.get("key_topics", []))
        ][:5],
    }
