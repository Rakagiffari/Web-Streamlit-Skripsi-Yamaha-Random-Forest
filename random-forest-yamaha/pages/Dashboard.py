import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard Analitik")

uploaded_file = st.file_uploader(
    "📂 Upload Dataset CSV",
    type=['csv']
)

if uploaded_file:

    # Membaca dataset
    df = pd.read_csv(uploaded_file)

    st.success("Dataset berhasil diupload")

    # Membuat tab
    tab1, tab2, tab3 = st.tabs([
        "Dataset",
        "Visualisasi",
        "Informasi"
    ])

    # =========================
    # TAB DATASET
    # =========================
    with tab1:

        st.dataframe(
            df.head(20),
            use_container_width=True
        )

    # =========================
    # TAB VISUALISASI
    # =========================
    with tab2:

        if 'Service' in df.columns:

            fig = px.histogram(
                df,
                x='Service',
                color='Service',
                title='Distribusi Layanan Service'
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # =========================
    # TAB INFORMASI
    # =========================
    with tab3:

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
