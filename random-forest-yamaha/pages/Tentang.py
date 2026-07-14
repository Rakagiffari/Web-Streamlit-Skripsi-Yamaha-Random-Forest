import streamlit as st
from pathlib import Path
import base64

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Tentang Sistem",
    page_icon="📘",
    layout="wide"
)

# ==========================================================
# PATH PROJECT
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================================
# FOTO PROFIL
# ==========================================================

FOTO_PATH = BASE_DIR / "assets" / "foto.jpg"

def load_image_base64(path):

    if not path.exists():
        return ""

    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

foto = load_image_base64(FOTO_PATH)

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

.stApp{
    background:#050817;
}

.block-container{

    max-width:1200px;

    padding-top:2rem;

    padding-bottom:2rem;

}

/* ==========================
TITLE
========================== */

.title{

    text-align:center;

    color:white;

    font-size:40px;

    font-weight:700;

    margin-bottom:12px;

}

.description{

    color:#d1d5db;

    font-size:19px;

    line-height:1.8;

    text-align:justify;

    margin-bottom:35px;

}

/* ==========================
CARD
========================== */

.card{

    background:#3b3e4d;

    border-radius:28px;

    padding:30px;

    transition:.35s;

    box-shadow:0 8px 25px rgba(0,0,0,.25);

}

.card:hover{

    transform:translateY(-5px);

    box-shadow:0 15px 35px rgba(0,0,0,.35);

}

/* ==========================
PROFILE
========================== */

.profile{

    display:flex;

    align-items:center;

}

.photo{

    width:165px;

    height:210px;

    border-radius:22px;

    overflow:hidden;

    border:3px solid white;

    flex-shrink:0;

    background:white;

}

.photo img{

    width:100%;

    height:100%;

    object-fit:cover;

}

.line{

    width:4px;

    height:215px;

    background:white;

    margin-left:35px;

    margin-right:35px;

}

.profile-text{

    color:white;

    font-size:20px;

    line-height:2;

}

/* ==========================
TECH
========================== */

.tech-title{

    color:white;

    text-align:center;

    font-size:28px;

    font-weight:bold;

    margin-bottom:25px;

}

.tech{

    color:white;

    text-align:center;

    font-size:21px;

    line-height:2;

}

/* ==========================
SECTION
========================== */

.section{

    background:#3b3e4d;

    border-radius:28px;

    padding:35px;

    margin-top:35px;

}

.section-title{

    text-align:center;

    color:white;

    font-size:34px;

    font-weight:700;

}

.section-text{

    color:#d1d5db;

    font-size:19px;

    line-height:1.8;

    text-align:justify;

}

/* ==========================
FOOTER
========================== */

