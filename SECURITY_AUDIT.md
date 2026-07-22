# Security audit toàn repository

Ngày kiểm tra: 2026-07-22  
Phạm vi: toàn bộ repository `portfolio`, gồm source Streamlit cũ, utility Python, React/Vite, tài liệu, JSON, notebook (nếu có), chart HTML/JavaScript, asset Office/PBIX, file ẩn, file nén tracked, production bundle và lịch sử Git.

## 1. Kết luận

- Đã tìm thấy một PostgreSQL password thật được hard-code cùng username/host/database trong `upload_database.py`.
- Cùng credential đó còn có một bản sao nén trong file tracked `.tmp.driveupload/191`. File cache này đã được xóa khỏi working tree và `.tmp.driveupload/` đã được thêm vào `.gitignore`.
- `upload_database.py` vẫn giữ nguyên chức năng ETL, nhưng đọc toàn bộ cấu hình kết nối và đường dẫn dữ liệu từ environment variables. Connection URL được tạo bằng `sqlalchemy.URL.create`, không còn nội suy password vào chuỗi URI.
- Không tìm thấy API key, access token có giá trị, private key, email credential hoặc Power BI token trong source hiện tại hay production bundle.
- Credential cũ **vẫn tồn tại trong lịch sử Git**. Nó được đưa vào ở commit `f082a4c` và còn hiện diện trong các commit hậu duệ; commit `6896b4d` còn đưa cache `.tmp.driveupload/` chứa blob cũ vào repository.
- Origin `https://github.com/phuocnhat1011/website_porfolio` hiện đang public: repository, raw `main/upload_database.py` và trang commit `f082a4c` đều trả HTTP 200 khi kiểm tra không đăng nhập. Credential vì vậy phải được coi là **đã lộ công khai** và cần rotate ngay.

Không ghi lại giá trị secret thật trong tài liệu này.

## 2. File và nhóm file đã kiểm tra

| Phạm vi | File/nhóm file | Kết quả |
| --- | --- | --- |
| Streamlit | `app.py`, `shared.py`, `.streamlit/config.toml`, `requirements.txt` | Không có credential; Power BI Chứng khoán là URL Publish to web công khai, không phải token. |
| PostgreSQL utility | `upload_database.py` | Đã loại bỏ credential/path hard-code và chuyển sang biến môi trường. |
| Cấu hình project | `data/projects.json` | Có placeholder Power BI Ngân hàng, không phải secret; React không dùng URL giả này. |
| Script/chart | `script_chart.R`, `assets/vn30f1m.html`, `assets/vn30f1m_20260601_files/`, `assets/vn30f1m_files/` | Không có token value. Chuỗi `mapboxgl.accessToken = x.mapboxToken` là code generic của thư viện ECharts/echarts4r. |
| React source | Toàn bộ `web-vite/src/`, `index.html`, `vite.config.ts`, `vercel.json`, `package*.json`, `README.md` | Không có secret, local Windows asset path, localhost production link hoặc placeholder URL được bundle. |
| React public | Toàn bộ `web-vite/public/` | Không có secret; chart chỉ có generic access-token hook không gán giá trị. |
| Production | Toàn bộ `web-vite/dist/` sau build | Không có credential cũ, `.env`, sourcemap, placeholder URL, localhost link hoặc Windows path. Match `password` trong main JS chỉ là danh sách input type của React DOM. |
| Tài liệu/prototype | `*.md`, `design.html`, toàn bộ `portfolio-static/` | Không có secret thật; các localhost URL chỉ là hướng dẫn preview local. |
| Office/data | DOCX/XLSX trong `assets/` và `web-vite/public/documents/` | Đã quét nội dung archive; không tìm thấy secret theo các pattern mục tiêu. |
| Power BI Desktop | `PDS.pbix`, `bctc_chungkhoan.pbix`, `test_demo.pbix` | Không tìm thấy plaintext credential. Hai file có từ khóa `password`/`secretKey` trong metadata của custom visual Inforiver, không có giá trị credential được phát hiện. `*.pbix` đang bị ignore và không có trong Git history hiện tại. |
| File ẩn/cache | `.tmp.driveupload/`, `__pycache__/`, `.venv/`, `node_modules/` | Cache tracked đã được giải nén để quét; `.tmp.driveupload/191` chứa secret cũ và đã bị xóa. Generated dependency/cache không được đưa vào bundle và đã được kiểm tra tracking. |
| Git | Toàn bộ commits/branches/tags và path history của `upload_database.py`, `.tmp.driveupload/` | Secret được đưa vào ở `f082a4c`, còn trong 10 commit reachable; bản blob nén liên quan được track từ `6896b4d`. Origin/raw file/commit đều đang public. |

