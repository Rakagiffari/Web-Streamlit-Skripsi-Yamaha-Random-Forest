import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from utils.preprocessing import preprocess_data
from utils.training import train_model

st.title("⚙️ Training Random Forest")

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
    with st.spinner("Melakukan preprocessing..."):

        X, y, label_encoders, target_encoder = preprocess_data(df)

    st.success("Preprocessing selesai")

    # =========================
    # TRAINING MODEL
    # =========================
    if st.button("🚀 Training Model"):

        progress = st.progress(0)

        for i in range(100):
            progress.progress(i + 1)

        (
            model,
            accuracy,
            precision,
            recall,
            f1,
            report,
            matrix
        ) = train_model(X, y)

        # Simpan model
        joblib.dump(
            model,
            'model/random_forest_model.pkl'
        )

        st.success("Model berhasil ditraining")

        # =========================
        # METRIK EVALUASI
        # =========================
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Accuracy",
                f"{accuracy:.2%}"
            )

        with col2:
            st.metric(
                "Precision",
                f"{precision:.2%}"
            )

        with col3:
            st.metric(
                "Recall",
                f"{recall:.2%}"
            )

        with col4:
            st.metric(
                "F1 Score",
                f"{f1:.2%}"
            )

        # =========================
        # CLASSIFICATION REPORT
        # =========================
        st.subheader("📋 Classification Report")

        st.text(report)

        # =========================
        # CONFUSION MATRIX
        # =========================
        st.subheader("📉 Confusion Matrix")

        fig, ax = plt.subplots(figsize=(5, 4))

        sns.heatmap(
            matrix,
            annot=True,
            fmt='d',
            cmap='Reds',
            ax=ax
        )

        st.pyplot(fig)
