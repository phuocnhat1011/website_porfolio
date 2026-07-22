import { PowerBIEmbed } from '../components/powerbi/PowerBIEmbed'
import { ProjectPageHeader } from '../components/projects/ProjectPageHeader'
import { ProjectTabs } from '../components/projects/ProjectTabs'
import { getProject } from '../data/projects'
import { securitiesWorkflow } from '../data/securities'
import styles from './ProjectPages.module.css'

function Overview() {
  return (
    <div className={`twoColumn ${styles.overviewCards}`}>
      <article className="card">
        <h2 className={`${styles.cardTitle} ${styles.purpleTitle}`}>🎯 Bối cảnh & Nhiệm vụ (Situation & Task)</h2>
        <p><strong>Bối cảnh:</strong> Danh mục tự doanh (FVTPL, AFS) là “trái tim” trong hiệu quả hoạt động của các công ty chứng khoán, nhưng dữ liệu này hiện rất khó tiếp cận khi nằm rải rác trong hàng trăm trang thuyết minh BCTC dưới dạng PDF. Nhà đầu tư và chuyên viên phân tích thường mất hàng giờ để tổng hợp thủ công mà vẫn thiếu tính đồng nhất để so sánh giữa các công ty.</p>
        <p><strong>Nhiệm vụ:</strong> Xây dựng một Hệ thống chuyên sâu về Phân tích danh mục tự doanh, tự động hóa việc bóc tách dữ liệu từ 3 báo cáo tài chính cốt lõi (CĐKT, KQKD, LCTT) và đặc biệt là chi tiết danh mục FVTPL/AFS của <strong>37+ công ty chứng khoán</strong> niêm yết trên thị trường Việt Nam.</p>
      </article>
      <article className="card">
        <h2 className={`${styles.cardTitle} ${styles.blueTitle}`}>⚡ Hành động & Kết quả (Action & Result)</h2>
        <p><strong>Hành động:</strong></p>
        <ul className={styles.cardList}>
          <li><strong>Targeted Extraction:</strong> Thiết lập quy trình trích xuất chuyên biệt, tập trung bóc tách các danh mục tài sản tài chính (FVTPL, AFS) từ các bảng thuyết minh PDF vốn là “điểm mù” của dữ liệu truyền thống.</li>
          <li><strong>Data Standardization:</strong> Hợp nhất dữ liệu từ <strong>37+ công ty chứng khoán</strong> vào một cấu trúc chung, cho phép so sánh trực tiếp danh mục, tỷ trọng đầu tư và biến động tài sản giữa các đơn vị.</li>
          <li><strong>Modeling & Metrics:</strong> Thiết kế mô hình dữ liệu quan hệ (Star Schema) để tự động hóa các chỉ số tài chính trọng yếu (NIM, ROA, ROE) kết hợp với cấu trúc danh mục đầu tư.</li>
          <li><strong>Visual Insights:</strong> Xây dựng Dashboard Power BI theo phương pháp Menu-driven Design, cho phép người dùng chỉ cần một cú click chuột để “X-ray” toàn bộ danh mục tự doanh của bất kỳ công ty chứng khoán nào.</li>
        </ul>
        <p><strong>Kết quả (Value Delivered):</strong></p>
        <ul className={styles.cardList}>
          <li><strong>Tiết kiệm thời gian:</strong> Chuyển đổi công việc tra cứu thủ công kéo dài hàng giờ thành báo cáo chỉ trong <strong>vài giây</strong>.</li>
          <li><strong>Độ bao phủ:</strong> Dữ liệu chuẩn hóa của <strong>37+ công ty chứng khoán</strong> niêm yết, cung cấp cái nhìn toàn cảnh về khẩu vị đầu tư của toàn ngành.</li>
          <li><strong>Ra quyết định:</strong> Giúp nhà đầu tư nhanh chóng nhận diện các biến động lớn trong danh mục tự doanh, từ đó đưa ra quyết định dựa trên dữ liệu (Data-driven) thay vì cảm tính.</li>
        </ul>
      </article>
    </div>
  )
}

