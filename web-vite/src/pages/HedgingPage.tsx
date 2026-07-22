import { BacktestExplorer } from '../components/backtest/BacktestExplorer'
import { InteractiveChartEmbed } from '../components/charts/InteractiveChartEmbed'
import { ProjectPageHeader } from '../components/projects/ProjectPageHeader'
import { ProjectTabs } from '../components/projects/ProjectTabs'
import { emailPreviews, exitRules, hedgingFeatures, hedgingPipeline, hedgingTech, shortRules, type EmailPreview } from '../data/hedging'
import { getProject } from '../data/projects'
import styles from './ProjectPages.module.css'

function Overview() {
  return (
    <section>
      <div className={`twoColumn ${styles.overviewCards}`}>
        <article className="card">
          <h2 className={`${styles.cardTitle} ${styles.purpleTitle}`}>🎯 Bối cảnh & Nhiệm vụ</h2>
          <p><strong>Situation:</strong> Thị trường Phái sinh VN30F1M đòi hỏi khả năng phản ứng tức thì với biến động giá trong phiên (9:00–14:30). Việc theo dõi màn hình thủ công liên tục không khả thi và dễ dẫn đến sai sót tâm lý.</p>
          <p><strong>Task:</strong> Xây dựng End-to-end Automated Trading Pipeline với các mục tiêu:</p>
          <ul className={styles.cardList}>
            <li><strong>Tự động hóa toàn trình:</strong> Xây dựng luồng dữ liệu (pipeline) thu thập OHLCV, tính toán tín hiệu (Entry/Stoploss/Take Profit) dựa trên bộ quy tắc cá nhân.</li>
            <li><strong>Kiểm định & Tối ưu:</strong> Thực hiện Backtest và tối ưu tham số để đánh giá hiệu quả chiến lược.</li>
            <li><strong>Thực thi:</strong> Phát cảnh báo qua email và tích hợp SSI FastConnect API để tự động hóa việc đặt lệnh theo thời gian thực.</li>
          </ul>
        </article>
        <article className="card">
          <h2 className={`${styles.cardTitle} ${styles.blueTitle}`}>⚡ Hành động & Kết quả</h2>
          <ul className={styles.cardList}>
            <li><strong>Data Handling:</strong> Tự động lấy dữ liệu OHLCV 1-phút từ các nguồn (SSI, DNSE) và chuẩn hóa dữ liệu bằng R để thuận tiện cho việc xử lý.</li>
            <li><strong>Entry/Exit Logic:</strong> Xây dựng các hàm (functions) tính toán chỉ báo và tín hiệu dựa trên các quy tắc cá nhân (như MA, spread, streak spread).</li>
            <li><strong>Visualization:</strong> Sử dụng biểu đồ nến (Candlestick chart) có tích hợp tín hiệu để theo dõi trạng thái chiến lược trực tiếp trong phiên.</li>
            <li><strong>Testing & Tuning:</strong> Kiểm tra chiến lược bằng cách thử nghiệm nhiều mức tham số khác nhau (Grid Search) và chạy thử cuốn chiếu trên dữ liệu quá khứ (Walk-forward) để tìm bộ thông số ổn định nhất.</li>
          </ul>
        </article>
      </div>

      <article className="card" style={{ marginTop: 16 }}>
        <h2 className={styles.cardTitle}>Tính năng cốt lõi</h2>
        <div className={styles.featureGrid}>
          {hedgingFeatures.map((feature) => (
            <div key={feature.title} className={styles.feature}>
              <span className={styles.featureIcon} aria-hidden="true">{feature.icon}</span>
              <strong>{feature.title}</strong>
              <p>{feature.description}</p>
            </div>
          ))}
        </div>
      </article>
      <div className={styles.techTags}>{hedgingTech.map((tech) => <span key={tech} className={styles.techTag}>{tech}</span>)}</div>
    </section>
  )
}

function StateMachine() {
  return (
    <div className={styles.stateMachine}>
      <div className={styles.stateNode}><strong>WAIT_SHORT</strong><span>Chờ tín hiệu short đủ điều kiện</span></div>
      <div className={styles.stateArrow}><span className={styles.condition}>spread &lt; threshold &amp; streak ≤ -N &amp; Signal5 ✓</span><span>↓ Gửi email SHORT signal</span></div>
      <div className={`${styles.stateNode} ${styles.green}`}><strong>WAIT_OUT</strong><span>Đang giữ lệnh — chờ điều kiện exit</span></div>
      <div className={styles.stateArrow}><span className={styles.condition}>TP hit / streak đảo chiều / EOD</span><span>↓ Gửi email EXIT signal</span></div>
      <div className={styles.stateNode}><strong>WAIT_SHORT</strong><span>Reset — chờ tín hiệu tiếp theo</span></div>
    </div>
  )
}

function Rules() {
  return (
    <div className={styles.rules}>
      <div>
        <h3 className={`${styles.rulesTitle} ${styles.shortTitle}`}>✅ Điều kiện SHORT</h3>
        <ul className={styles.ruleList}>{shortRules.map((rule) => <li key={rule}>{rule}</li>)}</ul>
      </div>
      <div>
        <h3 className={`${styles.rulesTitle} ${styles.exitTitle}`}>❌ Điều kiện EXIT</h3>
        <ul className={`${styles.ruleList} ${styles.exit}`}>{exitRules.map((rule) => <li key={rule}>{rule}</li>)}</ul>
      </div>
    </div>
  )
}

