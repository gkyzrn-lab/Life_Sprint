"""Scam detection mini-game for Life Sprint.

Teaches students:
- How to spot phishing emails
- Red flags in job postings
- Romance/social media scams
- Tech support scams
- Financial fraud tactics
- Identity theft prevention
- Safe online practices
"""

from typing import Dict, List, Optional, Literal
from pydantic import BaseModel, Field
import random


class ScamScenario(BaseModel):
    """A scam scenario for the player to evaluate."""
    scenario_id: str
    scam_type: Literal["phishing_email", "fake_job", "romance_scam", "tech_support", 
                       "investment_scam", "rental_scam", "scholarship_scam", "prize_notification"]
    difficulty: Literal["easy", "medium", "hard"]
    
    # The scenario content
    title: str
    sender: str  # Who it's from
    content: str  # Full text of email/message/posting
    
    # Truth
    is_scam: bool
    
    # Red flags present (if scam)
    red_flags: List[str] = Field(default_factory=list)
    
    # Green flags (if legitimate)
    legitimate_signs: List[str] = Field(default_factory=list)
    
    # Educational info
    why_scam_or_legit: str = ""
    real_world_example: str = ""


class ScamDetectionResponse(BaseModel):
    """Player's response to a scam scenario."""
    player_verdict: Literal["scam", "legitimate", "unsure"]
    confidence: Literal["low", "medium", "high"]
    
    # Which red flags did player identify?
    identified_red_flags: List[str] = Field(default_factory=list)


class ScamDetectionResult(BaseModel):
    """Result of scam detection attempt."""
    correct: bool
    score: int  # Points earned (0-100)
    
    # Feedback
    actual_answer: Literal["scam", "legitimate"]
    red_flags_missed: List[str] = Field(default_factory=list)
    false_positives: List[str] = Field(default_factory=list)
    
    # Educational feedback
    explanation: str
    prevention_tip: str
    
    # Stats
    scam_detection_skill_gained: int = 0


class ScamPreventionTip(BaseModel):
    """A tip for preventing scams."""
    tip_id: str
    category: Literal["email_safety", "job_hunting", "online_dating", "financial", "tech", "general"]
    title: str
    description: str
    example: str
    importance: Literal["low", "medium", "high", "critical"]


