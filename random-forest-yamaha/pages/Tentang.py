import streamlit as st
from pathlib import Path
from PIL import Image

# ==========================================================
# PAGE CONFIG
# ==========================================================

BASE_DIR = Path(__file__).parent

foto_path = BASE_DIR / "assets" / "foto.jpg"

foto = Image.open(foto_path)

st.set_page_config(
    page_title="Tentang Sistem",
    page_icon=foto,
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
HEADER STREAMLIT
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
    padding-top:1rem;
    padding-bottom:3rem;
    max-width:1400px;
}

/* ===================================================
TITLE
=================================================== */

.main-title{

    text-align:center;
    color:white;

    font-size:42px;
    font-weight:900;

    letter-spacing:1px;

    margin-top:5px;
    margin-bottom:18px;

}

.subtitle{

    color:#e2e8f0;

    font-size:15px;

    text-align:justify;

    line-height:1.8;

    max-width:1100px;

    margin:auto;

    margin-bottom:40px;

}

/* ===================================================
CARD
=================================================== */

.card{

    background:#3b3d4d;

    border-radius:28px;

    padding:28px;

    border:1px solid rgba(255,255,255,.05);

    transition:.3s;

}

.card:hover{

    transform:translateY(-5px);

    box-shadow:0 15px 35px rgba(0,0,0,.25);

}

/* ===================================================
FOOTER
=================================================== */

.footer{

    text-align:center;

    color:#d1d5db;

    font-size:15px;

    margin-top:45px;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# JUDUL HALAMAN
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""

<div class="main-title">

TENTANG SISTEM

</div>

""", unsafe_allow_html=True)

st.markdown("""

<div class="subtitle">

Halaman ini menyajikan informasi mengenai penelitian,
tujuan pengembangan sistem, teknologi yang digunakan,
serta profil pengembang aplikasi.
Seluruh desain halaman dibuat konsisten dengan halaman utama
sehingga pengguna memperoleh pengalaman penggunaan
yang nyaman dan mudah dipahami.

</div>

""", unsafe_allow_html=True)
