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
    title: 'Vietnam Market Data Warehouse',
    description:
      'An end-to-end personal project for Vietnam’s listed equity market, combining automated data collection, dimensional modeling, PostgreSQL, SQL analysis and Power BI reporting.',
    tags: ['Python', 'PostgreSQL', 'SQL', 'Power BI', 'Data Modeling', 'Market Data'],
    note: 'Designed for HOSE, HNX and UPCOM coverage.',
    status: 'In development',
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
