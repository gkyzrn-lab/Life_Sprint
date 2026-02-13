"""
Side Gigs & Freelancing Catalog

DESIGN PHILOSOPHY:
This catalog represents MODERN REALITY for Gen Z workers:
- Traditional jobs aren't the only option
- Gig economy provides flexibility (but income varies)
- Passive income takes TIME (months/years to pay off)
- Entrepreneurship is RISKY (80% of businesses fail in first 5 years)
- Skills = money (coding/design can earn $50-100/hour)
- Multiple income streams = financial security

Teaching moments:
1. DoorDash seems easy but costs gas + wear on car
2. Freelancing requires building portfolio first (low pay initially)
3. YouTube/blogging take 6-12 months before earning meaningful $
4. Starting a business requires capital (often $5k-50k+)
5. Time management is critical (burnout from overwork is real)
6. Diversification matters (don't rely on one income source)
"""

from core_domain.side_gigs.side_gigs_models import (
    GigOpportunity,
    GigType,
    PassiveIncomeType,
    BusinessType,
)

# =============================================================================
# GIG ECONOMY OPPORTUNITIES
# =============================================================================

GIG_OPPORTUNITIES = {
    # DELIVERY GIGS (Low barrier, flexible, wear on car)
    "doordash_delivery": GigOpportunity(
        gig_id="doordash_delivery",
        gig_type=GigType.DELIVERY,
        name="DoorDash Delivery",
        description="Deliver food from restaurants to customers. Use your car or bike.",
        min_age=18,
        requires_car=True,
        requires_smartphone=True,
        skill_requirements={},
        min_hourly_rate=12.0,  # Slow day
        avg_hourly_rate=18.0,  # Average with tips
        max_hourly_rate=28.0,  # Peak hours (dinner rush)
        flexible_hours=True,
        min_hours_per_week=0,
        max_hours_per_week=40,
        startup_cost=0.0,  # Just need car + phone
        ongoing_costs_per_month=150.0,  # Gas, car maintenance
        stress_per_hour=3.0,  # Moderate stress (traffic, time pressure)
        energy_per_hour=5.0,
        skill_improvement_per_hour={
            "time_management": 0.1,
            "navigation": 0.1,
        },
        portfolio_boost=False,
    ),
    
    "instacart_shopper": GigOpportunity(
        gig_id="instacart_shopper",
        gig_type=GigType.DELIVERY,
        name="Instacart Shopper",
        description="Shop for groceries and deliver to customers.",
        min_age=18,
        requires_car=True,
        requires_smartphone=True,
        skill_requirements={},
        min_hourly_rate=14.0,
        avg_hourly_rate=20.0,
        max_hourly_rate=30.0,  # Big orders, good tips
        flexible_hours=True,
        min_hours_per_week=0,
        max_hours_per_week=40,
        startup_cost=0.0,
        ongoing_costs_per_month=150.0,  # Gas, car maintenance
        stress_per_hour=4.0,  # Higher stress (finding items, heavy lifting)
        energy_per_hour=6.0,  # Physical work
        skill_improvement_per_hour={
            "time_management": 0.1,
            "organization": 0.1,
        },
        portfolio_boost=False,
    ),
    
    # RIDESHARE (Higher income, but car wear)
    "uber_driver": GigOpportunity(
        gig_id="uber_driver",
        gig_type=GigType.RIDESHARE,
        name="Uber Driver",
        description="Drive passengers to their destinations.",
        min_age=21,  # Most cities require 21+
        requires_car=True,
        requires_smartphone=True,
        skill_requirements={},
        min_hourly_rate=15.0,
        avg_hourly_rate=22.0,
        max_hourly_rate=35.0,  # Surge pricing
        flexible_hours=True,
        min_hours_per_week=0,
        max_hours_per_week=40,
        startup_cost=0.0,
        ongoing_costs_per_month=200.0,  # Gas, car maintenance, cleaning
        stress_per_hour=4.0,  # Dealing with passengers, traffic
        energy_per_hour=5.0,
        skill_improvement_per_hour={
            "communication": 0.1,
            "navigation": 0.1,
        },
        portfolio_boost=False,
    ),
    
    # TUTORING (Higher rate, requires expertise)
    "online_tutoring": GigOpportunity(
        gig_id="online_tutoring",
        gig_type=GigType.TUTORING,
        name="Online Tutoring",
        description="Tutor students in subjects you're strong in (math, science, English).",
        min_age=18,
        requires_car=False,
        requires_smartphone=True,
        skill_requirements={
            "academic_performance": 75,  # Need good GPA
        },
        min_hourly_rate=20.0,  # Elementary level
        avg_hourly_rate=30.0,  # High school level
        max_hourly_rate=50.0,  # SAT/ACT prep, college level
        flexible_hours=True,
        min_hours_per_week=0,
        max_hours_per_week=20,  # Hard to fill more hours
        startup_cost=0.0,
        ongoing_costs_per_month=0.0,
        stress_per_hour=3.0,
        energy_per_hour=4.0,  # Mentally draining
        skill_improvement_per_hour={
            "teaching": 0.2,
            "communication": 0.1,
            "subject_knowledge": 0.1,
        },
        portfolio_boost=True,  # Build reputation
    ),
    
    # FREELANCE WRITING (Low barrier, but low pay initially)
    "freelance_writing_beginner": GigOpportunity(
        gig_id="freelance_writing_beginner",
        gig_type=GigType.FREELANCE_WRITING,
        name="Freelance Writing (Beginner)",
        description="Write blog posts, articles, and web content for clients.",
        min_age=18,
        requires_car=False,
        requires_smartphone=True,
        skill_requirements={
            "writing": 40,
        },
        min_hourly_rate=15.0,  # Low-paying content mills
        avg_hourly_rate=25.0,
        max_hourly_rate=40.0,
        flexible_hours=True,
        min_hours_per_week=0,
        max_hours_per_week=30,
        startup_cost=0.0,
        ongoing_costs_per_month=0.0,
        stress_per_hour=2.0,
        energy_per_hour=4.0,
        skill_improvement_per_hour={
            "writing": 0.3,
            "research": 0.1,
            "time_management": 0.1,
        },
        portfolio_boost=True,
    ),
    
    "freelance_writing_experienced": GigOpportunity(
        gig_id="freelance_writing_experienced",
        gig_type=GigType.FREELANCE_WRITING,
        name="Freelance Writing (Experienced)",
        description="Write for premium clients (tech companies, magazines).",
        min_age=18,
        requires_car=False,
        requires_smartphone=True,
        skill_requirements={
            "writing": 70,
            "portfolio_quality": 60,
        },
        min_hourly_rate=40.0,
        avg_hourly_rate=60.0,
        max_hourly_rate=100.0,  # Premium tech/finance writing
        flexible_hours=True,
        min_hours_per_week=0,
        max_hours_per_week=30,
        startup_cost=0.0,
        ongoing_costs_per_month=0.0,
        stress_per_hour=3.0,
        energy_per_hour=5.0,
        skill_improvement_per_hour={
            "writing": 0.2,
            "expertise": 0.2,
        },
        portfolio_boost=True,
    ),
    
    # FREELANCE DESIGN (Requires skills, but high pay)
    "freelance_design_beginner": GigOpportunity(
        gig_id="freelance_design_beginner",
        gig_type=GigType.FREELANCE_DESIGN,
        name="Freelance Design (Beginner)",
        description="Create logos, social media graphics, basic web design.",
        min_age=18,
        requires_car=False,
        requires_smartphone=True,
        skill_requirements={
            "design": 50,
        },
        min_hourly_rate=20.0,
        avg_hourly_rate=35.0,
        max_hourly_rate=60.0,
        flexible_hours=True,
        min_hours_per_week=0,
        max_hours_per_week=30,
        startup_cost=50.0,  # Adobe Creative Cloud subscription
        ongoing_costs_per_month=55.0,  # Software
        stress_per_hour=3.0,
        energy_per_hour=5.0,
        skill_improvement_per_hour={
            "design": 0.3,
            "creativity": 0.2,
        },
        portfolio_boost=True,
    ),
    
    "freelance_design_experienced": GigOpportunity(
        gig_id="freelance_design_experienced",
        gig_type=GigType.FREELANCE_DESIGN,
        name="Freelance Design (Experienced)",
        description="Full branding packages, UX/UI design, advanced web design.",
        min_age=18,
        requires_car=False,
        requires_smartphone=True,
        skill_requirements={
            "design": 75,
            "portfolio_quality": 70,
        },
        min_hourly_rate=50.0,
        avg_hourly_rate=75.0,
        max_hourly_rate=125.0,  # High-end branding projects
        flexible_hours=True,
        min_hours_per_week=0,
        max_hours_per_week=30,
        startup_cost=50.0,
        ongoing_costs_per_month=55.0,
        stress_per_hour=4.0,
        energy_per_hour=6.0,
        skill_improvement_per_hour={
            "design": 0.2,
            "business": 0.1,
        },
        portfolio_boost=True,
    ),
    
    # FREELANCE CODING (High skill requirement, highest pay)
    "freelance_coding_beginner": GigOpportunity(
        gig_id="freelance_coding_beginner",
        gig_type=GigType.FREELANCE_CODING,
        name="Freelance Coding (Beginner)",
        description="Build simple websites, WordPress sites, basic web apps.",
        min_age=18,
        requires_car=False,
        requires_smartphone=True,
        skill_requirements={
            "coding": 60,
        },
        min_hourly_rate=30.0,
        avg_hourly_rate=50.0,
        max_hourly_rate=80.0,
        flexible_hours=True,
        min_hours_per_week=0,
        max_hours_per_week=30,
        startup_cost=0.0,
        ongoing_costs_per_month=0.0,
        stress_per_hour=4.0,
        energy_per_hour=6.0,  # Mentally intensive
        skill_improvement_per_hour={
            "coding": 0.4,
            "problem_solving": 0.2,
        },
        portfolio_boost=True,
    ),
    
    "freelance_coding_experienced": GigOpportunity(
        gig_id="freelance_coding_experienced",
        gig_type=GigType.FREELANCE_CODING,
        name="Freelance Coding (Experienced)",
        description="Full-stack development, mobile apps, complex web applications.",
        min_age=18,
        requires_car=False,
        requires_smartphone=True,
        skill_requirements={
            "coding": 80,
            "portfolio_quality": 75,
        },
        min_hourly_rate=70.0,
        avg_hourly_rate=100.0,
        max_hourly_rate=150.0,  # Complex projects, consulting
        flexible_hours=True,
        min_hours_per_week=0,
        max_hours_per_week=30,
        startup_cost=0.0,
        ongoing_costs_per_month=0.0,
        stress_per_hour=5.0,
        energy_per_hour=7.0,
        skill_improvement_per_hour={
            "coding": 0.3,
            "architecture": 0.2,
        },
        portfolio_boost=True,
    ),
    
    # PHOTOGRAPHY (Equipment cost, but creative)
    "event_photography": GigOpportunity(
        gig_id="event_photography",
        gig_type=GigType.PHOTOGRAPHY,
        name="Event Photography",
        description="Shoot weddings, parties, corporate events.",
        min_age=18,
        requires_car=True,  # Need to transport equipment
        requires_smartphone=False,
        skill_requirements={
            "photography": 60,
        },
        min_hourly_rate=40.0,  # Small events
        avg_hourly_rate=75.0,
        max_hourly_rate=150.0,  # Weddings
        flexible_hours=True,
        min_hours_per_week=0,
        max_hours_per_week=20,  # Mostly weekends
        startup_cost=1500.0,  # Camera, lenses, lights
        ongoing_costs_per_month=50.0,  # Editing software, storage
        stress_per_hour=4.0,
        energy_per_hour=5.0,
        skill_improvement_per_hour={
            "photography": 0.3,
            "editing": 0.2,
        },
        portfolio_boost=True,
    ),
    
    # SOCIAL MEDIA MANAGEMENT (Modern skill, growing demand)
    "social_media_management": GigOpportunity(
        gig_id="social_media_management",
        gig_type=GigType.SOCIAL_MEDIA_MANAGEMENT,
        name="Social Media Management",
        description="Manage Instagram, TikTok, Facebook for small businesses.",
        min_age=18,
        requires_car=False,
        requires_smartphone=True,
        skill_requirements={
            "social_media": 60,
            "marketing": 40,
        },
        min_hourly_rate=25.0,
        avg_hourly_rate=40.0,
        max_hourly_rate=75.0,  # Multiple clients, high-value clients
        flexible_hours=True,
        min_hours_per_week=5,  # Need to post consistently
        max_hours_per_week=25,
        startup_cost=0.0,
        ongoing_costs_per_month=30.0,  # Scheduling tools (Buffer, Hootsuite)
        stress_per_hour=3.0,
        energy_per_hour=4.0,
        skill_improvement_per_hour={
            "social_media": 0.3,
            "marketing": 0.2,
            "communication": 0.1,
        },
        portfolio_boost=True,
    ),
    
    # VIRTUAL ASSISTANT (Low skill, steady income)
    "virtual_assistant": GigOpportunity(
        gig_id="virtual_assistant",
        gig_type=GigType.VIRTUAL_ASSISTANT,
        name="Virtual Assistant",
        description="Administrative tasks: email management, scheduling, data entry.",
        min_age=18,
        requires_car=False,
        requires_smartphone=True,
        skill_requirements={
            "organization": 50,
        },
        min_hourly_rate=18.0,
        avg_hourly_rate=25.0,
        max_hourly_rate=40.0,
        flexible_hours=True,
        min_hours_per_week=10,  # Clients want consistency
        max_hours_per_week=30,
        startup_cost=0.0,
        ongoing_costs_per_month=0.0,
        stress_per_hour=2.0,
        energy_per_hour=3.0,
        skill_improvement_per_hour={
            "organization": 0.1,
            "communication": 0.1,
        },
        portfolio_boost=False,
    ),
    
    # PET SITTING (Easy, fun, but limited income)
    "dog_walking": GigOpportunity(
        gig_id="dog_walking",
        gig_type=GigType.PET_SITTING,
        name="Dog Walking (Rover)",
        description="Walk dogs for busy owners.",
        min_age=18,
        requires_car=False,
        requires_smartphone=True,
        skill_requirements={},
        min_hourly_rate=15.0,
        avg_hourly_rate=20.0,
        max_hourly_rate=30.0,  # Multiple dogs
        flexible_hours=True,
        min_hours_per_week=0,
        max_hours_per_week=20,
        startup_cost=0.0,
        ongoing_costs_per_month=0.0,
        stress_per_hour=1.0,  # Low stress, fun
        energy_per_hour=4.0,  # Physical activity
        skill_improvement_per_hour={},
        portfolio_boost=False,
    ),
}


