import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime, timedelta

# ======================================================
# PAGE CONFIG
# ======================================================

BASE_DIR = Path(__file__).parent

logo_path = BASE_DIR / "assets" / "yamaha_logo.png"

logo = Image.open(logo_path)

st.set_page_config(
    page_title="Klasifikasi Layanan Servis Yamaha",
    page_icon=logo,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# DATE TIME
# ======================================================

utc_now = datetime.utcnow()
wib = utc_now + timedelta(hours=7)

tanggal = wib.strftime("%d %B %Y")
jam = wib.strftime("%H:%M WIB")

# ======================================================
# CSS
# ======================================================

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.stApp{
    background:#F5F7FA;
}

.block-container{
    max-width:1350px;
    padding-top:20px;
    padding-bottom:50px;
}

section[data-testid="stSidebar"]{

    background:#27463d;

}

section[data-testid="stSidebar"] *{

    color:white;

}

/* HERO */

.hero-title{

    text-align:center;
    font-size:54px;
    font-weight:900;
    color:#14332A;
    margin-top:5px;
    margin-bottom:5px;
    letter-spacing:1px;

}

.hero-sub{

    text-align:center;
    font-size:18px;
    color:#5B6472;
    line-height:1.7;
    margin-bottom:35px;

}

/* CARD */

.info-card{

    background:white;

    border-radius:15px;

    padding:25px;

    border:1px solid #E5E7EB;

    box-shadow:0px 5px 20px rgba(0,0,0,.05);

    transition:.3s;

    min-height:150px;

}

.info-card:hover{

    transform:translateY(-5px);

    box-shadow:0px 12px 25px rgba(0,0,0,.08);

}

.card-icon{

    font-size:30px;

}

.card-title{

    color:#64748B;

    font-size:15px;

    margin-top:10px;

    margin-bottom:12px;

}

.card-value{

    font-size:30px;

    font-weight:700;

    color:#14332A;

}

.card-desc{

    margin-top:10px;

    color:#94A3B8;

    font-size:14px;

}

/* SECTION */

.section-title{

    text-align:center;

    font-size:36px;

    font-weight:800;

    color:#14332A;

    margin-top:60px;

    margin-bottom:8px;

}

.section-desc{

    text-align:center;

    color:#64748B;

    font-size:17px;

    margin-bottom:30px;

}

</style>
""", unsafe_allow_html=True)

# ======================================================
# HERO
# ======================================================

st.image(str(logo_path), width=130)

st.markdown("""

<div class="hero-title">

KLASIFIKASI LAYANAN SERVIS YAMAHA

</div>

""", unsafe_allow_html=True)

st.markdown("""

<div class="hero-sub">

Penerapan <b>Algoritma Random Forest</b> untuk mengklasifikasikan
layanan servis kendaraan Yamaha berdasarkan pola data servis.

</div>

""", unsafe_allow_html=True)

# ======================================================
# INFO CARD
# ======================================================

c1,c2,c3 = st.columns(3)

with c1:

    st.markdown("""

<div class="info-card">

<div class="card-icon">

🏢

</div>

<div class="card-title">

Dealer Penelitian

</div>

<div class="card-value">

Tjahaja Baru Tabing

</div>

<div class="card-desc">

Lokasi penelitian yang digunakan dalam pengumpulan dataset.

</div>

</div>

""", unsafe_allow_html=True)

with c2:

    st.markdown("""

<div class="info-card">

<div class="card-icon">

🌲

</div>

<div class="card-title">

Algoritma

</div>

<div class="card-value">

Random Forest

</div>

<div class="card-desc">

Algoritma ensemble berbasis Decision Tree dengan metode Majority Voting.

</div>

</div>

""", unsafe_allow_html=True)

with c3:

    st.markdown(f"""

<div class="info-card">

<div class="card-icon">

🕒

</div>

<div class="card-title">

Update Sistem

</div>

<div class="card-value" style="font-size:24px;">

{tanggal}

</div>

<div class="card-desc">

{jam}

</div>

</div>

""", unsafe_allow_html=True)

# ======================================================
# TENTANG SISTEM
# ======================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
📌 Tentang Sistem
</div>

<div class="section-desc">
Sistem ini dikembangkan untuk membantu proses klasifikasi layanan servis
kendaraan Yamaha menggunakan algoritma <b>Random Forest</b>.
Model mempelajari pola dari data servis sehingga mampu menghasilkan
klasifikasi layanan secara lebih konsisten dan terstruktur.
</div>
""", unsafe_allow_html=True)

