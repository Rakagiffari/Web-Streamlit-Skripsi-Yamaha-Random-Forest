import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import time

from pathlib import Path

from utils.preprocessing import preprocess_data
from utils.training import train_model
from utils.report import generate_pdf

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Training Random Forest",
    page_icon="⚙️",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================

if "dataset_loaded" not in st.session_state:
    st.session_state.dataset_loaded = False

if "dataset_ready" not in st.session_state:
    st.session_state.dataset_ready = False

if "training_done" not in st.session_state:
    st.session_state.training_done = False

if "model_result" not in st.session_state:
    st.session_state.model_result = None

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

/* ================================
BACKGROUND
================================ */

.stApp{
    background:#020617;
}

/* ================================
HEADER
================================ */

.main-title{

    font-size:42px;

    font-weight:800;

    color:white;

    margin-bottom:0;

}

.sub-title{

    color:#94a3b8;

    font-size:16px;

    margin-top:-5px;

    margin-bottom:30px;

}

/* ================================
CARD
================================ */

.metric-card{

    background:linear-gradient(145deg,#111827,#1e293b);

    border:1px solid #334155;

    border-radius:18px;

    padding:18px;

    text-align:center;

}

.metric-title{

    color:#94a3b8;

    font-size:14px;

}

.metric-value{

    color:white;

    font-size:30px;

    font-weight:bold;

}

/* ================================
SECTION
================================ */

.section-title{

    color:white;

    font-size:22px;

    font-weight:700;

    margin-top:20px;

    margin-bottom:10px;

}

/* ================================
SUCCESS
================================ */

.stAlert{

    border-radius:15px;

}

/* ================================
UPLOAD
================================ */

[data-testid="stFileUploader"]{

    border-radius:15px;

}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="main-title">
⚙️ Training Random Forest
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">
Random Forest untuk Klasifikasi Layanan Service Kendaraan Yamaha
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =====================================================
# UPLOAD DATASET
# =====================================================

st.markdown("### 📂 Upload Dataset")

uploaded_file = st.file_uploader(

    "Upload file CSV atau Excel",

    type=["csv","xlsx","xls"]

)

# =====================================================
# BELUM ADA DATA
# =====================================================

if uploaded_file is None:

    st.info("Silakan upload dataset untuk memulai proses klasifikasi.")

    st.stop()

# =====================================================
# MEMBACA DATASET
# =====================================================

try:

    if uploaded_file.name.endswith(".csv"):

        df = pd.read_csv(uploaded_file)

    else:

        df = pd.read_excel(uploaded_file)

except Exception as e:

    st.error(e)

    st.stop()

# =====================================================
# VALIDASI KOLOM
# =====================================================

required_columns=[

    "Model",

    "Tahun",

    "Km",

    "Indikasi",

    "Service"

]

missing=[

    c

    for c in required_columns

    if c not in df.columns

]

if len(missing)>0:

    st.error(

        f"Kolom berikut tidak ditemukan : {', '.join(missing)}"

    )

    st.stop()

# =====================================================
# STATUS
# =====================================================

st.session_state.dataset_loaded=True

st.success("✅ Dataset berhasil diupload")

# =====================================================
# METRIC
# =====================================================

c1,c2,c3=st.columns(3)

with c1:

    st.markdown(f"""

    <div class="metric-card">

        <div class="metric-title">

        Nama File

        </div>

        <div class="metric-value">

        {uploaded_file.name}

        </div>

    </div>

    """,unsafe_allow_html=True)

with c2:

    st.markdown(f"""

    <div class="metric-card">

        <div class="metric-title">

        Jumlah Data

        </div>

        <div class="metric-value">

        {len(df)}

        </div>

    </div>

    """,unsafe_allow_html=True)

with c3:

    st.markdown(f"""

    <div class="metric-card">

        <div class="metric-title">

        Jumlah Kolom

        </div>

        <div class="metric-value">

        {len(df.columns)}

        </div>

    </div>

    """,unsafe_allow_html=True)

# =====================================================
# DATA SIAP DIPROSES
# =====================================================

st.session_state.dataset_ready=True

st.markdown("<br>",unsafe_allow_html=True)

st.success("🟢 Dataset valid dan siap diproses.")

# =====================================================
# PART 2 START
# =====================================================
# PROGRESS PIPELINE
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
📌 Progress Pipeline
</div>
""", unsafe_allow_html=True)

progress_placeholder = st.empty()
status_placeholder = st.empty()

# =====================================================
# JALANKAN PROGRESS SEKALI
# =====================================================

if "pipeline_finished" not in st.session_state:
    st.session_state.pipeline_finished = False

if not st.session_state.pipeline_finished:

    progress = progress_placeholder.progress(0)

    pipeline_steps = [

        ("📂 Membaca dataset...", 10),

        ("🔍 Memvalidasi struktur dataset...", 25),

        ("📊 Mengecek missing value...", 45),

        ("🧹 Mengecek data duplikat...", 60),

        ("⚙️ Menyiapkan proses preprocessing...", 80),

        ("✅ Dataset siap diproses...", 100)

    ]

    current = 0

    for text, target in pipeline_steps:

        status_placeholder.info(text)

        while current < target:

            current += 1

            progress.progress(current)

            time.sleep(0.01)

    status_placeholder.success(
        "🎉 Dataset berhasil diproses dan siap memasuki tahapan sistem."
    )

    st.session_state.pipeline_finished = True

else:

    progress_placeholder.progress(100)

    status_placeholder.success(
        "🎉 Dataset berhasil diproses dan siap memasuki tahapan sistem."
    )

# =====================================================
# STATUS PIPELINE
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
📍 Status Pipeline
</div>
""", unsafe_allow_html=True)

