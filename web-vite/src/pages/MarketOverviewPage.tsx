import { useEffect, useState } from 'react'
import { PowerBIEmbed } from '../components/powerbi/PowerBIEmbed'
import { ProjectTabs } from '../components/projects/ProjectTabs'
import {
  marketDataQualityControls,
  marketDataSources,
  marketModelDimensions,
  marketModelFacts,
  marketModelImage,
  marketModelRelationships,
  marketModelScope,
  marketOverviewContent,
  marketOverviewProject,
  marketWorkflowStages,
  powerBiReportModules,
  sqlAnalyticsRoadmap,
  type ProjectStatusTone,
} from '../data/marketOverview'
import styles from './MarketOverviewPage.module.css'

const marketOverviewPowerBIUrl = import.meta.env.VITE_MARKET_OVERVIEW_POWERBI_URL
const hasMarketOverviewPowerBI =
  typeof marketOverviewPowerBIUrl === 'string' &&
  marketOverviewPowerBIUrl.trim().length > 0
const resolvedMarketOverviewPowerBIUrl = hasMarketOverviewPowerBI
  ? marketOverviewPowerBIUrl.trim()
  : ''
const SHOW_MARKET_SQL_ANALYTICS = true

function SectionHeading({
  eyebrow,
  title,
  description,
  id,
}: {
  eyebrow: string
  title: string
  description: string
  id: string
}) {
  return (
    <header className={styles.sectionHeading}>
      <p>{eyebrow}</p>
      <h2 id={id}>{title}</h2>
      <span>{description}</span>
    </header>
  )
}

function StatusBadge({
  label,
  value,
  tone,
}: {
  label: string
  value: string
  tone: ProjectStatusTone
}) {
  return (
    <span className={`${styles.statusBadge} ${styles[tone]}`}>
      <span>{label}</span>
      <strong>{value}</strong>
    </span>
  )
}

