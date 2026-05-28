import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from pathlib import Path

from utils.preprocessing import preprocess_data
from utils.training import train_model

# =====================================
# TITLE
# =====================================
st.title("⚙️ Training Random Forest")

# =====================================
# UPLOAD DATASET
# =====================================
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
    with st.spinner("Melakukan preprocessing..."):

        X, y, label_encoders, target_encoder = preprocess_data(df)

    st.success("Preprocessing selesai")

    # =========================
    # TRAIN MODEL
    # =========================
    if st.button("🚀 Training Model"):

        with st.spinner("Melakukan training model..."):

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

                # =========================
                # MEMBUAT FOLDER MODEL
                # =========================
                BASE_DIR = Path(__file__).parent.parent

                model_dir = BASE_DIR / "model"

                model_dir.mkdir(exist_ok=True)

                # =========================
                # SAVE MODEL
                # =========================
                model_path = model_dir / "random_forest_model.pkl"

                joblib.dump(model, model_path)

                # =========================
                # VALIDASI MODEL
                # =========================
                if model_path.exists():

                    file_size = model_path.stat().st_size

                    if file_size > 0:

                        st.success(
                            "Model berhasil ditraining dan disimpan"
                        )

                        st.write(
                            f"Ukuran model: {file_size / 1024:.2f} KB"
                        )

                    else:

                        st.error(
                            "Model gagal disimpan (file kosong)"
                        )

                else:

                    st.error(
                        "File model tidak ditemukan"
                    )

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

            except Exception as e:

                st.error(
                    f"Terjadi error saat training: {e}"
                )
