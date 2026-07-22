import { useEffect, useState } from 'react'
import { Outlet, useLocation } from 'react-router-dom'
import { SidebarNavigation } from '../navigation/SidebarNavigation'
import styles from './AppLayout.module.css'

export function AppLayout() {
  const [menuOpen, setMenuOpen] = useState(false)
  const location = useLocation()

  useEffect(() => {
    setMenuOpen(false)
    window.scrollTo({ top: 0, behavior: 'auto' })
  }, [location.pathname])

  useEffect(() => {
    document.body.style.overflow = menuOpen ? 'hidden' : ''
    return () => { document.body.style.overflow = '' }
  }, [menuOpen])

  return (
    <div className={styles.appShell}>
      <a className="skip-link" href="#main-content">Bỏ qua điều hướng</a>

      <aside className={styles.sidebar}>
        <SidebarNavigation />
      </aside>

      <header className={styles.mobileHeader}>
        <div className={styles.mobileBrand}>
          <span>VN</span>
          <strong>Võ Phước Nhật</strong>
        </div>
        <button
          type="button"
          className={styles.menuToggle}
          aria-expanded={menuOpen}
          aria-controls="mobile-navigation"
          aria-label={menuOpen ? 'Đóng menu' : 'Mở menu'}
          onClick={() => setMenuOpen((open) => !open)}
        >
          <span /><span /><span />
        </button>
      </header>

      {menuOpen && (
        <div className={styles.mobileOverlay} onClick={() => setMenuOpen(false)}>
          <div id="mobile-navigation" className={styles.mobileDrawer} onClick={(event) => event.stopPropagation()}>
            <SidebarNavigation mobile onNavigate={() => setMenuOpen(false)} />
          </div>
        </div>
      )}

      <main id="main-content" className={styles.main} tabIndex={-1}>
        <div className={styles.content}>
          <Outlet />
        </div>
      </main>
    </div>
  )
}
