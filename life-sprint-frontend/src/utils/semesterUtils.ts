/**
 * Semester and calendar utilities for Life Sprint
 * Academic calendar starts in August and follows typical US college schedule
 */

export interface SemesterInfo {
    semester: number
    academicYear: number
    period: 'Fall' | 'Spring' | 'Summer'
    startDate: Date
    endDate: Date
    displayName: string
    monthRange: string
    status: 'active' | 'break' | 'work-period'
}

/**
 * Calculate the academic year and semester info given a semester number
 * Semester 1 = Fall (Aug-Dec), Semester 2 = Spring (Jan-May), etc.
 */
export function getSemesterInfo(semesterNumber: number, startYear: number = 2024): SemesterInfo {
    // Each academic year has 2 semesters: Fall + Spring
    const yearsSinceStart = Math.floor((semesterNumber - 1) / 2)
    const semesterInYear = ((semesterNumber - 1) % 2) + 1 // 1 or 2
    const academicYear = startYear + yearsSinceStart

    let period: 'Fall' | 'Spring' | 'Summer'
    let startDate: Date
    let endDate: Date
    let monthRange: string

    if (semesterInYear === 1) {
        // Fall semester: August to December
        period = 'Fall'
        startDate = new Date(academicYear, 7, 1) // August 1st
        endDate = new Date(academicYear, 11, 15) // Mid December
        monthRange = 'August - Mid December'
    } else {
        // Spring semester: January to May
        period = 'Spring'
        startDate = new Date(academicYear, 0, 15) // Mid January
        endDate = new Date(academicYear, 4, 31) // End of May
        monthRange = 'Mid January - End of May'
    }

    return {
        semester: semesterNumber,
        academicYear,
        period,
        startDate,
        endDate,
        displayName: `${period} ${academicYear}`,
        monthRange,
        status: 'active'
    }
}

/**
 * Get current phase information (class period, break, or work period)
 */
export function getCurrentPhase(
    semesterNumber: number,
    dayOfSemester: number = 1,
    startYear: number = 2024
): {
    phase: 'classes' | 'winter-break' | 'summer-break' | 'internship-period'
    description: string
    canAttendClasses: boolean
    canWork: boolean
} {
    const semesterInfo = getSemesterInfo(semesterNumber, startYear)
    const daysInSemester = Math.floor((semesterInfo.endDate.getTime() - semesterInfo.startDate.getTime()) / (1000 * 60 * 60 * 24))

    if (semesterInfo.period === 'Fall') {
        // Fall: Classes Aug 1 - Dec 15
        if (dayOfSemester <= daysInSemester) {
            return {
                phase: 'classes',
                description: 'Active classes - Focus on your coursework!',
                canAttendClasses: true,
                canWork: true // Part-time work is allowed
            }
        }
    } else {
        // Spring: Classes Jan 15 - May 31
        if (dayOfSemester <= daysInSemester - 15) {
            // Before mid-May
            return {
                phase: 'classes',
                description: 'Active classes - Focus on your coursework!',
                canAttendClasses: true,
                canWork: true
            }
        } else {
            // Mid-May to end of May: Internship/work period
            return {
                phase: 'internship-period',
                description: 'Summer break approaching! Ideal for internships, work, or skill development.',
                canAttendClasses: false,
                canWork: true
            }
        }
    }

    // Winter break (mid-Dec to mid-Jan between semesters)
    if (semesterInfo.period === 'Fall' && dayOfSemester > daysInSemester) {
        return {
            phase: 'winter-break',
            description: 'Winter break! Take time to relax or work on projects.',
            canAttendClasses: false,
            canWork: true
        }
    }

    return {
        phase: 'summer-break',
        description: 'Summer break! Perfect for internships, jobs, or skill development.',
        canAttendClasses: false,
        canWork: true
    }
}

/**
 * Format semester display with both number and dates
 */
export function formatSemesterDisplay(semesterNumber: number, startYear: number = 2024): string {
    const info = getSemesterInfo(semesterNumber, startYear)
    return `${info.displayName} (${info.monthRange})`
}

/**
 * Get all remaining semesters in the current academic year
 */
export function getRemainingSemestersInYear(
    currentSemester: number,
    startYear: number = 2024
): SemesterInfo[] {
    const semesterInfo = getSemesterInfo(currentSemester, startYear)
    const remaining: SemesterInfo[] = []

    // If in fall, next semester is spring of same year
    if (semesterInfo.period === 'Fall') {
        remaining.push(getSemesterInfo(currentSemester + 1, startYear))
    }

    return remaining
}
