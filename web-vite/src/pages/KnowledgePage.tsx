import { knowledgeArticles, knowledgeTips } from '../data/knowledge'
import styles from './ContentPages.module.css'

export default function KnowledgePage() {
  return (
    <>
      <header className={styles.header}>
        <h1>🧠 Góc Chia Sẻ Kiến Thức</h1>
        <p>Kinh nghiệm thực tế, mẹo lập trình và các bài viết sâu về phân tích dữ liệu tài chính & tối ưu hóa Power BI.</p>
      </header>
      <div className={styles.knowledgeGrid}>
        <section>
          <h2 className={styles.columnHeading}>💡 Tips Ngắn & Thủ Thuật</h2>
          {knowledgeTips.map((tip) => (
            <article key={tip.title} className={`card ${styles.contentCard}`}>
              <h3>{tip.title}</h3>
              <p>{tip.description}</p>
              {tip.code && <pre className="codeBlock"><code>{tip.code}</code></pre>}
            </article>
          ))}
        </section>
        <section>
          <h2 className={`${styles.columnHeading} ${styles.blue}`}>📚 Bài Viết Phân Tích Sâu</h2>
          {knowledgeArticles.map((article) => (
            <article key={article.title} className={`card ${styles.contentCard}`}>
              <h3>{article.title}</h3>
              <p className={styles.meta}>{article.meta}</p>
              <p>{article.description}</p>
            </article>
          ))}
        </section>
      </div>
    </>
  )
}
