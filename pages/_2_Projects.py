import json
import streamlit as st
from shared import apply_style
import html as _html

st.set_page_config(page_title="Projects | Võ Phước Nhật", page_icon="🧩", layout="wide")
apply_style()

with open("data/projects.json", "r", encoding="utf-8") as f:
    projects = json.load(f)

st.title("🧩 Projects")
#st.caption("Danh sách dự án chính (v1). Bạn có thể mở rộng thêm dự án nhỏ sau.")

# ---- Accordion global state: only ONE box open across the whole page
if "acc_open" not in st.session_state:
    st.session_state.acc_open = None  # e.g. "securities_vn::what"

def toggle_acc(project_id: str, section: str):
    key = f"{project_id}::{section}"
    st.session_state.acc_open = None if st.session_state.acc_open == key else key

def is_open(project_id: str, section: str) -> bool:
    return st.session_state.acc_open == f"{project_id}::{section}"

def ul_html(items):
    lis = "".join([f"<li>{_html.escape(str(x))}</li>" for x in items])
    return f"<ul>{lis}</ul>"

def ol_html(items):
    lis = "".join([f"<li>{_html.escape(str(x))}</li>" for x in items])
    return f"<ol>{lis}</ol>"

def fw_button(label: str, key: str) -> bool:
    """Full-width button across Streamlit versions (new width vs old use_container_width)."""
    try:
        return st.button(label, key=key, width="stretch")
    except TypeError:
        return st.button(label, key=key, use_container_width=True)

def section_box(project_id: str, section: str, title: str, content_html: str):
    opened = is_open(project_id, section)
    caret = "▾" if opened else "▸"

    if fw_button(f"{caret} {title}", key=f"btn_{project_id}_{section}"):
        toggle_acc(project_id, section)
        st.rerun()

    if opened:
        st.markdown(
            f"<div class='surface surface-tight' style='margin-top:8px;'>{content_html}</div>",
            unsafe_allow_html=True,
        )

cols = st.columns(2)

for i, p in enumerate(projects):
    pid = p.get("id", f"p{i}")
    with cols[i % 2]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        # Title + Status badge
        status = (p.get("status") or "").upper()
        if status == "DOING":
            status_badge = "<span class='badge'>🟡 DOING</span>"
        elif status == "DONE":
            status_badge = "<span class='badge'>🟢 DONE</span>"
        else:
            status_badge = ""

        st.markdown(
            f"<h3 style='margin:0;'>{p.get('title','')}</h3>",
            unsafe_allow_html=True
        )

        if status_badge:
            st.markdown(
                f"<div class='status-label'><b>Status:</b> {status_badge}</div>",
                unsafe_allow_html=True
            )

        tagline = (p.get("tagline") or "").strip()
        if tagline:
            st.markdown(f"<div class='muted'>{tagline}</div>", unsafe_allow_html=True)
            st.write("")

        # Stack badges
        st.markdown(
            "".join([f"<span class='badge'>{s}</span>" for s in p.get("stack", [])]),
            unsafe_allow_html=True
        )
        st.write("")

        # ---- Accordion sections (default closed)
        highlights = p.get("highlights", [])
        if highlights:
            section_box(pid, "highlights", "✨ Highlights", ul_html(highlights))



        what = p.get("what_i_did", [])
        if what:
            section_box(pid, "what", "🛠️ Bạn đã làm gì", ul_html(what))



        proc = p.get("process", [])
        if proc:
            def _render_proc():
                st.markdown("\n".join([f"{idx}. {step}" for idx, step in enumerate(proc, 1)]))

            section_box(pid, "process", "🧭 Process", ul_html(proc))

        st.write("")
        st.page_link(p["page_path"], label="📊 Mở dashboard", icon=None)

        st.markdown("</div>", unsafe_allow_html=True)
