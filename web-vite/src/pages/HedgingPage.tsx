import { BacktestExplorer } from '../components/backtest/BacktestExplorer'
import { InteractiveChartEmbed } from '../components/charts/InteractiveChartEmbed'
import { ProjectTabs } from '../components/projects/ProjectTabs'
import {
  analyticalValues,
  automationControls,
  emailPreviews,
  exitRules,
  hedgingPipeline,
  hedgingSolutions,
  hedgingTech,
  pipelineSummary,
  shortRules,
  type EmailPreview,
} from '../data/hedging'
import { getProject } from '../data/projects'
import styles from './HedgingPage.module.css'

function SectionHeading({
  eyebrow,
  title,
  description,
}: {
  eyebrow: string
  title: string
  description?: string
}) {
  return (
    <header className={styles.sectionHeading}>
      <p>{eyebrow}</p>
      <h2>{title}</h2>
      {description && <span>{description}</span>}
    </header>
  )
}

function CaseHeader() {
  return (
    <header className={styles.caseHeader}>
      <p className={styles.eyebrow}>Personal Technical Project · Financial Data Analytics</p>
      <h1>VN30F1M Hedging &amp; Monitoring System</h1>
      <p className={styles.subtitle}>Financial Time-Series, Backtesting &amp; Rule-Based Automation</p>
      <p className={styles.description}>
        Hệ thống xử lý dữ liệu VN30F1M intraday, xây dựng tín hiệu hedge theo bộ quy tắc, kiểm định bằng
        Grid Search và quản lý cảnh báo theo State Machine.
      </p>
      <div className={styles.techChips} aria-label="Công nghệ sử dụng">
        {hedgingTech.map((tech) => <span key={tech}>{tech}</span>)}
      </div>
    </header>
  )
}

function Overview() {
  return (
    <section className={styles.caseSection}>
      <SectionHeading
        eyebrow="Tổng quan dự án"
        title="Quy trình phân tích VN30F1M có thể tái lập"
        description="Xử lý dữ liệu intraday, tạo tín hiệu theo rule-based logic, kiểm định nhiều bộ tham số bằng Grid Search và quản lý cảnh báo bằng State Machine."
      />

      <div className={styles.problemGrid}>
        <article className={styles.contextCard}>
          <span className={styles.cardIndex}>01 · BÀI TOÁN</span>
          <h3>Theo dõi thủ công khó kiểm định</h3>
          <p>Dữ liệu VN30F1M intraday biến động liên tục trong phiên, khiến việc theo dõi tín hiệu hedge thủ công thiếu nhất quán và khó kiểm định trên nhiều điều kiện thị trường.</p>
        </article>
        <article className={styles.contextCard}>
          <span className={styles.cardIndex}>02 · MỤC TIÊU</span>
          <h3>Xây dựng workflow hedge có thể tái lập</h3>
          <p>Xây dựng một workflow xử lý dữ liệu, tạo tín hiệu theo bộ quy tắc, kiểm định nhiều bộ tham số và quản lý vòng đời cảnh báo theo trạng thái.</p>
        </article>
      </div>

      <div className={styles.contentBlock}>
        <h3>Các thành phần chính</h3>
        <div className={styles.solutionGrid}>
          {hedgingSolutions.map((solution) => (
            <article key={solution.number} className={styles.compactCard}>
              <span className={styles.compactNumber}>{solution.number}</span>
              <h4>{solution.title}</h4>
              <p>{solution.description}</p>
            </article>
          ))}
        </div>
      </div>

      <div className={styles.contentBlock}>
        <h3>Giá trị phân tích</h3>
        <div className={styles.valueGrid}>
          {analyticalValues.map((value) => (
            <article key={value.title} className={styles.valueCard}>
              <h4>{value.title}</h4>
              <p>{value.description}</p>
            </article>
          ))}
        </div>
      </div>

      <div className={styles.contentBlock}>
        <h3>Luồng hệ thống</h3>
        <ol className={styles.pipelineSummary}>
          {pipelineSummary.map((step) => <li key={step}>{step}</li>)}
        </ol>
      </div>
    </section>
  )
}

