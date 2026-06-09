import streamlit as st
from shared import apply_style

st.set_page_config(
    page_title="CK VN | Võ Phước Nhật",
    page_icon="📊",
    layout="wide"
)

apply_style()

# ---- FULL WIDTH FIX (only this page)
st.markdown("""
<style>
.block-container {
    max-width: 100% !important;
    padding-left: 0.5rem !important;
    padding-right: 0.5rem !important;
}
</style>
""", unsafe_allow_html=True)

# ====== POWER BI EMBED ======
POWER_BI_URL = "https://app.powerbi.com/view?r=eyJrIjoiNTAxZjNhMDAtOTY2ZS00YWJiLTljOTktM2VjMzhjNDMxN2Y3IiwidCI6IjI4ZmZjMDE1LWFlOWEtNDEzNC1hOGQ2LWU3MTI4MTEzMDc2OSIsImMiOjEwfQ%3D%3D"

st.markdown(
    f"""
    <div style="width:100%; height:92vh;">
        <iframe 
            src="{POWER_BI_URL}" 
            style="width:100%; height:100%; border:none; border-radius:12px;"
            allowfullscreen="true">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)
