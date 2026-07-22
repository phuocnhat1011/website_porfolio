# Migration checklist

Ngày kiểm tra: 2026-07-22

## Audit và bảo toàn source

- [x] Đã audit entry point `app.py`, helper `shared.py`, JSON, Excel, ảnh, CV, chart, PBIX, R script và utility database.
- [x] Đã quét security toàn repository, file ẩn/nén tracked, Office/PBIX, production bundle và Git history; chi tiết trong `SECURITY_AUDIT.md`.
- [x] Đã lập mapping Streamlit → React trong `MIGRATION_AUDIT.md` trước khi code.
- [x] Không xóa hoặc ghi đè source Streamlit cũ.
- [x] Không ghi đè thay đổi sẵn có trong `portfolio-static/` hoặc CV `.docx`.
- [x] Đã nhận diện nội dung dormant: Bank, Knowledge, Contact.

## Chức năng và nội dung

- [x] Home giữ hero, avatar, mô tả, badge, hồ sơ, CV, strengths và 2 project active.
- [x] Navigation giữ Home + Projects + 2 project con.
- [x] Mobile navigation có toggle, đóng sau khi chuyển route và khóa scroll nền khi mở.
- [x] Trang Chứng khoán giữ đủ 4 tab và toàn bộ nội dung STAR/workflow/source/Power BI.
- [x] Trang Hedging giữ đủ 5 tab, pipeline, state machine, rule, chart, backtest và 3 email preview.
- [x] Project Ngân hàng được migrate thành route riêng nhưng không thêm vào menu chính.
- [x] Knowledge và Contact được migrate thành route riêng nhưng không thêm vào menu chính.
- [x] CV download hoạt động từ static asset.
- [x] SHA-256 của CV, workbook, ECharts HTML, avatar và 6 ảnh/diagram gốc trong `web-vite/public/` khớp source Streamlit tương ứng.
- [x] GitHub/LinkedIn/email và repository Hedging giữ đúng URL.
- [x] Securities repository giữ trạng thái disabled vì source chỉ có `#`.
- [x] Nút Securities repository hiển thị rõ “Repository — Coming soon”, không còn control giả có vẻ hoạt động.
- [x] Không thêm nội dung cá nhân mới ngoài source.
- [x] Format nội dung được giữ bằng heading, paragraph, strong/emphasis, list, badge, code block, tab và card tương ứng; không redesign.

## Backtest

- [x] Workbook gốc có 1.296 dòng, 10 cột và không có null.
- [x] Đã chuyển dữ liệu sang JSON tĩnh 1.296 dòng; vẫn giữ workbook gốc để download.
- [x] Good trả 8 dòng; KPI đầu: 65.0%, +5.80 pts, +232.0 pts, 40 trades.
- [x] Avg trả 88 dòng; KPI đầu: 59.5%, +5.30 pts, +196.1 pts, 37 trades.
- [x] Bad trả 395 dòng; KPI đầu: 49.4%, +1.67 pts, +128.8 pts, 77 trades.
- [x] Bảng có vùng scroll riêng trên mobile, không làm trang bị horizontal overflow.

## Power BI và chart

- [x] `PowerBIEmbed.tsx` nhận `title`, `embedUrl`, `aspectRatio` qua props.
- [x] URL Chứng khoán giữ nguyên chính xác từ source.
- [x] Có loading state, timeout/fallback, retry, fullscreen và link mở report riêng.
- [x] Iframe dùng lazy loading và không tràn mobile.
- [x] Không có access token hoặc secret trong React frontend.
- [x] Chart ECharts local giữ nguyên file và lazy-load trong iframe.
- [x] Power BI Ngân hàng không render iframe giả hoặc cảnh báo kỹ thuật; hiển thị placeholder nhẹ “Báo cáo đang được hoàn thiện”.
- [ ] Power BI Ngân hàng chưa thể embed vì source chỉ có placeholder, chưa có URL thật.

## Responsive/browser QA

- [x] Đã kiểm tra 375×812.
- [x] Đã kiểm tra 768×900.
- [x] Đã kiểm tra 1024×900.
- [x] Đã kiểm tra 1440×900.
- [x] Navigation desktop/mobile đổi đúng breakpoint.
- [x] Text, project card, button, iframe và section không tràn viewport.
- [x] Footer là N/A: source Streamlit chủ động ẩn footer, nên bản migration không tự thêm footer mới.
- [x] Không có horizontal scrollbar ngoài ý muốn trên các route active.
- [x] Đã phát hiện và sửa overflow của code block trang Knowledge ở 375px.
- [x] Browser console không có error hoặc warning sau các luồng kiểm tra.
- [x] Final QA xác nhận không horizontal overflow trên cả 6 route ở 375px và 1440px; 3 route active cũng pass ở 768px và 1024px.
- [x] Power BI iframe pass responsive ở 375/768/1024/1440; ECharts canvas resize đúng bốn kích thước.
- [x] Mobile drawer mở/đóng đúng, đóng sau khi điều hướng và trả body scroll về bình thường.

