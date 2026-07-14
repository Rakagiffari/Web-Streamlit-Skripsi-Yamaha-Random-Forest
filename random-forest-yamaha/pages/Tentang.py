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
# CSS
# ==========================================================
st.markdown("""
<style>

.stApp{
    background:#0f172a;
}

.block-container{
    max-width:1250px;
    padding-top:2rem;
    padding-bottom:2rem;
}

/* HERO */

.hero{

    background:linear-gradient(135deg,#111827,#1e293b);

    border-radius:22px;

    padding:55px;

    border:1px solid rgba(255,255,255,.08);

    box-shadow:0 12px 35px rgba(0,0,0,.35);

    margin-bottom:45px;

}

.hero h1{

    color:white;

    font-size:46px;

    font-weight:700;

    margin-bottom:15px;

}

.hero p{

    color:#cbd5e1;

    font-size:18px;

    line-height:1.9;

    margin-bottom:28px;

}

.badge{

    display:inline-block;

    background:#2563eb;

    color:white;

    padding:8px 20px;

    border-radius:999px;

    font-weight:600;

    font-size:14px;

}

/* SECTION */

.section-title{

    color:white;

    text-align:center;

    font-size:34px;

    font-weight:700;

    margin-top:20px;

    margin-bottom:10px;

}

.section-subtitle{

    color:#94a3b8;

    text-align:center;

    font-size:17px;

    margin-bottom:35px;

}

/* CARD */

.card{

    background:linear-gradient(145deg,#111827,#1e293b);

    border-radius:20px;

    border:1px solid rgba(255,255,255,.08);

    padding:28px;

    transition:.35s;

    box-shadow:0 8px 20px rgba(0,0,0,.25);

}

.card:hover{

    transform:translateY(-6px);

    border-color:#3b82f6;

    box-shadow:0 15px 35px rgba(59,130,246,.25);

}

.card h3{

    color:white;

    margin-bottom:18px;

}

.card p{

    color:#cbd5e1;

    line-height:1.8;

}

.divider{

    border-top:1px solid rgba(255,255,255,.08);

    margin:55px 0;

}
/* Card Title */

h3{

    color:white !important;

    font-weight:700 !important;

}

/* Caption */

[data-testid="stCaptionContainer"]{

    color:#60a5fa !important;

    font-size:14px;

    margin-bottom:10px;

}

/* Paragraph */

[data-testid="stMarkdownContainer"] p{

    color:#d1d5db;

    line-height:1.8;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HERO
# ==========================================================

st.markdown("""
<div class="hero">

<h1>📘 Sistem Klasifikasi Layanan Servis Yamaha</h1>

<p>

Aplikasi ini merupakan implementasi penelitian yang bertujuan
mengklasifikasikan layanan servis sepeda motor Yamaha
menggunakan algoritma <b>Random Forest</b>. Sistem dibangun
untuk mempermudah proses pengolahan data, pelatihan model,
hingga evaluasi hasil melalui antarmuka web yang interaktif.

</p>

<span class="badge">
Version 1.0
</span>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# TENTANG SISTEM
# ==========================================================

st.markdown("""
<div class="section-title">
    Tentang Sistem
</div>

<div class="section-subtitle">
Informasi mengenai penelitian dan sistem yang dikembangkan.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,1], gap="large")

# ==========================================================
# CARD KIRI
# ==========================================================

with col1:

    with st.container(border=True):

        st.markdown("## 🎓 Informasi Penelitian")

        st.markdown("---")

        st.markdown("**Judul Penelitian**")
        st.write(
            "Penerapan Algoritma Random Forest untuk "
            "Mengklasifikasi Layanan Servis pada Yamaha."
        )

        st.markdown("**Metode**")
        st.write("Random Forest Classification")

        st.markdown("**Platform**")
        st.write("Aplikasi Web berbasis Streamlit")

        st.markdown("**Tujuan Penelitian**")
        st.write(
            "Membangun sistem yang mampu membantu proses "
            "klasifikasi layanan servis secara otomatis "
            "berdasarkan data historis."
        )

# ==========================================================
# CARD KANAN
# ==========================================================

with col2:

    with st.container(border=True):

        st.markdown("## 📖 Deskripsi Sistem")

        st.markdown("---")

        st.write(
            """
            Sistem ini dirancang untuk membantu proses
            klasifikasi layanan servis sepeda motor Yamaha
            menggunakan pendekatan Machine Learning.

            Pengguna dapat mengunggah dataset, melakukan
            preprocessing data, melatih model, mengevaluasi
            performa model, serta memperoleh hasil prediksi
            melalui antarmuka web yang sederhana dan mudah
            digunakan.

            Seluruh proses dikembangkan agar analisis data
            menjadi lebih cepat, konsisten, dan efisien.
            """
        )
        # ==========================================================
# TEKNOLOGI
# ==========================================================

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    ⚙️ Teknologi yang Digunakan
</div>

<div class="section-subtitle">
Framework dan library yang digunakan dalam pengembangan aplikasi.
</div>
""", unsafe_allow_html=True)

# ==========================================================
# BARIS 1
# ==========================================================

col1, col2, col3 = st.columns(3, gap="large")

with col1:

    with st.container(border=True):

        st.markdown("### 🐍 Python")

        st.caption("Bahasa Pemrograman")

        st.write(
            "Digunakan sebagai bahasa utama dalam pengembangan "
            "aplikasi dan implementasi algoritma Machine Learning."
        )

with col2:

    with st.container(border=True):

        st.markdown("### 🎈 Streamlit")

        st.caption("Framework Web")

        st.write(
            "Digunakan untuk membangun antarmuka web yang "
            "interaktif, responsif, dan mudah digunakan."
        )

with col3:

    with st.container(border=True):

        st.markdown("### 🤖 Scikit-Learn")

        st.caption("Machine Learning")

        st.write(
            "Library Machine Learning yang digunakan untuk "
            "membangun model Random Forest."
        )

# ==========================================================
# BARIS 2
# ==========================================================

st.write("")

col4, col5, col6 = st.columns(3, gap="large")

with col4:

    with st.container(border=True):

        st.markdown("### 🐼 Pandas")

        st.caption("Data Processing")

        st.write(
            "Digunakan untuk membaca, membersihkan, dan "
            "mengolah dataset penelitian."
        )

with col5:

    with st.container(border=True):

        st.markdown("### 📊 Plotly")

        st.caption("Visualization")

        st.write(
            "Menyajikan visualisasi data secara interaktif "
            "untuk mempermudah proses analisis."
        )

with col6:

    with st.container(border=True):

        st.markdown("### 📁 OpenPyXL")

        st.caption("Excel Processing")

        st.write(
            "Digunakan untuk membaca dan memproses file "
            "berformat Microsoft Excel."
        )
