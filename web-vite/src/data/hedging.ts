export const hedgingFeatures = [
  { icon: '📡', title: 'ETL Intraday', description: 'Tự động lấy OHLCV từ SSI API, chuẩn hóa theo khung thời gian 1-min / 5-min, lưu trữ RDS.' },
  { icon: '🧮', title: 'Signal Engine', description: 'MA spread ratio, negative streak, had_positive_today flag, Signal5 confirmation, hedge nhánh early entry.' },
  { icon: '📊', title: 'Backtest Engine', description: 'Grid search tham số, walk-forward validation, candlestick chart tích hợp trade annotation.' },
  { icon: '📧', title: 'Alert Email', description: 'State machine persist qua file, 3 loại email: SHORT signal, EXIT signal, Daily summary.' },
  { icon: '🔁', title: 'Auto Refresh', description: 'HTML chart tự động refresh mỗi 5 phút trong phiên, xuất báo cáo cuối ngày.' },
  { icon: '🎯', title: 'TP Tiers', description: 'Take-profit nhiều mức, streak-based exit, stop-loss tự động. Logic exit tích hợp trong get_trade_log.' },
]

export const hedgingTech = ['Data Processing', 'Automated Scripting', 'Interactive Charts', 'SSI FastConnect', 'VN30F1M Futures', 'Entry/Exit Logic', 'Backtesting', 'Walk-forward', 'Grid Search']

export const hedgingPipeline = [
  { number: '01 / Extract', title: 'Data Ingestion', items: ['Kết nối SSI FastConnect API và DNSE API', 'Thu thập dữ liệu OHLCV theo khung 1 phút (intraday)'] },
  { number: '02 / Transform', title: 'Signal Processing', items: ['Chuẩn hóa dữ liệu OHLCV, xử lý timestamp', 'Tính MA ngắn/dài hạn và spread ratio', 'Xây dựng các điều kiện tín hiệu vào/ra lệnh'] },
  { number: '03 / Validate', title: 'Backtest & Optimization', items: ['Mô phỏng chiến lược trên dữ liệu lịch sử (1 trade/ngày)', 'Cơ chế thoát lệnh: TP cố định + streak exit 2 tầng', 'Grid search ~300+ tổ hợp tham số (spread, streak, nb_except)', 'Đánh giá theo win rate, avg P&L, total P&L'] },
  { number: '04 / Alert', title: 'Output & Monitoring', items: ['State machine 2 trạng thái (WAIT_SHORT / WAIT_OUT) — lưu trạng thái ra file .rds theo ngày, chống gửi tín hiệu trùng', 'Gửi email cảnh báo theo thời gian thực (EARLY WARNING → SHORT → OUT)', 'Biểu đồ HTML tự động cập nhật', 'Tổng kết P&L hàng ngày'] },
]

export const shortRules = [
  'No trades in the first 5 minutes after market open.',
  'MA spread ratio < ngưỡng âm (từ grid search)',
  'Streak âm liên tiếp ≥ N candle',
  'MA cross down today: TRUE',
  'Signal_special xác nhận (Volume spike + spread cực âm)',
]

export const exitRules = [
  'Take-profit : đạt mốc +X pts',
  'Spread ratio đảo chiều về dương > ngưỡng dương (từ grid search)',
  'Streak dương liên tiếp ≥ N candle',
  'Tự động đóng lệnh vào cuối ngày',
]

export interface EmailPreview {
  id: string
  label: string
  subject: string
  meta: string
  tone: 'short' | 'exit' | 'daily'
  rows: Array<[string, string, 'normal' | 'red' | 'green' | 'purple']>
  footer?: string
}

export const emailPreviews: EmailPreview[] = [
  {
    id: 'short', label: '📉 SHORT signal', subject: '📉 [SIGNAL] SHORT VN30F1M — 10:44 | 28/05/2026',
    meta: 'From: nhat.vophuoc@gmail.com · To: nhat.vophuoc@gmail.com', tone: 'short',
    rows: [
      ['Prices Current', '2,012.2', 'normal'], ['MA spread ratio', '-0.216 (vượt ngưỡng)', 'red'],
      ['Streak count', '20 candle âm liên tiếp', 'red'], ['Has positive spread', 'TRUE ✓', 'green'],
      ['Except', '5', 'green'], ['TP target', '1,999 (−13.2 pts)', 'normal'],
      ['Stop loss', '2,024 (+11.8 pts)', 'red'], ['State mới', 'WAIT_OUT', 'purple'],
    ],
  },
  {
    id: 'exit', label: '✅ EXIT signal', subject: '✅ [EXIT] VN30F1M — PnL: +22.1 pts | 14:45',
    meta: 'From: nhat.vophuoc@gmail.com · To: nhat.vophuoc@gmail.com', tone: 'exit',
    rows: [
      ['Entry', '2,012.2 at 10:44', 'normal'], ['Exit', '1,990.1 at 14:45', 'normal'],
      ['PnL', '+22.1 pts', 'green'], ['%PnL', '~1.1%', 'green'],
      ['Reason exit', 'End of day', 'normal'], ['Hold duration', '241 minutes', 'normal'],
      ['State mới', 'DONE FOR TODAY', 'purple'],
    ],
    footer: 'Trade #3 hôm nay. Tổng PnL tạm tính: +26.6 pts. Phiên giao dịch đã kết thúc.',
  },
  {
    id: 'daily', label: '📊 Daily summary', subject: '📊 [DAILY] VN30F1M Summary — 28/05/2026',
    meta: 'From: nhat.vophuoc@gmail.com · To: nhat.vophuoc@gmail.com', tone: 'daily',
    rows: [
      ['Tổng số trade', '4', 'normal'], ['Win / Loss', '3W / 1L', 'normal'],
      ['Win rate ngày', '75%', 'green'], ['Tổng PnL (pts)', '+10.2 pts', 'green'],
      ['Best trade', '+4.4 pts (10:44–11:01)', 'normal'], ['Worst trade', '-3.1 pts (10:30–11:15)', 'red'],
      ['Tham số dùng', 'spread -0.0025 / streak -3', 'normal'],
    ],
    footer: 'Ngày mai pipeline sẽ tiếp tục với cùng tham số. Kiểm tra biểu đồ chi tiết tại dashboard.',
  },
]