# ======================================================
# OVERVIEW CARD
# ======================================================

o1,o2,o3 = st.columns(3)

with o1:

    st.markdown("""

<div class="info-card">

<div class="card-icon">
📂
</div>

<div class="card-title">

Dataset

</div>

<div class="card-value">

1.483 Data

</div>

<div class="card-desc">

Dataset servis kendaraan Yamaha
yang digunakan sebagai data pelatihan
dan pengujian model.

</div>

</div>

""", unsafe_allow_html=True)

with o2:

    st.markdown("""

<div class="info-card">

<div class="card-icon">
🌲
</div>

<div class="card-title">

Machine Learning

</div>

<div class="card-value">

Random Forest

</div>

<div class="card-desc">

Algoritma Ensemble Learning
yang membangun banyak
Decision Tree.

</div>

</div>

""", unsafe_allow_html=True)

with o3:

    st.markdown("""

<div class="info-card">

<div class="card-icon">
🎯
</div>

<div class="card-title">

Output

</div>

<div class="card-value">

Klasifikasi

</div>

<div class="card-desc">

Menghasilkan klasifikasi
layanan servis berdasarkan
pola data yang dipelajari.

</div>

</div>

""", unsafe_allow_html=True)

# ======================================================
# PENJELASAN
# ======================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""

<div style="

background:#ffffff;

padding:28px;

border-radius:15px;

border:1px solid #E5E7EB;

box-shadow:0px 5px 20px rgba(0,0,0,.05);

line-height:1.9;

font-size:16px;

color:#4B5563;

">

<b>Tujuan Sistem</b>

<br><br>

Sistem ini memanfaatkan algoritma <b>Random Forest</b> untuk mempelajari
hubungan antar fitur seperti <b>jenis motor, usia motor, kilometer,
indikasi,</b> dan <b>jumlah komponen (Qty)</b>.
Pengetahuan yang dipelajari model digunakan untuk menghasilkan
<b>hasil klasifikasi layanan servis</b> secara otomatis berdasarkan
pola data historis.

</div>

""", unsafe_allow_html=True)

# ======================================================
# CARA KERJA RANDOM FOREST
# ======================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
🌲 Cara Kerja Random Forest
</div>

<div class="section-desc">
Random Forest merupakan algoritma Ensemble Learning yang terdiri dari
banyak <b>Decision Tree</b>. Setiap pohon mempelajari pola data secara
mandiri, kemudian seluruh hasil digabung menggunakan
<b>Majority Voting</b> untuk menghasilkan klasifikasi akhir.
</div>
""", unsafe_allow_html=True)

# ======================================================
# DATASET
# ======================================================

st.markdown("""
<div class="info-card" style="text-align:center;">

<div style="font-size:40px;">📂</div>

<h3 style="color:#14332A;margin-bottom:5px;">
Dataset Servis
</h3>

Dataset kendaraan Yamaha
yang digunakan sebagai data pelatihan.

</div>
""", unsafe_allow_html=True)

st.markdown(
"<h1 style='text-align:center;color:#16A34A;'>↓</h1>",
unsafe_allow_html=True)

# ======================================================
# DATA PREPARATION
# ======================================================

st.markdown("""
<div class="info-card" style="text-align:center;">

<div style="font-size:40px;">⚙️</div>

<h3 style="color:#14332A;margin-bottom:5px;">
Data Preparation
</h3>

Preprocessing • Feature Engineering

Encoding • Train-Test Split

</div>
""", unsafe_allow_html=True)

st.markdown(
"<h1 style='text-align:center;color:#16A34A;'>↓</h1>",
unsafe_allow_html=True)

# ======================================================
# RANDOM FOREST
# ======================================================

