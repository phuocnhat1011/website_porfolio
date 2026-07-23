import { expertiseItems } from '../../data/home'
import styles from './HomeSections.module.css'

export function ExpertiseStrip() {
  return (
    <section className={`${styles.expertiseStrip} surface`} aria-labelledby="expertise-heading">
      <h2 id="expertise-heading" className="sr-only">Core expertise</h2>
      {expertiseItems.map((item) => (
        <article className={styles.expertiseItem} key={item.label}>
          <strong>{item.label}</strong>
          <p>{item.detail}</p>
        </article>
      ))}
    </section>
  )
}
