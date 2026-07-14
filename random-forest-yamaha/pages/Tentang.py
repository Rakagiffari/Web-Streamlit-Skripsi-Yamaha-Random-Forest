import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="Tentang Sistem",
    page_icon="📘",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================
st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1250px;
}

/* Background */

.stApp{
    background:#0f172a;
}

/* Section Title */

.section-title{
    text-align:center;
    font-size:34px;
    font-weight:700;
    color:white;
    margin-bottom:10px;
}

.section-subtitle{
    text-align:center;
    color:#94a3b8;
    font-size:17px;
    margin-bottom:35px;
}

/* Hero */

.hero-card{
    background:linear-gradient(145deg,#111827,#1e293b);
    padding:45px;
    border-radius:22px;
    border:1px solid rgba(255,255,255,.08);
    box-shadow:0 8px 35px rgba(0,0,0,.35);
    margin-bottom:35px;
}

.hero-title{
    color:white;
    font-size:42px;
    font-weight:700;
    margin-bottom:12px;
}

.hero-text{
    color:#cbd5e1;
    font-size:18px;
    line-height:1.8;
}

.version-badge{
    display:inline-block;
    margin-top:22px;
    padding:8px 18px;
    background:#2563eb;
    color:white;
    border-radius:999px;
    font-size:14px;
    font-weight:600;
}

/* Card */

.info-card{
    background:linear-gradient(145deg,#111827,#1e293b);
    border:1px solid rgba(255,255,255,.08);
    border-radius:20px;
    padding:28px;
    box-shadow:0 6px 20px rgba(0,0,0,.25);
    transition:.35s;
    height:100%;
}

.info-card:hover{

    transform:translateY(-6px);

    box-shadow:0 15px 35px rgba(37,99,235,.20);

    border:1px solid rgba(96,165,250,.45);

}

.card-icon{
    font-size:40px;
    margin-bottom:10px;
}

.card-title{
    color:white;
    font-size:24px;
    font-weight:700;
    margin-bottom:18px;
}

.card-text{
    color:#cbd5e1;
    font-size:16px;
    line-height:1.8;
}

.card-list{

    color:#d1d5db;

    line-height:2;

    font-size:16px;

}

.divider{

    margin:55px 0 35px;

    border-top:1px solid rgba(255,255,255,.08);

}

.footer{

    text-align:center;

    color:#94a3b8;

    padding:30px 0;

    font-size:14px;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HERO
# ==========================================================

st.markdown("""

<div class="hero-card">

<div class="hero-title">

📘 Sistem Klasifikasi Layanan Servis Yamaha

</div>

<div class="hero-text">

Aplikasi ini dikembangkan sebagai implementasi penelitian
mengenai klasifikasi layanan servis sepeda motor Yamaha
menggunakan pendekatan Machine Learning.

Sistem menyediakan proses pengolahan data mulai dari
unggah dataset, preprocessing, pelatihan model hingga
evaluasi hasil secara otomatis melalui antarmuka web yang
interaktif dan mudah digunakan.

</div>

<div class="version-badge">

Version 1.0

</div>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# PENELITIAN & DESKRIPSI SISTEM
# ==========================================================

col1, col2 = st.columns([1, 1], gap="large")

# ----------------------------------------------------------
# CARD 1
# ----------------------------------------------------------
with col1:

    st.markdown("""
    <div class="info-card">

        <div class="card-icon">🎓</div>

        <div class="card-title">
            Informasi Penelitian
        </div>

        <div class="card-list">

        <b>Judul</b><br>
        Penerapan Algoritma Random Forest untuk
        Mengklasifikasi Layanan Servis pada Yamaha

        <br><br>

        <b>Metode</b><br>
        Random Forest Classification

        <br><br>

        <b>Platform</b><br>
        Aplikasi Berbasis Web (Streamlit)

        <br><br>

        <b>Tujuan</b><br>
        Mengembangkan sistem yang mampu
        membantu proses klasifikasi layanan
        servis berdasarkan data historis.

        </div>

    </div>
    """, unsafe_allow_html=True)


# ----------------------------------------------------------
# CARD 2
# ----------------------------------------------------------
with col2:

    st.markdown("""
    <div class="info-card">

        <div class="card-icon">📖</div>

        <div class="card-title">
            Deskripsi Sistem
        </div>

        <div class="card-text">

        Sistem ini dirancang untuk mengotomatisasi proses
        klasifikasi layanan servis sepeda motor Yamaha
        menggunakan pendekatan Machine Learning.

        <br><br>

        Pengguna dapat mengunggah dataset, melakukan
        preprocessing data, melatih model klasifikasi,
        melakukan evaluasi performa model, hingga
        memperoleh hasil prediksi secara terintegrasi
        dalam satu aplikasi.

        <br><br>

        Seluruh proses dirancang dengan antarmuka yang
        sederhana, responsif, dan mudah digunakan
        sehingga dapat membantu proses analisis data
        secara lebih efisien.

        </div>

    </div>
    """, unsafe_allow_html=True)

# ==========================================================
# TEKNOLOGI YANG DIGUNAKAN
# ==========================================================

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    ⚙️ Teknologi yang Digunakan
</div>

<div class="section-subtitle">
Library dan framework yang digunakan dalam pengembangan sistem.
</div>
""", unsafe_allow_html=True)


# ==========================================================
# BARIS PERTAMA
# ==========================================================

col1, col2, col3 = st.columns(3, gap="large")

with col1:

    st.markdown("""
    <div class="info-card" style="text-align:center;">

        <div style="font-size:55px;">🐍</div>

        <div class="card-title">
            Python
        </div>

        <div class="card-text">
            Bahasa pemrograman utama yang digunakan
            untuk membangun sistem.
        </div>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="info-card" style="text-align:center;">

        <div style="font-size:55px;">🎈</div>

        <div class="card-title">
            Streamlit
        </div>

        <div class="card-text">
            Framework web yang digunakan
            untuk membangun antarmuka aplikasi.
        </div>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="info-card" style="text-align:center;">

        <div style="font-size:55px;">🤖</div>

        <div class="card-title">
            Scikit-Learn
        </div>

        <div class="card-text">
            Library Machine Learning
            untuk proses klasifikasi model.
        </div>

    </div>
    """, unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)


# ==========================================================
# BARIS KEDUA
# ==========================================================

col4, col5, col6 = st.columns(3, gap="large")

with col4:

    st.markdown("""
    <div class="info-card" style="text-align:center;">

        <div style="font-size:55px;">🐼</div>

        <div class="card-title">
            Pandas
        </div>

        <div class="card-text">
            Digunakan untuk membaca,
            mengolah, dan memanipulasi dataset.
        </div>

    </div>
    """, unsafe_allow_html=True)

with col5:

    st.markdown("""
    <div class="info-card" style="text-align:center;">

        <div style="font-size:55px;">📊</div>

        <div class="card-title">
            Plotly
        </div>

        <div class="card-text">
            Digunakan untuk membuat visualisasi
            data yang interaktif.
        </div>

    </div>
    """, unsafe_allow_html=True)

with col6:

    st.markdown("""
    <div class="info-card" style="text-align:center;">

        <div style="font-size:55px;">📄</div>

        <div class="card-title">
            OpenPyXL
        </div>

        <div class="card-text">
            Mendukung pembacaan
            dan pengolahan file Excel.
        </div>

    </div>
    """, unsafe_allow_html=True)
