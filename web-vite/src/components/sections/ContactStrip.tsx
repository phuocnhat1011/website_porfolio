import { siteConfig } from '../../config/site'
import styles from './HomeSections.module.css'

export function ContactStrip() {
  return (
    <section id="contact" className={`${styles.contactStrip} surface`} aria-labelledby="contact-heading">
      <h2 id="contact-heading">
        Open to Financial Data Analyst, Market Data Analyst and Investment Data Analyst opportunities.
      </h2>
      <nav className={styles.contactActions} aria-label="Contact links">
        <a href={`mailto:${siteConfig.email}`}>Email</a>
        <a href={siteConfig.linkedinUrl} target="_blank" rel="noopener noreferrer">LinkedIn</a>
        <a href={siteConfig.githubUrl} target="_blank" rel="noopener noreferrer">GitHub</a>
      </nav>
    </section>
  )
}
