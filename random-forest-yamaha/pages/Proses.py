import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from pathlib import Path
from datetime import datetime

from utils.preprocessing import preprocess_data
from utils.training import train_model
from utils.report import generate_pdf

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="Training Random Forest",
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
}

.sub-title{
    color:#9ca3af;
    font-size:16px;
    margin-top:-8px;
}

.block-title{
    font-size:22px;
    font-weight:bold;
    margin-top:10px;
}

hr{
    margin-top:20px;
    margin-bottom:20px;
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
# UPLOAD DATASET
# =========================================

uploaded_file = st.file_uploader(
    "📂 Upload Dataset",
    type=["csv","xlsx","xls"]
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

        elif uploaded_file.name.endswith((".xlsx",".xls")):

            df = pd.read_excel(uploaded_file)

        else:

            st.error("Format file tidak didukung")
            st.stop()

        # =====================================
        # VALIDASI DATASET
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

        if len(missing_columns)>0:

            st.error(
                f"Kolom berikut tidak ditemukan : {missing_columns}"
            )

            st.stop()

        # =====================================
        # DATASET BERHASIL
        # =====================================

        st.success("✅ Dataset berhasil diupload")

        c1,c2,c3 = st.columns(3)

        with c1:

            st.metric(
                "Jumlah Data",
                len(df)
            )

        with c2:

            st.metric(
                "Jumlah Kolom",
                len(df.columns)
            )

        with c3:

            st.metric(
                "Jumlah Kelas",
                df["Service"].nunique()
            )

        st.markdown("---")

        # =====================================
        # PREVIEW DATASET
        # =====================================

        st.markdown("## 📄 Preview Dataset")

        st.dataframe(

            df.head(10),

            use_container_width=True,

            hide_index=True

        )

        # =====================================
        # INFORMASI DATASET
        # =====================================

        st.markdown("## 📊 Informasi Dataset")

        total_missing = df.isnull().sum().sum()

        total_duplicate = df.duplicated().sum()

        numeric_columns = len(

            df.select_dtypes(include="number").columns

        )

        categorical_columns = len(

            df.select_dtypes(include=["object"]).columns

        )

        c1,c2,c3,c4 = st.columns(4)

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
                "Kolom Numerik",
                numeric_columns
            )

        with c4:

            st.metric(
                "Kolom Kategori",
                categorical_columns
            )

        st.markdown("### Missing Value per Kolom")

        missing_df = pd.DataFrame({

            "Kolom":df.columns,

            "Jumlah Missing":df.isnull().sum().values

        })

        st.dataframe(

            missing_df,

            use_container_width=True,

            hide_index=True

        )

        st.markdown("---")
        
