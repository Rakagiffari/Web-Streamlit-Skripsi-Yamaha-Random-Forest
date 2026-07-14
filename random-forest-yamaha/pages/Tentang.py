import streamlit as st
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
# LOAD FOTO
# ==========================================================

def get_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

# Ganti sesuai lokasi foto
foto = get_base64("assets/foto.jpg")


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
JUDUL
========================== */

.title{

    text-align:center;
    color:white;
    font-size:42px;
    font-weight:700;
    margin-bottom:10px;

}

.description{

    color:#d1d5db;
    font-size:20px;
    line-height:1.8;
    text-align:justify;
    margin-bottom:35px;

}

/* ==========================
CARD
========================== */

.card{

    background:#3a3d4d;

    border-radius:28px;

    padding:30px;

    box-shadow:0 8px 25px rgba(0,0,0,.25);

    transition:0.3s;

}

.card:hover{

    transform:translateY(-5px);

    box-shadow:0 15px 40px rgba(0,0,0,.35);

}

/* ==========================
PROFILE
========================== */

.profile{

    display:flex;

    align-items:center;

}

/* FOTO */

.photo{

    width:160px;

    height:210px;

    border-radius:22px;

    overflow:hidden;

    border:3px solid white;

    flex-shrink:0;

}

.photo img{

    width:100%;

    height:100%;

    object-fit:cover;

}

/* GARIS */

.line{

    width:4px;

    height:210px;

    background:white;

    margin-left:35px;

    margin-right:35px;

}

/* TEXT */

.profile-text{

    color:white;

    font-size:20px;

    line-height:2.0;

}

/* ==========================
TEKNOLOGI
========================== */

.tech-title{

    text-align:center;

    color:white;

    font-size:28px;

    font-weight:bold;

    margin-bottom:25px;

}

.tech{

    text-align:center;

    color:white;

    font-size:21px;

    line-height:2;

}

/* ==========================
SECTION
========================== */

.section{

    background:#3a3d4d;

    border-radius:28px;

    padding:35px;

    margin-top:35px;

}

.section-title{

    text-align:center;

    color:white;

    font-size:34px;

    font-weight:700;

    margin-bottom:20px;

}

.section-text{

    color:#E5E7EB;

    font-size:19px;

    line-height:1.9;

    text-align:justify;

}

/* ==========================
FOOTER
========================== */

