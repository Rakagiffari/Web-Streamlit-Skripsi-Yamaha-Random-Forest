import streamlit as st
import pandas as pd

st.title("📊 Dashboard Dataset")

uploaded_file = st.file_uploader(
    "📂 Upload Dataset CSV",
    type=['csv']
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success(
        "Dataset berhasil diupload"
    )

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

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
