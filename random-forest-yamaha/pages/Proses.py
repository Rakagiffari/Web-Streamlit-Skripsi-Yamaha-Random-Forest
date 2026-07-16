import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import matplotlib.patches as patches

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

/* =========================================
UPLOAD INFORMATION CARD
========================================= */

.upload-card{
    background:linear-gradient(145deg,#111827,#1e293b);
    border:1px solid #334155;
    border-radius:18px;
    padding:22px;
    text-align:center;
    transition:.3s;
    box-shadow:0 5px 15px rgba(0,0,0,.08);
    min-height:120px;

    display:flex;
    flex-direction:column;
    justify-content:center;
}

.upload-card:hover{
    transform:translateY(-5px);
    box-shadow:0 0 18px rgba(239,68,68,.25);
}

.upload-icon{
    font-size:30px;
    margin-bottom:8px;
}

.upload-title{
    font-size:14px;
    color:#94a3b8;
    font-weight:600;
    margin-bottom:8px;
}

.upload-value{
    font-size:22px;
    color:white;
    font-weight:800;
    word-break:break-word;
}

/* EXPANDER */

div[data-testid="stExpander"]{
    border:1px solid #E5E7EB;
    border-radius:12px;
    background:#020617;
    box-shadow:0 2px 8px rgba(0,0,0,.05);
    margin-bottom:18px;
}

div[data-testid="stExpander"] details summary{
    font-size:16px;
    font-weight:600;
    padding:12px 18px;
}

div[data-testid="stExpander"] details summary:hover{
    background:#1f2937;
    border-radius:12px;
}

div[data-testid="stExpanderDetails"]{
    padding:15px 18px 18px 18px;
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
        # INFORMASI DATASET
        # =====================================
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"""
            <div class="upload-card">
                <div class="upload-title">
                    Nama File
                </div>
                <div class="upload-value">
                    {uploaded_file.name}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="upload-card">
                <div class="upload-title">
                    Jumlah Data
                </div>
                <div class="upload-value">
                    {len(df):,}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="upload-card">
                <div class="upload-title">
                    Jumlah Kolom
                </div>
                <div class="upload-value">
                    {len(df.columns)}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        # =====================================
        # PREVIEW DATASET
        # =====================================

        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.expander("🔍 Preview Dataset", expanded=False):
            st.caption(f"Menampilkan seluruh dataset ({len(df)} baris).")
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                height=500
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

        with st.expander("📝 Informasi Tipe Data", expanded=False):

            st.caption("Ringkasan tipe data pada dataset yang diunggah.")

            # Ringkasan tipe data
            numeric_cols = len(
                df.select_dtypes(include=["number"]).columns
            )

            categorical_cols = len(
                df.select_dtypes(include=["object", "category"]).columns
            )

            datetime_cols = len(
                df.select_dtypes(include=["datetime"]).columns
            )

            st.write(f"**Kolom Numerik :** {numeric_cols}")
            st.write(f"**Kolom Kategori :** {categorical_cols}")
            st.write(f"**Kolom Tanggal/Waktu :** {datetime_cols}")

            st.markdown("### Detail Tipe Data")

            dtype_df = pd.DataFrame({

                "Kolom": df.columns,
                "Tipe Data": df.dtypes.astype(str)

            })

            st.dataframe(
                dtype_df,
                use_container_width=True,
                hide_index=True,
                height=400
            )
        # =====================================
        # MISSING VALUE
        # =====================================

        with st.expander("🔍 Missing Value", expanded=False):
            st.caption("Pemeriksaan Missing Value pada dataset yang diunggah.")
            total_missing = df.isnull().sum().sum()
            missing_df = (
                df.isnull()
                .sum()
                .reset_index()
            )
            
            missing_df.columns = [
                "Kolom",
                "Jumlah Missing"
            ]
            
            st.write(f"**Total Missing Value : {total_missing}**")
            
            st.dataframe(
                missing_df,
                use_container_width=True,
                hide_index=True,
                height=400
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
                train_size,
                test_size,
                feature_names 
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
            
            # ==========================================================
            # REPRESENTATIVE DECISION TREE
            # ==========================================================
            st.markdown("---")
            st.markdown("## 🌳 Representative Decision Tree")

            st.info("""
Visualisasi berikut merupakan salah satu Decision Tree
yang membentuk Random Forest.

Tree ditampilkan hingga kedalaman 3 level agar pola
pengambilan keputusan lebih mudah dipahami.

Decision Tree ini digunakan sebagai representasi proses
klasifikasi, sedangkan keputusan akhir Random Forest
tetap berasal dari gabungan seluruh Decision Tree.
""")

            fig_tree, ax = plt.subplots(figsize=(20,8))

            plot_tree(

                model.estimators_[0],

                feature_names=feature_names,

                class_names=["Ringan","Berat"],

                filled=True,

                rounded=True,

                fontsize=9,

                impurity=False,

                proportion=True,

                max_depth=3,

                ax=ax

            )

            plt.tight_layout()

            st.pyplot(fig_tree)

            # ==========================================================
            # TREE ANALYSIS
            # ==========================================================

            st.markdown("### 📍 Tree Analysis")

            top1 = importance_grouped.iloc[0]["Fitur"]
            top2 = importance_grouped.iloc[1]["Fitur"]
            top3 = importance_grouped.iloc[2]["Fitur"]

            col1, col2 = st.columns([1.2,1])

            with col1:

                st.success(f"""
### 🌲 Representative Tree

Tree di atas merupakan salah satu Decision Tree
yang dipelajari oleh algoritma Random Forest.

Node pada bagian paling atas (root node)
menunjukkan fitur pertama yang digunakan
untuk memisahkan data.

Selanjutnya Decision Tree melakukan
pemisahan data secara bertahap
hingga menghasilkan prediksi kategori service.
""")

            with col2:

                st.info(f"""
### ⭐ Feature Dominan

🥇 **{top1}**

🥈 **{top2}**

🥉 **{top3}**

Ketiga fitur tersebut merupakan
fitur yang paling sering dimanfaatkan
oleh Random Forest.
""")

            # ==========================================================
            # INSIGHT
            # ==========================================================

            st.markdown("### 💡 Insight Decision Tree")

            st.markdown(f"""
<div style="
background:#111827;
padding:20px;
border-radius:15px;
border-left:6px solid #ef4444;
">

<b>Interpretasi Decision Tree</b>

<br><br>

Representative Decision Tree menunjukkan bahwa proses
klasifikasi dilakukan secara bertahap dengan memisahkan
data berdasarkan nilai pada setiap node.

Berdasarkan hasil Feature Importance,
Random Forest lebih banyak memanfaatkan fitur
<b>{top1}</b>,
kemudian
<b>{top2}</b>,
serta
<b>{top3}</b>
untuk membedakan kategori
<b>Service Ringan</b>
dan
<b>Service Berat</b>.

Decision Tree di atas memberikan gambaran bagaimana
salah satu pohon melakukan proses klasifikasi.

Namun prediksi akhir Random Forest
tetap diperoleh melalui proses
<b>Majority Voting</b>
dari seluruh Decision Tree.

</div>
""", unsafe_allow_html=True)
            
            # ==========================================================
            # TREE INSIGHT
            # ==========================================================

            st.markdown("### 💡 Insight Decision Tree")

            top1 = importance_grouped.iloc[0]["Fitur"]
            top2 = importance_grouped.iloc[1]["Fitur"]
            top3 = importance_grouped.iloc[2]["Fitur"]

            st.info(f"""
Representative Decision Tree di atas merupakan salah satu pohon
yang membentuk algoritma Random Forest.

Pada proses klasifikasi, Decision Tree melakukan pemisahan data
berdasarkan beberapa fitur hingga menghasilkan prediksi.

Berdasarkan hasil Feature Importance,
fitur yang paling dominan adalah **{top1}**.

Selanjutnya model juga banyak memanfaatkan
**{top2}** dan **{top3}**
untuk meningkatkan ketepatan klasifikasi.

Artinya ketiga fitur tersebut memiliki kontribusi terbesar
dalam membedakan kategori **Service Ringan**
dan **Service Berat**.

Perlu diperhatikan bahwa prediksi akhir Random Forest
tidak berasal dari satu Decision Tree saja,
melainkan dari gabungan seluruh Decision Tree
melalui proses Majority Voting.
""")
            
            # ==========================================================
            # STATISTIK DATASET
            # ==========================================================

            st.markdown("### 📈 Ringkasan Dataset")

            col_km, col_usia = st.columns(2)

            if "Km" in df.columns:

                with col_km:

                    km_summary = (
                        df.groupby("Service")["Km"]
                        .mean()
                        .round(1)
                        .reset_index()
                    )

                    st.markdown("#### 🚗 Rata-rata Kilometer")

                    st.dataframe(
                        km_summary,
                        use_container_width=True,
                        hide_index=True
                    )

            if "Usia Motor" in feature_df.columns:

                with col_usia:

                    usia_summary = (
                        feature_df.groupby("Service")["Usia Motor"]
                        .mean()
                        .round(1)
                        .reset_index()
                    )

                    st.markdown("#### 📅 Rata-rata Usia Motor")

                    st.dataframe(
                        usia_summary,
                        use_container_width=True,
                        hide_index=True
                    )

            st.markdown("### 📝 Kesimpulan")

            st.success(f"""
Model Random Forest memperoleh Accuracy sebesar **{accuracy:.2%}**.

Feature Importance menunjukkan bahwa fitur yang paling dominan adalah **{top1['Fitur']}**.

Keputusan model merupakan kombinasi seluruh fitur yang dipelajari oleh banyak Decision Tree melalui mekanisme Majority Voting.

Seluruh insight pada halaman ini dihitung secara otomatis dari hasil pelatihan model sehingga akan berubah ketika dataset yang digunakan berubah.
""")
                        
                    
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
