import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from pathlib import Path

from utils.preprocessing import preprocess_data
from utils.training import train_model
from sklearn.tree import plot_tree
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
        # MEMBACA DATASET
        # =====================================

        if uploaded_file.name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)

        elif uploaded_file.name.endswith((".xlsx", ".xls")):

            df = pd.read_excel(uploaded_file)

        else:

            st.error("Format file tidak didukung.")
            st.stop()

        # =====================================
        # VALIDASI KOLOM
        # =====================================

        required_columns = [

            "Model",
            "Tahun",
            "Km",
            "Indikasi",
            "Service"

        ]

        missing_columns = [

            col
            for col in required_columns
            if col not in df.columns

        ]

        if missing_columns:

            st.error(
                f"Kolom berikut tidak ditemukan:\n{', '.join(missing_columns)}"
            )

            st.stop()

        # =====================================
        # DATASET BERHASIL
        # =====================================

        st.success("Dataset berhasil diupload")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Nama File",
                uploaded_file.name
            )

        with col2:

            st.metric(
                "Jumlah Data",
                len(df)
            )

        with col3:

            st.metric(
                "Jumlah Kolom",
                len(df.columns)
            )

        # =====================================
        # PREVIEW DATASET
        # =====================================

        st.markdown("## 🗃️ Preview Dataset")

        st.dataframe(
            df.head(),
            use_container_width=True,
            hide_index=True
        )

        # =====================================
        # INFORMASI DATASET
        # =====================================

        st.markdown("## 📊 Hasil Prepocessing")

        total_missing = df.isnull().sum().sum()

        total_duplicate = df.duplicated().sum()

        numeric_cols = len(
            df.select_dtypes(include="number").columns
        )

        categorical_cols = len(
            df.select_dtypes(include=["object", "category"]).columns
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "Jumlah Data",
                len(df)
            )
        
        with c2:

            st.metric(
                "Missing Value",
                total_missing
            )

        with c3:

            st.metric(
                "Data Duplikat",
                total_duplicate
            )

        with c4:

            st.metric(
                "Jumlah Kelas",
                df["Service"].nunique()
            )

        # =====================================
        # INFORMASI TIPE DATA
        # =====================================

        st.markdown("### 📝 Ringkasan Tipe Data")

        info_df = pd.DataFrame({

            "Informasi": [

                "Kolom Numerik",
                "Kolom Kategori"

            ],

            "Jumlah": [

                numeric_cols,
                categorical_cols

            ]

        })

        st.dataframe(
            info_df,
            use_container_width=True,
            hide_index=True
        )

        # =====================================
        # MISSING VALUE
        # =====================================

        st.markdown("### 🔍 Missing Value per Kolom")

        missing_df = (

            df.isnull()
            .sum()
            .reset_index()

        )

        missing_df.columns = [

            "Kolom",
            "Jumlah Missing"

        ]

        st.dataframe(

            missing_df,

            use_container_width=True,

            hide_index=True

        )

        # =====================================
        # DUPLIKAT
        # =====================================

        st.markdown("### 📑 Informasi Data Duplikat")

        dup1, dup2 = st.columns(2)

        with dup1:

            st.metric(
                "Jumlah Data",
                len(df)
            )

        with dup2:

            st.metric(
                "Jumlah Duplikat",
                total_duplicate
            )

        st.markdown("---")

                # =====================================
        # PREPROCESSING
        # =====================================

        st.markdown("## 📇 Feature Engineering")

        st.markdown("### Dataset Awal")

        st.dataframe(
            df.head(),
            use_container_width=True,
            hide_index=True
        )

        feature_df = df.copy()

        # =====================================
        # Feature 1 : Usia Motor
        # =====================================

        from datetime import datetime

        tahun_sekarang = datetime.now().year

        feature_df["Usia Motor"] = (
            tahun_sekarang - feature_df["Tahun"]
        )

        # =====================================
        # Feature 2 : Jenis Motor
        # =====================================

        def get_jenis(model):

            model = str(model).upper()

            if any(x in model for x in [
                "XMAX", "NMAX", "AEROX", "LEXI", "TMAX"
            ]):
                return "MAXi"

            elif any(x in model for x in [
                "FAZZIO", "FILANO"
            ]):
                return "Classy"

            elif any(x in model for x in [
                "MIO", "SOUL", "XEON", "FINO",
                "GEAR", "FREEGO", "X-RIDE",
                "XRIDE", "NOUVO", "LEXAM"
            ]):
                return "Matic"

            elif any(x in model for x in [
                "R15", "R25", "R6", "R1",
                "VIXION", "BYSON",
                "SCORPIO", "RX",
                "XSR", "MT"
            ]):
                return "Sport"

            elif any(x in model for x in [
                "WR", "YZ"
            ]):
                return "Off-road"

            elif any(x in model for x in [
                "JUPITER", "VEGA",
                "CRYPTON", "ALFA",
                "SIGMA", "F1ZR",
                "MX"
            ]):
                return "Moped"

            return "Unknown"

        feature_df["Jenis"] = feature_df["Model"].apply(get_jenis)

        # =====================================
        # HASIL FEATURE ENGINEERING
        # =====================================

        st.markdown("### Hasil Feature Engineering")

        st.dataframe(
            feature_df[
                [
                    "Model",
                    "Jenis",
                    "Tahun",
                    "Usia Motor",
                    "Km",
                    "Indikasi",
                    "Service"
                ]
            ].head(5),
            use_container_width=True,
            hide_index=True
        )

        X, y = preprocess_data(df)

        st.success("Feature Engineering berhasil")
        # =====================================
        # DISTRIBUSI TARGET
        # =====================================

        st.markdown("## 📌 Distribusi Target")

        service_count = df["Service"].value_counts()

        col_bar, col_pie = st.columns(2)

        # ==========================
        # BAR CHART
        # ==========================

        with col_bar:

            fig1, ax1 = plt.subplots(figsize=(6, 5))

            sns.barplot(
                x=service_count.index,
                y=service_count.values,
                palette="Reds",
                ax=ax1
            )

            ax1.set_title("Distribusi Target")
            ax1.set_xlabel("Kategori Service")
            ax1.set_ylabel("Jumlah Data")

            for i, value in enumerate(service_count.values):
                ax1.text(
                    i,
                    value,
                    str(value),
                    ha="center",
                    va="bottom",
                    fontsize=10,
                    fontweight="bold"
                )

            plt.tight_layout()

            st.pyplot(fig1)

        # ==========================
        # PIE CHART
        # ==========================

        with col_pie:

            fig2, ax2 = plt.subplots(figsize=(6, 5))

            colors = sns.color_palette("Reds", len(service_count))

            ax2.pie(
                service_count.values,
                labels=service_count.index,
                autopct="%1.1f%%",
                startangle=90,
                colors=colors,
                textprops={"fontsize":10}
            )

            ax2.set_title("Persentase Target")

            ax2.axis("equal")      # membuat pie benar-benar bulat

            plt.tight_layout()

            st.pyplot(fig2)

        # ==========================
        # TABEL RINGKASAN
        # ==========================

        summary_df = pd.DataFrame({

            "Kategori": service_count.index,
            "Jumlah": service_count.values,
            "Persentase (%)":
                (service_count.values /
                 service_count.sum() * 100).round(2)

        })

        st.dataframe(
            summary_df,
            use_container_width=True,
            hide_index=True
        )

        # =====================================
        # TRAINING
        # =====================================

        if st.button(
            "🚀 Training Model"
        ):

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

            BASE_DIR = Path(
                __file__
            ).parent.parent

            model_dir = (
                BASE_DIR / "model"
            )

            model_dir.mkdir(
                parents=True,
                exist_ok=True
            )

            joblib.dump(
                model,
                model_dir /
                "random_forest_model.pkl"
            )

            # =====================================
            # METRICS
            # =====================================

            st.markdown(
                "## 📈 Hasil Evaluasi"
            )

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "Accuracy",
                f"{accuracy:.2%}"
            )

            c2.metric(
                "Precision",
                f"{precision:.2%}"
            )

            c3.metric(
                "Recall",
                f"{recall:.2%}"
            )

            c4.metric(
                "F1 Score",
                f"{f1:.2%}"
            )

            # =====================================
            # CLASSIFICATION REPORT
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
                ax=ax2
            )

            st.pyplot(fig2)

            cm_path = (
                BASE_DIR /
                "confusion_matrix.png"
            )

            fig2.savefig(
                cm_path,
                bbox_inches="tight"
            )

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
                x="Importance",
                y="Fitur",
                ax=ax3
            )

            st.pyplot(fig3)

            fi_path = (
                BASE_DIR /
                "feature_importance.png"
            )

            fig3.savefig(
                fi_path,
                bbox_inches="tight"
            )

            st.dataframe(
                importance_grouped,
                use_container_width=True
            )

            # =====================================
