import { PowerBIEmbed } from '../components/powerbi/PowerBIEmbed'
import { ProjectPageHeader } from '../components/projects/ProjectPageHeader'
import { ProjectTabs } from '../components/projects/ProjectTabs'
import { getProject } from '../data/projects'
import styles from './ProjectPages.module.css'

function Overview() {
  return (
    <div className={`twoColumn ${styles.overviewCards}`}>
      <article className="card">
        <h2 className={`${styles.cardTitle} ${styles.purpleTitle}`}>🎯 Bối cảnh & Nhiệm vụ (STAR)</h2>
        <p><strong>Situation (Bối cảnh):</strong> Báo cáo tài chính của các ngân hàng thương mại Việt Nam có tính chất đặc thù rất cao (thu nhập lãi thuần, NIM, tỷ lệ nợ xấu NPL...) và thường được phân tán trên nhiều nguồn khác nhau dưới dạng PDF quét. Việc tổng hợp dữ liệu, tính toán các chỉ số an toàn vốn và phân tích cơ cấu tài sản sinh lời thủ công tốn rất nhiều thời gian và dễ sai sót.</p>
        <p><strong>Task (Nhiệm vụ):</strong> Xây dựng giải pháp tự động hóa thu thập và chuẩn hóa dữ liệu tài chính cho nhóm các ngân hàng lớn toàn thị trường, giúp chuyển đổi nhanh dữ liệu thô sang Star Schema để tính toán tức thời các chỉ số tài chính.</p>
      </article>
      <article className="card">
        <h2 className={`${styles.cardTitle} ${styles.blueTitle}`}>⚡ Hành động & Kết quả</h2>
        <p><strong>Action (Hành động):</strong></p>
        <ul className={styles.cardList}>
          <li>Xây dựng pipeline Python tự động thu thập và chuẩn hóa dữ liệu BCTC ngân hàng theo kỳ hạn.</li>
          <li>Thiết kế mô hình dữ liệu quan hệ tối ưu Star Schema phân bổ theo kỳ hạn và nhóm nợ.</li>
          <li>Phát triển hệ thống các measures DAX phức tạp để tính toán chỉ số NIM, tỷ lệ nợ xấu, và biên lợi nhuận lãi thuần.</li>
          <li>Thiết kế giao diện dashboard Power BI trực quan dựa trên phương pháp định hướng module.</li>
        </ul>
        <p><strong>Result (Kết quả):</strong></p>
        <ul className={styles.cardList}>
          <li>Tự động hóa hoàn toàn quy trình xử lý dữ liệu tài chính ngân hàng, giúp <strong>tiết kiệm 2 giờ</strong> làm việc mỗi ngày.</li>
          <li>Độ chính xác chuẩn hóa đạt <strong>99.9%</strong>.</li>
          <li>Cung cấp cái nhìn toàn diện về sức khỏe tài chính của các ngân hàng chỉ trong <strong>vài giây</strong>.</li>
        </ul>
      </article>
    </div>
  )
}

function Workflow() {
  return (
    <section>
      <h2>🔄 Quy trình ETL & Kiến trúc Dữ liệu Ngân hàng</h2>
      <p>Sơ đồ quy trình mô tả luồng di chuyển dữ liệu từ nguồn thông tin phi cấu trúc, qua pipeline xử lý và lưu trữ dữ liệu tập trung, cho đến lớp biểu diễn trực quan trên Power BI.</p>
      <picture>
        <source srcSet="/images/etl-pipeline.webp" type="image/webp" />
        <img className={styles.diagram} src="/images/etl-pipeline.png" alt="Kiến trúc quy trình ETL tự động hóa dữ liệu BCTC Ngân hàng" width="3079" height="1469" loading="lazy" />
      </picture>
      <p className={styles.caption}>Kiến trúc quy trình ETL tự động hóa dữ liệu BCTC Ngân hàng</p>
    </section>
  )
}

function Source() {
  return (
    <section>
      <h2>💻 Mã nguồn Kỹ thuật Tiêu biểu (Ngân hàng)</h2>
      <div className={styles.toolCallout}><strong>Python</strong> — Chuẩn hóa dữ liệu BCTC Ngân hàng</div>
      <pre className="codeBlock"><code>{`# File python xử lý làm sạch và chuyển đổi cấu trúc BCTC ngân hàng (tương tự chứng khoán)\ndef clean_and_normalize_banking_financials(raw_data_list):\n    # Code xử lý đặc thù cho các chỉ tiêu BCTC ngân hàng\n    pass`}</code></pre>
    </section>
  )
}

export default function BankProjectPage() {
  const project = getProject('bank_bctc')
  return (
    <>
      <ProjectPageHeader
        title="🏦 Phân tích BCTC Ngân Hàng Việt Nam"
        description="Hệ thống thu thập và phân tích tự động Báo cáo tài chính (BCTC) ngành ngân hàng thương mại Việt Nam. Dự án giải quyết bài toán đồng nhất dữ liệu tài chính đa nguồn, tự động hóa luồng xử lý và trực quan hóa các chỉ số tài chính đặc thù của ngân hàng như NIM, nợ xấu (NPL), và cơ cấu tài sản sinh lời."
      />
      <ProjectTabs
        label="Chi tiết dự án BCTC Ngân hàng"
        tabs={[
          { id: 'overview', label: 'Tổng quan', content: <Overview /> },
          { id: 'workflow', label: 'Quy trình', content: <Workflow /> },
          { id: 'source', label: 'Source Code & Data Model', content: <Source /> },
          { id: 'powerbi', label: 'Power BI', content: <PowerBIEmbed title="Power BI — Phân tích BCTC Ngân hàng Việt Nam" embedUrl={project.powerBiUrl ?? ''} /> },
        ]}
      />
    </>
  )
}
