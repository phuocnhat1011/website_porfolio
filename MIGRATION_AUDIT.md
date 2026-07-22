# Migration audit: Streamlit → React/Vite

Ngày audit: 2026-07-22  
Source được xem là nguồn sự thật: `app.py`, `shared.py`, `data/projects.json` và các asset được những file này tham chiếu. Thư mục `portfolio-static/` cũng đã được đọc để đối chiếu nhưng đang là thay đổi chưa commit và không được dùng thay cho việc audit source Streamlit.

## 1. Kết luận nhanh

- Entry point của website hiện tại là `app.py`; `shared.py` cung cấp CSS và helper hiển thị ảnh/Power BI.
- Website đang hoạt động như một ứng dụng nhiều view với sidebar: Home, BCTC Chứng khoán VN và Hedging VN30F1M. Menu cha `Projects` chuyển thẳng đến trang BCTC Chứng khoán VN.
- `render_bank`, `render_knowledge` và `render_contact` có đầy đủ nội dung trong source nhưng hiện không xuất hiện trong menu đang chạy. Đây là nội dung dormant, vẫn phải có component React tương ứng để không mất nội dung.
- Runtime website không gọi API riêng, không ghi dữ liệu, không xử lý form, không dùng database và không tạo Power BI token. Bản portfolio có thể deploy như frontend tĩnh trên Vercel, không cần backend.
- Power BI Chứng khoán dùng URL `app.powerbi.com/view?...`, tức Publish to web công khai. Dự án Ngân hàng chỉ có placeholder `PASTE_YOUR_PUBLISH_TO_WEB_URL`, chưa có report để embed.
- Trang Hedging đọc `assets/data_backtesting.xlsx` (1 sheet, 1.296 dòng, 10 cột) để lọc Good/Avg/Bad, tính KPI và render bảng. Logic này có thể chuyển trực tiếp sang TypeScript với dữ liệu JSON tĩnh.
- `assets/vn30f1m.html` là biểu đồ ECharts tự chứa, tương tác ở phía trình duyệt và tự refresh iframe mỗi 30 giây. Không cần Python/R ở runtime.
- `upload_database.py` là utility ETL PostgreSQL độc lập, không được import bởi website. Credential hard-code đã được chuyển sang environment variables trong vòng security audit cuối; giá trị cũ vẫn tồn tại trong lịch sử Git và phải được rotate/làm sạch trước khi public repository.

## 2. Cấu trúc repository đã audit

```text
portfolio/
├── app.py                         # Streamlit entry point, toàn bộ page/view
├── shared.py                      # CSS toàn cục, helper ảnh/SVG/Power BI
├── data/projects.json             # Metadata 3 project
├── assets/
│   ├── avatar.jpg
│   ├── CV.pdf
│   ├── data_backtesting.xlsx
│   ├── vn30f1m.html               # Biểu đồ ECharts đang được embed
│   ├── vn30f1m_files/             # Dependency của bản chart không self-contained khác
│   └── previews/                  # Cover, ETL, ERD, data model
├── script_chart.R                 # Sinh biểu đồ ECharts; không chạy trong website
├── upload_database.py             # ETL local → PostgreSQL; không chạy trong website
├── requirements.txt               # Streamlit + streamlit-antd-components
├── .streamlit/config.toml         # Theme light/purple
├── *.pbix                         # Power BI Desktop source, không được website serve
├── design.html                    # Prototype Hedging độc lập, không phải entry point
└── portfolio-static/              # Bản static chưa commit; chỉ dùng đối chiếu
```

Các file generated/vendor của `vn30f1m_files/`, `.venv/`, `__pycache__/` và `.tmp.driveupload/` đã được nhận diện nhưng không phải logic website cần viết lại.

## 3. Chức năng hiện tại

### Navigation và state

- Sidebar Ant Design gồm Home và Projects; Projects có 2 page con.
- State `current_page` giữ view hiện tại; `last_page` và `scroll_counter` hỗ trợ scroll-to-top khi đổi page.
- `home_acc_open` là state accordion trên Home, nhưng các accordion helper hiện không được gọi trong project card đang render.
- Các tab project và bộ lọc Rank dùng state nội bộ của `streamlit-antd-components`.
- Không có query parameter, URL parameter hoặc deep link ở bản Streamlit.

### Home

- Hero với avatar, tên, mô tả, 5 badge chuyên môn.
- Hồ sơ cá nhân và tải CV PDF.
- 3 thẻ thế mạnh chuyên môn.
- Project grid lấy từ `data/projects.json`, chủ động ẩn project Ngân hàng; hiển thị Chứng khoán và Hedging.
- Nút “Chi tiết dự án” chuyển sang view tương ứng.

### BCTC Chứng khoán VN

