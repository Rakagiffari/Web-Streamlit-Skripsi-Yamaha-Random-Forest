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
    text-align: center;
    font-size: 43px;
    font-weight: 900;
    color: white;
    line-height: 1.1;
    margin-top: 5px;
    margin-bottom: 10px;
    letter-spacing: 1px;
}

.section-desc{
    text-align: center;
    color: #cbd5e1;
    font-size: 14px;
    margin-top: 0px;
    margin-bottom: 45px;
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
    font-size:30px;
    font-weight:700;
    color: #14332a;
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
    background: linear-gradient(145deg, #111827, #1e293b);
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
    box-shadow:0 0 20px rgba(239,68,68,0.25);
}

.flow-number{
    width:42px;
    height:42px;
    border-radius:50%;
    background:#ffffff;
    color:white;
    display:flex;
    align-items:center;
    justify-content:center;
    margin:auto;
    font-weight:bold;
    margin-bottom:18px;
}

.flow-title{
    font-size:14px;
    font-weight:700;
    color: white;
    margin-bottom:10px;
}

.flow-desc{
    color: white;
    font-size:15px;
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
# ALUR SISTEM
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div class="section-title">
        Alur Sistem Klasifikasi
    </div>
    <div class="section-desc">
        Tahapan proses klasifikasi layanan servis menggunakan algoritma Random Forest.
    </div>
""", unsafe_allow_html=True)

flow_data = [
    ("1","📂","Upload Dataset"),
    ("2","🧹","Preprocessing",),
    ("3","⚙️","Feature Engineering"),
    ("4","🔤","Encoding"),
    ("5","✂️","Train-Test Split"),
    ("6","🌲","Random Forest"),
    ("7","📊","Evaluasi Model"),
    ("8","🎯","Prediksi"),
    ("9","📄","Laporan PDF")
]
# ==========================================================
# BARIS 1
# ==========================================================
cols = st.columns(7)
for i in range(7):
    no,icon,title = flow_data[i]
    with cols[i]:
        st.markdown(f"""
            <div class="flow-card">
                <div class="flow-number">
                    {no}
                </div>
                <div style="font-size:35px;margin-bottom:15px;">
                    {icon}
                </div>

<div class="flow-title">

{title}

</div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
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
