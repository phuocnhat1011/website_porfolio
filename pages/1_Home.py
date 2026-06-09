import json
import base64
import html as _html
from pathlib import Path
import base64
import mimetypes
import streamlit as st
from shared import apply_style
from textwrap import dedent


st.set_page_config(
    page_title="Home | Võ Phước Nhật",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_style()

# ---- FIX spacing / UI tweaks (để không bị "dính" giữa hero và CTA)
st.markdown(
    """
<style>
/* đẩy nội dung lên cao hơn (giảm header padding mặc định) */
.block-container { padding-top: 1.2rem !important; }

/* hero tách rõ khỏi phần dưới */
.hero { margin-bottom: 16px !important; }

/* CTA row gọn về trái */
.cta-row-left { display:flex; gap:12px; align-items:center; flex-wrap:wrap; margin-top: 8px; }

/* KPI row dạng flex gọn */
.kpi-row { display:flex; gap:14px; flex-wrap:wrap; margin-top: 12px; margin-bottom: 4px; }
.kpi-compact { max-width: 340px; min-width: 260px; }

/* Title section rõ hơn */
.section-title { font-size: 1.7rem; font-weight: 800; margin: 6px 0 0 0; }

/* Project card */
.proj-card { padding-top: 14px !important; }

/* Status line */
.status-label { margin-top: 8px; display:flex; gap:8px; align-items:center; }

/* Tagline spacing */
.proj-meta { margin-top: 6px; }

/* CTA inside project card (đẩy lên gần tags) */
.proj-cta { margin: 10px 0 8px 0; }

/* UL trong surface chặt hơn */
.surface-tight ul { margin: 0; padding-left: 18px; }
.surface-tight li { margin: 6px 0; }
/* Card container trong 2 cột (chỉ affect project cards) */
div[data-testid="column"] div[data-testid="stContainer"]{
  border: 1px solid rgba(15,23,42,0.10) !important;
  background: rgba(255,255,255,0.92) !important;
  border-radius: 18px !important;
  padding: 18px !important;
  box-shadow: 0 10px 24px rgba(15,23,42,0.06) !important;
}

/* Cover: bleed sát mép card + không dư trắng */
.cover{
  position: relative;
  overflow: hidden;
  border-radius: 18px 18px 14px 14px;
  margin: -18px -18px 14px -18px; /* ăn sát padding container */
  background: rgba(15,23,42,0.02);
}
.cover img{
  position:absolute;
  inset:0;
  width:100% !important;
  height:100% !important;
  object-fit: cover !important;
  display:block;
}

</style>
""",
    unsafe_allow_html=True,
)

with open("data/projects.json", "r", encoding="utf-8") as f:
    projects = json.load(f)

# ---- Sidebar
with st.sidebar:
    st.markdown("### Võ Phước Nhật")
    st.caption("Power BI • BCTC • DAX")
    st.markdown("---")

# ---- Prepare avatar base64 (JPG)
avatar_b64 = ""
try:
    avatar_bytes = Path("assets/avatar.jpg").read_bytes()
    avatar_b64 = base64.b64encode(avatar_bytes).decode("utf-8")
except Exception:
    avatar_b64 = ""

hero_avatar_html = (
    f"<div class='avatar-ring'><img class='avatar-img' src='data:image/jpeg;base64,{avatar_b64}'/></div>"
    if avatar_b64
    else "<div class='avatar-ring'><div class='avatar-img' style='display:flex;align-items:center;justify-content:center;font-weight:700;'>VNJ</div></div>"
)

# ---- HERO
st.markdown(
    f"""
    <div class="hero">
      <div class="hero-row">
        <div class="hero-left">
          <h1 style="margin:0;">👋 Võ Phước Nhật</h1>
          <p class="muted" style="font-size:1.02rem; margin-top:10px;">
            Mình xây <b>Power BI dashboards</b> cho <b>BCTC</b> (Ngân hàng & Chứng khoán VN) —
            tập trung vào <b>data modeling</b>, <b>DAX</b> và <b>UX</b> để người xem ra insight nhanh.
          </p>
          <div style="margin-top:10px;">
            <span class="badge">Power BI</span>
            <span class="badge">DAX</span>
            <span class="badge">Financial Statements</span>
            <span class="badge">Data Modeling</span>
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



# ✅ spacer nhỏ (chắc chắn không dính)
st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)

# ---- Find projects by id
proj_bank = next((p for p in projects if p.get("id") == "bank_bctc"), None)
proj_sec = next((p for p in projects if p.get("id") == "securities_vn"), None)


# ---- KPI row (flex gọn)
# st.markdown(
#     """
#     <div class="kpi-row">
#       <div class="kpi kpi-compact"><b>📊 2 flagship dashboards</b><div class="muted">Ngân hàng & CK VN</div></div>
#       <div class="kpi kpi-compact"><b>🧠 Modeling + DAX</b><div class="muted">Measures • performance • UX</div></div>
#       <div class="kpi kpi-compact"><b>🧭 Menu-driven navigation</b><div class="muted">Xem theo module, không rối tab</div></div>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

st.markdown("<hr/>", unsafe_allow_html=True)

# =========================================================
#  Flagship Projects (2 cards + Accordion)
# =========================================================
st.markdown("<div class='section-title'>Flagship Projects</div>", unsafe_allow_html=True)
st.markdown(
    "<p class='muted' style='margin-top:6px;'>2 dự án chính — mở theo từng mục để trang không bị dài.</p>",
    unsafe_allow_html=True,
)

# ---- Accordion state: only ONE open across Home
if "home_acc_open" not in st.session_state:
    st.session_state.home_acc_open = None

def _toggle_home(pid: str, section: str):
    key = f"{pid}::{section}"
    st.session_state.home_acc_open = None if st.session_state.home_acc_open == key else key

def _is_home_open(pid: str, section: str) -> bool:
    return st.session_state.home_acc_open == f"{pid}::{section}"

def _fw_button(label: str, key: str) -> bool:
    try:
        return st.button(label, key=key, width="stretch")
    except TypeError:
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
        return "<span class='badge'>🟡 DOING</span>"
    if status == "DONE":
        return "<span class='badge'>🟢 DONE</span>"
    return ""
def cover_block(path, height=160):
    if not path:
        st.markdown(f"<div class='cover' style='height:{height}px;'></div>", unsafe_allow_html=True)
        return

    p = Path(path)
    if not p.exists():
        # im lặng cho đẹp (khỏi warning)
        st.markdown(f"<div class='cover' style='height:{height}px;'></div>", unsafe_allow_html=True)
        return

    mime = mimetypes.guess_type(p.name)[0] or "image/png"
    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")

    st.markdown(
        f"""
        <div class='cover' style='height:{height}px;'>
          <img src="data:{mime};base64,{b64}" />
        </div>
        """,
        unsafe_allow_html=True,
    )

def _cta_go_to_page(page_path: str, key: str):
    # CTA quan trọng: ưu tiên primary
    if st.button("📊 Mở dashboard", type="primary", use_container_width=True, key=key):
        if hasattr(st, "switch_page"):
            st.switch_page(page_path)

def render_project_accordion(p, col):
    pid = p.get("id", "p")
    with col:
        with st.container(border=True):
            cover_block(p.get("cover"), height=160)

            st.markdown(f"<h3 style='margin:0;'>{p.get('title','')}</h3>", unsafe_allow_html=True)

            sb = _status_badge(p.get("status"))
            if sb:
                st.markdown(f"<div class='status-label'><b>Status:</b> {sb}</div>", unsafe_allow_html=True)

            tagline = (p.get("tagline") or "").strip()
            if tagline:
                st.markdown(f"<div class='muted proj-meta'>{tagline}</div>", unsafe_allow_html=True)

            st.write("")
            st.markdown("".join([f"<span class='badge'>{s}</span>" for s in p.get("stack", [])]), unsafe_allow_html=True)

            st.markdown("<div class='proj-cta'></div>", unsafe_allow_html=True)
            _cta_go_to_page(p["page_path"], key=f"cta_{pid}")

            highlights = p.get("highlights", [])
            what = p.get("what_i_did", [])
            proc = p.get("process", [])

            if highlights:
                _section_box(pid, "highlights", "✨ Highlights", _ul_html(highlights))
            if what:
                _section_box(pid, "what", "🛠️ Bạn đã làm gì", _ul_html(what))
            if proc:
                _section_box(pid, "process", "🧭 Process", _ul_html(proc))


colA, colB = st.columns(2, vertical_alignment="top")

left = proj_bank or (projects[0] if projects else None)
right = proj_sec or (projects[1] if len(projects) > 1 else None)

if left:
    render_project_accordion(left, colA)
if right:
    render_project_accordion(right, colB)

if not right and len(projects) == 1:
    st.info("Hiện mới có 1 dự án trong data/projects.json. Thêm dự án thứ 2 để hiển thị đủ 2 cột.")
