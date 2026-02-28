import React, { useState, useEffect } from 'react'
import { TutorialStep, getTutorialSequence, completeTutorial, disableTutorials, createPlayer, getColleges, getMajors } from '../utils/api'
import './OnboardingModal.css'

interface OnboardingModalProps {
    playerName: string
    onComplete: (player: any) => void
}

// College options with major-dependent tuition (fallback if API fails)
const COLLEGES = [
    {
        id: 'cuny_baruch',
        name: 'CUNY Baruch College',
        baseNote: 'Public City College - Most Affordable',
        tuitionByMajor: {
            'cs': 8650,
            'ba': 7520,
            'engineering': 9050,
            'liberal_arts': 7280
        },
        benefits: [
            'Most affordable tuition',
            'Excellent value for money',
            'Strong NYC business connections',
            'Diverse, motivated student body',
            'Lower financial stress'
        ],
        cons: [
            'Large class sizes (100+ students)',
            'Limited on-campus housing',
            'Competitive course registration',
            'Less hand-holding from advisors',
            'Fewer resources than private schools'
        ],
        jobPaths: ['NYC corporations', 'Finance & accounting', 'Public sector', 'Small business']
    },
    {
        id: 'nyu',
        name: 'New York University',
        baseNote: 'Elite Private University',
        tuitionByMajor: {
            'cs': 71200,
            'ba': 62000,
            'engineering': 72200,
            'liberal_arts': 59500
        },
        benefits: [
            'Prestigious global reputation',
            'Elite alumni network',
            'Excellent career services',
            'Smaller class sizes',
            'World-class professors',
            'Top-tier internship access'
        ],
        cons: [
            'Very high tuition ($240K+ total)',
            'High academic pressure',
            'Competitive peer environment',
            'Expensive NYC lifestyle expected',
            'Heavy loan burden post-graduation'
        ],
        jobPaths: ['Investment banking', 'Top tech companies', 'Consulting firms', 'Corporate leadership']
    },
    {
        id: 'columbia',
        name: 'Columbia University',
        baseNote: '🏆 Ivy League - Highest Prestige & Challenge',
        tuitionByMajor: {
            'cs': 80750,
            'ba': 70200,
            'engineering': 81800,
            'liberal_arts': 67800
        },
        benefits: [
            'Ivy League prestige opens doors everywhere',
            'Unmatched alumni network (CEOs, founders, leaders)',
            'World-renowned faculty',
            'Premium career placement services',
            'Exclusive networking events',
            'Highest starting salaries'
        ],
        cons: [
            'Extremely high tuition ($270K+ total)',
            'Most academically challenging (hardest curves)',
            'Intense competition with brilliant peers',
            'High stress and burnout risk',
            'Pressure to maintain top performance',
            'Massive debt if no financial aid'
        ],
        jobPaths: ['Fortune 500 executives', 'Goldman Sachs / JP Morgan', 'Top law/med schools', 'Silicon Valley leadership']
    }
]