# DYNAMIC MODEL INSIGHT
# =====================================

st.markdown("---")
st.markdown("## 💡 Insight Model Random Forest")

# Ambil Top Feature Importance
top_features = importance_grouped.sort_values(
    by="Importance",
    ascending=False
).reset_index(drop=True)

# Top 3 fitur
top1 = top_features.iloc[0]
top2 = top_features.iloc[1]
top3 = top_features.iloc[2]

col1, col2 = st.columns([1.3,1])

# =====================================
# HASIL ANALISIS
# =====================================

with col1:

    st.success(f"""
### 📊 Hasil Analisis Model

Model Random Forest memperoleh performa sebagai berikut:

• Accuracy : **{accuracy:.2%}**

• Precision : **{precision:.2%}**

• Recall : **{recall:.2%}**

• F1 Score : **{f1:.2%}**

Berdasarkan hasil pelatihan, model paling banyak memanfaatkan fitur:

🥇 **{top1['Fitur']}** ({top1['Importance']:.2%})

🥈 **{top2['Fitur']}** ({top2['Importance']:.2%})

🥉 **{top3['Fitur']}** ({top3['Importance']:.2%})

Semakin tinggi nilai Feature Importance maka semakin besar kontribusinya terhadap proses klasifikasi.
""")

# =====================================
# CARA KERJA
# =====================================

