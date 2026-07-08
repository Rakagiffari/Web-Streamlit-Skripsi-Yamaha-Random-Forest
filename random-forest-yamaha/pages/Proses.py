import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from pathlib import Path

from utils.preprocessing import preprocess_data
from utils.training import train_model
from utils.report import generate_pdf

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="Training Model",
    page_icon="⚙️",
    layout="wide"
)

# =========================================
# STYLE
# =========================================

st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:700;
    color:white;
    margin-bottom:0px;
}

.sub-title{
    color:#9ca3af;
    font-size:16px;
    margin-top:-10px;
}

.metric-card{
    background:#1f2937;
    padding:20px;
    border-radius:16px;
    text-align:center;
}

.metric-label{
    color:#9ca3af;
    font-size:15px;
}

.metric-value{
    color:white;
    font-size:30px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown(
    '<p class="main-title">⚙️ Training Random Forest</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Random Forest untuk Klasifikasi Layanan Service Kendaraan Yamaha</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# =========================================
# FILE UPLOAD
# =========================================

uploaded_file = st.file_uploader(
    "📂 Upload Dataset",
    type=["csv", "xlsx", "xls"]
)

# =========================================
# MAIN
# =========================================

if uploaded_file is not None:

    try:

        # =====================================
        # MEMBACA DATASET
        # =====================================

        if uploaded_file.name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)

        elif uploaded_file.name.endswith((".xlsx", ".xls")):

            df = pd.read_excel(uploaded_file)

        else:

            st.error("Format file tidak didukung.")
            st.stop()

        # =====================================
        # VALIDASI KOLOM
        # =====================================

        required_columns = [

            "Model",
            "Tahun",
            "Km",
            "Indikasi",
            "Service"

        ]

        missing_columns = [

            col
            for col in required_columns
            if col not in df.columns

        ]

        if missing_columns:

            st.error(
                f"Kolom berikut tidak ditemukan:\n{', '.join(missing_columns)}"
            )

            st.stop()

        # =====================================
        # DATASET BERHASIL
        # =====================================

        st.success("✅ Dataset berhasil diupload")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Nama File",
                uploaded_file.name
            )

        with col2:

            st.metric(
                "Jumlah Data",
                len(df)
            )

        with col3:

            st.metric(
                "Jumlah Kolom",
                len(df.columns)
            )

        # =====================================
        # PREVIEW DATASET
        # =====================================

        st.markdown("## 📄 Preview Dataset")

        st.dataframe(
            df.head(),
            use_container_width=True,
            hide_index=True
        )

        # =====================================
        # INFORMASI DATASET
        # =====================================

        st.markdown("## 📊 Informasi Dataset")

        total_missing = df.isnull().sum().sum()

        total_duplicate = df.duplicated().sum()

        numeric_cols = len(
            df.select_dtypes(include="number").columns
        )

        categorical_cols = len(
            df.select_dtypes(include=["object", "category"]).columns
        )

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Missing Value",
                total_missing
            )

        with c2:

            st.metric(
                "Data Duplikat",
                total_duplicate
            )

        with c3:

            st.metric(
                "Jumlah Kelas",
                df["Service"].nunique()
            )

        # =====================================
        # INFORMASI TIPE DATA
        # =====================================

        st.markdown("### 🧾 Ringkasan Tipe Data")

        info_df = pd.DataFrame({

            "Informasi": [

                "Kolom Numerik",
                "Kolom Kategori"

            ],

            "Jumlah": [

                numeric_cols,
                categorical_cols

            ]

        })

        st.dataframe(
            info_df,
            use_container_width=True,
            hide_index=True
        )

        # =====================================
        # MISSING VALUE
        # =====================================

        st.markdown("### 🔍 Missing Value per Kolom")

        missing_df = (

            df.isnull()
            .sum()
            .reset_index()

        )

        missing_df.columns = [

            "Kolom",
            "Jumlah Missing"

        ]

        st.dataframe(

            missing_df,

            use_container_width=True,

            hide_index=True

        )

        # =====================================
        # DUPLIKAT
        # =====================================

        st.markdown("### 📑 Informasi Data Duplikat")

        dup1, dup2 = st.columns(2)

        with dup1:

            st.metric(
                "Sebelum Hapus",
                len(df)
            )

        with dup2:

            st.metric(
                "Jumlah Duplikat",
                total_duplicate
            )

        st.markdown("---")
        # =====================================
        # PREPROCESSING
        # =====================================

        with st.spinner("Sedang melakukan preprocessing data..."):

    X, y = preprocess_data(df)

st.success("✅ Preprocessing berhasil dilakukan")

st.markdown("## ⚙️ Hasil Preprocessing")