.footer{

    color:#cbd5e1;

    text-align:center;

    margin-top:40px;

    font-size:18px;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""
<div class="title">
    TENTANG SISTEM
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="description">

Halaman ini menyajikan informasi mengenai sistem klasifikasi
layanan servis sepeda motor Yamaha menggunakan algoritma
<b>Random Forest</b>. Selain informasi penelitian, halaman
ini juga menampilkan profil pengembang dan teknologi yang
digunakan dalam membangun aplikasi.

</div>
""", unsafe_allow_html=True)

# ==========================================================
# FOTO HTML
# ==========================================================

if foto:
    foto_html = f"""
    <img src="data:image/jpeg;base64,{foto}">
    """
else:
    foto_html = """
    <div style="
        width:100%;
        height:100%;
        display:flex;
        justify-content:center;
        align-items:center;
        font-size:26px;
        color:#64748b;
        font-weight:bold;
    ">
        FOTO
    </div>
    """

# ==========================================================
# BIODATA & TEKNOLOGI
# ==========================================================

left, right = st.columns([2, 1], gap="large")

# ==========================================================
# CARD BIODATA
# ==========================================================

with left:

    st.markdown(f"""

    <div class="card">

        <div class="profile">

            <div class="photo">

                {foto_html}

            </div>

            <div class="line"></div>

            <div class="profile-text">

                <b>Nama</b><br>
                Giffari

                <br>

                <b>NIM</b><br>
                20XXXXXXXX

                <br>

                <b>Program Studi</b><br>
                Sistem Informasi

                <br>

                <b>Universitas</b><br>
                Universitas Muhammadiyah Kalimantan Timur

                <br>

                <b>Email</b><br>
                giffari@email.com

            </div>

        </div>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# CARD TEKNOLOGI
# ==========================================================

with right:

    st.markdown("""

    <div class="card">

        <div class="tech-title">

            Teknologi yang Digunakan

        </div>

        <div class="tech">

            🐍 Python <br><br>

            🌲 Random Forest <br><br>

            📊 Pandas <br><br>

            🤖 Scikit-Learn <br><br>

            🎈 Streamlit <br><br>

            📄 ReportLab

        </div>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# TENTANG PENELITIAN
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""

<div class="section">

    <div class="section-title">

        TENTANG PENELITIAN

    </div>

    <br>

    <div class="section-text">

Penelitian ini bertujuan mengembangkan sistem klasifikasi layanan
servis sepeda motor Yamaha menggunakan algoritma
<b>Random Forest</b>. Sistem dibangun berbasis web menggunakan
framework <b>Streamlit</b> sehingga pengguna dapat melakukan
proses upload dataset, preprocessing, feature engineering,
pelatihan model, evaluasi, hingga memperoleh hasil prediksi
secara otomatis dalam satu aplikasi.

<br><br>

Aplikasi ini diharapkan dapat membantu proses analisis data
layanan servis menjadi lebih cepat, konsisten, dan mudah
digunakan baik untuk kebutuhan penelitian maupun pengembangan
lebih lanjut.

    </div>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# INFORMASI PENELITIAN
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

# ==========================================================
# ALGORITMA
# ==========================================================

with col1:

    st.markdown("""

    <div class="card">

        <div style="font-size:55px;text-align:center;">
            🌲
        </div>

        <h3 style="text-align:center;color:white;">
            Random Forest
        </h3>

        <p style="
            color:#d1d5db;
            text-align:center;
            line-height:1.8;
            font-size:16px;
        ">

        Algoritma Random Forest digunakan
        sebagai model klasifikasi untuk
        memprediksi kategori layanan servis
        berdasarkan data historis.

        </p>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# DATASET
# ==========================================================

with col2:

    st.markdown("""

    <div class="card">

        <div style="font-size:55px;text-align:center;">
            📊
        </div>

        <h3 style="text-align:center;color:white;">
            Dataset
        </h3>

        <p style="
            color:#d1d5db;
            text-align:center;
            line-height:1.8;
            font-size:16px;
        ">

        Dataset layanan servis Yamaha
        diproses melalui preprocessing,
        feature engineering, encoding,
        serta pembagian data latih
        dan data uji.

        </p>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# SISTEM
# ==========================================================

with col3:

    st.markdown("""

    <div class="card">

        <div style="font-size:55px;text-align:center;">
            💻
        </div>

        <h3 style="text-align:center;color:white;">
            Sistem
        </h3>

        <p style="
            color:#d1d5db;
            text-align:center;
            line-height:1.8;
            font-size:16px;
        ">

        Sistem menyediakan proses
        upload dataset, pelatihan
        model Random Forest,
        evaluasi performa,
        dan visualisasi hasil.

        </p>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# RINGKASAN SISTEM
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    INFORMASI APLIKASI
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4, gap="large")

# ==========================================================
# CARD 1
# ==========================================================

with col1:

    st.markdown("""

    <div class="card" style="text-align:center;min-height:220px;">

        <div style="font-size:55px;">🌲</div>

        <h3 style="color:white;margin-top:10px;">
            Algoritma
        </h3>

        <p style="
            color:#d1d5db;
            line-height:1.8;
            font-size:16px;
        ">

        Random Forest digunakan
        sebagai model klasifikasi
        layanan servis.

        </p>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# CARD 2
# ==========================================================

with col2:

    st.markdown("""

    <div class="card" style="text-align:center;min-height:220px;">

        <div style="font-size:55px;">📊</div>

        <h3 style="color:white;margin-top:10px;">
            Dataset
        </h3>

        <p style="
            color:#d1d5db;
            line-height:1.8;
            font-size:16px;
        ">

        Dataset histori layanan
        servis Yamaha yang telah
        diproses melalui
        preprocessing.

        </p>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# CARD 3
# ==========================================================

with col3:

    st.markdown("""

    <div class="card" style="text-align:center;min-height:220px;">

        <div style="font-size:55px;">💻</div>

        <h3 style="color:white;margin-top:10px;">
            Platform
        </h3>

        <p style="
            color:#d1d5db;
            line-height:1.8;
            font-size:16px;
        ">

        Web Application
        menggunakan
        Streamlit Framework.

        </p>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# CARD 4
# ==========================================================

with col4:

    st.markdown("""

    <div class="card" style="text-align:center;min-height:220px;">

        <div style="font-size:55px;">⚙️</div>

        <h3 style="color:white;margin-top:10px;">
            Versi
        </h3>

        <p style="
            color:#d1d5db;
            line-height:1.8;
            font-size:16px;
        ">

        Version 1.0

        <br>

        Tahun 2026

        </p>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# GARIS PEMBATAS
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<hr style="
border:1px solid rgba(255,255,255,.10);
margin-top:10px;
margin-bottom:25px;
">
""", unsafe_allow_html=True)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("""

<div class="footer">

<div style="
font-size:22px;
font-weight:700;
color:white;
margin-bottom:10px;
">

Sistem Klasifikasi Layanan Servis Yamaha

</div>

<div style="
font-size:17px;
line-height:1.8;
">

Dikembangkan sebagai implementasi penelitian
menggunakan algoritma <b>Random Forest</b>
untuk membantu proses klasifikasi layanan
servis sepeda motor Yamaha.

</div>

<br>

<div style="
font-size:15px;
color:#9ca3af;
">

© 2026 Giffari | Universitas Muhammadiyah Kalimantan Timur

</div>

</div>

""", unsafe_allow_html=True)
