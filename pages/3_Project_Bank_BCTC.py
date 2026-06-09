import json
import streamlit as st
from shared import apply_style, embed_powerbi

st.set_page_config(page_title="BCTC Ngân hàng | Võ Phước Nhật", page_icon="🏦", layout="wide")
apply_style()

with open("data/projects.json", "r", encoding="utf-8") as f:
    projects = {p["id"]: p for p in json.load(f)}

p = projects["bank_bctc"]

st.title("🏦 " + p["title"])
st.markdown(f"<div class='muted'>{p['tagline']}</div>", unsafe_allow_html=True)
st.write("")
st.markdown("".join([f"<span class='badge'>{s}</span>" for s in p.get("stack", [])]), unsafe_allow_html=True)

st.write("")
st.subheader("What’s inside")
st.write("- Tổng quan BCTC theo kỳ")
st.write("- CĐKT / KQKD / LCTT (năm/quý/6T tuỳ report)")
st.write("- Chỉ số & so sánh theo ngân hàng (nếu có)")

with st.expander("How to use (30s)"):
    st.write("1) Bắt đầu từ trang **MENU/Overview**")
    st.write("2) Chọn **Ngân hàng / Kỳ** bằng slicer")
    st.write("3) Click chart để cross-filter các phần liên quan")

st.write("")
st.subheader("Live dashboard")
url = p["powerbi_url"]
if "PASTE_YOUR" in url:
    st.warning("Bạn chưa dán link Power BI. Vào `data/projects.json` và thay `powerbi_url` bằng Publish-to-web URL.")
else:
    embed_powerbi(url, height=900)
