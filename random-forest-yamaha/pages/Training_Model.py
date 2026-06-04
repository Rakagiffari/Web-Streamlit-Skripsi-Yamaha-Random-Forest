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
# =========================================
# CUSTOM CSS
# =========================================
st.markdown("""
<style>

/* =========================
   BACKGROUND
========================= */
.stApp{
    background-color: #020617;
}

/* =========================
   SIDEBAR
========================= */
section[data-testid="stSidebar"]{

    min-width: 270px !important;
    max-width: 270px !important;

    background:
        linear-gradient(
            180deg,
            #050b18 0%,
            #091428 45%,
            #0f172a 100%
        );

    border-right: 1px solid rgba(255,255,255,0.06);
}

/* =========================
   SIDEBAR CONTENT
========================= */
[data-testid="stSidebarContent"]{

    padding-top: 20px;
    padding-left: 14px;
    padding-right: 14px;
    padding-bottom: 20px;
}

/* =========================
   SIDEBAR TITLE
========================= */
[data-testid="stSidebarNav"]::before{

    content: "MENU";

    display: block;

    text-align: center;

    color: white;

    font-size: 15px;

    font-weight: 900;

    letter-spacing: 4px;

    margin-bottom: 28px;

    padding-bottom: 14px;

    border-bottom: 1px solid rgba(255,255,255,0.08);

    opacity: 0.95;
}

/* =========================
   SIDEBAR NAV
========================= */
[data-testid="stSidebarNav"]{

    display: flex;
    flex-direction: column;
    height: 100%;
}

/* =========================
   MENU LIST
========================= */
[data-testid="stSidebarNav"] ul{

    display: flex;
    flex-direction: column;

    gap: 14px;

    height: 100%;

    padding-top: 5px;
}

/* =========================
   MENU ITEM
========================= */
[data-testid="stSidebarNav"] li{

    list-style: none;

    border-radius: 16px;

    overflow: hidden;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.03),
            rgba(255,255,255,0.01)
        );

    border: 1px solid rgba(255,255,255,0.05);

    transition:
        transform 0.25s ease,
        background 0.25s ease,
        border 0.25s ease,
        box-shadow 0.25s ease;
}

/* =========================
   MENU LINK
========================= */
[data-testid="stSidebarNav"] li a{

    color: #e2e8f0 !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    text-decoration: none !important;

    padding: 14px 18px;

    display: flex;
    align-items: center;

    border-radius: 16px;

    transition: all 0.25s ease;
}

/* =========================
   HOVER EFFECT
========================= */
[data-testid="stSidebarNav"] li:hover{

    transform: translateX(5px);

    background:
        linear-gradient(
            145deg,
            rgba(239,68,68,0.18),
            rgba(127,29,29,0.15)
        );

    border: 1px solid rgba(239,68,68,0.45);

    box-shadow:
        0 0 15px rgba(239,68,68,0.18);
}

/* =========================
   HOVER TEXT
========================= */
[data-testid="stSidebarNav"] li:hover a{

    color: white !important;
}

/* =========================
   ACTIVE MENU
========================= */
[data-testid="stSidebarNav"] li:has([aria-current="page"]){

    background:
        linear-gradient(
            135deg,
            #ef4444 0%,
            #dc2626 50%,
            #991b1b 100%
        );

    border: 1px solid rgba(255,255,255,0.08);

    box-shadow:
        0 0 18px rgba(239,68,68,0.35);
}

/* =========================
   ACTIVE TEXT
========================= */
[data-testid="stSidebarNav"] li:has([aria-current="page"]) a{

    color: white !important;

    font-weight: 800 !important;
}

/* =========================
   ABOUT MENU POSITION
========================= */
[data-testid="stSidebarNav"] li:last-child{

    margin-top: auto;

    margin-bottom: 10px;
}

/* =========================
   BOTTOM ABOUT STYLE
========================= */
[data-testid="stSidebarNav"] li:last-child{

    opacity: 0.92;

    border: 1px solid rgba(255,255,255,0.04);
}

/* =========================
   MAIN CONTAINER
========================= */
.block-container{
    padding-top: 1rem;
    padding-bottom: 2rem;
}

/* =========================
   MAIN TITLE
========================= */
.main-title{
    text-align: center;
    font-size: 58px;
    font-weight: 900;
    color: white;
    line-height: 1.1;
    margin-top: 5px;
    margin-bottom: 10px;
    letter-spacing: 1px;
}

/* =========================
   DESCRIPTION
========================= */
.desc{
    text-align: center;
    color: #cbd5e1;
    font-size: 20px;
    margin-top: 0px;
    margin-bottom: 45px;
}

/* =========================
   METRIC CARD
========================= */
.metric-card{
    background: linear-gradient(145deg, #111827, #1e293b);
    padding: 28px 20px;
    border-radius: 22px;
    border: 1px solid #334155;
    text-align: center;
    transition: 0.3s ease;
    box-shadow: 0 0 15px rgba(0,0,0,0.25);
    min-height: 150px;

    display:flex;
    flex-direction:column;
    justify-content:center;
}

/* =========================
   HOVER EFFECT
========================= */
.metric-card:hover{
    transform: translateY(-6px);
    border: 1px solid #ef4444;
    box-shadow: 0 0 20px rgba(239,68,68,0.25);
}

/* =========================
   METRIC TITLE
========================= */
.metric-title{
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 12px;
    font-weight: 600;
}

/* =========================
   METRIC VALUE
========================= */
.metric-value{
    color: white;
    font-size: 30px;
    font-weight: 800;
}

/* =========================
   SUCCESS BOX
========================= */
.stAlert{
    border-radius: 15px;
}

/* =========================
   SCROLLBAR
========================= */
::-webkit-scrollbar{

    width: 5px;
}

::-webkit-scrollbar-thumb{

    background: #475569;

    border-radius: 10px;
}

/* =========================
   HIDE STREAMLIT MENU
========================= */
#MainMenu{
    visibility: hidden;
}

footer{
    visibility: hidden;
}

header{
    visibility: hidden;
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

        fitur_asli = [

            "Category",
            "Brand",
            "Model Name",
            "Status",
            "Last Kilometer",
            "Usia Motor",
            "Parts Qty"

        ]

        with c1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Jumlah Data</div>
                <div class="metric-value">{len(df)}</div>
            </div>
            """, unsafe_allow_html=True)

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

            fig3, ax3 = plt.subplots(
                figsize=(5,3)
            )

            sns.barplot(
                data=importance_grouped,
                y="Fitur",
                x="Importance",
                ax=ax3
            )

            ax3.set_title(
                "Feature Importance",
                fontsize=10
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

            # =========================
            # TABEL
            # =========================
            st.dataframe(
                importance_grouped,
                use_container_width=True
            )

    except Exception as e:

        st.error(
            f"Terjadi error: {e}"
        )