## Build và asset

- [x] `npm install` thành công: 177 packages, 0 vulnerability.
- [x] `npm run build` thành công.
- [x] `npm run preview` serve production build thành công; `/`, `/projects/securities`, `/projects/hedging` đều trả HTTP 200.
- [x] TypeScript compile không có error.
- [x] `npm run lint` không còn lỗi sau khi sửa kiểm tra `prefer-const`.
- [x] Tất cả public asset và 6 route kiểm tra trả HTTP 200 ở local dev server.
- [x] Các page được lazy-load; bundle JS chính gzip khoảng 76.38 kB.
- [x] Build cuối: main JS 237.19 kB (gzip 76.38 kB); page chunks lớn nhất Hedging 18.97 kB và Securities 11.87 kB.
- [x] Ảnh WebP được tạo và file gốc vẫn được giữ trong `public/images/`.
- [x] Không có import thiếu hoặc asset path hỏng được phát hiện.
- [x] `npm audit --omit=dev`: 0 production vulnerability.

## Link và placeholder

- [x] Không có `href="#"`, URL rỗng, localhost production link, Windows absolute asset path hoặc placeholder URL trong React production bundle.
- [x] `#main-content` chỉ là skip link accessibility hợp lệ, không phải placeholder.
- [x] Placeholder Bank còn ở legacy `data/projects.json`; React dùng `powerBiUrl: ''` có chủ đích để hiện empty state, không phát sinh URL giả.
- [x] `YOUR_EMBED_ID` chỉ còn trong đoạn dbdiagram đã comment của `app.py`; không render hoặc bundle.
- [x] Hai path `S:/...` chỉ là output path của offline `script_chart.R`; không phải link/asset path của website React.
- [x] Localhost chỉ còn trong hướng dẫn chạy local của README; không có trong runtime production.
- [x] GitHub profile và repository Hedging trả HTTP 200; LinkedIn trả 999 cho automated request nhưng URL/href đúng và không phải placeholder.
- [x] Email dùng đúng `mailto:nhat.vophuoc@gmail.com`.
- [x] CV `/documents/Vo-Phuoc-Nhat-CV.pdf` trả HTTP 200 và browser phát sinh download với filename đúng.
- [x] Toàn bộ 6 internal route và asset được kiểm tra trả HTTP 200; unknown route redirect về Home.

## Routing, SEO và Vercel

- [x] Dùng React Router vì source có nhiều view.
- [x] Route không tồn tại redirect về Home.
- [x] `vercel.json` có SPA rewrite theo hướng dẫn Vercel cho Vite.
- [x] Có title, meta description, favicon, canonical, Open Graph và Twitter metadata.
- [x] Có `robots.txt` và `sitemap.xml` cho các route public chính.
- [x] README có hướng dẫn local, build, preview, GitHub, Vercel, DNS, HTTPS và redirect www.
- [ ] Chưa deploy thật lên Vercel; chưa được yêu cầu/ủy quyền kết nối tài khoản.
- [ ] Chưa thay đổi DNS thật của `phuocnhat.dev` theo đúng yêu cầu an toàn.

## Security

- [x] Không sao chép credential PostgreSQL hoặc secret từ source cũ sang `web-vite/`.
- [x] `upload_database.py` đã chuyển PostgreSQL config và local data folder sang environment variables; chức năng ETL được giữ nguyên.
- [x] Tạo `.env.example` bằng giá trị mẫu không nhạy cảm; `.env`/`.env.*` và `.tmp.driveupload/` được ignore.
- [x] Đã xóa cache tracked `.tmp.driveupload/191` chứa bản sao nén của secret cũ.
- [x] Vercel frontend hiện không cần environment variable.
- [x] Không có secret thật trong production bundle; các match React DOM/ECharts/PBIX đã được xác minh là false positive.
- [ ] **Bắt buộc:** rotate PostgreSQL password; chưa có bằng chứng rotation đã hoàn tất.
- [ ] **Bắt buộc trước khi public:** rewrite Git history vì commit `f082a4c` và cache được thêm ở `6896b4d` còn giữ secret cũ.
- [ ] **Khẩn cấp:** origin GitHub hiện public; raw `main/upload_database.py` và commit `f082a4c` đều truy cập được không cần đăng nhập. Cân nhắc chuyển private trong lúc xử lý.
- [ ] Chưa thể tuyên bố repository an toàn để public cho đến khi hai mục bắt buộc trên hoàn tất và history được scan lại.
