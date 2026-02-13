# app/core/config.py

# ===== Time constants =====
WEEKLY_TIME_BUDGET = 60
SEM_MONTHS = 4                 # months per semester (finance + interest)
WEEKS_PER_SEMESTER = 16        # time budget framing (UI / future logic)

# ===== Game rules =====
MAX_STRESS = 100.0
MAX_HAPPINESS = 100.0
MAX_BURNOUT = 100.0

# ===== Limits =====
MAX_REQUEST_MONTHS_REPAY = 240  # guardrail for repayment simulation endpoint
MAX_EXAM_QUESTIONS = 10         # guardrail

# ===== Defaults =====
DEFAULT_START_AGE = 18
DEFAULT_START_BALANCE = 1000.0
DEFAULT_BASE_MONTHLY_NONHOUSING_EXPENSES = 350.0
