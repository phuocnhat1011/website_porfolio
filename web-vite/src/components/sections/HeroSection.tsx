import styles from './HomeSections.module.css'

const specialties = ['Data Analytics', 'Financial Analysis', 'Automation Pipeline', 'R & Python', 'Power BI & DAX']

export function HeroSection() {
  return (
    <section className={`${styles.hero} surface`} aria-labelledby="home-title">
      <div className={styles.heroCopy}>
        <h1 id="home-title">👋 Võ Phước Nhật</h1>
        <p className={styles.heroLead}>
          Phát triển giải pháp dữ liệu và báo cáo tự động cho lĩnh vực <strong>Tài chính & Chứng khoán</strong>. Tập trung vào <strong>Financial Data Engineering</strong>, <strong>Algo Trading</strong> và tự động hóa pipeline dữ liệu cho thị trường chứng khoán Việt Nam.
        </p>
        <div className={styles.badges} aria-label="Chuyên môn chính">
          {specialties.map((item) => <span key={item} className="badge">{item}</span>)}
        </div>
      </div>
      <div className={styles.avatarRing}>
        <picture>
          <source srcSet="/images/avatar.webp" type="image/webp" />
          <img src="/images/avatar.jpg" alt="Ảnh Võ Phước Nhật" width="2048" height="2048" fetchPriority="high" />
        </picture>
      </div>
    </section>
  )
}
