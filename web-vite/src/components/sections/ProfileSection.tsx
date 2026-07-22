import { siteConfig } from '../../config/site'
import styles from './HomeSections.module.css'

export function ProfileSection() {
  return (
    <section className={styles.profileGrid} aria-labelledby="profile-heading">
      <div>
        <h2 id="profile-heading" className={styles.subsectionTitle}>Hồ Sơ Cá Nhân</h2>
        <blockquote className={styles.profileQuote}>
          “Xuất phát từ nền tảng tài chính, tôi chuyển hướng sang kỹ thuật dữ liệu vì nhận ra rằng dữ liệu tốt mới tạo ra quyết định tốt. Tôi thích giải quyết những bài toán thực tế — lấy dữ liệu lộn xộn, làm sạch, mô hình hóa và biến nó thành thứ người dùng có thể đọc và hiểu ngay.”
        </blockquote>
        <a className="button buttonPrimary" href={siteConfig.cvUrl} download="Vo-Phuoc-Nhat-CV.pdf">📥 Tải bản CV đầy đủ (PDF)</a>
      </div>
      <StrengthsSection />
    </section>
  )
}

export function StrengthsSection() {
  const strengths = [
    ['📊', 'Data & BI Solutions', 'Dashboard BCTC & danh mục tự doanh trực quan.'],
    ['🧠', 'Data Modeling', 'Star Schema & DAX measures cho chỉ số tài chính.'],
    ['⚙️', 'Automation & Pipeline', 'ETL tự động: SSI/PDF → PostgreSQL → Power BI.'],
  ] as const

  return (
    <div>
      <h2 className={styles.subsectionTitle}>Thế Mạnh Chuyên Môn</h2>
      <div className={styles.strengthGrid}>
        {strengths.map(([icon, title, description]) => (
          <article key={title} className={`${styles.strengthCard} surface`}>
            <span className={styles.strengthIcon} aria-hidden="true">{icon}</span>
            <strong>{title}</strong>
            <p>{description}</p>
          </article>
        ))}
      </div>
    </div>
  )
}
