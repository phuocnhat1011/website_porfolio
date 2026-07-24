import { useEffect, useMemo, useState } from 'react'
import type { BacktestDataset, BacktestRow } from '../../types'
import styles from './BacktestExplorer.module.css'

type Rank = 'Good' | 'Avg' | 'Bad'

const rankLabels: Record<Rank, string> = {
  Good: 'Good',
  Avg: 'Average',
  Bad: 'Weak',
}

const filterRows = (rows: BacktestRow[], rank: Rank) => {
  const filtered = rows.filter((row) => {
    const winRate = row[7]
    const totalPnl = row[9]
    if (rank === 'Good') return winRate > 60 && totalPnl > 200
    if (rank === 'Avg') return winRate > 50 && winRate < 60 && totalPnl > 150 && totalPnl < 200
    return winRate < 50 && totalPnl < 150
  })
  return filtered.sort((a, b) => rank === 'Bad' ? b[7] - a[7] : b[8] - a[8])
}

const signed = (value: number, digits: number) => `${value >= 0 ? '+' : ''}${value.toFixed(digits)}`

function RowStatus({ rank, index }: { rank: Rank; index: number }) {
  const label = rank === 'Good' ? (index === 0 ? 'Best' : 'Good') : rank === 'Avg' ? 'Average' : 'Weak'
  return <span className={`${styles.pill} ${rank === 'Good' ? styles.best : rank === 'Avg' ? styles.mid : styles.low}`}>{label}</span>
}

export function BacktestExplorer() {
  const [dataset, setDataset] = useState<BacktestDataset | null>(null)
  const [rank, setRank] = useState<Rank>('Good')
  const [error, setError] = useState('')

  useEffect(() => {
    const controller = new AbortController()
    fetch('/data/backtesting.json', { signal: controller.signal })
      .then((response) => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`)
        return response.json() as Promise<BacktestDataset>
      })
      .then(setDataset)
      .catch((reason: unknown) => {
        if (reason instanceof DOMException && reason.name === 'AbortError') return
        setError(reason instanceof Error ? reason.message : 'Unknown error')
      })
    return () => controller.abort()
  }, [])

  const filteredRows = useMemo(() => dataset ? filterRows(dataset.rows, rank) : [], [dataset, rank])
  const best = filteredRows[0]

  if (error) {
    return <div className="notice">⚠️ Không thể tải dữ liệu backtest ({error}). Bạn vẫn có thể <a href="/documents/data-backtesting.xlsx" download>tải workbook gốc</a>.</div>
  }

  if (!dataset) return <div className={styles.loading} role="status">Đang tải 1.296 kết quả backtest…</div>

  return (
    <section>
      <div className={styles.rankControl} role="group" aria-label="Filter results by performance tier">
        <span>Performance Tier</span>
        {(['Good', 'Avg', 'Bad'] as const).map((item) => (
          <button key={item} type="button" aria-pressed={rank === item} onClick={() => setRank(item)}>{rankLabels[item]}</button>
        ))}
      </div>

      <div className={styles.kpiBlock}>
        <div className={styles.kpiGrid} aria-label="Metrics for the highest-ranked parameter set in the selected tier">
          <article className="surface"><span>WIN RATE</span><strong className={styles.positive}>{best ? `${best[7].toFixed(1)}%` : '0.0%'}</strong></article>
          <article className="surface"><span>AVG P&amp;L / TRADE</span><strong>{best ? `${signed(best[8], 2)} pts` : '0.00 pts'}</strong></article>
          <article className="surface"><span>TOTAL P&amp;L</span><strong className={styles.total}>{best ? `${signed(best[9], 1)} pts` : '0.0 pts'}</strong></article>
          <article className="surface"><span>TOTAL TRADES</span><strong className={styles.trades}>{best ? best[6] : 0}</strong></article>
        </div>
        <p className={styles.kpiCaption}>Metrics reflect the highest-ranked parameter set in the selected tier.</p>
      </div>

      <div className={`card ${styles.tableCard}`}>
        <div className={styles.tableHeading}>
          <h3>Grid Search Results — Spread &amp; Streak Parameters ({filteredRows.length} configurations)</h3>
          <a className="button buttonSecondary" href="/documents/data-backtesting.xlsx" download>Download Raw Results</a>
        </div>
        <div className={styles.tableWrap} tabIndex={0} aria-label={`${filteredRows.length} Backtest configurations in the ${rankLabels[rank]} tier`}>
          <table>
            <thead><tr><th>Spread In</th><th>Streak In</th><th>Spread Out</th><th>Streak Out</th><th>Except</th><th>TP</th><th>Win Rate</th><th>Avg PnL</th><th>Total PnL</th><th>Tổng Trade</th><th>RATING</th></tr></thead>
            <tbody>
              {filteredRows.length === 0 ? <tr><td colSpan={11} className={styles.empty}>Không có dữ liệu phù hợp</td></tr> : filteredRows.map((row, index) => {
                const [spreadIn, streakIn, spreadOut, streakOut, nbExcept, takeProfit, nbTrades, winRate, avgPnl, totalPnl] = row
                return (
                  <tr
                    key={`${spreadIn}-${streakIn}-${spreadOut}-${streakOut}-${nbExcept}-${takeProfit}`}
                    className={index === 0 ? styles.representativeRow : undefined}
                  >
                    <td className={styles.mono}>{spreadIn}</td><td>{streakIn}</td><td className={styles.mono}>{spreadOut}</td><td>{streakOut}</td><td>{nbExcept}</td><td>{Number.isInteger(takeProfit) ? takeProfit : takeProfit.toFixed(1)}</td><td className={styles.positive}>{winRate.toFixed(1)}%</td><td className={avgPnl >= 0 ? styles.positive : styles.negative}>{signed(avgPnl, 2)} pts</td><td className={totalPnl >= 0 ? styles.positive : styles.negative}>{signed(totalPnl, 1)} pts</td><td>{nbTrades}</td><td><RowStatus rank={rank} index={index} /></td>
                  </tr>
                )
              })}
            </tbody>
          </table>
        </div>
        <div className={styles.disclosures}>
          <p>P&amp;L được biểu diễn theo điểm VN30F1M.</p>
          <p>Kết quả chưa bao gồm phí giao dịch và slippage.</p>
          <p>Số liệu là historical simulation trên dữ liệu VN30F1M intraday từ đầu năm 2026 tới nay và không đại diện cho hiệu suất tương lai.</p>
        </div>
      </div>
    </section>
  )
}
