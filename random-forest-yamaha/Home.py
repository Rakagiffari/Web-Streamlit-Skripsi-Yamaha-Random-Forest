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

/* =========================
   BACKGROUND
========================= */
.stApp{
    background-color: #020617;
}

/* =========================
   SIDEBAR
========================= */
section[data-testid="stSidebar"]{
    background-color: #0f172a;
    border-right: 1px solid #1e293b;
}

/* =========================
   MAIN CONTAINER
========================= */
.block-container{
    padding-top: 1rem;
    padding-bottom: 2rem;
}

/* =========================
   MAIN TITLE
========================= */
.main-title{
    text-align: center;
    font-size: 43px;
    font-weight: 900;
    color: white;
    line-height: 1.1;
    margin-top: 5px;
    margin-bottom: 10px;
    letter-spacing: 1px;
}

/* =========================
   DESCRIPTION
========================= */
.desc{
    text-align: center;
    color: #cbd5e1;
    font-size: 14px;
    margin-top: 0px;
    margin-bottom: 45px;
}

/* =========================
   METRIC CARD
========================= */
.metric-card{
    background: linear-gradient(145deg, #111827, #1e293b);
    padding: 28px 20px;
    border-radius: 22px;
    border: 1px solid #334155;
    text-align: center;
    transition: 0.3s ease;
    box-shadow: 0 0 15px rgba(0,0,0,0.25);
    min-height: 150px;

    display:flex;
    flex-direction:column;
    justify-content:center;
}

/* =========================
   HOVER EFFECT
========================= */
.metric-card:hover{
    transform: translateY(-6px);
    border: 1px solid #ef4444;
    box-shadow: 0 0 20px rgba(239,68,68,0.25);
}

/* =========================
   METRIC TITLE
========================= */
.metric-title{
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 12px;
    font-weight: 600;
}

/* =========================
   METRIC VALUE
========================= */
.metric-value{
    color: white;
    font-size: 20px;
    font-weight: 800;
}

/* =========================
   SUCCESS BOX
========================= */
.stAlert{
    border-radius: 15px;
}
.stAlert p{
    font-size: 13px !important;
    font-weight: 500 !important;
}

/* =========================
   HIDE STREAMLIT MENU
========================= */
#MainMenu{
    visibility: hidden;
}

footer{
    visibility: hidden;
}

header{
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# SPACE TOP
# =========================================
st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)

# =========================================
# CENTER LOGO
# =========================================
col1, col2, col3 = st.columns([2,1,2])

with col2:
    st.image(
        str(logo_path),
        width=200
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
# 2 CENTER CARDS
# =========================================
space1, col1, col2, space2 = st.columns([1, 1.2, 1.2, 1])

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
            YAMAHA
        </div>
        <div class="metric-value">
            Tjahaja Baru Tabing
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
            Tanggal & Jam WIB
        </div>
        <div class="metric-value" style="font-size:20px;">
            {tanggal_jam}
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================
# SPACE
# =========================================
st.markdown("<br><br>", unsafe_allow_html=True)

# =========================================
# SUCCESS MESSAGE
# =========================================
st.success(
    "ⓘ Gunakan menu sidebar untuk memulai sistem klasifikasi layanan servis Yamaha."
)