# Scam scenarios database
SCAM_SCENARIOS: Dict[str, ScamScenario] = {
    # ========== EASY PHISHING EMAILS ==========
    "phishing_easy_1": ScamScenario(
        scenario_id="phishing_easy_1",
        scam_type="phishing_email",
        difficulty="easy",
        title="URGENT: Your Bank Account Has Been Compromised!!!",
        sender="security@chase-bank-security.net",
        content="""Dear Valued Customer,

Your account has been COMPROMISED and will be CLOSED in 24 hours unless you verify your identity immediately!

Click here to verify: http://chase-verify-account.net/secure

If you do not respond, your account will be permanently suspended and you will lose access to your funds!!!

Chase Bank Security Team""",
        is_scam=True,
        red_flags=[
            "Multiple exclamation marks and ALL CAPS",
            "Creates artificial urgency (24 hours)",
            "Suspicious domain (chase-bank-security.net, not chase.com)",
            "Threatening language about losing funds",
            "Generic greeting ('Dear Valued Customer')",
            "Asks to click suspicious link"
        ],
        why_scam_or_legit="Banks never send urgent emails asking you to click links. They'll call or send official mail. The domain is fake (not chase.com), and real banks use your name, not 'Valued Customer'.",
        real_world_example="In 2023, phishing emails stole over $52 million from consumers. Chase and other banks explicitly state they'll never ask for credentials via email."
    ),
    
    "phishing_easy_2": ScamScenario(
        scenario_id="phishing_easy_2",
        scam_type="phishing_email",
        difficulty="easy",
        title="Congratulations! You've Won $5,000,000",
        sender="lottery@international-prize-claims.com",
        content="""CONGRATULATIONS!!!

You have been selected as the WINNER of our International Sweepstakes! You have won $5,000,000 USD!

To claim your prize, please send:
- Full name
- Date of birth
- Social Security Number
- Bank account information for wire transfer
- Processing fee of $500 (for taxes and administrative costs)

Reply within 48 hours or prize will go to alternate winner!

International Prize Committee""",
        is_scam=True,
        red_flags=[
            "You never entered a sweepstakes",
            "Asks for Social Security Number",
            "Asks for bank account information",
            "Requires upfront payment ($500 'fee')",
            "Creates false urgency (48 hours)",
            "Generic sender name",
            "Too good to be true ($5 million)"
        ],
        why_scam_or_legit="Real sweepstakes never require payment or ask for SSN via email. If you didn't enter, you can't win. The 'processing fee' scam is classic fraud.",
        real_world_example="The FTC reports that fake prize/lottery scams cost Americans over $166 million in 2022. No legitimate prize requires upfront payment."
    ),
    
    # ========== MEDIUM PHISHING (More Sophisticated) ==========
    "phishing_medium_1": ScamScenario(
        scenario_id="phishing_medium_1",
        scam_type="phishing_email",
        difficulty="medium",
        title="Security Alert: New Sign-In from Unknown Device",
        sender="no-reply@account-security.apple-support.com",
        content="""Hi Sarah,

We noticed a new sign-in to your Apple ID from a device we don't recognize.

Device: Windows PC
Location: Moscow, Russia
Time: February 13, 2026 at 3:42 AM EST

If this was you, you can disregard this email.

If this wasn't you, your account may be compromised. Secure your account immediately:

https://appleid.apple.com.secure-verify.net/account/manage

Your Apple Security Team

Apple ID: s.chen@email.com""",
        is_scam=True,
        red_flags=[
            "Suspicious subdomain (apple.com.secure-verify.net instead of apple.com)",
            "Uses your real name and email (scraped from data breach)",
            "Link goes to fake domain (not apple.com)",
            "Creates fear (Russia, 3:42 AM)",
            "Sender domain is fake (apple-support.com)"
        ],
        legitimate_signs=[
            "Uses your actual name",
            "References specific device and location",
            "Professional formatting",
            "Realistic scenario (security alert)"
        ],
        why_scam_or_legit="This is sophisticated! Uses your real info and looks professional. But the URL is fake: 'apple.com.secure-verify.net' means secure-verify.net owns it, not apple.com. Real Apple links only use apple.com.",
        real_world_example="Phishers buy leaked email/name databases from data breaches to personalize scams. In 2023, over 8 billion records were exposed in data breaches. Always check URLs carefully - the LAST part before .com/.net is what matters (apple.com vs fake-apple.net)."
    ),
    
    "phishing_medium_2": ScamScenario(
        scenario_id="phishing_medium_2",
        scam_type="phishing_email",
        difficulty="medium",
        title="Your Amazon Order #402-8291847-9283749",
        sender="auto-confirm@amazon.com",
        content="""Hello,

Thank you for your Amazon order.

Order Details:
- iPhone 15 Pro Max 256GB - Quantity: 2
- Total: $2,398.00
- Delivery: February 15, 2026

Shipping Address:
1247 Oak Street
Chicago, IL 60614

If you did not place this order, please contact us immediately at:
1-888-555-0199 (Amazon Fraud Prevention)

You can also review your order here:
https://amazon.com-orders.net/track/402-8291847-9283749

Thank you for being an Amazon customer.

Amazon Customer Service""",
        is_scam=True,
        red_flags=[
            "Domain is fake (amazon.com-orders.net instead of amazon.com)",
            "Phone number likely fake (not official Amazon support)",
            "Creates panic (expensive unauthorized purchase)",
            "Order number looks realistic but is fake",
            "Link goes to fake domain"
        ],
        legitimate_signs=[
            "Professional formatting",
            "Realistic order details",
            "Plausible scenario",
            "No urgent deadline pressure"
        ],
        why_scam_or_legit="Clever scam! Fake domain (amazon.com-orders.net) and phone number. Scammers hope you'll panic about the $2,398 charge and call the fake number, where they'll ask for account info. Real Amazon emails come from @amazon.com only.",
        real_world_example="This 'fake order confirmation' scam tricked 1.5 million people in 2023. Always go directly to the company's website/app, don't click email links or call numbers in suspicious emails."
    ),
    
    # ========== LEGITIMATE EMAILS ==========
    "legitimate_email_1": ScamScenario(
        scenario_id="legitimate_email_1",
        scam_type="phishing_email",
        difficulty="medium",
        title="Your Order Has Shipped - Order #123456",
        sender="shipment-tracking@amazon.com",
        content="""Hello Marcus,

Good news! Your order has shipped.

Order #112-9384756-2847563
Ordered on February 10, 2026

Items:
- Calculus Textbook (ISBN: 978-0134438986)
- Wireless Mouse

Track your package:
Visit Your Orders at amazon.com or use the Amazon app
Estimated delivery: February 16, 2026

Questions? Visit our Help Center at amazon.com/help

The Amazon Team""",
        is_scam=False,
        legitimate_signs=[
            "Sent from @amazon.com (official domain)",
            "Uses your actual name",
            "Directs to amazon.com, not external link",
            "No urgency or threats",
            "No request for personal information",
            "Professional formatting",
            "Tells you to use official site/app"
        ],
        why_scam_or_legit="This is legitimate! Real @amazon.com sender, directs you to the official website (not a sketchy link), uses your name, no urgency or scare tactics, doesn't ask for any information.",
        real_world_example="Real companies will: 1) Use official domains, 2) Never ask for passwords/SSN via email, 3) Let you check status on their official site, 4) Use your name, 5) No artificial urgency. The FTC reports that 90% of scam emails fail these basic checks."
    ),
    
    # ========== FAKE JOB POSTINGS ==========
    "fake_job_easy": ScamScenario(
        scenario_id="fake_job_easy",
        scam_type="fake_job",
        difficulty="easy",
        title="MAKE $5000/WEEK FROM HOME!!! NO EXPERIENCE NEEDED!!!",
        sender="hiring@easy-money-jobs.biz",
        content="""💰 URGENT HIRING - START TODAY! 💰

Position: Data Entry Specialist
Pay: $5,000/week ($260,000/year)
Hours: 2-3 hours/day
Location: Work from home!

NO EXPERIENCE REQUIRED! NO DEGREE NEEDED!

Job duties:
- Simple data entry
- Process payments
- Receive packages at your home and forward them

TO START:
1. Pay $297 for training materials and software
2. Provide bank account for direct deposit setup
3. Purchase $500 in gift cards for "verification"

APPLY NOW - LIMITED SPOTS!!!

Email: hiring@easy-money-jobs.biz""",
        is_scam=True,
        red_flags=[
            "Unrealistic pay ($260k/year for 2-3 hours/day)",
            "Requires upfront payment ($297)",
            "Asks to buy gift cards ($500)",
            "Asks for bank account info upfront",
            "No company name or details",
            "Excessive urgency and caps",
            "'Receive packages' = reshipping scam",
            "Suspicious domain (.biz)"
        ],
        why_scam_or_legit="Classic job scam! No legitimate job pays $260k/year for part-time data entry. Asking for money upfront is a HUGE red flag. 'Receiving packages' is a reshipping scam where you forward stolen goods. Gift cards = instant scam.",
        real_world_example="Job scams cost victims $367 million in 2023. Real employers never charge application/training fees or ask you to buy gift cards. If it sounds too good to be true, it is."
    ),
    
    "fake_job_medium": ScamScenario(
        scenario_id="fake_job_medium",
        scam_type="fake_job",
        difficulty="medium",
        title="Junior Software Engineer - Remote Position",
        sender="careers@techinnov8solutions.com",
        content="""TechInnov8 Solutions is hiring!

Position: Junior Software Engineer (Remote)
Salary: $95,000-$110,000/year
Experience: 0-2 years
Location: Fully remote

About TechInnov8:
We're a fast-growing tech startup working with Fortune 500 clients on cutting-edge AI projects.

Responsibilities:
- Develop web applications using React and Node.js
- Collaborate with senior engineers
- Participate in code reviews

Requirements:
- Bachelor's degree in CS or related field (or equivalent experience)
- Knowledge of JavaScript/TypeScript
- Strong problem-solving skills

Application Process:
1. Complete initial interview via Google Meet
2. Background check fee: $49.99 (reimbursed after 30 days)
3. Equipment deposit: $200 (for company laptop - refunded on return)

Apply: careers@techinnov8solutions.com

TechInnov8 Solutions | Building Tomorrow's Technology""",
        is_scam=True,
        red_flags=[
            "Asks for 'background check fee' ($49.99)",
            "Requires 'equipment deposit' ($200)",
            "Company website likely doesn't exist or is fake",
            "No physical address or phone number",
            "Reimbursement promises often unfulfilled",
            "Real companies provide equipment free"
        ],
        legitimate_signs=[
            "Realistic salary range",
            "Professional job description",
            "Reasonable requirements",
            "Uses Google Meet (common tool)"
        ],
        why_scam_or_legit="Sophisticated scam! Looks professional, but legitimate companies NEVER charge application/background check fees. Real employers either handle background checks themselves or use third-party services. The 'equipment deposit' is another red flag - real companies provide equipment at no cost.",
        real_world_example="In 2024, the FTC found that 30% of job seekers encountered fake postings. Real employers: 1) Never charge fees, 2) Have verifiable companies (check LinkedIn, Glassdoor), 3) Interview on professional platforms, 4) Provide equipment."
    ),
    
    "legitimate_job": ScamScenario(
        scenario_id="legitimate_job",
        scam_type="fake_job",
        difficulty="medium",
        title="Marketing Coordinator - ABC Corporation",
        sender="talent@abccorp.com",
        content="""ABC Corporation - Marketing Coordinator

Location: Chicago, IL (Hybrid - 3 days in office)
Salary: $48,000-$55,000/year
Experience: Entry-level (0-2 years)

About ABC Corp:
ABC Corporation is a 200+ employee marketing agency serving clients in healthcare and technology. Founded in 2005, we're based in downtown Chicago.

Responsibilities:
- Support marketing campaign execution
- Create social media content
- Assist with market research
- Coordinate with design team

Requirements:
- Bachelor's degree in Marketing, Communications, or related field
- Strong written communication skills
- Proficiency in Microsoft Office
- Social media knowledge a plus

Benefits:
- Health, dental, vision insurance
- 401(k) with 4% match
- 15 days PTO
- Professional development budget

To Apply:
Submit resume and cover letter via our careers portal:
https://abccorp.com/careers

ABC Corporation
123 Michigan Avenue, Suite 400
Chicago, IL 60601
Phone: (312) 555-0100

An Equal Opportunity Employer""",
        is_scam=False,
        legitimate_signs=[
            "Professional domain (@abccorp.com)",
            "Physical address and phone number",
            "Realistic salary and requirements",
            "Detailed company information",
            "No upfront fees or payments",
            "Apply through company website",
            "Specific job duties",
            "Standard benefits package",
            "Verifiable company (can Google)"
        ],
        why_scam_or_legit="This is legitimate! Has all the signs: real company with address/phone, reasonable salary, no fees, apply through official website, detailed job description, professional tone. You can verify ABC Corporation exists via Google/LinkedIn/Glassdoor.",
        real_world_example="Verify jobs by: 1) Googling the company, 2) Checking LinkedIn/Glassdoor reviews, 3) Calling the company directly (look up number separately), 4) Verifying the domain matches company website, 5) Never paying fees. In 2024, legitimate employers posted over 8 million jobs on verified platforms."
    ),
    
    # ========== ROMANCE SCAMS ==========
    "romance_scam_easy": ScamScenario(
        scenario_id="romance_scam_easy",
        scam_type="romance_scam",
        difficulty="easy",
        title="Message from Chris (Dating App Match)",
        sender="chris_williams_uk@protonmail.com",
        content="""Hi Beautiful!

I'm Chris, 32, from London. I'm a civil engineer working on an oil rig offshore. I saw your profile and felt an instant connection!

I have to tell you - I've never felt this way about someone I just met online. You're so beautiful and seem like such an amazing person. I think we have something really special here.

I know this is fast, but I feel like I can trust you. I'd love to video chat but the internet connection here on the rig is terrible - only email works.

I want to come visit you soon! But I have a small problem... my paycheck is delayed and I need to pay some bills. Could you help me with $500? I'll pay you back triple when I get paid next week. I promise.

I really think you're the one for me.

Love,
Chris

P.S. Here's a photo of me [stock photo of handsome man]""",
        is_scam=True,
        red_flags=[
            "Instant 'love' after just matching",
            "Works in remote location (oil rig, military, overseas)",
            "Can't video chat (always an excuse)",
            "Asks for money within days/weeks",
            "Promises to pay back 'triple'",
            "Uses stock photo (reverse image search)",
            "Moves off dating app to email quickly",
            "Creates emotional pressure"
        ],
        why_scam_or_legit="Classic romance scam! Scammers claim to work in remote locations (oil rig, military, overseas) to excuse no video chat. They declare love fast to create emotional connection, then ask for money for 'emergencies'. The photo is likely stolen from elsewhere.",
        real_world_example="Romance scams cost victims $1.3 billion in 2023 - more than any other scam type. Scammers target lonely people and build fake relationships over weeks/months before asking for money. Average loss: $9,000 per victim."
    ),
    
    # ========== TECH SUPPORT SCAMS ==========
    "tech_support_scam": ScamScenario(
        scenario_id="tech_support_scam",
        scam_type="tech_support",
        difficulty="easy",
        title="VIRUS ALERT - Your Computer is Infected!!!",
        sender="microsoft-security-alert@techsupport-365.com",
        content="""⚠️ CRITICAL SECURITY ALERT ⚠️

Windows Defender has detected 37 viruses on your computer!

THREATS DETECTED:
- Trojan.Win32.Generic
- Ransomware.Cryptolocker
- Spyware.Keylogger

Your personal data, passwords, and banking information are at risk!

IMMEDIATE ACTION REQUIRED:

Call Microsoft Certified Support NOW:
1-888-555-TECH (8324)

Available 24/7

DO NOT shut down your computer! This will cause permanent data loss!

Authorization Code: MS-8473-URGENT
Reference #: WIN-SECURITY-2026-0213

Microsoft Security Team
Toll-Free Support: 1-888-555-8324

⚠️ This is an urgent security alert. Call within 30 minutes or your system will be locked! ⚠️""",
        is_scam=True,
        red_flags=[
            "Pop-up or unsolicited email claiming virus",
            "Creates extreme urgency (30 minutes)",
            "Fake phone number (Microsoft doesn't call you)",
            "Threatens data loss/system lock",
            "Sender domain is fake (not @microsoft.com)",
            "Multiple threats and scare tactics",
            "Random 'authorization codes'",
            "Claims to be from Microsoft but isn't"
        ],
        why_scam_or_legit="Tech support scam! Microsoft/Apple/Google NEVER send pop-ups or emails with phone numbers asking you to call. If you call, scammers ask for remote access to your computer and either: 1) Install actual malware, 2) 'Find' fake problems and charge $300-500 to 'fix' them, 3) Steal your passwords/banking info.",
        real_world_example="Tech support scams stole $806 million from victims in 2023, mostly targeting seniors. Real tech companies never cold-call or send pop-ups. If you see these: 1) Close browser, 2) Run real antivirus, 3) Never call the number, 4) Never give remote access."
    ),
    
    # ========== SCHOLARSHIP SCAMS ==========
    "scholarship_scam": ScamScenario(
        scenario_id="scholarship_scam",
        scam_type="scholarship_scam",
        difficulty="medium",
        title="Congratulations! You've Been Selected for the National Achievement Scholarship",
        sender="awards@national-scholarship-foundation.org",
        content="""Dear Student,

Congratulations! Based on your academic record, you have been pre-selected for the National Achievement Scholarship worth $25,000.

This prestigious scholarship is awarded to only 100 students nationwide each year.

To claim your scholarship, you must:

1. Submit the application processing fee: $95
   (This covers administrative costs and background verification)

2. Provide the following information:
   - Social Security Number (for tax reporting)
   - Bank account details (for scholarship deposit)
   - Parent/guardian financial information

3. Respond within 7 days or your spot will go to an alternate recipient.

Your pre-qualification code: NSF-2026-AWARD-8472

Payment can be made via:
- Credit card
- Wire transfer  
- Gift cards (iTunes, Amazon, Visa)

Apply now at: national-scholarship-foundation.org/claim

This is a limited opportunity. Don't miss out on $25,000 for your education!

Sincerely,
Dr. Jennifer Matthews
Director, National Scholarship Foundation
Email: awards@national-scholarship-foundation.org""",
        is_scam=True,
        red_flags=[
            "Requires application fee ($95)",
            "Asks for Social Security Number via email",
            "Asks for bank account details",
            "Accepts gift cards as payment (red flag!)",
            "You didn't apply for this scholarship",
            "Creates false urgency (7 days)",
            "No legitimate organization name/address",
            "Can't verify organization online"
        ],
        why_scam_or_legit="Scholarship scam! Red flags: 1) Real scholarships are FREE to apply, 2) Never ask for SSN or bank info via email, 3) Don't accept gift cards (instant red flag), 4) If you didn't apply, you weren't 'selected', 5) Can't find this 'National Scholarship Foundation' anywhere legitimate.",
        real_world_example="Scholarship scams target desperate students/families. In 2023, they stole $5 million. Real scholarships: 1) Never charge fees, 2) Apply through official channels (school counselor, fastweb.com, scholarships.com), 3) Verify organization exists, 4) Don't require SSN upfront."
    ),
    
    # ========== INVESTMENT SCAMS ==========
    "investment_scam_hard": ScamScenario(
        scenario_id="investment_scam_hard",
        scam_type="investment_scam",
        difficulty="hard",
        title="Exclusive Investment Opportunity - Limited Time",
        sender="wealth.advisor@premier-capital-mgmt.com",
        content="""Good afternoon,

I'm reaching out because you've been identified as a qualified investor who may be interested in an exclusive opportunity.

Premier Capital Management is launching a private equity fund focused on AI technology startups. Our previous fund returned 847% over 3 years.

Key Details:
- Minimum investment: $5,000
- Projected return: 200-400% in 12-18 months
- Fund closes February 28th (limited to 50 investors)
- Past performance: See attached testimonials

Several of your colleagues from [your university] have already invested:
- Michael R. invested $10,000 → now worth $34,000
- Sarah L. invested $25,000 → now worth $87,500

I can offer you a preferred entry position if you commit this week. This is normally reserved for institutional investors, but I'm making an exception.

To secure your position:
1. Complete the investor agreement (attached)
2. Wire funds to: [bank details]
3. Your returns start accruing immediately

Our firm is registered and operates under SEC guidelines. You can verify our credentials on our website: premier-capital-mgmt.com

This is a time-sensitive opportunity. Let me know if you'd like to schedule a brief call to discuss.

Best regards,

Marcus Donovan, CFP
Senior Wealth Advisor
Premier Capital Management
Phone: (212) 555-0177
LinkedIn: linkedin.com/in/marcus-donovan-cfp""",
        is_scam=True,
        red_flags=[
            "Unsolicited investment offer",
            "Unrealistic returns (847%, 200-400%)",
            "Pressure to act quickly ('this week', 'limited to 50 investors')",
            "Name-drops others to create social proof",
            "Asks to wire money directly",
            "Claims to be SEC registered (verify this separately!)",
            "'Exclusive' opportunity for average person",
            "Past performance seems too good to be true"
        ],
        legitimate_signs=[
            "Professional formatting",
            "Includes phone number and LinkedIn",
            "Mentions SEC registration",
            "Has a professional website",
            "Uses financial terminology correctly"
        ],
        why_scam_or_legit="Sophisticated investment scam! Red flags: 1) 847% returns are unrealistic (even great funds return 15-25%), 2) Pressure tactics, 3) Unsolicited outreach, 4) While they claim SEC registration, verify this yourself at adviserinfo.sec.gov - scammers lie, 5) Real advisors don't cold-email strangers with 'exclusive' offers.",
        real_world_example="Investment scams stole $3.8 billion in 2023. Verify anyone claiming to be registered: visit adviserinfo.sec.gov and brokercheck.finra.org. If returns sound too good (anything over 25% annually is suspicious), it's likely fraud. Real advisors don't cold-email 'exclusive' opportunities."
    ),
}


