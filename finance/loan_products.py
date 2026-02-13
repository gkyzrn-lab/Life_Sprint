# Loan products (simple v1).
# You can later customize by college type, credit score, etc.

LOAN_PRODUCTS = {
    "subsidized": {
        "annual_interest_rate": 0.045,
        "max_per_semester": 2750.0,
        "grace_months": 6,
        "repayment_months": 120,
    },
    "unsubsidized": {
        "annual_interest_rate": 0.055,
        "max_per_semester": 5500.0,
        "grace_months": 6,
        "repayment_months": 120,
    },
    "private": {
        "annual_interest_rate": 0.085,
        "max_per_semester": 20000.0,
        "grace_months": 0,
        "repayment_months": 120,
    },
}
