import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from pathlib import Path

from utils.preprocessing import preprocess_data
from utils.training import train_model

# =========================================
# LOAD CSS
# =========================================
BASE_DIR = Path(__file__).parent.parent

css_path = BASE_DIR / "global.css"

with open(css_path) as f:

    st.markdown(

        f"<style>{f.read()}</style>",

        unsafe_allow_html=True
    )

# =========================================
# TITLE
# =========================================
st.title("⚙️ Training Random Forest")

st.markdown("""
Halaman training model klasifikasi layanan servis Yamaha.
""")

# =========================================
# UPLOAD DATASET
# =========================================
uploaded_file = st.file_uploader(
    "📂 Upload Dataset",
    type=['csv']
)

# =========================================
# PROCESS
# =========================================
if uploaded_file:

    # =========================
    # LOAD DATASET
    # =========================
    df = pd.read_csv(uploaded_file)

    st.success(
        "✅ Dataset berhasil diupload"
    )

    # =========================
    # PREPROCESSING
    # =========================
    X, y = preprocess_data(df)

    # =========================
    # BUTTON
    # =========================
    if st.button("🚀 Training Model"):

        (
            model,
            accuracy,
            precision,
            recall,
            f1,
            report,
            matrix,
            feature_names
        ) = train_model(X, y)

        # =========================
        # SAVE MODEL
        # =========================
        model_dir = BASE_DIR / "model"

        model_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        model_path = (
            model_dir / "random_forest_model.pkl"
        )

        feature_path = (
            model_dir / "feature_columns.pkl"
        )

        # =========================
        # SAVE
        # =========================
        joblib.dump(
            model,
            model_path
        )

        joblib.dump(
            list(feature_names),
            feature_path
        )

        st.success(
            "✅ Model berhasil disimpan"
        )

        # =========================
        # METRIK
        # =========================
        st.subheader("📊 Hasil Evaluasi")

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
        # REPORT
        # =========================
        st.subheader(
            "📋 Classification Report"
        )

        st.text(report)

        # =========================
        # CONFUSION MATRIX
        # =========================
        st.subheader(
            "📉 Confusion Matrix"
        )

        fig, ax = plt.subplots(figsize=(6,5))

        sns.heatmap(

            matrix,

            annot=True,
            fmt='d',

            cmap='Reds',

            ax=ax
        )

        ax.set_xlabel("Prediksi")
        ax.set_ylabel("Aktual")

        st.pyplot(fig)