- 4 tab: Tổng quan, Quy trình, Source Code & Data Model, Power BI.
- Tổng quan có 2 card STAR với toàn bộ nội dung Situation/Task/Action/Result.
- Quy trình có ảnh ETL và workflow 5 bước chi tiết.
- Source hiển thị ERD PostgreSQL; nút repository hiện dùng `#`, không có URL GitHub thật trong source.
- Power BI Publish to web công khai qua iframe.

### Hedging VN30F1M

- 5 tab: Tổng quan, Quy trình, Source code, Backtest, Alert Email.
- Tổng quan có STAR, 6 tính năng cốt lõi và tech tags.
- Quy trình có pipeline 4 bước, state machine WAIT_SHORT/WAIT_OUT và đầy đủ entry/exit rules.
- Source code liên kết GitHub `https://github.com/phuocnhat1011/VN30F1M_HEDGING` và embed biểu đồ ECharts local.
- Backtest đọc workbook, hỗ trợ 3 filter:
  - Good: `Win Rate > 60` và `Total Pnl > 200`, sắp xếp `AVG Pnl` giảm dần (8 dòng).
  - Avg: `50 < Win Rate < 60` và `150 < Total Pnl < 200`, sắp xếp `AVG Pnl` giảm dần (88 dòng).
  - Bad: `Win Rate < 50` và `Total Pnl < 150`, sắp xếp `Win Rate` giảm dần (395 dòng).
- KPI lấy dòng đầu sau khi lọc: Win Rate, AVG Pnl, Total Pnl, Nb trades.
- Alert Email có state-machine summary và 3 preview: SHORT, EXIT, Daily summary.

### Nội dung dormant trong source

- Ngân hàng: 4 tab Tổng quan, Quy trình, Source Code & Data Model, Power BI; report đang thiếu URL thật.
- Góc Chia Sẻ Kiến Thức: 2 tip DAX/modeling và 2 bài viết mô tả chuyên sâu.
- Liên hệ & Kỹ năng: email, LinkedIn, GitHub, tải CV và 4 nhóm kỹ năng.

## 4. Frontend và backend

| Hạng mục | Phân loại | Kết luận migration |
| --- | --- | --- |
| Text, card, badge, sidebar, tab, accordion | Frontend | Chuyển trực tiếp sang React component/state |
| Project metadata JSON | Dữ liệu tĩnh | Chuyển sang TypeScript trong `src/data/projects.ts` |
| Backtest Excel + filter/KPI | Dữ liệu tĩnh + tính toán client | Chuyển workbook sang JSON tĩnh, giữ workbook gốc để download/đối chiếu |
| Power BI Chứng khoán | Iframe public | Giữ nguyên URL Publish to web, không cần token/backend |
| Power BI Ngân hàng | Chưa cấu hình | Hiển thị placeholder nhẹ, chuyên nghiệp; không suy đoán URL |
| Biểu đồ ECharts VN30F1M | Static HTML/JS | Serve nguyên file và lazy-load bằng iframe |
| CV download | Static document | Serve PDF từ `public/documents/` |
| `script_chart.R` | Offline data/chart generation | Không cần ở runtime React |
| `upload_database.py` | Offline ETL có ghi PostgreSQL | Không thuộc runtime portfolio; nếu đưa lên web trong tương lai bắt buộc dùng backend và secret manager |
| PBIX source | Authoring asset | Không đưa vào bundle web; giữ nguyên tại repository gốc |

### Kết luận backend

Không cần backend cho phạm vi website hiện tại. PostgreSQL và logic thu thập dữ liệu chỉ được mô tả trong portfolio hoặc chạy qua utility độc lập; website không truy cập database. Mọi secret/credential phải nằm ngoài `web-vite/`.

## 5. Mapping Streamlit → React

