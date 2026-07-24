import { lazy, Suspense } from 'react'
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import { AppLayout } from './components/layout/AppLayout'

const HomePage = lazy(() => import('./pages/HomePage'))
const MarketOverviewPage = lazy(() => import('./pages/MarketOverviewPage'))
const SecuritiesPage = lazy(() => import('./pages/SecuritiesPage'))
const HedgingPage = lazy(() => import('./pages/HedgingPage'))
const BankProjectPage = lazy(() => import('./pages/BankProjectPage'))
const KnowledgePage = lazy(() => import('./pages/KnowledgePage'))
const ContactPage = lazy(() => import('./pages/ContactPage'))

function PageLoading() {
  return <div className="surface" style={{ minHeight: 240, display: 'grid', placeItems: 'center', color: '#64748b' }} role="status">Đang tải nội dung…</div>
}

export default function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<PageLoading />}>
        <Routes>
          <Route element={<AppLayout />}>
            <Route index element={<HomePage />} />
            <Route path="market-overview" element={<MarketOverviewPage />} />
            <Route path="projects/securities" element={<SecuritiesPage />} />
            <Route path="projects/hedging" element={<HedgingPage />} />
            <Route path="projects/banking" element={<BankProjectPage />} />
            <Route path="knowledge" element={<KnowledgePage />} />
            <Route path="contact" element={<ContactPage />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Route>
        </Routes>
      </Suspense>
    </BrowserRouter>
  )
}