function CaseStudyHeader() {
  return (
    <header className={`${styles.caseHeader} surface`}>
      <div className={styles.headerCopy}>
        <p className={styles.eyebrow}>{marketOverviewProject.eyebrow}</p>
        <h1>{marketOverviewProject.name}</h1>
        <p className={styles.subtitle}>{marketOverviewProject.subtitle}</p>
        <p className={styles.description}>{marketOverviewProject.description}</p>

        <div className={styles.techChips} aria-label="Công nghệ sử dụng">
          {marketOverviewProject.technologies.map((technology) => (
            <span key={technology}>{technology}</span>
          ))}
        </div>

        <div className={styles.statusList} aria-label="Trạng thái project">
          {marketOverviewProject.statuses.map((status) => (
            <StatusBadge key={status.label} {...status} />
          ))}
        </div>
      </div>

      <dl className={styles.metrics} aria-label="Phạm vi project">
        {marketOverviewProject.metrics.map((metric) => (
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
    <section className={styles.caseSection} aria-labelledby="market-overview-heading">
      <SectionHeading
        eyebrow="TỔNG QUAN DỰ ÁN"
        title={marketOverviewContent.heading}
        description={marketOverviewContent.description}
        id="market-overview-heading"
      />

      <div className={styles.problemGrid}>
        <article className={styles.contextCard}>
          <span className={styles.cardIndex}>01 · BÀI TOÁN</span>
          <h3>{marketOverviewContent.problem.title}</h3>
          <p>{marketOverviewContent.problem.description}</p>
        </article>
        <article className={styles.contextCard}>
          <span className={styles.cardIndex}>02 · MỤC TIÊU</span>
          <h3>{marketOverviewContent.objective.title}</h3>
          <p>{marketOverviewContent.objective.description}</p>
        </article>
      </div>

      <div className={styles.contentBlock}>
        <h3>Các thành phần chính</h3>
        <div className={styles.componentGrid}>
          {marketOverviewContent.components.map((component, index) => (
            <article key={component.title} className={styles.compactCard}>
              <span className={styles.compactNumber}>{String(index + 1).padStart(2, '0')}</span>
              <h4>{component.title}</h4>
              <p>{component.description}</p>
            </article>
          ))}
        </div>
      </div>

      <div className={styles.contentBlock}>
        <h3>Giá trị phân tích</h3>
        <div className={styles.valueGrid}>
          {marketOverviewContent.values.map((value) => (
            <article key={value.title} className={styles.valueCard}>
              <h4>{value.title}</h4>
              <p>{value.description}</p>
            </article>
          ))}
        </div>
      </div>

      <div className={styles.contentBlock}>
        <h3>Luồng hệ thống</h3>
        <ol className={styles.pipeline} aria-label="Luồng hệ thống Market Overview">
          {marketOverviewContent.pipeline.map((node) => (
            <li key={node.label}>
              <span>{node.label}</span>
              {node.status && <small>{node.status}</small>}
            </li>
          ))}
        </ol>
      </div>
    </section>
  )
}

function DataPipeline() {
  return (
    <section className={styles.caseSection} aria-labelledby="market-pipeline-heading">
      <SectionHeading
        eyebrow="DATA WORKFLOW"
        title="Thu thập và chuẩn hóa dữ liệu thị trường"
        description="Pipeline thu thập, làm sạch, chuẩn hóa và kiểm tra dữ liệu trước khi đưa vào PostgreSQL và Power BI."
        id="market-pipeline-heading"
      />

      <div className={styles.sourceSection}>
        <div>
          <p className={styles.miniEyebrow}>DATA SOURCES</p>
          <h3>Data Sources</h3>
        </div>
        <div className={styles.sourceGrid}>
          {marketDataSources.map((source) => (
            <article key={source.title} className={styles.sourceCard}>
              <h4>{source.title}</h4>
              <p>{source.description}</p>
              <div className={styles.toolChips} aria-label={`Dữ liệu từ ${source.title}`}>
                {source.tags.map((tag) => <span key={tag}>{tag}</span>)}
              </div>
            </article>
          ))}
        </div>
      </div>

      <div className={styles.workflowGrid}>
        {marketWorkflowStages.map((stage) => (
          <article
            key={stage.number}
            className={`${styles.workflowCard} ${stage.number === '05' ? styles.analyticsCard : ''}`}
          >
            <header>
              <span>{stage.number}</span>
              <div>
                <small>{stage.eyebrow}</small>
                <h3>{stage.title}</h3>
              </div>
            </header>
            <ul>
              {stage.items.map((item) => <li key={item}>{item}</li>)}
            </ul>
            <div className={styles.toolChips} aria-label={`Công cụ cho ${stage.title}`}>
              {stage.tools.map((tool) => <span key={tool}>{tool}</span>)}
            </div>
            {stage.note && <p className={styles.workflowNote}>{stage.note}</p>}
          </article>
        ))}
      </div>

      <div className={styles.qualityPanel}>
        <div>
          <p className={styles.miniEyebrow}>DATA QUALITY</p>
          <h3>Data Quality Controls</h3>
          <p>Các bước kiểm tra được thực hiện trước khi dữ liệu được sử dụng cho SQL analysis hoặc Power BI.</p>
        </div>
        <div className={styles.qualityGrid}>
          {marketDataQualityControls.map((control) => (
            <article key={control.title} className={styles.qualityCard}>
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
  const [isModelOpen, setIsModelOpen] = useState(false)
  const [isModelLoaded, setIsModelLoaded] = useState(false)

  useEffect(() => {
    if (!isModelOpen) return

    const previousOverflow = document.body.style.overflow
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Escape') setIsModelOpen(false)
    }

    document.body.style.overflow = 'hidden'
    window.addEventListener('keydown', handleKeyDown)

    return () => {
      document.body.style.overflow = previousOverflow
      window.removeEventListener('keydown', handleKeyDown)
    }
  }, [isModelOpen])

  return (
    <section className={styles.caseSection} aria-labelledby="market-model-heading">
      <SectionHeading
        eyebrow="POSTGRESQL & POWER BI MODEL"
        title="Mô hình dữ liệu thị trường dạng Fact và Dimension"
        description="Mô hình sử dụng các Dimension dùng chung để kết nối dữ liệu giá, chỉ số, dòng tiền và thị trường toàn cầu, phục vụ SQL Analytics và Power BI."
        id="market-model-heading"
      />

      <div className={styles.modelStatusRow}>
        <StatusBadge label="Data Model" value="Completed" tone="complete" />
      </div>

      <div className={styles.modelGrid}>
        {marketModelScope.map((item) => (
          <article key={item.title} className={styles.modelCard}>
            <h3>{item.title}</h3>
            <p>{item.description}</p>
          </article>
        ))}
      </div>

      <section className={styles.inventorySection} aria-labelledby="market-schema-inventory-heading">
        <header className={styles.subsectionHeading}>
          <p className={styles.miniEyebrow}>SCHEMA INVENTORY</p>
          <h3 id="market-schema-inventory-heading">Dimensions &amp; Facts</h3>
          <p>
            Các bảng được tổ chức theo dimensional model, tách market entities khỏi dữ liệu giao dịch
            phát sinh theo ngày.
          </p>
        </header>

        <div className={styles.inventoryGrid}>
          <section className={styles.inventoryColumn} aria-labelledby="market-dimensions-heading">
            <h4 id="market-dimensions-heading">Dimensions</h4>
            <ul className={styles.tableList}>
              {marketModelDimensions.map((table) => (
                <li key={table.title}>
                  <code>{table.title}</code>
                  <p>{table.description}</p>
                </li>
              ))}
            </ul>
          </section>

          <section className={styles.inventoryColumn} aria-labelledby="market-facts-heading">
            <h4 id="market-facts-heading">Facts</h4>
            <ul className={styles.tableList}>
              {marketModelFacts.map((table) => (
                <li key={table.title}>
                  <div className={styles.tableTitleRow}>
                    <code>{table.title}</code>
                    {table.grain && <span className={styles.grainBadge}>Grain · {table.grain}</span>}
                  </div>
                  <p>{table.description}</p>
                </li>
              ))}
            </ul>
          </section>
        </div>
      </section>

      <section className={styles.relationshipSection} aria-labelledby="market-relationships-heading">
        <header className={styles.subsectionHeading}>
          <p className={styles.miniEyebrow}>RELATIONSHIP SUMMARY</p>
          <h3 id="market-relationships-heading">Shared Dimensions Across Market Facts</h3>
          <p>
            Shared dimensions giúp các Fact table sử dụng cùng một hệ thống ticker, ngành, sàn và thời
            gian, hỗ trợ filtering và drill-down nhất quán trong Power BI.
          </p>
        </header>
        <ul className={styles.relationshipList}>
          {marketModelRelationships.map((relationship) => (
            <li key={relationship}>{relationship}</li>
          ))}
        </ul>
      </section>

      <section className={styles.modelVisualSection} aria-labelledby="market-model-visual-heading">
        <header className={styles.subsectionHeading}>
          <p className={styles.miniEyebrow}>POWER BI MODEL VIEW</p>
          <h3 id="market-model-visual-heading">Market Overview Data Model</h3>
          <p>
            Power BI Model View thể hiện relationship giữa các shared dimensions và daily market facts
            trong analytical model.
          </p>
        </header>

        {marketModelImage.available ? (
          <div className={styles.modelImageArea}>
            <div className={styles.modelImageScroller}>
              {!isModelLoaded && <span className={styles.modelLoading}>Loading model view…</span>}
              <button
                type="button"
                className={styles.modelImageButton}
                aria-label="View Full Model"
                onClick={() => setIsModelOpen(true)}
              >
                <img
                  src={marketModelImage.src}
                  alt={marketModelImage.alt}
                  loading="lazy"
                  onLoad={() => setIsModelLoaded(true)}
                />
              </button>
            </div>
            <button
              type="button"
              className={styles.viewModelButton}
              onClick={() => setIsModelOpen(true)}
            >
              View Full Model
            </button>
          </div>
        ) : (
          <div className={styles.modelVisualPlaceholder} role="img" aria-label={marketModelImage.alt}>
            <div className={styles.diagramMark} aria-hidden="true">
              <span />
              <span />
              <span />
            </div>
            <div>
              <strong>Market Overview Data Model</strong>
              <p>Ảnh mô hình dữ liệu sẽ được cập nhật sau khi hoàn thiện bố cục Model View trong Power BI.</p>
            </div>
          </div>
        )}
      </section>

      {marketModelImage.available && isModelOpen && (
        <div
          className={styles.modelModal}
          role="dialog"
          aria-modal="true"
          aria-label="Vietnam Market Overview Power BI data model"
          onClick={() => setIsModelOpen(false)}
        >
          <div className={styles.modelModalContent} onClick={(event) => event.stopPropagation()}>
            <button
              type="button"
              className={styles.modelModalClose}
              aria-label="Đóng mô hình dữ liệu"
              onClick={() => setIsModelOpen(false)}
              autoFocus
            >
              ×
            </button>
            <div className={styles.modelModalScroller}>
              <img src={marketModelImage.src} alt={marketModelImage.alt} />
            </div>
          </div>
        </div>
      )}
    </section>
  )
}

function SQLAnalytics() {
  return (
    <section className={styles.caseSection} aria-labelledby="market-sql-heading">
      <SectionHeading
        eyebrow="ANALYTICAL SQL"
        title="Phân tích dữ liệu thị trường bằng SQL"
        description="SQL được sử dụng để tổng hợp, xếp hạng và chuẩn bị analytical datasets cho market monitoring và Power BI."
        id="market-sql-heading"
      />

      <div className={styles.progressIntro}>
        <span className={styles.inProgressBadge}>IN PROGRESS</span>
        <div>
          <h3>SQL Analytics Layer</h3>
          <p>
            Dimensional model đã hoàn thành. Các analytical SQL cases đang được xây dựng để phục vụ
            market breadth, sector ranking, liquidity analysis và trading-flow analysis.
          </p>
        </div>
      </div>

      <div className={styles.sqlGrid}>
        {sqlAnalyticsRoadmap.map((item, index) => (
          <article key={item} className={styles.sqlCard}>
            <span>{String(index + 1).padStart(2, '0')}</span>
            <h3>{item}</h3>
            <p>Planned analytical case</p>
          </article>
        ))}
      </div>

      <p className={styles.roadmapNote}>
        Planned analytical cases — results will be added after SQL validation.
      </p>
    </section>
  )
}

function PowerBISection() {
  return (
    <section className={styles.caseSection} aria-labelledby="market-powerbi-heading">
      <SectionHeading
        eyebrow="POWER BI REPORT"
        title="Từ bối cảnh toàn cầu đến thị trường Việt Nam"
        description="Power BI report đang được xây dựng để kết nối bối cảnh thị trường toàn cầu với chỉ số, ngành, cổ phiếu, thanh khoản và dòng tiền tại Việt Nam."
        id="market-powerbi-heading"
      />

      <div className={styles.progressIntro}>
        <span className={styles.inProgressBadge}>IN PROGRESS</span>
        <div>
          <h3>Power BI Report</h3>
          <p>The data model and analytical structure are complete. The interactive Power BI report will be published soon.</p>
        </div>
      </div>

      <div className={styles.reportSection}>
        <h3>Report Structure</h3>
        <div className={styles.reportGrid}>
          {powerBiReportModules.map((module) => (
            <article key={module.number} className={styles.reportCard}>
              <header>
                <span>{module.number}</span>
                <small>{module.status}</small>
              </header>
              <h4>{module.title}</h4>
              <ul>{module.scope.map((item) => <li key={item}>{item}</li>)}</ul>
            </article>
          ))}
        </div>
      </div>

      {hasMarketOverviewPowerBI ? (
        <div className={styles.powerBiFrame}>
          <PowerBIEmbed
            title="Power BI — Vietnam Market Overview & Analytics"
            embedUrl={resolvedMarketOverviewPowerBIUrl}
          />
        </div>
      ) : (
        <article className={styles.powerBiPlaceholder} aria-labelledby="market-powerbi-placeholder-title">
          <div className={styles.placeholderVisual} aria-hidden="true">
            <span />
            <span />
            <span />
            <span />
          </div>
          <div>
            <p className={styles.miniEyebrow}>POWER BI REPORT</p>
            <h3 id="market-powerbi-placeholder-title">Power BI Dashboard — In Progress</h3>
            <p>
              Dashboard đang được hoàn thiện để kết nối bối cảnh thị trường toàn cầu với chỉ số, ngành,
              cổ phiếu, thanh khoản và dòng tiền trên thị trường Việt Nam.
            </p>
            <small>The data model and analytical structure are complete. The interactive report will be published soon.</small>
          </div>
          <span className={styles.comingSoon}>COMING SOON</span>
        </article>
      )}
    </section>
  )
}

export default function MarketOverviewPage() {
  return (
    <div className={styles.marketPage}>
      <CaseStudyHeader />
      <div className={styles.mainTabs}>
        <ProjectTabs
          label="Chi tiết dự án Vietnam Market Overview & Analytics"
          tabs={[
            { id: 'overview', label: 'Tổng quan', content: <Overview /> },
            { id: 'pipeline', label: 'Data Pipeline', content: <DataPipeline /> },
            { id: 'model', label: 'Data Model', content: <DataModel /> },
            ...(SHOW_MARKET_SQL_ANALYTICS
              ? [{ id: 'sql', label: 'SQL Analytics', content: <SQLAnalytics /> }]
              : []),
            { id: 'powerbi', label: 'Power BI', content: <PowerBISection /> },
          ]}
        />
      </div>
    </div>
  )
}
