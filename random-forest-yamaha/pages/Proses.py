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

        X, y = preprocess_data(df)
