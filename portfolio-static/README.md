# Portfolio static — Võ Phước Nhật

## 1. Mục tiêu

Đây là bản chuyển đổi tĩnh của portfolio Streamlit hiện tại. Website production chỉ dùng HTML, CSS, JavaScript và tài nguyên tĩnh; không cần Python, Streamlit, Node.js server hoặc backend runtime. Mục tiêu là triển khai bằng Render Static Site để loại bỏ cold start nhưng vẫn giữ domain `phuocnhat.dev`.

Source Streamlit cũ nằm ở thư mục cha và chưa bị xóa hoặc sửa, nên có thể rollback bất kỳ lúc nào.

## 2. Công nghệ

- HTML5 semantic
- CSS responsive, không framework
- JavaScript thuần cho menu mobile, tabs và trạng thái navigation
- Power BI public iframe
- ECharts HTML export cục bộ cho biểu đồ VN30F1M

## 3. Cấu trúc

```text
portfolio-static/
├── index.html                 # Nội dung và metadata
├── css/style.css              # Toàn bộ giao diện responsive
├── js/main.js                 # Menu, tabs, navigation
├── assets/
│   ├── images/                # Avatar, preview, ETL, ERD
│   ├── documents/             # CV PDF
│   ├── charts/                # ECharts export và dependencies
│   └── data/                  # Workbook backtest tải xuống
├── favicon.svg
├── robots.txt
├── sitemap.xml
├── render.yaml
└── README.md
```

## 4. Chạy và kiểm tra local

Không mở trực tiếp `index.html` bằng `file://`, vì iframe biểu đồ có thể bị trình duyệt hạn chế. Mở terminal tại `portfolio-static`, rồi dùng một trong hai cách:

```bash
python -m http.server 8000
```

Sau đó mở `http://localhost:8000`. Python chỉ phục vụ preview local, không phải dependency production. Có thể dùng VS Code Live Server thay thế.

Kiểm tra menu, tabs bằng chuột và bàn phím, link ngoài, CV, workbook, Power BI, biểu đồ và các breakpoint 1920, 1440, 1366, 390, 375, 360 px. DevTools Console không được có lỗi nghiêm trọng; Network không được có asset 404.

## 5. Deploy Render Static Site

1. Push repository hoặc branch chứa thư mục này lên Git provider.
2. Trong Render chọn **New → Static Site** và kết nối repository.
3. Nếu repository vẫn giữ cả source Streamlit và thư mục tĩnh, đặt **Root Directory** là `portfolio-static`.
4. **Build Command:** để trống.
5. **Publish Directory:** `.`.
6. Deploy và kiểm tra URL `onrender.com` mới trước khi đụng tới service cũ.

`render.yaml` đã khai báo static publish path và hai security headers cơ bản. Site chỉ có một trang và dùng anchor, nên không cần rewrite `/*` về `index.html`.

## 6. Chuyển custom domain an toàn

1. Giữ nguyên Render Web Service Streamlit đang hoạt động.
2. Tạo và deploy Static Site bằng URL `onrender.com` riêng.
3. Kiểm tra toàn bộ nội dung, Power BI, desktop/mobile, link, CV, ảnh, Console và Network.
4. Khi đã xác nhận bản mới ổn định, gỡ `phuocnhat.dev` khỏi Web Service cũ.
5. Trong Static Site, mở **Settings → Custom Domains → Add Custom Domain** và thêm `phuocnhat.dev`.
6. Cập nhật DNS đúng theo giá trị Render hiển thị. Không đoán hoặc tái sử dụng record nếu Render hướng dẫn khác.
7. Chờ Render xác minh domain và cấp SSL.
8. Kiểm tra `https://phuocnhat.dev`, certificate, redirect HTTPS, Power BI, CV và asset.
9. Theo dõi bản mới ổn định rồi mới suspend/delete Web Service cũ.

Không chuyển DNS hoặc xóa Web Service cũ trong quá trình chuẩn bị source.

## 7. Rollback về Streamlit

Nếu Static Site có lỗi sau khi chuyển domain:

1. Giữ nguyên source và Web Service Streamlit cũ.
2. Gỡ custom domain khỏi Static Site.
3. Gắn lại domain vào Web Service cũ theo hướng dẫn Render.
4. Khôi phục DNS nếu Render yêu cầu giá trị khác.
5. Chờ SSL/domain verified rồi kiểm tra production.

Không cần phục hồi file vì bản static nằm trong thư mục riêng và source Streamlit chưa bị xóa.

## 8. Cập nhật nội dung

- Nội dung portfolio và SEO: `index.html`
- Giao diện: `css/style.css`
- Tương tác tabs/menu: `js/main.js`
- Power BI: tìm iframe có title `Power BI — Phân tích BCTC Chứng khoán Việt Nam` trong `index.html`. Link hiện tại được lấy nguyên văn từ `app.py`/`data/projects.json`.
- CV: thay `assets/documents/vo-phuoc-nhat-cv.pdf`, giữ nguyên tên để không phải sửa link.
- Ảnh: thay file tương ứng trong `assets/images/`, giữ nguyên tên và tỷ lệ hợp lý.
- Biểu đồ: thay `assets/charts/vn30f1m.html` và thư mục dependency đi kèm.

## 9. Bảo mật

Bản static không chứa API key, token, credential hoặc database configuration. Không đưa `.env`, `.streamlit/secrets.toml`, cookie hay private Power BI embed token vào thư mục này.

Source cũ hiện có mật khẩu PostgreSQL hard-code trong `upload_database.py`. Mật khẩu này không được sao chép sang bản static. Nên rotate credential trên database và chuyển cấu hình của script cũ sang environment variables trước lần sử dụng tiếp theo. Nếu repository từng được push công khai, cần coi mật khẩu cũ là đã lộ.

Power BI iframe dùng đúng public Publish-to-web URL có sẵn. Nội dung public qua Publish-to-web có thể được bất kỳ ai truy cập; không dùng cách này cho dữ liệu riêng tư.

## 10. Checklist production

- [ ] URL `onrender.com` tải ngay, không có Service Waking Up
- [ ] Header/menu hoạt động ở desktop và mobile
- [ ] Không có horizontal overflow ở 390, 375 và 360 px
- [ ] Tabs hoạt động bằng chuột, Enter và phím mũi tên
- [ ] Avatar, preview, ETL, ERD và ECharts tải không lỗi
- [ ] Power BI hiển thị và không vượt viewport
- [ ] CV và workbook tải đúng
- [ ] GitHub, LinkedIn và email đúng
- [ ] Không có asset 404 hoặc lỗi JavaScript nghiêm trọng
- [ ] `robots.txt`, `sitemap.xml`, favicon và metadata hoạt động
- [ ] Domain và SSL đã verified trước khi dừng Web Service cũ
- [ ] Credential PostgreSQL cũ đã được rotate

## 11. Giới hạn đã biết

- Power BI và Google Fonts phụ thuộc dịch vụ bên ngoài; phần HTML còn lại vẫn hiển thị khi chúng tải chậm.
- Project ngân hàng trong source có placeholder Power BI và đang bị lọc khỏi Home/navigation, nên không được đưa thành project công khai trong bản static.
- Link GitHub của project chứng khoán trong source là `#`, nên bản static không tạo một URL mới chưa được xác nhận.
- Bộ lọc backtest Streamlit dựa trên pandas. Bản static giữ workbook tải xuống và tiêu chí phân loại, nhưng không chạy pandas trong production.
