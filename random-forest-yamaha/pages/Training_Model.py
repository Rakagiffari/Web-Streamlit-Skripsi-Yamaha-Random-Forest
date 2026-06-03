import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import numpy as np

from pathlib import Path

from utils.preprocessing import preprocess_data
from utils.training import train_model


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

.block{
    background-color:#111827;
    padding:25px;
    border-radius:18px;
    border:1px solid rgba(255,255,255,0.08);
    margin-bottom:20px;
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
    '<p class="sub-title">Klasifikasi Service Ringan & Berat</p>',
    unsafe_allow_html=True
)

st.markdown("---")


# =========================================
# FILE UPLOAD
# =========================================
uploaded_file = st.file_uploader(
    "📂 Upload Dataset CSV",
    type=["csv"]
)


# =========================================
# MAIN
# =========================================
if uploaded_file is not None:

    try:

        # =========================================
        # READ DATASET
        # =========================================
        df = pd.read_csv(uploaded_file)

        st.success("Dataset berhasil diupload")

        # =========================================
        # PREVIEW
        # =========================================
        with st.container():

            st.markdown("## 📄 Preview Dataset")

            st.dataframe(
                df.head(),
                use_container_width=True
            )

        # =========================================
        # VALIDASI TARGET
        # =========================================
        if "Service" not in df.columns:

            st.error(
                "Kolom 'Service' tidak ditemukan"
            )

            st.stop()

        # =========================================
        # PREPROCESSING
        # =========================================
        X, y = preprocess_data(df)

        st.success("Preprocessing berhasil")

        # =========================================
        # INFO DATASET
        # =========================================
        st.markdown("## 📊 Informasi Dataset")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Jumlah Data</div>
                <div class="metric-value">{len(df)}</div>
            </div>
            """, unsafe_allow_html=True)

        fitur_asli = [

    "Category",
    "Brand",
    "Model Name",
    "Status",
    "Last Kilometer",
    "Usia Motor",
    "Parts Qty"

]

with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Jumlah Fitur</div>
        <div class="metric-value">{len(fitur_asli)}</div>
    </div>
    """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Jumlah Kelas</div>
                <div class="metric-value">{len(y.unique())}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # =========================================
        # DISTRIBUSI TARGET
        # =========================================
        st.markdown(
            "## 📌 Distribusi Target"
        )

        service_count = (
            df["Service"]
            .value_counts()
        )

        fig, ax = plt.subplots(
            figsize=(4, 2.5)
        )

        sns.barplot(
            x=service_count.index,
            y=service_count.values,
            ax=ax
        )

        ax.set_xlabel(
            "Kategori Service",
            fontsize=9
        )

        ax.set_ylabel(
            "Jumlah",
            fontsize=9
        )

        ax.tick_params(
            labelsize=8
        )

        c1, c2, c3 = st.columns([1,2,1])

        with c2:

            st.pyplot(
                fig,
                use_container_width=False
            )

        # =========================================
        # VALIDASI KELAS
        # =========================================
        if len(y.unique()) < 2:

            st.error(
                "Target hanya memiliki 1 kelas"
            )

            st.stop()

        # =========================================
        # BUTTON TRAIN
        # =========================================
        if st.button("🚀 Training Model"):

            progress = st.progress(0)

            status = st.empty()

            status.info("Memulai training model...")
            progress.progress(20)

            try:

                (
                    model,
                    accuracy,
                    precision,
                    recall,
                    f1,
                    report,
                    matrix,
                    importance_grouped
                ) = train_model(X, y)

                progress.progress(80)

            except Exception as e:

                st.error(
                    f"Error training: {e}"
                )

                st.stop()

            # =========================================
            # SAVE MODEL
            # =========================================
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

            # =========================================
            # METRICS
            # =========================================
            st.markdown("## 📈 Hasil Evaluasi")

            m1, m2, m3, m4 = st.columns(4)

            metrics = [
                ("Accuracy", accuracy),
                ("Precision", precision),
                ("Recall", recall),
                ("F1 Score", f1)
            ]

            cols = [m1, m2, m3, m4]

            for col, (label, value) in zip(cols, metrics):

                with col:

                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">{label}</div>
                        <div class="metric-value">
                            {value:.2%}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

            # =========================================
            # REPORT
            # =========================================
            st.markdown("## 📋 Classification Report")

            st.code(report)

            # =========================================
            # CONFUSION MATRIX
            # =========================================
            st.markdown(
                "## 📉 Confusion Matrix"
            )

            fig2, ax2 = plt.subplots(
                figsize=(4,3)
            )

            sns.heatmap(
                matrix,
                annot=True,
                fmt="d",
                cmap="Reds",
                linewidths=1,
                linecolor='white',
                cbar=False,
                ax=ax2
            )

            ax2.set_xlabel(
                "Prediksi",
                fontsize=9
            )

            ax2.set_ylabel(
                "Aktual",
                fontsize=9
            )

            ax2.tick_params(
                labelsize=8
            )

            c1, c2, c3 = st.columns([1,2,1])

            with c2:

                st.pyplot(
                    fig2,
                    use_container_width=False
                )

            st.markdown("---")

            # =========================================
            # FEATURE IMPORTANCE
            # =========================================
            st.markdown(
                "## ⭐ Feature Importance"
            )

            importance_df = pd.DataFrame({

                "Feature":
                X.columns,

                "Importance":
                model.feature_importances_

            })

            importance_df = (
                importance_df
                .sort_values(
                    by="Importance",
                    ascending=False
                )
                .head(10)
            )

            fig3, ax3 = plt.subplots(
                figsize=(5,3)
            )

            sns.barplot(
                data=importance_df,
                y="Feature",
                x="Importance",
                ax=ax3
            )

            ax3.tick_params(
                labelsize=8
            )

            c1, c2, c3 = st.columns([1,2,1])

            with c2:

                st.pyplot(
                    fig3,
                    use_container_width=False
                )


    except Exception as e:

        st.error(
            f"Terjadi error: {e}"
        )
