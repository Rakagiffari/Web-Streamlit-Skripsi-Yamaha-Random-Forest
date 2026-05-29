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

/* =========================================
BACKGROUND
========================================= */
.stApp{
    background-color: #020617;
}

/* =========================================
SIDEBAR
========================================= */
section[data-testid="stSidebar"] {

    min-width: 220px !important;
    max-width: 220px !important;

    background:
        linear-gradient(
            180deg,
            #020617 0%,
            #081225 100%
        );

    border-right:
        1px solid rgba(255,255,255,0.05);
}

/* =========================================
SIDEBAR CONTENT
========================================= */
[data-testid="stSidebarContent"] {

    padding-top: 18px;
    padding-left: 12px;
    padding-right: 12px;
    padding-bottom: 18px;
}

/* =========================================
MENU TITLE
========================================= */
[data-testid="stSidebarNav"]::before {

    content: "MENU";

    display: block;

    color: white;

    font-size: 18px;

    font-weight: 800;

    margin-bottom: 14px;

    padding-left: 4px;

    letter-spacing: 1px;
}

/* =========================================
MENU LIST
========================================= */
[data-testid="stSidebarNav"] ul {

    display: flex;
    flex-direction: column;

    gap: 7px;

    height: 100%;
}

/* =========================================
MENU ITEM
========================================= */
[data-testid="stSidebarNav"] li {

    border-radius: 11px;

    overflow: hidden;

    background:
        rgba(255,255,255,0.025);

    border:
        1px solid rgba(255,255,255,0.04);

    transition:
        all 0.18s ease;
}

/* =========================================
MENU HOVER
========================================= */
[data-testid="stSidebarNav"] li:hover {

    transform: translateX(3px);

    background:
        rgba(255,255,255,0.05);

    border:
        1px solid rgba(239,68,68,0.18);
}

/* =========================================
ACTIVE MENU
========================================= */
[data-testid="stSidebarNav"] li:has([aria-current="page"]) {

    background:
        linear-gradient(
            90deg,
            #ef4444,
            #dc2626
        );

    box-shadow:
        0 0 12px rgba(239,68,68,0.15);
}

/* =========================================
MENU LINK
========================================= */
[data-testid="stSidebarNav"] a {

    color: white !important;

    font-size: 12.5px !important;

    font-weight: 700 !important;

    padding: 11px 14px;

    text-decoration: none;
}

/* =========================================
ABOUT MENU BOTTOM
========================================= */
[data-testid="stSidebarNav"] li:last-child {

    margin-top: auto;

    border-top:
        1px solid rgba(255,255,255,0.08);

    padding-top: 6px;

    border-radius: 0;
}

/* =========================================
MAIN CONTAINER
========================================= */
.block-container{

    padding-top: 1rem;
    padding-bottom: 2rem;
}

/* =========================================
LOGO
========================================= */
.logo-wrapper{

    text-align: center;

    margin-top: 5px;
    margin-bottom: 8px;
}

/* =========================================
MAIN TITLE
========================================= */
.main-title{

    text-align: center;

    font-size: 50px;

    font-weight: 900;

    text-transform: uppercase;

    color: white;

    line-height: 1.05;

    margin-top: 0px;

    margin-bottom: 6px;

    letter-spacing: 1.5px;
}

/* =========================================
DESCRIPTION
========================================= */
.desc{

    text-align: center;

    color: #94a3b8;

    font-size: 14px;

    font-weight: 500;

    margin-top: 0px;

    margin-bottom: 28px;

    letter-spacing: 0.2px;
}

/* =========================================
METRIC CARDS
========================================= */
.metric-card{

    background:
        linear-gradient(
            145deg,
            #0f172a,
            #1e293b
        );

    padding: 16px 14px;

    border-radius: 16px;

    border:
        1px solid rgba(255,255,255,0.06);

    text-align: center;

    transition: 0.22s ease;

    min-height: 105px;

    display:flex;

    flex-direction:column;

    justify-content:center;
}

/* =========================================
CARD HOVER
========================================= */
.metric-card:hover{

    transform: translateY(-4px);

    border:
        1px solid rgba(239,68,68,0.30);

    box-shadow:
        0 0 14px rgba(239,68,68,0.10);
}

/* =========================================
CARD TITLE
========================================= */
.metric-title{

    color: #94a3b8;

    font-size: 12px;

    font-weight: 600;

    margin-bottom: 8px;

    letter-spacing: 0.3px;
}

/* =========================================
CARD VALUE
========================================= */
.metric-value{

    color: white;

    font-size: 17px;

    font-weight: 800;

    line-height: 1.2;

    margin: 0;
}

/* =========================================
TIME VALUE
========================================= */
.time-value{

    font-size: 15px;
}

/* =========================================
SUCCESS BOX
========================================= */
.stAlert{

    border-radius: 12px;

    background:
        rgba(15,23,42,0.65);

    border:
        1px solid rgba(239,68,68,0.10);

    padding-top: 8px !important;

    padding-bottom: 8px !important;

    font-size: 13px !important;
}

/* =========================================
RESPONSIVE
========================================= */
@media (max-width: 1200px){

    .main-title{
        font-size: 42px !important;
    }

    .desc{
        font-size: 13px !important;
    }

    .metric-value{
        font-size: 16px !important;
    }
}

@media (max-width: 900px){

    .main-title{
        font-size: 32px !important;
    }

    .desc{
        font-size: 12px !important;
    }

    section[data-testid="stSidebar"] {

        min-width: 200px !important;
        max-width: 200px !important;
    }
}

/* =========================================
SCROLLBAR
========================================= */
::-webkit-scrollbar {

    width: 5px;
}

::-webkit-scrollbar-thumb {

    background: #334155;

    border-radius: 20px;
}

/* =========================================
HIDE STREAMLIT
========================================= */
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
st.markdown(
    "<div style='margin-top:5px;'></div>",
    unsafe_allow_html=True
)

# =========================================
# CENTER LOGO
# =========================================
col1, col2, col3 = st.columns([2,1,2])

with col2:

    st.markdown(
        '<div class="logo-wrapper">',
        unsafe_allow_html=True
    )

    st.image(
        str(logo_path),
        width=130
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
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
# METRIC CARDS
# =========================================
space1, col1, col2, col3, space2 = st.columns(
    [1.2,0.9,0.9,0.9,1.2]
)

# =========================================
# CARD 1
# =========================================
with col1:

    st.markdown("""
    <div class="metric-card">
        <p class="metric-title">Algoritma</p>
        <p class="metric-value">Random Forest</p>
    </div>
    """, unsafe_allow_html=True)

# =========================================
# CARD 2
# =========================================
with col2:

    st.markdown("""
    <div class="metric-card">
        <p class="metric-title">Dataset</p>
        <p class="metric-value">CSV File</p>
    </div>
    """, unsafe_allow_html=True)

# =========================================
# CARD 3
# =========================================
with col3:

    st.markdown(f"""
    <div class="metric-card">
        <p class="metric-title">Tanggal & Jam WIB</p>
        <p class="metric-value time-value">{tanggal_jam}</p>
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