function Workflow() {
  return (
    <section>
      <h2>🔄 Quy trình ETL & Kiến trúc Dữ liệu</h2>
      <p>Sơ đồ quy trình dưới đây mô tả luồng di chuyển dữ liệu từ nguồn thông tin phi cấu trúc, qua pipeline xử lý và lưu trữ dữ liệu tập trung, cho đến lớp biểu diễn trực quan trên Power BI.</p>
      <picture>
        <source srcSet="/images/etl-pipeline.webp" type="image/webp" />
        <img className={styles.diagram} src="/images/etl-pipeline.png" alt="Kiến trúc quy trình ETL tự động hóa dữ liệu BCTC Chứng khoán" width="3079" height="1469" loading="lazy" />
      </picture>
      <p className={styles.caption}>Kiến trúc quy trình ETL tự động hóa dữ liệu BCTC Chứng khoán</p>
      <hr className={styles.divider} />
      <h2 className={styles.workflowHeading}>🔄 PROJECT WORKFLOW</h2>
      <div className={styles.workflow}>
        {securitiesWorkflow.map((step) => (
          <article key={step.number} className={styles.workflowStep}>
            <header className={styles.workflowHeader}>
              <span className={styles.workflowNumber}>{step.number}</span>
              <h3 className={styles.workflowTitle}>{step.title}</h3>
            </header>
            {step.paragraphs.map((paragraph) => <p key={paragraph}>{paragraph}</p>)}
            {step.bullets && <ul>{step.bullets.map((item) => <li key={item}>{item}</li>)}</ul>}
            <div className={styles.toolCallout}><strong>🛠️ Công cụ sử dụng:</strong> {step.tools}</div>
          </article>
        ))}
      </div>
    </section>
  )
}

function SourceAndModel() {
  return (
    <section className={styles.sourceSection}>
      <h2>💻 Source Code & Data Model</h2>
      <p className={styles.sourceIntro}>Toàn bộ mã nguồn, cấu trúc luồng xử lý dữ liệu (ETL) và kịch bản tự động hóa của dự án được quản lý tập trung và phân module chi tiết trên GitHub.</p>
      <button type="button" className={`button buttonSecondary ${styles.sourceAction}`} disabled>💻 Repository — Coming soon</button>
      <hr className={styles.divider} />
      <h2>🏗️ Kiến trúc Dữ liệu (Star Schema)</h2>
      <picture>
        <source srcSet="/images/erd-postgresql.webp" type="image/webp" />
        <img className={styles.diagram} src="/images/erd-postgresql.png" alt="Sơ đồ cơ sở dữ liệu quan hệ (Star Schema)" width="1317" height="1075" loading="lazy" />
      </picture>
      <p className={styles.caption}>Sơ đồ cơ sở dữ liệu quan hệ (Star Schema)</p>
    </section>
  )
}

export default function SecuritiesPage() {
  const project = getProject('securities_vn')
  return (
    <>
      <ProjectPageHeader
        title="📊 Phân tích BCTC Chứng Khoán Việt Nam"
        description="Hệ thống thu thập và phân tích tự động Báo cáo tài chính (BCTC) ngành chứng khoán Việt Nam. Dự án giải quyết bài toán đồng nhất dữ liệu tài chính đa chiều, tự động hóa luồng xử lý và trực quan hóa các chỉ số tài chính trọng yếu phục vụ hoạt động theo dõi và đánh giá danh mục tự doanh (FVTPL, AFS)."
      />
      <ProjectTabs
        label="Chi tiết dự án BCTC Chứng khoán Việt Nam"
        tabs={[
          { id: 'overview', label: 'Tổng quan', content: <Overview /> },
          { id: 'workflow', label: 'Quy trình', content: <Workflow /> },
          { id: 'source', label: 'Source Code & Data Model', content: <SourceAndModel /> },
          { id: 'powerbi', label: 'Power BI', content: <PowerBIEmbed title="Power BI — Phân tích BCTC Chứng khoán Việt Nam" embedUrl={project.powerBiUrl ?? ''} /> },
        ]}
      />
    </>
  )
}