st.markdown("""

<div style="

background:#14332A;

padding:18px;

border-radius:12px;

text-align:center;

color:white;

font-size:28px;

font-weight:bold;

">

🌲 RANDOM FOREST MODEL

</div>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ======================================================
# DECISION TREE
# ======================================================

t1,t2,t3,t4 = st.columns(4)

with t1:

    st.success("🌳\n\nDecision Tree 1")

with t2:

    st.success("🌳\n\nDecision Tree 2")

with t3:

    st.success("🌳\n\nDecision Tree 3")

with t4:

    st.success("🌳\n\nDecision Tree n")

st.markdown(
"<h1 style='text-align:center;color:#16A34A;'>↓</h1>",
unsafe_allow_html=True)

# ======================================================
# MAJORITY VOTING
# ======================================================

st.markdown("""

<div class="info-card" style="text-align:center;">

<div style="font-size:40px;">
🗳️
</div>

<h3 style="color:#14332A;">

Majority Voting

</h3>

Seluruh hasil prediksi dari setiap
Decision Tree digabung untuk
menentukan hasil akhir.

</div>

""", unsafe_allow_html=True)

st.markdown(
"<h1 style='text-align:center;color:#16A34A;'>↓</h1>",
unsafe_allow_html=True)

# ======================================================
# OUTPUT
# ======================================================

st.markdown("""

<div style="

background:#16A34A;

padding:20px;

border-radius:12px;

text-align:center;

color:white;

">

<h2>

🎯 HASIL KLASIFIKASI

</h2>

Model menghasilkan klasifikasi
layanan servis berdasarkan
pola data yang telah dipelajari.

</div>

""", unsafe_allow_html=True)

# ======================================================
# WORKFLOW SISTEM
# ======================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
⚙️ Workflow Sistem
</div>

<div class="section-desc">
Tahapan utama proses klasifikasi layanan servis kendaraan Yamaha.
</div>
""", unsafe_allow_html=True)

col1,col_arrow1,col2,col_arrow2,col3,col_arrow3,col4,col_arrow4,col5 = st.columns(
    [2,0.5,2,0.5,2,0.5,2,0.5,2]
)

# ======================================================
# STEP 1
# ======================================================

with col1:

    st.markdown("""

<div class="info-card" style="text-align:center;height:200px;">

<div style="font-size:45px;">📂</div>

<h4 style="color:#14332A;">Upload Dataset</h4>

<div style="font-size:14px;color:#64748B;">

Mengunggah dataset
CSV atau Excel.

</div>

</div>

""", unsafe_allow_html=True)

with col_arrow1:

    st.markdown("<h1 style='text-align:center;margin-top:70px;'>➜</h1>",
    unsafe_allow_html=True)

# ======================================================
# STEP 2
# ======================================================

with col2:

    st.markdown("""

<div class="info-card" style="text-align:center;height:200px;">

<div style="font-size:45px;">⚙️</div>

<h4 style="color:#14332A;">Data Preparation</h4>

<div style="font-size:14px;color:#64748B;">

Preprocessing

Feature Engineering

Encoding

Train-Test Split

</div>

</div>

""", unsafe_allow_html=True)

with col_arrow2:

    st.markdown("<h1 style='text-align:center;margin-top:70px;'>➜</h1>",
    unsafe_allow_html=True)

# ======================================================
# STEP 3
# ======================================================

with col3:

    st.markdown("""

<div class="info-card" style="text-align:center;height:200px;">

<div style="font-size:45px;">🌲</div>

<h4 style="color:#14332A;">Random Forest</h4>

<div style="font-size:14px;color:#64748B;">

Training model

Decision Tree

Majority Voting

</div>

</div>

""", unsafe_allow_html=True)

with col_arrow3:

    st.markdown("<h1 style='text-align:center;margin-top:70px;'>➜</h1>",
    unsafe_allow_html=True)

# ======================================================
# STEP 4
# ======================================================

with col4:

    st.markdown("""

<div class="info-card" style="text-align:center;height:200px;">

<div style="font-size:45px;">📊</div>

<h4 style="color:#14332A;">Evaluation</h4>

<div style="font-size:14px;color:#64748B;">

Accuracy

Confusion Matrix

Classification Report

Feature Importance

</div>

</div>

""", unsafe_allow_html=True)

