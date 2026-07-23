# ==========================================================
# IMPORT
# ==========================================================

import streamlit as st
from datetime import datetime, timedelta

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Analisis Data Baru",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# WAKTU
# ==========================================================

wib_now = datetime.utcnow() + timedelta(hours=7)

tanggal = wib_now.strftime("%d %B %Y")
jam = wib_now.strftime("%H:%M WIB")

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

.block-container{
    max-width:1400px;
    padding-top:1.2rem;
    padding-bottom:2rem;
}

.page-title{
    font-size:36px;
    font-weight:700;
    color:#1F2937;
    margin-bottom:2px;
}

.page-subtitle{
    font-size:15px;
    color:#6B7280;
}

.datetime{
    text-align:right;
    font-size:14px;
    color:#6B7280;
    margin-top:6px;
}

.datetime b{
    color:#111827;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

col_title, col_date = st.columns([5,1])

with col_title:

    st.markdown(
        '<div class="page-title">📊 Analisis Data Baru</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Input data kendaraan untuk memperoleh hasil analisis layanan servis.'
        '</div>',
        unsafe_allow_html=True
    )

with col_date:

    st.markdown(
        f"""
<div class="datetime">
<b>{tanggal}</b><br>
{jam}
</div>
""",
        unsafe_allow_html=True
    )

st.divider()
