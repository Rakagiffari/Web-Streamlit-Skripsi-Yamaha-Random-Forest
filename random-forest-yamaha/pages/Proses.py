import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from pathlib import Path

from utils.preprocessing import preprocess_data
from utils.training import train_model
from utils.report import generate_pdf


# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="Training Model",
    page_icon="⚙️",
    layout="wide"
)

# =========================================
# STYLE
# =========================================

st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:700;
    color:white;
    margin-bottom:0px;
}

.sub-title{
    color:#9ca3af;
    font-size:16px;
    margin-top:-10px;
}

.metric-card{
    background:#1f2937;
    padding:20px;
    border-radius:16px;
    text-align:center;
}

.metric-label{
    color:#9ca3af;
    font-size:15px;
}

.metric-value{
    color:white;
    font-size:30px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown(
    '<p class="main-title">⚙️ Training Random Forest</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Random Forest untuk Klasifikasi Layanan Service Kendaraan Yamaha</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# =========================================
# FILE UPLOAD
# =========================================

uploaded_file = st.file_uploader(
    "📂 Upload Dataset",
    type=["csv", "xlsx", "xls"]
)

# =========================================
# MAIN
# =========================================

if uploaded_file is not None:

    try:

        # =====================================
        # BACA FILE
        # =====================================

        if uploaded_file.name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)

        elif uploaded_file.name.endswith(".xlsx"):

            df = pd.read_excel(
                uploaded_file,
                engine="openpyxl"
            )

        elif uploaded_file.name.endswith(".xls"):

            df = pd.read_excel(
                uploaded_file
            )

        else:

            st.error(
                "Format file tidak didukung"
            )

            st.stop()

        # =====================================
        # VALIDASI KOLOM
        # =====================================

        required_columns = [

            "Brand",
            "Model",
            "Tahun",
            "Km",
            "Indikasi",
            "Qty",
            "Service"

        ]

        missing_columns = [

            col for col in required_columns
            if col not in df.columns

        ]

        if missing_columns:

            st.error(
                f"Kolom tidak ditemukan: {missing_columns}"
            )

            st.stop()

        # =====================================
        # INFO DATASET
        # =====================================

        st.success(
            "Dataset berhasil diupload"
        )

        st.info(
            f"File : {uploaded_file.name}"
        )

        st.markdown(
            "## 📄 Preview Dataset"
        )

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        # =====================================
        # PREPROCESSING
        # =====================================

        X, y = preprocess_data(df)

        st.success(
            "Preprocessing berhasil"
        )

        # =====================================
        # INFORMASI DATASET
        # =====================================

        st.markdown(
            "## 📊 Informasi Dataset"
        )

        fitur_asli = [

            "Brand",
            "Jenis",
            "Km",
            "Usia Motor",
            "Indikasi",
            "Qty"

        ]

        c1, c2, c3 = st.columns(3)

        with c1:

            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">
                    Jumlah Data
                </div>
                <div class="metric-value">
                    {len(df)}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c2:

            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">
                    Jumlah Fitur
                </div>
                <div class="metric-value">
                    {len(fitur_asli)}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c3:

            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">
                    Jumlah Kelas
                </div>
                <div class="metric-value">
                    {len(y.unique())}
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # =====================================
        # DISTRIBUSI TARGET
        # =====================================

        st.markdown(
            "## 📌 Distribusi Target"
        )

        service_count = df["Service"].value_counts()

        fig, ax = plt.subplots(
            figsize=(5,3)
        )

        sns.barplot(
            x=service_count.index,
            y=service_count.values,
            palette="Reds",
            ax=ax
        )

        c1, c2, c3 = st.columns([1,2,1])

        with c2:

            st.pyplot(fig)

        if len(y.unique()) < 2:

            st.error(
                "Target hanya memiliki 1 kelas"
            )

            st.stop()

        # =====================================
        # TRAIN BUTTON
        # =====================================

        if st.button(
            "🚀 Training Model"
        ):

            progress = st.progress(0)

            status = st.empty()

            status.info(
                "Memulai training..."
            )

            progress.progress(20)

            (
                model,
                accuracy,
                precision,
                recall,
                f1,
                report,
                matrix,
                importance_grouped,
                train_count,
                test_count

            ) = train_model(X, y)

            progress.progress(80)

            # =====================================
            # SAVE MODEL
            # =====================================

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

            progress.progress(100)

            status.success(
                "Training selesai & model berhasil disimpan"
            )

            st.markdown("---")

            # =====================================
            # METRICS
            # =====================================

            st.markdown(
                "## 📈 Hasil Evaluasi"
            )

            m1, m2, m3, m4 = st.columns(4)

            metrics = [

                ("Accuracy", accuracy),
                ("Precision", precision),
                ("Recall", recall),
                ("F1 Score", f1)

            ]

            cols = [m1, m2, m3, m4]

            for col, (label, value) in zip(
                cols,
                metrics
            ):

                with col:

                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">
                            {label}
                        </div>
                        <div class="metric-value">
                            {value:.2%}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True)

            # =====================================
            # REPORT
            # =====================================

            st.markdown(
                "## 📋 Classification Report"
            )

            st.code(report)

            # =====================================
            # CONFUSION MATRIX
            # =====================================

            st.markdown(
                "## 📉 Confusion Matrix"
            )

            fig2, ax2 = plt.subplots(
                figsize=(5,4)
            )

            sns.heatmap(
                matrix,
                annot=True,
                fmt="d",
                cmap="Reds",
                linewidths=1,
                linecolor="white",
                cbar=False,
                ax=ax2
            )

            ax2.set_xlabel("Prediksi")
            ax2.set_ylabel("Aktual")

            c1, c2, c3 = st.columns([1,2,1])

            with c2:

                st.pyplot(fig2)

            cm_path = BASE_DIR / "confusion_matrix.png"

            fig2.savefig(
                str(cm_path),
                bbox_inches="tight"
            )

            plt.close(fig2)

            # =====================================
            # FEATURE IMPORTANCE
            # =====================================

            st.markdown(
                "## ⭐ Feature Importance"
            )

            fig3, ax3 = plt.subplots(
                figsize=(6,4)
            )

            sns.barplot(
                data=importance_grouped,
                y="Fitur",
                x="Importance",
                ax=ax3
            )

            ax3.set_title(
                "Feature Importance Random Forest"
            )

            c1, c2, c3 = st.columns([1,2,1])

            with c2:

                st.pyplot(fig3)

            fi_path = BASE_DIR / "feature_importance.png"

            fig3.savefig(
                str(fi_path),
                bbox_inches="tight"
            )

            plt.close(fig3)

            st.dataframe(
                importance_grouped,
                use_container_width=True
            )

            # =====================================
            # PDF
            # =====================================

            logo_path = (
                BASE_DIR /
                "assets" /
                "yamaha_logo.png"
            )

            top_features = (
                importance_grouped["Fitur"]
                .head(6)
                .tolist()
            )

            pdf_path = generate_pdf(

                pdf_path="laporan_training_model.pdf",

                logo_path=str(logo_path),

                total_data=len(df),

                train_data=train_count,

                test_data=test_count,

                accuracy=accuracy,

                precision=precision,

                recall=recall,

                f1=f1,

                cm_image=str(cm_path),

                fi_image=str(fi_path),

                top_features=top_features
            )

            st.success(
                "Laporan PDF berhasil dibuat"
            )

            with open(
                pdf_path,
                "rb"
            ) as pdf_file:

                st.download_button(

                    label="📄 Download Laporan Training Model",

                    data=pdf_file,

                    file_name="Laporan_Training_Model.pdf",

                    mime="application/pdf"
                )

    except Exception as e:

        st.error(
            f"Terjadi error: {e}"
        )
