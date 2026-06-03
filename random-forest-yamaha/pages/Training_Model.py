import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from pathlib import Path

from utils.preprocessing import preprocess_data
from utils.training import train_model


# ========================================
# TITLE
# ========================================
st.title("⚙️ Training Random Forest")


# ========================================
# FILE UPLOAD
# ========================================
uploaded_file = st.file_uploader(
    "📂 Upload Dataset",
    type=["csv"]
)


# ========================================
# MAIN
# ========================================
if uploaded_file is not None:

    try:

        # ========================================
        # READ DATASET
        # ========================================
        df = pd.read_csv(
            uploaded_file
        )

        st.success(
            "Dataset berhasil diupload"
        )

        # ========================================
        # PREVIEW
        # ========================================
        st.subheader(
            "📄 Preview Dataset"
        )

        st.dataframe(
            df.head()
        )

        # ========================================
        # VALIDASI TARGET
        # ========================================
        if "Service" not in df.columns:

            st.error(
                "Kolom 'Service' tidak ditemukan"
            )

            st.stop()

        # ========================================
        # PREPROCESSING
        # ========================================
        X, y = preprocess_data(df)

        st.success(
            "Preprocessing berhasil"
        )

        # ========================================
        # INFO DATA
        # ========================================
        st.subheader(
            "📊 Informasi Dataset"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"Jumlah Data: {len(df)}"
            )

        with col2:

            st.write(
                f"Jumlah Fitur: {X.shape[1]}"
            )

        # ========================================
        # DISTRIBUSI TARGET
        # ========================================
        st.subheader(
            "📌 Distribusi Target"
        )

        st.write(
            df["Service"].value_counts()
        )

        # ========================================
        # VALIDASI JUMLAH KELAS
        # ========================================
        if len(y.unique()) < 2:

            st.error(
                "Target hanya memiliki 1 kelas"
            )

            st.stop()

        # ========================================
        # BUTTON TRAINING
        # ========================================
        if st.button("🚀 Training Model"):

            with st.spinner(
                "Sedang training model..."
            ):

                try:

                    (
                        model,
                        accuracy,
                        precision,
                        recall,
                        f1,
                        report,
                        matrix
                    ) = train_model(X, y)

                except Exception as e:

                    st.error(
                        f"Error training: {e}"
                    )

                    st.stop()

            # ========================================
            # SAVE MODEL
            # ========================================
            BASE_DIR = Path(__file__).parent.parent

            model_dir = BASE_DIR / "model"

            model_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            model_path = (
                model_dir /
                "random_forest_model.pkl"
            )

            joblib.dump(
                model,
                model_path
            )

            st.success(
                "Model berhasil disimpan"
            )

            # ========================================
            # METRICS
            # ========================================
            st.subheader(
                "📈 Hasil Evaluasi"
            )

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

            # ========================================
            # REPORT
            # ========================================
            st.subheader(
                "📋 Classification Report"
            )

            st.text(report)

            # ========================================
            # CONFUSION MATRIX
            # ========================================
            st.subheader(
                "📉 Confusion Matrix"
            )

            fig, ax = plt.subplots(
                figsize=(5, 4)
            )

            sns.heatmap(
                matrix,
                annot=True,
                fmt="d",
                cmap="Reds",
                ax=ax
            )

            ax.set_xlabel(
                "Prediksi"
            )

            ax.set_ylabel(
                "Aktual"
            )

            st.pyplot(fig)

    except Exception as e:

        st.error(
            f"Terjadi error: {e}"
        )
