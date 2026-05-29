import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime, timedelta

# =========================================
# PAGE CONFIG
# =========================================
BASE_DIR = Path(__file__).parent

logo_path = BASE_DIR / "assets" / "yamaha_logo.png"

css_path = BASE_DIR / "global.css"

logo = Image.open(logo_path)

st.set_page_config(
    page_title="Yamaha Random Forest",
    page_icon=logo,
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# LOAD CSS
# =========================================
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
left_space, center_logo, right_space = st.columns([1.5,1,1.5])

with center_logo:

    st.image(
        str(logo_path),
        width=210
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
# CARD SECTION
# =========================================
space1, col1, col2, col3, space2 = st.columns([0.5,1,1,1,0.5])

# =========================================
# CARD 1
# =========================================
with col1:

    st.markdown(
        f"""
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
        f"""
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
st.markdown("<br><br>", unsafe_allow_html=True)

# =========================================
# SUCCESS BOX
# =========================================
st.success(
    "ⓘ Gunakan menu sidebar untuk memulai sistem klasifikasi layanan servis Yamaha."
)
