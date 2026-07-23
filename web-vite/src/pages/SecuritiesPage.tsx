import { PowerBIEmbed } from '../components/powerbi/PowerBIEmbed'
import { ProjectTabs } from '../components/projects/ProjectTabs'
import { getProject } from '../data/projects'
import {
  architectureGroups,
  powerBiCapabilities,
  securitiesMetrics,
  securitiesOverview,
  securitiesTechnologies,
  securitiesWorkflow,
  verifiedQualityControls,
} from '../data/securities'
import styles from './SecuritiesPage.module.css'

function CaseStudyHeader() {
  return (
    <header className={`${styles.caseHeader} surface`}>
      <p className={styles.eyebrow}>Personal Project · Financial Data Analytics</p>
      <h1>Phân tích BCTC ngành Chứng khoán Việt Nam</h1>
      <p className={styles.englishTitle}>Vietnam Securities Financial Statements Analytics</p>
      <p className={styles.description}>
        Hệ thống tự động thu thập, chuẩn hóa và phân tích báo cáo tài chính của các công ty chứng khoán
        Việt Nam, từ dữ liệu nguồn đến mô hình PostgreSQL và báo cáo Power BI.
      </p>

      <div className={styles.techChips} aria-label="Công nghệ sử dụng">
        {securitiesTechnologies.map((technology) => <span key={technology}>{technology}</span>)}
      </div>

      <dl className={styles.metrics} aria-label="Quy mô dự án">
        {securitiesMetrics.map((metric) => (
          <div key={metric.label} className={styles.metric}>
            <dt>
              <strong>{metric.value}</strong>
              <span>{metric.label}</span>
            </dt>
            <dd>{metric.detail}</dd>
          </div>
        ))}
      </dl>
    </header>
  )
}

function Overview() {
  return (
    <section className={styles.caseSection} aria-labelledby="overview-heading">
      <div className={styles.sectionHeading}>
        <p>TỔNG QUAN DỰ ÁN</p>
        <h2 id="overview-heading">Từ dữ liệu phân tán đến nguồn phân tích nhất quán</h2>
      </div>

      <div className={styles.problemGrid}>
        <article className={styles.contextCard}>
          <span className={styles.cardIndex}>01</span>
          <h3>Bài toán</h3>
          <p>{securitiesOverview.problem}</p>
        </article>
        <article className={styles.contextCard}>
          <span className={styles.cardIndex}>02</span>
          <h3>Mục tiêu</h3>
          <p>{securitiesOverview.objective}</p>
        </article>
      </div>

      <div className={styles.contentBlock}>
        <h3>Giải pháp đã xây dựng</h3>
        <div className={styles.builtGrid}>
          {securitiesOverview.whatBuilt.map((item, index) => (
            <article key={item.title} className={styles.compactCard}>
              <span className={styles.compactNumber}>{String(index + 1).padStart(2, '0')}</span>
              <h4>{item.title}</h4>
              <p>{item.description}</p>
            </article>
          ))}
        </div>
      </div>

      <div className={styles.contentBlock}>
        <h3>Giá trị phân tích</h3>
        <div className={styles.valueGrid}>
          {securitiesOverview.businessValue.map((item) => (
            <article key={item.title} className={styles.valueCard}>
              <h4>{item.title}</h4>
              <p>{item.description}</p>
            </article>
          ))}
        </div>
      </div>

      <div className={styles.contentBlock}>
        <h3>Luồng xử lý tổng quan</h3>
        <ol className={styles.pipelineSummary} aria-label="Luồng xử lý dữ liệu tổng quan">
          {securitiesOverview.pipeline.map((step) => <li key={step}>{step}</li>)}
        </ol>
      </div>
    </section>
  )
}

