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
    page_icon="🛠️",
    layout="wide"
)

# ==========================================================
# WAKTU INDONESIA (WIB)
# ==========================================================

utc_now = datetime.utcnow()
wib_now = utc_now + timedelta(hours=7)

tanggal = wib_now.strftime("%A, %d %B %Y")
jam = wib_now.strftime("%H:%M:%S WIB")

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

/* ==========================================================
PAGE
========================================================== */

.block-container{
    max-width:1400px;
    padding-top:1.5rem;
    padding-bottom:2rem;
}

/* ==========================================================
HEADER
========================================================== */

.page-title{
    font-size:38px;
    font-weight:700;
    color:#111827;
    margin-bottom:4px;
    line-height:1.2;
}

.page-subtitle{
    font-size:15px;
    color:#6B7280;
    margin-top:0;
}

.datetime-card{
    background:#FFFFFF;
    border:1px solid #E5E7EB;
    border-radius:12px;
    padding:14px 18px;
    text-align:center;
    box-shadow:0 2px 8px rgba(0,0,0,.05);
}

.datetime-title{
    font-size:13px;
    color:#6B7280;
    margin-bottom:6px;
}

.datetime-date{
    font-size:15px;
    font-weight:600;
    color:#111827;
}

.datetime-time{
    font-size:14px;
    color:#2563EB;
    font-weight:600;
    margin-top:3px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# WAKTU WIB
# ==========================================================

from datetime import datetime, timedelta

utc_now = datetime.utcnow()
wib_now = utc_now + timedelta(hours=7)

tanggal = wib_now.strftime("%A, %d %B %Y")
jam = wib_now.strftime("%H:%M WIB")

# ==========================================================
# HEADER
# ==========================================================

left, right = st.columns([4,1])

with left:

    st.markdown("""
    <div class="page-title">
        📊 Analisis Data Baru
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="page-subtitle">
        Analisis kendaraan menggunakan algoritma Random Forest untuk memperoleh prediksi layanan servis.
    </div>
    """, unsafe_allow_html=True)

with right:

    st.markdown(f"""
    <div class="datetime-card">

        <div class="datetime-title">
            Tanggal & Jam
        </div>

        <div class="datetime-date">
            {tanggal}
        </div>

        <div class="datetime-time">
            {jam}
        </div>

    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
