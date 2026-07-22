import { useState } from 'react'
import styles from './InteractiveChartEmbed.module.css'

export function InteractiveChartEmbed() {
  const [status, setStatus] = useState<'loading' | 'loaded' | 'error'>('loading')

  return (
    <div className={styles.shell}>
      {status === 'loading' && <div className={styles.message} role="status">Biểu đồ tương tác đang tải…</div>}
      {status === 'error' && <div className={styles.error} role="alert">Không thể tải biểu đồ. File gốc vẫn có thể mở tại <a href="/charts/vn30f1m.html" target="_blank" rel="noopener noreferrer">đây</a>.</div>}
      <iframe
        src="/charts/vn30f1m.html"
        title="Biểu đồ tín hiệu VN30F1M tương tác"
        loading="lazy"
        onLoad={() => setStatus('loaded')}
        onError={() => setStatus('error')}
      />
    </div>
  )
}
