export type ProjectStatusTone = 'complete' | 'progress' | 'soon'

export interface ProjectStatus {
  label: string
  value: string
  tone: ProjectStatusTone
}

export interface MarketMetric {
  value: string
  label: string
  detail: string
}

export interface ContentCard {
  title: string
  description: string
}

export interface PipelineNode {
  label: string
  status?: 'Completed' | 'In Progress'
}

export interface WorkflowStage {
  number: string
  eyebrow: string
  title: string
  items: readonly string[]
  tools: readonly string[]
  note?: string
}

export interface MarketDataSource extends ContentCard {
  tags: readonly string[]
}

export interface MarketModelTable extends ContentCard {
  grain?: string
}

export interface ReportModule {
  number: string
  title: string
  status: 'In Progress' | 'Planned'
  scope: readonly string[]
}

export const marketOverviewProject = {
  route: '/market-overview',
  name: 'Vietnam Market Overview & Analytics',
  eyebrow: 'PERSONAL PROJECT · MARKET DATA ANALYTICS',
  subtitle: 'Market Data Warehouse · SQL Analytics · Power BI',
  description:
    'Hệ thống dữ liệu và phân tích thị trường chứng khoán Việt Nam, bao phủ chỉ số, sàn giao dịch, ngành, công ty niêm yết, diễn biến giá, thanh khoản và dòng tiền giao dịch.',
  technologies: ['Python', 'PostgreSQL', 'SQL', 'Power BI', 'DAX', 'ETL', 'Dimensional Modeling'],
  statuses: [
    { label: 'Data Model', value: 'Completed', tone: 'complete' },
    { label: 'ETL & Data Quality', value: 'Completed', tone: 'complete' },
    { label: 'SQL Analytics', value: 'In Progress', tone: 'progress' },
    { label: 'Power BI Report', value: 'In Progress', tone: 'progress' },
  ] satisfies readonly ProjectStatus[],
  metrics: [
    {
      value: '1,500+',
      label: 'Listed Companies',
      detail: 'HOSE · HNX · UPCOM',
    },
    {
      value: '3',
      label: 'Exchanges',
      detail: 'Vietnam listed-market scope',
    },
    {
      value: 'Multi-Fact',
      label: 'Data Model',
      detail: 'Prices · Indices · Foreign Flow',
    },
  ] satisfies readonly MarketMetric[],
} as const

export const marketOverviewContent = {
  heading: 'Nền tảng phân tích thị trường chứng khoán Việt Nam',
  description:
    'Project xây dựng một data platform có cấu trúc để kết nối bối cảnh thị trường toàn cầu với diễn biến chỉ số, sàn, ngành, cổ phiếu, thanh khoản và dòng tiền tại Việt Nam.',
  problem: {
    title: 'Dữ liệu thị trường phân tán và khó phân tích nhất quán',
    description:
      'Dữ liệu chỉ số, cổ phiếu, ngành, thanh khoản và dòng tiền được thu thập từ nhiều nguồn với khác biệt về ticker, lịch giao dịch, cấu trúc cột và phạm vi lịch sử. Việc xử lý thủ công gây khó khăn cho phân tích toàn thị trường và so sánh đa chiều.',
  },
  objective: {
    title: 'Xây dựng market-data platform có thể mở rộng',
    description:
      'Thu thập, chuẩn hóa và mô hình hóa dữ liệu thành các Fact và Dimension dùng chung, tạo nền tảng cho PostgreSQL, SQL Analytics và Power BI theo hướng phân tích từ toàn cảnh đến từng cổ phiếu.',
  },
  components: [
    {
      title: 'Global Market Context',
      description:
        'Kết nối lớp dữ liệu bối cảnh toàn cầu trước khi đi sâu vào diễn biến của thị trường Việt Nam.',
    },
    {
      title: 'Vietnam Market Universe',
      description:
        'Tổ chức công ty niêm yết, sàn giao dịch, ngành, chỉ số và thành phần chỉ số trong mô hình dùng chung.',
    },
    {
      title: 'Daily Market Activity',
      description:
        'Phân tích giá, biến động, khối lượng và thanh khoản theo ngày trên nhiều lát cắt thị trường.',
    },
    {
      title: 'Trading Flow Analytics',
      description:
        'Theo dõi giao dịch khối ngoại và các nguồn trading-flow đã được tích hợp.',
    },
  ] satisfies readonly ContentCard[],
  values: [
    {
      title: 'Theo dõi toàn thị trường',
      description: 'Phân tích theo luồng từ bối cảnh toàn cầu đến sàn, ngành, chỉ số và cổ phiếu.',
    },
    {
      title: 'So sánh dữ liệu nhất quán',
      description: 'Chuẩn hóa ticker, Date và các Dimension dùng chung để giảm sai lệch giữa nguồn dữ liệu.',
    },
    {
      title: 'Nền tảng có thể tái sử dụng',
      description: 'Một data model dùng chung cho SQL analysis, Power BI và các module mở rộng sau này.',
    },
  ] satisfies readonly ContentCard[],
  pipeline: [
    { label: 'Market APIs', status: 'Completed' },
    { label: 'Python ETL', status: 'Completed' },
    { label: 'Data Quality', status: 'Completed' },
    { label: 'PostgreSQL', status: 'Completed' },
    { label: 'SQL Analytics', status: 'In Progress' },
    { label: 'Power BI', status: 'In Progress' },
  ] satisfies readonly PipelineNode[],
} as const

