import { Link } from 'react-router-dom'
import { homeProjectContent } from '../../data/home'
import { getProject } from '../../data/projects'
import styles from './HomeSections.module.css'

const marketDataProject = getProject('securities_vn')
const hedgingProject = getProject('hedging_vn30f1m')

export function FeaturedProjectsSection() {
  return (
    <section id="featured-projects" className={styles.featured} aria-labelledby="featured-heading">
      <div className={styles.sectionHeading}>
        <p>Selected work</p>
        <h2 id="featured-heading">Featured Projects</h2>
      </div>

      <div className={styles.projectGrid}>
        <article className={`${styles.projectCard} ${styles.flagshipCard} surface`}>
          <picture className={styles.projectCover}>
            <source srcSet="/images/data-model.webp" type="image/webp" />
            <img
              src="/images/data-model.png"
              alt="Data model for Vietnam Securities Financial Statements Analytics"
              loading="lazy"
              width="1592"
              height="754"
            />
          </picture>
          <div className={styles.projectBody}>
            <div className={styles.projectTitleRow}>
              <h3>{homeProjectContent.marketData.title}</h3>
              <span className={styles.statusBadge}>{homeProjectContent.marketData.status}</span>
            </div>
            <p className={styles.projectDescription}>{homeProjectContent.marketData.description}</p>
            <div className={styles.projectTags} aria-label="Vietnam Securities Financial Statements Analytics technology stack">
              {homeProjectContent.marketData.tags.map((tag) => <span key={tag}>{tag}</span>)}
            </div>
            <p className={styles.projectNote}>{homeProjectContent.marketData.note}</p>
            <Link className="button buttonPrimary" to={marketDataProject.route}>
              {homeProjectContent.marketData.cta}
            </Link>
          </div>
        </article>

        <article className={`${styles.projectCard} surface`}>
          <picture className={styles.projectCover}>
            <source srcSet={hedgingProject.cover} type="image/webp" />
            <img
              src={hedgingProject.coverOriginal}
              alt="Preview of the VN30F1M hedging and monitoring project"
              loading="lazy"
              width="1592"
              height="754"
            />
          </picture>
          <div className={styles.projectBody}>
            <div className={styles.projectTitleRow}>
              <h3>{homeProjectContent.hedging.title}</h3>
            </div>
            <p className={styles.projectDescription}>{homeProjectContent.hedging.description}</p>
            <div className={styles.projectTags} aria-label="VN30F1M Hedging System technology stack">
              {homeProjectContent.hedging.tags.map((tag) => <span key={tag}>{tag}</span>)}
            </div>
            <Link className="button buttonSecondary" to={hedgingProject.route}>
              {homeProjectContent.hedging.cta}
            </Link>
          </div>
        </article>
      </div>
    </section>
  )
}
