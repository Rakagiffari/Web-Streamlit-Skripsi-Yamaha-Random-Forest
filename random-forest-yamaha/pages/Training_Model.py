import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from pathlib import Path

from utils.preprocessing import preprocess_data
from utils.training import train_model

st.title("⚙️ Training Random Forest")

uploaded_file = st.file_uploader(
    "📂 Upload Dataset",
    type=['csv']
)

if uploaded_file:

    # =========================
    # LOAD DATASET
    # =========================

    df = pd.read_csv(uploaded_file)

    st.success("Dataset berhasil diupload")

    # =========================
    # PREPROCESSING
    # =========================

    X, y = preprocess_data(df)

    st.info(f"Jumlah fitur setelah preprocessing: {X.shape[1]}")

    # =========================
    # BUTTON TRAINING
    # =========================

    if st.button("🚀 Training Model"):

        try:

            (
                model,
                accuracy,
                precision,
                recall,
                f1,
                report,
                matrix,
                importance_df
            ) = train_model(X, y)

            # =========================
            # SAVE MODEL
            # =========================

            BASE_DIR = Path(__file__).parent.parent

            model_dir = BASE_DIR / "model"

            model_dir.mkdir(

                parents=True,
                exist_ok=True

            )

            model_path = (
                model_dir / "random_forest_model.pkl"
            )

            joblib.dump(model, model_path)

            # =========================
            # SUCCESS
            # =========================

            st.success(
                "Model berhasil ditraining dan disimpan!"
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
            # CLASSIFICATION REPORT
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

            fig, ax = plt.subplots(figsize=(5, 4))

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

            # =========================
            # FEATURE IMPORTANCE
            # =========================

            st.subheader(
                "🔥 Feature Importance"
            )

            st.dataframe(

                importance_df,

                use_container_width=True

            )

            # =========================
            # BARPLOT IMPORTANCE
            # =========================

            fig2, ax2 = plt.subplots(figsize=(8, 5))

            sns.barplot(

                data=importance_df,

                x='Importance',
                y='Fitur',

                palette='Reds',

                ax=ax2

            )

            ax2.set_title("Feature Importance")

            st.pyplot(fig2)

        except Exception as e:

            st.error(f"Error training: {e}")
