import { NavLink } from 'react-router-dom'
import { navigation } from '../../config/site'
import styles from './SidebarNavigation.module.css'

interface SidebarNavigationProps {
  mobile?: boolean
  onNavigate?: () => void
}

export function SidebarNavigation({ mobile = false, onNavigate }: SidebarNavigationProps) {
  return (
    <nav className={`${styles.navigation} ${mobile ? styles.mobile : ''}`} aria-label="Điều hướng chính">
      <div className={styles.brand} aria-label="Võ Phước Nhật portfolio">
        <span className={styles.brandMark}>VN</span>
        <span>
          <strong>Võ Phước Nhật</strong>
          <small>Portfolio</small>
        </span>
      </div>

      <ul className={styles.menu}>
        {navigation.map((item) => (
          <li key={item.label}>
            {item.to ? (
              <NavLink
                to={item.to}
                end={item.to === '/'}
                className={({ isActive }) => `${styles.menuLink} ${isActive ? styles.active : ''}`}
                onClick={onNavigate}
              >
                <span aria-hidden="true">{item.icon}</span>
                {item.label}
              </NavLink>
            ) : (
              <>
                <div className={styles.groupLabel}>
                  <span aria-hidden="true">{item.icon}</span>
                  {item.label}
                </div>
                <ul className={styles.submenu}>
                  {item.children?.map((child) => (
                    <li key={child.label}>
                      <NavLink
                        to={child.to ?? '/'}
                        className={({ isActive }) => `${styles.submenuLink} ${isActive ? styles.active : ''}`}
                        onClick={onNavigate}
                      >
                        <span aria-hidden="true">{child.icon}</span>
                        {child.label}
                      </NavLink>
                    </li>
                  ))}
                </ul>
              </>
            )}
          </li>
        ))}
      </ul>
    </nav>
  )
}
