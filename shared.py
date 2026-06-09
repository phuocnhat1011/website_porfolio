import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
import mimetypes

CSS = """
<style>
/* Layout */
.block-container {padding-top: 2.2rem; padding-bottom: 3rem; max-width: 1180px;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Light background */
.stApp{
  background:
    radial-gradient(900px 600px at 12% 8%, rgba(91,33,182,0.10), transparent 55%),
    radial-gradient(900px 600px at 85% 12%, rgba(37,99,235,0.10), transparent 60%),
    linear-gradient(180deg, #F6F7FB 0%, #FFFFFF 45%, #F6F7FB 100%);
}

/* Typography */
h1, h2, h3 {letter-spacing: -0.02em;}
p {line-height: 1.65;}
.muted {opacity: 0.75;}
.small {font-size: 0.92rem; opacity: 0.85;}

/* Surfaces (cards) */
.surface, .card, .kpi, .hero{
  border: 1px solid rgba(15,23,42,0.10);
  background: rgba(255,255,255,0.92);
  border-radius: 18px;
  box-shadow: 0 10px 24px rgba(15,23,42,0.06);
}

/* Hero */
.hero{
  background: linear-gradient(135deg, rgba(91,33,182,0.10), rgba(37,99,235,0.06));
  padding: 26px;
}

.kpi {padding: 14px 16px;}
.card {padding: 18px;}
.surface {padding: 18px;}

/* Badges */
.badge{
  display:inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  border: 1px solid rgba(15,23,42,0.12);
  background: rgba(15,23,42,0.04);
  margin-right: 8px;
  margin-bottom: 8px;
  font-size: 0.85rem;
}

/* ========= COVER (FIX) =========
   - ép ảnh fill full khung, hết dư trắng
   - bleed đúng padding card 18px
*/
.cover{
  height: 170px;
  border-radius: 14px;
  margin-bottom: 14px;
  border: 1px solid rgba(15,23,42,0.10);
  overflow: hidden;
  position: relative;
  background: rgba(15,23,42,0.02);
}

/* ép img fill tuyệt đối */
.cover > img{
  position: absolute;
  inset: 0;
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  display: block;
}

.cover.placeholder{
  background: linear-gradient(135deg, rgba(91,33,182,0.12), rgba(37,99,235,0.08));
}

/* cover ăn sát mép card (để không giống “box riêng” và không hở viền) */
.proj-card .cover{
  margin: -18px -18px 14px -18px;   /* ✅ card padding là 18px */
  border-radius: 18px 18px 14px 14px;
  border: none;                     /* tránh double-border */
}

hr {border:none; border-top:1px solid rgba(15,23,42,0.10); margin: 22px 0;}
a {text-decoration:none;}

/* Sidebar polish */
section[data-testid="stSidebar"]{
  background: rgba(255,255,255,0.88);
  border-right: 1px solid rgba(15,23,42,0.10);
}
section[data-testid="stSidebar"] > div{
  padding-top: 18px;
  padding-left: 10px;
  padding-right: 10px;
}
section[data-testid="stSidebar"] a{
  border-radius: 12px;
  padding: 10px 12px !important;
  margin: 4px 6px !important;
  color: rgba(15,23,42,0.92) !important;
}
section[data-testid="stSidebar"] a:hover{
  background: rgba(91,33,182,0.08);
}
section[data-testid="stSidebar"] a[aria-current="page"]{
  background: rgba(91,33,182,0.12);
  border: 1px solid rgba(91,33,182,0.18);
}
section[data-testid="stSidebar"]{
  min-width: 255px;
}

/* Hero layout */
.hero-row{
  display:flex;
  gap: 22px;
  align-items:center;
  justify-content:space-between;
  flex-wrap: wrap;
}
.hero-left{flex: 1; min-width: 360px;}
.hero-right{width: 220px; display:flex; justify-content:center; align-items:center;}
.avatar-ring{
  width: 200px; height: 200px;
  border-radius: 999px;
  padding: 4px;
  background: linear-gradient(135deg, rgba(91,33,182,0.45), rgba(37,99,235,0.35));
  box-shadow: 0 14px 30px rgba(15,23,42,0.10);
}
.avatar-img{
  width: 100%; height: 100%;
  border-radius: 999px;
  object-fit: cover;
  border: 4px solid rgba(255,255,255,0.95);
  background: white;
}

.cta-wrap{ margin-top: 12px; margin-bottom: 6px; }
div.stPageLink a, div.stLinkButton a{
  border-radius: 14px !important;
  padding: 10px 14px !important;
  border: 1px solid rgba(15,23,42,0.12) !important;
}
div.stPageLink a:hover, div.stLinkButton a:hover{
  border-color: rgba(91,33,182,0.35) !important;
  background: rgba(91,33,182,0.06) !important;
}

/* Tight content box for accordion */
.surface-tight{ padding: 12px 16px !important; }
.surface-tight p{ margin: 0.35rem 0 !important; }
.surface-tight ul{ margin: 0.35rem 0 0.35rem 1.2rem !important; }
.surface-tight li{ margin: 0.25rem 0 !important; }

.status-label{
  font-size: 0.92rem;
  opacity: 0.85;
  margin-top: 6px;
  margin-bottom: 10px;
}

/* HOME/GENERAL TIGHTEN */
.block-container{
  padding-top: 1.0rem !important;
  padding-bottom: 2.0rem !important;
}
div[data-testid="stVerticalBlock"]{ gap: 0.75rem !important; }
hr{ margin: 14px 0 !important; }

.kpi-row{
  display:flex;
  gap: 14px;
  flex-wrap: wrap;
  align-items: stretch;
  margin-top: 10px;
}
.kpi.kpi-compact{
  flex: 1;
  min-width: 240px;
  max-width: 360px;
  padding: 14px 16px;
}

.proj-card{
  display:flex;
  flex-direction: column;
  height: 100%;
}
.proj-meta{ margin-top: 6px; }
.proj-cta{ margin-top: 12px; margin-bottom: 8px; }

.section-title{
  font-size: 1.7rem;
  font-weight: 800;
  margin: 0;
}

.stButton > button{
  border-radius: 14px !important;
}
.hero-actions{ margin-top: 14px; display:flex; gap:10px; flex-wrap:wrap; }

.hero-contact{
  display:inline-flex; align-items:center; gap:8px;
  padding: 10px 14px;
  border-radius: 14px;
  border: 1px solid rgba(15,23,42,0.14);
  background: rgba(255,255,255,0.75);
  color: rgba(15,23,42,0.92);
  font-weight: 600;
}

.hero-contact:hover{
  border-color: rgba(91,33,182,0.35);
  background: rgba(91,33,182,0.06);
}
</style>
"""


def apply_style():
    st.markdown(CSS, unsafe_allow_html=True)


def file_exists(path: str) -> bool:
    return Path(path).exists()


def embed_powerbi(url: str, height: int = 900):
    components.iframe(url, height=height + 56, scrolling=True)


def cover_block(path, height=160):
    # Nếu không có ảnh -> show placeholder (đỡ rỗng)
    if not path or not Path(path).exists():
        st.markdown(
            f"<div class='cover placeholder' style='height:{height}px;'></div>",
            unsafe_allow_html=True,
        )
        return

    p = Path(path)
    mime, _ = mimetypes.guess_type(str(p))
    if not mime:
        # fallback
        mime = "image/png" if p.suffix.lower() == ".png" else "image/jpeg"

    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")

    st.markdown(
        f"""
        <div class="cover" style="height:{height}px;">
          <img src="data:{mime};base64,{b64}" />
        </div>
        """,
        unsafe_allow_html=True,
    )