.footer{

    color:#cbd5e1;

    text-align:center;

    margin-top:35px;

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

Halaman ini menyajikan informasi mengenai sistem klasifikasi layanan
servis sepeda motor Yamaha menggunakan algoritma <b>Random Forest</b>.
Selain informasi mengenai penelitian, halaman ini juga menampilkan
profil pengembang serta teknologi yang digunakan dalam membangun
aplikasi berbasis web.

</div>
""", unsafe_allow_html=True)

# ==========================================================
# BIODATA & TEKNOLOGI
# ==========================================================

left, right = st.columns([2,1], gap="large")

# ==========================================================
# CARD BIODATA
# ==========================================================

with left:

    st.markdown(f"""

    <div class="card">

        <div class="profile">

            <div class="photo">

                <img src="data:image/png;base64,{foto}">

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

            🐍 Python

            <br><br>

            🌲 Random Forest

            <br><br>

            📊 Pandas

            <br><br>

            🤖 Scikit-Learn

            <br><br>

            🎈 Streamlit

            <br><br>

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
        📖 Tentang Penelitian
    </div>

    <div class="section-text">

    Penelitian ini berjudul <b>
    "Penerapan Algoritma Random Forest untuk Mengklasifikasi
    Layanan Servis pada Yamaha"
    </b>.
    <br><br>

    Sistem dikembangkan sebagai implementasi algoritma
    <b>Random Forest</b> untuk membantu proses klasifikasi
    layanan servis sepeda motor Yamaha berdasarkan data historis.
    Seluruh proses dilakukan secara otomatis mulai dari
    pengunggahan dataset, preprocessing, feature engineering,
    pelatihan model, evaluasi performa, hingga menghasilkan
    prediksi layanan servis.

    <br><br>

    <b>Tujuan Penelitian</b>

    <ul>

        <li>
        Mengembangkan sistem klasifikasi layanan servis
        berbasis Machine Learning.
        </li>

        <li>
        Mengimplementasikan algoritma Random Forest
        sebagai metode klasifikasi.
        </li>

        <li>
        Membantu proses analisis data layanan servis
        secara lebih cepat, konsisten, dan efisien.
        </li>

    </ul>

    </div>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# INFORMASI PENELITIAN
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

# ----------------------------------------------------------

with col1:

    st.markdown("""

    <div class="card">

        <div style="text-align:center;font-size:55px;">
        🌲
        </div>

        <div class="tech-title">

        Algoritma

        </div>

        <div class="section-text" style="text-align:center;">

        Random Forest digunakan sebagai
        metode klasifikasi utama karena
        mampu menghasilkan performa yang
        baik pada data penelitian.

        </div>

    </div>

    """, unsafe_allow_html=True)

# ----------------------------------------------------------

with col2:

    st.markdown("""

    <div class="card">

        <div style="text-align:center;font-size:55px;">
        📊
        </div>

        <div class="tech-title">

        Dataset

        </div>

        <div class="section-text" style="text-align:center;">

        Dataset berisi data historis
        layanan servis sepeda motor Yamaha
        yang telah melalui proses
        preprocessing dan feature engineering.

        </div>

    </div>

    """, unsafe_allow_html=True)

# ----------------------------------------------------------

with col3:

    st.markdown("""

    <div class="card">

        <div style="text-align:center;font-size:55px;">
        💻
        </div>

        <div class="tech-title">

        Output Sistem

        </div>

        <div class="section-text" style="text-align:center;">

        Sistem menghasilkan model
        klasifikasi beserta evaluasi
        performa dan prediksi layanan
        servis secara otomatis.

        </div>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# RINGKASAN SISTEM
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    🚀 Ringkasan Sistem
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4, gap="large")

# ==========================================================
# CARD 1
# ==========================================================

with col1:

    st.markdown("""

    <div class="card" style="text-align:center; min-height:220px;">

        <div style="font-size:55px;">
        🌲
        </div>

        <h3 style="color:white;">
        Algoritma
        </h3>

        <div class="section-text"
             style="text-align:center;font-size:17px;">

        Random Forest

        </div>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# CARD 2
# ==========================================================

with col2:

    st.markdown("""

    <div class="card" style="text-align:center; min-height:220px;">

        <div style="font-size:55px;">
        💻
        </div>

        <h3 style="color:white;">
        Platform
        </h3>

        <div class="section-text"
             style="text-align:center;font-size:17px;">

        Web Application
        <br>
        Streamlit

        </div>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# CARD 3
# ==========================================================

with col3:

    st.markdown("""

    <div class="card" style="text-align:center; min-height:220px;">

        <div style="font-size:55px;">
        🐍
        </div>

        <h3 style="color:white;">
        Bahasa
        </h3>

        <div class="section-text"
             style="text-align:center;font-size:17px;">

        Python

        </div>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# CARD 4
# ==========================================================

with col4:

    st.markdown("""

    <div class="card" style="text-align:center; min-height:220px;">

        <div style="font-size:55px;">
        📦
        </div>

        <h3 style="color:white;">
        Versi
        </h3>

        <div class="section-text"
             style="text-align:center;font-size:17px;">

        Version 1.0

        </div>

    </div>

    """, unsafe_allow_html=True)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<hr style="border:1px solid rgba(255,255,255,.12);">
""", unsafe_allow_html=True)

st.markdown("""

<div class="footer">

<h3 style="color:white; margin-bottom:8px;">

Sistem Klasifikasi Layanan Servis Yamaha

</h3>

<div style="font-size:17px;">

Dikembangkan sebagai implementasi penelitian menggunakan
algoritma <b>Random Forest</b> untuk membantu proses
klasifikasi layanan servis sepeda motor Yamaha.

<br><br>

© 2026 Giffari • Universitas Muhammadiyah Kalimantan Timur

</div>

</div>

""", unsafe_allow_html=True)
