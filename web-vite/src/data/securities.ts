export const securitiesWorkflow = [
  {
    number: '01',
    title: 'Data Ingestion — Thu thập dữ liệu tự động',
    paragraphs: [
      'Hệ thống tự động hóa việc truy xuất dữ liệu từ SSI iBoard cho toàn bộ các mã cổ phiếu ngành chứng khoán. Quy trình thực hiện quét dữ liệu theo từng kỳ báo cáo (năm, quý, 6 tháng, 9 tháng), tự động tải các bảng CĐKT, KQKD, LCTT về máy và phân loại vào cấu trúc thư mục logic. Điều này giúp loại bỏ hoàn toàn các thao tác thủ công và đảm bảo tính nhất quán của dữ liệu đầu vào.',
    ],
    tools: 'Python, Selenium, Requests, OS,..',
  },
  {
    number: '02',
    title: 'Transformation & Modeling — Xử lý & Mô hình hóa dữ liệu tài chính',
    paragraphs: [
      'Dữ liệu báo cáo tài chính thô thường không đồng nhất do sự khác biệt trong cách ghi nhận của các doanh nghiệp hoặc do thay đổi thông tư kế toán qua các năm. Bước này đóng vai trò làm sạch và tổ chức lại toàn bộ dữ liệu thành một hệ thống chuẩn chỉnh.',
    ],
    bullets: [
      'Data Cleaning: Gộp hàng loạt file Excel rời rạc thành bảng thống nhất. Xử lý triệt để các thay đổi về chỉ tiêu kế toán (ví dụ: gộp các khoản mục bị đổi tên qua các năm) để đảm bảo chuỗi dữ liệu tài chính xuyên suốt, không bị đứt gãy.',
      'Unpivot: Chuyển đổi cấu trúc dữ liệu từ dạng báo cáo ngang truyền thống sang định dạng dọc chuẩn, phục vụ trực tiếp cho việc vẽ biểu đồ và phân tích đa chiều.',
      'Data Modeling: Xây dựng mô hình dữ liệu Star Schema. Phân tách dữ liệu thành các bảng Danh mục (Công ty, Thời gian) và bảng Số liệu sự kiện (CĐKT, KQKD), giúp loại bỏ dữ liệu thừa và tối ưu hóa tốc độ tính toán cho các báo cáo sau này.',
    ],
    tools: 'Python, thư viện Pandas.',
  },
  {
    number: '03',
    title: 'Data Extraction & Quality Assurance — Trích xuất & Kiểm tra dữ liệu',
    paragraphs: ['Quy trình: Lọc và xử lý dữ liệu từ Báo cáo tài chính để đảm bảo số liệu về danh mục đầu tư (FVTPL, AFS) luôn chính xác trước khi sử dụng cho báo cáo.'],
    bullets: [
      'Thu thập: Tự động tải BCTC theo năm và quý của các công ty chứng khoán niêm yết.',
      'Trích xuất: Dùng Python (OCR) để đọc dữ liệu từ báo cáo.',
      'Kiểm tra: Tôi chạy một đoạn script nhỏ để cộng lại các khoản mục, nếu tổng không khớp với số tổng trên báo cáo, hệ thống sẽ đánh dấu các công ty đó. Với những công ty bị đánh dấu lỗi, tôi sử dụng NotebookLM hoặc ChatGPT để hỗ trợ trích xuất lại thủ công, đảm bảo không bỏ sót số liệu.',
      'Kết quả: Có được tập dữ liệu sạch, đảm bảo tính khớp đúng để phục vụ phân tích.',
    ],
    tools: 'Python, Pandas, NotebookLM, ChatGPT.',
  },
  {
    number: '04',
    title: 'Data Storage & Management — Lưu trữ & Quản trị dữ liệu',
    paragraphs: ['Thay vì quản lý bằng các file rời rạc và load thủ công, toàn bộ dữ liệu sau khi được làm sạch bằng Python sẽ được đẩy vào PostgreSQL. Việc chuyển đổi từ lưu trữ tệp sang Database giúp quản lý tập trung toàn bộ khối lượng dữ liệu tài chính, tạo nền tảng ổn định cho báo cáo.'],
    bullets: [
      'Lưu trữ tập trung: Nạp dữ liệu vào PostgreSQL, tổ chức phân lớp rõ ràng theo mô hình Star Schema (gồm các bảng Fact và Dimension) đã thiết kế ở bước trước.',
      'Đảm bảo tính toàn vẹn: Thiết lập các ràng buộc dữ liệu cơ bản (Khóa chính - Primary Key, Khóa ngoại - Foreign Key) để đảm bảo không bị mâu thuẫn số liệu giữa các bảng.',
    ],
    tools: 'PostgreSQL, SQL, Python.',
  },
  {
    number: '05',
    title: 'Visualization Power BI — Trực quan hóa dữ liệu',
    paragraphs: ['Ở bước cuối cùng, Power BI được kết nối trực tiếp vào Database PostgreSQL để kéo dữ liệu sạch lên và xây dựng các báo cáo tương tác.'],
    bullets: [
      'Giao diện đa nhiệm: Tích hợp đầy đủ 3 bảng báo cáo (CĐKT, KQKD, LCTT) giúp người dùng dễ dàng chuyển đổi góc nhìn.',
      'Tương tác linh hoạt: Sử dụng tính năng Drill-down (xem chi tiết đa cấp độ) và các bộ lọc (Slicer) động theo mã công ty, kỳ báo cáo giúp việc truy xuất số liệu trở nên trực quan và nhanh chóng.',
    ],
    tools: 'Power BI Desktop & Service, DAX.',
  },
]
