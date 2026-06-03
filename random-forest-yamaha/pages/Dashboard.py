import streamlit as st
import pandas as pd
import os

# =========================================
# LOAD CSS
# =========================================
css_path = os.path.join(

    os.path.dirname(__file__),

    "..",

    "styles",

    "global.css"
)

with open(css_path) as f:

    st.markdown(

        f"<style>{f.read()}</style>",

        unsafe_allow_html=True
    )

# =========================================
# TITLE
# =========================================
st.title("📊 Dashboard Dataset")

st.markdown("""
Menampilkan informasi dataset servis Yamaha.
""")

# =========================================
# UPLOAD DATASET
# =========================================
uploaded_file = st.file_uploader(
    "📂 Upload Dataset CSV",
    type=['csv']
)

# =========================================
# PROCESS
# =========================================
if uploaded_file:

    # =========================
    # READ CSV
    # =========================
    df = pd.read_csv(uploaded_file)

    # =========================
    # SUCCESS
    # =========================
    st.success(
        "✅ Dataset berhasil diupload"
    )

    # =========================
    # METRIC
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Jumlah Data",
            len(df)
        )

    with col2:

        st.metric(
            "Jumlah Kolom",
            len(df.columns)
        )

    with col3:

        st.metric(
            "Missing Value",
            df.isnull().sum().sum()
        )

    # =========================
    # SPACE
    # =========================
    st.markdown("<br>", unsafe_allow_html=True)

    # =========================
    # DATAFRAME
    # =========================
    st.subheader("📋 Preview Dataset")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

    # =========================
    # INFO KOLOM
    # =========================
    st.subheader("📑 Informasi Kolom")

    info_df = pd.DataFrame({

        "Nama Kolom": df.columns,
        "Tipe Data": df.dtypes.astype(str)

    })

    st.dataframe(
        info_df,
        use_container_width=True
    )
