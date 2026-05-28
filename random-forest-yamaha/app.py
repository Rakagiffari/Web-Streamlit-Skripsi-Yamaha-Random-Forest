import streamlit as st
from pathlib import Path
from PIL import Image

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
# CUSTOM CSS
# =========================================
st.markdown("""
<style>

/* =========================
   BACKGROUND
========================= */
.stApp{
    background-color: #FFFFFF;
}

/* =========================
   SIDEBAR
========================= */
section[data-testid="stSidebar"]{
    background-color: #0f172a;
    border-right: 1px solid #1e293b;
}

/* =========================
   REMOVE TOP SPACE
========================= */
.block-container{
    padding-top: 2rem;
}

/* =========================
   MAIN TITLE
========================= */
.main-title{
    text-align: center;
    font-size: 56px;
    font-weight: 900;
    color: white;
    line-height: 1.1;
    margin-top: 10px;
    margin-bottom: 8px;
}

/* =========================
   SUB TITLE
========================= */
.sub-title{
    text-align: center;
    font-size: 32px;
    font-weight: 800;
    color: white;
    margin-bottom: 15px;
}

/* =========================
   DESCRIPTION
========================= */
.desc{
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 40px;
}

/* =========================
   METRIC CARD
========================= */
.metric-card{
    background: linear-gradient(145deg, #111827, #1e293b);
    padding: 28px;
    border-radius: 20px;
    border: 1px solid #334155;
    text-align: center;
    transition: 0.3s;
}

.metric-card:hover{
    transform: translateY(-5px);
    border: 1px solid #ef4444;
}

/* =========================
   METRIC TITLE
========================= */
.metric-title{
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 10px;
}

/* =========================
   METRIC VALUE
========================= */
.metric-value{
    color: white;
    font-size: 36px;
    font-weight: 800;
}

/* =========================
   SIDEBAR TITLE
========================= */
.sidebar-title{
    text-align: center;
    font-size: 30px;
    font-weight: 900;
    color: white;
    margin-top: 10px;
    margin-bottom: 25px;
}

/* =========================
   SUCCESS BOX
========================= */
.stAlert{
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# LOGO PALING ATAS
# =========================================
st.markdown("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2,1.6,1.2])

with col2:
    st.image(
        str(logo_path),
        width=280
    )

# =========================================
# TITLE
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
        Sistem machine learning untuk klasifikasi layanan servis kendaraan Yamaha.
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================
# METRIC CARDS
# =========================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Algoritma</div>
        <div class="metric-value">Random Forest</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Target</div>
        <div class="metric-value">2 Class</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Dataset</div>
        <div class="metric-value">CSV</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Status</div>
        <div class="metric-value">Ready</div>
    </div>
    """, unsafe_allow_html=True)

# =========================================
# SUCCESS MESSAGE
# =========================================
st.markdown("<br>", unsafe_allow_html=True)

st.success(
    "Gunakan menu sidebar untuk memulai sistem klasifikasi layanan servis Yamaha."
)
