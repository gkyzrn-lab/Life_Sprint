/**
 * BitLife-Style Visual Components for Life Sprint
 * 
 * This module exports all the visual components needed to create a BitLife-like interface
 * for the Life Sprint financial education game.
 * 
 * Components:
 * - GameLayout: Main container component with three-column layout
 * - CharacterCard: Character stats and profile display
 * - AgeProgression: Timeline and life stage indicator
 * - FinancialDashboard: Money, assets, and financial overview
 * - LifeTimeline: Event history and milestone tracker
 * - DecisionCard: Choice presentation and decision-making interface
 * - BadgesPanel: Achievement badges tracker
 * - QuestsPanel: Quest objectives and progress
 */

export { GameLayout } from './GameLayout'
export { CharacterCard } from './CharacterCard'
export { AgeProgression } from './AgeProgression'
export { FinancialDashboard } from './FinancialDashboard'
export { LifeTimeline } from './LifeTimeline'
export { DecisionCard } from './DecisionCard'
export { BadgesPanel } from './BadgesPanel'
export { QuestsPanel } from './QuestsPanel'

// Type exports for components
export type { CharacterCardProps, CharacterStats } from './CharacterCard'
export type { DecisionCardProps, DecisionOption } from './DecisionCard'
export type { AgeProgressionProps } from './AgeProgression'
export type { FinancialDashboardProps, FinancialData } from './FinancialDashboard'
export type { LifeTimelineProps, LifeEvent } from './LifeTimeline'
export type { GameLayoutProps } from './GameLayout'
export type { Badge, BadgesPanelProps } from './BadgesPanel'
export type { Quest, QuestsPanelProps } from './QuestsPanel'
