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
# PROFESSIONAL SIDEBAR STYLE
# =========================================
st.markdown("""
<style>

/* ========================================
SIDEBAR FIXED SIZE
======================================== */
[data-testid="stSidebar"] {

    min-width: 290px;
    max-width: 290px;

    background: linear-gradient(
        180deg,
        #081225 0%,
        #0d1b3d 100%
    );

    border-right: 1px solid rgba(255,255,255,0.08);
}

/* ========================================
SIDEBAR CONTENT
======================================== */
[data-testid="stSidebarContent"] {

    display: flex;
    flex-direction: column;

    height: 100vh;

    padding-top: 20px;
    padding-left: 16px;
    padding-right: 16px;
}

/* ========================================
SIDEBAR TITLE
======================================== */
[data-testid="stSidebarNav"]::before {

    content: "YAMAHA MENU";

    display: block;

    color: white;

    font-size: 25px;

    font-weight: 800;

    letter-spacing: 1px;

    margin-bottom: 30px;

    padding-left: 10px;
}

/* ========================================
NAVIGATION CONTAINER
======================================== */
[data-testid="stSidebarNav"] {

    flex-grow: 1;
}

/* ========================================
MENU LIST
======================================== */
[data-testid="stSidebarNav"] ul {

    display: flex;

    flex-direction: column;

    height: 100%;

    gap: 14px;
}

/* ========================================
MENU CARD
======================================== */
[data-testid="stSidebarNav"] li {

    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 16px;

    overflow: hidden;

    transition: all 0.3s ease;
}

/* ========================================
HOVER EFFECT
======================================== */
[data-testid="stSidebarNav"] li:hover {

    background: rgba(255,255,255,0.10);

    transform: translateX(4px);

    border: 1px solid rgba(255,255,255,0.15);
}

/* ========================================
ACTIVE PAGE
======================================== */
[data-testid="stSidebarNav"] li:has([aria-current="page"]) {

    background: linear-gradient(
        90deg,
        #ff0000 0%,
        #b30000 100%
    );

    border: none;

    box-shadow: 0 0 18px rgba(255,0,0,0.35);
}

/* ========================================
MENU TEXT
======================================== */
[data-testid="stSidebarNav"] a {

    color: white !important;

    font-size: 17px !important;

    font-weight: 700 !important;

    padding: 14px 18px;

    border-radius: 14px;

    text-decoration: none;
}

/* ========================================
ABOUT MENU AT BOTTOM
======================================== */
[data-testid="stSidebarNav"] li:last-child {

    margin-top: auto;

    margin-bottom: 25px;

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.06);
}

/* ========================================
REMOVE STREAMLIT DEFAULT
======================================== */
[data-testid="collapsedControl"] {

    color: white;
}

/* ========================================
SCROLLBAR
======================================== */
::-webkit-scrollbar {

    width: 8px;
}

::-webkit-scrollbar-thumb {

    background: #777;

    border-radius: 10px;
}

/* ========================================
MAIN PAGE
======================================== */
.main {

    background-color: #f5f7fb;
}

/* ========================================
REMOVE DEFAULT STREAMLIT HEADER
======================================== */
header {

    visibility: hidden;
}

/* ========================================
TOP SPACING
======================================== */
.block-container {

    padding-top: 2rem;
}

/* ========================================
IMAGE CENTER
======================================== */
.center-logo {

    display: flex;
    justify-content: center;
}

/* ========================================
TITLE
======================================== */
.main-title {

    text-align: center;

    font-size: 42px;

    font-weight: 800;

    color: #0d1b3d;

    margin-top: 10px;

    margin-bottom: 5px;
}

/* ========================================
SUBTITLE
======================================== */
.sub-title {

    text-align: center;

    font-size: 18px;

    font-weight: 600;

    color: #c00000;

    margin-bottom: 40px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# WIB TIME
# =========================================
utc_now = datetime.utcnow()

wib_now = utc_now + timedelta(hours=7)

tanggal = wib_now.strftime("%d %B %Y")
jam = wib_now.strftime("%H:%M:%S WIB")

# =========================================
# LOGO
# =========================================
st.markdown('<div class="center-logo">', unsafe_allow_html=True)

st.image(
    logo,
    width=220
)

st.markdown('</div>', unsafe_allow_html=True)

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
# SUBTITLE
# =========================================
st.markdown(
    """
    <div class="sub-title">
        Penerapan Algoritma Random Forest untuk Klasifikasi Layanan Servis Kendaraan Yamaha
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================
# INFO BOX
# =========================================
col1, col2 = st.columns(2)

with col1:
    st.success(f"📅 Tanggal : {tanggal}")

with col2:
    st.success(f"🕒 Jam WIB : {jam}")

st.divider()

# =========================================
# MAIN CONTENT
# =========================================
st.markdown("""
### 👋 Selamat Datang

Aplikasi ini digunakan untuk melakukan klasifikasi layanan servis kendaraan Yamaha menggunakan algoritma Random Forest.

Gunakan menu sidebar untuk navigasi fitur aplikasi.
""")