# Scam prevention tips
SCAM_PREVENTION_TIPS: Dict[str, ScamPreventionTip] = {
    "check_url": ScamPreventionTip(
        tip_id="check_url",
        category="email_safety",
        title="Always Check the Full URL",
        description="The most important part of a URL is the domain (the part right before .com/.net/.org). Scammers create URLs like 'apple.com.verify-security.net' - this is owned by verify-security.net, NOT apple.com.",
        example="✅ Real: amazon.com/orders  ❌ Fake: amazon.com-orders.net, amazon-security.com",
        importance="critical"
    ),
    
    "verify_sender": ScamPreventionTip(
        tip_id="verify_sender",
        category="email_safety",
        title="Verify the Sender Email Address",
        description="Look at the actual email address, not just the display name. Scammers can make the display name say 'Apple Security' but the actual email is 'fake@scammer.net'.",
        example="Display name: 'Chase Bank Security' | Actual email: security@chase-verify.net ← FAKE (not @chase.com)",
        importance="critical"
    ),
    
    "no_urgency": ScamPreventionTip(
        tip_id="no_urgency",
        category="general",
        title="Scammers Create Artificial Urgency",
        description="Phrases like 'Act now!', 'Account will be closed in 24 hours!', 'Limited time!' are designed to make you panic and act without thinking. Real companies give you reasonable time.",
        example="❌ Red flag: 'Your account will be deleted in 2 hours!'  ✅ Real: 'Please review your account settings at your convenience.'",
        importance="high"
    ),
    
    "never_pay_fees": ScamPreventionTip(
        tip_id="never_pay_fees",
        category="job_hunting",
        title="Real Jobs Never Charge Fees",
        description="Legitimate employers never ask for money upfront - no application fees, background check fees, training fees, or equipment deposits. If they ask for money, it's a scam.",
        example="❌ Scam: 'Pay $49 for background check'  ✅ Real: 'We'll conduct a background check at no cost to you'",
        importance="critical"
    ),
    
    "gift_cards_scam": ScamPreventionTip(
        tip_id="gift_cards_scam",
        category="financial",
        title="Gift Cards = Instant Scam",
        description="No legitimate company, government agency, or court will ever ask for payment in gift cards (iTunes, Amazon, Visa gift cards, etc.). If someone asks for gift cards, it's 100% a scam. No exceptions.",
        example="❌ 'Pay your IRS bill with iTunes gift cards'  ❌ 'Send Google Play cards for job training'  ← ALWAYS SCAMS",
        importance="critical"
    ),
    
    "google_company": ScamPreventionTip(
        tip_id="google_company",
        category="job_hunting",
        title="Google Everything",
        description="Before applying for a job, wiring money, or giving personal info, Google the company name + 'scam' or 'review'. Check LinkedIn, Glassdoor, BBB. Real companies have online presence, reviews, and verifiable information.",
        example="Search: '[Company Name] reviews', '[Company Name] scam', check LinkedIn for employee profiles, verify address on Google Maps",
        importance="high"
    ),
    
    "no_ssn_email": ScamPreventionTip(
        tip_id="no_ssn_email",
        category="financial",
        title="Never Give SSN or Bank Info via Email",
        description="Legitimate companies never ask for Social Security Number, bank account details, credit card numbers, or passwords via email. If you need to provide this info, do it through official websites (HTTPS) or in person.",
        example="❌ Email asking for SSN 'for verification'  ✅ Providing SSN on official government website with HTTPS",
        importance="critical"
    ),
    
    "reverse_image": ScamPreventionTip(
        tip_id="reverse_image",
        category="online_dating",
        title="Reverse Image Search Profile Photos",
        description="If you're talking to someone online (dating, job offer, investment advisor), do a reverse image search of their photo (Google Images or TinEye.com). Scammers often use stock photos or stolen images.",
        example="On Google Images, click the camera icon and upload the person's profile photo. If it appears on multiple sites or stock photo sites, it's stolen.",
        importance="high"
    ),
    
    "too_good_true": ScamPreventionTip(
        tip_id="too_good_true",
        category="general",
        title="If It Sounds Too Good to Be True, It Is",
        description="$250k/year for part-time work? 800% investment returns? Won a prize you never entered? Free money? These don't exist. Scammers exploit hope and greed. Be skeptical of anything that sounds too easy or profitable.",
        example="❌ '$5000/week working 2 hours/day'  ❌ '1000% return guaranteed'  ❌ 'You won $1 million!'",
        importance="high"
    ),
    
    "video_call_verify": ScamPreventionTip(
        tip_id="video_call_verify",
        category="online_dating",
        title="Video Call Before Getting Emotionally Invested",
        description="Romance scammers always have excuses for not video calling (bad internet, broken camera, military deployment). Insist on a video call within the first week. If they refuse or make excuses, it's a scam.",
        example="✅ 'Let's video chat this week to get to know each other better!'  ❌ They say: 'My camera is broken / I'm on an oil rig with no internet / I'm shy'",
        importance="critical"
    ),
    
    "dont_wire_strangers": ScamPreventionTip(
        tip_id="dont_wire_strangers",
        category="financial",
        title="Never Wire Money to Someone You Haven't Met",
        description="Wire transfers, cryptocurrency, and gift cards are untraceable. Never send money to: online romantic interests, 'employers' before you start work, 'landlords' before seeing property, or 'investment advisors' you found online.",
        example="❌ Wiring rent deposit before seeing apartment  ❌ Sending Bitcoin to online boyfriend  ❌ Paying job 'training fee'",
        importance="critical"
    ),
    
    "call_directly": ScamPreventionTip(
        tip_id="call_directly",
        category="general",
        title="Don't Call Numbers in Suspicious Emails",
        description="If you get a concerning email (fraud alert, account suspension, prize notification), don't call the number in the email. Look up the company's official number separately (Google or back of your credit card) and call that.",
        example="Email says: 'Call 1-888-555-FAKE'  ✅ Instead: Google 'Chase Bank phone number' and call the official number",
        importance="high"
    ),
    
    "sec_verify": ScamPreventionTip(
        tip_id="sec_verify",
        category="financial",
        title="Verify Financial Advisors on SEC/FINRA Sites",
        description="Anyone offering investment advice should be registered with SEC or FINRA. Verify them at adviserinfo.sec.gov and brokercheck.finra.org. If they're not listed, don't invest.",
        example="Visit adviserinfo.sec.gov → Search advisor name → Check for disciplinary history, credentials, and registration status",
        importance="critical"
    ),
    
    "scholarship_free": ScamPreventionTip(
        tip_id="scholarship_free",
        category="financial",
        title="Legitimate Scholarships Are Always Free",
        description="Any scholarship that charges an application fee, processing fee, or requires upfront payment is a scam. Use free resources like Fastweb, Scholarships.com, or your school counselor.",
        example="✅ Free: Fastweb.com, college financial aid office  ❌ Scam: 'Pay $99 application fee to win $10,000'",
        importance="high"
    ),
}


