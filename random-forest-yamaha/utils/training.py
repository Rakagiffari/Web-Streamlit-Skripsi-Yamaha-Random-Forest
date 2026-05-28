import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from utils.preprocessing import preprocess_data
from utils.training import train_model

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Random Forest Yamaha",
    page_icon="⚙️",
    layout="wide"
)

# =========================
# TITLE
# =========================
st.title("⚙️ Training Random Forest")
st.markdown("Sistem klasifikasi layanan servis Yamaha menggunakan algoritma Random Forest")

# =========================
# FILE UPLOAD
# =========================
uploaded_file = st.file_uploader(
    "📂 Upload Dataset CSV",
    type=["csv"]
)

# =========================
# PROCESS DATA
# =========================
if uploaded_file is not None:

    # Load dataset
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Preview Dataset")
    st.dataframe(df.head())

    # Preprocessing
    with st.spinner("Melakukan preprocessing data..."):

        X, y, label_encoders, target_encoder = preprocess_data(df)

    st.success("✅ Preprocessing selesai")

    # =========================
    # TRAIN BUTTON
    # =========================
    if st.button("🚀 Training Model"):

        progress_bar = st.progress(0)
        status_text = st.empty()

        # Fake loading animation
        for i in range(100):
            progress_bar.progress(i + 1)
            status_text.text(f"Training model... {i+1}%")

        # Training model
        (
            model,
            accuracy,
            precision,
            recall,
            f1,
            report,
            matrix
        ) = train_model(X, y)

        # Save model
        joblib.dump(
            model,
            "model/random_forest_model.pkl"
        )

        st.success("✅ Model berhasil ditraining")

        # =========================
        # METRICS
        # =========================
        st.subheader("📊 Evaluasi Model")

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

        st.code(report)

        # =========================
        # CONFUSION MATRIX
        # =========================
        st.subheader("📉 Confusion Matrix")

        fig, ax = plt.subplots(figsize=(6, 4))

        sns.heatmap(
            matrix,
            annot=True,
            fmt='d',
            cmap='Reds',
            ax=ax
        )

        ax.set_xlabel("Predicted")
        ax.set_ylabel("Actual")

        st.pyplot(fig)

        # =========================
        # FEATURE IMPORTANCE
        # =========================
        st.subheader("🔥 Feature Importance")

        importance_df = pd.DataFrame({
            "Feature": X.columns,
            "Importance": model.feature_importances_
        }).sort_values(
            by="Importance",
            ascending=False
        )

        st.dataframe(importance_df)

        fig2, ax2 = plt.subplots(figsize=(10, 5))

        sns.barplot(
            data=importance_df.head(10),
            x="Importance",
            y="Feature",
            ax=ax2
        )

        st.pyplot(fig2)
