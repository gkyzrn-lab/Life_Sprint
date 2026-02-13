"""
Example: Comparing Premium Cards with Annual Fees vs No-Fee Basic Cards
"""

from catalogs.credit_cards import (
    get_card,
    estimate_annual_cost_benefit,
    compare_cards
)

print("=" * 70)
print("CREDIT CARD COMPARISON: Annual Fees vs No-Fee Cards")
print("=" * 70)

# Get cards
premium = get_card("premium_rewards_platinum")
standard = get_card("standard_student_visa")

print("\n📊 CARD 1: Premium Card (with annual fee)")
print(f"   {premium['bank_name']} {premium['card_name']}")
print(f"   Annual Fee: ${premium['annual_fee']} (waived first year)")
print(f"   APR: {premium['apr']}%")
print(f"   Cashback: {premium['perks']['cashback_rate'] * 100}%")
print(f"   Perks: $25/month gym, $10/month streaming")

print("\n📊 CARD 2: Standard Card (no annual fee)")
print(f"   {standard['bank_name']} {standard['card_name']}")
print(f"   Annual Fee: ${standard['annual_fee']}")
print(f"   APR: {standard['apr']}%")
print(f"   Cashback: {standard['perks']['cashback_rate'] * 100}%")
print(f"   Perks: Spotify Premium ($10/month)")

print("\n" + "=" * 70)
print("SCENARIO 1: Light Spender - $300/month")
print("=" * 70)

premium_low = estimate_annual_cost_benefit(premium, 300)
standard_low = estimate_annual_cost_benefit(standard, 300)

print("\n💳 Premium Card:")
print(f"   Cashback earned: ${premium_low['cashback_earned']}")
print(f"   Perks value: ${premium_low['perks_annual_value']}")
print(f"   Signup bonus: ${premium_low['signup_bonus']}")
print(f"   Annual fee: ${premium_low['annual_fee']}")
print(f"   ✅ First year net: ${premium_low['first_year_net_benefit']}")
print(f"   📅 Ongoing years: ${premium_low['ongoing_annual_benefit']}")

print("\n💳 Standard Card (No Fee):")
print(f"   Cashback earned: ${standard_low['cashback_earned']}")
print(f"   Perks value: ${standard_low['perks_annual_value']}")
print(f"   Signup bonus: ${standard_low['signup_bonus']}")
print(f"   Annual fee: ${standard_low['annual_fee']}")
print(f"   ✅ First year net: ${standard_low['first_year_net_benefit']}")
print(f"   📅 Ongoing years: ${standard_low['ongoing_annual_benefit']}")

print("\n🏆 VERDICT: ", end="")
if premium_low['ongoing_annual_benefit'] > standard_low['ongoing_annual_benefit']:
    diff = premium_low['ongoing_annual_benefit'] - standard_low['ongoing_annual_benefit']
    print(f"Premium wins by ${diff:.2f}/year (if you use the gym!)")
else:
    diff = standard_low['ongoing_annual_benefit'] - premium_low['ongoing_annual_benefit']
    print(f"No-fee card wins by ${diff:.2f}/year")

print("\n" + "=" * 70)
print("SCENARIO 2: Heavy Spender - $800/month")
print("=" * 70)

premium_high = estimate_annual_cost_benefit(premium, 800)
standard_high = estimate_annual_cost_benefit(standard, 800)

print("\n💳 Premium Card:")
print(f"   Cashback earned: ${premium_high['cashback_earned']}")
print(f"   Perks value: ${premium_high['perks_annual_value']}")
print(f"   Signup bonus: ${premium_high['signup_bonus']}")
print(f"   Annual fee: ${premium_high['annual_fee']}")
print(f"   ✅ First year net: ${premium_high['first_year_net_benefit']}")
print(f"   📅 Ongoing years: ${premium_high['ongoing_annual_benefit']}")

print("\n💳 Standard Card (No Fee):")
print(f"   Cashback earned: ${standard_high['cashback_earned']}")
print(f"   Perks value: ${standard_high['perks_annual_value']}")
print(f"   Signup bonus: ${standard_high['signup_bonus']}")
print(f"   Annual fee: ${standard_high['annual_fee']}")
print(f"   ✅ First year net: ${standard_high['first_year_net_benefit']}")
print(f"   📅 Ongoing years: ${standard_high['ongoing_annual_benefit']}")

print("\n🏆 VERDICT: ", end="")
if premium_high['ongoing_annual_benefit'] > standard_high['ongoing_annual_benefit']:
    diff = premium_high['ongoing_annual_benefit'] - standard_high['ongoing_annual_benefit']
    print(f"Premium wins by ${diff:.2f}/year (higher spending pays off!)")
else:
    diff = standard_high['ongoing_annual_benefit'] - premium_high['ongoing_annual_benefit']
    print(f"No-fee card wins by ${diff:.2f}/year")

print("\n" + "=" * 70)
print("KEY LESSONS:")
print("=" * 70)
print("1. Annual fees require you to USE the perks to justify the cost")
print("2. Light spenders often do better with no-fee cards")
print("3. Heavy spenders benefit from premium cards with higher cashback")
print("4. Students on tight budgets: Start with $0 annual fee!")
print("5. First year is often best (fee waived + signup bonus)")
print("6. Break-even for premium card:", end=" ")
if premium_high['break_even_spending']:
    print(f"${premium_high['break_even_spending']:.2f}/year spending")
print("\n")
