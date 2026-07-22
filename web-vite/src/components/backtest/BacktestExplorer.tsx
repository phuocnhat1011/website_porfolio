import { useEffect, useMemo, useState } from 'react'
import type { BacktestDataset, BacktestRow } from '../../types'
import styles from './BacktestExplorer.module.css'

type Rank = 'Good' | 'Avg' | 'Bad'

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

function RowStatus({ rank, index, trades }: { rank: Rank; index: number; trades: number }) {
  const label = rank === 'Good' ? (index === 0 ? 'Best' : 'Tốt') : rank === 'Avg' ? 'Trung bình' : trades < 100 ? 'Chưa tốt' : 'Nhiều noise'
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
      <div className={styles.rankControl} role="group" aria-label="Lọc kết quả theo Rank">
        <span>Rank</span>
        {(['Good', 'Avg', 'Bad'] as const).map((item) => (
          <button key={item} type="button" aria-pressed={rank === item} onClick={() => setRank(item)}>{item}</button>
        ))}
      </div>

      <div className={styles.kpiGrid} aria-label="Chỉ số tốt nhất trong nhóm đã chọn">
        <article className="surface"><span>Win rate</span><strong className={styles.positive}>{best ? `${best[7].toFixed(1)}%` : '0.0%'}</strong></article>
        <article className="surface"><span>Avg profit / trade</span><strong>{best ? `${signed(best[8], 2)} pts` : '0.00 pts'}</strong></article>
        <article className="surface"><span>Total PnL</span><strong className={styles.total}>{best ? `${signed(best[9], 1)} pts` : '0.0 pts'}</strong></article>
        <article className="surface"><span>Tổng trade</span><strong className={styles.trades}>{best ? best[6] : 0}</strong></article>
      </div>

      <div className={`card ${styles.tableCard}`}>
        <div className={styles.tableHeading}>
          <h3>Grid Search — Spread & Streak Parameters ({filteredRows.length} kết quả)</h3>
          <a className="button buttonSecondary" href="/documents/data-backtesting.xlsx" download>Tải Excel gốc</a>
        </div>
        <div className={styles.tableWrap} tabIndex={0} aria-label={`Bảng ${filteredRows.length} kết quả backtest nhóm ${rank}`}>
          <table>
            <thead><tr><th>Spread In</th><th>Streak In</th><th>Spread Out</th><th>Streak Out</th><th>Except</th><th>TP</th><th>Win Rate</th><th>Avg PnL</th><th>Total PnL</th><th>Tổng Trade</th><th>Đánh giá</th></tr></thead>
            <tbody>
              {filteredRows.length === 0 ? <tr><td colSpan={11} className={styles.empty}>Không có dữ liệu phù hợp</td></tr> : filteredRows.map((row, index) => {
                const [spreadIn, streakIn, spreadOut, streakOut, nbExcept, takeProfit, nbTrades, winRate, avgPnl, totalPnl] = row
                return (
                  <tr key={`${spreadIn}-${streakIn}-${spreadOut}-${streakOut}-${nbExcept}-${takeProfit}`}>
                    <td className={styles.mono}>{spreadIn}</td><td>{streakIn}</td><td className={styles.mono}>{spreadOut}</td><td>{streakOut}</td><td>{nbExcept}</td><td>{Number.isInteger(takeProfit) ? takeProfit : takeProfit.toFixed(1)}</td><td className={styles.positive}>{winRate.toFixed(1)}%</td><td className={avgPnl >= 0 ? styles.positive : styles.negative}>{signed(avgPnl, 2)} pts</td><td className={totalPnl >= 0 ? styles.positive : styles.negative}>{signed(totalPnl, 1)} pts</td><td>{nbTrades}</td><td><RowStatus rank={rank} index={index} trades={nbTrades} /></td>
                  </tr>
                )
              })}
            </tbody>
          </table>
        </div>
        <p className={styles.note}>* Số liệu trên đây là kết quả backtest thực tế từ Intraday VN30F1M từ đầu năm 2026 tới nay.</p>
      </div>
    </section>
  )
}
