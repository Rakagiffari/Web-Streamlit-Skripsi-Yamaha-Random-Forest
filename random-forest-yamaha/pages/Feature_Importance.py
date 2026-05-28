import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

from pathlib import Path
from utils.preprocessing import preprocess_data

st.title("📈 Feature Importance")

uploaded_file = st.file_uploader(
    "📂 Upload Dataset",
    type=['csv']
)

if uploaded_file:

    # =========================
    # LOAD DATASET
    # =========================
    df = pd.read_csv(uploaded_file)

    X, y, label_encoders, target_encoder = preprocess_data(df)

    # =========================
    # LOAD MODEL
    # =========================
    BASE_DIR = Path(__file__).parent.parent

    model_path = BASE_DIR / "model" / "random_forest_model.pkl"

    if not model_path.exists():

        st.warning(
            "Model belum tersedia. Silakan training model terlebih dahulu."
        )

    else:

        model = joblib.load(model_path)

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
