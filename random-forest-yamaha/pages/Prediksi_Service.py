import streamlit as st
import pandas as pd
import joblib

from pathlib import Path

from utils.preprocessing import preprocess_data

st.title("🔍 Prediksi Service")

# =========================
# LOAD MODEL
# =========================
BASE_DIR = Path(__file__).parent.parent

model_path = (
    BASE_DIR / "model" / "random_forest_model.pkl"
)

if not model_path.exists():

    st.warning(
        "Silakan training model terlebih dahulu."
    )

else:

    model = joblib.load(model_path)

    # =========================
    # UPLOAD DATA
    # =========================
    uploaded_file = st.file_uploader(

        "📂 Upload Data Prediksi CSV",

        type=['csv']
    )

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

        st.subheader("📋 Data Input")

        st.dataframe(df)

        # =========================
        # PREPROCESS
        # =========================
        X, y = preprocess_data(df)

        # =========================
        # PREDIKSI
        # =========================
        prediction = model.predict(X)

        hasil = []

        for pred in prediction:

            if pred == 1:

                hasil.append("Service Berat")

            else:

                hasil.append("Service Ringan")

        df["Hasil Prediksi"] = hasil

        # =========================
        # HASIL
        # =========================
        st.subheader("✅ Hasil Prediksi")

        st.dataframe(df)
