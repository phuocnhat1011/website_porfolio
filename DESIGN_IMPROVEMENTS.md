# Design improvements đề xuất sau migration

Các đề xuất dưới đây **chưa được áp dụng** để bản React đầu tiên giữ thiết kế, màu sắc, font, thứ tự và trải nghiệm gần source Streamlit nhất.

## Ưu tiên cao

1. **Bổ sung link thật cho repository Chứng khoán**  
   Source hiện dùng `#`, vì vậy CTA đang disabled. Khi có URL thật, chỉ cần thêm vào `src/data/projects.ts`.

2. **Hoàn thiện project Ngân hàng**  
   Cập nhật Publish to web URL, cover riêng và xác nhận lại nội dung hiện đang dùng một số mô tả giống project Chứng khoán trong `data/projects.json`.

3. **Quyết định có công khai Knowledge/Contact hay không**  
   Hai page đã được migrate nhưng giữ ngoài menu vì source Streamlit hiện comment navigation. Có thể thêm vào menu sau khi duyệt nội dung.

4. **Social preview chuyên dụng**  
   Hiện Open Graph dùng avatar có sẵn. Có thể thiết kế ảnh OG landscape 1200×630 theo đúng brand khi chuyển sang giai đoạn redesign.

## Trải nghiệm và nội dung

5. Thêm breadcrumb nhẹ trên project page nếu số project tăng.
6. Cho phép link trực tiếp đến từng project tab bằng query/hash sau khi chốt URL scheme.
7. Thêm ngày cập nhật cho dữ liệu Backtest để người xem biết độ mới của kết quả.
8. Bổ sung disclaimer rõ ràng cho nội dung trading/backtest nếu portfolio được dùng cho mục đích tuyển dụng hoặc chia sẻ công khai rộng rãi.
9. Rà soát lại thuật ngữ Việt/Anh để thống nhất cách viết giữa hai project.

## Hiệu năng/kỹ thuật

10. Tách chart ECharts tự chứa sang phiên bản non-self-contained tối ưu hơn nếu có thể kiểm soát pipeline sinh chart.
11. Tự host Plus Jakarta Sans nếu muốn loại bỏ request Google Fonts và đảm bảo font luôn giống nhau trong mạng nội bộ.
12. Tạo pipeline tự động chuyển workbook Backtest sang JSON mỗi lần dữ liệu Excel thay đổi.
13. Thêm automated accessibility test và visual regression test sau khi layout ổn định.

## Không khuyến nghị ở giai đoạn hiện tại

- Không thêm animation library hoặc UI framework nặng.
- Không thêm backend chỉ để serve dữ liệu tĩnh.
- Không chuyển Power BI Publish to web sang secure embed nếu chưa có yêu cầu xác thực và backend tạo token.
