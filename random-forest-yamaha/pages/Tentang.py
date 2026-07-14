import streamlit as st
from pathlib import Path

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Tentang Sistem",
    page_icon="ℹ️",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.stApp{
    background:#0f172a;
}

.block-container{
    max-width:1200px;
    padding-top:2rem;
    padding-bottom:2rem;
}

.main-title{

    color:white;

    font-size:40px;

    font-weight:bold;

    text-align:center;

    margin-bottom:10px;

}

.main-desc{

    color:#cbd5e1;

    font-size:18px;

    text-align:center;

    margin-bottom:35px;

    line-height:1.8;

}

.card{

    background:linear-gradient(145deg,#111827,#1e293b);

    border-radius:20px;

    padding:25px;

    border:1px solid rgba(255,255,255,.08);

}

.section-title{

    color:white;

    font-size:28px;

    font-weight:bold;

    margin-bottom:20px;

}

.info{

    color:#d1d5db;

    font-size:17px;

    line-height:1.9;

}

.footer{

    text-align:center;

    color:#94a3b8;

    margin-top:50px;

    font-size:14px;

}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    "<div class='main-title'>📘 Tentang Sistem</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class='main-desc'>

Sistem ini merupakan implementasi algoritma <b>Random Forest</b>
untuk mengklasifikasikan layanan servis sepeda motor Yamaha.
Aplikasi dibangun menggunakan Streamlit sehingga proses
preprocessing, pelatihan model, evaluasi, hingga prediksi
dapat dilakukan dalam satu antarmuka.

</div>
""",
    unsafe_allow_html=True
)
# ==========================================================
# BIODATA & TEKNOLOGI
# ==========================================================

st.markdown("---")

left, right = st.columns([2, 1], gap="large")

# ==========================================================
# CARD BIODATA
# ==========================================================

with left:

    with st.container(border=True):

        st.markdown("### 👤 Biodata Pengembang")

        foto_col, data_col = st.columns([1, 2])

        # -------------------------
        # FOTO
        # -------------------------

        with foto_col:

            foto_path = Path(__file__).resolve().parent.parent / "assets" / "foto.jpg"

            if foto_path.exists():
                st.image(str(foto_path), use_container_width=True)
            else:
                st.warning("Foto tidak ditemukan")

        # -------------------------
        # BIODATA
        # -------------------------

        with data_col:

            st.write("**Nama**")
            st.write("Giffari")

            st.write("**NIM**")
            st.write("20XXXXXXXX")

            st.write("**Program Studi**")
            st.write("Sistem Informasi")

            st.write("**Universitas**")
            st.write("Universitas Muhammadiyah Kalimantan Timur")

            st.write("**Email**")
            st.write("giffari@email.com")

# ==========================================================
# CARD TEKNOLOGI
# ==========================================================

with right:

    with st.container(border=True):

        st.markdown("### ⚙️ Teknologi")

        st.markdown("🐍 **Python**")

        st.progress(100)

        st.markdown("🌲 **Random Forest**")

        st.progress(100)

        st.markdown("📊 **Pandas**")

        st.progress(100)

        st.markdown("🤖 **Scikit-Learn**")

        st.progress(100)

        st.markdown("🎈 **Streamlit**")

        st.progress(100)

        st.markdown("📄 **ReportLab**")

        st.progress(100)

# ==========================================================
# TENTANG PENELITIAN
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("## 📖 Tentang Penelitian")

with st.container(border=True):

    st.write("""
Penelitian ini bertujuan membangun sistem klasifikasi layanan servis
sepeda motor Yamaha menggunakan algoritma **Random Forest**.
Sistem mampu membantu proses klasifikasi berdasarkan data historis
layanan servis sehingga proses analisis menjadi lebih cepat,
konsisten, dan mudah digunakan.

Tahapan sistem meliputi proses **upload dataset, preprocessing,
feature engineering, pelatihan model, evaluasi model,** hingga
**prediksi layanan servis** melalui antarmuka berbasis web.
""")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# INFORMASI PENELITIAN
# ==========================================================

st.markdown("## 📊 Informasi Penelitian")

col1, col2, col3 = st.columns(3)

# ----------------------------------------------------------

with col1:

    with st.container(border=True):

        st.markdown("### 🌲 Algoritma")

        st.metric(
            label="Metode",
            value="Random Forest"
        )

        st.caption(
            "Digunakan sebagai algoritma klasifikasi utama."
        )

# ----------------------------------------------------------

with col2:

    with st.container(border=True):

        st.markdown("### 📂 Dataset")

        st.metric(
            label="Jenis Data",
            value="Layanan Servis"
        )

        st.caption(
            "Dataset historis servis sepeda motor Yamaha."
        )

# ----------------------------------------------------------

with col3:

    with st.container(border=True):

        st.markdown("### 💻 Platform")

        st.metric(
            label="Aplikasi",
            value="Streamlit"
        )

        st.caption(
            "Aplikasi berbasis web interaktif."
        )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# FITUR SISTEM
# ==========================================================

st.markdown("## 🚀 Fitur Sistem")

fitur1, fitur2 = st.columns(2)

with fitur1:

    st.success("✅ Upload Dataset")

    st.success("✅ Preprocessing Data")

    st.success("✅ Feature Engineering")

with fitur2:

    st.success("✅ Training Random Forest")

    st.success("✅ Evaluasi Model")

    st.success("✅ Prediksi Layanan")

# ==========================================================
# RINGKASAN SISTEM
# ==========================================================

st.markdown("---")

st.markdown("## 📌 Ringkasan Sistem")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Algoritma",
        value="Random Forest"
    )

with col2:
    st.metric(
        label="Framework",
        value="Streamlit"
    )

with col3:
    st.metric(
        label="Bahasa",
        value="Python"
    )

with col4:
    st.metric(
        label="Versi",
        value="1.0"
    )

# ==========================================================
# ALUR SINGKAT
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("## 🔄 Alur Sistem")

with st.container(border=True):

    st.markdown("""
1. 📂 Upload Dataset

2. 🧹 Preprocessing Data

3. ⚙️ Feature Engineering

4. 🌲 Training Model Random Forest

5. 📈 Evaluasi Model

6. 🎯 Prediksi Layanan Servis

7. 📄 Generate Laporan
""")

# ==========================================================
# LIBRARY
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("## 📚 Library yang Digunakan")

lib1, lib2, lib3 = st.columns(3)

with lib1:

    st.info("""
🐍 Python

📊 Pandas

🔢 NumPy
""")

with lib2:

    st.info("""
🌲 Scikit-Learn

📈 Plotly

📉 Matplotlib
""")

with lib3:

    st.info("""
🎈 Streamlit

📄 ReportLab

📂 OpenPyXL
""")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
    "Sistem Klasifikasi Layanan Servis Yamaha "
    "| Random Forest Classification"
)

st.caption(
    "Dikembangkan oleh Giffari • Universitas Muhammadiyah Kalimantan Timur • 2026"
)
