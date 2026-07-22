import type { Project } from '../types'

export const projects: Project[] = [
  {
    id: 'bank_bctc',
    title: 'Phân tích BCTC Ngân hàng VN',
    status: 'DOING',
    tagline: '',
    stack: ['R/Python', 'Power BI', 'DAX', 'Data Modeling', 'Financial Analysis', 'AI-assisted Extraction'],
    highlights: [
      'Tự động crawl BCTC ngành chứng khoán từ SSI và chuẩn hoá dữ liệu theo kỳ/công ty/chỉ tiêu',
      'Thiết kế mô hình Dim/Fact bằng R & Python để tối ưu phân tích đa chiều và so sánh theo công ty/toàn ngành',
    ],
    whatIDid: [
      'Crawl và chuẩn hoá dữ liệu BCTC ngành chứng khoán từ SSI bằng Python (pipeline thu thập + làm sạch)',
      'Thiết kế schema Dim/Fact (Company/Date/Item → Fact values) để hỗ trợ phân tích theo nhiều lát cắt',
      'Xây dựng hệ measures DAX (giá trị, tăng trưởng, hiệu suất, so sánh) và tối ưu tính tái sử dụng',
      'Xây dựng Power BI report theo module (menu tiles), hỗ trợ cross-filter và drill nhanh insight',
    ],
    process: [
      'Data acquisition: crawl BCTC từ SSI, chuẩn hoá định dạng và kiểm soát chất lượng dữ liệu',
      'Data modeling: xây dựng Dim/Fact bằng Python (kỳ, công ty, chỉ tiêu) để tối ưu truy vấn và phân tích',
      'DAX layer: phát triển measures (value, YoY/QoQ, hiệu suất, so sánh) và chuẩn hoá measure table',
      'Reporting: thiết kế UX theo module, hoàn thiện report và chuẩn bị publish/embed',
    ],
    cover: '/images/bank-bctc.webp',
    coverOriginal: '/images/bank-bctc.png',
    route: '/projects/banking',
    powerBiUrl: '',
    visibleOnHome: false,
    visibleInNavigation: false,
  },
  {
    id: 'securities_vn',
    title: 'Phân tích BCTC Chứng khoán VN',
    status: 'DONE',
    tagline: '',
    stack: ['Power BI', 'DAX', 'Python/R', 'Data Modeling', 'Financial Analysis', 'PDF Parsing accurate'],
    highlights: [
      'Tự động crawl BCTC ngành chứng khoán từ SSI và chuẩn hoá dữ liệu theo kỳ/công ty/chỉ tiêu',
      'Thiết kế mô hình Dim/Fact bằng Python để tối ưu phân tích đa chiều và so sánh theo công ty/toàn ngành',
      'Drill-down vào thuyết minh FVTPL & AFS (khoản mục trọng yếu của CTCK) bằng pipeline Python + AI',
    ],
    whatIDid: [
      'Crawl và chuẩn hoá dữ liệu BCTC ngành chứng khoán từ SSI bằng Python (pipeline thu thập + làm sạch)',
      'Thiết kế schema Dim/Fact (Company/Date/Item → Fact values) để hỗ trợ phân tích theo nhiều lát cắt',
      'Xây dựng hệ measures DAX (giá trị, tăng trưởng, hiệu suất, so sánh) và tối ưu tính tái sử dụng',
      'Crawl & cấu trúc thuyết minh FVTPL và AFS bằng Python kết hợp AI để bổ sung lớp phân tích trọng yếu',
      'Xây dựng Power BI report theo module (menu tiles), hỗ trợ cross-filter và drill nhanh insight',
    ],
    process: [
      'Data acquisition: crawl BCTC từ SSI, chuẩn hoá định dạng và kiểm soát chất lượng dữ liệu',
      'Data modeling: xây dựng Dim/Fact bằng Python (kỳ, công ty, chỉ tiêu) để tối ưu truy vấn và phân tích',
      'DAX layer: phát triển measures (value, YoY/QoQ, hiệu suất, so sánh) và chuẩn hoá measure table',
      'Deep-dive notes: trích xuất & cấu trúc thuyết minh FVTPL/AFS bằng Python + AI',
      'Reporting: thiết kế UX theo module, hoàn thiện report và chuẩn bị publish/embed',
    ],
    cover: '/images/securities-vn.webp',
    coverOriginal: '/images/securities-vn.png',
    route: '/projects/securities',
    powerBiUrl: 'https://app.powerbi.com/view?r=eyJrIjoiMjhmZDQzMTQtODFkNy00YjljLTlhMGEtNWM2NmM3ZjlkYjliIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9',
    visibleOnHome: true,
    visibleInNavigation: true,
  },
  {
    id: 'hedging_vn30f1m',
    title: 'Hệ thống Hedging VN30F1M',
    status: 'DONE',
    tagline: '',
    stack: ['Data Processing', 'Automated Scripting', 'Interactive Charts', 'SSI FastConnect', 'Entry/Exit Logic', 'Backtesting'],
    highlights: [
      'ETL OHLCV 1-min từ SSI FastConnect, chuẩn hóa bằng R data.table',
      'Tính toán tín hiệu short dựa trên MA spread ratio, streak count, Signal5 confirmation',
      'State machine WAIT_SHORT ↔ WAIT_OUT + email alert realtime',
    ],
    whatIDid: [
      'Tự động lấy dữ liệu OHLCV 1-min intraday từ SSI API, chuẩn hóa và lưu trữ RDS',
      'Thiết kế signal engine phát hiện tín hiệu Short bằng MA spread ratio, negative streak và confirmation filter',
      'Xây dựng backtest engine mô phỏng giao dịch, walk-forward validation và tối ưu hóa tham số',
      'Phát triển bộ cảnh báo email realtime qua state machine (WAIT_SHORT, WAIT_OUT) và gửi báo cáo cuối ngày',
    ],
    process: [
      'Data acquisition: tự động lấy dữ liệu 1-min từ SSI API và lưu trữ RDS',
      'Signal processing: lập trình bộ tính toán tín hiệu dựa trên mean-reversion và streak count',
      'Backtesting: chạy mô phỏng giao dịch, walk-forward validation để tối ưu tham số',
      'Output & alerting: tích hợp state machine và email alert tự động realtime',
    ],
    cover: '/images/hedging-vn30f1m.webp',
    coverOriginal: '/images/hedging-vn30f1m.png',
    route: '/projects/hedging',
    githubUrl: 'https://github.com/phuocnhat1011/VN30F1M_HEDGING',
    visibleOnHome: true,
    visibleInNavigation: true,
  },
]

export const getProject = (id: Project['id']) => {
  const project = projects.find((item) => item.id === id)
  if (!project) throw new Error(`Missing project configuration: ${id}`)
  return project
}