// Major options with detailed information
const MAJORS = [
    {
        id: 'cs',
        name: 'Computer Science',
        description: 'Learn programming, data structures, algorithms, and software engineering. High earning potential but demanding coursework (advanced math, problem-solving). Leads to tech careers, startups, and innovation roles.',
        focus: 'Software development, algorithms, systems',
        difficulty: 'high',
        typical_salaries: '$90K-$160K entry level',
        job_outlook: 'excellent',
        costMultiplier: 1.15,
        costNote: 'Higher costs - Lab & equipment fees',
        benefits: [
            'Highest starting salary potential',
            'Abundant job opportunities',
            'Remote work flexibility',
            'Startup opportunities'
        ],
        cons: [
            'Very challenging coursework',
            'High burnout risk',
            'Requires constant upskilling',
            'Competitive job market'
        ],
        jobPaths: ['Software Engineer', 'Data Scientist', 'AI/ML Engineer', 'Full-Stack Developer', 'Engineering Lead'],
        skillsGained: ['Python', 'Algorithms', 'Databases', 'System design']
    },
    {
        id: 'ba',
        name: 'Business Administration',
        description: 'Master management, finance, marketing, and entrepreneurship. Versatile degree with good work-life balance. Strong networking is essential for success.',
        focus: 'Finance, management, entrepreneurship',
        difficulty: 'moderate',
        typical_salaries: '$60K-$95K entry level',
        job_outlook: 'good',
        costMultiplier: 1.0,
        costNote: 'Base rate - Most affordable',
        benefits: [
            'Versatile career paths',
            'Good work-life balance',
            'Less technical stress',
            'Entrepreneurship friendly'
        ],
        cons: [
            'More networking required',
            'Broader competition',
            'Results depend on connections',
            'Less specialized skills'
        ],
        jobPaths: ['Financial Analyst', 'Management Consultant', 'Entrepreneur', 'Marketing Manager', 'Product Manager'],
        skillsGained: ['Finance', 'Leadership', 'Communications', 'Analytics']
    },
    {
        id: 'engineering',
        name: 'Engineering',
        description: 'Design and build systems, machines, and infrastructure. Combines physics, math, and hands-on lab work. Rigorous but rewarding with stable career paths.',
        focus: 'Hardware, mechanical, civil systems',
        difficulty: 'very_high',
        typical_salaries: '$80K-$110K entry level',
        job_outlook: 'strong',
        costMultiplier: 1.20,
        costNote: 'Most expensive - Advanced labs & equipment',
        benefits: [
            'Strong salary growth',
            'Stable employment',
            'Impactful work',
            'Clear promotion paths'
        ],
        cons: [
            'Rigorous math requirements',
            'Lab work time-intensive',
            'Project deadlines',
            'Licensing requirements (PE exam)'
        ],
        jobPaths: ['Mechanical Engineer', 'Civil Engineer', 'Systems Engineer', 'Project Lead', 'Technical Director'],
        skillsGained: ['MATLAB', 'CAD', 'Physics', 'Problem-solving']
    },
    {
        id: 'liberal_arts',
        name: 'Liberal Arts',
        description: 'Explore humanities, social sciences, and critical thinking. Develops well-rounded perspective and communication skills. Career path less defined but offers flexibility.',
        focus: 'Humanities, social sciences, philosophy',
        difficulty: 'moderate',
        typical_salaries: '$50K-$75K entry level',
        job_outlook: 'moderate',
        costMultiplier: 0.95,
        costNote: 'Most affordable - Lower overhead costs',
        benefits: [
            'Flexible curriculum',
            'Creative thinking',
            'Well-rounded education',
            'Lower course intensity'
        ],
        cons: [
            'Lower starting salary',
            'Unclear career path',
            'Job market flexibility needed',
            'May need grad school'
        ],
        jobPaths: ['Teacher', 'Content Writer', 'Policy Analyst', 'Nonprofit Manager', 'Graduate School'],
        skillsGained: ['Critical thinking', 'Writing', 'Analysis', 'Communication']
    }
]