status_col1, status_col2 = st.columns(2)

with status_col1:

    st.success("✅ Upload Dataset")

    st.success("✅ Validasi Dataset")

    st.success("✅ Dataset Siap")

    st.info("⏳ Menunggu Preprocessing")

with status_col2:

    st.info("⚪ Random Forest")

    st.info("⚪ Evaluasi")

    st.info("⚪ Insight")

    st.info("⚪ Prediksi & Laporan")

# =====================================================
# ACCORDION
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
🛠 Tahapan Sistem
</div>
""", unsafe_allow_html=True)

# =====================================================
# STEP 1
# =====================================================

with st.expander(
    "① Upload Dataset",
    expanded=True
):

    st.info(
        "Preview dataset akan ditampilkan pada tahap ini."
    )

# =====================================================
# STEP 2
# =====================================================

with st.expander(
    "② Preprocessing"
):

    st.info(
        "Tahap preprocessing akan dibuat pada Part 3."
    )

# =====================================================
# STEP 3
# =====================================================

with st.expander(
    "③ Persiapan Data"
):

    st.info(
        "Feature Engineering dan Encoding akan dibuat pada Part 4."
    )

# =====================================================
# STEP 4
# =====================================================

with st.expander(
    "④ Random Forest"
):

    st.info(
        "Training Random Forest akan dibuat pada Part 5."
    )

# =====================================================
# STEP 5
# =====================================================

with st.expander(
    "⑤ Evaluasi Model"
):

    st.info(
        "Evaluasi model akan dibuat pada Part 6."
    )

# =====================================================
# STEP 6
# =====================================================

with st.expander(
    "⑥ Insight"
):

    st.info(
        "Insight otomatis akan dibuat pada Part 7."
    )

# =====================================================
# STEP 7
# =====================================================

with st.expander(
    "⑦ Prediksi"
):

    st.info(
        "Prediksi manual akan dibuat pada Part 8."
    )

# =====================================================
# STEP 8
# =====================================================

with st.expander(
    "⑧ Download Laporan"
):

    st.info(
        "Download PDF akan dibuat pada Part 9."
    )

# =====================================================
# PART 3 START
# =====================================================
#
# Upload Dataset
# Preview Dataset
# Ringkasan Dataset
#