# =====================================
# INFORMASI PREPROCESSING
# =====================================

tahun_sekarang = pd.Timestamp.now().year

preview_df = df.copy()

# -----------------------------
# Feature Engineering
# -----------------------------

preview_df["Usia Motor"] = tahun_sekarang - preview_df["Tahun"]

def get_jenis(model):

    model = str(model).upper()

    if any(x in model for x in [
        "XMAX","NMAX","AEROX","LEXI","TMAX"
    ]):
        return "MAXi"

    elif any(x in model for x in [
        "FAZZIO","FILANO"
    ]):
        return "Classy"

    elif any(x in model for x in [
        "MIO","SOUL","XEON",
        "FINO","GEAR",
        "FREEGO","X-RIDE",
        "XRIDE","NOUVO",
        "LEXAM"
    ]):
        return "Matic"

    elif any(x in model for x in [
        "R15","R25","R6","R1",
        "VIXION","BYSON",
        "SCORPIO","RX",
        "XSR","MT"
    ]):
        return "Sport"

    elif any(x in model for x in [
        "WR","YZ"
    ]):
        return "Off-road"

    elif any(x in model for x in [
        "JUPITER","VEGA",
        "CRYPTON","ALFA",
        "SIGMA","F1ZR",
        "MX KING"
    ]):
        return "Moped"

    return "Unknown"

preview_df["Jenis"] = preview_df["Model"].apply(get_jenis)

# =====================================
# STATUS PREPROCESSING
# =====================================

st.markdown("### 📋 Status Tahapan Preprocessing")

status_df = pd.DataFrame({

    "Tahapan":[

        "Validasi Dataset",
        "Pengecekan Missing Value",
        "Pengecekan Data Duplikat",
        "Feature Engineering",
        "Encoding Dataset"

    ],

    "Status":[

        "✅ Berhasil",
        "✅ Berhasil",
        "✅ Berhasil",
        "✅ Berhasil",
        "✅ Berhasil"

    ]

})

st.dataframe(
    status_df,
    use_container_width=True,
    hide_index=True
)

# =====================================
# RINGKASAN PREPROCESSING
# =====================================

st.markdown("### 📊 Ringkasan Hasil Preprocessing")

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "Jumlah Data",
        len(preview_df)
    )

with c2:

    st.metric(
        "Jumlah Fitur",
        X.shape[1]
    )

with c3:

    st.metric(
        "Jumlah Target",
        y.nunique()
    )

with c4:

    st.metric(
        "Fitur Setelah Encoding",
        X.shape[1]
    )

# =====================================
# HASIL FEATURE ENGINEERING
# =====================================

st.markdown("## 🛠 Hasil Feature Engineering")

st.info(
    "Feature Engineering menghasilkan dua fitur baru yaitu **Jenis Motor** "
    "dan **Usia Motor** yang akan digunakan pada proses klasifikasi."
)

feature_df = preview_df[

    [

        "Indikasi",
        "Model",
        "Jenis",
        "Tahun",
        "Usia Motor",
        "Km",
        "Service"

    ]

].head(10)

st.dataframe(
    feature_df,
    use_container_width=True,
    hide_index=True
)

# =====================================
# INFORMASI FITUR MODEL
# =====================================

st.markdown("### 📌 Fitur yang Digunakan")

fitur_df = pd.DataFrame({

    "Fitur":[

        "Indikasi",
        "Jenis",
        "Km",
        "Usia Motor"

    ],

    "Keterangan":[

        "Kategori indikasi kerusakan",
        "Hasil Feature Engineering",
        "Kilometer kendaraan",
        "Hasil Feature Engineering"

    ]

})

st.dataframe(
    fitur_df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

            # =====================================
            # PDF
            # =====================================

            logo_path = (
                BASE_DIR /
                "assets" /
                "yamaha_logo.png"
            )

            pdf_path = generate_pdf(

                pdf_path=
                "laporan_training_model.pdf",

                logo_path=
                str(logo_path),

                total_data=
                len(df),

                train_data=
                train_count,

                test_data=
                test_count,

                accuracy=
                accuracy,

                precision=
                precision,

                recall=
                recall,

                f1=
                f1,

                cm_image=
                str(cm_path),

                fi_image=
                str(fi_path),

                top_features=
                importance_grouped[
                    "Fitur"
                ].head(5).tolist()
            )

            with open(
                pdf_path,
                "rb"
            ) as pdf_file:

                st.download_button(

                    "📄 Download Laporan",

                    pdf_file,

                    file_name=
                    "Laporan_Training_Model.pdf",

                    mime=
                    "application/pdf"
                )

    except Exception as e:

        st.error(
            f"Terjadi error: {e}"
        )
