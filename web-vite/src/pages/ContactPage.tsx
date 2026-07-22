import { siteConfig } from '../config/site'
import { skillGroups } from '../data/skills'
import styles from './ContentPages.module.css'

export default function ContactPage() {
  return (
    <>
      <header className={styles.header}>
        <h1>👤 Thông Tin Liên Hệ & Kỹ Năng</h1>
        <p>Kết nối với mình hoặc tìm hiểu thêm về các công nghệ mình đang sử dụng.</p>
      </header>
      <div className={styles.contactGrid}>
        <section>
          <h2 className={styles.contactHeading}>✉️ Thông Tin Liên Hệ</h2>
          <article className={`card ${styles.contactCard}`}>
            <ul className={styles.contactList}>
              <li>💡 <strong>Họ và tên:</strong> Võ Phước Nhật</li>
              <li>📧 <strong>Email:</strong> <a href={`mailto:${siteConfig.email}`}>{siteConfig.email}</a></li>
              <li>🔗 <strong>LinkedIn:</strong> <a href={siteConfig.linkedinUrl} target="_blank" rel="noopener noreferrer">linkedin.com/in/phuocnhat1011</a></li>
              <li>🐙 <strong>GitHub:</strong> <a href={siteConfig.githubUrl} target="_blank" rel="noopener noreferrer">github.com/phuocnhat1011</a></li>
            </ul>
          </article>
          <div className={styles.downloadBlock}>
            <h3>Tải Hồ Sơ Năng Lực (CV)</h3>
            <a className="button buttonPrimary" href={siteConfig.cvUrl} download="Vo-Phuoc-Nhat-CV.pdf">📥 Tải bản CV đầy đủ (PDF)</a>
          </div>
        </section>
        <section>
          <h2 className={styles.contactHeading}>🛠️ Bản Đồ Kỹ Năng (Skills)</h2>
          {skillGroups.map((group) => (
            <article key={group.title} className={`card ${styles.skillCard}`}>
              <h3>{group.icon} {group.title}</h3>
              <div className={styles.skillList}>{group.skills.map((skill) => <span key={skill} className="badge">{skill}</span>)}</div>
            </article>
          ))}
        </section>
      </div>
    </>
  )
}