function Workflow() {
  return (
    <section>
      <h2>🔄 Quy trình ETL & Kiến trúc Dữ liệu</h2>
      <div className={styles.pipelineGrid}>
        {hedgingPipeline.map((step) => (
          <article key={step.number} className={styles.pipelineStep}>
            <div className={styles.pipelineNumber}>{step.number}</div>
            <div className={styles.pipelineTitle}>{step.title}</div>
            <ul>{step.items.map((item) => <li key={item}>{item}</li>)}</ul>
          </article>
        ))}
      </div>
      <hr className={styles.divider} />
      <div className="twoColumn">
        <article className="card">
          <h2 className={styles.cardTitle}>State machine — ALERT_EMAIL</h2>
          <StateMachine />
        </article>
        <article className="card">
          <h2 className={styles.cardTitle}>Entry & exit rules</h2>
          <Rules />
        </article>
      </div>
    </section>
  )
}

function SourceCode() {
  const project = getProject('hedging_vn30f1m')
  return (
    <section className={styles.sourceSection}>
      <h2>💻 Source Code & Data Model</h2>
      <p>Toàn bộ mã nguồn, cấu trúc luồng xử lý dữ liệu (ETL) và kịch bản tự động hóa của dự án được quản lý tập trung và phân module chi tiết trên GitHub.</p>
      <a className="button buttonSecondary" href={project.githubUrl} target="_blank" rel="noopener noreferrer">💻 Xem chi tiết Repository trên GitHub</a>
      <hr className={styles.divider} />
      <h2>🏗️ Signal Visualization</h2>
      <InteractiveChartEmbed />
    </section>
  )
}

function Backtest() {
  return (
    <section>
      <h2>📊 Kết quả Backtest & Tối ưu hóa tham số</h2>
      <BacktestExplorer />
      <article className="card" style={{ marginTop: 16 }}>
        <h2 className={styles.cardTitle}>Phương pháp Walk-Forward (Planned)</h2>
        <div className={styles.plannedGrid}>
          <article><strong>In-sample (Train)</strong><p>60 ngày giao dịch. Chạy Grid search để tìm kiếm bộ tham số tối ưu (Spread threshold, Streak) trên tập dữ liệu lịch sử này.</p></article>
          <article><strong>Out-of-sample (Test)</strong><p>20 ngày giao dịch tiếp theo. Kiểm nghiệm hiệu năng bằng bộ tham số tối ưu từ In-sample để đánh giá mức độ Overfitting.</p></article>
          <article><strong>Roll forward</strong><p>Tịnh tiến cửa sổ thời gian thêm 20 ngày và lặp lại liên tục quy trình Train-Test, so sánh tỉ mỉ hiệu năng giữa hai tập để đảm bảo độ tin cậy.</p></article>
        </div>
      </article>
    </section>
  )
}

function EmailCard({ preview }: { preview: EmailPreview }) {
  return (
    <div className={styles.emailPreview}>
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
    </div>
  )
}

function AlertEmail() {
  return (
    <section className={styles.emailLayout}>
      <article className={`card ${styles.emailSummary}`}>
        <h2 className={styles.cardTitle}>State Machine & Tự động hóa</h2>
        <StateMachine />
        <hr className={styles.divider} />
        <strong>DAILY SUMMARY</strong>
        <div className={styles.dailySummary}>Cuối mỗi phiên (lúc 14:45), hệ thống tự động tổng hợp kết quả giao dịch trong ngày bao gồm: số lượng lệnh, tổng P&amp;L tạm tính, Win rate và tham số áp dụng, sau đó gửi email định dạng HTML cho Trader.</div>
      </article>
      <ProjectTabs
        label="Mẫu email cảnh báo"
        tabs={emailPreviews.map((preview) => ({ id: preview.id, label: preview.label, content: <EmailCard preview={preview} /> }))}
      />
    </section>
  )
}

export default function HedgingPage() {
  return (
    <>
      <ProjectPageHeader
        title="📉 VN30F1M Intraday Hedging System"
        description="Hệ thống giao dịch phái sinh tự động hóa toàn diện cho hợp đồng tương lai VN30F1M — từ ETL dữ liệu OHLCV intraday, phát hiện tín hiệu short dựa trên MA spread ratio & streak count, đến backtest walk-forward và gửi cảnh báo email theo state machine thời gian thực."
      />
      <ProjectTabs
        label="Chi tiết dự án Hedging VN30F1M"
        tabs={[
          { id: 'overview', label: 'Tổng quan', content: <Overview /> },
          { id: 'workflow', label: 'Quy trình', content: <Workflow /> },
          { id: 'source', label: 'Source code', content: <SourceCode /> },
          { id: 'backtest', label: 'Backtest', content: <Backtest /> },
          { id: 'alert', label: 'Alert Email', content: <AlertEmail /> },
        ]}
      />
    </>
  )
}
