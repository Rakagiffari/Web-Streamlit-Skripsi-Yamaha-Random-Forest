import streamlit as st
from pathlib import Path
from PIL import Image

# ==========================================================
# PAGE CONFIG
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

foto_path = BASE_DIR.parent / "assets" / "foto.jpg"

page_icon = Image.open(foto_path)

st.set_page_config(
    page_title="Tentang Sistem",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="expanded"
)

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
STREAMLIT
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
TITLE
=================================================== */

.main-title{

    text-align:center;

    font-size:42px;

    font-weight:900;

    color:white;

    letter-spacing:1px;

    margin-top:10px;

    margin-bottom:20px;

}

/* ===================================================
DESCRIPTION
=================================================== */

.main-desc{

    color:#e2e8f0;

    text-align:justify;

    font-size:15px;

    line-height:1.8;

    max-width:1100px;

    margin:auto;

    margin-bottom:40px;

}

# ===================================================
# PROFILE CARD
# ===================================================

.profile-card{

    background:linear-gradient(145deg,#2d3142,#3b4255);

    border:1px solid rgba(255,255,255,.08);

    border-radius:22px;

    padding:28px;

    min-height:340px;

}

.tech-card{

    background:linear-gradient(145deg,#2d3142,#3b4255);

    border:1px solid rgba(255,255,255,.08);

    border-radius:22px;

    padding:28px;

    min-height:340px;

}

.card-title{

    color:white;

    font-size:22px;

    font-weight:700;

    margin-bottom:20px;

}

.biodata{

    color:white;

    font-size:15px;

    line-height:2.0;

}

.tech-item{

    background:#1f2937;

    padding:12px;

    border-radius:12px;

    margin-bottom:12px;

    color:white;

    font-size:15px;

    border:1px solid rgba(255,255,255,.05);

}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">

TENTANG SISTEM

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-desc">

Halaman ini menyajikan informasi mengenai penelitian,
tujuan pengembangan sistem, teknologi yang digunakan,
serta profil pengembang aplikasi.
Seluruh tampilan dirancang konsisten dengan halaman utama
agar memberikan pengalaman penggunaan yang nyaman,
modern, dan mudah dipahami.

</div>
""", unsafe_allow_html=True)

with left:

    st.markdown("""
    <div class="profile-card">
    """,unsafe_allow_html=True)

    foto,bio = st.columns([1,2])

    with foto:

        st.image(
            foto_path,
            use_container_width=True
        )

    with bio:

        st.markdown("""
        <div class="card-title">
        Profil Pengembang
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div class="biodata">

        <b>Nama</b><br>
        Raka Giffari Ramadhan

        <br><br>

        <b>NIM</b><br>
        22101152620332

        <br><br>

        <b>Program Studi</b><br>
        Teknik Informatika

        <br><br>

        <b>Universitas</b><br>
        Universitas Putra Indonesia "YPTK" Padang

        <br><br>

        <b>Email</b><br>
        giffari@email.com

        </div>
        """,unsafe_allow_html=True)

    st.markdown("</div>",unsafe_allow_html=True)

with right:

    st.markdown("""
    <div class="tech-card">

    <div class="card-title">
    Teknologi yang Digunakan
    </div>

    <div class="tech-item">
    🐍 Python
    </div>

    <div class="tech-item">
    🌲 Random Forest
    </div>

    <div class="tech-item">
    📊 Pandas
    </div>

    <div class="tech-item">
    📈 Scikit-Learn
    </div>

    <div class="tech-item">
    🎨 Streamlit
    </div>

    <div class="tech-item">
    📄 ReportLab
    </div>

    </div>
    """,unsafe_allow_html=True)
