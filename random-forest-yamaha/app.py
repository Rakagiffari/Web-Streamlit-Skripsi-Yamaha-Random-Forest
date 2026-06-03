import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime, timedelta
import os

# =========================================
# BASE DIRECTORY
# =========================================
BASE_DIR = Path(__file__).parent

# =========================================
# LOGO PATH
# =========================================
logo_path = BASE_DIR / "assets" / "yamaha_logo.png"

logo = Image.open(logo_path)

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(

    page_title="Yamaha Random Forest",

    page_icon=logo,

    layout="wide",

    initial_sidebar_state="expanded"
)

# =========================================
# LOAD GLOBAL CSS
# =========================================
css_path = os.path.join(

    BASE_DIR,

    "styles",

    "global.css"
)

with open(css_path) as f:

    st.markdown(

        f"<style>{f.read()}</style>",

        unsafe_allow_html=True
    )

# =========================================
# DATE & TIME WIB
# =========================================
utc_now = datetime.utcnow()

wib_now = utc_now + timedelta(hours=7)

tanggal_jam = wib_now.strftime("%d-%m-%Y | %H:%M")

# =========================================
# SPACE TOP
# =========================================
st.markdown(

    "<div style='margin-top:10px;'></div>",

    unsafe_allow_html=True
)

# =========================================
# CENTER LOGO
# =========================================
col1, col2, col3 = st.columns([2,1,2])

with col2:

    st.image(

        str(logo_path),

        width=220
    )

# =========================================
# MAIN TITLE
# =========================================
st.markdown(
    """
    <div class="main-title">
        KLASIFIKASI LAYANAN SERVIS YAMAHA
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================
# DESCRIPTION
# =========================================
st.markdown(
    """
    <div class="desc">
        Penerapan Algoritma Random Forest untuk klasifikasi layanan servis kendaraan Yamaha.
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================
# CENTER CARDS
# =========================================
space1, col1, col2, col3, space2 = st.columns(

    [0.7,1,1,1,0.7]
)

# =========================================
# CARD 1
# =========================================
with col1:

    st.markdown(
        """
        <div class="metric-card">

            <div class="metric-title">
                Algoritma
            </div>

            <div class="metric-value">
                Random Forest
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================
# CARD 2
# =========================================
with col2:

    st.markdown(
        """
        <div class="metric-card">

            <div class="metric-title">
                Dataset
            </div>

            <div class="metric-value">
                CSV File
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================
# CARD 3
# =========================================
with col3:

    st.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-title">
                Tanggal & Jam WIB
            </div>

            <div class="metric-value" style="font-size:20px;">
                {tanggal_jam}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================
# SPACE
# =========================================
st.markdown(

    "<br><br>",

    unsafe_allow_html=True
)

# =========================================
# SUCCESS MESSAGE
# =========================================
st.success(
    "ⓘ Gunakan menu sidebar untuk memulai sistem klasifikasi layanan servis Yamaha."
)

# =========================================
# FOOTER
# =========================================
st.markdown(
    """
    <div style="
        text-align:center;
        margin-top:40px;
        color:#94a3b8;
        font-size:14px;
    ">
        Yamaha Random Forest Classification System
    </div>
    """,
    unsafe_allow_html=True
)
