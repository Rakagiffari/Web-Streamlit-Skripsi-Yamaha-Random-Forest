import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Yamaha Random Forest",
    page_icon="🏍️",
    layout="wide"
)

BASE_DIR = Path(__file__).parent
logo_path = BASE_DIR / "assets" / "yamaha_logo.png"

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🏍️ Yamaha ML Dashboard")

# =========================
# CSS
# =========================
st.markdown("""
<style>

.main-title{
    font-size: 48px;
    font-weight: 800;
    color: white;
    margin-bottom: 5px;
}

.sub-title{
    font-size: 22px;
    font-weight: 700;
    color: white;
    margin-top: -10px;
}

.desc{
    color: #dcdcdc;
    font-size: 16px;
    margin-bottom: 30px;
}

.logo-center{
    display: flex;
    justify-content: center;
    margin-top: 10px;
    margin-bottom: 20px;
}

.metric-box{
    background-color: #111827;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #1f2937;
}

.metric-title{
    color: #9ca3af;
    font-size: 15px;
}

.metric-value{
    color: white;
    font-size: 32px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown(
    '<div class="main-title">🏍️ KLASIFIKASI LAYANAN SERVIS YAMAHA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Penerapan Algoritma Random Forest</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="desc">Sistem machine learning untuk klasifikasi layanan servis kendaraan Yamaha.</div>',
    unsafe_allow_html=True
)

# =========================
# LOGO DI TENGAH (BUKAN SIDEBAR)
# =========================
if logo_path.exists():

    col_logo1, col_logo2, col_logo3 = st.columns([1,1,1])

    with col_logo2:
        st.image(str(logo_path), width=220)

# =========================
# METRICS
# =========================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-title">Algoritma</div>
        <div class="metric-value">Random Forest</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-title">Target</div>
        <div class="metric-value">2 Class</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-title">Dataset</div>
        <div class="metric-value">CSV</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-title">Status</div>
        <div class="metric-value">Ready</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# SUCCESS BOX
# =========================
st.success("Gunakan menu sidebar untuk memulai.")