with col2:

    st.info("""
### 🌳 Cara Kerja Random Forest

1. Dataset dibagi menjadi banyak Decision Tree.

2. Setiap Decision Tree mempelajari pola data.

3. Setiap Tree menghasilkan prediksi.

4. Semua prediksi dikumpulkan.

5. Majority Voting menentukan hasil akhir.
""")

# =====================================
# FEATURE IMPORTANCE
# =====================================

st.markdown("### ⭐ Ranking Feature Importance")

ranking_df = top_features.copy()

ranking_df["Importance"] = (
    ranking_df["Importance"] * 100
).round(2)

ranking_df.columns = [
    "Fitur",
    "Importance (%)"
]

st.dataframe(
    ranking_df,
    use_container_width=True,
    hide_index=True
)

# =====================================
# INSIGHT OTOMATIS
# =====================================

st.markdown("### 📌 Insight Otomatis")

st.info(
f"""
Model menunjukkan bahwa **{top1['Fitur']}** merupakan faktor yang paling berpengaruh
dengan nilai Feature Importance sebesar **{top1['Importance']:.2%}**.

Fitur tersebut lebih sering digunakan oleh Decision Tree dibandingkan fitur lainnya
ketika menentukan kategori layanan service.

Selanjutnya model juga mempertimbangkan fitur
**{top2['Fitur']}** ({top2['Importance']:.2%})
dan
**{top3['Fitur']}** ({top3['Importance']:.2%})
untuk meningkatkan ketepatan klasifikasi.

Hal ini menunjukkan bahwa keputusan Random Forest tidak hanya dipengaruhi oleh satu variabel,
melainkan merupakan kombinasi dari beberapa karakteristik kendaraan yang dipelajari secara bersamaan.
"""
)

# =====================================
# RULE REPRESENTATIVE
# =====================================

st.markdown("### 🌲 Contoh Rule Decision Tree")

from sklearn.tree import export_text

try:

    rules = export_text(
        model.estimators_[0],
        feature_names=list(X.columns)
    )

    st.code(rules[:2500])

except:

    st.warning(
        "Rule Decision Tree tidak dapat ditampilkan karena fitur telah mengalami proses encoding."
    )

# =====================================
# KESIMPULAN
# =====================================

st.markdown("### 📝 Kesimpulan")

st.success(
f"""
Model Random Forest berhasil mencapai **Accuracy sebesar {accuracy:.2%}**.

Analisis Feature Importance menunjukkan bahwa fitur yang paling dominan adalah
**{top1['Fitur']}**, diikuti oleh
**{top2['Fitur']}**
dan
**{top3['Fitur']}**.

Artinya proses klasifikasi lebih banyak dipengaruhi oleh kombinasi ketiga fitur tersebut dibandingkan fitur lainnya.

Karena Random Forest terdiri dari banyak Decision Tree, keputusan akhir diperoleh melalui mekanisme Majority Voting sehingga hasil klasifikasi menjadi lebih stabil dan robust.
"""
)   
                # =====================================
                # PDF
                # =====================================

            logo_path = (
                BASE_DIR /
                "assets" /
                "yamaha_logo.png"
            )

            pdf_path = generate_pdf(

                pdf_path=
                "laporan_training_model.pdf",

                logo_path=
                str(logo_path),

                total_data=
                len(df),

                train_data=
                train_count,

                test_data=
                test_count,

                accuracy=
                accuracy,

                precision=
                precision,

                recall=
                recall,

                f1=
                f1,

                cm_image=
                str(cm_path),

                fi_image=
                str(fi_path),

                top_features=
                importance_grouped[
                    "Fitur"
                ].head(5).tolist()
            )

            with open(
                pdf_path,
                "rb"
            ) as pdf_file:

                st.download_button(

                    "📄 Download Laporan",

                    pdf_file,

                    file_name=
                    "Laporan_Training_Model.pdf",

                    mime=
                    "application/pdf"
                )

    except Exception as e:

        st.error(
            f"Terjadi error: {e}"
        )