function StateMachine({ compact = false }: { compact?: boolean }) {
  if (compact) {
    return (
      <ol className={styles.compactState} aria-label="Luồng trạng thái cảnh báo">
        {['WAIT_SHORT', 'SHORT alert', 'WAIT_OUT', 'EXIT alert', 'WAIT_SHORT'].map((state, index) => (
          <li key={`${state}-${index}`}>{state}</li>
        ))}
      </ol>
    )
  }

  return (
    <div className={styles.stateMachine} aria-label="State Machine kiểm soát cảnh báo">
      <div className={styles.stateNode}><strong>WAIT_SHORT</strong><span>Chờ tín hiệu short đủ điều kiện</span></div>
      <div className={styles.stateArrow}><span className={styles.condition}>spread &lt; threshold · streak đạt N · tín hiệu xác nhận</span><span>SHORT signal</span></div>
      <div className={`${styles.stateNode} ${styles.activeState}`}><strong>WAIT_OUT</strong><span>Theo dõi điều kiện thoát</span></div>
      <div className={styles.stateArrow}><span className={styles.condition}>TP · streak đảo chiều · cuối ngày</span><span>EXIT signal</span></div>
      <div className={styles.stateNode}><strong>WAIT_SHORT</strong><span>Reset và chờ tín hiệu tiếp theo</span></div>
    </div>
  )
}

function Rules() {
  return (
    <div className={styles.rules}>
      <section aria-labelledby="short-rules-title">
        <h3 id="short-rules-title" className={styles.shortTitle}>Short Entry Conditions</h3>
        <ul>{shortRules.map((rule) => <li key={rule}>{rule}</li>)}</ul>
      </section>
      <section aria-labelledby="exit-rules-title">
        <h3 id="exit-rules-title" className={styles.exitTitle}>Exit Conditions</h3>
        <ul>{exitRules.map((rule) => <li key={rule}>{rule}</li>)}</ul>
      </section>
    </div>
  )
}

function Workflow() {
  return (
    <section className={styles.caseSection}>
      <SectionHeading
        eyebrow="System workflow"
        title="Quy trình xử lý & Logic kiểm soát"
        description="Luồng xử lý từ dữ liệu intraday đến tạo tín hiệu, kiểm định Backtest và giám sát cảnh báo theo trạng thái."
      />
      <div className={styles.workflowGrid}>
        {hedgingPipeline.map((step) => (
          <article key={step.number} className={styles.workflowCard}>
            <header>
              <span>{step.number}</span>
              <div>
                <small>{step.label}</small>
                <h3>{step.title}</h3>
              </div>
            </header>
            <ul>{step.items.map((item) => <li key={item}>{item}</li>)}</ul>
          </article>
        ))}
      </div>

      <div className={styles.systemGrid}>
        <article className={styles.systemCard}>
          <span className={styles.miniEyebrow}>Workflow control</span>
          <h2>State Machine kiểm soát cảnh báo</h2>
          <p>State Machine kiểm soát vòng đời tín hiệu, hạn chế cảnh báo trùng lặp và lưu trạng thái giữa các lần chạy.</p>
          <StateMachine />
        </article>
        <article className={styles.systemCard}>
          <span className={styles.miniEyebrow}>Rule engine</span>
          <h2>Rule-Based Signal Logic</h2>
          <Rules />
        </article>
      </div>
    </section>
  )
}

function SourceCode() {
  const project = getProject('hedging_vn30f1m')
  return (
    <section className={styles.caseSection}>
      <SectionHeading
        eyebrow="Implementation"
        title="Source code & Signal Visualization"
        description="Mã R cho Backtest và biểu đồ tín hiệu được tổ chức trong repository công khai của dự án."
      />
      <div className={styles.repositoryRow}>
        <div>
          <h3>VN30F1M_HEDGING</h3>
          <p>Backtest engine và signal chart source.</p>
        </div>
        <a className="button buttonSecondary" href={project.githubUrl} target="_blank" rel="noopener noreferrer">
          Xem repository trên GitHub
        </a>
      </div>
      <div className={styles.chartBlock}>
        <div>
          <span className={styles.miniEyebrow}>ECharts</span>
          <h2>Biểu đồ tín hiệu VN30F1M</h2>
        </div>
        <InteractiveChartEmbed />
      </div>
    </section>
  )
}

