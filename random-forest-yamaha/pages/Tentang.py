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
# BIODATA & TEKNOLOGI
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

# ---------- CSS ----------
st.markdown("""
<style>

.profile-card{
    background:#3b3d4d;
    border-radius:28px;
    padding:25px 28px;
    min-height:315px;
    border:1px solid rgba(255,255,255,.05);
    transition:.3s;
}

.profile-card:hover{
    transform:translateY(-5px);
    box-shadow:0 15px 35px rgba(0,0,0,.25);
}

.profile-wrapper{
    display:flex;
    align-items:center;
    gap:30px;
}

.profile-image{

    width:160px;
    height:220px;

    border-radius:22px;

    object-fit:cover;

    border:4px solid white;

}

.profile-divider{

    width:4px;
    height:235px;

    background:white;

    border-radius:10px;

}

.profile-info{

    color:white;

    font-size:18px;

    line-height:2.0;

}

.profile-info b{

    color:white;

}

.tech-card{

    background:#3b3d4d;

    border-radius:28px;

    padding:25px;

    min-height:315px;

    border:1px solid rgba(255,255,255,.05);

    transition:.3s;

}

.tech-card:hover{

    transform:translateY(-5px);

    box-shadow:0 15px 35px rgba(0,0,0,.25);

}

.tech-title{

    text-align:center;

    color:white;

    font-size:18px;

    font-weight:700;

    margin-bottom:25px;

}

.tech-grid{

    display:grid;

    grid-template-columns:1fr 1fr;

    gap:18px;

}

.tech-item{

    color:white;

    font-size:18px;

    text-align:center;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# LAYOUT
# ==========================================================

col1, col2 = st.columns([1.8,1.1], gap="large")

# ==========================================================
# CARD PROFIL
# ==========================================================

with col1:

    st.markdown('<div class="profile-card">', unsafe_allow_html=True)

    kiri, garis, kanan = st.columns([1,0.08,2])

    with kiri:
        st.image(
            str(foto_path),
            use_container_width=True
        )

    with garis:
        st.markdown("""
        <div class="profile-divider"></div>
        """, unsafe_allow_html=True)

    with kanan:

        st.markdown("""

<div class="profile-info">

<b>Nama</b><br>

<b>NIM</b><br>

<b>Program Studi</b><br>

<b>Universitas</b><br>

<b>Email</b>

</div>

""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# CARD TEKNOLOGI
# ==========================================================

with col2:

    st.markdown("""

<div class="tech-card">

<div class="tech-title">

Teknologi yang Digunakan

</div>

<div class="tech-grid">

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

</div>

""", unsafe_allow_html=True)