# =============================================================================
# PASSIVE INCOME OPPORTUNITIES (Long-term payoff)
# =============================================================================

PASSIVE_INCOME_OPTIONS = {
    "tech_blog": {
        "income_type": PassiveIncomeType.BLOG,
        "name": "Tech Blog",
        "description": "Write about technology, coding tutorials, gadget reviews. Monetize with ads and affiliate links.",
        "startup_cost": 150.0,  # Domain ($15/year) + hosting ($135/year)
        "initial_time_investment_hours": 100.0,  # Setup, first 10-15 posts
        "hours_per_month_required": 20.0,  # New posts, SEO
        "months_to_monetization": 6,  # Need traffic before earning $
        "income_timeline": {
            # Month: Monthly income
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 5,  # First few dollars from ads
            5: 12,
            6: 25,  # Monetization threshold reached
            9: 100,
            12: 250,  # After 1 year
            18: 600,
            24: 1200,  # After 2 years (if consistent)
            36: 2500,  # After 3 years (successful blog)
        },
        "success_rate": 0.15,  # Only 15% of blogs reach $1000/month
        "growth_rate": 1.12,  # 12% monthly growth (if consistent)
        "skills_required": {"writing": 50, "seo": 30},
        "skills_improved": {"writing": 0.5, "seo": 0.3, "marketing": 0.2},
    },
    
    "youtube_channel": {
        "income_type": PassiveIncomeType.YOUTUBE,
        "name": "YouTube Channel",
        "description": "Create videos (gaming, tutorials, vlogs). Monetize with ads and sponsorships.",
        "startup_cost": 800.0,  # Camera ($400), microphone ($150), lights ($150), editing software ($100)
        "initial_time_investment_hours": 150.0,  # Learn editing, first 10 videos
        "hours_per_month_required": 40.0,  # Film, edit, upload weekly
        "months_to_monetization": 8,  # Need 1000 subs + 4000 watch hours
        "income_timeline": {
            0: 0,
            3: 0,
            6: 0,
            8: 50,  # Hit monetization threshold
            12: 200,
            18: 600,
            24: 1500,  # After 2 years
            36: 4000,  # Successful channel after 3 years
        },
        "success_rate": 0.10,  # Only 10% reach monetization
        "growth_rate": 1.15,  # 15% monthly growth (if viral videos)
        "skills_required": {"video_editing": 40, "creativity": 50},
        "skills_improved": {"video_editing": 0.6, "creativity": 0.4, "presentation": 0.3},
    },
    
    "stock_dividends": {
        "income_type": PassiveIncomeType.STOCK_DIVIDENDS,
        "name": "Dividend Stocks",
        "description": "Invest in dividend-paying stocks (requires capital).",
        "startup_cost": 5000.0,  # Initial investment
        "initial_time_investment_hours": 20.0,  # Research stocks
        "hours_per_month_required": 2.0,  # Monitor portfolio
        "months_to_monetization": 0,  # Immediate (quarterly dividends)
        "income_timeline": {
            # Based on 4% annual dividend yield
            0: 17,  # $5000 * 4% / 12 months
            12: 17,  # Stable (unless reinvest)
            24: 17,
            36: 17,
        },
        "success_rate": 0.90,  # Reliable if you invest in stable companies
        "growth_rate": 1.01,  # 1% monthly (if reinvest dividends)
        "skills_required": {"finance": 40},
        "skills_improved": {"finance": 0.2, "investing": 0.3},
    },
    
    "etsy_shop_digital": {
        "income_type": PassiveIncomeType.ETSY_SHOP,
        "name": "Etsy Shop (Digital Products)",
        "description": "Sell printables, templates, graphics (no inventory needed).",
        "startup_cost": 100.0,  # Design software, initial listings
        "initial_time_investment_hours": 80.0,  # Create 20-30 products
        "hours_per_month_required": 15.0,  # New products, customer service
        "months_to_monetization": 3,  # Etsy SEO takes time
        "income_timeline": {
            0: 0,
            1: 10,  # First few sales
            2: 30,
            3: 80,  # Gaining traction
            6: 200,
            12: 500,  # After 1 year
            24: 1200,
        },
        "success_rate": 0.25,  # 25% reach $500/month
        "growth_rate": 1.10,  # 10% monthly growth
        "skills_required": {"design": 50},
        "skills_improved": {"design": 0.3, "marketing": 0.2, "business": 0.2},
    },
    
    "online_course": {
        "income_type": PassiveIncomeType.ONLINE_COURSE,
        "name": "Online Course (Udemy/Teachable)",
        "description": "Create and sell courses on skills you know (coding, design, etc.).",
        "startup_cost": 200.0,  # Recording equipment, course platform
        "initial_time_investment_hours": 120.0,  # Create 5-10 hour course
        "hours_per_month_required": 10.0,  # Answer questions, update content
        "months_to_monetization": 1,  # Immediate once course is live
        "income_timeline": {
            0: 0,
            1: 100,  # Initial sales from launch
            2: 150,
            3: 120,
            6: 200,  # Steady sales
            12: 400,
            24: 600,  # Long-tail sales
        },
        "success_rate": 0.30,  # 30% make decent income
        "growth_rate": 1.05,  # 5% monthly growth
        "skills_required": {"teaching": 60, "expertise_in_topic": 70},
        "skills_improved": {"teaching": 0.4, "video_editing": 0.2},
    },
    
    "stock_photography": {
        "income_type": PassiveIncomeType.STOCK_PHOTOGRAPHY,
        "name": "Stock Photography",
        "description": "Sell photos on Shutterstock, Adobe Stock, Getty Images.",
        "startup_cost": 1000.0,  # Camera, lenses
        "initial_time_investment_hours": 60.0,  # Shoot 200-300 photos
        "hours_per_month_required": 15.0,  # Upload new photos
        "months_to_monetization": 2,  # Photos need to be approved
        "income_timeline": {
            0: 0,
            2: 20,  # First sales
            3: 40,
            6: 100,  # Portfolio growing
            12: 300,
            24: 700,  # 1000+ photos
        },
        "success_rate": 0.20,  # 20% make decent income
        "growth_rate": 1.08,  # 8% monthly growth as portfolio grows
        "skills_required": {"photography": 60},
        "skills_improved": {"photography": 0.4, "editing": 0.2},
    },
}


