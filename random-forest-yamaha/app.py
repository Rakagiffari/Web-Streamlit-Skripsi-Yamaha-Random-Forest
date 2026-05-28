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
    padding-bottom: 1rem;
}

/* =========================
   TITLE
========================= */
.main-title{
    text-align: center;
    font-size: 58px;
    font-weight: 900;
    color: white;
    line-height: 1.1;
    margin-top: 5px;
    margin-bottom: 12px;
    letter-spacing: 1px;
}

/* =========================
   DESCRIPTION
========================= */
.desc{
    text-align: center;
    color: #cbd5e1;
    font-size: 20px;
    margin-bottom: 45px;
}

/* =========================
   CARD
========================= */
.metric-card{
    background: linear-gradient(145deg, #111827, #1e293b);
    border: 1px solid #334155;
    border-radius: 22px;
    padding: 30px 20px;
    min-height: 170px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    text-align: center;

    transition: 0.3s ease;
    box-shadow: 0 0 15px rgba(0,0,0,0.25);
}

.metric-card:hover{
    transform: translateY(-6px);
    border: 1px solid #ef4444;
    box-shadow: 0 0 20px rgba(239,68,68,0.25);
}

/* =========================
   CARD TITLE
========================= */
.metric-title{
    color: #94a3b8;
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 14px;
}

/* =========================
   CARD VALUE
========================= */
.metric-value{
    color: white;
    font-size: 30px;
    font-weight: 800;
}

/* =========================
   DATE
========================= */
.date-text{
    color: white;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 8px;
}

/* =========================
   TIME
========================= */
.time-text{
    color: #ef4444;
    font-size: 30px;
    font-weight: 900;
}

/* =========================
   ALERT
========================= */
.stAlert{
    border-radius: 15px;
}

/* =========================
   HIDE STREAMLIT
========================= */
#MainMenu,
footer,
header{
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# LOGO
# =========================================
col1, col2, col3 = st.columns([2,1,2])

with col2:
    st.image(
        str(logo_path),
        width=240
    )

# =========================================
# TITLE
# =========================================
st.markdown("""
<h1 class="main-title">
KLASIFIKASI LAYANAN SERVIS YAMAHA
</h1>
""", unsafe_allow_html=True)

# =========================================
# DESCRIPTION
# =========================================
st.markdown("""
<p class="desc">
Penerapan Algoritma Random Forest untuk klasifikasi layanan servis kendaraan Yamaha.
</p>
""", unsafe_allow_html=True)

# =========================================
# REALTIME CARD
# =========================================
placeholder = st.empty()

while True:

    now = datetime.now()

    hari_dict = {
        "Monday": "Senin",
        "Tuesday": "Selasa",
        "Wednesday": "Rabu",
        "Thursday": "Kamis",
        "Friday": "Jumat",
        "Saturday": "Sabtu",
        "Sunday": "Minggu"
    }

    hari = hari_dict[now.strftime("%A")]
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
                <span class="metric-title">Algoritma</span>
                <span class="metric-value">Random Forest</span>
            </div>
            """, unsafe_allow_html=True)

        # =========================================
        # CARD 2
        # =========================================
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <span class="metric-title">Dataset</span>
                <span class="metric-value">CSV File</span>
            </div>
            """, unsafe_allow_html=True)

        # =========================================
        # CARD 3
        # =========================================
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <span class="metric-title">Tanggal & Jam</span>

                <span class="date-text">
                    {tanggal}
                </span>

                <span class="time-text">
                    {jam}
                </span>
            </div>
            """, unsafe_allow_html=True)

        # =========================================
        # CARD 4
        # =========================================
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <span class="metric-title">Hari</span>
                <span class="metric-value">{hari}</span>
            </div>
            """, unsafe_allow_html=True)

    time.sleep(1)
