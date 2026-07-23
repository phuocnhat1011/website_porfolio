import { siteConfig } from '../../config/site'
import styles from './HomeSections.module.css'

const tools = ['R', 'Python', 'SQL', 'PostgreSQL', 'Power BI'] as const

export function HeroSection() {
  return (
    <section className={`${styles.hero} surface`} aria-labelledby="home-title">
      <div className={styles.heroCopy}>
        <p className={styles.eyebrow}>Financial Data Analyst · Market Data</p>
        <h1 id="home-title">Võ Phước Nhật</h1>
        <p className={styles.heroLead}>
          Financial Data Analyst with 2 years of experience in multi-asset financial market data,
          specializing in data automation, financial time-series processing, data quality validation,
          and analytical workflows.
        </p>

        <div className={styles.heroHighlights}>
          <p>
            <span>Professional experience</span>{' '}
            Across global indices, equities, commodities, futures and crypto assets.
          </p>
          <p>
            <span>Personal project</span>{' '}
            Built an end-to-end financial statements analytics workflow for Vietnamese securities companies.
          </p>
        </div>

        <div className={styles.techChips} aria-label="Core technology stack">
          {tools.map((tool) => <span key={tool}>{tool}</span>)}
        </div>

        <div className={styles.heroActions}>
          <a className="button buttonPrimary" href="#featured-projects">View Projects</a>
          <a className="button buttonSecondary" href={siteConfig.cvUrl} download="Vo-Phuoc-Nhat-CV.pdf">
            Download CV
          </a>
          <a className={styles.contactLink} href="#contact">Contact me →</a>
        </div>
      </div>

      <div className={styles.avatarRing}>
        <picture>
          <source srcSet="/images/avatar.webp" type="image/webp" />
          <img
            src="/images/avatar.jpg"
            alt="Portrait of Võ Phước Nhật"
            width="2048"
            height="2048"
            fetchPriority="high"
          />
        </picture>
      </div>
    </section>
  )
}
