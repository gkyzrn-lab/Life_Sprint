from finance.dtos import (
    BorrowForSemesterRequest,
    BorrowForSemesterResponse,
    SetRepaymentProfileRequest,
    RepayMonthsRequest,
    RepayMonthsResponse,
)
from finance.loan_products import LOAN_PRODUCTS
from finance.calculators import amortized_payment, compute_idr_monthly_payment
from finance.service import (
    borrow_for_semester,
    set_repayment_profile,
    repay_months,
    transition_loans_to_repayment,
    accrue_interest_in_school,
)
