import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime, timedelta

# =========================================
# PAGE CONFIG
# =========================================

BASE_DIR = Path(__file__).parent

logo_path = BASE_DIR / "assets" / "yamaha_logo.png"

logo = Image.open(logo_path)

st.set_page_config(
    page_title="Yamaha Random Forest",
    page_icon=logo,
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# DATE & TIME WIB
# =========================================

utc_now = datetime.utcnow()

wib_now = utc_now + timedelta(hours=7)

tanggal_jam = wib_now.strftime("%d-%m-%Y | %H:%M")

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
""", unsafe_allow_html=True)

# =========================================
# SPACE TOP
# =========================================

st.markdown(
    "",
    unsafe_allow_html=True
)

# =========================================
# CENTER LOGO
# =========================================

col1, col2, col3 = st.columns([2, 1, 2])

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
    KLASIFIKASI LAYANAN SERVIS YAMAHA
    """,
    unsafe_allow_html=True
)

# =========================================
# DESCRIPTION
# =========================================

st.markdown(
    """
    Penerapan Algoritma Random Forest untuk klasifikasi layanan servis kendaraan Yamaha.
    """,
    unsafe_allow_html=True
)

# =========================================
# 3 CENTER CARDS
# =========================================

space1, col1, col2, col3, space2 = st.columns(
    [0.7, 1, 1, 1, 0.7]
)

with col1:

    st.markdown(
        f"""
        Algoritma
        Random Forest
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        f"""
        Dataset
        CSV File
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        f"""
        Tanggal & Jam WIB
        {tanggal_jam}
        """,
        unsafe_allow_html=True
    )

# =========================================
# SPACE
# =========================================

st.markdown(
    "",
    unsafe_allow_html=True
)

# =========================================
# SUCCESS MESSAGE
# =========================================

st.success(
    "ⓘ Gunakan menu sidebar untuk memulai sistem klasifikasi layanan servis Yamaha."
)
