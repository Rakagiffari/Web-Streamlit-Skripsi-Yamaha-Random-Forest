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

    min-width: 250px !important;
    max-width: 250px !important;

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
    padding-left: 14px;
    padding-right: 14px;
    padding-bottom: 18px;
}

/* =========================================
MENU TITLE
========================================= */
[data-testid="stSidebarNav"]::before {

    content: "MENU";

    display: block;

    color: white;

    font-size: 22px;

    font-weight: 800;

    letter-spacing: 1px;

    margin-bottom: 18px;

    padding-left: 6px;
}

/* =========================================
MENU LIST
========================================= */
[data-testid="stSidebarNav"] ul {

    display: flex;
    flex-direction: column;

    gap: 10px;

    height: 100%;
}

/* =========================================
MENU ITEM
========================================= */
[data-testid="stSidebarNav"] li {

    list-style: none;

    border-radius: 14px;

    overflow: hidden;

    background:
        rgba(255,255,255,0.03);

    border:
        1px solid rgba(255,255,255,0.05);

    transition:
        all 0.2s ease;
}

/* =========================================
MENU HOVER
========================================= */
[data-testid="stSidebarNav"] li:hover {

    transform: translateX(4px);

    background:
        rgba(255,255,255,0.06);

    border:
        1px solid rgba(239,68,68,0.25);
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

    border:
        1px solid rgba(255,255,255,0.08);

    box-shadow:
        0 0 16px rgba(239,68,68,0.18);
}

/* =========================================
MENU LINK
========================================= */
[data-testid="stSidebarNav"] a {

    color: white !important;

    font-size: 14px !important;

    font-weight: 700 !important;

    padding: 14px 16px;

    text-decoration: none;
}

/* =========================================
ABOUT MENU BOTTOM
========================================= */
[data-testid="stSidebarNav"] li:last-child {

    margin-top: auto;

    border-top:
        1px solid rgba(255,255,255,0.08);

    padding-top: 8px;

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
    margin-bottom: 10px;
}

/* =========================================
MAIN TITLE
========================================= */
.main-title{

    text-align: center;

    font-size: 48px;

    font-weight: 900;

    color: white;

    line-height: 1.1;

    margin-top: 0px;

    margin-bottom: 10px;

    letter-spacing: 1px;
}

/* =========================================
DESCRIPTION
========================================= */
.desc{

    text-align: center;

    color: #cbd5e1;

    font-size: 18px;

    margin-top: 0px;

    margin-bottom: 40px;
}

/* =========================================
CARD
========================================= */
.metric-card{

    background:
        linear-gradient(
            145deg,
            #111827,
            #1e293b
        );

    padding: 24px 18px;

    border-radius: 22px;

    border:
        1px solid #334155;

    text-align: center;

    transition: 0.3s ease;

    min-height: 145px;

    display:flex;
    flex-direction:column;
    justify-content:center;
}

/* =========================================
CARD HOVER
========================================= */
.metric-card:hover{

    transform: translateY(-5px);

    border:
        1px solid #ef4444;

    box-shadow:
        0 0 20px rgba(239,68,68,0.15);
}

/* =========================================
CARD TITLE
========================================= */
.metric-title{

    color: #94a3b8;

    font-size: 14px;

    margin-bottom: 12px;

    font-weight: 600;
}

/* =========================================
CARD VALUE
========================================= */
.metric-value{

    color: white;

    font-size: 24px;

    font-weight: 800;
}

/* =========================================
SUCCESS BOX
========================================= */
.stAlert{

    border-radius: 16px;

    background:
        rgba(15,23,42,0.75);

    border:
        1px solid rgba(239,68,68,0.15);
}

/* =========================================
RESPONSIVE
========================================= */
@media (max-width: 1200px){

    .main-title{
        font-size: 42px !important;
    }

    .desc{
        font-size: 16px !important;
    }

    .metric-value{
        font-size: 20px !important;
    }
}

@media (max-width: 900px){

    .main-title{
        font-size: 34px !important;
    }

    .desc{
        font-size: 15px !important;
    }

    section[data-testid="stSidebar"] {

        min-width: 220px !important;
        max-width: 220px !important;
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
        width=150
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
    [0.5,1,1,1,0.5]
)

# =========================================
# CARD 1
# =========================================
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

# =========================================
# CARD 2
# =========================================
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

# =========================================
# CARD 3
# =========================================
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
st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# SUCCESS MESSAGE
# =========================================
st.success(
    "ⓘ Gunakan menu sidebar untuk memulai sistem klasifikasi layanan servis Yamaha."
)
