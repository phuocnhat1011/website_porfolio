export const expertiseItems = [
  {
    label: 'Multi-Asset Data',
    detail: 'Indices · Equities · Commodities · Futures · Crypto',
  },
  {
    label: 'ETL & Quality',
    detail: 'Automation · Validation · Standardization',
  },
  {
    label: 'SQL & Modeling',
    detail: 'PostgreSQL · Fact/Dimension · Analytical SQL',
  },
  {
    label: 'BI & Analysis',
    detail: 'Power BI · Monitoring · Reporting',
  },
] as const

export const homeProjectContent = {
  marketData: {
    title: 'Vietnam Securities Financial Statements Analytics',
    description:
      'An end-to-end personal project for collecting, standardizing and analyzing financial statements of Vietnamese securities companies using Python, PostgreSQL, SQL and Power BI.',
    tags: ['Python', 'Pandas', 'PostgreSQL', 'SQL', 'Power BI', 'Data Modeling'],
    note: 'Automated workflow covering 37+ Vietnamese securities companies.',
    status: 'Financial Data Analytics',
    cta: 'View Case Study',
  },
  hedging: {
    title: 'VN30F1M Hedging System',
    description:
      'An R-based financial time-series and hedging workflow using backtesting, Grid Search, state-machine logic and SSI FastConnect.',
    tags: ['R', 'Backtesting', 'Grid Search', 'State Machine', 'SSI FastConnect'],
    cta: 'View Technical Project',
  },
} as const
