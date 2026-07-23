export const securitiesTechnologies = [
  'Python',
  'Pandas',
  'PostgreSQL',
  'SQL',
  'Power BI',
  'DAX',
  'Dimensional Modeling',
] as const

export const securitiesMetrics = [
  {
    value: '37+',
    label: 'Công ty chứng khoán',
    detail: 'Phạm vi dữ liệu đa công ty',
  },
  {
    value: '3 nhóm',
    label: 'Báo cáo tài chính',
    detail: 'CĐKT · KQKD · LCTT',
  },
  {
    value: 'PDF/Excel',
    label: '→ Power BI',
    detail: 'Quy trình phân tích tự động',
  },
] as const

export const securitiesOverview = {
  problem:
    'Dữ liệu báo cáo tài chính và danh mục tự doanh của các công ty chứng khoán nằm rải rác trong nhiều file PDF/Excel, khác nhau về cấu trúc, tên chỉ tiêu và kỳ báo cáo. Việc tổng hợp thủ công gây mất thời gian và khó so sánh giữa các công ty.',
  objective:
    'Xây dựng một pipeline có khả năng thu thập, chuẩn hóa và mô hình hóa dữ liệu báo cáo tài chính, tạo nguồn dữ liệu nhất quán cho phân tích đa công ty, đa kỳ và báo cáo Power BI.',
  whatBuilt: [
    {
      title: 'Thu thập tự động',
      description: 'Tự động tải báo cáo theo công ty, năm và kỳ.',
    },
    {
      title: 'Chuẩn hóa dữ liệu BCTC',
      description: 'Chuẩn hóa chỉ tiêu và cấu trúc báo cáo.',
    },
    {
      title: 'Mô hình dữ liệu Dim/Fact',
      description: 'Fact/Dimension dùng chung cho phân tích đa kỳ.',
    },
    {
      title: 'Báo cáo Power BI tương tác',
      description: 'Bộ lọc, drill-down và phân tích so sánh.',
    },
  ],
  businessValue: [
    {
      title: 'Tra cứu nhanh hơn',
      description: 'Rút ngắn đáng kể thời gian tổng hợp và tra cứu.',
    },
    {
      title: 'So sánh nhất quán',
      description: 'So sánh các công ty trên cùng một cấu trúc dữ liệu.',
    },
    {
      title: 'Dữ liệu sẵn sàng phân tích',
      description:
        'Dữ liệu đã chuẩn hóa và kiểm soát chất lượng, sẵn sàng cho truy vấn SQL và báo cáo Power BI.',
    },
  ],
  pipeline: ['PDF / Excel', 'Thu thập', 'Trích xuất', 'Làm sạch & QA', 'Mô hình PostgreSQL', 'Power BI'],
} as const

export interface SecuritiesWorkflowStep {
  number: string
  title: string
  description: string
  input: string
  output: string
  tools: readonly string[]
  note?: string
}

export const securitiesWorkflow: readonly SecuritiesWorkflowStep[] = [
  {
    number: '01',
    title: 'Thu thập dữ liệu',
    description:
      'Tự động tải CĐKT, KQKD và LCTT theo công ty, năm và kỳ báo cáo; tổ chức file theo cấu trúc thư mục nhất quán.',
    input: 'SSI iBoard · Công ty · Kỳ báo cáo',
    output: 'Bộ file báo cáo có cấu trúc',
    tools: ['Python', 'Selenium', 'Requests'],
  },
  {
    number: '02',
    title: 'Trích xuất dữ liệu',
    description:
      'Đọc dữ liệu từ Excel hoặc PDF theo định dạng nguồn. OCR chỉ được sử dụng cho báo cáo dạng ảnh hoặc không có text layer.',
    input: 'PDF · Excel',
    output: 'Bảng dữ liệu đã trích xuất',
    tools: ['Python', 'PDF/Excel parsing', 'OCR fallback'],
  },
  {
    number: '03',
    title: 'Chuẩn hóa & kiểm soát chất lượng',
    description:
      'Chuẩn hóa tên chỉ tiêu, gộp dữ liệu nhiều file, unpivot sang cấu trúc phân tích và kiểm tra tổng nhằm phát hiện các trường hợp sai lệch.',
    input: 'Dữ liệu trích xuất',
    output: 'Dataset chuẩn hóa · Danh sách ngoại lệ',
    tools: ['Python', 'Pandas', 'Validation rules'],
    note: 'Các trường hợp sai lệch được đánh dấu để rà soát có kiểm soát. AI chỉ hỗ trợ rà soát các cấu trúc tài liệu ngoại lệ.',
  },
  {
    number: '04',
    title: 'Mô hình hóa & lưu trữ',
    description:
      'Thiết kế Fact/Dimension, khóa chính và khóa ngoại; lưu dữ liệu tập trung trong PostgreSQL để hỗ trợ truy vấn và Power BI.',
    input: 'Dữ liệu tài chính chuẩn hóa',
    output: 'Mô hình dữ liệu PostgreSQL',
    tools: ['PostgreSQL', 'SQL', 'Dimensional Modeling'],
  },
  {
    number: '05',
    title: 'Phân tích trên Power BI',
    description:
      'Kết nối dữ liệu đã chuẩn hóa vào Power BI, xây dựng DAX measures, slicer theo công ty/kỳ và drill-down cho phân tích chi tiết.',
    input: 'PostgreSQL model',
    output: 'Báo cáo Power BI tương tác',
    tools: ['Power BI', 'DAX'],
  },
] as const

export const verifiedQualityControls = [
  {
    title: 'Chuẩn hóa tên chỉ tiêu',
    description: 'Chuẩn hóa tên chỉ tiêu giữa các công ty và kỳ báo cáo.',
  },
  {
    title: 'Đối chiếu tổng báo cáo',
    description: 'Đối chiếu tổng khoản mục với số tổng trên báo cáo.',
  },
  {
    title: 'Tổ chức theo công ty và kỳ',
    description: 'Tổ chức dữ liệu theo công ty, năm và kỳ báo cáo.',
  },
  {
    title: 'Rà soát ngoại lệ có kiểm soát',
    description: 'Đánh dấu sai lệch để kiểm tra lại theo quy trình có kiểm soát.',
  },
] as const

export const architectureGroups = [
  {
    title: 'Các bảng Fact BCTC',
    tables: ['fact_cdkt', 'fact_kqkd', 'fact_lctt'],
    description: 'Ba bảng fact cho CĐKT, KQKD và LCTT.',
  },
  {
    title: 'Các Dimension dùng chung',
    tables: [
      'dim_company',
      'dim_date',
      'dim_indicator',
      'dim_periodtype',
      'dim_auditstatus',
      'dim_consolidationstatus',
    ],
    description: 'Các dimension dùng chung cho phân tích đa công ty và đa kỳ.',
  },
  {
    title: 'Fact danh mục đầu tư',
    tables: ['fact_fvtpl_afs'],
    description: 'Giá trị và phân loại danh mục tài sản đầu tư FVTPL/AFS.',
  },
  {
    title: 'Dữ liệu thị trường bổ sung',
    tables: ['fact_market'],
    description:
      'Bổ sung dữ liệu cổ phiếu lưu hành, vốn hóa thị trường và giá đóng cửa cho phân tích tài chính.',
  },
] as const

export const powerBiCapabilities = [
  'Bộ lọc công ty & kỳ báo cáo',
  'Drill-down báo cáo tài chính',
  'Phân tích danh mục & hiệu quả',
] as const
