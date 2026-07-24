export const hedgingSolutions = [
  {
    number: '01',
    title: 'Intraday Data Pipeline',
    description: 'Thu thập và chuẩn hóa OHLCV một phút từ nguồn SSI/DNSE.',
  },
  {
    number: '02',
    title: 'Signal Engine',
    description: 'Tính MA spread ratio, streak logic và các điều kiện xác nhận tín hiệu.',
  },
  {
    number: '03',
    title: 'Backtesting Engine',
    description: 'Grid Search nhiều bộ tham số và đánh giá bằng Win Rate, Avg P&L, Total P&L.',
  },
  {
    number: '04',
    title: 'State Machine & Alerts',
    description: 'Quản lý trạng thái tín hiệu, email cảnh báo, daily summary và lớp tích hợp execution.',
  },
]

export const analyticalValues = [
  {
    title: 'Tín hiệu có thể tái lập',
    description: 'Tín hiệu được tạo bằng bộ quy tắc rõ ràng và có thể kiểm tra lại.',
  },
  {
    title: 'So sánh tham số nhất quán',
    description: 'So sánh nhiều tổ hợp tham số bằng cùng một framework Backtest.',
  },
  {
    title: 'Tự động hóa có kiểm soát',
    description: 'State Machine kiểm soát vòng đời tín hiệu và tránh cảnh báo trùng lặp.',
  },
]

export const hedgingTech = [
  'R',
  'Financial Time Series',
  'Backtesting',
  'Grid Search',
  'State Machine',
  'SSI FastConnect',
]

export const pipelineSummary = [
  'SSI / DNSE',
  'OHLCV Processing',
  'Signal Rules',
  'Grid Search Backtest',
  'State Machine',
  'Alerts / Execution',
]

export const hedgingPipeline = [
  {
    number: '01',
    label: 'DATA',
    title: 'Data Ingestion',
    items: [
      'Kết nối SSI FastConnect và DNSE.',
      'Thu thập OHLCV một phút.',
      'Chuẩn hóa timestamp và cấu trúc dữ liệu.',
    ],
  },
  {
    number: '02',
    label: 'SIGNAL',
    title: 'Signal Processing',
    items: [
      'Tính MA ngắn và MA dài.',
      'Tính spread ratio và streak count.',
      'Tạo điều kiện tín hiệu dựa trên bộ quy tắc.',
    ],
  },
  {
    number: '03',
    label: 'VALIDATION',
    title: 'Backtesting & Validation',
    items: [
      'Backtesting trên dữ liệu lịch sử.',
      'Grid Search các tổ hợp tham số.',
      'Xếp hạng theo Win Rate, Avg P&L và Total P&L.',
      'Walk-forward là bước kiểm định dự kiến tiếp theo.',
    ],
  },
  {
    number: '04',
    label: 'MONITORING',
    title: 'Alert Monitoring',
    items: [
      'State Machine WAIT_SHORT / WAIT_OUT.',
      'Email SHORT / EXIT và báo cáo cuối ngày.',
      'Auto-refresh và lưu log trạng thái.',
    ],
  },
]

export const shortRules = [
  'Không phát tín hiệu trong 5 phút đầu phiên.',
  'MA spread ratio thấp hơn ngưỡng âm từ Grid Search.',
  'Streak âm liên tiếp đạt điều kiện N candle.',
  'MA cross down trong phiên được xác nhận.',
  'Tín hiệu xác nhận bổ sung: volume spike và spread âm mạnh.',
]

export const exitRules = [
  'Take-profit đạt mốc +X điểm.',
  'Spread ratio đảo chiều về ngưỡng dương từ Grid Search.',
  'Streak dương liên tiếp đạt điều kiện N candle.',
  'Phát tín hiệu thoát bắt buộc vào cuối ngày.',
]

export const automationControls = [
  'Tránh gửi cảnh báo trùng.',
  'Lưu trạng thái giữa các lần chạy.',
  'Gửi báo cáo cuối ngày.',
  'Lưu log tín hiệu và trạng thái.',
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

const demoEmailMeta = 'From: automated-alert@portfolio-demo · To: analyst@portfolio-demo'

export const emailPreviews: EmailPreview[] = [
  {
    id: 'short',
    label: 'SHORT Signal',
    subject: '📉 [SIGNAL] SHORT VN30F1M — 10:44 | 28/05/2026',
    meta: demoEmailMeta,
    tone: 'short',
    rows: [
      ['Giá hiện tại', '2,012.2', 'normal'],
      ['MA spread ratio', '-0.216 (vượt ngưỡng)', 'red'],
      ['Streak count', '20 candle âm liên tiếp', 'red'],
      ['Has positive spread', 'TRUE ✓', 'green'],
      ['Except', '5', 'green'],
      ['TP target', '1,999 (−13.2 pts)', 'normal'],
      ['Stop loss', '2,024 (+11.8 pts)', 'red'],
      ['Trạng thái mới', 'WAIT_OUT', 'purple'],
    ],
  },
  {
    id: 'exit',
    label: 'EXIT Signal',
    subject: '✅ [EXIT] VN30F1M — P&L: +22.1 pts | 14:45',
    meta: demoEmailMeta,
    tone: 'exit',
    rows: [
      ['Entry', '2,012.2 at 10:44', 'normal'],
      ['Exit', '1,990.1 at 14:45', 'normal'],
      ['P&L', '+22.1 pts', 'green'],
      ['%P&L', '~1.1%', 'green'],
      ['Lý do thoát', 'End of day', 'normal'],
      ['Thời gian giữ', '241 phút', 'normal'],
      ['Trạng thái mới', 'DONE FOR TODAY', 'purple'],
    ],
    footer: 'Trade #3 hôm nay. Tổng P&L tạm tính: +26.6 pts. Phiên giao dịch đã kết thúc.',
  },
  {
    id: 'daily',
    label: 'Daily Summary',
    subject: '📊 [DAILY] VN30F1M Summary — 28/05/2026',
    meta: demoEmailMeta,
    tone: 'daily',
    rows: [
      ['Tổng số lệnh', '4', 'normal'],
      ['Win / Loss', '3W / 1L', 'normal'],
      ['Win Rate ngày', '75%', 'green'],
      ['Tổng P&L (pts)', '+10.2 pts', 'green'],
      ['Best trade', '+4.4 pts (10:44–11:01)', 'normal'],
      ['Worst trade', '-3.1 pts (10:30–11:15)', 'red'],
      ['Tham số dùng', 'spread -0.0025 / streak -3', 'normal'],
    ],
    footer: 'Pipeline tiếp tục ở phiên kế tiếp với cùng tham số. Biểu đồ chi tiết được lưu tại dashboard.',
  },
]