// Housing options with detailed information
const HOUSING_CATEGORIES = [
    {
        id: 'dorm',
        icon: '🏢',
        name: 'Dorm',
        description: 'On-campus housing with flexible terms',
        minLeaseSemesters: 1,
        penaltyFee: 0,
        options: [
            {
                id: 'dorm_standard',
                name: 'Standard Dorm',
                monthlyCost: 900,
                upfrontCost: 0,
                commuteMinutes: 5,
                stressLevel: 'Low',
                benefits: ['Walking distance to classes', 'Social community', 'No lease commitment'],
                cons: ['Shared facilities', 'Limited privacy']
            }
        ]
    },
    {
        id: 'family',
        icon: '👨‍👩‍👧‍👦',
        name: 'Family',
        description: 'Living with family members',
        minLeaseSemesters: 1,
        penaltyFee: 0,
        options: [
            {
                id: 'family_stay',
                name: 'Live with Family',
                monthlyCost: 0,
                upfrontCost: 0,
                commuteMinutes: 45,
                stressLevel: 'Medium',
                benefits: ['Free housing', 'Family support', 'No lease'],
                cons: ['Long commute', 'Less independence']
            }
        ]
    },
    {
        id: 'rent',
        icon: '🏠',
        name: 'Rent',
        description: 'Rent your own apartment (2+ semester commitment)',
        minLeaseSemesters: 2,
        penaltyFee: 3000,
        options: [
            {
                id: 'apt_cozy',
                name: 'Budget Apartment',
                monthlyCost: 1100,
                upfrontCost: 2200,
                commuteMinutes: 25,
                stressLevel: 'Medium',
                benefits: ['Own space', 'Affordable', 'Manageable commute'],
                cons: ['2-semester minimum', 'Tight budget if break lease']
            },
            {
                id: 'apt_spacious',
                name: 'Modern Apartment',
                monthlyCost: 1500,
                upfrontCost: 3000,
                commuteMinutes: 15,
                stressLevel: 'Low',
                benefits: ['Modern amenities', 'Close to campus', 'More comfortable'],
                cons: ['2-semester minimum', 'Higher rent']
            },
            {
                id: 'apt_luxury',
                name: 'Luxury Apartment',
                monthlyCost: 2000,
                upfrontCost: 4000,
                commuteMinutes: 10,
                stressLevel: 'Low',
                benefits: ['Premium amenities', 'Walking distance', 'Great social scene'],
                cons: ['2-semester minimum', 'Very expensive']
            }
        ]
    },
    {
        id: 'shared',
        icon: '🤝',
        name: 'House Sharing',
        description: 'Share a house/apartment with roommates',
        minLeaseSemesters: 1,
        penaltyFee: 1500,
        options: [
            {
                id: 'shared_basic',
                name: 'Basic Shared House',
                monthlyCost: 650,
                upfrontCost: 1300,
                commuteMinutes: 30,
                stressLevel: 'Medium-High',
                benefits: ['Very affordable', 'Social living', 'Shared utilities'],
                cons: ['Noisy roommates', 'Shared facilities']
            },
            {
                id: 'shared_comfortable',
                name: 'Comfortable Apartment',
                monthlyCost: 850,
                upfrontCost: 1700,
                commuteMinutes: 20,
                stressLevel: 'Medium',
                benefits: ['Affordable', 'Good location', 'Nice roommates'],
                cons: ['Shared space', 'Can have conflicts']
            },
            {
                id: 'shared_upscale',
                name: 'Upscale Loft',
                monthlyCost: 1100,
                upfrontCost: 2200,
                commuteMinutes: 12,
                stressLevel: 'Low',
                benefits: ['Modern space', 'Close to campus', 'Great community'],
                cons: ['More expensive sharing', 'Still shared space']
            }
        ]
    }
]

