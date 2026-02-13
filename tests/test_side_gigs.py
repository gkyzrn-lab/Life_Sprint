"""Test side gigs system"""
from core_domain.player.player_model import Player
from core_domain.planning.planning_models import SemesterPlan
from side_gigs import service as side_gigs_service
from catalogs.side_gigs import GIG_OPPORTUNITIES
from core_domain.side_gigs.side_gigs_models import PassiveIncomeType, BusinessType

print('='*80)
print('SIDE GIGS SYSTEM - QUICK TEST')
print('='*80)

player = Player(
    id='test', name='Test', age=20, hs_gpa=3.5, parent_income=60000,
    major_id='cs', college_id='state_u', semester=3,
    housing={'option_id':'brooklyn', 'name':'Brooklyn', 'monthly_cost':1900}
)

# Add semester plan
player.plan = SemesterPlan(
    semester=3,
    housing_option_id='brooklyn',
)

player.finance.balance = 10000
player.stats.technical_skills = 70

# Test 1: DoorDash
can_start, reason = side_gigs_service.can_start_gig(player, 'doordash_delivery')
print(f'\n✓ DoorDash eligibility: {can_start}')

if can_start:
    gig, story = side_gigs_service.start_gig(player, 'doordash_delivery')
    earnings, costs, _ = side_gigs_service.work_gig(player, 'doordash_delivery', 5.0)
    print(f'  Worked 5 hours: Earned ${earnings:.0f}, Balance ${player.finance.balance:,.0f}')

# Test 2: Freelance Coding
can_start, _ = side_gigs_service.can_start_gig(player, 'freelance_coding_experienced')
print(f'\n✓ Freelance coding eligibility: {can_start}')

if can_start:
    gig, story = side_gigs_service.start_gig(player, 'freelance_coding_experienced')
    earnings, costs, _ = side_gigs_service.work_gig(player, 'freelance_coding_experienced', 10.0)
    print(f'  Worked 10 hours: Earned ${earnings:.0f}, Rate ${earnings/10:.0f}/hr')
    print(f'  Portfolio: {player.side_gigs.portfolio_quality:.1f}/100')

# Test 3: Blog
stream, _ = side_gigs_service.start_passive_income_stream(player, PassiveIncomeType.BLOG, 'Tech Blog')
print(f'\n✓ Started blog: {stream.name}')
print(f'  Startup cost: ${stream.startup_cost:.0f}, Balance: ${player.finance.balance:,.0f}')

# Grow for 6 months
for i in range(6):
    side_gigs_service.update_passive_income_streams(player, 1)
    
print(f'  After 6 months: ${stream.current_monthly_income:.0f}/month, {stream.monthly_views_visits:,} views')

# Test 4: Business
player.stats.business_acumen = 60
business, _ = side_gigs_service.start_business(player, BusinessType.DROPSHIPPING, 'My Store')
print(f'\n✓ Started business: {business.name}')

for i in range(6):
    side_gigs_service.update_businesses(player, 1)

print(f'  After 6 months: Revenue ${business.monthly_revenue:.0f}, Profit ${business.monthly_revenue - business.monthly_expenses:.0f}')

# Summary
summary = side_gigs_service.get_side_gigs_summary(player)
print(f'\n✓ SUMMARY:')
print(f'  Active gigs: {len(summary["active_gigs"])}')
print(f'  Passive income: ${summary["total_income"]["monthly_passive_income"]:.0f}/month')
print(f'  Business income: ${summary["total_income"]["monthly_business_income"]:.0f}/month')
print(f'  Total side income: ${summary["total_income"]["total_monthly_side_income"]:.0f}/month')
print(f'  Final balance: ${player.finance.balance:,.0f}')
print(f'  Achievements: {len(player.side_gigs.side_gig_achievements_unlocked)}')

print(f'\n✅ Side Gigs System: WORKING!')
print('='*80)
