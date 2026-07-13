import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime, timedelta

# ==========================================================
# PAGE CONFIG
# ==========================================================

BASE_DIR = Path(__file__).parent

logo_path = BASE_DIR / "assets" / "yamaha_logo.png"

logo = Image.open(logo_path)

st.set_page_config(
    page_title="Klasifikasi Layanan Servis Yamaha",
    page_icon=logo,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# DATE & TIME (WIB)
# ==========================================================

utc_now = datetime.utcnow()
wib_now = utc_now + timedelta(hours=7)

tanggal = wib_now.strftime("%d-%m-%Y")
jam = wib_now.strftime("%H:%M WIB")

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
    text-align: center;
    font-size: 43px;
    font-weight: 900;
    color: white;
    line-height: 1.1;
    margin-top: 5px;
    margin-bottom: 10px;
    letter-spacing: 1px;
}

.subtitle{
    text-align: center;
    color: #cbd5e1;
    font-size: 14px;
    margin-top: 0px;
    margin-bottom: 45px;
}

/* ===================================================
INFO CARD
=================================================== */
.info-card{
    background: linear-gradient(145deg, #111827, #1e293b);
    padding: 28px 20px;
    border-radius: 22px;
    border: 1px solid #334155;
    text-align: center;
    transition: 0.3s ease;
    box-shadow: 0px 5px 15px rgba(0,0,0,.08);
    min-height: 150px;

    display:flex;
    flex-direction:column;
    justify-content:center;
}

.info-card:hover{
    transform:translateY(-5px);
    box-shadow:0 0 20px rgba(239,68,68,0.25);
}

.card-title{
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 12px;
    font-weight: 600;
}

.card-value{
    color: white;
    font-size: 20px;
    font-weight: 800;
}

/* ===================================================
SECTION TITLE
=================================================== */
.section-title{
    text-align:center;
    font-size:34px;
    font-weight:800;
    color:#ffffff;
    margin-top:60px;
    margin-bottom:8px;
}

.section-desc{
    text-align:center;
    color:#ffffff;
    font-size:16px;
    margin-bottom:35px;
}

/* ===================================================
RANDOM FOREST BOX
=================================================== */
.rf-box{
    background: linear-gradient(145deg, #111827, #1e293b);
    padding: 28px 20px;
    border-radius: 22px;
    border: 1px solid #334155;
    text-align: center;
    transition: 0.3s ease;
    box-shadow: 0px 5px 15px rgba(0,0,0,.08);
    min-height: 150px;

    display:flex;
    flex-direction:column;
    justify-content:center;
}

/* ===================================================
FEATURE BOX
=================================================== */

.feature-box{
    background: linear-gradient(145deg, #111827, #1e293b);
    padding: 28px 20px;
    border-radius: 22px;
    border: 1px solid #334155;
    text-align: center;
    transition: 0.3s ease;
    box-shadow: 0px 5px 15px rgba(0,0,0,.08);
    min-height: 150px;
    display:flex;
    flex-direction:column;
    justify-content:center;
}

.feature-box:hover{
    transform:translateY(-8px);
    box-shadow:0 0 20px rgba(239,68,68,0.25);
}

.feature-icon{
    font-size:45px;
    margin-bottom:10px;
}

.feature-title{
    font-size:20px;
    font-weight:700;
    color: white;
    margin-bottom:10px;
}

.feature-desc{
    color: white;
    font-size:15px;
}

/* ===================================================
FLOW CARD
=================================================== */
.flow-card{
    background:linear-gradient(145deg, #111827, #1e293b);
    border-radius:20px;
    border:1px solid #e5e7eb;
    padding:20px;
    text-align:center;
    box-shadow:0px 5px 15px rgba(0,0,0,.08);
    min-height:200px;
    transition:.3s;
}

.flow-card:hover{
    transform:translateY(-6px);
}

.flow-number{
    width:42px;
    height:42px;
    border-radius:50%;
    background:#14332a;
    color:white;
    display:flex;
    align-items:center;
    justify-content:center;
    margin:auto;
    font-weight:bold;
    margin-bottom:18px;
}

.flow-title{
    font-size:20px;
    font-weight:700;
    color:#14332a;
    margin-bottom:12px;
}

.flow-desc{
    color:#64748b;
    font-size:14px;
}

/* ===================================================
ALERT
=================================================== */

.stAlert{
    border-radius:15px;
}

/* ===================================================
HR
=================================================== */
hr{
    border:none;
    border-top:1px solid #e5e7eb;
    margin-top:45px;
    margin-bottom:45px;
}
/* =====================================================
   RANDOM FOREST WORKFLOW
===================================================== */

.workflow-container{
    max-width:1000px;
    margin:auto;
}

.workflow-step{
    width:320px;
    margin:auto;
    background:linear-gradient(145deg,#111827,#1e293b);
    border:1px solid #334155;
    border-radius:18px;
    padding:18px;
    text-align:center;
    color:white;
    font-size:22px;
    font-weight:700;
    transition:.35s;
    box-shadow:0 8px 18px rgba(0,0,0,.25);
}

.workflow-step:hover{
    transform:translateY(-5px);
    box-shadow:0 0 25px rgba(34,197,94,.25);
}

.workflow-arrow{
    text-align:center;
    color:#22c55e;
    font-size:42px;
    margin:8px 0;
}

.rf-container{

    margin-top:15px;
    border-radius:24px;

    background:linear-gradient(
        145deg,
        #0f3d2e,
        #123d35
    );

    padding:30px;

    border:2px solid rgba(34,197,94,.25);

    box-shadow:
        0 20px 40px rgba(0,0,0,.35),
        inset 0 0 0 1px rgba(255,255,255,.05);

}

.rf-title{

    text-align:center;
    color:white;
    font-size:38px;
    font-weight:800;
    margin-bottom:25px;

}

.rf-card{

    background:white;

    border-radius:18px;

    padding:16px;

    text-align:center;

    font-size:18px;

    font-weight:700;

    color:#111827;

    width:320px;

    margin:auto;

    box-shadow:0 8px 20px rgba(0,0,0,.15);

    transition:.3s;

}

.rf-card:hover{

    transform:scale(1.04);

}

.rf-tree-row{

    display:flex;

    justify-content:space-between;

    gap:20px;

    margin-top:35px;

    margin-bottom:35px;

}

.rf-tree{

    flex:1;

    background:white;

    border-radius:18px;

    padding:18px;

    text-align:center;

    font-size:18px;

    font-weight:700;

    color:#111827;

    transition:.3s;

    box-shadow:0 8px 18px rgba(0,0,0,.18);

}

.rf-tree:hover{

    transform:translateY(-6px);

}

.rf-note{

    margin-top:20px;

    border:1px dashed rgba(255,255,255,.35);

    border-radius:15px;

    padding:15px;

    text-align:center;

    color:white;

    font-size:18px;

}

.rf-result{

    width:350px;

    margin:auto;

    background:linear-gradient(145deg,#111827,#1e293b);

    color:white;

    padding:20px;

    border-radius:18px;

    font-size:26px;

    font-weight:800;

    text-align:center;

    box-shadow:0 10px 25px rgba(0,0,0,.25);

}

.rf-down{

    text-align:center;

    font-size:42px;

    color:#22c55e;

    margin:12px;

}

.rf-center{

    text-align:center;

    color:white;

    font-size:38px;

    margin:12px;

}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2.5,1,2.5])

with col2:
    st.image(str(logo_path), width=180)

st.markdown("""
<div class="main-title">
KLASIFIKASI LAYANAN SERVIS YAMAHA
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
    Penerapan Algoritma Random Forest untuk mengklasifikasikan layanan servis
    kendaraan Yamaha berdasarkan pola data servis.
</div>
""", unsafe_allow_html=True)

# ==========================================================
# INFORMATION CARD
# ==========================================================

space1,col1,col2,space2 = st.columns([0.6,1,1,0.6])

with col1:

    st.markdown(f"""

<div class="info-card">
    <div class="card-title">
        Dealer Yamaha
    </div>
    <div class="card-value">
        Tjahaja Baru Tabing
    </div>
</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown(f"""

<div class="info-card">
    <div class="card-title">
        Tanggal & Jam
    </div>
    <div class="card-value">
    {tanggal} | {jam}
    </div> 
</div>

""", unsafe_allow_html=True)

# ==========================================================
# RANDOM FOREST DESCRIPTION
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""

<div class="rf-box">
    <h2 style="color:#ffffff;text-align:center;">
        Apa itu Random Forest ?
    </h2>  
    
Random Forest merupakan algoritma Machine Learning berbasis
Decision Tree yang bekerja dengan membangun banyak pohon keputusan
(Tree). Setiap Decision Tree mempelajari pola data servis yang berbeda,
kemudian seluruh hasil klasifikasi digabung menggunakan
Majority Voting sehingga menghasilkan prediksi yang lebih stabil,
lebih akurat, dan mengurangi risiko overfitting.

</div>
""", unsafe_allow_html=True)

# ==========================================================
# KEUNGGULAN SISTEM
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">
                🎯
            </div>
            <div class="feature-title">
                Akurat
            </div>
            <div class="feature-desc">
                Random Forest memanfaatkan banyak Decision Tree sehingga menghasilkan
                klasifikasi dengan tingkat akurasi yang baik.
            </div>
        </div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">
                ⚡
            </div>
            <div class="feature-title">
                Cepat
            </div>
            <div class="feature-desc">
                Seluruh proses preprocessing, training hingga prediksi
                dapat dilakukan secara otomatis dalam satu sistem.
            </div>
        </div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class="feature-box">
            <div class="feature-icon">
                📖
            </div>
            <div class="feature-title">
                Mudah Dipahami
            </div>
            <div class="feature-desc">
                Sistem menampilkan konsep Random Forest,
                Decision Tree serta proses klasifikasi
                agar pengguna memahami cara kerja model.
            </div>
        </div>
""", unsafe_allow_html=True)

# ==========================================================
# RANDOM FOREST WORKFLOW
# ==========================================================
st.markdown("""
    <div class="section-title">
        🛠️ Cara Kerja Algoritma Random Forest
    </div>
    <div class="section-desc">
        Random Forest membangun banyak <b>Decision Tree</b> dari dataset pelatihan.
        Setiap pohon melakukan proses klasifikasi secara independen, kemudian seluruh
        hasil digabung menggunakan <b>Majority Voting</b> untuk memperoleh prediksi akhir.
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="workflow-container">
        <div class="rf-container">
            <div class="rf-title">
                🌲 Random Forest
            </div>
            <div class="rf-card"
                🗂 Bootstrap Sampling
            </div>
            <div class="rf-center">
                ⬇
            </div>

<div class="rf-card">
📊 Gini Index
</div>

<div class="rf-center">
⬇
</div>

<div class="rf-tree-row">

<div class="rf-tree">
🌳 Tree 1
</div>

<div class="rf-tree">
🌳 Tree 2
</div>

<div class="rf-tree">
🌳 Tree 3
</div>

</div>

<div class="rf-center">
⬇
</div>

<div class="rf-card">
👥 Majority Voting
</div>

<div class="rf-note">
Menggabungkan hasil seluruh Decision Tree untuk menentukan prediksi akhir.
</div>

</div>

<div class="rf-down">
⬇
</div>

<div class="rf-result">
🎯 Hasil Klasifikasi
</div>

</div>

""", unsafe_allow_html=True)
# ==========================================================
# ALUR SISTEM
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
⚙️ Alur Sistem Klasifikasi
</div>

<div class="section-desc">
Tahapan proses klasifikasi layanan servis menggunakan algoritma Random Forest.
</div>
""", unsafe_allow_html=True)

flow_data = [

("1","📂","Upload Dataset",
"Pengguna mengunggah dataset servis Yamaha dalam format CSV atau Excel."),

("2","🧹","Preprocessing",
"Pembersihan data, menghapus missing value, duplikasi, serta menyiapkan data."),

("3","⚙️","Feature Engineering",
"Membentuk fitur baru seperti Usia Motor, Jenis Motor, dan Indikasi."),

("4","🔤","Encoding",
"Mengubah data kategorikal menjadi data numerik agar dapat diproses model."),

("5","✂️","Train-Test Split",
"Membagi dataset menjadi data latih dan data uji."),

("6","🌲","Random Forest",
"Model membangun banyak Decision Tree untuk mempelajari pola data servis."),

("7","📊","Evaluasi Model",
"Menghasilkan Accuracy, Confusion Matrix, Classification Report, dan Feature Importance."),

("8","🎯","Prediksi",
"Model melakukan klasifikasi layanan servis menjadi Ringan atau Berat."),

("9","📄","Laporan PDF",
"Sistem menghasilkan laporan hasil pelatihan model dalam format PDF.")

]

# ==========================================================
# BARIS 1
# ==========================================================

cols = st.columns(3)

for i in range(3):

    no,icon,title,desc = flow_data[i]

    with cols[i]:

        st.markdown(f"""
<div class="flow-card">

<div class="flow-number">

{no}

</div>

<div style="font-size:48px;margin-bottom:15px;">

{icon}

</div>

<div class="flow-title">

{title}

</div>

<div class="flow-desc">

{desc}

</div>

</div>
""", unsafe_allow_html=True)

st.markdown("<div style='text-align:center;font-size:35px;'>⬇️</div>", unsafe_allow_html=True)

# ==========================================================
# BARIS 2
# ==========================================================

cols = st.columns(3)

for i in range(3,6):

    no,icon,title,desc = flow_data[i]

    with cols[i-3]:

        st.markdown(f"""
<div class="flow-card">

<div class="flow-number">

{no}

</div>

<div style="font-size:48px;margin-bottom:15px;">

{icon}

</div>

<div class="flow-title">

{title}

</div>

<div class="flow-desc">

{desc}

</div>

</div>
""", unsafe_allow_html=True)

st.markdown("<div style='text-align:center;font-size:35px;'>⬇️</div>", unsafe_allow_html=True)

# ==========================================================
# BARIS 3
# ==========================================================

cols = st.columns(3)

for i in range(6,9):

    no,icon,title,desc = flow_data[i]

    with cols[i-6]:

        st.markdown(f"""
<div class="flow-card">

<div class="flow-number">

{no}

</div>

<div style="font-size:48px;margin-bottom:15px;">

{icon}

</div>

<div class="flow-title">

{title}

</div>

<div class="flow-desc">

{desc}

</div>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# PENJELASAN
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.info("""

💡 **Cara kerja sistem**

Dataset servis yang diunggah akan melalui proses preprocessing dan feature engineering.
Selanjutnya data diubah ke bentuk numerik melalui proses encoding, kemudian dibagi
menjadi data latih dan data uji. Model Random Forest membangun banyak Decision Tree
untuk mempelajari pola data, kemudian melakukan klasifikasi menggunakan mekanisme
**Majority Voting**. Hasil pelatihan dievaluasi menggunakan Accuracy, Confusion Matrix,
Classification Report, dan Feature Importance sebelum digunakan untuk melakukan prediksi
layanan servis kendaraan Yamaha.

""")
# ==========================================================
# FITUR SISTEM
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
🚀 Fitur Utama Sistem
</div>

<div class="section-desc">
Fitur-fitur yang tersedia pada Sistem Klasifikasi Layanan Servis Yamaha.
</div>
""", unsafe_allow_html=True)

fitur1, fitur2, fitur3 = st.columns(3)

with fitur1:

    st.markdown("""

<div class="feature-box">

<div class="feature-icon">
📂
</div>

<div class="feature-title">
Upload Dataset
</div>

<div class="feature-desc">

Mendukung dataset format
CSV maupun Excel
untuk proses pelatihan model.

</div>

</div>

""", unsafe_allow_html=True)

with fitur2:

    st.markdown("""

<div class="feature-box">

<div class="feature-icon">
🌲
</div>

<div class="feature-title">
Random Forest
</div>

<div class="feature-desc">

Model membangun banyak
Decision Tree untuk
mempelajari pola data servis.

</div>

</div>

""", unsafe_allow_html=True)

with fitur3:

    st.markdown("""

<div class="feature-box">

<div class="feature-icon">
📊
</div>

<div class="feature-title">
Evaluasi Model
</div>

<div class="feature-desc">

Menampilkan Accuracy,
Confusion Matrix,
Classification Report,
dan Feature Importance.

</div>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# INFORMASI SISTEM
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

col1,col2 = st.columns([1.2,1])

with col1:

    st.markdown("""

<div class="rf-box">

<h2 style="color:#14332a;">
🎯 Tujuan Sistem
</h2>

<p style="line-height:1.9;color:#475569;font-size:16px;">

Sistem ini dikembangkan untuk membantu proses
klasifikasi layanan servis kendaraan Yamaha
menggunakan algoritma <b>Random Forest</b>.

Model mempelajari pola dari data servis
berdasarkan fitur seperti:

<ul>

<li>Jenis Motor</li>

<li>Usia Motor</li>

<li>Kilometer</li>

<li>Indikasi</li>

<li>Qty</li>

</ul>

Hasil pembelajaran digunakan untuk
mengklasifikasikan layanan servis menjadi
<b>Service Ringan</b> atau
<b>Service Berat</b>.

</p>

</div>

""", unsafe_allow_html=True)

with col2:

    st.markdown("""

<div class="rf-box">

<h2 style="color:#14332a;">
🛠 Teknologi
</h2>

<table width="100%" style="font-size:16px;">

<tr>
<td><b>Bahasa</b></td>
<td>Python</td>
</tr>

<tr>
<td><b>Framework</b></td>
<td>Streamlit</td>
</tr>

<tr>
<td><b>Machine Learning</b></td>
<td>Random Forest</td>
</tr>

<tr>
<td><b>Library</b></td>
<td>Scikit-Learn</td>
</tr>

<tr>
<td><b>Visualisasi</b></td>
<td>Matplotlib</td>
</tr>

<tr>
<td><b>Laporan</b></td>
<td>PDF Report</td>
</tr>

</table>

</div>

""", unsafe_allow_html=True)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.success(
"""
✅ Selamat datang di Sistem Klasifikasi Layanan Servis Yamaha.

Gunakan menu pada sidebar untuk memulai proses klasifikasi,
melatih model Random Forest, melihat visualisasi Decision Tree,
mengevaluasi performa model, dan menghasilkan laporan PDF.
"""
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<hr>

<div style="text-align:center;
font-size:15px;
color:#64748b;
line-height:1.8;">

<b>Sistem Klasifikasi Layanan Servis Yamaha</b><br>

Penerapan Algoritma Random Forest untuk Klasifikasi Layanan Servis Kendaraan Yamaha<br><br>

© 2026 | Universitas Putra Indonesia "YPTK" Padang

</div>
""", unsafe_allow_html=True)
