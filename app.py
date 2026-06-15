import json
import base64
import html as _html
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
from shared import apply_style, cover_block, render_svg

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


def get_projects_data():
    try:
        with open("data/projects.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

@st.cache_data
def get_avatar_b64():
    try:
        avatar_bytes = Path("assets/avatar.jpg").read_bytes()
        return base64.b64encode(avatar_bytes).decode("utf-8")
    except Exception:
        return ""


# ---------------------------------------------------------
# 2. TAB RENDER FUNCTIONS
# ---------------------------------------------------------

def render_home():
    # Load projects data from cache
    projects = get_projects_data()
    # Filter out BCTC Banking project (bank_bctc) as requested
    projects = [p for p in projects if p.get("id") != "bank_bctc"]
    
    # Load avatar base64 string from cache
    avatar_b64 = get_avatar_b64()
        
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
              <p class="muted" style="font-size:1.02rem; margin-top:14px; line-height: 1.6;">
                Phát triển giải pháp dữ liệu và báo cáo tự động cho lĩnh vực <b>Tài chính & Chứng khoán</b>. 
                Tập trung vào <b>Financial Data Engineering</b>, <b>Algo Trading</b> và tự động hóa pipeline dữ liệu cho thị trường chứng khoán Việt Nam.
              </p>
              <div style="margin-top:16px;">
                <span class="badge">Data Analytics</span>
                <span class="badge">Financial Analysis</span>
                <span class="badge">Automation Pipeline</span>
                <span class="badge">R & Python</span>
                <span class="badge">Power BI & DAX</span>
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
                <p style="font-size: 0.95rem; line-height: 1.65; margin: 0; color: #475569; font-style: italic;">
                "Xuất phát từ nền tảng tài chính, tôi chuyển hướng sang kỹ thuật dữ liệu vì nhận ra rằng dữ liệu tốt mới tạo ra quyết định tốt. Tôi thích giải quyết những bài toán thực tế — lấy dữ liệu lộn xộn, làm sạch, mô hình hóa và biến nó thành thứ người dùng có thể đọc và hiểu ngay."
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
                        <div style="font-size: 1.5rem; margin-bottom: 1px;">📊</div>
                        <div class="kpi-title">Data & BI Solutions</div>
                    </div>
                    <div class="muted" style="font-size: 0.78rem; margin-top: 6px; line-height: 1.35;">Dashboard BCTC & danh mục tự doanh trực quan.</div>
                </div>
                <div class="kpi" style="flex: 1; display: flex; flex-direction: column; justify-content: space-between; padding: 16px 14px;">
                    <div>
                        <div style="font-size: 1.5rem; margin-bottom: 1px;">🧠</div>
                        <div class="kpi-title">Data Modeling</div>
                    </div>
                    <div class="muted" style="font-size: 0.78rem; margin-top: 6px; line-height: 1.35;">Star Schema & DAX measures cho chỉ số tài chính.</div>
                </div>
                <div class="kpi" style="flex: 1; display: flex; flex-direction: column; justify-content: space-between; padding: 16px 14px;">
                    <div>
                        <div style="font-size: 1.5rem; margin-bottom: 1px;">⚙️</div>
                        <div class="kpi-title">Automation & Pipeline</div>
                    </div>
                    <div class="muted" style="font-size: 0.78rem; margin-top: 6px; line-height: 1.35;">ETL tự động: SSI/PDF → PostgreSQL → Power BI.</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
    st.markdown("<hr/>", unsafe_allow_html=True)
    
    # Flagship Projects section
    st.markdown("<div class='section-title'>Dự án Tiêu Biểu</div>", unsafe_allow_html=True)
    st.markdown(
        "<p class='muted' style='margin-bottom:20px;'>Các dự án phân tích dữ liệu tài chính — bấm vào 'Chi tiết dự án'.</p>",
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
        return ""

    # Grid layout for active projects
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
                    if st.button("Chi tiết dự án", type="primary", use_container_width=True, key=f"cta_{pid}"):
                        st.session_state.current_page = "📊 BCTC Chứng Khoán VN"
                        st.rerun()
                elif pid == "bank_bctc":
                    st.button("📊 Tạm ẩn", type="secondary", disabled=True, use_container_width=True, key=f"cta_{pid}")
                elif pid == "hedging_vn30f1m":
                    if st.button("Chi tiết dự án", type="primary", use_container_width=True, key=f"cta_{pid}"):
                        st.session_state.current_page = "📈 Hedging VN30F1M"
                        st.rerun()
                else:
                    st.button("🔧 Hệ thống Backend (Không demo)", type="secondary", disabled=True, use_container_width=True, key=f"cta_{pid}")
                



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
    
    # 4 Sub-tabs navigation using sac.tabs for lazy loading
    active_tab = sac.tabs([
        sac.TabsItem(label="Tổng quan", icon="info-circle"),
        sac.TabsItem(label="Quy trình", icon="diagram-3"),
        sac.TabsItem(label="Source Code & Data Model", icon="code-slash"),
        sac.TabsItem(label="Power BI", icon="bar-chart-line")
    ], align="start", size="sm", key="bank_tab_selector")
    
    if active_tab == "Tổng quan":
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
            
    elif active_tab == "Quy trình":
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
            
    elif active_tab == "Source Code & Data Model":
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
        
    elif active_tab == "Power BI":
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        
        # Read bank powerbi_url from projects.json dynamically
        bank_url = ""
        try:
            projs = get_projects_data()
            bank_url = next((p["powerbi_url"] for p in projs if p["id"] == "bank_bctc"), "")
        except Exception:
            bank_url = ""
            
        if not bank_url or "PASTE_YOUR" in bank_url:
            st.warning("⚠️ Bạn chưa cấu hình đường dẫn Power BI thực tế cho dự án Ngân Hàng. Vui lòng cập nhật `powerbi_url` của dự án 'bank_bctc' trong file `data/projects.json`.")
        else:
            st.markdown(
                f"""
                <div class="shimmer-loader" style="width:100%; height:820px; margin-top: 10px; position:relative; border-radius:16px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
                    <div class="spinner-pbi"></div>
                    <iframe 
                        src="{bank_url}" 
                        style="position:absolute; top:0; left:0; width:100%; height:100%; border:1px solid rgba(226, 232, 240, 0.8); border-radius:16px; background:transparent;"
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
    
    # 4 Sub-tabs navigation using sac.tabs for lazy loading
    active_tab = sac.tabs([
        sac.TabsItem(label="Tổng quan", icon="info-circle"),
        sac.TabsItem(label="Quy trình", icon="diagram-3"),
        sac.TabsItem(label="Source Code & Data Model", icon="code-slash"),
        sac.TabsItem(label="Power BI", icon="bar-chart-line")
    ], align="start", size="sm", key="securities_tab_selector")
    
    if active_tab == "Tổng quan":
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                <div class="card" style="height: 100%; min-height: 320px;">
                    <h3 style="margin-top: 0; color: #5B21B6; font-size:1.3rem;">🎯 Bối cảnh &amp; Nhiệm vụ (Situation &amp; Task)</h3>
                    <p><b>Bối cảnh:</b> Danh mục tự doanh (FVTPL, AFS) là "trái tim" trong hiệu quả hoạt động của các công ty chứng khoán, nhưng dữ liệu này hiện rất khó tiếp cận khi nằm rải rác trong hàng trăm trang thuyết minh BCTC dưới dạng PDF. Nhà đầu tư và chuyên viên phân tích thường mất hàng giờ để tổng hợp thủ công mà vẫn thiếu tính đồng nhất để so sánh giữa các công ty.</p>
                    <p><b>Nhiệm vụ:</b> Xây dựng một Hệ thống chuyên sâu về Phân tích danh mục tự doanh, tự động hóa việc bóc tách dữ liệu từ 3 báo cáo tài chính cốt lõi (CĐKT, KQKD, LCTT) và đặc biệt là chi tiết danh mục FVTPL/AFS của <b>37+ công ty chứng khoán</b> niêm yết trên thị trường Việt Nam.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                """
                <div class="card" style="height: 100%; min-height: 320px;">
                    <h3 style="margin-top: 0; color: #2563EB; font-size:1.3rem;">⚡ Hành động &amp; Kết quả (Action &amp; Result)</h3>
                    <p><b>Hành động:</b>
                        <ul style="padding-left: 1.2rem; margin-top: 6px; margin-bottom: 12px;">
                            <li style="margin-bottom: 6px;"><b>Targeted Extraction:</b> Thiết lập quy trình trích xuất chuyên biệt, tập trung bóc tách các danh mục tài sản tài chính (FVTPL, AFS) từ các bảng thuyết minh PDF vốn là "điểm mù" của dữ liệu truyền thống.</li>
                            <li style="margin-bottom: 6px;"><b>Data Standardization:</b> Hợp nhất dữ liệu từ <b>37+ công ty chứng khoán</b> vào một cấu trúc chung, cho phép so sánh trực tiếp danh mục, tỷ trọng đầu tư và biến động tài sản giữa các đơn vị.</li>
                            <li style="margin-bottom: 6px;"><b>Modeling &amp; Metrics:</b> Thiết kế mô hình dữ liệu quan hệ (Star Schema) để tự động hóa các chỉ số tài chính trọng yếu (NIM, ROA, ROE) kết hợp với cấu trúc danh mục đầu tư.</li>
                            <li style="margin-bottom: 6px;"><b>Visual Insights:</b> Xây dựng Dashboard Power BI theo phương pháp Menu-driven Design, cho phép người dùng chỉ cần một cú click chuột để "X-ray" toàn bộ danh mục tự doanh của bất kỳ công ty chứng khoán nào.</li>
                        </ul>
                    </p>
                    <p><b>Kết quả (Value Delivered):</b>
                        <ul style="padding-left: 1.2rem; margin-top: 6px;">
                            <li style="margin-bottom: 4px;"><b>Tiết kiệm thời gian:</b> Chuyển đổi công việc tra cứu thủ công kéo dài hàng giờ thành báo cáo chỉ trong <b>vài giây</b>.</li>
                            <li style="margin-bottom: 4px;"><b>Độ bao phủ:</b> Dữ liệu chuẩn hóa của <b>37+ công ty chứng khoán</b> niêm yết, cung cấp cái nhìn toàn cảnh về khẩu vị đầu tư của toàn ngành.</li>
                            <li style="margin-bottom: 4px;"><b>Ra quyết định:</b> Giúp nhà đầu tư nhanh chóng nhận diện các biến động lớn trong danh mục tự doanh, từ đó đưa ra quyết định dựa trên dữ liệu (Data-driven) thay vì cảm tính.</li>
                        </ul>
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    elif active_tab == "Quy trình":
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
            
        # PROJECT WORKFLOW (Long-form layout) section
        st.markdown(
            """
            <style>
              .workflow-container {
                max-width: 100%;
                margin: 20px 0 0 0;
                padding: 0 10px;
              }
              .workflow-section {
                margin-bottom: 32px;
                padding-bottom: 24px;
                border-bottom: 1px dashed rgba(226, 232, 240, 0.8);
              }
              .workflow-section:last-child {
                margin-bottom: 0;
                padding-bottom: 0;
                border-bottom: none;
              }
              .workflow-header {
                display: flex;
                align-items: baseline;
                gap: 16px;
                margin-bottom: 10px;
              }
              .workflow-num {
                font-size: 2.2rem;
                font-weight: 800;
                color: #5B21B6;
                font-family: 'JetBrains Mono', 'Plus Jakarta Sans', monospace;
                line-height: 1;
                opacity: 0.9;
              }
              .workflow-title {
                font-size: 1.4rem;
                font-weight: 700;
                color: #0F172A;
                margin: 0;
              }
              .workflow-desc {
                font-size: 1.05rem;
                line-height: 1.8;
                color: #334155;
                margin-bottom: 12px;
                text-align: justify;
              }
              .workflow-callout {
                background: rgba(91, 33, 182, 0.03);
                border-left: 5px solid #5B21B6;
                border-radius: 8px;
                padding: 12px 18px;
                font-size: 0.95rem;
                color: #334155;
                line-height: 1.6;
                margin-top: 10px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.01);
              }
              .workflow-callout-header {
                font-weight: 700;
                color: #1E1B4B;
                margin-bottom: 4px;
              }
            </style>
            
            <hr style="border:none; border-top:1px solid rgba(226,232,240,0.8); margin: 32px 0;"/>
            <h3 style="margin-top:0; font-size:1.6rem; color:#0F172A; margin-bottom: 28px; letter-spacing: -0.02em;">🔄 PROJECT WORKFLOW</h3>
            
            <div class="workflow-container">
              
              <!-- STEP 1 -->
              <div class="workflow-section">
                <div class="workflow-header">
                  <span class="workflow-num">01</span>
                  <h4 class="workflow-title">Data Ingestion — Thu thập dữ liệu tự động</h4>
                </div>
                <p class="workflow-desc">
                  Hệ thống tự động hóa việc truy xuất dữ liệu từ SSI iBoard cho toàn bộ các mã cổ phiếu ngành chứng khoán. Quy trình thực hiện quét dữ liệu theo từng kỳ báo cáo (năm, quý, 6 tháng, 9 tháng), tự động tải các bảng CĐKT, KQKD, LCTT về máy và phân loại vào cấu trúc thư mục logic. Điều này giúp loại bỏ hoàn toàn các thao tác thủ công và đảm bảo tính nhất quán của dữ liệu đầu vào.
                </p>
                <div class="workflow-callout">
                  <div class="workflow-callout-header">🛠️ <b>Công cụ sử dụng:</b></div>
                  <div style="margin-top: 6px;">
                    Python, Selenium, Requests, OS,..
                  </div>
                </div>
              </div>
              
              <!-- STEP 2 -->
              <div class="workflow-section">
                <div class="workflow-header">
                  <span class="workflow-num">02</span>
                  <h4 class="workflow-title">Transformation &amp; Modeling — Xử lý &amp; Mô hình hóa dữ liệu tài chính</h4>
                </div>
                <p class="workflow-desc">
                  Dữ liệu báo cáo tài chính thô thường không đồng nhất do sự khác biệt trong cách ghi nhận của các doanh nghiệp hoặc do thay đổi thông tư kế toán qua các năm. Bước này đóng vai trò làm sạch và tổ chức lại toàn bộ dữ liệu thành một hệ thống chuẩn chỉnh.<br/><br/>
                  <b>Các bước xử lý chính:</b><br/>
                  • <b>Data Cleaning:</b> Gộp hàng loạt file Excel rời rạc thành bảng thống nhất. Xử lý triệt để các thay đổi về chỉ tiêu kế toán (ví dụ: gộp các khoản mục bị đổi tên qua các năm) để đảm bảo chuỗi dữ liệu tài chính xuyên suốt, không bị đứt gãy.<br/>
                  • <b>Unpivot:</b> Chuyển đổi cấu trúc dữ liệu từ dạng báo cáo ngang truyền thống sang định dạng dọc chuẩn, phục vụ trực tiếp cho việc vẽ biểu đồ và phân tích đa chiều.<br/>
                  • <b>Data Modeling:</b> Xây dựng mô hình dữ liệu Star Schema. Phân tách dữ liệu thành các bảng Danh mục (Công ty, Thời gian) và bảng Số liệu sự kiện (CĐKT, KQKD), giúp loại bỏ dữ liệu thừa và tối ưu hóa tốc độ tính toán cho các báo cáo sau này.
                </p>
                <div class="workflow-callout">
                  <div class="workflow-callout-header">🧠 <b>Công cụ sử dụng:</b></div>
                  <div style="margin-top: 6px;">
                    Python, thư viện Pandas.
                  </div>
                </div>
              </div>
              
              <!-- STEP 3 -->
              <div class="workflow-section">
                <div class="workflow-header">
                  <span class="workflow-num">03</span>
                  <h4 class="workflow-title">Data Extraction &amp; Quality Assurance — Trích xuất &amp; Kiểm tra dữ liệu</h4>
                </div>
                <p class="workflow-desc">
                  <b>Quy trình:</b> Lọc và xử lý dữ liệu từ Báo cáo tài chính để đảm bảo số liệu về danh mục đầu tư (FVTPL, AFS) luôn chính xác trước khi sử dụng cho báo cáo.<br/><br/>
                  <b>Quy trình thực hiện:</b><br/>
                  • <b>Thu thập:</b> Tự động tải BCTC theo năm và quý của các công ty chứng khoán niêm yết.<br/>
                  • <b>Trích xuất:</b> Dùng Python (OCR) để đọc dữ liệu từ báo cáo.<br/>
                  • <b>Kiểm tra:</b> Tôi chạy một đoạn script nhỏ để cộng lại các khoản mục, nếu tổng không khớp với số tổng trên báo cáo, hệ thống sẽ đánh dấu các công ty đó. Với những công ty bị đánh dấu lỗi, tôi sử dụng NotebookLM hoặc ChatGPT để hỗ trợ trích xuất lại thủ công, đảm bảo không bỏ sót số liệu.<br/>
                  • <b>Kết quả:</b> Có được tập dữ liệu sạch, đảm bảo tính khớp đúng để phục vụ phân tích.
                </p>
                <div class="workflow-callout">
                  <div class="workflow-callout-header">⚙️ <b>Công cụ sử dụng:</b></div>
                  <div style="margin-top: 6px;">
                    Python, Pandas, NotebookLM, ChatGPT.
                  </div>
                </div>
              </div>

              <!-- STEP 4 -->
              <div class="workflow-section">
                <div class="workflow-header">
                  <span class="workflow-num">04</span>
                  <h4 class="workflow-title">Data Storage &amp; Management — Lưu trữ &amp; Quản trị dữ liệu</h4>
                </div>
                <p class="workflow-desc">
                  Thay vì quản lý bằng các file rời rạc và load thủ công, toàn bộ dữ liệu sau khi được làm sạch bằng Python sẽ được đẩy vào PostgreSQL. Việc chuyển đổi từ lưu trữ tệp sang Database giúp quản lý tập trung toàn bộ khối lượng dữ liệu tài chính, tạo nền tảng ổn định cho báo cáo.<br/><br/>
                  <b>Quản trị &amp; Triển khai:</b><br/>
                  • <b>Lưu trữ tập trung:</b> Nạp dữ liệu vào PostgreSQL, tổ chức phân lớp rõ ràng theo mô hình Star Schema (gồm các bảng Fact và Dimension) đã thiết kế ở bước trước.<br/>
                  • <b>Đảm bảo tính toàn vẹn:</b> Thiết lập các ràng buộc dữ liệu cơ bản (Khóa chính - Primary Key, Khóa ngoại - Foreign Key) để đảm bảo không bị mâu thuẫn số liệu giữa các bảng.
                </p>
                <div class="workflow-callout">
                  <div class="workflow-callout-header">🗄️ <b>Công cụ sử dụng:</b></div>
                  <div style="margin-top: 6px;">
                    PostgreSQL, SQL, Python.
                  </div>
                </div>
              </div>
              
              <!-- STEP 5 -->
              <div class="workflow-section">
                <div class="workflow-header">
                  <span class="workflow-num">05</span>
                  <h4 class="workflow-title">Visualization Power BI — Trực quan hóa dữ liệu</h4>
                </div>
                <p class="workflow-desc">
                  Ở bước cuối cùng, Power BI được kết nối trực tiếp vào Database PostgreSQL để kéo dữ liệu sạch lên và xây dựng các báo cáo tương tác.<br/><br/>
                  • <b>Giao diện đa nhiệm:</b> Tích hợp đầy đủ 3 bảng báo cáo (CĐKT, KQKD, LCTT) giúp người dùng dễ dàng chuyển đổi góc nhìn.<br/>
                  • <b>Tương tác linh hoạt:</b> Sử dụng tính năng Drill-down (xem chi tiết đa cấp độ) và các bộ lọc (Slicer) động theo mã công ty, kỳ báo cáo giúp việc truy xuất số liệu trở nên trực quan và nhanh chóng.
                </p>
                <div class="workflow-callout">
                  <div class="workflow-callout-header">📊 <b>Công cụ sử dụng:</b></div>
                  <div style="margin-top: 6px;">
                    Power BI Desktop &amp; Service, DAX.
                  </div>
                </div>
              </div>
              
            </div>
            """,
            unsafe_allow_html=True
        )
            
    elif active_tab == "Source Code & Data Model":
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        st.markdown("### 💻 Source Code & Data Model")
        
        # Phần 1: Repository Navigation
        st.markdown(
            "Toàn bộ mã nguồn, cấu trúc luồng xử lý dữ liệu (ETL) và kịch bản tự động hóa của dự án "
            "được quản lý tập trung và phân module chi tiết trên GitHub."
        )
        st.link_button("💻 Xem chi tiết Repository trên GitHub", "#", use_container_width=False)
        
        # Phân cách
        st.divider()
        
        # Phần 2: Data Model
        st.markdown("### 🏗️ Kiến trúc Dữ liệu (Star Schema)")
        
        # Option 1: Dùng st.image() để hiển thị sơ đồ (ERD_PostgreSQL.png)
        img_path = Path("assets/previews/ERD_PostgreSQL.png")
        if img_path.exists():
            st.image(str(img_path), caption="Sơ đồ cơ sở dữ liệu quan hệ (Star Schema)", use_container_width=True)
        else:
            st.info("💡 Lưu ý: Hãy đặt sơ đồ cơ sở dữ liệu tại `assets/previews/ERD_PostgreSQL.png` để hiển thị.")
            
        # Option 2: Dùng st.components.v1.html để nhúng mã Iframe từ dbdiagram.io (Mặc định được ẩn, hãy bỏ comment để sử dụng)
        # dbdiagram_iframe = '<iframe src="https://dbdiagram.io/embed/YOUR_EMBED_ID" width="100%" height="600" frameborder="0"></iframe>'
        # components.html(dbdiagram_iframe, height=600)
        
    elif active_tab == "Power BI":
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        POWER_BI_URL = "https://app.powerbi.com/view?r=eyJrIjoiNTAxZjNhMDAtOTY2ZS00YWJiLTljOTktM2VjMzhjNDMxN2Y3IiwidCI6IjI4ZmZjMDE1LWFlOWEtNDEzNC1hOGQ2LWU3MTI4MTEzMDc2OSIsImMiOjEwfQ%3D%3D"
        st.markdown(
            f"""
            <div class="shimmer-loader" style="width:100%; height:820px; margin-top: 10px; position:relative; border-radius:16px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
                <div class="spinner-pbi"></div>
                <iframe 
                    src="{POWER_BI_URL}" 
                    style="position:absolute; top:0; left:0; width:100%; height:100%; border:1px solid rgba(226, 232, 240, 0.8); border-radius:16px; background:transparent;"
                    allowfullscreen="true">
                </iframe>
            </div>
            """,
            unsafe_allow_html=True
        )


def render_hedging():
    # Page specific CSS styles
    st.markdown(
        """
        <style>
          .title-badge {
            background: #EEEDFE; color: #534AB7;
            font-size: 11px; font-weight: 500; padding: 3px 10px;
            border-radius: 20px; border: 1px solid #AFA9EC;
            letter-spacing: .3px; text-transform: uppercase;
            display: inline-block;
            vertical-align: middle;
            margin-left: 10px;
          }
          .tech-tags { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 20px; }
          .tech-tag {
            background: #EFEFED; color: #5F5E5A; font-size: 12px;
            font-weight: 500; padding: 5px 12px; border-radius: 20px; font-family: 'JetBrains Mono', monospace;
          }
          .tech-tag.purple { background: #EEEDFE; color: #534AB7; }
          .tech-tag.teal { background: #E1F5EE; color: #0F6E56; }

          /* Pipeline Step */
          .pipeline-step {
            background: #FFFFFF; border: 1px solid #E2E1DC;
            border-radius: 12px; padding: 18px 16px; position: relative;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
            height: 100%;
          }
          .step-num {
            font-size: 10px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase;
            color: #6C63D5; margin-bottom: 6px; font-family: 'JetBrains Mono', monospace;
          }
          .step-title { font-size: 13px; font-weight: 600; color: #1A1A19; margin-bottom: 8px; }
          .step-items { list-style: none; padding: 0; }
          .step-items li {
            font-size: 12px; color: #5F5E5A; padding: 3px 0;
            border-bottom: 1px solid #EFEFED; line-height: 1.5;
          }
          .step-items li:last-child { border-bottom: none; }
          .step-items li::before { content: '•  '; color: #6C63D5; margin-right: 4px; }

          /* State Machine */
          .sm-node {
            border-radius: 10px; padding: 12px 16px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
          }
          .sm-node.purple { background: #EEEDFE; border: 1.5px solid #AFA9EC; }
          .sm-node.teal { background: #E1F5EE; border: 1.5px solid #9FE1CB; }
          .sm-node-label { font-size: 13px; font-weight: 600; color: #3C3489; }
          .sm-node.teal .sm-node-label { color: #0F6E56; }
          .sm-node-sub { font-size: 11px; color: #534AB7; margin-top: 3px; }
          .sm-node.teal .sm-node-sub { color: #1D9E75; }

          .sm-arrow {
            display: flex; align-items: center; gap: 8px; padding: 6px 0;
          }
          .sm-arrow-line { flex: 1; height: 1px; background: #E2E1DC; }
          .sm-arrow-cond {
            font-size: 11px; color: #888780; background: #F7F7F6;
            padding: 3px 10px; border-radius: 20px; border: 1px solid #E2E1DC;
            white-space: nowrap;
          }

          /* Email preview */
          .email-preview {
            background: #FFFFFF; border: 1px solid #E2E1DC; border-radius: 14px; overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
          }
          .email-header {
            background: #2D2B55; padding: 14px 18px;
          }
          .email-subject { font-size: 13px; font-weight: 600; color: #fff; margin-bottom: 4px; }
          .email-meta { font-size: 11px; color: rgba(255,255,255,.55); }
          .email-body { padding: 18px; }
          .email-row { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #EFEFED; font-size: 13px; }
          .email-row:last-child { border-bottom: none; }
          .email-row .lbl { color: #888780; }
          .email-row .val { font-weight: 500; color: #1A1A19; }
          .val.red { color: #D85A30; }
          .val.green { color: #1D9E75; }
          .val.purple { color: #6C63D5; }

          .email-footer {
            margin: 12px 18px 18px; background: #EEEDFE; border-radius: 8px;
            padding: 10px 14px; font-size: 12px; color: #3C3489; line-height: 1.6;
          }
          .email-footer strong { font-weight: 600; }

          /* Table styling */
          .bt-table-wrap { overflow-x: auto; border-radius: 12px; border: 1px solid #E2E1DC; }
          table.bt-table { width: 100%; border-collapse: collapse; font-size: 13px; }
          table.bt-table thead th {
              background: #F7F7F6; padding: 10px 14px; text-align: left;
              font-size: 11px; font-weight: 600; letter-spacing: .5px; text-transform: uppercase;
              color: #888780; border-bottom: 1px solid #E2E1DC;
          }
          table.bt-table tbody td { padding: 10px 14px; border-bottom: 1px solid #EFEFED; color: #5F5E5A; }
          table.bt-table tbody tr:last-child td { border-bottom: none; }
          table.bt-table tbody tr:hover td { background: #F7F7F6; }

          .pill {
              display: inline-block; padding: 2px 10px; border-radius: 20px; font-size: 11px; font-weight: 600;
          }
          .pill.best { background: #E1F5EE; color: #0F6E56; }
          .pill.mid { background: #EEEDFE; color: #3C3489; }
          .pill.low { background: #FAECE7; color: #993C1D; }
          
          /* Streamlit tabs override for this page */
          .stTabs [data-baseweb="tab-list"] {
              gap: 8px;
          }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.header("📉 VN30F1M Intraday Hedging System")
    st.markdown(
        """
        <p class='muted' style='font-size: 1.05rem; margin-bottom: 24px;'>
        Hệ thống giao dịch phái sinh tự động hóa toàn diện cho hợp đồng tương lai VN30F1M — từ ETL dữ liệu OHLCV intraday, 
        phát hiện tín hiệu short dựa trên MA spread ratio &amp; streak count, đến backtest walk-forward và gửi cảnh báo email theo state machine thời gian thực.
        </p>
        """,
        unsafe_allow_html=True
    )

    active_tab = sac.tabs([
        sac.TabsItem(label="Tổng quan", icon="info-circle"),
        sac.TabsItem(label="Quy trình", icon="diagram-3"),
        sac.TabsItem(label="Source code", icon="code-slash"),
        sac.TabsItem(label="Backtest", icon="play-circle"),
        sac.TabsItem(label="Alert Email", icon="envelope-at")
    ], align="start", size="sm", key="hedging_tab_selector")
    
    if active_tab == "Tổng quan":
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                <div class="card" style="height: 100%; min-height: 250px;">
                    <h3 style="margin-top: 0; color: #5B21B6; font-size:1.3rem;">🎯 Bối cảnh &amp; Nhiệm vụ</h3>
                    <p><b>Situation:</b> Thị trường Phái sinh VN30F1M đòi hỏi khả năng phản ứng tức thì với biến động giá trong phiên (9:00–14:30). Việc theo dõi màn hình thủ công liên tục không khả thi và dễ dẫn đến sai sót tâm lý.</p>
                    <p><b>Task:</b> Xây dựng End-to-end Automated Trading Pipeline với các mục tiêu:
                        <ul>
                            <li><b>Tự động hóa toàn trình:</b> Xây dựng luồng dữ liệu (pipeline) thu thập OHLCV, tính toán tín hiệu (Entry/Stoploss/Take Profit) dựa trên bộ quy tắc cá nhân.</li>
                            <li><b>Kiểm định &amp; Tối ưu:</b> Thực hiện Backtest và tối ưu tham số để đánh giá hiệu quả chiến lược.</li>
                            <li><b>Thực thi:</b> Phát cảnh báo qua email và tích hợp SSI FastConnect API để tự động hóa việc đặt lệnh theo thời gian thực.</li>
                        </ul>
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                """
                <div class="card" style="height: 100%; min-height: 250px;">
                    <h3 style="margin-top: 0; color: #2563EB; font-size:1.3rem;">⚡ Hành động &amp; Kết quả</h3>
                    <ul>
                        <li><b>Data Handling:</b> Tự động lấy dữ liệu OHLCV 1-phút từ các nguồn (SSI, DNSE) và chuẩn hóa dữ liệu bằng R để thuận tiện cho việc xử lý.</li>
                        <li><b>Entry/Exit Logic:</b> Xây dựng các hàm (functions) tính toán chỉ báo và tín hiệu dựa trên các quy tắc cá nhân (như MA, spread, streak spread).</li>
                        <li><b>Visualization:</b> Sử dụng biểu đồ nến (Candlestick chart) có tích hợp tín hiệu để theo dõi trạng thái chiến lược trực tiếp trong phiên.</li>
                        <li><b>Testing &amp; Tuning:</b> Kiểm tra chiến lược bằng cách thử nghiệm nhiều mức tham số khác nhau (Grid Search) và chạy thử cuốn chiếu trên dữ liệu quá khứ (Walk-forward) để tìm bộ thông số ổn định nhất.</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
        
        st.markdown(
            """
            <div class="card">
                <h3 style="margin-top: 0; color: #0F172A; font-size:1.3rem; margin-bottom:16px;">Tính năng cốt lõi</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px;">
                    <div style="border: 1px solid rgba(226,232,240,0.8); border-radius: 12px; padding: 16px; background: rgba(255,255,255,0.5);">
                        <div style="font-size: 20px; margin-bottom: 8px;">📡</div>
                        <div style="font-size: 13px; font-weight: 600; color: #0F172A; margin-bottom: 6px;">ETL Intraday</div>
                        <div style="font-size: 12px; color: #475569; line-height: 1.6;">Tự động lấy OHLCV từ SSI API, chuẩn hóa theo khung thời gian 1-min / 5-min, lưu trữ RDS.</div>
                    </div>
                    <div style="border: 1px solid rgba(226,232,240,0.8); border-radius: 12px; padding: 16px; background: rgba(255,255,255,0.5);">
                        <div style="font-size: 20px; margin-bottom: 8px;">🧮</div>
                        <div style="font-size: 13px; font-weight: 600; color: #0F172A; margin-bottom: 6px;">Signal Engine</div>
                        <div style="font-size: 12px; color: #475569; line-height: 1.6;">MA spread ratio, negative streak, had_positive_today flag, Signal5 confirmation, hedge nhánh early entry.</div>
                    </div>
                    <div style="border: 1px solid rgba(226,232,240,0.8); border-radius: 12px; padding: 16px; background: rgba(255,255,255,0.5);">
                        <div style="font-size: 20px; margin-bottom: 8px;">📊</div>
                        <div style="font-size: 13px; font-weight: 600; color: #0F172A; margin-bottom: 6px;">Backtest Engine</div>
                        <div style="font-size: 12px; color: #475569; line-height: 1.6;">Grid search tham số, walk-forward validation, candlestick chart tích hợp trade annotation.</div>
                    </div>
                    <div style="border: 1px solid rgba(226,232,240,0.8); border-radius: 12px; padding: 16px; background: rgba(255,255,255,0.5);">
                        <div style="font-size: 20px; margin-bottom: 8px;">📧</div>
                        <div style="font-size: 13px; font-weight: 600; color: #0F172A; margin-bottom: 6px;">Alert Email</div>
                        <div style="font-size: 12px; color: #475569; line-height: 1.6;">State machine persist qua file, 3 loại email: SHORT signal, EXIT signal, Daily summary.</div>
                    </div>
                    <div style="border: 1px solid rgba(226,232,240,0.8); border-radius: 12px; padding: 16px; background: rgba(255,255,255,0.5);">
                        <div style="font-size: 20px; margin-bottom: 8px;">🔁</div>
                        <div style="font-size: 13px; font-weight: 600; color: #0F172A; margin-bottom: 6px;">Auto Refresh</div>
                        <div style="font-size: 12px; color: #475569; line-height: 1.6;">HTML chart tự động refresh mỗi 5 phút trong phiên, xuất báo cáo cuối ngày.</div>
                    </div>
                    <div style="border: 1px solid rgba(226,232,240,0.8); border-radius: 12px; padding: 16px; background: rgba(255,255,255,0.5);">
                        <div style="font-size: 20px; margin-bottom: 8px;">🎯</div>
                        <div style="font-size: 13px; font-weight: 600; color: #0F172A; margin-bottom: 6px;">TP Tiers</div>
                        <div style="font-size: 12px; color: #475569; line-height: 1.6;">Take-profit nhiều mức, streak-based exit, stop-loss tự động. Logic exit tích hợp trong <code>get_trade_log</code>.</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown(
            """
            <div class="tech-tags">
                <span class="tech-tag purple">Data Processing</span>
                <span class="tech-tag purple">Automated Scripting</span>
                <span class="tech-tag purple">Interactive Charts</span>
                <span class="tech-tag teal">SSI FastConnect</span>
                <span class="tech-tag teal">VN30F1M Futures</span>
                <span class="tech-tag">Entry/Exit Logic</span>
                <span class="tech-tag">Backtesting</span>
                <span class="tech-tag">Walk-forward</span>
                <span class="tech-tag">Grid Search</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif active_tab == "Quy trình":
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        st.markdown("### 🔄 Quy trình ETL &amp; Kiến trúc Dữ liệu")
        
        cols_step = st.columns(4)
        with cols_step[0]:
            st.markdown(
                """
                <div class="pipeline-step">
                    <div class="step-num">01 / Extract</div>
                    <div class="step-title">Data Ingestion</div>
                    <ul class="step-items">
                        <li>Kết nối SSI FastConnect API và DNSE API</li>
                        <li>Thu thập dữ liệu OHLCV theo khung 1 phút (intraday)</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
        with cols_step[1]:
            st.markdown(
                """
                <div class="pipeline-step">
                    <div class="step-num">02 / Transform</div>
                    <div class="step-title">Signal Processing</div>
                    <ul class="step-items">
                        <li>Chuẩn hóa dữ liệu OHLCV, xử lý timestamp</li>
                        <li>Tính MA ngắn/dài hạn và spread ratio</li>
                        <li>Xây dựng các điều kiện tín hiệu vào/ra lệnh</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
        with cols_step[2]:
            st.markdown(
                """
                <div class="pipeline-step">
                    <div class="step-num">03 / Validate</div>
                    <div class="step-title">Backtest &amp; Optimization</div>
                    <ul class="step-items">
                        <li>Mô phỏng chiến lược trên dữ liệu lịch sử (1 trade/ngày)</li>
                        <li>Cơ chế thoát lệnh: TP cố định + streak exit 2 tầng</li>
                        <li>Grid search ~300+ tổ hợp tham số (spread, streak, nb_except)</li>
                        <li>Đánh giá theo win rate, avg P&amp;L, total P&amp;L</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
        with cols_step[3]:
            st.markdown(
                """
                <div class="pipeline-step">
                    <div class="step-num">04 / Alert</div>
                    <div class="step-title">Output &amp; Monitoring</div>
                    <ul class="step-items">
                        <li>State machine 2 trạng thái (WAIT_SHORT / WAIT_OUT) — lưu trạng thái ra file .rds theo ngày, chống gửi tín hiệu trùng</li>
                        <li>Gửi email cảnh báo theo thời gian thực (EARLY WARNING &rarr; SHORT &rarr; OUT)</li>
                        <li>Biểu đồ HTML tự động cập nhật</li>
                        <li>Tổng kết P&amp;L hàng ngày</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
        
        col_flow, col_rules = st.columns(2)
        with col_flow:
            st.markdown(
                """
                <div class="card" style="height: 100%;">
                    <h3 style="margin-top: 0; color: #0F172A; font-size:1.15rem; margin-bottom: 16px;">State machine — ALERT_EMAIL_V2</h3>
                    <div class="state-machine-wrap">
                        <div class="sm-node purple">
                            <div class="sm-node-label">WAIT_SHORT</div>
                            <div class="sm-node-sub">Chờ tín hiệu short đủ điều kiện</div>
                        </div>
                        <div class="sm-arrow">
                            <div class="sm-arrow-line"></div>
                            <div class="sm-arrow-cond">spread &lt; threshold &amp; streak &le; -N &amp; Signal5 &check;</div>
                            <div class="sm-arrow-line"></div>
                        </div>
                        <div style="text-align:center; font-size:12px; margin-bottom:6px; color:#475569;">↓ Gửi email SHORT signal</div>
                        <div class="sm-node teal">
                            <div class="sm-node-label">WAIT_OUT</div>
                            <div class="sm-node-sub">Đang giữ lệnh — chờ điều kiện exit</div>
                        </div>
                        <div class="sm-arrow">
                            <div class="sm-arrow-line"></div>
                            <div class="sm-arrow-cond">TP hit / streak đảo chiều / EOD</div>
                            <div class="sm-arrow-line"></div>
                        </div>
                        <div style="text-align:center; font-size:12px; margin-bottom:6px; color:#475569;">↓ Gửi email EXIT signal</div>
                        <div class="sm-node purple">
                            <div class="sm-node-label">WAIT_SHORT</div>
                            <div class="sm-node-sub">Reset — chờ tín hiệu tiếp theo</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        with col_rules:
            st.markdown(
                """
                <div class="card" style="height: 100%;">
                    <h3 style="margin-top: 0; color: #0F172A; font-size:1.15rem; margin-bottom: 16px;">Entry &amp; exit rules</h3>
                    <div style="margin-bottom:16px;">
                        <div style="font-size:13px; font-weight:600; color:#0F6E56; margin-bottom:8px;">✅ Điều kiện SHORT (Entry)</div>
                        <div style="display:flex; flex-direction:column; gap:6px;">
                            <div style="background:#E1F5EE; border-radius:8px; padding:9px 12px; font-size:12px; color:#0F6E56; border-left: 3px solid #1D9E75;">MA spread ratio &lt; ngưỡng âm (từ grid search)</div>
                            <div style="background:#E1F5EE; border-radius:8px; padding:9px 12px; font-size:12px; color:#0F6E56; border-left: 3px solid #1D9E75;">Streak âm liên tiếp &le; -N candle</div>
                            <div style="background:#E1F5EE; border-radius:8px; padding:9px 12px; font-size:12px; color:#0F6E56; border-left: 3px solid #1D9E75;">had_positive_today = FALSE (chưa có candle dương trong ngày)</div>
                            <div style="background:#E1F5EE; border-radius:8px; padding:9px 12px; font-size:12px; color:#0F6E56; border-left: 3px solid #1D9E75;">Signal5 xác nhận (Volume spike + spread cực âm)</div>
                            <div style="background:#EEEDFE; border-radius:8px; padding:9px 12px; font-size:12px; color:#3C3489; border-left: 3px solid #6C63D5;">Hedge nhánh: early entry khi thỏa điều kiện phụ đặc biệt</div>
                        </div>
                    </div>
                    <div>
                        <div style="font-size:13px; font-weight:600; color:#993C1D; margin-bottom:8px;">❌ Điều kiện EXIT</div>
                        <div style="display:flex; flex-direction:column; gap:6px;">
                            <div style="background:#FAECE7; border-radius:8px; padding:9px 12px; font-size:12px; color:#993C1D; border-left: 3px solid #D85A30;">Take-profit tier 1: đạt mốc +X pts</div>
                            <div style="background:#FAECE7; border-radius:8px; padding:9px 12px; font-size:12px; color:#993C1D; border-left: 3px solid #D85A30;">Streak đảo chiều về dương (giá tăng trở lại)</div>
                            <div style="background:#FAECE7; border-radius:8px; padding:9px 12px; font-size:12px; color:#993C1D; border-left: 3px solid #D85A30;">Stop-loss tự động: chạm mốc -Y pts</div>
                            <div style="background:#FAECE7; border-radius:8px; padding:9px 12px; font-size:12px; color:#993C1D; border-left: 3px solid #D85A30;">Hết giờ giao dịch phiên intraday (14:30)</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    elif active_tab == "Source code":
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        st.markdown("### 💻 Source Code & Data Model")
        
        # Phần 1: Repository Navigation
        st.markdown(
            "Toàn bộ mã nguồn, cấu trúc luồng xử lý dữ liệu (ETL) và kịch bản tự động hóa của dự án "
            "được quản lý tập trung và phân module chi tiết trên GitHub."
        )
        st.link_button("💻 Xem chi tiết Repository trên GitHub", "#", use_container_width=False)
        
        # Phân cách
        st.divider()
        
        # Phần 2: Data Model
        st.markdown("### 🏗️ Kiến trúc Dữ liệu (Star Schema)")
        
        # Option 1: Dùng st.image() để hiển thị sơ đồ (ERD_PostgreSQL.png)
        img_path = Path("assets/previews/ERD_PostgreSQL.png")
        if img_path.exists():
            st.image(str(img_path), caption="Sơ đồ cơ sở dữ liệu quan hệ (Star Schema)", use_container_width=True)
        else:
            st.info("💡 Lưu ý: Hãy đặt sơ đồ cơ sở dữ liệu tại `assets/previews/ERD_PostgreSQL.png` để hiển thị.")
        
        st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

    elif active_tab == "Backtest":
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        st.markdown("### 📊 Kết quả Backtest &amp; Tối ưu hóa tham số")
        
        # KPI Row
        col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
        with col_kpi1:
            st.markdown(
                """
                <div class="kpi" style="text-align: center;">
                    <div style="font-size: 11px; color: #888780; margin-bottom: 6px; text-transform: uppercase; letter-spacing: .4px;">Win rate</div>
                    <div style="font-size: 22px; font-weight: 600; color: #1D9E75;">68.4%</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_kpi2:
            st.markdown(
                """
                <div class="kpi" style="text-align: center;">
                    <div style="font-size: 11px; color: #888780; margin-bottom: 6px; text-transform: uppercase; letter-spacing: .4px;">Avg profit / trade</div>
                    <div style="font-size: 22px; font-weight: 600; color: #1A1A19;">+4.2 pts</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_kpi3:
            st.markdown(
                """
                <div class="kpi" style="text-align: center;">
                    <div style="font-size: 11px; color: #888780; margin-bottom: 6px; text-transform: uppercase; letter-spacing: .4px;">Max drawdown</div>
                    <div style="font-size: 22px; font-weight: 600; color: #D85A30;">-12.1 pts</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_kpi4:
            st.markdown(
                """
                <div class="kpi" style="text-align: center;">
                    <div style="font-size: 11px; color: #888780; margin-bottom: 6px; text-transform: uppercase; letter-spacing: .4px;">Tổng trade</div>
                    <div style="font-size: 22px; font-weight: 600; color: #6C63D5;">247</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
        
        st.markdown(
            """
            <div class="card">
                <h3 style="margin-top: 0; color: #0F172A; font-size:1.15rem; margin-bottom: 16px;">Grid search — spread threshold &amp; court streak</h3>
                <div class="bt-table-wrap">
                    <table class="bt-table">
                        <thead>
                            <tr>
                                <th>Spread threshold</th>
                                <th>Min streak</th>
                                <th>Signal5</th>
                                <th>Win rate</th>
                                <th>Avg profit</th>
                                <th>Max DD</th>
                                <th>Tổng trade</th>
                                <th>Đánh giá</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="font-family: 'JetBrains Mono', monospace;">-0.0025</td>
                                <td>-3</td>
                                <td>✓</td>
                                <td style="color:#1D9E75; font-weight:500;">68.4%</td>
                                <td>+4.2 pts</td>
                                <td style="color:#D85A30;">-12.1</td>
                                <td>247</td>
                                <td><span class="pill best">Best</span></td>
                            </tr>
                            <tr>
                                <td style="font-family: 'JetBrains Mono', monospace;">-0.0020</td>
                                <td>-3</td>
                                <td>✓</td>
                                <td>63.1%</td>
                                <td>+3.8 pts</td>
                                <td style="color:#D85A30;">-14.5</td>
                                <td>312</td>
                                <td><span class="pill mid">Tốt</span></td>
                            </tr>
                            <tr>
                                <td style="font-family: 'JetBrains Mono', monospace;">-0.0025</td>
                                <td>-4</td>
                                <td>✓</td>
                                <td>71.2%</td>
                                <td>+3.1 pts</td>
                                <td style="color:#D85A30;">-8.9</td>
                                <td>118</td>
                                <td><span class="pill mid">Tốt</span></td>
                            </tr>
                            <tr>
                                <td style="font-family: 'JetBrains Mono', monospace;">-0.0015</td>
                                <td>-2</td>
                                <td>✗</td>
                                <td>51.8%</td>
                                <td>+1.4 pts</td>
                                <td style="color:#D85A30;">-21.3</td>
                                <td>489</td>
                                <td><span class="pill low">Nhiều noise</span></td>
                            </tr>
                            <tr>
                                <td style="font-family: 'JetBrains Mono', monospace;">-0.0030</td>
                                <td>-5</td>
                                <td>✓</td>
                                <td>74.5%</td>
                                <td>+2.8 pts</td>
                                <td style="color:#D85A30;">-7.2</td>
                                <td>53</td>
                                <td><span class="pill low">Ít signal</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div style="margin-top:12px; font-size:11px; color:#888780;">
                    * Số liệu trên đây là kết quả backtest mô phỏng tham chiếu từ hệ thống.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
        
        st.markdown(
            """
            <div class="card">
                <h3 style="margin-top: 0; color: #0F172A; font-size:1.15rem; margin-bottom: 16px;">Phương pháp walk-forward</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px;">
                    <div style="border:1px solid #E2E1DC; border-radius:10px; padding:14px; background:rgba(255,255,255,0.4);">
                        <div style="font-size:12px; font-weight:600; color:#6C63D5; margin-bottom:6px;">In-sample (Train)</div>
                        <div style="font-size:12px; color:#5F5E5A; line-height:1.6;">60 ngày giao dịch. Chạy Grid search để tìm kiếm bộ tham số tối ưu (Spread threshold, Streak) trên tập dữ liệu lịch sử này.</div>
                    </div>
                    <div style="border:1px solid #E2E1DC; border-radius:10px; padding:14px; background:rgba(255,255,255,0.4);">
                        <div style="font-size:12px; font-weight:600; color:#0F6E56; margin-bottom:6px;">Out-of-sample (Test)</div>
                        <div style="font-size:12px; color:#5F5E5A; line-height:1.6;">20 ngày giao dịch tiếp theo. Kiểm nghiệm hiệu năng bằng bộ tham số tối ưu từ In-sample để đánh giá mức độ Overfitting.</div>
                    </div>
                    <div style="border:1px solid #E2E1DC; border-radius:10px; padding:14px; background:rgba(255,255,255,0.4);">
                        <div style="font-size:12px; font-weight:600; color:#D85A30; margin-bottom:6px;">Roll forward</div>
                        <div style="font-size:12px; color:#5F5E5A; line-height:1.6;">Tịnh tiến cửa sổ thời gian thêm 20 ngày và lặp lại liên tục quy trình Train-Test, so sánh tỉ mỉ hiệu năng giữa hai tập để đảm bảo độ tin cậy.</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif active_tab == "Alert Email":
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        
        col_sm, col_preview = st.columns([1, 1.2])
        
        with col_sm:
            st.markdown(
                """
                <div class="card" style="height: 100%;">
                    <h3 style="margin-top: 0; color: #0F172A; font-size:1.15rem; margin-bottom: 16px;">State Machine &amp; Tự động hóa</h3>
                    <div class="sm-node purple" style="margin-bottom:6px;">
                        <div class="sm-node-label">WAIT_SHORT</div>
                        <div class="sm-node-sub">Chờ điều kiện short</div>
                    </div>
                    <div style="text-align:center; padding:4px 0;">
                        <div style="font-size:11px; color:#888780; margin-bottom:2px;">↓ spread &lt; thresh &amp; streak &le; -N &amp; Signal5</div>
                        <div style="font-size:11px; color:#6C63D5; font-weight:500;">→ Gửi email SHORT</div>
                    </div>
                    <div class="sm-node teal" style="margin:6px 0;">
                        <div class="sm-node-label">WAIT_OUT</div>
                        <div class="sm-node-sub">Giữ lệnh, theo dõi exit</div>
                    </div>
                    <div style="text-align:center; padding:4px 0;">
                        <div style="font-size:11px; color:#888780; margin-bottom:2px;">↓ TP hit / streak đảo / EOD</div>
                        <div style="font-size:11px; color:#1D9E75; font-weight:500;">→ Gửi email EXIT</div>
                    </div>
                    <div class="sm-node purple" style="margin-bottom:16px;">
                        <div class="sm-node-label">WAIT_SHORT</div>
                        <div class="sm-node-sub">Reset, chờ signal tiếp</div>
                    </div>
                    <hr style="border:none; border-top:1px solid #E2E1DC; margin:16px 0;">
                    <div style="font-size:12px; font-weight:600; color:#888780; margin-bottom:10px; text-transform:uppercase; letter-spacing:.5px;">Daily summary</div>
                    <div style="background:#F7F7F6; border-radius:8px; padding:12px; font-size:12px; color:#5F5E5A; line-height:1.7;">
                        Cuối mỗi phiên (lúc 14:45), hệ thống tự động tổng hợp kết quả giao dịch trong ngày bao gồm: số lượng lệnh, tổng P&amp;L tạm tính, Win rate và tham số áp dụng, sau đó gửi email định dạng HTML cho Trader.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        with col_preview:
            email_active_tab = sac.tabs([
                sac.TabsItem(label="📉 SHORT signal"),
                sac.TabsItem(label="✅ EXIT signal"),
                sac.TabsItem(label="📊 Daily summary")
            ], align="start", size="sm", key="hedging_email_tab_selector")
            
            if email_active_tab == "📉 SHORT signal":
                st.markdown(
                    """
                    <div class="email-preview">
                        <div class="email-header">
                            <div class="email-subject">📉 [SIGNAL] SHORT VN30F1M — 10:44 | 28/05/2026</div>
                            <div class="email-meta">From: nhat.vophuoc@gmail.com &nbsp;·&nbsp; To: nhat.vophuoc@gmail.com</div>
                        </div>
                        <div class="email-body">
                            <div class="email-row"><span class="lbl">Prices Current</span><span class="val">2,012.2</span></div>
                            <div class="email-row"><span class="lbl">MA spread ratio</span><span class="val red">-0.216 (vượt ngưỡng)</span></div>
                            <div class="email-row"><span class="lbl">Streak count</span><span class="val red">20 candle âm liên tiếp</span></div>
                            <div class="email-row"><span class="lbl">Has positive spread</span><span class="val green">TRUE ✓</span></div>
                            <div class="email-row"><span class="lbl">Except</span><span class="val green">5</span></div>
                            <div class="email-row"><span class="lbl">TP target</span><span class="val">1,999 (−13.2 pts)</span></div>
                            <div class="email-row"><span class="lbl">Stop loss</span><span class="val red">2,024 (+11.8 pts)</span></div>
                            <div class="email-row"><span class="lbl">State mới</span><span class="val purple">WAIT_OUT</span></div>
                        </div>
                        <div class="email-footer">
                            <strong>Hedge nhánh:</strong> Early entry đã kích hoạt lúc 10:37 — spread -0.0028, streak -3. Tham số hiện dùng: spread -0.0025 / streak -3 / Signal5 ON.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
            elif email_active_tab == "✅ EXIT signal":
                st.markdown(
                    """
                    <div class="email-preview">
                        <div class="email-header" style="background:#1A4A3A;">
                            <div class="email-subject">✅ [EXIT] VN30F1M — PnL: +22.1 pts | 14:45</div>
                            <div class="email-meta">From: nhat.vophuoc@gmail.com &nbsp;·&nbsp; To: nhat.vophuoc@gmail.com</div>
                        </div>
                        <div class="email-body">
                            <div class="email-row"><span class="lbl">Entry</span><span class="val">2,012.2 at 10:44</span></div>
                            <div class="email-row"><span class="lbl">Exit</span><span class="val">1,990.1 at 14:45</span></div>
                            <div class="email-row"><span class="lbl">PnL</span><span class="val green">+22.1 pts</span></div>
                            <div class="email-row"><span class="lbl">%PnL</span><span class="val green">~1.1%</span></div>
                            <div class="email-row"><span class="lbl">Reason exit</span><span class="val">End of day</span></div>
                            <div class="email-row"><span class="lbl">Hold duration</span><span class="val">241 minutes</span></div>
                            <div class="email-row"><span class="lbl">State mới</span><span class="val purple">DONE FOR TODAY</span></div>
                        </div>
                        <div class="email-footer" style="background:#E1F5EE; color:#0F6E56;">
                            <strong>Trade #3 hôm nay.</strong> Tổng PnL tạm tính: +26.6 pts. Phiên giao dịch đã kết thúc.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
            elif email_active_tab == "📊 Daily summary":
                st.markdown(
                    """
                    <div class="email-preview">
                        <div class="email-header" style="background:#2D2B45;">
                            <div class="email-subject">📊 [DAILY] VN30F1M Summary — 28/05/2026</div>
                            <div class="email-meta">From: nhat.vophuoc@gmail.com &nbsp;·&nbsp; To: nhat.vophuoc@gmail.com</div>
                        </div>
                        <div class="email-body">
                            <div class="email-row"><span class="lbl">Tổng số trade</span><span class="val">4</span></div>
                            <div class="email-row"><span class="lbl">Win / Loss</span><span class="val">3W / 1L</span></div>
                            <div class="email-row"><span class="lbl">Win rate ngày</span><span class="val green">75%</span></div>
                            <div class="email-row"><span class="lbl">Tổng PnL (pts)</span><span class="val green">+10.2 pts</span></div>
                            <div class="email-row"><span class="lbl">Best trade</span><span class="val">+4.4 pts (10:44–11:01)</span></div>
                            <div class="email-row"><span class="lbl">Worst trade</span><span class="val red">-3.1 pts (10:30–11:15)</span></div>
                            <div class="email-row"><span class="lbl">Tham số dùng</span><span class="val" style="font-family: 'JetBrains Mono', monospace; font-size:12px;">spread -0.0025 / streak -3</span></div>
                        </div>
                        <div class="email-footer">
                            Ngày mai pipeline sẽ tiếp tục với cùng tham số. Kiểm tra biểu đồ chi tiết tại dashboard.
                        </div>
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
# 3. SIDEBAR NAVIGATION USING STREAMLIT-ANTD-COMPONENTS
# ---------------------------------------------------------
import streamlit_antd_components as sac

# Map page names to their indices in sac.menu
menu_map = {
    '🏠 Home': 0,
    '📁 Projects': 1,
    '📊 BCTC Chứng Khoán VN': 2,
    '📈 Hedging VN30F1M': 3,
    '👤 Contact': 4
}

# Initialize session state for active selection if not present
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 Home"
if "last_page" not in st.session_state:
    st.session_state.last_page = st.session_state.current_page

# Get the index of the current page
current_index = menu_map.get(st.session_state.current_page, 0)

with st.sidebar:
    selected = sac.menu([
        sac.MenuItem('🏠 Home'),
        sac.MenuItem('📁 Projects', children=[
            sac.MenuItem('📊 BCTC Chứng Khoán VN'),
            sac.MenuItem('📈 Hedging VN30F1M'),
        ]),
        sac.MenuItem('👤 Contact'),
    ], index=current_index, key="sidebar_menu")

# Update session state with the selected page
st.session_state.current_page = selected

# Handle parent menu click redirect to first child
if selected == '📁 Projects':
    selected = '📊 BCTC Chứng Khoán VN'
    st.session_state.current_page = '📊 BCTC Chứng Khoán VN'

# Scroll to top if page changed (run before page rendering to prevent lag)
if st.session_state.last_page != st.session_state.current_page:
    if "scroll_counter" not in st.session_state:
        st.session_state.scroll_counter = 0
    st.session_state.scroll_counter += 1
    
    components.html(
        f"""
        <!-- scroll_id: {st.session_state.scroll_counter} -->
        <script>
            const scrollToTop = () => {{
                try {{
                    window.parent.scrollTo(0, 0);
                    if (window.parent.document.documentElement) {{
                        window.parent.document.documentElement.scrollTop = 0;
                    }}
                    if (window.parent.document.body) {{
                        window.parent.document.body.scrollTop = 0;
                    }}
                    const main = window.parent.document.querySelector('.main');
                    if (main) {{
                        main.scrollTop = 0;
                        main.scrollTo(0, 0);
                    }}
                    const app = window.parent.document.querySelector('.stApp');
                    if (app) {{
                        app.scrollTop = 0;
                        app.scrollTo(0, 0);
                    }}
                }} catch (e) {{
                    console.error("Scroll to top error:", e);
                }}
            }};
            
            // Run at key intervals to beat Streamlit's rendering & scroll restoration without lag
            scrollToTop();
            setTimeout(scrollToTop, 50);
            setTimeout(scrollToTop, 200);
        </script>
        """,
        height=0,
        width=0
    )
    st.session_state.last_page = st.session_state.current_page

# Render corresponding pages based on selection
if selected == '🏠 Home':
    render_home()
elif selected == '📊 BCTC Chứng Khoán VN':
    render_securities()
elif selected == '📈 Hedging VN30F1M':
    render_hedging()
elif selected == '👤 Contact':
    render_contact()

# Inject custom JS to style the Ant Design menu inside its iframe (forcing Plus Jakarta Sans font)
components.html(
    """
    <script>
    const styleIframe = (doc) => {
        if (doc.getElementById('custom-font-style')) return;
        const style = doc.createElement('style');
        style.id = 'custom-font-style';
        style.textContent = `
            @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
            * {
                font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
                font-size: 14px !important;
            }
            
            /* Force all top-level items (Home, Projects, Contact) to be bold and purple */
            .ant-menu-root > .ant-menu-item,
            .ant-menu-root > .ant-menu-submenu > .ant-menu-submenu-title {
                color: #5B21B6 !important;
                font-weight: 600 !important;
            }
            .ant-menu-root > .ant-menu-item .ant-menu-title-content,
            .ant-menu-root > .ant-menu-submenu > .ant-menu-submenu-title .ant-menu-title-content {
                color: #5B21B6 !important;
            }
            
            /* Sub-menu items (children) should be normal weight and slate color */
            .ant-menu-sub .ant-menu-item {
                color: #475569 !important;
                font-weight: 450 !important;
            }
            .ant-menu-sub .ant-menu-item .ant-menu-title-content {
                color: #475569 !important;
            }
            .ant-menu-sub .ant-menu-item:hover,
            .ant-menu-sub .ant-menu-item:hover .ant-menu-title-content {
                color: #5B21B6 !important;
            }
            
            /* Custom styling for Ant Design active/selected items */
            .ant-menu-item-selected {
                background-color: rgba(91, 33, 182, 0.08) !important;
                color: #5B21B6 !important;
                font-weight: 600 !important;
            }
            .ant-menu-item-selected .ant-menu-title-content {
                color: #5B21B6 !important;
            }

            /* Disable expand/collapse transition animations for submenu to show all items instantly */
            .ant-menu-sub.ant-motion-collapse {
                animation: none !important;
                transition: none !important;
            }
            .ant-menu-sub.ant-motion-collapse-appear,
            .ant-menu-sub.ant-motion-collapse-enter {
                opacity: 1 !important;
                height: auto !important;
                animation: none !important;
                transition: none !important;
            }
            .ant-motion-collapse-appear-active,
            .ant-motion-collapse-enter-active {
                animation: none !important;
                transition: none !important;
            }
            .ant-menu-item {
                transition: none !important;
            }
            .ant-menu-submenu-arrow {
                transition: none !important;
            }
        `;
        doc.head.appendChild(style);
    };

    const tryAllIframes = () => {
        const iframes = parent.document.getElementsByTagName('iframe');
        for (let iframe of iframes) {
            try {
                const doc = iframe.contentDocument || iframe.contentWindow.document;
                if (doc && doc.querySelector('.ant-menu')) {
                    styleIframe(doc);
                }
            } catch(e) {}
        }
    };

    // Observe parent DOM for new iframes being added
    const observer = new MutationObserver(tryAllIframes);
    observer.observe(parent.document.body, { childList: true, subtree: true });

    // Also run immediately
    tryAllIframes();
    </script>
    """,
    height=0,
    width=0
)
