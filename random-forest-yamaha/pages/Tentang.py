import streamlit as st
from pathlib import Path
from PIL import Image

# ==========================================================
# PAGE CONFIG
# ==========================================================

from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent

foto_path = BASE_DIR.parent / "assets" / "foto.jpg"

import base64

with open(foto_path, "rb") as image_file:
    foto_base64 = base64.b64encode(image_file.read()).decode("utf-8")

page_icon = None

if foto_path.exists():
    page_icon = Image.open(foto_path)

st.set_page_config(
    page_title="Tentang Sistem",
    page_icon=page_icon,
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

# ==========================================================
# PROFIL & TEKNOLOGI
# ==========================================================

st.markdown("""

<style>

.about-wrapper{

    display:flex;

    gap:35px;

    align-items:stretch;

    margin-top:20px;

}

.profile-card{

    flex:1.8;

    background:#3b3d4d;

    border-radius:30px;

    padding:28px;

    display:flex;

    align-items:center;

    transition:.3s;

}

.profile-card:hover{

    transform:translateY(-5px);

}

.profile-photo{

    width:160px;

    height:220px;

    object-fit:cover;

    border-radius:20px;

    border:4px solid white;

}

.profile-divider{

    width:4px;

    height:230px;

    background:white;

    margin:0px 28px;

    border-radius:20px;

}

.profile-info{

    color:white;

    font-size:18px;

    line-height:2.2;

}

.profile-info b{

    display:inline-block;

    width:170px;

}

.tech-card{

    flex:1;

    background:#3b3d4d;

    border-radius:30px;

    padding:30px;

    transition:.3s;

}

.tech-card:hover{

    transform:translateY(-5px);

}

.tech-title{

    color:white;

    text-align:center;

    font-size:18px;

    font-weight:bold;

    margin-bottom:30px;

}

.tech-grid{

    display:grid;

    grid-template-columns:1fr 1fr;

    gap:20px;

}

.tech-item{

    color:white;

    font-size:18px;

    text-align:center;

}

</style>

""", unsafe_allow_html=True)

st.markdown(f"""

<div class="about-wrapper">

    <div class="profile-card">

        <img class="profile-photo"
        src="data:image/jpeg;base64,{foto_base64}">

        <div class="profile-divider"></div>

        <div class="profile-info">

            <b>Nama</b> : Raka Giffari Ramadhan<br>

            <b>NIM</b> : 22101152620332<br>

            <b>Program Studi</b> : Teknik Informatika<br>

            <b>Universitas</b> : UPI "YPTK" Padang<br>

            <b>Email</b> : giffari@email.com

        </div>

    </div>

    <div class="tech-card">

        <div class="tech-title">

            Teknologi yang Digunakan

        </div>

        <div class="tech-grid">

            <div class="tech-item">🐍 Python</div>

            <div class="tech-item">🌲 Random Forest</div>

            <div class="tech-item">📊 Pandas</div>

            <div class="tech-item">📈 Scikit-Learn</div>

            <div class="tech-item">🎨 Streamlit</div>

            <div class="tech-item">📄 ReportLab</div>

        </div>

    </div>

</div>

""", unsafe_allow_html=True)
