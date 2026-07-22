import type { SkillGroup } from '../types'

export const skillGroups: SkillGroup[] = [
  {
    title: 'Data Analytics & Visualization',
    icon: '📊',
    skills: ['Power BI', 'DAX', 'Power Query', 'Data Modeling', 'Dashboard UX/UI'],
  },
  {
    title: 'Programming & Automation',
    icon: '💻',
    skills: ['Python', 'SQL', 'R', 'Pandas / NumPy', 'LangChain (RAG)', 'Git / GitHub'],
  },
  {
    title: 'Finance & Domain Knowledge',
    icon: '🏦',
    skills: ['Financial Statements Analysis', 'Banking Metrics (NIM, NPL, CAR)', 'Securities Portfolios (FVTPL, AFS, HTM)'],
  },
  {
    title: 'Platforms & Databases',
    icon: '📦',
    skills: ['PostgreSQL', 'Snowflake', 'Excel (Advanced)', 'Docker'],
  },
]