with col_arrow4:

    st.markdown("<h1 style='text-align:center;margin-top:70px;'>➜</h1>",
    unsafe_allow_html=True)

# ======================================================
# STEP 5
# ======================================================

with col5:

    st.markdown("""

<div class="info-card" style="text-align:center;height:200px;">

<div style="font-size:45px;">🎯</div>

<h4 style="color:#14332A;">Prediction</h4>

<div style="font-size:14px;color:#64748B;">

Model menghasilkan

hasil klasifikasi

layanan servis.

</div>

</div>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.info("""
💡 **Workflow Sistem** menunjukkan tahapan utama mulai dari pengunggahan dataset, proses persiapan data, pelatihan model Random Forest, evaluasi performa model, hingga menghasilkan prediksi klasifikasi layanan servis.
""")

# ======================================================
# WORKFLOW SISTEM
# ======================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
⚙️ Workflow Sistem
</div>

<div class="section-desc">
Tahapan utama proses klasifikasi layanan servis kendaraan Yamaha.
</div>
""", unsafe_allow_html=True)

col1,col_arrow1,col2,col_arrow2,col3,col_arrow3,col4,col_arrow4,col5 = st.columns(
    [2,0.5,2,0.5,2,0.5,2,0.5,2]
)

# ======================================================
# STEP 1
# ======================================================

with col1:

    st.markdown("""

<div class="info-card" style="text-align:center;height:200px;">

<div style="font-size:45px;">📂</div>

<h4 style="color:#14332A;">Upload Dataset</h4>

<div style="font-size:14px;color:#64748B;">

Mengunggah dataset
CSV atau Excel.

</div>

</div>

""", unsafe_allow_html=True)

with col_arrow1:

    st.markdown("<h1 style='text-align:center;margin-top:70px;'>➜</h1>",
    unsafe_allow_html=True)

# ======================================================
# STEP 2
# ======================================================

with col2:

    st.markdown("""

<div class="info-card" style="text-align:center;height:200px;">

<div style="font-size:45px;">⚙️</div>

<h4 style="color:#14332A;">Data Preparation</h4>

<div style="font-size:14px;color:#64748B;">

Preprocessing

Feature Engineering

Encoding

Train-Test Split

</div>

</div>

""", unsafe_allow_html=True)

with col_arrow2:

    st.markdown("<h1 style='text-align:center;margin-top:70px;'>➜</h1>",
    unsafe_allow_html=True)

# ======================================================
# STEP 3
# ======================================================

with col3:

    st.markdown("""

<div class="info-card" style="text-align:center;height:200px;">

<div style="font-size:45px;">🌲</div>

<h4 style="color:#14332A;">Random Forest</h4>

<div style="font-size:14px;color:#64748B;">

Training model

Decision Tree

Majority Voting

</div>

</div>

""", unsafe_allow_html=True)

with col_arrow3:

    st.markdown("<h1 style='text-align:center;margin-top:70px;'>➜</h1>",
    unsafe_allow_html=True)

# ======================================================
# STEP 4
# ======================================================

with col4:

    st.markdown("""

<div class="info-card" style="text-align:center;height:200px;">

<div style="font-size:45px;">📊</div>

<h4 style="color:#14332A;">Evaluation</h4>

<div style="font-size:14px;color:#64748B;">

Accuracy

Confusion Matrix

Classification Report

Feature Importance

</div>

</div>

""", unsafe_allow_html=True)

with col_arrow4:

    st.markdown("<h1 style='text-align:center;margin-top:70px;'>➜</h1>",
    unsafe_allow_html=True)

# ======================================================
# STEP 5
# ======================================================

with col5:

    st.markdown("""

<div class="info-card" style="text-align:center;height:200px;">

<div style="font-size:45px;">🎯</div>

<h4 style="color:#14332A;">Prediction</h4>

<div style="font-size:14px;color:#64748B;">

Model menghasilkan

hasil klasifikasi

layanan servis.

</div>

</div>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.info("""
💡 **Workflow Sistem** menunjukkan tahapan utama mulai dari pengunggahan dataset, proses persiapan data, pelatihan model Random Forest, evaluasi performa model, hingga menghasilkan prediksi klasifikasi layanan servis.
""")