export function OnboardingModal({ playerName, onComplete }: OnboardingModalProps) {
    const [currentStep, setCurrentStep] = useState(0)
    const [tutorials, setTutorials] = useState<TutorialStep[]>([])
    const [playerId, setPlayerId] = useState<string | null>(null)
    const [progress, setProgress] = useState(0)
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState<string | null>(null)
    const [playerAge, setPlayerAge] = useState(18)
    const [showAgeScreen, setShowAgeScreen] = useState(true)
    const [selectedCollege, setSelectedCollege] = useState('cuny_baruch')
    const [selectedMajor, setSelectedMajor] = useState('cs')
    const [colleges, setColleges] = useState<any[]>([])
    const [majors, setMajors] = useState<any[]>([])
    const [loadingCatalogs, setLoadingCatalogs] = useState(true)
    const [showSelection, setShowSelection] = useState(false)
    const [showHousingScreen, setShowHousingScreen] = useState(false)
    const [selectedHousingCategory, setSelectedHousingCategory] = useState<string | null>(null)
    const [selectedHousingOption, setSelectedHousingOption] = useState<string | null>(null)

    // New states for setup step
    const [showSetup, setShowSetup] = useState(false)
    const [playsCollege, setPlaysCollege] = useState(false)
    const [highSchoolGPA, setHighSchoolGPA] = useState(3.5)
    const [suggestedBudget, setSuggestedBudget] = useState(5000)
    const [playerBudget, setPlayerBudget] = useState(5000)
    const [budgetWarning, setBudgetWarning] = useState('')

    // Calculate scholarship based on GPA
    const getScholarshipPercentage = (gpa: number): number => {
        if (gpa >= 3.8) return 50
        if (gpa >= 3.5) return 30
        if (gpa >= 3.0) return 15
        return 0
    }

    // Validate budget and show warning
    const handleBudgetChange = (value: number) => {
        setPlayerBudget(value)
        if (value < 1000) {
            setBudgetWarning('⚠️ Very risky - Less than $1000 is extremely tight. You may struggle to cover expenses.')
        } else if (value < suggestedBudget * 0.5) {
            setBudgetWarning('⚠️ Below average - You\'ll need to be very careful with money.')
        } else if (value > suggestedBudget * 2.5) {
            setBudgetWarning('💰 Above average - This is more cushion than most NYC freshmen have.')
        } else {
            setBudgetWarning('')
        }
    }

    // Fetch colleges and majors from API
    useEffect(() => {
        const fetchCatalogs = async () => {
            try {
                const [collegesData, majorsData] = await Promise.all([getColleges(), getMajors()])

                // Transform colleges data
                const transformedColleges = Object.values(collegesData).map((college: any) => ({
                    id: college.id,
                    name: college.name,
                    baseNote: college.notes || college.type.charAt(0).toUpperCase() + college.type.slice(1) + ' Institution',
                    offeredMajors: college.offered_majors || [],  // List of major IDs this college offers
                    benefits: college.benefits || [],
                    cons: college.cons || [],
                    jobPaths: college.career_paths || [],
                    networkingMultiplier: college.networking_multiplier || 1.0,
                    jobOpportunityBonus: college.job_opportunity_bonus || 0,
                    startingSalaryMultiplier: college.starting_salary_multiplier || 1.0,
                    baseTuition: college.base_tuition_per_year || 0
                }))

                setColleges(transformedColleges)

                // Store all majors (will be filtered by college selection)
                const transformedMajors = Object.values(majorsData).map((major: any) => ({
                    ...major,
                    jobPaths: major.career_paths || [],
                    tuitionMultiplier: major.tuition_multiplier || 1.0
                })).sort((a: any, b: any) => (a.name || '').localeCompare(b.name || ''))

                setMajors(transformedMajors)

                // Set default selections to first available options
                if (transformedColleges.length > 0) {
                    setSelectedCollege(transformedColleges[0].id)
                }
            } catch (err) {
                console.error('Failed to fetch catalogs:', err)
                // Use fallback hardcoded data
                setColleges(COLLEGES)
                setMajors(MAJORS)
            } finally {
                setLoadingCatalogs(false)
            }
        }
        fetchCatalogs()
    }, [])

    // Handle starting the game (creates player and loads tutorials)
    const handleStartGame = async () => {
        try {
            console.log('Starting game with:', { playerName, selectedCollege, selectedMajor, selectedHousingOption })
            setLoading(true)

            // 1. Create player with selected college and major
            console.log('Creating player...')
            const player = await createPlayer(
                playerName,
                selectedCollege,
                selectedMajor,
                highSchoolGPA,
                playerBudget,
                playerAge,
                selectedHousingOption || 'dorm'
            )
            console.log('Player created:', player)
            setPlayerId(player.id)
            setShowSetup(false) // Clear setup flag
            setShowSelection(false) // Clear selection flag so we show tutorials next

            // 2. Fetch tutorial sequence
            console.log('Fetching tutorial sequence...')
            const { sequence } = await getTutorialSequence()
            console.log('Tutorials loaded:', sequence)
            setTutorials(sequence)
            setLoading(false)
        } catch (err) {
            console.error('Error in handleStartGame:', err)
            setError(err instanceof Error ? err.message : 'Failed to initialize game')
            setLoading(false)
        }
    }

    const handleNext = async () => {
        if (!playerId) return

        try {
            setLoading(true)
            // Mark current tutorial as complete
            const response = await completeTutorial(playerId, tutorials[currentStep].step_id)
            setProgress(response.completion_percentage)

            if (currentStep < tutorials.length - 1) {
                setCurrentStep(currentStep + 1)
            } else {
                // Onboarding complete!
                const playerResponse = await fetch(`http://localhost:8000/player/${playerId}`)
                const finalPlayer = await playerResponse.json()
                onComplete(finalPlayer)
            }
            setLoading(false)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to complete tutorial')
            setLoading(false)
        }
    }

    const handleSkip = async () => {
        if (!playerId) return

        try {
            setLoading(true)
            // Disable tutorials and proceed
            await disableTutorials(playerId)
            const playerResponse = await fetch(`http://localhost:8000/player/${playerId}`)
            const finalPlayer = await playerResponse.json()
            onComplete(finalPlayer)
            setLoading(false)
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to skip tutorials')
            setLoading(false)
        }
    }

    if (error) {
        return (
            <div className="onboarding-container">
                <div className="onboarding-modal">
                    <div className="error-message">
                        <h2>Error</h2>
                        <p>{error}</p>
                        <p>Make sure the backend is running at http://localhost:8000</p>
                    </div>
                </div>
            </div>
        )
    }

    // Show age screen - FIRST step
    if (showAgeScreen) {
        return (
            <div className="onboarding-container">
                <div className="onboarding-modal age-modal">
                    <div className="age-content">
                        <h1>🎂 Welcome to Life Sprint!</h1>
                        <p className="age-intro">Hello, {playerName}! How old are you?</p>

                        <div className="age-section">
                            <p className="age-label">Age: <span className="age-value">{playerAge}</span></p>
                            <input
                                type="range"
                                min="16"
                                max="25"
                                value={playerAge}
                                onChange={(e) => setPlayerAge(parseInt(e.target.value))}
                                className="age-slider"
                            />
                            <div className="age-scale">
                                <span>16</span>
                                <span>18</span>
                                <span>25</span>
                            </div>
                            <p className="age-hint">
                                {playerAge < 18
                                    ? '🏫 High school student - You\'re just starting your journey!'
                                    : playerAge === 18
                                        ? '🎓 College freshman - Time to make important decisions!'
                                        : playerAge < 25
                                            ? '👨‍💼 Recent graduate - Navigating early career life!'
                                            : '🚀 Established adult - Making strategic life moves!'}
                            </p>
                        </div>

                        <div className="button-group">
                            <button
                                onClick={() => {
                                    setShowAgeScreen(false)
                                    setShowSelection(true)
                                }}
                                className="btn btn-primary"
                            >
                                Continue →
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

    // Show college and major selection first
    if (showSelection) {
        const collegeList = colleges.length > 0 ? colleges : COLLEGES
        const selectedCollegeData = collegeList.find(c => c.id === selectedCollege)

        // Filter majors based on selected college's offered_majors
        const allMajors = majors.length > 0 ? majors : MAJORS
        const majorList = allMajors
            .filter(m => {
                if (!selectedCollegeData || !selectedCollegeData.offeredMajors) {
                    return true  // Show all if no filtering data
                }
                return selectedCollegeData.offeredMajors.includes(m.id)
            })
            .sort((a, b) => (a.name || '').localeCompare(b.name || ''))

        // Reset major selection if it's not offered by the selected college
        if (majorList.length > 0 && !majorList.find(m => m.id === selectedMajor)) {
            setSelectedMajor(majorList[0].id)
        }

        const selectedMajorData = majorList.find(m => m.id === selectedMajor)

        const calculateTuition = () => {
            if (!selectedCollegeData || !selectedMajorData) return 8000
            const baseTuition = selectedCollegeData.baseTuition || 8000
            const multiplier = selectedMajorData.tuitionMultiplier || 1.0
            return Math.round(baseTuition * multiplier)
        }

        if (loadingCatalogs) {
            return (
                <div className="onboarding-container">
                    <div className="onboarding-modal">
                        <p>Loading colleges and majors...</p>
                    </div>
                </div>
            )
        }

        return (
            <div className="onboarding-container">
                <div className="onboarding-modal selection-modal">
                    <div className="selection-content">
                        <h1>🎓 Welcome to Life Sprint!</h1>
                        <p className="welcome-message">Hello, {playerName}! Choose your college and major to begin your journey.</p>

                        <div style={{ background: '#e3f2fd', padding: '12px 16px', borderRadius: '8px', marginBottom: '20px', borderLeft: '4px solid #1976d2' }}>
                            <p style={{ margin: 0, fontSize: '13px', color: '#1565c0', lineHeight: '1.5' }}>
                                💡 <strong>Tip:</strong> Your college choice affects networking opportunities, job access, and starting salaries.
                                Higher-tier schools provide better connections but cost more.
                            </p>
                        </div>

                        <div className="selection-grid">
                            {/* College Selection */}
                            <div className="selection-column">
                                <h2>Select Your College</h2>
                                <div className="cards-container">
                                    {collegeList.map((college) => {
                                        const tuitionCost = college.tuitionByMajor[selectedMajor as keyof typeof college.tuitionByMajor] || 8000
                                        return (
                                            <div
                                                key={college.id}
                                                className={`info-card ${selectedCollege === college.id ? 'selected' : ''}`}
                                                onClick={() => setSelectedCollege(college.id)}
                                            >
                                                <h3>{college.name}</h3>
                                                <p className="college-type">{college.baseNote}</p>
                                                <p className="tuition">💰 ${tuitionCost.toLocaleString()}/year</p>

                                                <div className="card-section">
                                                    <h4>Benefits</h4>
                                                    <ul>
                                                        {college.benefits.map((b, i) => (
                                                            <li key={i}>✓ {b}</li>
                                                        ))}
                                                    </ul>
                                                </div>

                                                <div className="card-section">
                                                    <h4>Considerations</h4>
                                                    <ul>
                                                        {college.cons.map((c, i) => (
                                                            <li key={i}>⚠ {c}</li>
                                                        ))}
                                                    </ul>
                                                </div>
                                            </div>
                                        )
                                    })}
                                </div>
                            </div>

                            {/* Major Selection */}
                            <div className="selection-column">
                                <h2>Select Your Major</h2>
                                <div className="cards-container">
                                    {majorList.map((major) => (
                                        <div
                                            key={major.id}
                                            className={`info-card ${selectedMajor === major.id ? 'selected' : ''}`}
                                            onClick={() => setSelectedMajor(major.id)}
                                        >
                                            <h3>{major.name}</h3>
                                            {major.typical_salaries && (
                                                <p className="cost-note">💰 {major.typical_salaries}</p>
                                            )}
                                            {major.job_outlook && (
                                                <p className="cost-note">📈 Job Outlook: {major.job_outlook}</p>
                                            )}

                                            {major.description && (
                                                <div className="card-section">
                                                    <h4>Overview</h4>
                                                    <p style={{ fontSize: '12px', color: '#666', margin: 0, lineHeight: '1.4' }}>
                                                        {major.description.length > 150
                                                            ? major.description.substring(0, 150) + '...'
                                                            : major.description}
                                                    </p>
                                                </div>
                                            )}

                                            {major.jobPaths && major.jobPaths.length > 0 && (
                                                <div className="card-section">
                                                    <h4>Career Paths</h4>
                                                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
                                                        {major.jobPaths.map((path: string, i: number) => (
                                                            <span key={i} style={{ backgroundColor: '#e3f2fd', padding: '4px 12px', borderRadius: '12px', fontSize: '11px', color: '#1976d2' }}>
                                                                {path}
                                                            </span>
                                                        ))}
                                                    </div>
                                                </div>
                                            )}
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </div>

                        <div className="selection-summary">
                            <h3>Your Selection & Cost</h3>
                            <p className="selection-text">{selectedCollegeData?.name} + {selectedMajorData?.name}</p>
                            {selectedCollegeData && selectedMajorData && (
                                <p className="cost-text">
                                    💰 Annual Tuition: ${calculateTuition().toLocaleString()}/year
                                </p>
                            )}

                            <div className="button-group">
                                <button
                                    onClick={() => {
                                        setShowSetup(true)
                                        setShowSelection(false)
                                    }}
                                    className="btn btn-primary"
                                >
                                    Continue to Setup
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

    // Show setup screen (sports, GPA, budget)
    if (showSetup && !playerId) {
        const scholarship = getScholarshipPercentage(highSchoolGPA)
        return (
            <div className="onboarding-container">
                <div className="onboarding-modal setup-modal">
                    <div className="setup-content">
                        <h1>⚙️ Let's Set Up Your Game</h1>
                        <p className="setup-intro">A few more details to personalize your experience</p>

                        {/* Sports Question */}
                        <div className="setup-section">
                            <h2>Do you play college sports?</h2>
                            <div className="button-group sports-group">
                                <button
                                    className={`btn btn-option ${playsCollege ? 'active' : ''}`}
                                    onClick={() => setPlaysCollege(true)}
                                >
                                    ⚽ Yes, I play sports
                                </button>
                                <button
                                    className={`btn btn-option ${!playsCollege ? 'active' : ''}`}
                                    onClick={() => setPlaysCollege(false)}
                                >
                                    📚 No, I don't play sports
                                </button>
                            </div>
                            <p className="option-hint">
                                {playsCollege
                                    ? '🎯 Playing sports boosts your network and health, but takes time away from studying.'
                                    : '💡 More study time, but you\'ll need other ways to build connections.'}
                            </p>
                        </div>

                        {/* High School GPA Question */}
                        <div className="setup-section">
                            <h2>What was your high school GPA?</h2>
                            <p className="gpa-hint">This determines your eligibility for scholarships</p>
                            <div className="gpa-input-group">
                                <input
                                    type="range"
                                    min="2.0"
                                    max="4.0"
                                    step="0.1"
                                    value={highSchoolGPA}
                                    onChange={(e) => setHighSchoolGPA(parseFloat(e.target.value))}
                                    className="gpa-slider"
                                />
                                <div className="gpa-display">
                                    <span className="gpa-value">{highSchoolGPA.toFixed(1)}</span>
                                    <span className="scholarship-badge">{scholarship}% scholarship</span>
                                </div>
                            </div>
                            <div className="gpa-scale">
                                <span>2.0</span>
                                <span>3.0</span>
                                <span>3.5</span>
                                <span>4.0</span>
                            </div>
                        </div>

                        {/* Budget Setup */}
                        <div className="setup-section">
                            <h2>Starting Budget</h2>
                            <p className="budget-hint">💰 NYC freshman average savings: ${suggestedBudget.toLocaleString()}</p>
                            <div className="budget-input-group">
                                <input
                                    type="number"
                                    min="500"
                                    max="50000"
                                    step="100"
                                    value={playerBudget}
                                    onChange={(e) => handleBudgetChange(parseInt(e.target.value))}
                                    className="budget-input"
                                />
                                <span className="budget-label">${playerBudget.toLocaleString()}</span>
                            </div>
                            {budgetWarning && (
                                <p className="budget-warning">{budgetWarning}</p>
                            )}
                            <p className="budget-note">💡 Keep it realistic! This is your starting money. You'll need to earn more through part-time jobs.</p>
                        </div>

                        <div className="button-group">
                            <button
                                onClick={() => setShowSetup(false)}
                                className="btn btn-secondary"
                            >
                                ← Back
                            </button>
                            <button
                                onClick={() => {
                                    setShowHousingScreen(true)
                                    setShowSetup(false)
                                }}
                                disabled={loading}
                                className="btn btn-primary"
                            >
                                Continue to Housing →
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

    // Show housing selection screen (after setup, before creating player)
    if (showHousingScreen && !playerId) {
        // We need to use state variables from component level, not create new ones here
        const handleCategorySelect = (categoryId: string) => {
            const category = HOUSING_CATEGORIES.find(c => c.id === categoryId)
            if (category && category.options.length === 1) {
                // Single option - select directly
                setSelectedHousingOption(category.options[0].id)
                setSelectedHousingCategory(categoryId)
                setShowHousingScreen(false)
                handleStartGame()
            } else {
                // Multiple options - show options screen
                setSelectedHousingCategory(categoryId)
            }
        }

        const handleOptionSelect = (optionId: string) => {
            setSelectedHousingOption(optionId)
            setShowHousingScreen(false)
            handleStartGame()
        }

        const selectedCategoryData = HOUSING_CATEGORIES.find(c => c.id === selectedHousingCategory)
        const showHousingOptions = selectedHousingCategory && HOUSING_CATEGORIES.find(c => c.id === selectedHousingCategory)?.options.length! > 1

        return (
            <div className="onboarding-container">
                <div className="onboarding-modal housing-modal">
                    <div className="housing-content">
                        {!showHousingOptions ? (
                            <>
                                <h1>🏠 Where Will You Live?</h1>
                                <p className="housing-intro">Choose your housing carefully - it affects your budget, commute, stress, and social life!</p>

                                <div className="housing-categories">
                                    {HOUSING_CATEGORIES.map((category) => (
                                        <div
                                            key={category.id}
                                            className={`housing-card ${selectedHousingCategory === category.id ? 'selected' : ''}`}
                                            onClick={() => handleCategorySelect(category.id)}
                                        >
                                            <div className="housing-card-header">
                                                <span className="housing-icon">{category.icon}</span>
                                                <h3>{category.name}</h3>
                                            </div>
                                            <p className="housing-description">{category.description}</p>
                                            {category.minLeaseSemesters > 0 && (
                                                <p className="lease-info">
                                                    📋 Min {category.minLeaseSemesters} sem{category.minLeaseSemesters > 1 ? 's' : ''} • ${category.penaltyFee.toLocaleString()} penalty
                                                </p>
                                            )}
                                            <p className="housing-hint">
                                                {category.options.length === 1
                                                    ? '👉 Click to select'
                                                    : `👉 ${category.options.length} options available`}
                                            </p>
                                        </div>
                                    ))}
                                </div>
                            </>
                        ) : selectedCategoryData && selectedCategoryData.options.length > 1 ? (
                            <>
                                <h1>🏠 {selectedCategoryData.name} Options</h1>
                                <p className="housing-intro">Compare your choices:</p>

                                <div className="housing-options">
                                    {selectedCategoryData.options.map((option) => (
                                        <div
                                            key={option.id}
                                            className={`option-card ${selectedHousingOption === option.id ? 'selected' : ''}`}
                                            onClick={() => handleOptionSelect(option.id)}
                                        >
                                            <h3>{option.name}</h3>

                                            <div className="option-stats">
                                                <div className="stat">
                                                    <span className="stat-icon">💰</span>
                                                    <div>
                                                        <p className="stat-label">Monthly Cost</p>
                                                        <p className="stat-value">${option.monthlyCost.toLocaleString()}</p>
                                                    </div>
                                                </div>
                                                <div className="stat">
                                                    <span className="stat-icon">🚗</span>
                                                    <div>
                                                        <p className="stat-label">Commute</p>
                                                        <p className="stat-value">{option.commuteMinutes} min</p>
                                                    </div>
                                                </div>
                                                <div className="stat">
                                                    <span className="stat-icon">😟</span>
                                                    <div>
                                                        <p className="stat-label">Stress Level</p>
                                                        <p className="stat-value">{option.stressLevel}</p>
                                                    </div>
                                                </div>
                                            </div>

                                            <div className="option-details">
                                                <div>
                                                    <h4>✓ Benefits</h4>
                                                    <ul>
                                                        {option.benefits.map((b, i) => (
                                                            <li key={i}>{b}</li>
                                                        ))}
                                                    </ul>
                                                </div>
                                                <div>
                                                    <h4>⚠ Considerations</h4>
                                                    <ul>
                                                        {option.cons.map((c, i) => (
                                                            <li key={i}>{c}</li>
                                                        ))}
                                                    </ul>
                                                </div>
                                            </div>

                                            <button className="btn btn-primary" onClick={(e) => { e.stopPropagation(); handleOptionSelect(option.id) }}>
                                                Select this housing
                                            </button>
                                        </div>
                                    ))}
                                </div>
                            </>
                        ) : null}

                        <div className="button-group">
                            <button
                                onClick={() => {
                                    if (showHousingOptions) {
                                        setSelectedHousingCategory(null)
                                    } else {
                                        setShowSetup(true)
                                        setShowHousingScreen(false)
                                    }
                                }}
                                className="btn btn-secondary"
                            >
                                ← Back
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

    if (loading || (playerId && tutorials.length === 0)) {
        return (
            <div className="onboarding-container">
                <div className="onboarding-modal">
                    <div className="loading">
                        <div className="spinner"></div>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
        )
    }

    const tutorial = tutorials[currentStep]

    return (
        <div className="onboarding-container">
            <div className="onboarding-modal">
                <div className="tutorial-content">
                    <h1>{tutorial.title}</h1>
                    <p className="description">{tutorial.description}</p>
                    {tutorial.action_hint && <p className="hint">{tutorial.action_hint}</p>}
                </div>

                <div className="progress-section">
                    <div className="progress-bar">
                        <div className="progress-fill" style={{ width: `${progress}%` }}></div>
                    </div>
                    <p className="progress-text">
                        {currentStep + 1} of {tutorials.length}
                    </p>
                </div>

                <div className="button-group">
                    <button onClick={handleNext} className="btn btn-primary" disabled={loading}>
                        {loading ? 'Loading...' : currentStep < tutorials.length - 1 ? 'Next' : 'Start Playing'}
                    </button>
                    <button onClick={handleSkip} className="btn btn-secondary" disabled={loading}>
                        Skip Tutorial
                    </button>
                </div>
            </div>
        </div>
    )
}
