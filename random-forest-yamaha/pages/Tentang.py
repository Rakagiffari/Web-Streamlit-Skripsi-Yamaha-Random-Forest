import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Tentang Sistem",
    page_icon="ℹ️",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.stApp{
    background:#05081b;
}

.block-container{
    max-width:1200px;
    padding-top:2rem;
    padding-bottom:2rem;
}

/* =============================== */

.title{

    text-align:center;
    color:white;
    font-size:42px;
    font-weight:700;

}

.desc{

    color:#E5E7EB;

    text-align:justify;

    font-size:20px;

    line-height:1.8;

    margin-top:15px;

    margin-bottom:35px;

}

/* =============================== */

.card{

    background:#3b3e4d;

    border-radius:28px;

    padding:30px;

    box-shadow:0 8px 25px rgba(0,0,0,.25);

    transition:.3s;

}

.card:hover{

    transform:translateY(-4px);

}

/* =============================== */

.profile{

    display:flex;

    align-items:center;

}

.photo{

    width:160px;

    height:210px;

    border-radius:25px;

    background:white;

}

.line{

    width:4px;

    height:210px;

    background:white;

    margin-left:35px;

    margin-right:35px;

}

.profile-text{

    color:white;

    font-size:22px;

    line-height:2.1;

}

/* =============================== */

.tech-title{

    color:white;

    text-align:center;

    font-size:28px;

    font-weight:700;

    margin-bottom:25px;

}

.tech{

    text-align:center;

    color:white;

    font-size:23px;

    line-height:2;

}

/* =============================== */

.section{

    margin-top:35px;

    background:#3b3e4d;

    border-radius:28px;

    padding:35px;

}

.section h2{

    color:white;

    text-align:center;

}

.section p{

    color:#E5E7EB;

    font-size:20px;

    text-align:justify;

    line-height:1.8;

}

/* =============================== */

.footer{

    text-align:center;

    color:#d1d5db;

    margin-top:35px;

    font-size:18px;

}

</style>
""", unsafe_allow_html=True)

# =====================================================
# JUDUL
# =====================================================

st.markdown(
    "<div class='title'>TENTANG SISTEM</div>",
    unsafe_allow_html=True
)

st.markdown("""
<div class='desc'>

Halaman ini menyajikan informasi mengenai penelitian,
tujuan pengembangan sistem, teknologi yang digunakan,
serta profil pengembang aplikasi. Seluruh desain halaman
dibuat konsisten dengan halaman utama sehingga pengguna
memperoleh pengalaman penggunaan yang nyaman dan mudah dipahami.

</div>
""", unsafe_allow_html=True)

# =====================================================
# CARD
# =====================================================

col1, col2 = st.columns([2,1], gap="large")

# =============================================

with col1:

    st.markdown("""

    <div class="card">

        <div class="profile">

            <div class="photo"></div>

            <div class="line"></div>

            <div class="profile-text">

            <b>Nama</b><br>
            Giffari

            <br>

            <b>NIM</b><br>
            20xxxxxxxx

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

# =============================================

with col2:

    st.markdown("""

    <div class="card">

    <div class="tech-title">

    Teknologi yang Digunakan

    </div>

    <div class="tech">

    🐍 Python

    <br>

    🌲 Random Forest

    <br>

    📊 Pandas

    <br>

    📈 Scikit-Learn

    <br>

    🎨 Streamlit

    <br>

    📄 ReportLab

    </div>

    </div>

    """, unsafe_allow_html=True)

# =====================================================
# TENTANG PENELITIAN
# =====================================================

st.markdown("""

<div class="section">

<h2>TENTANG PENELITIAN</h2>

<p>

Penelitian ini bertujuan membangun sistem klasifikasi layanan
servis sepeda motor Yamaha menggunakan algoritma Random Forest.
Sistem mampu melakukan proses unggah dataset, preprocessing,
pelatihan model, evaluasi performa, serta menghasilkan prediksi
layanan secara otomatis melalui aplikasi berbasis web.

</p>

</div>

""", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""

<div class="footer">

© 2026 Giffari &nbsp;&nbsp; | &nbsp;&nbsp;
Sistem Prediksi Layanan Servis Yamaha

</div>

""", unsafe_allow_html=True)
