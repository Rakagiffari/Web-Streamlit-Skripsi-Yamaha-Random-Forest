import streamlit as st
from pathlib import Path
from PIL import Image

# ==========================================================
# PAGE CONFIG
# ==========================================================

BASE_DIR = Path(__file__).parent

logo_path = BASE_DIR / "assets" / "yamaha_logo.png"
logo = Image.open(logo_path)

st.set_page_config(
    page_title="Tentang Sistem",
    page_icon=logo,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD CSS
# ==========================================================

st.markdown("""
<style>

/* ===================================================
GLOBAL
=================================================== */

html,
body,
[class*="css"]{
    font-family:"Segoe UI",sans-serif;
}

.stApp{
    background:#020617;
}

/* ===================================================
SIDEBAR
=================================================== */

section[data-testid="stSidebar"]{
    background:#0f172a;
    border-right:none;
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* ===================================================
HEADER
=================================================== */

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

#MainMenu{
    visibility:hidden;
}

/* ===================================================
CONTAINER
=================================================== */

.block-container{
    max-width:1400px;
    padding-top:1rem;
    padding-bottom:3rem;
}

/* ===================================================
MAIN TITLE
=================================================== */

.main-title{

    text-align:center;

    font-size:43px;

    font-weight:900;

    color:white;

    letter-spacing:1px;

    line-height:1.1;

    margin-top:5px;

    margin-bottom:15px;

}

/* ===================================================
SUBTITLE
=================================================== */

.subtitle{

    max-width:1000px;

    margin:auto;

    text-align:center;

    color:#cbd5e1;

    font-size:16px;

    line-height:1.9;

    margin-bottom:45px;

}

/* ===================================================
TITLE DIVIDER
=================================================== */

.title-divider{

    width:120px;

    height:4px;

    margin:auto;

    border-radius:30px;

    background:linear-gradient(
        90deg,
        #2563eb,
        #38bdf8
    );

    margin-bottom:60px;

}

/* ===================================================
SECTION TITLE
=================================================== */

.section-title{

    text-align:center;

    color:white;

    font-size:36px;

    font-weight:800;

}

/* ===================================================
CARD (Dipakai pada Part berikutnya)
=================================================== */

.card{

    background:linear-gradient(145deg,#111827,#1e293b);

    border:1px solid #334155;

    border-radius:22px;

    padding:30px;

    box-shadow:0 8px 25px rgba(0,0,0,.15);

    transition:.3s;

}

.card:hover{

    transform:translateY(-6px);

    box-shadow:0 0 20px rgba(239,68,68,.25);

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2.5,1,2.5])

with col2:
    st.image(str(logo_path), width=170)

st.markdown("""
<div class="main-title">
    TENTANG SISTEM
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">

Sistem ini dikembangkan sebagai implementasi algoritma <b>Random Forest</b>
untuk mengklasifikasikan layanan servis kendaraan Yamaha berdasarkan
pola data servis. Melalui proses preprocessing, feature engineering,
pelatihan model, evaluasi, hingga prediksi, sistem dirancang untuk
membantu proses analisis data secara lebih cepat, konsisten, dan mudah
dipahami.

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-divider"></div>
""", unsafe_allow_html=True)
