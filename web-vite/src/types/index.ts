export interface Project {
  id: 'bank_bctc' | 'securities_vn' | 'hedging_vn30f1m'
  title: string
  status: 'DOING' | 'DONE'
  tagline: string
  stack: string[]
  highlights: string[]
  whatIDid: string[]
  process: string[]
  cover: string
  coverOriginal: string
  route: string
  powerBiUrl?: string
  githubUrl?: string
  visibleOnHome: boolean
  visibleInNavigation: boolean
}

export interface NavigationItem {
  label: string
  icon: string
  to?: string
  children?: NavigationItem[]
}

export interface SkillGroup {
  title: string
  icon: string
  skills: string[]
}

export type BacktestRow = [
  spreadIn: number,
  streakIn: number,
  spreadOut: number,
  streakOut: number,
  nbExcept: number,
  takeProfit: number,
  nbTrades: number,
  winRate: number,
  avgPnl: number,
  totalPnl: number,
]

export interface BacktestDataset {
  columns: string[]
  rows: BacktestRow[]
}