# =============================================================================
# SMALL BUSINESS OPTIONS (High risk, high reward)
# =============================================================================

BUSINESS_OPTIONS = {
    "dropshipping_store": {
        "business_type": BusinessType.DROPSHIPPING,
        "name": "Dropshipping Store",
        "description": "Sell products online without holding inventory. Low startup cost but competitive.",
        "startup_cost": 500.0,  # Shopify ($29/month), domain, initial ads
        "monthly_fixed_costs": 150.0,  # Shopify, apps, domain
        "monthly_variable_costs_percent": 0.30,  # 30% of revenue (product cost, ads)
        "initial_time_investment_hours": 100.0,  # Setup store, find products
        "ongoing_hours_per_week": 20.0,  # Customer service, marketing
        "revenue_timeline": {
            # Month: Monthly revenue (before expenses)
            1: 200,  # Testing products
            2: 400,
            3: 800,  # Finding winning products
            6: 2000,  # Scaling ads
            12: 5000,  # Established store
            24: 10000,  # Successful (if survive)
        },
        "success_rate": 0.10,  # Only 10% become profitable
        "failure_rate_per_month": 0.05,  # 5% chance of failure each month
        "breakeven_months": 6,  # Average time to profitability
        "skills_required": {"marketing": 50, "business": 40},
        "skills_improved": {"marketing": 0.5, "business": 0.4, "ecommerce": 0.5},
    },
    
    "freelance_agency": {
        "business_type": BusinessType.FREELANCE_AGENCY,
        "name": "Freelance Agency",
        "description": "Hire other freelancers, manage client projects. High leverage but complex.",
        "startup_cost": 2000.0,  # Website, legal (LLC), initial marketing
        "monthly_fixed_costs": 500.0,  # Website, tools, bookkeeping
        "monthly_variable_costs_percent": 0.60,  # 60% goes to freelancers
        "initial_time_investment_hours": 150.0,  # Setup, find clients, hire freelancers
        "ongoing_hours_per_week": 30.0,  # Project management, client communication
        "revenue_timeline": {
            1: 1000,  # First few clients
            2: 2000,
            3: 4000,  # Growing client base
            6: 8000,
            12: 15000,  # Established agency
            24: 30000,  # Successful agency
        },
        "success_rate": 0.30,  # 30% become profitable
        "failure_rate_per_month": 0.03,
        "breakeven_months": 4,
        "skills_required": {"business": 60, "management": 50, "sales": 50},
        "skills_improved": {"business": 0.6, "management": 0.5, "sales": 0.4},
    },
    
    "mobile_app": {
        "business_type": BusinessType.MOBILE_APP,
        "name": "Mobile App",
        "description": "Build and launch iOS/Android app. High risk but potential for huge payoff.",
        "startup_cost": 3000.0,  # Development tools, App Store fees, initial marketing
        "monthly_fixed_costs": 200.0,  # Servers, tools
        "monthly_variable_costs_percent": 0.30,  # 30% on ads/marketing
        "initial_time_investment_hours": 300.0,  # 3-6 months to build
        "ongoing_hours_per_week": 15.0,  # Updates, support
        "revenue_timeline": {
            # Most apps fail, but some succeed
            3: 0,  # Still building
            6: 100,  # Launch, few downloads
            9: 300,  # Growing slowly
            12: 1000,  # If app is good
            18: 3000,  # Gaining traction
            24: 8000,  # Successful app
        },
        "success_rate": 0.01,  # Only 1% of apps make significant money
        "failure_rate_per_month": 0.08,  # 8% chance of giving up each month
        "breakeven_months": 12,
        "skills_required": {"coding": 80, "product_design": 60},
        "skills_improved": {"coding": 0.8, "product_design": 0.5, "business": 0.4},
    },
    
    "online_store_handmade": {
        "business_type": BusinessType.ONLINE_STORE,
        "name": "Online Store (Handmade Products)",
        "description": "Sell handmade products (jewelry, art, crafts) on Etsy/Shopify.",
        "startup_cost": 1000.0,  # Materials, packaging, initial inventory
        "monthly_fixed_costs": 100.0,  # Platform fees, materials
        "monthly_variable_costs_percent": 0.40,  # 40% on materials, shipping
        "initial_time_investment_hours": 80.0,  # Create initial inventory
        "ongoing_hours_per_week": 25.0,  # Make products, fulfill orders
        "revenue_timeline": {
            1: 300,
            2: 500,
            3: 800,
            6: 1500,
            12: 3000,
            24: 6000,
        },
        "success_rate": 0.40,  # 40% become profitable (higher than dropshipping)
        "failure_rate_per_month": 0.02,
        "breakeven_months": 5,
        "skills_required": {"creativity": 60, "crafting": 60},
        "skills_improved": {"crafting": 0.5, "business": 0.4, "marketing": 0.3},
    },
    
    "social_media_agency": {
        "business_type": BusinessType.SERVICE_BUSINESS,
        "name": "Social Media Agency",
        "description": "Manage social media for multiple small businesses. Scalable service business.",
        "startup_cost": 1500.0,  # Website, tools (Hootsuite), initial marketing
        "monthly_fixed_costs": 300.0,  # Tools, website hosting
        "monthly_variable_costs_percent": 0.20,  # 20% on ads, content creation
        "initial_time_investment_hours": 100.0,  # Setup, find first clients
        "ongoing_hours_per_week": 25.0,  # Manage 5-10 clients
        "revenue_timeline": {
            1: 1000,  # First 2-3 clients at $500/month each
            2: 2000,
            3: 3000,
            6: 5000,  # 10 clients
            12: 8000,
            24: 12000,
        },
        "success_rate": 0.50,  # 50% become profitable (high demand)
        "failure_rate_per_month": 0.02,
        "breakeven_months": 3,
        "skills_required": {"social_media": 70, "business": 50},
        "skills_improved": {"social_media": 0.6, "business": 0.5, "marketing": 0.5},
    },
}