export const marketDataSources = [
  {
    title: 'DNSE Market APIs',
    description:
      'Danh sách công ty, thông tin ticker và dữ liệu OHLCV hằng ngày của cổ phiếu và chỉ số.',
    tags: ['Company Universe', 'Stock OHLCV', 'Index OHLCV'],
  },
  {
    title: 'CafeF Trading Flow',
    description:
      'Dữ liệu giao dịch khối ngoại theo cổ phiếu và ngày trên HOSE, HNX và UPCOM.',
    tags: ['Foreign Buy', 'Foreign Sell', 'Net Flow'],
  },
  {
    title: 'International Market Data',
    description:
      'Dữ liệu chỉ số toàn cầu, commodities, futures và crypto phục vụ Global Market Context.',
    tags: ['Indices', 'Commodities', 'Futures', 'Crypto'],
  },
  {
    title: 'Manual Mapping & Staging Files',
    description:
      'Các file mapping ngành, ticker và dữ liệu CSV/Excel trung gian trước khi chuẩn hóa vào analytical model.',
    tags: ['Sector Mapping', 'CSV', 'Excel'],
  },
] satisfies readonly MarketDataSource[]

export const marketWorkflowStages: readonly WorkflowStage[] = [
  {
    number: '01',
    eyebrow: 'COLLECTION',
    title: 'Data Collection',
    items: [
      'Thu thập danh sách ticker và thông tin công ty niêm yết.',
      'Thu thập daily OHLCV cho cổ phiếu và benchmark indices.',
      'Thu thập dữ liệu giao dịch khối ngoại theo ngày.',
      'Thu thập global-market data cho lớp Global Market Context.',
      'Ghi log request thành công, thất bại và phạm vi dữ liệu đã tải.',
    ],
    tools: ['Python', 'Requests', 'APIs'],
  },
  {
    number: '02',
    eyebrow: 'STANDARDIZATION',
    title: 'Data Standardization',
    items: [
      'Chuẩn hóa ticker, Date và kiểu dữ liệu.',
      'Chuẩn hóa tên sàn, ngành và cấu trúc cột.',
      'Mapping external ticker vào Company_ID và các surrogate keys.',
      'Đồng nhất schema giữa các nguồn dữ liệu.',
      'Chuẩn bị dữ liệu theo grain của từng Fact table.',
    ],
    tools: ['Python', 'Pandas'],
  },
  {
    number: '03',
    eyebrow: 'DATA QUALITY',
    title: 'Validation & Quality Checks',
    items: [
      'Kiểm tra duplicate theo Date × Entity.',
      'Kiểm tra Min Date, Max Date và phạm vi lịch sử.',
      'Kiểm tra ticker chưa mapping hoặc mapping không hợp lệ.',
      'Đối chiếu ngày dữ liệu với trading calendar.',
      'Theo dõi missing values và failed requests.',
      'Kiểm tra referential integrity trước khi load PostgreSQL.',
    ],
    tools: ['Python', 'Validation Rules'],
  },
  {
    number: '04',
    eyebrow: 'MODELING',
    title: 'Data Modeling & Storage',
    items: [
      'Thiết kế các Fact và Dimension dùng chung.',
      'Xác định grain, Primary Key và Foreign Key.',
      'Lưu trữ reporting-ready data trong PostgreSQL.',
      'Tổ chức relationship phục vụ SQL và Power BI.',
      'Chuẩn bị cấu trúc có thể mở rộng cho các Fact mới.',
    ],
    tools: ['PostgreSQL', 'SQL', 'Dimensional Modeling'],
  },
  {
    number: '05',
    eyebrow: 'ANALYTICS',
    title: 'BI & Analytical Layer',
    items: [
      'Xây dựng analytical SQL cases cho market monitoring.',
      'Hoàn thiện Power BI semantic model và DAX measures.',
      'Thiết kế filtering, drill-down và cross-market analysis.',
      'Chuẩn bị các report module từ Global Context đến Vietnam Market Detail.',
    ],
    tools: ['SQL', 'Power BI', 'DAX'],
    note: 'Dimensional model đã hoàn thành. SQL Analytics và Power BI report đang được hoàn thiện.',
  },
]

