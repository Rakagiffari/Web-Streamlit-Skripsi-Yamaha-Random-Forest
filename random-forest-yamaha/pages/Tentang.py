import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Tentang Sistem",
    page_icon="📘",
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
    font-family: "Segoe UI", sans-serif;
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
    font-size:43px;
    font-weight:900;
    color:white;
    margin-top:5px;
    margin-bottom:10px;
    letter-spacing:1px;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:15px;
    margin-bottom:45px;
}

/* ===================================================
SECTION
=================================================== */

.section-title{
    text-align:center;
    font-size:40px;
    font-weight:900;
    color:white;
    margin-bottom:10px;
}

.section-desc{
    text-align:center;
    color:#cbd5e1;
    font-size:14px;
    margin-bottom:40px;
}

/* ===================================================
CARD
=================================================== */

.app-card{

    background:linear-gradient(145deg,#111827,#1e293b);

    border:1px solid #334155;

    border-radius:22px;

    padding:30px;

    transition:.3s ease;

    box-shadow:0 5px 15px rgba(0,0,0,.08);

}

.app-card:hover{

    transform:translateY(-6px);

    box-shadow:0 0 20px rgba(239,68,68,.25);

}

.card-title{

    color:white;

    font-size:30px;

    font-weight:700;

    margin-bottom:15px;

}

.card-text{

    color:#e2e8f0;

    font-size:15px;

    line-height:1.9;

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

st.markdown("""

<div class="main-title">

📘 TENTANG SISTEM

</div>

<div class="subtitle">

Sistem Klasifikasi Layanan Servis Yamaha berbasis
Machine Learning menggunakan algoritma Random Forest.

</div>

""", unsafe_allow_html=True)

# ==========================================================
# DESKRIPSI SINGKAT
# ==========================================================

st.markdown("""

<div class="app-card">

<h2 style="text-align:center;color:white;">

Selamat Datang

</h2>

<p class="card-text" style="text-align:center;">

Halaman ini menyajikan informasi mengenai penelitian,
tujuan pengembangan sistem, teknologi yang digunakan,
serta profil pengembang aplikasi.

Seluruh desain halaman dibuat konsisten dengan halaman
utama sehingga pengguna memperoleh pengalaman penggunaan
yang nyaman dan mudah dipahami.

</p>

</div>

""", unsafe_allow_html=True)
# ==========================================================
# INFORMASI PENELITIAN
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
Informasi Penelitian
</div>

<div class="section-desc">
Ringkasan penelitian yang menjadi dasar pengembangan sistem.
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

# ==========================================================
# CARD 1
# ==========================================================

with c1:

    st.markdown("""

<div class="app-card">

<div style="font-size:48px;text-align:center;">
🎓
</div>

<div class="card-title" style="text-align:center;">
Penelitian
</div>

<div class="card-text" style="text-align:center;">

<b>Judul</b>

<br><br>

Penerapan Algoritma Random Forest
untuk Mengklasifikasi
Layanan Servis
pada Yamaha.

</div>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# CARD 2
# ==========================================================

with c2:

    st.markdown("""

<div class="app-card">

<div style="font-size:48px;text-align:center;">
🎯
</div>

<div class="card-title" style="text-align:center;">
Tujuan
</div>

<div class="card-text" style="text-align:center;">

Mengembangkan sistem
berbasis Machine Learning
untuk membantu proses
klasifikasi layanan servis
secara otomatis.

</div>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# CARD 3
# ==========================================================

with c3:

    st.markdown("""

<div class="app-card">

<div style="font-size:48px;text-align:center;">
📊
</div>

<div class="card-title" style="text-align:center;">
Dataset
</div>

<div class="card-text" style="text-align:center;">

Dataset historis
layanan servis Yamaha
digunakan sebagai
data pelatihan
dan evaluasi model.

</div>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# KEMAMPUAN SISTEM
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
Kemampuan Sistem
</div>

<div class="section-desc">
Fitur utama yang tersedia pada Sistem Klasifikasi Layanan Servis Yamaha.
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

# ==========================================================
# CARD 1
# ==========================================================

with c1:

    st.markdown("""

<div class="app-card">

<div style="font-size:48px;text-align:center;">
📂
</div>

<div class="card-title" style="text-align:center;">
Upload Dataset
</div>

<div class="card-text" style="text-align:center;">

Mendukung proses
unggah dataset
berformat CSV
maupun Excel
untuk dianalisis.

</div>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# CARD 2
# ==========================================================

with c2:

    st.markdown("""

<div class="app-card">

<div style="font-size:48px;text-align:center;">
🌲
</div>

<div class="card-title" style="text-align:center;">
Training Model
</div>

<div class="card-text" style="text-align:center;">

Melatih model
Random Forest
secara otomatis
menggunakan
dataset penelitian.

</div>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# CARD 3
# ==========================================================

with c3:

    st.markdown("""

<div class="app-card">

<div style="font-size:48px;text-align:center;">
📊
</div>

<div class="card-title" style="text-align:center;">
Evaluasi Model
</div>

<div class="card-text" style="text-align:center;">

Menampilkan
Accuracy,
Precision,
Recall,
F1-Score,
dan Confusion Matrix.

</div>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# MODUL SISTEM
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
Modul Sistem
</div>

<div class="section-desc">
Menu utama yang tersedia pada aplikasi klasifikasi layanan servis Yamaha.
</div>
""", unsafe_allow_html=True)

modul = [

    ("1","🏠","Home"),
    ("2","📘","Tentang"),
    ("3","📂","Dataset"),
    ("4","⚙️","Preprocessing"),

    ("5","🌲","Proses"),
    ("6","📊","Insight"),
    ("7","🎯","Prediksi"),
    ("8","📄","Laporan")

]

# ==========================================================
# BARIS 1
# ==========================================================

cols = st.columns(4)

for i in range(4):

    no,icon,title = modul[i]

    with cols[i]:

        st.markdown(f"""

<div class="flow-card">

<div class="flow-number">

{no}

</div>

<div style="font-size:40px;margin-bottom:15px;">

{icon}

</div>

<div class="flow-title">

{title}

</div>

</div>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# BARIS 2
# ==========================================================

cols = st.columns(4)

for i in range(4,8):

    no,icon,title = modul[i]

    with cols[i-4]:

        st.markdown(f"""

<div class="flow-card">

<div class="flow-number">

{no}

</div>

<div style="font-size:40px;margin-bottom:15px;">

{icon}

</div>

<div class="flow-title">

{title}

</div>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# PENUTUP
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""

<div class="rf-box">

<h2 style="color:white;text-align:center;">
📌 Ringkasan Sistem
</h2>

<p style="
color:#e2e8f0;
text-align:center;
font-size:16px;
line-height:2;
">

Sistem Klasifikasi Layanan Servis Yamaha merupakan aplikasi
berbasis web yang dikembangkan untuk membantu proses klasifikasi
layanan servis menggunakan algoritma <b>Random Forest</b>.

Melalui aplikasi ini, pengguna dapat melakukan pengelolaan dataset,
preprocessing, pelatihan model, evaluasi performa, analisis hasil,
hingga prediksi layanan servis secara terintegrasi dalam satu sistem.

Diharapkan aplikasi ini dapat menjadi media pembelajaran sekaligus
alat bantu analisis data yang mudah digunakan, interaktif,
dan informatif.

</p>

</div>

""", unsafe_allow_html=True)
