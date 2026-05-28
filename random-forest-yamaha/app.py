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

/* ===== Background ===== */
.stApp{
    background-color: #020617;
}

/* ===== Sidebar ===== */
section[data-testid="stSidebar"]{
    background-color: #0f172a;
    border-right: 1px solid #1e293b;
}

/* ===== Main Title ===== */
.main-title{
    font-size: 52px;
    font-weight: 800;
    color: white;
    margin-bottom: 0px;
    line-height: 1.1;
}

/* ===== Subtitle ===== */
.sub-title{
    font-size: 34px;
    font-weight: 700;
    color: white;
    margin-top: -5px;
    margin-bottom: 10px;
}

/* ===== Description ===== */
.desc{
    color: #cbd5e1;
    font-size: 17px;
    margin-bottom: 35px;
}

/* ===== Yamaha Logo Center ===== */
.logo-center{
    display: flex;
    justify-content: center;
    margin-top: 10px;
    margin-bottom: 25px;
}

/* ===== Metric Card ===== */
.metric-card{
    background: linear-gradient(145deg, #111827, #1e293b);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #334155;
    text-align: center;
    transition: 0.3s;
}

.metric-card:hover{
    transform: translateY(-3px);
    border: 1px solid #ef4444;
}

/* ===== Metric Title ===== */
.metric-title{
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 10px;
}

/* ===== Metric Value ===== */
.metric-value{
    color: white;
    font-size: 34px;
    font-weight: 700;
}

/* ===== Success Box ===== */
.stAlert{
    border-radius: 15px;
}

/* ===== Sidebar Text ===== */
.sidebar-title{
    font-size: 28px;
    font-weight: 800;
    color: white;
    margin-top: 10px;
    margin-bottom: 20px;
    text-align: center;
}

/* ===== Remove top spacing ===== */
.block-container{
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================
st.sidebar.markdown(
    '<div class="sidebar-title">Yamaha ML Dashboard</div>',
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

st.sidebar.write("### 📌 Menu")
st.sidebar.write("• About Research")
st.sidebar.write("• Dashboard")
st.sidebar.write("• Feature Importance")
st.sidebar.write("• Training Model")

# =========================================
# HEADER
# =========================================
st.markdown(
    """
    <div class="main-title">
        KLASIFIKASI LAYANAN SERVIS YAMAHA
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
        Penerapan Algoritma Random Forest
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="desc">
        Sistem machine learning untuk klasifikasi layanan servis kendaraan Yamaha.
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================
# LOGO TENGAH
# =========================================
if logo_path.exists():

    col1, col2, col3 = st.columns([1,1,1])

    with col2:
        st.image(str(logo_path), width=220)

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