Ghi chú: PBIX là định dạng proprietary có thể giữ datasource metadata không hiển thị dưới dạng plaintext. Kết quả ở trên là static scan; tiếp tục không commit/publish PBIX là lựa chọn an toàn.

## 3. Thay đổi đã thực hiện

### `upload_database.py`

Script hiện yêu cầu các biến:

- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_HOST`
- `POSTGRES_PORT`
- `POSTGRES_DB`
- `PDS_FACT_FOLDER`
- `PDS_DIM_FOLDER`

Nếu thiếu biến, script dừng với thông báo rõ ràng; không fallback sang password hoặc đường dẫn máy cá nhân. Luồng đọc CSV/Excel và ghi PostgreSQL không bị xóa.

### Environment và Git ignore

- Tạo `.env.example` chỉ chứa tên biến và giá trị mẫu không nhạy cảm.
- `.gitignore` bỏ qua `.env`, `.env.*`, `.tmp.driveupload/`, nhưng cho phép track `.env.example`.
- Xóa `.tmp.driveupload/191` khỏi working tree. Đây là cache nén không được ứng dụng tham chiếu và có thể phục hồi từ Git history.

## 4. False positive đã xác minh

- `password` trong bundle React: tên HTML input type của React DOM, không có credential.
- `mapboxgl.accessToken = x.mapboxToken` trong chart: hook thư viện, không có token value.
- `password` và `secretKey` trong hai PBIX: chuỗi metadata của custom visual Inforiver, không phát hiện giá trị credential.
- Email công khai, GitHub/LinkedIn URL và Power BI Publish to web URL là nội dung portfolio, không phải credential.
- `POSTGRES_PASSWORD` trong `.env.example` và `required_env("POSTGRES_PASSWORD")` chỉ là tên biến/sample, không phải secret thật.

## 5. Việc bắt buộc phải làm thủ công

1. **Rotate PostgreSQL password ngay**. Credential đã public; không chờ đến lúc push migration. Nếu password từng được tái sử dụng, rotate ở mọi nơi liên quan.
2. Cân nhắc chuyển origin sang private ngay trong lúc xử lý để hạn chế tiếp tục lộ; việc này không thay thế rotation.
3. Xác nhận user/database không còn chấp nhận password cũ; đóng session/connection cũ nếu hệ thống hỗ trợ.
4. Làm sạch Git history trên mọi branch/tag, xử lý cả `upload_database.py` và toàn bộ `.tmp.driveupload/`. Thực hiện trên bản backup bằng `git filter-repo` hoặc BFG, rồi phối hợp force-push vì commit hash sẽ thay đổi.
5. Kiểm tra fork, clone, archive, CI log và remote cache; history rewrite không thu hồi được secret đã bị sao chép.
6. Chỉ để repository public trở lại sau khi scan lại history đã rewrite và xác nhận credential đã rotate.

## 6. Trạng thái public/private

- Working tree và production bundle hiện tại không còn giá trị credential thật.
- Production dependencies: `npm audit --omit=dev` báo 0 vulnerability ở mọi mức.
- **Private repository:** chưa thể gọi là hoàn toàn an toàn trước khi rotate; history vẫn chứa secret đã bị public. Chỉ nên tiếp tục làm việc trên private remote được kiểm soát sau khi rotate, hoặc dùng nó như bước tạm để phối hợp history rewrite.
- **Public repository:** **không an toàn để public ở thời điểm này**. Origin thực tế đang public và credential cũ vẫn truy cập được; cần rotate, rewrite/force-push history và scan lại.
