import streamlit as st
from pathlib import Path

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Tentang Sistem",
    page_icon="📘",
    layout="wide"
)

# ==========================================================
# ASSETS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
foto_path = BASE_DIR / "assets" / "foto.jpg"

# ==========================================================
# CSS
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

.block-container{
    padding-top:1rem;
    padding-bottom:3rem;
    max-width:1400px;
}

/* ===================================================
HEADER
=================================================== */

.main-title{
    text-align:center;
    font-size:43px;
    font-weight:900;
    color:white;
    letter-spacing:1px;
    margin-bottom:8px;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:15px;
    margin-bottom:40px;
}

/* ===================================================
CARD
=================================================== */

.info-card{

    background:linear-gradient(145deg,#111827,#1e293b);

    padding:28px;

    border-radius:22px;

    border:1px solid #334155;

    transition:.35s;

    box-shadow:0 5px 15px rgba(0,0,0,.08);

}

.info-card:hover{

    transform:translateY(-6px);

    box-shadow:0 0 20px rgba(239,68,68,.25);

}

/* ===================================================
TITLE
=================================================== */

.card-title{

    color:white;

    font-size:24px;

    font-weight:700;

    margin-bottom:20px;

    text-align:center;

}

/* ===================================================
TEXT
=================================================== */

.card-text{

    color:#d1d5db;

    font-size:16px;

    line-height:1.9;

}

/* ===================================================
SECTION TITLE
=================================================== */

.section-title{

    text-align:center;

    color:white;

    font-size:38px;

    font-weight:800;

    margin-top:25px;

    margin-bottom:8px;

}

.section-desc{

    text-align:center;

    color:#94a3b8;

    font-size:15px;

    margin-bottom:35px;

}

/* ===================================================
FOOTER
=================================================== */

.footer{

    text-align:center;

    color:#64748b;

    font-size:12px;

    line-height:1.8;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<div class="main-title">

TENTANG SISTEM

</div>

<div class="subtitle">

Informasi mengenai pengembang, penelitian,
serta teknologi yang digunakan dalam
Sistem Klasifikasi Layanan Servis Yamaha.

</div>

""", unsafe_allow_html=True)
