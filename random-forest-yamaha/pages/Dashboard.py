import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard Dataset")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=['csv']
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Preview Dataset")
    st.dataframe(df.head())

    st.subheader("Informasi Dataset")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Jumlah Data", len(df))

    with col2:
        st.metric("Jumlah Kolom", len(df.columns))

    if 'Service' in df.columns:

        fig = px.histogram(
            df,
            x='Service',
            color='Service',
            title='Distribusi Service'
        )

        st.plotly_chart(fig, use_container_width=True)
