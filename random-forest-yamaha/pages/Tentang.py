import streamlit as st
from pathlib import Path
from PIL import Image

# ==========================================================
# PAGE CONFIG
# ==========================================================

BASE_DIR = Path(__file__).parent

logo_path = BASE_DIR / "assets" / "yamaha_logo.png"
logo = Image.open(logo_path)

st.set_page_config(
    page_title="Tentang Sistem",
    page_icon=logo,
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
HEADER
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
SIDEBAR
=================================================== */

section[data-testid="stSidebar"]{

    background:#0f172a;

}

section[data-testid="stSidebar"] *{

    color:white;

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

    font-size:43px;

    font-weight:900;

    margin-top:5px;

    margin-bottom:12px;

}

.subtitle{

    text-align:center;

    color:#cbd5e1;

    font-size:15px;

    margin-bottom:45px;

}

/* ===================================================
CARD
=================================================== */

.app-card{

    background:linear-gradient(145deg,#111827,#1e293b);

    border:1px solid #334155;

    border-radius:22px;

    padding:30px;

    box-shadow:0 5px 15px rgba(0,0,0,.08);

    transition:.3s;

}

.app-card:hover{

    transform:translateY(-6px);

    box-shadow:0 0 20px rgba(239,68,68,.25);

}

/* ===================================================
CARD TITLE
=================================================== */

.card-title{

    color:white;

    font-size:28px;

    font-weight:700;

    margin-bottom:18px;

}

.card-text{

    color:#e2e8f0;

    line-height:1.9;

    font-size:15px;

}

.section-title{

    text-align:center;

    font-size:42px;

    font-weight:900;

    color:white;

    margin-top:15px;

    margin-bottom:10px;

}

.section-desc{

    text-align:center;

    color:#cbd5e1;

    margin-bottom:40px;

}

hr{

    border:none;

    border-top:1px solid #334155;

    margin-top:45px;

    margin-bottom:45px;

}

</style>

""", unsafe_allow_html=True)

# ==========================================================
# HERO
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2.5,1,2.5])

with col2:

    st.image(str(logo_path), width=180)

st.markdown("""

<div class="main-title">

TENTANG SISTEM

</div>

<div class="subtitle">

Informasi mengenai penelitian, tujuan pengembangan,
serta teknologi yang digunakan pada Sistem Klasifikasi
Layanan Servis Yamaha.

</div>

""", unsafe_allow_html=True)

# ==========================================================
# TENTANG SISTEM
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    Tentang Penelitian
</div>

<div class="section-desc">
Informasi mengenai penelitian dan sistem yang dikembangkan.
</div>
""", unsafe_allow_html=True)

left, right = st.columns(2, gap="large")

# ==========================================================
# INFORMASI PENELITIAN
# ==========================================================

with left:

    st.markdown("""

<div class="app-card">

<h2 style="color:white;text-align:center;">
🎓 Informasi Penelitian
</h2>

<hr style="border:1px solid #334155;">

<p class="card-text">

<b>Judul Penelitian</b><br>
Penerapan Algoritma Random Forest untuk
Mengklasifikasi Layanan Servis pada Yamaha.

<br><br>

<b>Metode</b><br>
Random Forest Classification

<br><br>

<b>Platform</b><br>
Aplikasi Web berbasis Streamlit

<br><br>

<b>Jenis Penelitian</b><br>
Implementasi Machine Learning

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# DESKRIPSI SISTEM
# ==========================================================

with right:

    st.markdown("""

<div class="app-card">

<h2 style="color:white;text-align:center;">
📘 Deskripsi Sistem
</h2>

<hr style="border:1px solid #334155;">

<p class="card-text">

Sistem ini dikembangkan untuk membantu proses
klasifikasi layanan servis kendaraan Yamaha
menggunakan algoritma Random Forest.

<br><br>

Pengguna dapat melakukan upload dataset,
preprocessing, pelatihan model,
evaluasi performa, serta memperoleh
hasil klasifikasi melalui satu aplikasi
berbasis web yang mudah digunakan.

<br><br>

Seluruh proses dirancang agar analisis data
menjadi lebih cepat, konsisten,
dan mudah dipahami.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# TUJUAN & MANFAAT
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    Tujuan dan Manfaat
</div>

<div class="section-desc">
Gambaran tujuan penelitian serta manfaat yang diberikan oleh sistem.
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

# ==========================================================
# CARD 1
# ==========================================================

with c1:

    st.markdown("""

<div class="app-card">

<div style="font-size:45px;text-align:center;">
🎯
</div>

<h3 style="color:white;text-align:center;margin-top:10px;">
Tujuan
</h3>

<p class="card-text" style="text-align:center;">

Mengembangkan sistem klasifikasi layanan
servis kendaraan Yamaha menggunakan
algoritma Random Forest sehingga proses
analisis data menjadi lebih efektif.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# CARD 2
# ==========================================================

with c2:

    st.markdown("""

<div class="app-card">

<div style="font-size:45px;text-align:center;">
💡
</div>

<h3 style="color:white;text-align:center;margin-top:10px;">
Manfaat
</h3>

<p class="card-text" style="text-align:center;">

Membantu pengguna memahami proses
klasifikasi layanan servis melalui
visualisasi, evaluasi model,
serta hasil prediksi.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# CARD 3
# ==========================================================

with c3:

    st.markdown("""

<div class="app-card">

<div style="font-size:45px;text-align:center;">
🖥️
</div>

<h3 style="color:white;text-align:center;margin-top:10px;">
Fitur Utama
</h3>

<p class="card-text" style="text-align:center;">

Upload Dataset,
Preprocessing,
Training Model,
Evaluasi,
Insight,
Prediksi,
dan Laporan PDF.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# TEKNOLOGI YANG DIGUNAKAN
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""

<div class="app-card">

<h2 style="color:#ffffff;text-align:center;">
⚙️ Teknologi yang Digunakan
</h2>

<p class="card-text" style="text-align:center;">

Sistem dikembangkan menggunakan kombinasi beberapa teknologi
untuk mendukung proses pengolahan data, pembangunan model,
visualisasi hasil, serta penyajian antarmuka aplikasi berbasis web.

</p>

<br>

</div>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# BARIS 1
# ==========================================================

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""

<div class="app-card">

<div style="font-size:45px;text-align:center;">
🐍
</div>

<h3 style="text-align:center;color:white;">
Python
</h3>

<p class="card-text" style="text-align:center;">

Bahasa pemrograman utama
yang digunakan untuk
mengembangkan sistem.

</p>

</div>

""", unsafe_allow_html=True)

with c2:

    st.markdown("""

<div class="app-card">

<div style="font-size:45px;text-align:center;">
🎈
</div>

<h3 style="text-align:center;color:white;">
Streamlit
</h3>

<p class="card-text" style="text-align:center;">

Framework web yang
digunakan sebagai
antarmuka aplikasi.

</p>

</div>

""", unsafe_allow_html=True)

with c3:

    st.markdown("""

<div class="app-card">

<div style="font-size:45px;text-align:center;">
🤖
</div>

<h3 style="text-align:center;color:white;">
Scikit-Learn
</h3>

<p class="card-text" style="text-align:center;">

Library Machine Learning
untuk membangun model
Random Forest.

</p>

</div>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# BARIS 2
# ==========================================================

c4, c5, c6 = st.columns(3)

with c4:

    st.markdown("""

<div class="app-card">

<div style="font-size:45px;text-align:center;">
🐼
</div>

<h3 style="text-align:center;color:white;">
Pandas
</h3>

<p class="card-text" style="text-align:center;">

Mengelola serta
memproses dataset
penelitian.

</p>

</div>

""", unsafe_allow_html=True)

with c5:

    st.markdown("""

<div class="app-card">

<div style="font-size:45px;text-align:center;">
📊
</div>

<h3 style="text-align:center;color:white;">
Plotly
</h3>

<p class="card-text" style="text-align:center;">

Visualisasi data
secara interaktif.

</p>

</div>

""", unsafe_allow_html=True)

with c6:

    st.markdown("""

<div class="app-card">

<div style="font-size:45px;text-align:center;">
📄
</div>

<h3 style="text-align:center;color:white;">
OpenPyXL
</h3>

<p class="card-text" style="text-align:center;">

Membaca dan
mengolah file
Microsoft Excel.

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# PENGEMBANG
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""

<div class="app-card">

<h2 style="color:white;text-align:center;">
👨‍💻 Profil Pengembang
</h2>

<p class="card-text" style="text-align:center;">

Aplikasi ini dikembangkan sebagai implementasi penelitian
Program Studi Sistem Informasi yang bertujuan menerapkan
algoritma Random Forest untuk mengklasifikasikan layanan
servis kendaraan Yamaha berdasarkan data historis servis.

</p>

</div>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# ==========================================================
# IDENTITAS
# ==========================================================

with col1:

    st.markdown("""

<div class="app-card">

<h3 style="color:white;text-align:center;">
📌 Identitas
</h3>

<p class="card-text">

<b>Nama</b><br>
Raka Giffari Ramadhan

<br><br>

<b>Program Studi</b><br>
Sistem Informasi

<br><br>

<b>Universitas</b><br>
Universitas Putra Indonesia "YPTK" Padang

<br><br>

<b>Tahun</b><br>
2026

</p>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# INFORMASI APLIKASI
# ==========================================================

with col2:

    st.markdown("""

<div class="app-card">

<h3 style="color:white;text-align:center;">
📘 Informasi Aplikasi
</h3>

<p class="card-text">

<b>Versi</b><br>
1.0

<br><br>

<b>Bahasa Pemrograman</b><br>
Python

<br><br>

<b>Framework</b><br>
Streamlit

<br><br>

<b>Machine Learning</b><br>
Scikit-Learn

</p>

</div>

""", unsafe_allow_html=True)
