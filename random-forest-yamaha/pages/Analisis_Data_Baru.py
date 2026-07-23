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
MAIN PAGE
========================================================== */

.block-container{
    max-width:1400px;
    padding-top:25px;
    padding-bottom:40px;
}

/* ==========================================================
HEADER
========================================================== */

.page-header{
    display:flex;
    justify-content:space-between;
    align-items:flex-start;
    margin-bottom:28px;
}

.page-left{
    display:flex;
    flex-direction:column;
}

.page-title{
    font-size:38px;
    font-weight:700;
    color:#111827;
    margin:0;
    line-height:1.2;
}

.page-subtitle{
    font-size:15px;
    color:#6B7280;
    margin-top:6px;
}

.page-right{
    text-align:right;
}

.datetime-box{
    display:flex;
    align-items:flex-start;
    gap:10px;
}

.datetime-icon{
    font-size:20px;
    margin-top:2px;
}

.datetime-text{
    font-size:14px;
    color:#374151;
    font-weight:500;
    line-height:1.5;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown(f"""
<div class="page-header">

    <div class="page-left">

        <div class="page-title">
            Analisis Data Baru
        </div>

        <div class="page-subtitle">
            Input data kendaraan untuk mendapatkan prediksi layanan
        </div>

    </div>

    <div class="page-right">

        <div class="datetime-box">

            <div class="datetime-icon">
                📅
            </div>

            <div class="datetime-text">
                <b>{tanggal}</b><br>
                {jam}
            </div>

        </div>

    </div>

</div>
""", unsafe_allow_html=True)
