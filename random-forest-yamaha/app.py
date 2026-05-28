import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime
import time

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
    padding: 30px 20px;
    border-radius: 22px;
    border: 1px solid #334155;
    text-align: center;
    transition: 0.3s ease;
    box-shadow: 0 0 15px rgba(0,0,0,0.25);
    min-height: 170px;
    display: flex;
    flex-direction: column;
    justify-content: center;
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
    margin-bottom: 14px;
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
   DATE TEXT
========================= */
.date-text{
    color: white;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 8px;
}

/* =========================
   TIME TEXT
========================= */
.time-text{
    color: #ef4444;
    font-size: 30px;
    font-weight: 900;
}

/* =========================
   SUCCESS BOX
========================= */
.stAlert{
    border-radius: 15px;
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
        width=240
    )

# =========================================
# MAIN TITLE
# =========================================
st.markdown(
    """
    <div class="main-title">
        KLASIFIKASI LAYANAN SERVICE YAMAHA
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
# REALTIME METRIC CARDS
# =========================================
placeholder = st.empty()

while True:

    now = datetime.now()

    hari_indonesia = {
        "Monday": "Senin",
        "Tuesday": "Selasa",
        "Wednesday": "Rabu",
        "Thursday": "Kamis",
        "Friday": "Jumat",
        "Saturday": "Sabtu",
        "Sunday": "Minggu"
    }

    hari = hari_indonesia[now.strftime("%A")]

    tanggal = now.strftime("%d-%m-%Y")

    jam = now.strftime("%H:%M:%S")

    with placeholder.container():

        col1, col2, col3, col4 = st.columns(4)

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
                    Tanggal & Jam
                </div>

                <div class="date-text">
                    {tanggal}
                </div>

                <div class="time-text">
                    {jam}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # =========================================
        # CARD 4
        # =========================================
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">
                    Hari
                </div>

                <div class="metric-value">
                    {hari}
                </div>
            </div>
            """, unsafe_allow_html=True)

    time.sleep(1)

# =========================================
# SPACE
# =========================================
st.markdown("<br><br>", unsafe_allow_html=True)

# =========================================
# SUCCESS MESSAGE
# =========================================
st.success(
    "Gunakan menu sidebar untuk memulai sistem klasifikasi layanan servis Yamaha."
)
