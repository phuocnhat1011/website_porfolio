import type { NavigationItem } from '../types'
import { marketOverviewProject } from '../data/marketOverview'

export const siteConfig = {
  name: 'Võ Phước Nhật',
  title: 'Võ Phước Nhật | Portfolio',
  canonicalUrl: 'https://phuocnhat.dev',
  email: 'nhat.vophuoc@gmail.com',
  linkedinUrl: 'https://linkedin.com/in/phuocnhat1011',
  githubUrl: 'https://github.com/phuocnhat1011',
  cvUrl: '/documents/Vo-Phuoc-Nhat-CV.pdf',
} as const

export const navigation: NavigationItem[] = [
  { label: 'Home', icon: '🏠', to: '/' },
  {
    label: 'Projects',
    icon: '📁',
    children: [
      { label: 'Market Overview', icon: '🌐', to: marketOverviewProject.route },
      { label: 'BCTC Chứng Khoán VN', icon: '📊', to: '/projects/securities' },
      { label: 'Hedging VN30F1M', icon: '📈', to: '/projects/hedging' },
    ],
  },
]

export const dormantRoutes = {
  banking: '/projects/banking',
  knowledge: '/knowledge',
  contact: '/contact',
} as const
