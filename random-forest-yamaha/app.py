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
<style>

.main-title{
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #111111;
    margin-top: 10px;
    margin-bottom: 10px;
    letter-spacing: 1px;
}

.sub-title{
    text-align: center;
    font-size: 18px;
    color: #c00000;
    margin-bottom: 35px;
    font-weight: 600;
}

.info-card{
    background-color: #ffffff;
    padding: 22px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    border: 1px solid #eeeeee;
}

.card-title{
    font-size: 15px;
    color: #666666;
    margin-bottom: 8px;
    font-weight: 600;
}

.card-value{
    font-size: 22px;
    font-weight: bold;
    color: #111111;
}

div[data-testid="stAlert"]{
    background-color: rgba(0, 128, 0, 0.75);
    color: white;
    border-radius: 14px;
    border: none;
    padding: 18px;
    font-size: 16px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# SPACE TOP
# =========================================
st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# CENTER LOGO
# =========================================
col1, col2, col3 = st.columns([2,1,2])

with col2:
    st.image(str(logo_path), width=220)

# =========================================
# MAIN TITLE
# =========================================
st.markdown("""
<div class="main-title">
KLASIFIKASI LAYANAN SERVIS YAMAHA
</div>
""", unsafe_allow_html=True)

# =========================================
# DESCRIPTION
# =========================================
st.markdown("""
<div class="sub-title">
Penerapan Algoritma Random Forest untuk klasifikasi layanan servis kendaraan Yamaha.
</div>
""", unsafe_allow_html=True)

# =========================================
# 3 CENTER CARDS
# =========================================
space1, col1, col2, col3, space2 = st.columns([0.7,1,1,1,0.7])

with col1:
    st.markdown(f"""
    <div class="info-card">
        <div class="card-title">Algoritma</div>
        <div class="card-value">Random Forest</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="info-card">
        <div class="card-title">Dataset</div>
        <div class="card-value">CSV File</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="info-card">
        <div class="card-title">Tanggal & Jam WIB</div>
        <div class="card-value">{tanggal_jam}</div>
    </div>
    """, unsafe_allow_html=True)

# =========================================
# SPACE
# =========================================
st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# SUCCESS MESSAGE
# =========================================
st.success(
    "ⓘ Gunakan menu sidebar untuk memulai sistem klasifikasi layanan servis Yamaha."
)