function Backtest() {
  return (
    <section className={styles.caseSection}>
      <SectionHeading
        eyebrow="Historical validation"
        title="Backtest Results & Parameter Optimization"
        description="Grid Search trên nhiều cấu hình quy tắc với dữ liệu VN30F1M intraday lịch sử."
      />
      <BacktestExplorer />

      <section className={styles.walkForward} aria-labelledby="walk-forward-title">
        <header className={styles.walkForwardHeader}>
          <div>
            <span className={styles.miniEyebrow}>Validation roadmap</span>
            <h2 id="walk-forward-title">Walk-Forward Validation Roadmap</h2>
          </div>
          <span className={styles.plannedBadge}>NEXT ITERATION</span>
        </header>
        <p className={styles.walkForwardIntro}>Grid Search backtest đã hoàn thành. Walk-forward chưa có kết quả và được giữ như bước kiểm định tiếp theo.</p>
        <div className={styles.plannedGrid}>
          <article><strong>In-sample</strong><p>Tối ưu tham số trên cửa sổ dữ liệu huấn luyện lịch sử.</p></article>
          <article><strong>Out-of-sample</strong><p>Đánh giá cấu hình đã chọn trên cửa sổ dữ liệu chưa tham gia tối ưu.</p></article>
          <article><strong>Roll-forward</strong><p>Tịnh tiến cửa sổ Train–Test và lặp lại quy trình đánh giá.</p></article>
        </div>
      </section>
    </section>
  )
}

function EmailCard({ preview }: { preview: EmailPreview }) {
  return (
    <article className={styles.emailPreview} aria-label={`Mẫu email tự động: ${preview.label}`}>
      <div className={styles.emailBadge}>Mẫu email tự động</div>
      <header className={`${styles.emailHeader} ${styles[preview.tone]}`}>
        <div className={styles.emailSubject}>{preview.subject}</div>
        <div className={styles.emailMeta}>{preview.meta}</div>
      </header>
      <div className={styles.emailBody}>
        {preview.rows.map(([label, value, tone]) => (
          <div key={label} className={styles.emailRow}>
            <span className={styles.emailLabel}>{label}</span>
            <span className={`${styles.emailValue} ${tone === 'normal' ? '' : styles[tone]}`}>{value}</span>
          </div>
        ))}
      </div>
      {preview.footer && <div className={styles.emailFooter}>{preview.footer}</div>}
    </article>
  )
}

function AlertEmail() {
  return (
    <section className={styles.caseSection}>
      <SectionHeading
        eyebrow="Automated monitoring"
        title="Hệ thống cảnh báo tự động"
        description="State Machine quản lý vòng đời tín hiệu, tự động tạo email khi trạng thái thay đổi và tổng hợp báo cáo cuối ngày."
      />

      <ol className={styles.automationFlow} aria-label="Quy trình tạo cảnh báo">
        {['Phát hiện tín hiệu', 'Cập nhật trạng thái', 'Tạo email', 'Lưu log'].map((step) => <li key={step}>{step}</li>)}
      </ol>

      <div className={styles.emailLayout}>
        <aside className={styles.emailAside}>
          <section className={styles.emailControlCard} aria-labelledby="compact-state-title">
            <span className={styles.miniEyebrow}>State lifecycle</span>
            <h2 id="compact-state-title">Vòng đời cảnh báo</h2>
            <StateMachine compact />
          </section>
          <section className={styles.emailControlCard} aria-labelledby="automation-controls-title">
            <span className={styles.miniEyebrow}>Controls</span>
            <h2 id="automation-controls-title">Kiểm soát tự động hóa</h2>
            <ul>{automationControls.map((control) => <li key={control}>{control}</li>)}</ul>
          </section>
          <section className={styles.dailySummary} aria-labelledby="daily-summary-title">
            <strong id="daily-summary-title">Báo cáo cuối ngày</strong>
            <p>Cuối mỗi phiên, hệ thống tổng hợp số lệnh, P&amp;L tạm tính, Win Rate và tham số áp dụng, sau đó gửi báo cáo HTML tự động cho người theo dõi hệ thống.</p>
          </section>
        </aside>
        <div className={styles.emailShowcase}>
          <ProjectTabs
            label="Mẫu email tự động"
            tabs={emailPreviews.map((preview) => ({
              id: preview.id,
              label: preview.label,
              content: <EmailCard preview={preview} />,
            }))}
          />
        </div>
      </div>
    </section>
  )
}

export default function HedgingPage() {
  return (
    <div className={styles.hedgingPage}>
      <CaseHeader />
      <div className={styles.mainTabs}>
        <ProjectTabs
          label="Chi tiết dự án Hedging VN30F1M"
          tabs={[
            { id: 'overview', label: 'Tổng quan', content: <Overview /> },
            { id: 'workflow', label: 'Workflow', content: <Workflow /> },
            { id: 'source', label: 'Source Code', content: <SourceCode /> },
            { id: 'backtest', label: 'Backtest', content: <Backtest /> },
            { id: 'alert', label: 'Email Alerts', content: <AlertEmail /> },
          ]}
        />
      </div>
    </div>
  )
}