# =============================================================================
# ACHIEVEMENTS
# =============================================================================

SIDE_GIG_ACHIEVEMENTS = [
    {
        "achievement_id": "first_gig",
        "name": "First Gig 🚗",
        "tier": "bronze",
        "description": "Start your first side gig",
        "trigger": "Start any gig",
        "message": "Welcome to the gig economy. Flexibility = freedom (but also instability).",
    },
    {
        "achievement_id": "gig_grinder",
        "name": "Gig Grinder 💪",
        "tier": "bronze",
        "description": "Work 100 hours across gigs",
        "trigger": "100 total gig hours",
        "message": "You're hustling. But remember: time is finite. Don't burn out.",
    },
    {
        "achievement_id": "side_income_1k",
        "name": "Side Income: $1K 💵",
        "tier": "silver",
        "description": "Earn $1,000 from side gigs",
        "trigger": "Earn $1,000 from gigs",
        "message": "$1K from side hustles! That's real money. Keep building.",
    },
    {
        "achievement_id": "portfolio_builder",
        "name": "Portfolio Builder 📁",
        "tier": "bronze",
        "description": "Build portfolio through freelance work",
        "trigger": "Portfolio quality reaches 50",
        "message": "Your portfolio is growing. Good work = future high-paying clients.",
    },
    {
        "achievement_id": "passive_income_starter",
        "name": "Passive Income Starter 🌱",
        "tier": "bronze",
        "description": "Start your first passive income stream",
        "trigger": "Start blog, YouTube, etc.",
        "message": "Passive income takes TIME. Don't expect $$ for 6-12 months. Be patient.",
    },
    {
        "achievement_id": "first_dollar_passive",
        "name": "First Passive Dollar 💸",
        "tier": "silver",
        "description": "Earn your first dollar from passive income",
        "trigger": "First passive income payment",
        "message": "Your first dollar! It's not much, but it's proof the model works. Keep going.",
    },
    {
        "achievement_id": "passive_income_100",
        "name": "Passive Income: $100/month 🎯",
        "tier": "gold",
        "description": "Earn $100/month from passive income",
        "trigger": "Monthly passive income reaches $100",
        "message": "$100/month passive! That's groceries paid for by content you made months ago.",
    },
    {
        "achievement_id": "passive_income_1k",
        "name": "Passive Income: $1K/month 🚀",
        "tier": "platinum",
        "description": "Earn $1,000/month from passive income",
        "trigger": "Monthly passive income reaches $1,000",
        "message": "$1K/month passive! That's a part-time job income without active work. Incredible.",
    },
    {
        "achievement_id": "entrepreneur",
        "name": "Entrepreneur 💼",
        "tier": "silver",
        "description": "Start your first small business",
        "trigger": "Start any business",
        "message": "You're a business owner. 80% fail. Will you be the 20%? Keep pushing.",
    },
    {
        "achievement_id": "first_profit",
        "name": "First Profit 📈",
        "tier": "gold",
        "description": "Make your first profitable month in business",
        "trigger": "Business revenue > expenses for first time",
        "message": "First profitable month! Most businesses take 6-12 months. You did it.",
    },
    {
        "achievement_id": "business_5k",
        "name": "Business Revenue: $5K/month 💰",
        "tier": "platinum",
        "description": "Reach $5,000/month in business revenue",
        "trigger": "Monthly business revenue reaches $5,000",
        "message": "$5K/month revenue! Your business is real. Now scale it sustainably.",
    },
    {
        "achievement_id": "diversified_income",
        "name": "Diversified Income 🌐",
        "tier": "gold",
        "description": "Have 3+ active income streams",
        "trigger": "Active in: job + gig + passive OR job + business + gig, etc.",
        "message": "Multiple income streams = financial security. Don't rely on one source.",
    },
    {
        "achievement_id": "burnout_warning",
        "name": "Burnout Warning ⚠️",
        "tier": "bronze",
        "description": "Work 60+ hours/week for 4 weeks straight",
        "trigger": "60+ hours for 4 consecutive weeks",
        "message": "You're burning out. Money isn't worth your health. Scale back.",
    },
]