| Streamlit hiện tại | React component mới | Nội dung/chức năng | Trạng thái |
| --- | --- | --- | --- |
| Sidebar `sac.menu` | `SidebarNavigation` + `MobileNavigation` | Home, Projects, active state, mobile drawer | Completed |
| Page dispatch/session state | `AppRouter` + `ScrollToTop` | URL riêng, back/forward, refresh route | Completed |
| `render_home` hero | `HeroSection` | Avatar, giới thiệu, badge | Completed |
| `render_home` hồ sơ | `ProfileSection` | Quote, CV download | Completed |
| `render_home` thế mạnh | `StrengthsSection` | 3 KPI/strength card | Completed |
| `render_home` project grid | `FeaturedProjectsSection` + `ProjectCard` | 2 project active, CTA route | Completed |
| `render_securities` header | `ProjectPageHeader` | Title và mô tả | Completed |
| Securities / Tổng quan | `SecuritiesOverview` | 2 card STAR đầy đủ | Completed |
| Securities / Quy trình | `SecuritiesWorkflow` | ETL image + workflow 5 bước | Completed |
| Securities / Source | `SecuritiesSource` | ERD + repo placeholder | Completed |
| Securities / Power BI | `PowerBIEmbed` | URL Publish to web, loading/fallback/fullscreen | Completed |
| `render_hedging` header | `ProjectPageHeader` | Title và mô tả | Completed |
| Hedging / Tổng quan | `HedgingOverview` | STAR, 6 feature card, tech tags | Completed |
| Hedging / Quy trình | `HedgingWorkflow` | Pipeline, state machine, entry/exit rules | Completed |
| Hedging / Source code | `HedgingSource` + `InteractiveChartEmbed` | GitHub link + chart HTML | Completed |
| Hedging / Backtest | `BacktestExplorer` | Fetch JSON, 3 filter, KPI, table | Completed |
| Hedging / Alert Email | `HedgingEmailAlerts` | 3 preview tab + state-machine summary | Completed |
| `render_bank` | `BankProjectPage` | Giữ 4 tab và placeholder Power BI đang hoàn thiện | Completed (route không đưa vào menu chính) |
| `render_knowledge` | `KnowledgePage` | Toàn bộ tip và bài viết | Completed (route không đưa vào menu chính) |
| `render_contact` | `ContactPage` | Contact, CV và skill map | Completed (route không đưa vào menu chính) |
| Helper `cover_block` | `ResponsiveImage`/`ProjectCard` | Cover + lazy loading | Completed |
| `load_backtest_data` | `backtest.ts` + JSON tĩnh | Parse/filter/sort phía client | Completed |
| Inline iframe Power BI | `PowerBIEmbed` | Component dùng props, không hard-code URL | Completed |

## 6. Asset và link phải giữ

### Asset được website tham chiếu trực tiếp

- `assets/avatar.jpg`
- `assets/CV.pdf`
- `assets/previews/securities_vn.png`
- `assets/previews/hedging_vn30f1m.png`
- `assets/previews/bank_bctc.png`
- `assets/previews/etl_pipeline.png`
- `assets/previews/ERD_PostgreSQL.png`
- `assets/data_backtesting.xlsx`
- `assets/vn30f1m.html`

### Asset source/đối chiếu, không nằm trong production bundle

- `assets/previews/data_model.png`, `ERD_PostgreSQL.svg`, các file `.pgerd`.
- `PDS.pbix`, `bctc_chungkhoan.pbix`, `test_demo.pbix`.
- `assets/VoPhuocNhat_CV.docx`, các bản CV trùng tên và các chart generated cũ.

Các file này vẫn được giữ nguyên trong source Streamlit/repository gốc; không xóa hoặc ghi đè.

### Link

- Email: `mailto:nhat.vophuoc@gmail.com`
- LinkedIn: `https://linkedin.com/in/phuocnhat1011`
- GitHub profile: `https://github.com/phuocnhat1011`
- Hedging repository: `https://github.com/phuocnhat1011/VN30F1M_HEDGING`
- Securities repository: chưa có link thật (`#` trong source), phải giữ trạng thái không khả dụng thay vì tạo link giả.
- Canonical: `https://phuocnhat.dev`

## 7. Rủi ro mất chức năng và biện pháp

1. **Power BI cross-origin:** iframe public có thể bị mạng/trình duyệt chặn; giữ URL nguyên bản, có loading, timeout/fallback và nút fullscreen.
2. **Power BI Ngân hàng thiếu URL:** không thể tự điền. Route React hiển thị placeholder nhẹ và không render iframe/token.
3. **Backtest sai biên lọc:** điều kiện dùng strict inequality (`>`, `<`), phải test count 8/88/395 và KPI dòng đầu.
4. **Chart ECharts lớn (~2,4 MB):** không import vào bundle React; serve static và lazy-load khi mở tab Source.
5. **Chart tự refresh 30 giây:** giữ nguyên file để bảo toàn hành vi; chỉ iframe refresh, không rerender toàn app.
6. **Link repo Securities là `#`:** render control disabled, không tạo URL giả.
7. **Credential cũ:** `upload_database.py` đã dùng environment variables, nhưng secret cũ từng nằm trong commit `f082a4c`. Bắt buộc rotate và rewrite Git history trước khi public repository.
8. **Nội dung dormant:** tạo route/component riêng nhưng không thêm vào menu chính để giữ trải nghiệm navigation hiện tại.
9. **Ảnh lớn:** tạo WebP tối ưu cho web nhưng giữ/copy file gốc để fallback và đối chiếu.
10. **Refresh URL con trên Vercel:** dùng SPA rewrite trong `vercel.json`.

## 8. Kiến trúc React đã chọn

- React + Vite + TypeScript.
- React Router vì website có nhiều view thực sự và cần deep link/refresh route.
- CSS Modules cho component/page, `src/styles/globals.css` cho token và reset.
- Page-level lazy loading; Backtest JSON, chart iframe và Power BI iframe chỉ tải khi cần.
- Dữ liệu tách khỏi UI trong `src/config/site.ts`, `src/data/projects.ts`, `src/data/skills.ts`, `src/data/knowledge.ts` và JSON backtest public.
- Không thêm UI framework, animation framework hoặc backend dependency.
