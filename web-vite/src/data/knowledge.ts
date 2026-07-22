export const knowledgeTips = [
  {
    title: '🚀 Tối ưu hóa hiệu năng DAX với KEEPFILTERS instead of CALCULATE filters',
    description: 'Khi bạn viết một điều kiện lọc đơn giản trong CALCULATE, mặc định nó sẽ thay thế toàn bộ bộ lọc hiện tại trên cột đó. Sử dụng KEEPFILTERS sẽ giữ nguyên bộ lọc ngữ cảnh ngoài và giao thoa với bộ lọc mới. Giúp cải thiện tốc độ đáng kể trong các báo cáo lớn.',
    code: `-- Lọc không tối ưu (Ghi đè filter)\nSales_VN = CALCULATE([Total Sales], Customer[Country] = "Vietnam")\n\n-- Lọc tối ưu (Giữ lại filter)\nSales_VN_Optimized = CALCULATE(\n    [Total Sales],\n    KEEPFILTERS(Customer[Country] = "Vietnam")\n)`,
  },
  {
    title: '🏗️ Thiết kế Star Schema cho báo cáo tài chính thay vì Flat Table',
    description: 'Nhiều người có xu hướng kéo tất cả các cột dữ liệu vào một bảng Fact lớn. Trong BCTC đa chỉ tiêu, việc tách bảng Chỉ tiêu tài chính (Dim_Items) và bảng Công ty (Dim_Company) riêng biệt sẽ giúp viết mã DAX tính tăng trưởng YoY/QoQ ngắn gọn và tái sử dụng dễ dàng hơn.',
  },
]

export const knowledgeArticles = [
  {
    title: '🏦 Thiết kế Schema Dữ liệu BCTC Ngành Ngân Hàng: Từ Raw Data đến Star Schema',
    meta: 'Người viết: Võ Phước Nhật | 5 phút đọc',
    description: 'Khác với doanh nghiệp thương mại, BCTC ngân hàng có cấu trúc đặc thù như NIM, nợ xấu (NPL), và hệ số an toàn vốn CAR. Bài viết này chia sẻ phương pháp thiết kế bảng Fact cân đối kế toán kết hợp phân bổ theo kỳ hạn và nhóm nợ, giúp nhà phân tích dễ dàng drill-down sâu vào thuyết minh dư nợ cho vay khách hàng.',
  },
  {
    title: '🤖 Tự động hoá trích xuất Thuyết minh BCTC bằng Python & AI (FVTPL & AFS)',
    meta: 'Người viết: Võ Phước Nhật | 7 phút đọc',
    description: 'Thuyết minh báo cáo tài chính là mỏ vàng thông tin nhưng thường được lưu trữ dưới dạng bảng PDF scan phi cấu trúc. Bài viết này trình bày chi tiết cách xây dựng pipeline RAG (Retrieval-Augmented Generation) kết hợp OCR độ phân giải cao để tìm kiếm, phân tích và trích xuất tự động danh mục đầu tư tài chính FVTPL, AFS của các công ty chứng khoán.',
  },
]