function Workflow() {
  return (
    <section className={styles.caseSection} aria-labelledby="workflow-heading">
      <div className={styles.sectionHeading}>
        <p>Data workflow</p>
        <h2 id="workflow-heading">Quy trình dữ liệu</h2>
        <span>
          Dữ liệu đi theo thứ tự từ thu thập, trích xuất và kiểm soát chất lượng đến mô hình PostgreSQL
          và lớp báo cáo Power BI.
        </span>
      </div>

      <figure className={styles.pipelineFigure}>
        <a href="/images/etl-pipeline.png" target="_blank" rel="noopener noreferrer" aria-label="Mở sơ đồ pipeline ở kích thước đầy đủ">
          <picture>
            <source srcSet="/images/etl-pipeline.webp" type="image/webp" />
            <img
              src="/images/etl-pipeline.png"
              alt="Sơ đồ pipeline ETL và trực quan hóa dữ liệu BCTC công ty chứng khoán"
              width="3079"
              height="1469"
              loading="lazy"
            />
          </picture>
        </a>
        <figcaption>
          Pipeline từ báo cáo tài chính nguồn đến PostgreSQL và Power BI. Chọn ảnh để xem kích thước đầy đủ.
        </figcaption>
      </figure>

      <div className={styles.workflowGrid}>
        {securitiesWorkflow.map((step) => (
          <article key={step.number} className={styles.workflowCard}>
            <header>
              <span>{step.number}</span>
              <h3>{step.title}</h3>
            </header>
            <p>{step.description}</p>
            <dl className={styles.ioList}>
              <div>
                <dt>Input</dt>
                <dd>{step.input}</dd>
              </div>
              <div>
                <dt>Output</dt>
                <dd>{step.output}</dd>
              </div>
            </dl>
            <div className={styles.toolChips} aria-label={`Công cụ cho bước ${step.number}`}>
              {step.tools.map((tool) => <span key={tool}>{tool}</span>)}
            </div>
            {step.note && <p className={styles.workflowNote}>{step.note}</p>}
          </article>
        ))}
      </div>

      <div className={styles.qualitySection}>
        <div>
          <p className={styles.miniEyebrow}>CÁC KIỂM SOÁT ĐÃ ÁP DỤNG</p>
          <h3>Kiểm soát chất lượng dữ liệu</h3>
          <p>
            Các kiểm soát dưới đây được giữ đúng theo quy trình đã mô tả trong source hiện tại.
          </p>
        </div>
        <div className={styles.qualityGrid}>
          {verifiedQualityControls.map((control) => (
            <article key={control.title}>
              <h4>{control.title}</h4>
              <p>{control.description}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  )
}

function DataModel() {
  return (
    <section className={styles.caseSection} aria-labelledby="model-heading">
      <div className={styles.sectionHeading}>
        <p>KIẾN TRÚC POSTGRESQL</p>
        <h2 id="model-heading">Mô hình dữ liệu &amp; Kiến trúc</h2>
        <span>
          Mô hình dữ liệu tách dữ liệu báo cáo tài chính khỏi các dimension dùng chung, hỗ trợ phân tích
          đa công ty, đa kỳ và tái sử dụng trên Power BI.
        </span>
      </div>

      <div className={styles.architectureGrid}>
        {architectureGroups.map((group) => (
          <article key={group.title} className={styles.architectureCard}>
            <h3>{group.title}</h3>
            <div className={styles.tableNames}>
              {group.tables.map((table) => <code key={table}>{table}</code>)}
            </div>
            <p>{group.description}</p>
          </article>
        ))}
      </div>

      <div className={styles.grainPanel}>
        <div>
          <span>GRAIN PHÂN TÍCH CỐT LÕI</span>
          <strong>Công ty × Kỳ báo cáo × Chỉ tiêu tài chính</strong>
        </div>
        <div>
          <span>GRAIN DANH MỤC ĐẦU TƯ</span>
          <strong>Công ty × Ngày/Kỳ × Nhóm tài sản</strong>
        </div>
      </div>

      <figure className={styles.schemaFigure}>
        <div className={styles.schemaToolbar}>
          <div>
            <h3>PostgreSQL Star Schema</h3>
            <p>Fact và Dimension dùng chung cho dữ liệu tài chính, danh mục và dữ liệu thị trường.</p>
          </div>
          <a className="button buttonSecondary" href="/images/erd-postgresql.png" target="_blank" rel="noopener noreferrer">
            Xem mô hình đầy đủ
          </a>
        </div>
        <a
          className={styles.schemaViewport}
          href="/images/erd-postgresql.png"
          target="_blank"
          rel="noopener noreferrer"
          aria-label="Mở Star Schema ở kích thước đầy đủ"
        >
          <picture>
            <source srcSet="/images/erd-postgresql.webp" type="image/webp" />
            <img
              src="/images/erd-postgresql.png"
              alt="Star Schema PostgreSQL gồm các bảng fact báo cáo tài chính, danh mục, thị trường và các dimension dùng chung"
              width="1317"
              height="1075"
              loading="lazy"
            />
          </picture>
        </a>
        <figcaption>Trên màn hình nhỏ, cuộn ngang trong vùng ảnh hoặc mở mô hình đầy đủ để đọc chi tiết.</figcaption>
      </figure>

      <div className={styles.repositoryRow}>
        <div>
          <h3>Repository</h3>
          <p>Mã nguồn dự án chưa được public.</p>
        </div>
        <button type="button" className="button buttonSecondary" disabled>
          Repository — Coming soon
        </button>
      </div>
    </section>
  )
}

function PowerBISection({ embedUrl }: { embedUrl: string }) {
  return (
    <section className={styles.caseSection} aria-labelledby="powerbi-heading">
      <div className={styles.powerBiIntro}>
        <div>
          <p className={styles.miniEyebrow}>Interactive analytics</p>
          <h2 id="powerbi-heading">Power BI</h2>
          <p>Báo cáo Power BI tương tác cho phân tích báo cáo tài chính theo từng công ty và so sánh đa công ty.</p>
        </div>
        <ul>
          {powerBiCapabilities.map((capability) => <li key={capability}>{capability}</li>)}
        </ul>
      </div>
      <div className={styles.powerBiFrame}>
        <PowerBIEmbed title="Power BI — Phân tích BCTC Chứng khoán Việt Nam" embedUrl={embedUrl} />
      </div>
    </section>
  )
}

export default function SecuritiesPage() {
  const project = getProject('securities_vn')

  return (
    <div className={styles.securitiesPage}>
      <CaseStudyHeader />
      <ProjectTabs
        label="Chi tiết dự án BCTC Chứng khoán Việt Nam"
        tabs={[
          { id: 'overview', label: 'Tổng quan', content: <Overview /> },
          { id: 'workflow', label: 'Quy trình dữ liệu', content: <Workflow /> },
          { id: 'model', label: 'Mô hình dữ liệu', content: <DataModel /> },
          { id: 'powerbi', label: 'Power BI', content: <PowerBISection embedUrl={project.powerBiUrl ?? ''} /> },
        ]}
      />
    </div>
  )
}
