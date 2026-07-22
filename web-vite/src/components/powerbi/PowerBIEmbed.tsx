import { useEffect, useRef, useState } from 'react'
import styles from './PowerBIEmbed.module.css'

export interface PowerBIEmbedProps {
  title: string
  embedUrl: string
  aspectRatio?: string
}

export function PowerBIEmbed({ title, embedUrl, aspectRatio = '16 / 9' }: PowerBIEmbedProps) {
  const [status, setStatus] = useState<'loading' | 'loaded' | 'error'>('loading')
  const [attempt, setAttempt] = useState(0)
  const containerRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    setStatus('loading')
    const timeout = window.setTimeout(() => setStatus((current) => current === 'loading' ? 'error' : current), 18000)
    return () => window.clearTimeout(timeout)
  }, [embedUrl, attempt])

  if (!embedUrl) {
    return (
      <div className={styles.emptyState} role="status">
        <span className={styles.emptyIcon} aria-hidden="true">📊</span>
        <strong>Báo cáo đang được hoàn thiện</strong>
        <span>Nội dung Power BI sẽ được cập nhật trong thời gian tới.</span>
      </div>
    )
  }

  const openFullscreen = async () => {
    try { await containerRef.current?.requestFullscreen() } catch { setStatus('error') }
  }

  return (
    <div className={styles.wrapper}>
      <div ref={containerRef} className={styles.embedShell} style={{ aspectRatio }}>
        {status === 'loading' && (
          <div className={styles.loading} role="status">
            <span className={styles.spinner} aria-hidden="true" />
            <span>Power BI đang tải…</span>
          </div>
        )}
        <iframe
          key={attempt}
          className={styles.iframe}
          src={embedUrl}
          title={title}
          loading="lazy"
          allow="fullscreen"
          allowFullScreen
          referrerPolicy="strict-origin-when-cross-origin"
          onLoad={() => setStatus('loaded')}
          onError={() => setStatus('error')}
        >
          Không thể tải Power BI. Hãy mở báo cáo bằng trình duyệt hiện đại.
        </iframe>
        {status === 'error' && (
          <div className={styles.fallback} role="alert">
            <strong>Không thể xác nhận báo cáo đã tải.</strong>
            <span>Kiểm tra kết nối hoặc thử tải lại iframe.</span>
            <button type="button" className="button buttonSecondary" onClick={() => setAttempt((value) => value + 1)}>Tải lại</button>
          </div>
        )}
      </div>
      <div className={styles.actions}>
        <button type="button" className="button buttonSecondary" onClick={openFullscreen}>⛶ Toàn màn hình</button>
        <a className="button buttonSecondary" href={embedUrl} target="_blank" rel="noopener noreferrer">Mở báo cáo riêng ↗</a>
      </div>
    </div>
  )
}
