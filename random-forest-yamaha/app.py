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

    min-width: 270px !important;
    max-width: 270px !important;

    background:
        linear-gradient(
            180deg,
            #050b18 0%,
            #091428 45%,
            #0f172a 100%
        );

    border-right: 1px solid rgba(255,255,255,0.06);
}

/* =========================
   SIDEBAR CONTENT
========================= */
[data-testid="stSidebarContent"]{

    padding-top: 20px;
    padding-left: 14px;
    padding-right: 14px;
    padding-bottom: 20px;
}

/* =========================
   SIDEBAR TITLE
========================= */
[data-testid="stSidebarNav"]::before{

    content: "MENU";

    display: block;

    text-align: center;

    color: white;

    font-size: 15px;

    font-weight: 900;

    letter-spacing: 4px;

    margin-bottom: 28px;

    padding-bottom: 14px;

    border-bottom: 1px solid rgba(255,255,255,0.08);

    opacity: 0.95;
}

/* =========================
   SIDEBAR NAV
========================= */
[data-testid="stSidebarNav"]{

    display: flex;
    flex-direction: column;
    height: 100%;
}

/* =========================
   MENU LIST
========================= */
[data-testid="stSidebarNav"] ul{

    display: flex;
    flex-direction: column;

    gap: 14px;

    height: 100%;

    padding-top: 5px;
}

/* =========================
   MENU ITEM
========================= */
[data-testid="stSidebarNav"] li{

    list-style: none;

    border-radius: 16px;

    overflow: hidden;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.03),
            rgba(255,255,255,0.01)
        );

    border: 1px solid rgba(255,255,255,0.05);

    transition:
        transform 0.25s ease,
        background 0.25s ease,
        border 0.25s ease,
        box-shadow 0.25s ease;
}

/* =========================
   MENU LINK
========================= */
[data-testid="stSidebarNav"] li a{

    color: #e2e8f0 !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    text-decoration: none !important;

    padding: 14px 18px;

    display: flex;
    align-items: center;

    border-radius: 16px;

    transition: all 0.25s ease;
}

/* =========================
   HOVER EFFECT
========================= */
[data-testid="stSidebarNav"] li:hover{

    transform: translateX(5px);

    background:
        linear-gradient(
            145deg,
            rgba(239,68,68,0.18),
            rgba(127,29,29,0.15)
        );

    border: 1px solid rgba(239,68,68,0.45);

    box-shadow:
        0 0 15px rgba(239,68,68,0.18);
}

/* =========================
   HOVER TEXT
========================= */
[data-testid="stSidebarNav"] li:hover a{

    color: white !important;
}

/* =========================
   ACTIVE MENU
========================= */
[data-testid="stSidebarNav"] li:has([aria-current="page"]){

    background:
        linear-gradient(
            135deg,
            #ef4444 0%,
            #dc2626 50%,
            #991b1b 100%
        );

    border: 1px solid rgba(255,255,255,0.08);

    box-shadow:
        0 0 18px rgba(239,68,68,0.35);
}

/* =========================
   ACTIVE TEXT
========================= */
[data-testid="stSidebarNav"] li:has([aria-current="page"]) a{

    color: white !important;

    font-weight: 800 !important;
}

/* =========================
   ABOUT MENU POSITION
========================= */
[data-testid="stSidebarNav"] li:last-child{

    margin-top: auto;

    margin-bottom: 10px;
}

/* =========================
   BOTTOM ABOUT STYLE
========================= */
[data-testid="stSidebarNav"] li:last-child{

    opacity: 0.92;

    border: 1px solid rgba(255,255,255,0.04);
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
    font-size: 58px;
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
    font-size: 20px;
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
    font-size: 30px;
    font-weight: 800;
}

/* =========================
   SUCCESS BOX
========================= */
.stAlert{
    border-radius: 15px;
}

/* =========================
   SCROLLBAR
========================= */
::-webkit-scrollbar{

    width: 5px;
}

::-webkit-scrollbar-thumb{

    background: #475569;

    border-radius: 10px;
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
# 3 CENTER CARDS
# =========================================
space1, col1, col2, col3, space2 = st.columns([0.7,1,1,1,0.7])

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
            Algoritma
        </div>
        <div class="metric-value">
            Random Forest
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
            Dataset
        </div>
        <div class="metric-value">
            CSV File
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
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
    "ⓘ    Gunakan menu sidebar untuk memulai sistem klasifikasi layanan servis Yamaha."
)
