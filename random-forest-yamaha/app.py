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

    background:
        linear-gradient(
            135deg,
            #f6f7f2 0%,
            #eef2dc 100%
        );
}

/* =========================
   SIDEBAR
========================= */
section[data-testid="stSidebar"]{

    background:
        linear-gradient(
            180deg,
            #3D4127 0%,
            #636B2F 100%
        );

    border-right:
        1px solid #BAC095;
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

    color: #3D4127;

    line-height: 1.1;

    margin-top: 5px;

    margin-bottom: 10px;

    letter-spacing: 1px;

    text-shadow:
        0 2px 8px rgba(61,65,39,0.08);
}

/* =========================
   DESCRIPTION
========================= */
.desc{

    text-align: center;

    color: #636B2F;

    font-size: 20px;

    margin-top: 0px;

    margin-bottom: 45px;
}

/* =========================
   METRIC CARD
========================= */
.metric-card{

    background:
        linear-gradient(
            145deg,
            #ffffff,
            #BAC095
        );

    padding: 28px 20px;

    border-radius: 24px;

    border:
        1px solid rgba(99,107,47,0.15);

    text-align: center;

    transition: 0.35s ease;

    box-shadow:
        0 8px 25px rgba(61,65,39,0.10);

    min-height: 160px;

    display:flex;

    flex-direction:column;

    justify-content:center;

    backdrop-filter: blur(6px);
}

/* =========================
   HOVER EFFECT
========================= */
.metric-card:hover{

    transform:
        translateY(-8px);

    border:
        1px solid #636B2F;

    box-shadow:
        0 15px 30px rgba(61,65,39,0.20);
}

/* =========================
   METRIC TITLE
========================= */
.metric-title{

    color: #3D4127;

    font-size: 15px;

    margin-bottom: 12px;

    font-weight: 700;

    letter-spacing: 0.5px;
}

/* =========================
   METRIC VALUE
========================= */
.metric-value{

    color: #1f2412;

    font-size: 30px;

    font-weight: 900;
}

/* =========================
   SUCCESS BOX
========================= */
.stAlert{

    border-radius: 16px;

    background:
        linear-gradient(
            90deg,
            #636B2F,
            #3D4127
        );

    color: white;

    border:
        1px solid #BAC095;

    box-shadow:
        0 4px 15px rgba(61,65,39,0.20);
}

/* =========================
   BUTTON
========================= */
.stButton>button{

    background:
        linear-gradient(
            90deg,
            #636B2F,
            #3D4127
        );

    color: white;

    border-radius: 12px;

    border: none;

    padding:
        0.6rem 1.3rem;

    font-weight: 700;

    transition: 0.3s ease;

    box-shadow:
        0 5px 15px rgba(61,65,39,0.15);
}

.stButton>button:hover{

    transform:
        translateY(-2px);

    background:
        linear-gradient(
            90deg,
            #3D4127,
            #636B2F
        );

    color: white;
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
st.markdown(
    "<div style='margin-top:10px;'></div>",
    unsafe_allow_html=True
)

# =========================================
# CENTER LOGO
# =========================================
col1, col2, col3 = st.columns([2,1,2])

with col2:

    st.image(
        str(logo_path),
        width=210
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
    [0.7,1,1,1,0.7]
)

# =========================================
# CARD 1
# =========================================
with col1:

    st.markdown("""
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

    st.markdown("""
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
st.markdown(
    "<br><br>",
    unsafe_allow_html=True
)

# =========================================
# SUCCESS MESSAGE
# =========================================
st.success(
    "ⓘ Gunakan menu sidebar untuk memulai sistem klasifikasi layanan servis Yamaha."
)
