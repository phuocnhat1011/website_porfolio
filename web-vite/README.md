# Võ Phước Nhật Portfolio — React/Vite

Bản migration frontend của portfolio từ Streamlit sang React + Vite + TypeScript. Source Streamlit ở thư mục cha được giữ nguyên để đối chiếu.

## Công nghệ và kiến trúc

- React, Vite, TypeScript và React Router.
- CSS Modules theo component/page; không dùng UI framework hay animation library.
- Multi-route SPA: `/`, `/market-overview`, `/projects/securities`, `/projects/hedging`.
- Các view có trong source nhưng từng bị ẩn khỏi menu vẫn được bảo toàn tại `/projects/banking`, `/knowledge`, `/contact`.
- Dữ liệu project nằm trong `src/data/`; Market Overview dùng config riêng tại `src/data/marketOverview.ts`.
- Backtest được chuyển từ Excel sang JSON tĩnh ở `public/data/backtesting.json`; workbook gốc vẫn nằm trong `public/documents/` để download và đối chiếu.
- Power BI và chart được lazy-load khi mở tab. Không có access token, credential hoặc backend.

## 1. Chạy local

Yêu cầu Node.js 20.19+ hoặc 22.12+.

```bash
cd web-vite
npm install
npm run dev
```

Mở URL mà Vite hiển thị trong terminal (thường là `http://localhost:5173`).

## 2. Build production

```bash
cd web-vite
npm run build
```

Build output nằm trong `web-vite/dist`.

## 3. Preview production local

```bash
cd web-vite
npm run preview
```

## 4. Kiểm tra lint

```bash
cd web-vite
npm run lint
```

## 5. Cập nhật nội dung sau này

- Thêm/sửa project: `src/data/projects.ts`.
- Sửa nội dung Market Overview: `src/data/marketOverview.ts`.
- Sửa navigation: `src/config/site.ts`.
- Sửa skill: `src/data/skills.ts`.
- Sửa bài viết/tip: `src/data/knowledge.ts`.
- Sửa workflow Chứng khoán/Hedging: `src/data/securities.ts`, `src/data/hedging.ts`.
- Thay URL Power BI BCTC: chỉ sửa `powerBiUrl` của project trong `src/data/projects.ts`; không sửa `PowerBIEmbed.tsx`.
- Bật Power BI Market Overview: copy `.env.example` thành `.env.local` trong `web-vite/` và điền `VITE_MARKET_OVERVIEW_POWERBI_URL`. Khi biến để trống, trang chỉ hiển thị placeholder và không render iframe/action.
- Thay CV/ảnh: cập nhật file trong `public/documents/` hoặc `public/images/`, giữ nguyên tên file nếu không muốn sửa code.

## 6. Push lên GitHub

Từ repository root:

```bash
git status
git add .gitignore .env.example upload_database.py .tmp.driveupload/191 SECURITY_AUDIT.md MIGRATION_AUDIT.md MIGRATION_CHECKLIST.md DESIGN_IMPROVEMENTS.md web-vite
git commit -m "Migrate portfolio to React and Vite"
git push origin <ten-branch>
```

Không add file `.env` thật, PBIX, `node_modules` hoặc `dist`.

Credential PostgreSQL trong `upload_database.py` đã được chuyển sang environment variables. Tuy nhiên origin GitHub hiện public và giá trị cũ vẫn truy cập được trong raw file/lịch sử từ commit `f082a4c`; phải rotate ngay và làm sạch Git history trước khi tiếp tục public repository. Xem `SECURITY_AUDIT.md` ở repository root.

## 7. Import vào Vercel

1. Vào Vercel → **Add New Project** → import GitHub repository.
2. Chọn **Root Directory** là `web-vite`.
3. Framework Preset: **Vite**.
4. Install Command: `npm install`.
5. Build Command: `npm run build`.
6. Output Directory: `dist`.
7. `VITE_MARKET_OVERVIEW_POWERBI_URL` là tùy chọn. Chỉ thêm khi có public embed URL thật; để trống trong giai đoạn report đang hoàn thiện.
8. Deploy và kiểm tra các URL con như `/market-overview`, `/projects/securities` và `/projects/hedging`.

`vercel.json` đã cấu hình SPA rewrite để refresh trực tiếp URL con không trả về 404, theo hướng dẫn Vite SPA của Vercel: <https://vercel.com/docs/frameworks/frontend/vite>.

## 8. Gắn domain `phuocnhat.dev`

1. Trong Vercel project, mở **Settings → Domains**.
2. Thêm `phuocnhat.dev` và `www.phuocnhat.dev`.
3. Vercel sẽ hiển thị record DNS chính xác cho project. Tại DNS provider hiện tại:
   - Apex `phuocnhat.dev`: thường dùng A record theo giá trị Vercel cung cấp.
   - `www.phuocnhat.dev`: thường dùng CNAME theo giá trị Vercel cung cấp.
4. Không dùng giá trị ví dụ nếu dashboard Vercel đưa ra giá trị khác.
5. Chờ Vercel báo domain hợp lệ và DNS đã propagate.

Hướng dẫn chính thức: <https://vercel.com/docs/domains/set-up-custom-domain>.

## 9. HTTPS và redirect www

- Sau khi DNS được xác minh, Vercel tự cấp chứng chỉ HTTPS.
- Canonical của site đang là `https://phuocnhat.dev`.
- Trong domain settings, đặt `phuocnhat.dev` làm primary và redirect `www.phuocnhat.dev` về domain gốc để tránh duplicate content.
- Kiểm tra cả HTTP→HTTPS và www→apex sau khi DNS hoàn tất.

## 10. Power BI

- Report Chứng khoán giữ nguyên Publish to web URL từ source Streamlit.
- Report Market Overview dùng biến `VITE_MARKET_OVERVIEW_POWERBI_URL`; hiện chưa có public embed URL nên không render iframe, Fullscreen hoặc Open Report.
- Project Ngân hàng chưa có URL thật trong source nên hiển thị placeholder nhẹ “Báo cáo đang được hoàn thiện”, không tự tạo URL/token.
- `PowerBIEmbed` nhận URL qua props, có loading, fallback, responsive aspect ratio và fullscreen.
- Publish to web là report công khai; không đưa dữ liệu riêng tư vào report theo phương thức này.

## Cấu trúc chính

```text
web-vite/
├── public/
│   ├── charts/
│   ├── data/
│   ├── documents/
│   ├── icons/
│   └── images/
├── src/
│   ├── components/
│   │   ├── backtest/
│   │   ├── charts/
│   │   ├── layout/
│   │   ├── navigation/
│   │   ├── powerbi/
│   │   ├── projects/
│   │   └── sections/
│   ├── config/
│   ├── data/
│   ├── pages/
│   ├── styles/
│   └── types/
├── vercel.json
└── package.json
```
