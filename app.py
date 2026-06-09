import json
import base64
import html as _html
from pathlib import Path
import streamlit as st
from shared import apply_style, cover_block

# ---------------------------------------------------------
# 1. PAGE LAYOUT CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Võ Phước Nhật | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply global custom styles from shared.py
apply_style()


# ---------------------------------------------------------
# 2. TAB RENDER FUNCTIONS
# ---------------------------------------------------------

def render_home():
    # Load projects data
    with open("data/projects.json", "r", encoding="utf-8") as f:
        projects = json.load(f)
    
    # Load avatar base64 string
    avatar_b64 = ""
    try:
        avatar_bytes = Path("assets/avatar.jpg").read_bytes()
        avatar_b64 = base64.b64encode(avatar_bytes).decode("utf-8")
    except Exception:
        avatar_b64 = ""
        
    hero_avatar_html = (
        f"<div class='avatar-ring'><img class='avatar-img' src='data:image/jpeg;base64,{avatar_b64}'/></div>"
        if avatar_b64
        else "<div class='avatar-ring'><div class='avatar-img' style='display:flex;align-items:center;justify-content:center;font-weight:700;background:#5B21B6;color:white;'>VNJ</div></div>"
    )
    
    # Hero profile introduction
    st.markdown(
        f"""
        <div class="hero">
          <div class="hero-row">
            <div class="hero-left">
              <h1 style="margin:0; font-size: 2.4rem;">👋 Võ Phước Nhật</h1>
              <p class="muted" style="font-size:1.05rem; margin-top:14px;">
                Mình xây dựng các <b>Power BI dashboards</b> chuyên nghiệp cho <b>BCTC</b> (Ngân hàng & Chứng khoán VN) —
                tập trung vào <b>data modeling</b>, <b>DAX</b> và <b>trải nghiệm người dùng (UX)</b> để người xem ra insight nhanh nhất.
              </p>
              <div style="margin-top:16px;">
                <span class="badge">Power BI</span>
                <span class="badge">DAX</span>
                <span class="badge">Financial Statements</span>
                <span class="badge">Data Modeling</span>
                <span class="badge">Python</span>
              </div>
            </div>
            <div class="hero-right">
              {hero_avatar_html}
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # L-Layout main grid (2 columns)
    col_left, col_right = st.columns([2, 3])
    
    with col_left:
        st.markdown("<div class='section-title' style='font-size: 1.4rem; margin-bottom:12px;'>Hồ Sơ Cá Nhân</div>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="border-left: 3px solid #5B21B6; padding-left: 16px; margin-bottom: 20px; margin-top: 8px;">
                <p style="font-size: 0.98rem; line-height: 1.65; margin: 0; color: #475569; font-style: italic;">
                "Đam mê kết hợp phân tích tài chính với kỹ thuật dữ liệu hiện đại để tạo ra các dashboard báo cáo có giá trị thực tế cao. 
                Tập trung giải quyết các bài toán dữ liệu lớn, trích xuất dữ liệu phi cấu trúc và mô hình hoá đa chiều."
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        cv_path = Path("assets/CV.pdf")
        if cv_path.exists():
            try:
                with open(cv_path, "rb") as f:
                    st.download_button("📥 Tải bản CV đầy đủ (PDF)", data=f, file_name="Vo-Phuoc-Nhat-CV.pdf", type="primary", use_container_width=False)
            except Exception as e:
                st.info("💡 Đã tìm thấy CV.pdf nhưng có lỗi khi đọc file. Vui lòng kiểm tra lại quyền truy cập.")
        else:
            st.info("💡 Lưu ý: Đặt file `assets/CV.pdf` để bật nút download CV.")
            
    with col_right:
        st.markdown("<div class='section-title' style='font-size: 1.4rem; margin-bottom:12px;'>Thế Mạnh Chuyên Môn</div>", unsafe_allow_html=True)
        
        st.markdown(
            """
            <div style="display: flex; gap: 14px; align-items: stretch; justify-content: space-between; margin-top: 8px;">
                <div class="kpi" style="flex: 1; display: flex; flex-direction: column; justify-content: space-between; padding: 16px 14px;">
                    <div>
                        <div style="font-size: 1.5rem; margin-bottom: 8px;">📊</div>
                        <b style="font-size: 0.9rem; color: #0F172A; display: block; line-height: 1.3;">2 Flagship Dashboards</b>
                    </div>
                    <div class="muted" style="font-size: 0.78rem; margin-top: 6px; line-height: 1.35;">Ngân hàng & CK VN phân tích sâu.</div>
                </div>
                <div class="kpi" style="flex: 1; display: flex; flex-direction: column; justify-content: space-between; padding: 16px 14px;">
                    <div>
                        <div style="font-size: 1.5rem; margin-bottom: 8px;">🧠</div>
                        <b style="font-size: 0.9rem; color: #0F172A; display: block; line-height: 1.3;">Modeling + DAX</b>
                    </div>
                    <div class="muted" style="font-size: 0.78rem; margin-top: 6px; line-height: 1.35;">Schema tối ưu & measures hiệu năng cao.</div>
                </div>
                <div class="kpi" style="flex: 1; display: flex; flex-direction: column; justify-content: space-between; padding: 16px 14px;">
                    <div>
                        <div style="font-size: 1.5rem; margin-bottom: 8px;">🧭</div>
                        <b style="font-size: 0.9rem; color: #0F172A; display: block; line-height: 1.3;">Trải nghiệm UX mượt</b>
                    </div>
                    <div class="muted" style="font-size: 0.78rem; margin-top: 6px; line-height: 1.35;">Menu-driven navigation tinh gọn.</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
    st.markdown("<hr/>", unsafe_allow_html=True)
    
    # Flagship Projects section
    st.markdown("<div class='section-title'>Dự án Tiêu Biểu</div>", unsafe_allow_html=True)
    st.markdown(
        "<p class='muted' style='margin-bottom:20px;'>Các dự án phân tích dữ liệu tài chính chính — bấm vào để mở rộng chi tiết.</p>",
        unsafe_allow_html=True,
    )
    
    # Accordion global session state
    if "home_acc_open" not in st.session_state:
        st.session_state.home_acc_open = None

    def _toggle_home(pid: str, section: str):
        key = f"{pid}::{section}"
        st.session_state.home_acc_open = None if st.session_state.home_acc_open == key else key

    def _is_home_open(pid: str, section: str) -> bool:
        return st.session_state.home_acc_open == f"{pid}::{section}"

    def _fw_button(label: str, key: str) -> bool:
        return st.button(label, key=key, use_container_width=True)

    def _ul_html(items):
        lis = "".join([f"<li>{_html.escape(str(x))}</li>" for x in items])
        return f"<ul>{lis}</ul>"

    def _section_box(pid: str, section: str, title: str, content_html: str):
        opened = _is_home_open(pid, section)
        caret = "▾" if opened else "▸"
        if _fw_button(f"{caret} {title}", key=f"home_btn_{pid}_{section}"):
            _toggle_home(pid, section)
            st.rerun()
        if opened:
            st.markdown(
                f"<div class='surface surface-tight' style='margin-top:8px;'>{content_html}</div>",
                unsafe_allow_html=True,
            )

    def _status_badge(status: str) -> str:
        status = (status or "").upper()
        if status == "DOING":
            return "<span class='badge' style='background: rgba(245, 158, 11, 0.1) !important; color: #D97706 !important; border-color: rgba(245, 158, 11, 0.2) !important;'>🟡 DOING</span>"
        if status == "DONE":
            return "<span class='badge' style='background: rgba(16, 185, 129, 0.1) !important; color: #059669 !important; border-color: rgba(16, 185, 129, 0.2) !important;'>🟢 DONE</span>"
        return ""

    # Grid layout for 2 projects
    cols = st.columns(2)
    for idx, p in enumerate(projects):
        pid = p.get("id", f"p_{idx}")
        with cols[idx % 2]:
            with st.container():
                cover_block(p.get("cover"), height=160)
                st.markdown(f"<h3 style='margin:0; font-size:1.25rem;'>{p.get('title','')}</h3>", unsafe_allow_html=True)
                
                sb = _status_badge(p.get("status"))
                if sb:
                    st.markdown(f"<div class='status-label'>Status: {sb}</div>", unsafe_allow_html=True)
                
                tagline = (p.get("tagline") or "").strip()
                if tagline:
                    st.markdown(f"<div class='muted' style='font-size:0.88rem; min-height: 40px;'>{tagline}</div>", unsafe_allow_html=True)
                
                # Stack
                st.markdown("".join([f"<span class='badge'>{s}</span>" for s in p.get("stack", [])]), unsafe_allow_html=True)
                
                st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
                
                # Actions/CTAs
                if pid == "securities_vn":
                    if st.button("📊 Mở dashboard", type="primary", use_container_width=True, key=f"cta_{pid}"):
                        st.switch_page(securities_page)
                elif pid == "bank_bctc":
                    if st.button("📊 Mở dashboard", type="primary", use_container_width=True, key=f"cta_{pid}"):
                        st.switch_page(bank_page)
                else:
                    st.button("🔧 Hệ thống Backend (Không demo)", type="secondary", disabled=True, use_container_width=True, key=f"cta_{pid}")
                
                # Accordion sections
                highlights = p.get("highlights", [])
                what = p.get("what_i_did", [])
                proc = p.get("process", [])
                
                if highlights:
                    _section_box(pid, "highlights", "✨ Điểm nổi bật", _ul_html(highlights))
                if what:
                    _section_box(pid, "what", "🛠️ Bạn đã làm gì", _ul_html(what))
                if proc:
                    _section_box(pid, "process", "🧭 Quy trình", _ul_html(proc))


def render_bank():
    import streamlit.components.v1 as components
    
    st.header("🏦 Phân tích BCTC Ngân Hàng Việt Nam")
    st.markdown(
        """
        <p class='muted' style='font-size: 1.05rem; margin-bottom: 24px;'>
        Hệ thống thu thập và phân tích tự động Báo cáo tài chính (BCTC) ngành ngân hàng thương mại Việt Nam. 
        Dự án giải quyết bài toán đồng nhất dữ liệu tài chính đa nguồn, tự động hóa luồng xử lý và trực quan hóa 
        các chỉ số tài chính đặc thù của ngân hàng như NIM, nợ xấu (NPL), và cơ cấu tài sản sinh lời.
        </p>
        """,
        unsafe_allow_html=True
    )
    
    # 4 Sub-tabs navigation
    tab_summary, tab_pipeline, tab_code, tab_pbi = st.tabs(["Tổng quan", "Quy trình", "Code mẫu", "Power BI"])
    
    with tab_summary:
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                <div class="card" style="height: 100%; min-height: 280px;">
                    <h3 style="margin-top: 0; color: #5B21B6; font-size:1.3rem;">🎯 Bối cảnh & Nhiệm vụ (STAR)</h3>
                    <p><b>Situation (Bối cảnh):</b> Báo cáo tài chính của các ngân hàng thương mại Việt Nam có tính chất đặc thù rất cao (thu nhập lãi thuần, NIM, tỷ lệ nợ xấu NPL...) và thường được phân tán trên nhiều nguồn khác nhau dưới dạng PDF quét. Việc tổng hợp dữ liệu, tính toán các chỉ số an toàn vốn và phân tích cơ cấu tài sản sinh lời thủ công tốn rất nhiều thời gian và dễ sai sót.</p>
                    <p><b>Task (Nhiệm vụ):</b> Xây dựng giải pháp tự động hóa thu thập và chuẩn hóa dữ liệu tài chính cho nhóm các ngân hàng lớn toàn thị trường, giúp chuyển đổi nhanh dữ liệu thô sang Star Schema để tính toán tức thời các chỉ số tài chính.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                """
                <div class="card" style="height: 100%; min-height: 280px;">
                    <h3 style="margin-top: 0; color: #2563EB; font-size:1.3rem;">⚡ Hành động & Kết quả</h3>
                    <p><b>Action (Hành động):</b>
                        <ul>
                            <li>Xây dựng pipeline Python tự động thu thập và chuẩn hóa dữ liệu BCTC ngân hàng theo kỳ hạn.</li>
                            <li>Thiết kế mô hình dữ liệu quan hệ tối ưu Star Schema phân bổ theo kỳ hạn và nhóm nợ.</li>
                            <li>Phát triển hệ thống các measures DAX phức tạp để tính toán chỉ số NIM, tỷ lệ nợ xấu, và biên lợi nhuận lãi thuần.</li>
                            <li>Thiết kế giao diện dashboard Power BI trực quan dựa trên phương pháp định hướng module.</li>
                        </ul>
                    </p>
                    <p><b>Result (Kết quả):</b>
                        <ul>
                            <li>Tự động hóa hoàn toàn quy trình xử lý dữ liệu tài chính ngân hàng, giúp <b>tiết kiệm 2 giờ</b> làm việc mỗi ngày.</li>
                            <li>Độ chính xác chuẩn hóa đạt <b>99.9%</b>.</li>
                            <li>Cung cấp cái nhìn toàn diện về sức khỏe tài chính của các ngân hàng chỉ trong <b>vài giây</b>.</li>
                        </ul>
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    with tab_pipeline:
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        st.markdown("### 🔄 Quy trình ETL & Kiến trúc Dữ liệu Ngân hàng")
        st.markdown(
            "Sơ đồ quy trình mô tả luồng di chuyển dữ liệu từ nguồn thông tin phi cấu trúc, "
            "qua pipeline xử lý và lưu trữ dữ liệu tập trung, cho đến lớp biểu diễn trực quan trên Power BI."
        )
        
        img_path = Path("assets/previews/etl_pipeline.png")
        if img_path.exists():
            st.image(str(img_path), caption="Kiến trúc quy trình ETL tự động hóa dữ liệu BCTC Ngân hàng", use_container_width=True)
        else:
            st.info("💡 Lưu ý: Hãy đặt sơ đồ kiến trúc tại `assets/previews/etl_pipeline.png` để hiển thị sơ đồ.")
            
    with tab_code:
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        st.markdown("### 💻 Mã nguồn Kỹ thuật Tiêu biểu (Ngân hàng)")
        
        st.markdown(
            """
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px; margin-top: 12px;">
                <span style="background: #10B981; color: white; padding: 3px 10px; border-radius: 6px; font-size: 0.78rem; font-weight: bold; text-transform: uppercase;">Python</span>
                <span style="font-weight: 700; color: #0F172A; font-size: 1.05rem;">Chuẩn hóa dữ liệu BCTC Ngân hàng</span>
            </div>
            """, 
            unsafe_allow_html=True
        )
        st.code(
            """
# File python xử lý làm sạch và chuyển đổi cấu trúc BCTC ngân hàng (tương tự chứng khoán)
def clean_and_normalize_banking_financials(raw_data_list):
    # Code xử lý đặc thù cho các chỉ tiêu BCTC ngân hàng
    pass
            """,
            language="python"
        )
        
    with tab_pbi:
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        
        # Read bank powerbi_url from projects.json dynamically
        bank_url = ""
        try:
            with open("data/projects.json", "r", encoding="utf-8") as f:
                projs = json.load(f)
                bank_url = next((p["powerbi_url"] for p in projs if p["id"] == "bank_bctc"), "")
        except Exception:
            bank_url = ""
            
        if not bank_url or "PASTE_YOUR" in bank_url:
            st.warning("⚠️ Bạn chưa cấu hình đường dẫn Power BI thực tế cho dự án Ngân Hàng. Vui lòng cập nhật `powerbi_url` của dự án 'bank_bctc' trong file `data/projects.json`.")
        else:
            st.markdown(
                f"""
                <div style="width:100%; height:820px; margin-top: 10px;">
                    <iframe 
                        src="{bank_url}" 
                        style="width:100%; height:100%; border:1px solid rgba(226, 232, 240, 0.8); border-radius:16px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);"
                        allowfullscreen="true">
                    </iframe>
                  </div>
                  """,
                  unsafe_allow_html=True
              )


def render_securities():
    import streamlit.components.v1 as components
    
    st.header("📊 Phân tích BCTC Chứng Khoán Việt Nam")
    st.markdown(
        """
        <p class='muted' style='font-size: 1.05rem; margin-bottom: 24px;'>
        Hệ thống thu thập và phân tích tự động Báo cáo tài chính (BCTC) ngành chứng khoán Việt Nam. 
        Dự án giải quyết bài toán đồng nhất dữ liệu tài chính đa chiều, tự động hóa luồng xử lý và trực quan hóa 
        các chỉ số tài chính trọng yếu phục vụ hoạt động theo dõi và đánh giá danh mục tự doanh (FVTPL, AFS).
        </p>
        """,
        unsafe_allow_html=True
    )
    
    # 4 Sub-tabs navigation
    tab_summary, tab_pipeline, tab_code, tab_pbi = st.tabs(["Tổng quan", "Quy trình", "Code mẫu", "Power BI"])
    
    with tab_summary:
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                <div class="card" style="height: 100%; min-height: 280px;">
                    <h3 style="margin-top: 0; color: #5B21B6; font-size:1.3rem;">🎯 Bối cảnh & Nhiệm vụ (STAR)</h3>
                    <p><b>Situation (Bối cảnh):</b> Báo cáo tài chính của các công ty chứng khoán Việt Nam thường được công bố ở dạng tài liệu PDF thô hoặc bảng biểu không đồng nhất qua nhiều kênh khác nhau. Điều này khiến cho việc tổng hợp dữ liệu, so sánh chỉ số và đặc biệt là phân tích chi tiết cấu trúc danh mục đầu tư tự doanh <b>FVTPL</b>, <b>AFS</b> gặp nhiều khó khăn, tốn kém thời gian nhập liệu thủ công.</p>
                    <p><b>Task (Nhiệm vụ):</b> Xây dựng một giải pháp kỹ thuật tự động hóa để thu thập, chuẩn hóa dữ liệu tài chính đa chiều cho <b>500+ mã</b> doanh nghiệp và chứng khoán toàn thị trường, giúp chuyển đổi dữ liệu thô thành thông tin phân tích có cấu trúc một cách nhanh chóng.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                """
                <div class="card" style="height: 100%; min-height: 280px;">
                    <h3 style="margin-top: 0; color: #2563EB; font-size:1.3rem;">⚡ Hành động & Kết quả</h3>
                    <p><b>Action (Hành động):</b>
                        <ul>
                            <li>Thiết kế pipeline crawl dữ liệu tự động bằng Python từ các nguồn cung cấp thông tin tài chính uy tín.</li>
                            <li>Xây dựng mô hình dữ liệu quan hệ tối ưu theo mô hình <b>Star Schema</b> (Dim/Fact) trên hệ quản trị cơ sở dữ liệu.</li>
                            <li>Tạo hệ thống <b>DAX Measures</b> hiệu năng cao để tính toán biên lợi nhuận ròng, tỷ suất sinh lời ROA, ROE và cơ cấu đóng góp tự doanh.</li>
                            <li>Thiết kế báo cáo Power BI trực quan dựa trên phương pháp định hướng module (Menu-driven).</li>
                        </ul>
                    </p>
                    <p><b>Result (Kết quả):</b>
                        <ul>
                            <li>Tự động hóa hoàn toàn quy trình cập nhật dữ liệu tài chính, giúp <b>tiết kiệm 2 giờ</b> làm việc thủ công mỗi ngày.</li>
                            <li>Quy trình làm sạch đạt độ chính xác dữ liệu lên tới <b>99.9%</b>.</li>
                            <li>Trích xuất và trực quan hóa chi tiết cơ cấu tự doanh của toàn ngành chỉ trong <b>vài giây</b>.</li>
                        </ul>
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    with tab_pipeline:
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        st.markdown("### 🔄 Quy trình ETL & Kiến trúc Dữ liệu")
        st.markdown(
            "Sơ đồ quy trình dưới đây mô tả luồng di chuyển dữ liệu từ nguồn thông tin phi cấu trúc, "
            "qua pipeline xử lý và lưu trữ dữ liệu tập trung, cho đến lớp biểu diễn trực quan trên Power BI."
        )
        
        img_path = Path("assets/previews/etl_pipeline.png")
        if img_path.exists():
            st.image(str(img_path), caption="Kiến trúc quy trình ETL tự động hóa dữ liệu BCTC Chứng khoán", use_container_width=True)
        else:
            st.info("💡 Lưu ý: Hãy đặt sơ đồ kiến trúc tại `assets/previews/etl_pipeline.png` để hiển thị sơ đồ.")
            
    with tab_code:
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        st.markdown("### 💻 Mã Nguồn Kỹ Thuật Tiêu Biểu")
        
        # Python Code block
        st.markdown(
            """
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px; margin-top: 12px;">
                <span style="background: #10B981; color: white; padding: 3px 10px; border-radius: 6px; font-size: 0.78rem; font-weight: bold; text-transform: uppercase;">Python</span>
                <span style="font-weight: 700; color: #0F172A; font-size: 1.05rem;">Chuẩn hóa & xoay trục (Unpivot) Fact table tài chính</span>
            </div>
            """, 
            unsafe_allow_html=True
        )
        st.code(
            """
import pandas as pd
import requests

def clean_and_normalize_financials(raw_data_list):
    # Khởi tạo dataframe từ dữ liệu thô
    df = pd.DataFrame(raw_data_list)
    
    # 1. Điền giá trị trống & chuẩn hóa kiểu dữ liệu
    df['value'] = pd.to_numeric(df['value'], errors='coerce').fillna(0)
    df['item_code'] = df['item_code'].str.strip().str.upper()
    df['company_code'] = df['company_code'].str.strip().str.upper()
    
    # 2. Unpivot dữ liệu để tạo Fact Table chuẩn tinh gọn
    fact_df = df.melt(
        id_vars=['company_code', 'fiscal_year', 'fiscal_quarter', 'item_code'],
        value_vars=['value'],
        var_name='metric_type',
        value_name='amount'
    )
    
    # 3. Tạo khoá phụ cho bảng Calendar
    fact_df['date_key'] = fact_df['fiscal_year'].astype(str) + "Q" + fact_df['fiscal_quarter'].astype(str)
    
    return fact_df
            """,
            language="python"
        )
        
        st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
        
        # SQL Code block
        st.markdown(
            """
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                <span style="background: #2563EB; color: white; padding: 3px 10px; border-radius: 6px; font-size: 0.78rem; font-weight: bold; text-transform: uppercase;">SQL</span>
                <span style="font-weight: 700; color: #0F172A; font-size: 1.05rem;">Xoay trục dữ liệu quan hệ & Tính chỉ số tài chính sinh lời</span>
            </div>
            """, 
            unsafe_allow_html=True
        )
        st.code(
            """
WITH raw_financials AS (
    SELECT 
        company_code,
        fiscal_year,
        fiscal_quarter,
        item_code,
        value
    FROM staging_sec_financials
),
pivoted_items AS (
    SELECT 
        company_code,
        fiscal_year,
        fiscal_quarter,
        MAX(CASE WHEN item_code = 'FVTPL_REV' THEN value END) as fvtpl_revenue,
        MAX(CASE WHEN item_code = 'TOTAL_REV' THEN value END) as total_revenue,
        MAX(CASE WHEN item_code = 'NET_PROFIT' THEN value END) as net_profit,
        MAX(CASE WHEN item_code = 'TOTAL_ASSETS' THEN value END) as total_assets,
        MAX(CASE WHEN item_code = 'OWNER_EQUITY' THEN value END) as owner_equity
    FROM raw_financials
    GROUP BY company_code, fiscal_year, fiscal_quarter
)
SELECT 
    company_code,
    fiscal_year,
    fiscal_quarter,
    total_revenue,
    net_profit,
    -- Ratios
    ROUND((net_profit::numeric / NULLIF(total_revenue, 0)) * 100, 2) as net_profit_margin,
    ROUND((net_profit::numeric / NULLIF(total_assets, 0)) * 100, 2) as roa,
    ROUND((net_profit::numeric / NULLIF(owner_equity, 0)) * 100, 2) as roe,
    -- Tỷ trọng đóng góp tự doanh
    ROUND((fvtpl_revenue::numeric / NULLIF(total_revenue, 0)) * 100, 2) as fvtpl_rev_ratio
FROM pivoted_items
ORDER BY company_code, fiscal_year DESC, fiscal_quarter DESC;
            """,
            language="sql"
        )
        
    with tab_pbi:
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        POWER_BI_URL = "https://app.powerbi.com/view?r=eyJrIjoiNTAxZjNhMDAtOTY2ZS00YWJiLTljOTktM2VjMzhjNDMxN2Y3IiwidCI6IjI4ZmZjMDE1LWFlOWEtNDEzNC1hOGQ2LWU3MTI4MTEzMDc2OSIsImMiOjEwfQ%3D%3D"
        st.markdown(
            f"""
            <div style="width:100%; height:820px; margin-top: 10px;">
                <iframe 
                    src="{POWER_BI_URL}" 
                    style="width:100%; height:100%; border:1px solid rgba(226, 232, 240, 0.8); border-radius:16px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);"
                    allowfullscreen="true">
                </iframe>
            </div>
            """,
            unsafe_allow_html=True
        )


def render_knowledge():
    st.markdown("<div class='section-title'>🧠 Góc Chia Sẻ Kiến Thức</div>", unsafe_allow_html=True)
    st.markdown(
        "<p class='muted'>Kinh nghiệm thực tế, mẹo lập trình và các bài viết sâu về phân tích dữ liệu tài chính & tối ưu hóa Power BI.</p>",
        unsafe_allow_html=True
    )
    
    col_tips, col_articles = st.columns(2)
    
    with col_tips:
        st.markdown("<h3 style='border-bottom: 2px solid #5B21B6; padding-bottom: 8px; font-size:1.3rem;'>💡 Tips Ngắn & Thủ Thuật</h3>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("##### 🚀 Tối ưu hóa hiệu năng DAX với `KEEPFILTERS` instead of `CALCULATE` filters")
            st.write(
                "Khi bạn viết một điều kiện lọc đơn giản trong `CALCULATE`, mặc định nó sẽ thay thế toàn bộ bộ lọc hiện tại trên cột đó. "
                "Sử dụng `KEEPFILTERS` sẽ giữ nguyên bộ lọc ngữ cảnh ngoài và giao thoa với bộ lọc mới. Giúp cải thiện tốc độ đáng kể trong các báo cáo lớn."
            )
            st.code(
                """
-- Lọc không tối ưu (Ghi đè filter)
Sales_VN = CALCULATE([Total Sales], Customer[Country] = "Vietnam")

-- Lọc tối ưu (Giữ lại filter)
Sales_VN_Optimized = CALCULATE(
    [Total Sales], 
    KEEPFILTERS(Customer[Country] = "Vietnam")
)
                """,
                language="dax"
            )
            
        with st.container(border=True):
            st.markdown("##### 🏗️ Thiết kế Star Schema cho báo cáo tài chính thay vì Flat Table")
            st.write(
                "Nhiều người có xu hướng kéo tất cả các cột dữ liệu vào một bảng Fact lớn. Trong BCTC đa chỉ tiêu, "
                "việc tách bảng Chỉ tiêu tài chính (`Dim_Items`) và bảng Công ty (`Dim_Company`) riêng biệt sẽ giúp "
                "viết mã DAX tính tăng trưởng YoY/QoQ ngắn gọn và tái sử dụng dễ dàng hơn."
            )
            
    with col_articles:
        st.markdown("<h3 style='border-bottom: 2px solid #2563EB; padding-bottom: 8px; font-size:1.3rem;'>📚 Bài Viết Phân Tích Sâu</h3>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("##### 🏦 Thiết kế Schema Dữ liệu BCTC Ngành Ngân Hàng: Từ Raw Data đến Star Schema")
            st.markdown("<p class='muted' style='font-size:0.85rem;'>Người viết: Võ Phước Nhật | 5 phút đọc</p>", unsafe_allow_html=True)
            st.write(
                "Khác với doanh nghiệp thương mại, BCTC ngân hàng có cấu trúc đặc thù như NIM, nợ xấu (NPL), và hệ số an toàn vốn CAR. "
                "Bài viết này chia sẻ phương pháp thiết kế bảng Fact cân đối kế toán kết hợp phân bổ theo kỳ hạn và nhóm nợ, "
                "giúp nhà phân tích dễ dàng drill-down sâu vào thuyết minh dư nợ cho vay khách hàng."
            )
            
        with st.container(border=True):
            st.markdown("##### 🤖 Tự động hoá trích xuất Thuyết minh BCTC bằng Python & AI (FVTPL & AFS)")
            st.markdown("<p class='muted' style='font-size:0.85rem;'>Người viết: Võ Phước Nhật | 7 phút đọc</p>", unsafe_allow_html=True)
            st.write(
                "Thuyết minh báo cáo tài chính là mỏ vàng thông tin nhưng thường được lưu trữ dưới dạng bảng PDF scan phi cấu trúc. "
                "Bài viết này trình bày chi tiết cách xây dựng pipeline RAG (Retrieval-Augmented Generation) kết hợp OCR độ phân giải cao "
                "để tìm kiếm, phân tích và trích xuất tự động danh mục đầu tư tài chính FVTPL, AFS của các công ty chứng khoán."
            )


def render_contact():
    st.markdown("<div class='section-title'>👤 Thông Tin Liên Hệ & Kỹ Năng</div>", unsafe_allow_html=True)
    st.markdown(
        "<p class='muted'>Kết nối với mình hoặc tìm hiểu thêm về các công nghệ mình đang sử dụng.</p>",
        unsafe_allow_html=True
    )
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("<h3 style='border-bottom: 2px solid #E2E8F0; padding-bottom: 8px; font-size:1.3rem;'>✉️ Thông Tin Liên Hệ</h3>", unsafe_allow_html=True)
        
        st.markdown(
            """
            <div class="card" style="margin-bottom: 20px;">
                <p>💡 <b>Họ và tên:</b> Võ Phước Nhật</p>
                <p>📧 <b>Email:</b> <a href="mailto:nhat.vophuoc@gmail.com">nhat.vophuoc@gmail.com</a></p>
                <p>🔗 <b>LinkedIn:</b> <a href="https://linkedin.com/in/phuocnhat1011" target="_blank">linkedin.com/in/phuocnhat1011</a></p>
                <p>🐙 <b>GitHub:</b> <a href="https://github.com/phuocnhat1011" target="_blank">github.com/phuocnhat1011</a></p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("##### Tải Hồ Sơ Năng Lực (CV)")
        cv_path = Path("assets/CV.pdf")
        if cv_path.exists():
            try:
                with open(cv_path, "rb") as f:
                    st.download_button("📥 Tải bản CV đầy đủ (PDF)", data=f, file_name="Vo-Phuoc-Nhat-CV.pdf", use_container_width=True)
            except Exception as e:
                st.info("💡 Đã tìm thấy CV.pdf nhưng có lỗi khi đọc file. Vui lòng kiểm tra lại quyền truy cập.")
        else:
            st.info("💡 Tip: đặt file `assets/CV.pdf` để bật nút download.")
            
    with col_right:
        st.markdown("<h3 style='border-bottom: 2px solid #E2E8F0; padding-bottom: 8px; font-size:1.3rem;'>🛠️ Bản Đồ Kỹ Năng (Skills)</h3>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("##### 📊 Data Analytics & Visualization")
            st.markdown(
                "<span class='badge'>Power BI</span>"
                "<span class='badge'>DAX</span>"
                "<span class='badge'>Power Query</span>"
                "<span class='badge'>Data Modeling</span>"
                "<span class='badge'>Dashboard UX/UI</span>",
                unsafe_allow_html=True
            )
            
        with st.container(border=True):
            st.markdown("##### 💻 Programming & Automation")
            st.markdown(
                "<span class='badge'>Python</span>"
                "<span class='badge'>SQL</span>"
                "<span class='badge'>R</span>"
                "<span class='badge'>Pandas / NumPy</span>"
                "<span class='badge'>LangChain (RAG)</span>"
                "<span class='badge'>Git / GitHub</span>",
                unsafe_allow_html=True
            )
            
        with st.container(border=True):
            st.markdown("##### 🏦 Finance & Domain Knowledge")
            st.markdown(
                "<span class='badge'>Financial Statements Analysis</span>"
                "<span class='badge'>Banking Metrics (NIM, NPL, CAR)</span>"
                "<span class='badge'>Securities Portfolios (FVTPL, AFS, HTM)</span>",
                unsafe_allow_html=True
            )
            
        with st.container(border=True):
            st.markdown("##### 📦 Platforms & Databases")
            st.markdown(
                "<span class='badge'>PostgreSQL</span>"
                "<span class='badge'>Snowflake</span>"
                "<span class='badge'>Excel (Advanced)</span>"
                "<span class='badge'>Docker</span>",
                unsafe_allow_html=True
            )


# ---------------------------------------------------------
# 3. MODERN MULTIPAGE SYSTEM CONFIGURATION
# ---------------------------------------------------------

# Declare Pages mapped to respective render functions
home_page = st.Page(render_home, title="Trang chủ", icon="🏠", default=True, url_path="home")
bank_page = st.Page(render_bank, title="BCTC Ngân Hàng", icon="🏦", url_path="bank")
securities_page = st.Page(render_securities, title="BCTC Chứng Khoán", icon="📊", url_path="securities")
knowledge_page = st.Page(render_knowledge, title="Góc Chia Sẻ", icon="🧠", url_path="knowledge")
contact_page = st.Page(render_contact, title="Giới thiệu & Liên hệ", icon="👤", url_path="contact")

# Setup Navigation Menu in st.sidebar
pg = st.navigation([home_page, bank_page, securities_page, contact_page])
pg.run()