export const marketDataQualityControls = [
  {
    title: 'Duplicate Check',
    description: 'Date × Entity uniqueness',
  },
  {
    title: 'Date Validation',
    description: 'Min/Max Date và trading-date consistency',
  },
  {
    title: 'Ticker Mapping',
    description: 'External ticker → internal surrogate key',
  },
  {
    title: 'Missing Data',
    description: 'Theo dõi missing values và incomplete loads',
  },
  {
    title: 'Request Logging',
    description: 'Ghi nhận failed requests để tải lại',
  },
  {
    title: 'Referential Integrity',
    description: 'Kiểm tra khóa trước khi load PostgreSQL',
  },
] satisfies readonly ContentCard[]

export const marketModelScope: readonly ContentCard[] = [
  {
    title: 'Shared Dimensions',
    description:
      'Các Dimension về công ty, sàn, ngành, chỉ số, ngày và tài sản toàn cầu được tái sử dụng giữa nhiều Fact table.',
  },
  {
    title: 'Daily Market Facts',
    description: 'Dữ liệu giá cổ phiếu và chỉ số được tổ chức theo grain Entity × Trading Date.',
  },
  {
    title: 'Trading-Flow Facts',
    description:
      'Dữ liệu giao dịch khối ngoại và các nguồn trading-flow được liên kết với công ty và ngày giao dịch.',
  },
  {
    title: 'Reusable Date Layer',
    description:
      'dim_date tạo lớp thời gian dùng chung cho filtering, trend analysis và period comparison.',
  },
]

export const marketModelDimensions: readonly MarketModelTable[] = [
  {
    title: 'dim_company',
    description: 'Công ty niêm yết, ticker, sàn, ngành, ngày niêm yết và các thuộc tính doanh nghiệp.',
  },
  {
    title: 'dim_exchange',
    description: 'Danh mục ba sàn HOSE, HNX và UPCOM.',
  },
  {
    title: 'dim_sector',
    description: 'Sector, Industry, Sub-industry và hệ phân cấp ngành.',
  },
  {
    title: 'dim_index',
    description: 'VNINDEX, VN30, HNXINDEX, HNX30 và UPCOMINDEX.',
  },
  {
    title: 'dim_date',
    description: 'Date, Year, Quarter, Month và các thuộc tính phục vụ time analysis.',
  },
  {
    title: 'dim_world',
    description: 'Global asset, asset class, region, market group và display order.',
  },
]

export const marketModelFacts: readonly MarketModelTable[] = [
  {
    title: 'fact_price_daily',
    grain: 'Company × Trading Date',
    description: 'Daily OHLCV và các chỉ số biến động giá của cổ phiếu.',
  },
  {
    title: 'fact_index_daily',
    grain: 'Index × Trading Date',
    description: 'Daily OHLCV và biến động của benchmark indices.',
  },
  {
    title: 'fact_foreign_trading_daily',
    grain: 'Company × Trading Date',
    description: 'Foreign buy, sell và net flow theo volume và value.',
  },
  {
    title: 'fact_index_constituent',
    grain: 'Index × Company × Effective Period',
    description: 'Thành phần chỉ số, thời gian hiệu lực và các thuộc tính liên quan.',
  },
  {
    title: 'fact_world_daily',
    grain: 'World Asset × Trading Date',
    description: 'Daily market data của global indices, commodities, futures và crypto.',
  },
]

export const marketModelRelationships = [
  'Exchange → Company',
  'Sector → Company',
  'Company → Price Daily',
  'Company → Foreign Trading',
  'Index → Index Daily',
  'Index ↔ Company through Index Constituent',
  'World Asset → World Daily',
  'Date → Daily Facts',
] as const

export const marketModelImage = {
  src: '/images/market-overview-data-model.png',
  alt: 'Vietnam Market Overview Power BI data model',
  available: false,
} as const

export const sqlAnalyticsRoadmap = [
  'Market Snapshot',
  'Market Breadth',
  'Sector Performance',
  'Liquidity Analysis',
  'Foreign Trading Flow',
] as const

export const powerBiReportModules: readonly ReportModule[] = [
  {
    number: '01',
    title: 'Global Market Snapshot',
    status: 'In Progress',
    scope: ['Global market context'],
  },
  {
    number: '02',
    title: 'Vietnam Market Overview',
    status: 'In Progress',
    scope: ['Benchmark indices', 'Market movement', 'Liquidity', 'Trading activity'],
  },
  {
    number: '03',
    title: 'Index Analysis',
    status: 'Planned',
    scope: ['Index-level trends and comparison'],
  },
  {
    number: '04',
    title: 'Sector & Industry',
    status: 'Planned',
    scope: ['Sector performance and market structure'],
  },
  {
    number: '05',
    title: 'Company Analysis',
    status: 'Planned',
    scope: ['Company-level price and liquidity analysis'],
  },
  {
    number: '06',
    title: 'Foreign Trading',
    status: 'Planned',
    scope: ['Foreign buy, sell and net-flow analysis'],
  },
]