# =============================================================================
# STORIES
# =============================================================================

SIDE_GIG_STORIES = [
    {
        "story_id": "first_gig_day",
        "title": "First Gig Day",
        "tone": "educational",
        "trigger": "Complete first gig shift",
        "message": """
You just finished your first DoorDash shift.

3 hours. $52 earned. Not bad.

But then you calculate:
- Gas: $12
- Car wear and tear: ~$6
- Actual earnings: $34

$11.33/hour after expenses.

Still, it's FLEXIBLE. You worked when you wanted. That's worth something.

But don't forget: Your car has 100,000 more miles on it. That has a cost.
""",
    },
    {
        "story_id": "gig_income_varies",
        "title": "Income Varies",
        "tone": "educational",
        "trigger": "Experience good week and bad week",
        "message": """
Two weeks of DoorDash:

Week 1: 15 hours, $320 earned ($21/hour) → Peak hours, good tips
Week 2: 15 hours, $215 earned ($14/hour) → Slow week, bad weather

Gig income is VARIABLE. You can't rely on $320 every week.

Some months will be great. Some will be rough.

Budget based on your AVERAGE income, not your best week.
""",
    },
    {
        "story_id": "freelance_low_pay_start",
        "title": "Freelance: The Beginning",
        "tone": "supportive",
        "trigger": "Start freelancing",
        "message": """
You land your first freelance writing gig:

$50 for a 1,000-word article.
Took you 4 hours to write.
$12.50/hour.

That's... less than you hoped.

But here's the thing: You're building a PORTFOLIO.
In 6 months, you'll charge $200 for that same article.
In 12 months, maybe $400.

Everyone starts at the bottom. Keep building.
""",
    },
    {
        "story_id": "portfolio_opens_doors",
        "title": "Portfolio Opens Doors",
        "tone": "triumphant",
        "trigger": "Portfolio quality reaches 60",
        "message": """
A client sees your portfolio and says:

"This is great work. I'll pay you $100/hour for a project."

Six months ago, you were charging $25/hour.

What changed? Your PORTFOLIO.

Good work attracts high-paying clients.
Every project is an investment in future income.
""",
    },
    {
        "story_id": "passive_income_reality",
        "title": "Passive Income Reality",
        "tone": "educational",
        "trigger": "Start blog/YouTube",
        "message": """
You start a tech blog.

Month 1: 50 visitors, $0 earned
Month 2: 120 visitors, $0 earned
Month 3: 300 visitors, $2.47 earned

"This is a waste of time," you think.

But then:
Month 6: 2,000 visitors, $87 earned
Month 12: 8,000 visitors, $420 earned
Month 18: 15,000 visitors, $980 earned

Passive income takes TIME. Months. Sometimes years.

But once it's built, it pays while you sleep.
""",
    },
    {
        "story_id": "first_passive_dollar",
        "title": "The First Passive Dollar",
        "tone": "triumphant",
        "trigger": "Earn first passive income",
        "message": """
You check your blog dashboard:

"AdSense payment: $12.47"

It's not much. But you wrote those blog posts MONTHS ago.

And people are STILL reading them.
And they're STILL earning you money.

That's passive income.

Imagine having 100 pieces of content, each earning $10-50/month.
That's $1,000-5,000/month. While you sleep.

Keep creating.
""",
    },
    {
        "story_id": "business_startup_costs",
        "title": "Startup Costs Hit Hard",
        "tone": "educational",
        "trigger": "Start business with high startup cost",
        "message": """
You decide to start a dropshipping store.

Startup costs:
- Shopify subscription: $29/month
- Domain: $15/year
- Logo design: $100
- Initial Facebook ads: $300
- Product samples: $150

Total: $594 spent before you make a single sale.

Month 1: $250 in sales, but $200 in ads.
Profit: $50

You're $544 in the red.

Starting a business requires CAPITAL and PATIENCE.
Most businesses take 6-12 months to become profitable.
""",
    },
    {
        "story_id": "business_first_profit",
        "title": "First Profitable Month!",
        "tone": "triumphant",
        "trigger": "Business becomes profitable",
        "message": """
Month 6 of your business:

Revenue: $3,200
Expenses: $2,100
Profit: $1,100

Your first PROFITABLE month!

You've invested $8,000 and 300 hours over 6 months.
You're still down $6,900 total.

But the trend is clear: Growth.

This is how businesses work. Invest first. Profit later.

Keep scaling.
""",
    },
    {
        "story_id": "time_management_crisis",
        "title": "Time Management Crisis",
        "tone": "supportive",
        "trigger": "Work 60+ hours/week",
        "message": """
Your schedule this week:

- Classes: 15 hours
- Part-time job: 20 hours
- DoorDash: 15 hours
- Freelance project: 12 hours
- Sleep: 6 hours/night (42 hours/week)

Total: 104 hours scheduled in a 168-hour week.

You're exhausted. Stressed. Grades slipping.

LESSON: You can't do everything.

Diversification is good. Overwork is not.
Choose 1-2 side hustles. Not 5.

Burnout costs more than the extra $200/week.
""",
    },
    {
        "story_id": "diversified_income_security",
        "title": "Diversified Income = Security",
        "tone": "triumphant",
        "trigger": "Have 3+ income streams",
        "message": """
Your income this month:

- Part-time job: $800
- Freelance design: $600
- Blog passive income: $150

Total: $1,550

Your part-time job cuts your hours.
Your income drops to $400 from that job.

But:
- Freelance: $600 (unchanged)
- Blog: $150 (unchanged)

Total: $1,150

You lost 50% of one income stream but only 25% of total income.

DIVERSIFICATION = SECURITY.

Don't rely on one income source. Build multiple streams.
""",
    },
    {
        "story_id": "skill_monetization",
        "title": "Your Skills = Money",
        "tone": "educational",
        "trigger": "Reach $75/hour+ freelance rate",
        "message": """
A year ago: You charged $25/hour for design work.

Today: A client offers $100/hour.

What changed?
✓ Your skills improved
✓ Your portfolio grew
✓ Your reputation built

SKILLS = INCOME.

Want to earn more? Get better at valuable skills:
- Coding
- Design
- Writing
- Marketing

The market pays for VALUE. Become more valuable.
""",
    },
]
