import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
import mimetypes

CSS = """
<style>
/* Font import */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Layout adjustments */
header[data-testid="stHeader"] {
    background-color: transparent !important;
}
/* Hide only the Deploy button and settings menu, keeping the sidebar toggle button visible */
[data-testid="stHeader"] [data-testid="stHeaderMenu"],
[data-testid="stHeader"] div[data-testid="stConnectionStatus"],
[data-testid="stHeader"] .stDeployButton {
    display: none !important;
}

.block-container,
.main .block-container,
[data-testid="stMain"] .block-container,
[data-testid="stAppViewContainer"] .block-container {
    padding-top: 0rem !important; 
    padding-bottom: 1rem !important; 
    margin-top: 0px !important;
    max-width: 1200px !important;
}
[data-testid="stVerticalBlock"] {
    padding-top: 0px !important;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Custom Radial Background (Premium Dark/Light Hybrid vibe) */
.stApp {
  background:
    radial-gradient(1200px 800px at 10% 5%, rgba(91, 33, 182, 0.06), transparent 50%),
    radial-gradient(1000px 800px at 90% 15%, rgba(37, 99, 235, 0.06), transparent 50%),
    linear-gradient(180deg, #F8FAFC 0%, #FFFFFF 40%, #F8FAFC 100%) !important;
}

/* Typography & Headings */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    letter-spacing: -0.03em !important;
    font-weight: 700 !important;
    color: #0F172A !important;
}
p {
    line-height: 1.7;
    color: #334155;
}
.muted {
    color: #64748B;
    font-size: 0.95rem;
}
.small {
    font-size: 0.88rem;
    color: #64748B;
}

/* Text Gradient Effect */
.text-gradient {
    background: linear-gradient(135deg, #5B21B6 0%, #2563EB 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
}

/* Glassmorphism Surfaces */
.surface, .card, .kpi, .hero {
  border: 1px solid rgba(226, 232, 240, 0.8) !important;
  background: rgba(255, 255, 255, 0.75) !important;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-radius: 20px !important;
  box-shadow: 0 10px 30px -10px rgba(15, 23, 42, 0.04), 0 1px 3px rgba(15, 23, 42, 0.02) !important;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

/* Hero Section specific details */
.hero {
  background: linear-gradient(135deg, rgba(91, 33, 182, 0.05) 0%, rgba(37, 99, 235, 0.03) 100%) !important;
  border: 1px solid rgba(91, 33, 182, 0.08) !important;
  padding: 32px !important;
  margin-bottom: 24px !important;
}

.kpi { padding: 18px 20px !important; }
.card { padding: 24px !important; }
.surface { padding: 24px !important; }

/* Interactive Hover Transitions */
.card:hover, .kpi:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px -15px rgba(91, 33, 182, 0.12), 0 0 0 1px rgba(91, 33, 182, 0.1) !important;
  border-color: rgba(91, 33, 182, 0.2) !important;
}

/* Badges */
.badge {
  display: inline-flex;
  align-items: center;
  padding: 5px 12px;
  border-radius: 999px;
  border: 1px solid rgba(226, 232, 240, 0.8) !important;
  background: rgba(241, 245, 249, 0.8) !important;
  color: #475569 !important;
  margin-right: 6px;
  margin-bottom: 8px;
  font-size: 0.82rem;
  font-weight: 550;
  transition: all 0.2s ease;
}
.badge:hover {
  background: rgba(91, 33, 182, 0.06) !important;
  border-color: rgba(91, 33, 182, 0.2) !important;
  color: #5B21B6 !important;
}

/* Cover Image Bleed Settings */
.cover {
  height: 180px;
  border-radius: 16px;
  margin-bottom: 16px;
  overflow: hidden;
  position: relative;
  background: rgba(15, 23, 42, 0.02);
  border: 1px solid rgba(226, 232, 240, 0.8);
}
.cover > img {
  position: absolute;
  inset: 0;
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  display: block;
  transition: transform 0.5s ease;
}
.card:hover .cover > img {
  transform: scale(1.04);
}

.cover.placeholder {
  background: linear-gradient(135deg, rgba(91, 33, 182, 0.08), rgba(37, 99, 235, 0.06)) !important;
}

/* Bleed cover image inside container cards */
div[data-testid="column"] div[data-testid="stContainer"] {
  border: 1px solid rgba(226, 232, 240, 0.8) !important;
  background: rgba(255, 255, 255, 0.75) !important;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-radius: 20px !important;
  padding: 24px !important;
  box-shadow: 0 10px 30px -10px rgba(15, 23, 42, 0.04) !important;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
div[data-testid="column"] div[data-testid="stContainer"]:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px -15px rgba(91, 33, 182, 0.12), 0 0 0 1px rgba(91, 33, 182, 0.1) !important;
  border-color: rgba(91, 33, 182, 0.2) !important;
}
div[data-testid="column"] div[data-testid="stContainer"] .cover {
  margin: -24px -24px 16px -24px !important;
  border-radius: 20px 20px 0 0 !important;
  border: none !important;
}

hr {
  border: none !important;
  border-top: 1px solid rgba(226, 232, 240, 0.8) !important;
  margin: 24px 0 !important;
}

/* Navigation & Sidebar styles */
section[data-testid="stSidebar"] {
  background: rgba(255, 255, 255, 0.8) !important;
  border-right: 1px solid rgba(226, 232, 240, 0.8) !important;
  backdrop-filter: blur(10px);
}
section[data-testid="stSidebar"] > div {
  padding-top: 0px !important;
}
section[data-testid="stSidebar"] [data-testid="stSidebarNav"] {
  padding-top: 0px !important;
  margin-top: 0px !important;
}
section[data-testid="stSidebar"] [data-testid="stSidebarNavItems"] {
  padding-top: 0px !important;
  margin-top: 0px !important;
}
section[data-testid="stSidebar"] [data-testid="stSidebarNav"] > ul {
  padding-top: 0px !important;
  margin-top: 0px !important;
}

/* Hero Section Layout */
.hero-row {
  display: flex;
  gap: 32px;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
}
.hero-left { flex: 1; min-width: 320px; }
.hero-right { display: flex; justify-content: center; align-items: center; }
.avatar-ring {
  width: 170px;
  height: 170px;
  border-radius: 999px;
  padding: 4px;
  background: linear-gradient(135deg, #5B21B6, #2563EB);
  box-shadow: 0 10px 25px rgba(91, 33, 182, 0.2);
}
.avatar-img {
  width: 100%;
  height: 100%;
  border-radius: 999px;
  object-fit: cover;
  border: 4px solid #FFFFFF;
  background: white;
}

/* Custom layout classes */
.kpi-row {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
  margin-top: 16px;
  margin-bottom: 8px;
}
.kpi-compact {
  flex: 1;
  min-width: 200px;
}

.status-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: #475569;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 8px;
  margin-bottom: 12px;
}

/* Buttons and Links */
div.stButton > button, div.stDownloadButton > button {
  border-radius: 12px !important;
  font-weight: 600 !important;
  padding: 8px 16px !important;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

/* Style for primary buttons in Streamlit */
div.stButton > button[data-testid="stBaseButton-primary"], 
div.stButton > button[kind="primary"],
div.stDownloadButton > button[data-testid="stBaseButton-primary"],
div.stDownloadButton > button[kind="primary"] {
    background: linear-gradient(135deg, #5B21B6 0%, #2563EB 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(91, 33, 182, 0.18) !important;
}
div.stButton > button[data-testid="stBaseButton-primary"] *, 
div.stButton > button[kind="primary"] *,
div.stDownloadButton > button[data-testid="stBaseButton-primary"] *,
div.stDownloadButton > button[kind="primary"] * {
    color: #FFFFFF !important;
}

div.stButton > button[data-testid="stBaseButton-primary"]:hover, 
div.stButton > button[kind="primary"]:hover,
div.stDownloadButton > button[data-testid="stBaseButton-primary"]:hover,
div.stDownloadButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 18px rgba(91, 33, 182, 0.28) !important;
    background: linear-gradient(135deg, #6D28D9 0%, #1D4ED8 100%) !important;
    color: #FFFFFF !important;
}
div.stButton > button[data-testid="stBaseButton-primary"]:hover *, 
div.stButton > button[kind="primary"]:hover *,
div.stDownloadButton > button[data-testid="stBaseButton-primary"]:hover *,
div.stDownloadButton > button[kind="primary"]:hover * {
    color: #FFFFFF !important;
}

/* Style for secondary buttons (like accordions or default secondary) */
div.stButton > button[data-testid="stBaseButton-secondary"], 
div.stButton > button[kind="secondary"],
div.stDownloadButton > button[data-testid="stBaseButton-secondary"],
div.stDownloadButton > button[kind="secondary"] {
    background: #FFFFFF !important;
    color: #475569 !important;
    border: 1px solid rgba(226, 232, 240, 1) !important;
    box-shadow: 0 2px 4px rgba(15, 23, 42, 0.02) !important;
}
div.stButton > button[data-testid="stBaseButton-secondary"] *, 
div.stButton > button[kind="secondary"] *,
div.stDownloadButton > button[data-testid="stBaseButton-secondary"] *,
div.stDownloadButton > button[kind="secondary"] * {
    color: #475569 !important;
}

div.stButton > button[data-testid="stBaseButton-secondary"]:hover, 
div.stButton > button[kind="secondary"]:hover,
div.stDownloadButton > button[data-testid="stBaseButton-secondary"]:hover,
div.stDownloadButton > button[kind="secondary"]:hover {
    border-color: rgba(91, 33, 182, 0.25) !important;
    background: rgba(91, 33, 182, 0.04) !important;
    color: #5B21B6 !important;
    transform: translateY(-1px) !important;
}
div.stButton > button[data-testid="stBaseButton-secondary"]:hover *, 
div.stButton > button[kind="secondary"]:hover *,
div.stDownloadButton > button[data-testid="stBaseButton-secondary"]:hover *,
div.stDownloadButton > button[kind="secondary"]:hover * {
    color: #5B21B6 !important;
}

/* Accordion sections */
.surface-tight {
  padding: 16px 20px !important;
  border-radius: 14px !important;
  background: rgba(248, 250, 252, 0.7) !important;
}
.surface-tight ul {
  margin: 0;
  padding-left: 1.2rem;
}
.surface-tight li {
  margin: 6px 0;
  font-size: 0.92rem;
  color: #475569;
}

.section-title {
  font-size: 1.8rem;
  font-weight: 800;
  color: #0F172A;
  margin-bottom: 8px;
}

.hero-contact {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 14px;
  border-radius: 12px;
  border: 1px solid rgba(226, 232, 240, 0.8);
  background: #FFFFFF;
  color: #475569 !important;
  font-size: 0.88rem;
  font-weight: 600;
  transition: all 0.25s ease;
  text-decoration: none;
}
.hero-contact:hover {
  border-color: rgba(91, 33, 182, 0.25);
  background: rgba(91, 33, 182, 0.05);
  color: #5B21B6 !important;
  transform: translateY(-2px);
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
