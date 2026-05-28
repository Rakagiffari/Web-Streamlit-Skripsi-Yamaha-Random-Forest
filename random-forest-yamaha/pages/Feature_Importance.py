import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

from utils.preprocessing import preprocess_data

st.title("📈 Feature Importance")

uploaded_file = st.file_uploader(
    "📂 Upload Dataset",
    type=['csv']
)

if uploaded_file:

    # Membaca dataset
    df = pd.read_csv(uploaded_file)

    # =========================
    # PREPROCESSING
    # =========================
    X, y, label_encoders, target_encoder = preprocess_data(df)

    # =========================
    # LOAD MODEL
    # =========================
    model = joblib.load(
        'model/random_forest_model.pkl'
    )

    # =========================
    # FEATURE IMPORTANCE
    # =========================
    importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': model.feature_importances_
    })

    importance = importance.sort_values(
        by='Importance',
        ascending=False
    )

    # =========================
    # VISUALISASI
    # =========================
    fig = px.bar(
        importance.head(10),
        x='Importance',
        y='Feature',
        orientation='h',
        title='Top Feature Importance'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
