import streamlit as st
from shared import apply_style

st.set_page_config(page_title="About | Võ Phước Nhật", page_icon="👤", layout="wide")
apply_style()

st.title("👤 About / Contact")
st.write("Mình xây dashboard tài chính bằng Power BI, tập trung vào mô hình dữ liệu, DAX và trải nghiệm xem báo cáo.")

st.subheader("Skills")
st.markdown(
    "".join([
        "<span class='badge'>Power BI</span>",
        "<span class='badge'>DAX</span>",
        "<span class='badge'>Data Modeling</span>",
        "<span class='badge'>Financial Statements</span>",
        "<span class='badge'>Dashboard UX</span>",
    ]),
    unsafe_allow_html=True
)

st.subheader("Contact")
st.write("- Email: nhat.vophuoc@gmail.com")
st.write("- LinkedIn: https://linkedin.com/in/yourprofile")
st.write("- GitHub: https://github.com/yourprofile")

st.subheader("CV")
try:
    with open("assets/CV.pdf", "rb") as f:
        st.download_button("Download CV (PDF)", data=f, file_name="Vo-Phuoc-Nhat-CV.pdf")
except Exception:
    st.info("Tip: đặt file `assets/CV.pdf` để bật nút download.")