def get_random_scenario(difficulty: Optional[Literal["easy", "medium", "hard"]] = None) -> ScamScenario:
    """Get a random scam scenario, optionally filtered by difficulty."""
    scenarios = list(SCAM_SCENARIOS.values())
    
    if difficulty:
        scenarios = [s for s in scenarios if s.difficulty == difficulty]
    
    return random.choice(scenarios)


def get_scenarios_by_type(scam_type: str) -> List[ScamScenario]:
    """Get all scenarios of a specific type."""
    return [s for s in SCAM_SCENARIOS.values() if s.scam_type == scam_type]


def evaluate_scam_detection(
    scenario: ScamScenario,
    response: ScamDetectionResponse,
    player_critical_thinking: int = 50
) -> ScamDetectionResult:
    """Evaluate player's scam detection attempt.
    
    Args:
        scenario: The scam scenario being evaluated
        response: Player's response
        player_critical_thinking: Player's critical thinking skill (0-100)
    
    Returns:
        Result with score and feedback
    """
    
    # Check if verdict is correct
    actual_answer = "scam" if scenario.is_scam else "legitimate"
    correct_verdict = (
        (response.player_verdict == "scam" and scenario.is_scam) or
        (response.player_verdict == "legitimate" and not scenario.is_scam)
    )
    
    # Base score
    if correct_verdict:
        base_score = 60
    elif response.player_verdict == "unsure":
        base_score = 30  # Better to be cautious than wrong
    else:
        base_score = 0  # Wrong answer
    
    # Bonus for identifying red flags correctly
    red_flags_missed = []
    false_positives = []
    
    if scenario.is_scam:
        # Check which red flags player identified
        correct_flags = [f for f in response.identified_red_flags if f in scenario.red_flags]
        false_positives = [f for f in response.identified_red_flags if f not in scenario.red_flags]
        red_flags_missed = [f for f in scenario.red_flags if f not in response.identified_red_flags]
        
        # Bonus for each correctly identified red flag
        flag_bonus = (len(correct_flags) / len(scenario.red_flags)) * 30 if scenario.red_flags else 0
        base_score += flag_bonus
        
        # Small penalty for false positives
        base_score -= len(false_positives) * 2
    
    else:
        # For legitimate scenarios, check if player identified legitimate signs
        if response.player_verdict == "legitimate":
            # Bonus for being confident when correct
            if response.confidence == "high":
                base_score += 15
            elif response.confidence == "medium":
                base_score += 10
    
    # Adjust for player skill
    skill_modifier = 0.8 + (player_critical_thinking / 100) * 0.4  # 0.8 to 1.2
    final_score = int(base_score * skill_modifier)
    final_score = max(0, min(100, final_score))
    
    # Skill gained
    if correct_verdict:
        skill_gained = 3 if scenario.difficulty == "hard" else (2 if scenario.difficulty == "medium" else 1)
    else:
        skill_gained = 1  # Learn from mistakes
    
    # Generate explanation
    if correct_verdict:
        explanation = f"Correct! {scenario.why_scam_or_legit}"
    else:
        explanation = f"Not quite. {scenario.why_scam_or_legit}"
    
    # Prevention tip
    prevention_tip = get_random_prevention_tip_for_type(scenario.scam_type)
    
    return ScamDetectionResult(
        correct=correct_verdict,
        score=final_score,
        actual_answer=actual_answer,
        red_flags_missed=red_flags_missed,
        false_positives=false_positives,
        explanation=explanation,
        prevention_tip=prevention_tip.description if prevention_tip else "",
        scam_detection_skill_gained=skill_gained
    )


def get_random_prevention_tip_for_type(scam_type: str) -> Optional[ScamPreventionTip]:
    """Get a relevant prevention tip for a scam type."""
    category_map = {
        "phishing_email": "email_safety",
        "fake_job": "job_hunting",
        "romance_scam": "online_dating",
        "investment_scam": "financial",
        "scholarship_scam": "financial",
        "tech_support": "tech",
    }
    
    category = category_map.get(scam_type, "general")
    relevant_tips = [t for t in SCAM_PREVENTION_TIPS.values() if t.category == category or t.category == "general"]
    
    return random.choice(relevant_tips) if relevant_tips else None


def get_tip(tip_id: str) -> Optional[ScamPreventionTip]:
    """Get a specific prevention tip by ID."""
    return SCAM_PREVENTION_TIPS.get(tip_id)


def get_all_tips() -> List[ScamPreventionTip]:
    """Get all prevention tips."""
    return list(SCAM_PREVENTION_TIPS.values())


def get_tips_by_category(category: str) -> List[ScamPreventionTip]:
    """Get all tips for a specific category."""
    return [t for t in SCAM_PREVENTION_TIPS.values() if t.category == category]
