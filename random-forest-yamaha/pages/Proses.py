# ==========================================================
# IMPORT LIBRARY
# ==========================================================

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from pathlib import Path

from utils.preprocessing import preprocess_data
from utils.training import train_model
from utils.report import generate_pdf

# ==========================================================
# CONFIG PAGE
# ==========================================================

st.set_page_config(
    page_title="Training Model",
    page_icon="⚙️",
    layout="wide"
)

# ==========================================================
# STYLE
# ==========================================================

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
    margin-bottom:20px;
}

.section-title{
    font-size:24px;
    font-weight:700;
    margin-top:20px;
    margin-bottom:10px;
}

.metric-card{
    background:#1f2937;
    padding:18px;
    border-radius:12px;
}

.metric-label{
    color:#9ca3af;
    font-size:14px;
}

.metric-value{
    color:white;
    font-size:28px;
    font-weight:bold;
}

div[data-testid="stDataFrame"]{
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    '<p class="main-title">⚙️ Training Random Forest</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Random Forest untuk Klasifikasi Layanan Service Kendaraan Yamaha</p>',
    unsafe_allow_html=True
)

st.markdown("---")
# ==========================================================
# FILE UPLOAD
# ==========================================================

uploaded_file = st.file_uploader(
    "📂 Upload Dataset",
    type=["csv", "xlsx", "xls"]
)

# ==========================================================
# MAIN
# ==========================================================

if uploaded_file is not None:

    try:

        # ==================================================
        # MEMBACA DATASET
        # ==================================================

        with st.spinner("Membaca dataset..."):

            if uploaded_file.name.endswith(".csv"):

                df = pd.read_csv(uploaded_file)

            elif uploaded_file.name.endswith(".xlsx"):

                df = pd.read_excel(
                    uploaded_file,
                    engine="openpyxl"
                )

            elif uploaded_file.name.endswith(".xls"):

                df = pd.read_excel(uploaded_file)

            else:

                st.error("Format file tidak didukung.")
                st.stop()

        # ==================================================
        # VALIDASI DATASET
        # ==================================================

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
                f"""
Kolom berikut tidak ditemukan:

{', '.join(missing_columns)}

Silakan gunakan dataset yang sesuai.
"""
            )

            st.stop()

        # ==================================================
        # DATASET BERHASIL
        # ==================================================

        st.success("✅ Dataset berhasil diupload")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Nama File",
                uploaded_file.name
            )

        with c2:

            st.metric(
                "Jumlah Data",
                f"{len(df):,}"
            )

        with c3:

            st.metric(
                "Jumlah Kolom",
                len(df.columns)
            )

        # ==================================================
        # PREVIEW DATASET
        # ==================================================

        st.markdown("## 📄 Preview Dataset")

        st.dataframe(
            df.head(10),
            use_container_width=True,
            hide_index=True
        )

        with st.expander("📋 Lihat seluruh nama kolom"):

            kolom_df = pd.DataFrame({

                "No" : range(1, len(df.columns)+1),

                "Nama Kolom" : df.columns

            })

            st.dataframe(
                kolom_df,
                use_container_width=True,
                hide_index=True
            )

        st.markdown("---")
        # ==========================================================
# INFORMASI DATASET
# ==========================================================

st.markdown("## 📊 Informasi Dataset")

total_data = len(df)
total_kolom = len(df.columns)
total_missing = int(df.isnull().sum().sum())
total_duplicate = int(df.duplicated().sum())
jumlah_kelas = df["Service"].nunique()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Jumlah Data",
        f"{total_data:,}"
    )

with col2:
    st.metric(
        "Jumlah Kolom",
        total_kolom
    )

with col3:
    st.metric(
        "Missing Value",
        total_missing
    )

with col4:
    st.metric(
        "Data Duplikat",
        total_duplicate
    )

with col5:
    st.metric(
        "Jumlah Kelas",
        jumlah_kelas
    )

# ==========================================================
# TIPE DATA
# ==========================================================

st.markdown("### 📑 Informasi Tipe Data")

dtype_df = pd.DataFrame({

    "Nama Kolom": df.columns,
    "Tipe Data": df.dtypes.astype(str)

})

st.dataframe(
    dtype_df,
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# MISSING VALUE
# ==========================================================

st.markdown("### 🔍 Missing Value")

missing_df = pd.DataFrame({

    "Kolom": df.columns,
    "Jumlah Missing": df.isnull().sum().values,
    "Persentase (%)":
        (
            df.isnull().sum()
            / len(df)
            * 100
        ).round(2)

})

st.dataframe(
    missing_df,
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# DATA DUPLIKAT
# ==========================================================

st.markdown("### 📋 Informasi Data Duplikat")

dup_col1, dup_col2 = st.columns(2)

with dup_col1:

    st.metric(
        "Jumlah Data",
        len(df)
    )

with dup_col2:

    st.metric(
        "Jumlah Data Duplikat",
        total_duplicate
    )

# ==========================================================
# RINGKASAN DATA NUMERIK
# ==========================================================

st.markdown("### 📈 Statistik Data Numerik")

numeric_columns = df.select_dtypes(
    include="number"
).columns

if len(numeric_columns) > 0:

    st.dataframe(

        df[
            numeric_columns
        ].describe().T,

        use_container_width=True

    )

else:

    st.info(
        "Dataset tidak memiliki kolom numerik."
    )

# ==========================================================
# DISTRIBUSI TARGET
# ==========================================================

st.markdown("### 📌 Distribusi Target")

target_df = (

    df["Service"]
    .value_counts()
    .reset_index()

)

target_df.columns = [

    "Kategori",
    "Jumlah"

]

target_df["Persentase (%)"] = (

    target_df["Jumlah"]
    / target_df["Jumlah"].sum()
    * 100

).round(2)

st.dataframe(

    target_df,

    use_container_width=True,

    hide_index=True

)

st.markdown("---")
# ==========================================================
# PREPROCESSING
# ==========================================================

st.markdown("## ⚙️ Preprocessing Dataset")

with st.spinner("Melakukan preprocessing dataset..."):

    X, y = preprocess_data(df)

st.success("✅ Preprocessing berhasil dilakukan")

# ==========================================================
# STATUS PREPROCESSING
# ==========================================================

st.markdown("### 📋 Status Preprocessing")

status_df = pd.DataFrame({

    "Tahapan": [

        "Validasi Dataset",
        "Pemeriksaan Missing Value",
        "Pemeriksaan Data Duplikat",
        "Feature Engineering",
        "Encoding Dataset"

    ],

    "Status": [

        "✅ Berhasil",
        "✅ Berhasil",
        "✅ Berhasil",
        "✅ Berhasil",
        "✅ Berhasil"

    ]

})

st.dataframe(
    status_df,
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# FEATURE ENGINEERING
# ==========================================================

st.markdown("## 🛠️ Hasil Feature Engineering")

tahun_sekarang = pd.Timestamp.now().year

feature_df = df.copy()

feature_df["Usia Motor"] = (
    tahun_sekarang -
    feature_df["Tahun"]
)

# ==========================================================
# PEMBENTUKAN JENIS MOTOR
# ==========================================================

def get_jenis(model):

    model = str(model).upper()

    if any(x in model for x in [
        "XMAX",
        "NMAX",
        "AEROX",
        "LEXI",
        "TMAX"
    ]):
        return "MAXi"

    elif any(x in model for x in [
        "FAZZIO",
        "FILANO"
    ]):
        return "Classy"

    elif any(x in model for x in [
        "MIO",
        "SOUL",
        "XEON",
        "FINO",
        "GEAR",
        "FREEGO",
        "X-RIDE",
        "XRIDE",
        "NOUVO",
        "LEXAM"
    ]):
        return "Matic"

    elif any(x in model for x in [
        "R15",
        "R25",
        "R6",
        "R1",
        "VIXION",
        "BYSON",
        "SCORPIO",
        "RX",
        "XSR",
        "MT"
    ]):
        return "Sport"

    elif any(x in model for x in [
        "WR",
        "YZ"
    ]):
        return "Off-road"

    elif any(x in model for x in [
        "JUPITER",
        "VEGA",
        "CRYPTON",
        "ALFA",
        "SIGMA",
        "F1ZR",
        "MX KING"
    ]):
        return "Moped"

    return "Unknown"

feature_df["Jenis"] = feature_df["Model"].apply(get_jenis)

# ==========================================================
# INFORMASI FEATURE ENGINEERING
# ==========================================================

st.info(
    """
Feature Engineering menghasilkan dua fitur baru yaitu:

• **Jenis** → hasil pengelompokan Model Motor.

• **Usia Motor** → dihitung dari Tahun Motor terhadap tahun saat ini.

Kedua fitur tersebut akan digunakan sebagai fitur pada proses klasifikasi Random Forest.
"""
)

# ==========================================================
# PREVIEW FEATURE ENGINEERING
# ==========================================================

st.markdown("### 📄 Preview Hasil Feature Engineering")

preview_feature = feature_df[

    [

        "Indikasi",
        "Model",
        "Jenis",
        "Tahun",
        "Usia Motor",
        "Km",
        "Service"

    ]

].head(10)

st.dataframe(

    preview_feature,

    use_container_width=True,

    hide_index=True

)

# ==========================================================
# INFORMASI FITUR MODEL
# ==========================================================

st.markdown("### 📌 Fitur yang Digunakan Model")

fitur_df = pd.DataFrame({

    "Nama Fitur": [

        "Indikasi",
        "Jenis",
        "Km",
        "Usia Motor"

    ],

    "Jenis Data": [

        "Kategori",
        "Kategori",
        "Numerik",
        "Numerik"

    ],

    "Keterangan": [

        "Kategori indikasi kerusakan",

        "Hasil Feature Engineering",

        "Kilometer kendaraan",

        "Hasil Feature Engineering"

    ]

})

st.dataframe(

    fitur_df,

    use_container_width=True,

    hide_index=True

)

# ==========================================================
# RINGKASAN PREPROCESSING
# ==========================================================

st.markdown("### 📊 Ringkasan Preprocessing")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Jumlah Data",
        len(feature_df)
    )

with col2:

    st.metric(
        "Jumlah Fitur Awal",
        4
    )

with col3:

    st.metric(
        "Jumlah Fitur Setelah Encoding",
        X.shape[1]
    )

with col4:

    st.metric(
        "Jumlah Target",
        y.nunique()
    )

st.markdown("---")
# ==========================================================
# VISUALISASI DATASET
# ==========================================================

st.markdown("## 📊 Visualisasi Dataset")

# ==========================================================
# DISTRIBUSI TARGET
# ==========================================================

st.markdown("### 📌 Distribusi Target Service")

target_count = feature_df["Service"].value_counts()

col1, col2 = st.columns(2)

# ----------------------------------------------------------
# BAR CHART
# ----------------------------------------------------------

with col1:

    fig1, ax1 = plt.subplots(figsize=(6,4))

    sns.barplot(
        x=target_count.index,
        y=target_count.values,
        palette="Reds",
        ax=ax1
    )

    ax1.set_title("Diagram Batang")
    ax1.set_xlabel("Kategori Service")
    ax1.set_ylabel("Jumlah Data")

    for p in ax1.patches:

        ax1.annotate(
            f"{int(p.get_height())}",
            (
                p.get_x()+p.get_width()/2,
                p.get_height()
            ),
            ha="center",
            va="bottom",
            fontsize=10
        )

    st.pyplot(fig1)

# ----------------------------------------------------------
# PIE CHART
# ----------------------------------------------------------

with col2:

    fig2, ax2 = plt.subplots(figsize=(5,5))

    ax2.pie(
        target_count,
        labels=target_count.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=sns.color_palette("Reds", len(target_count))
    )

    ax2.set_title("Diagram Pie")

    st.pyplot(fig2)

st.dataframe(

    pd.DataFrame({

        "Kategori":target_count.index,
        "Jumlah":target_count.values,
        "Persentase (%)":(
            target_count.values/
            target_count.sum()*100
        ).round(2)

    }),

    hide_index=True,
    use_container_width=True

)

# ==========================================================
# DISTRIBUSI JENIS MOTOR
# ==========================================================

st.markdown("### 🏍️ Distribusi Jenis Motor")

jenis_count = feature_df["Jenis"].value_counts()

col1, col2 = st.columns(2)

with col1:

    fig3, ax3 = plt.subplots(figsize=(7,4))

    sns.barplot(

        x=jenis_count.values,
        y=jenis_count.index,
        palette="Reds",
        ax=ax3

    )

    ax3.set_title("Diagram Batang Horizontal")
    ax3.set_xlabel("Jumlah Data")
    ax3.set_ylabel("Jenis Motor")

    st.pyplot(fig3)

with col2:

    fig4, ax4 = plt.subplots(figsize=(5,5))

    ax4.pie(

        jenis_count,

        labels=jenis_count.index,

        autopct="%1.1f%%",

        startangle=90,

        colors=sns.color_palette(
            "Reds",
            len(jenis_count)
        )

    )

    ax4.set_title("Diagram Pie")

    st.pyplot(fig4)

# ==========================================================
# DISTRIBUSI INDIKASI
# ==========================================================

st.markdown("### 🔧 Distribusi Indikasi")

indikasi_count = (
    feature_df["Indikasi"]
    .value_counts()
)

fig5, ax5 = plt.subplots(figsize=(9,5))

sns.barplot(

    x=indikasi_count.values,

    y=indikasi_count.index,

    palette="Reds",

    ax=ax5

)

ax5.set_title("Distribusi Indikasi")
ax5.set_xlabel("Jumlah Data")
ax5.set_ylabel("Indikasi")

st.pyplot(fig5)

# ==========================================================
# DISTRIBUSI KILOMETER
# ==========================================================

st.markdown("### 🚗 Distribusi Kilometer")

col1, col2 = st.columns([2,1])

with col1:

    fig6, ax6 = plt.subplots(figsize=(8,4))

    sns.histplot(

        feature_df["Km"],

        bins=25,

        kde=True,

        color="red",

        ax=ax6

    )

    ax6.set_title("Histogram Kilometer")
    ax6.set_xlabel("Kilometer")
    ax6.set_ylabel("Frekuensi")

    st.pyplot(fig6)

with col2:

    km_stat = pd.DataFrame({

        "Statistik":[

            "Minimum",
            "Maksimum",
            "Rata-rata",
            "Median"

        ],

        "Nilai":[

            int(feature_df["Km"].min()),
            int(feature_df["Km"].max()),
            round(feature_df["Km"].mean(),2),
            round(feature_df["Km"].median(),2)

        ]

    })

    st.dataframe(

        km_stat,

        hide_index=True,

        use_container_width=True

    )

# ==========================================================
# DISTRIBUSI USIA MOTOR
# ==========================================================

st.markdown("### 📅 Distribusi Usia Motor")

col1, col2 = st.columns(2)

with col1:

    fig7, ax7 = plt.subplots(figsize=(6,4))

    sns.histplot(

        feature_df["Usia Motor"],

        bins=15,

        kde=True,

        color="red",

        ax=ax7

    )

    ax7.set_title("Histogram Usia Motor")

    st.pyplot(fig7)

with col2:

    fig8, ax8 = plt.subplots(figsize=(6,4))

    sns.boxplot(

        x=feature_df["Usia Motor"],

        color="red",

        ax=ax8

    )

    ax8.set_title("Boxplot Usia Motor")

    st.pyplot(fig8)

usia_stat = pd.DataFrame({

    "Statistik":[

        "Minimum",
        "Maksimum",
        "Rata-rata",
        "Median"

    ],

    "Nilai":[

        int(feature_df["Usia Motor"].min()),
        int(feature_df["Usia Motor"].max()),
        round(feature_df["Usia Motor"].mean(),2),
        round(feature_df["Usia Motor"].median(),2)

    ]

})

st.dataframe(

    usia_stat,

    hide_index=True,

    use_container_width=True

)

st.markdown("---")

# ==========================================================
# TRAINING MODEL
# ==========================================================

st.markdown("## 🤖 Training Model")

if st.button(
    "🚀 Mulai Training Random Forest",
    use_container_width=True
):

    with st.spinner("Melatih model Random Forest..."):
                # ==================================================
        # TRAIN MODEL
        # ==================================================

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

    st.success("✅ Training Model Berhasil")

    # ==================================================
    # SIMPAN MODEL
    # ==================================================

    BASE_DIR = Path(__file__).parent.parent

    model_dir = BASE_DIR / "model"

    model_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    joblib.dump(

        model,

        model_dir /
        "random_forest_model.pkl"

    )

    # ==================================================
    # HASIL EVALUASI
    # ==================================================

    st.markdown("## 📈 Hasil Evaluasi Model")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Accuracy",
            f"{accuracy:.2%}"
        )

    with c2:

        st.metric(
            "Precision",
            f"{precision:.2%}"
        )

    with c3:

        st.metric(
            "Recall",
            f"{recall:.2%}"
        )

    with c4:

        st.metric(
            "F1 Score",
            f"{f1:.2%}"
        )

    # ==================================================
    # DATA TRAIN & TEST
    # ==================================================

    st.markdown("### 📊 Pembagian Dataset")

    d1, d2 = st.columns(2)

    with d1:

        st.metric(
            "Data Training",
            train_count
        )

    with d2:

        st.metric(
            "Data Testing",
            test_count
        )

    # ==================================================
    # CLASSIFICATION REPORT
    # ==================================================

    st.markdown("## 📋 Classification Report")

    st.code(report)

    # ==================================================
    # CONFUSION MATRIX
    # ==================================================

    st.markdown("## 📉 Confusion Matrix")

    fig_cm, ax_cm = plt.subplots(figsize=(6,5))

    sns.heatmap(

        matrix,

        annot=True,

        fmt="d",

        cmap="Reds",

        linewidths=.5,

        cbar=False,

        ax=ax_cm

    )

    ax_cm.set_xlabel("Prediksi")
    ax_cm.set_ylabel("Aktual")
    ax_cm.set_title("Confusion Matrix")

    st.pyplot(fig_cm)

    cm_path = (
        BASE_DIR /
        "confusion_matrix.png"
    )

    fig_cm.savefig(
        cm_path,
        bbox_inches="tight"
    )

    # ==================================================
    # FEATURE IMPORTANCE
    # ==================================================

    st.markdown("## ⭐ Feature Importance")

    fig_fi, ax_fi = plt.subplots(figsize=(8,5))

    sns.barplot(

        data=importance_grouped,

        x="Importance",

        y="Fitur",

        palette="Reds",

        ax=ax_fi

    )

    ax_fi.set_title("Feature Importance Random Forest")
    ax_fi.set_xlabel("Importance")
    ax_fi.set_ylabel("Fitur")

    st.pyplot(fig_fi)

    fi_path = (
        BASE_DIR /
        "feature_importance.png"
    )

    fig_fi.savefig(

        fi_path,

        bbox_inches="tight"

    )

    st.dataframe(

        importance_grouped,

        use_container_width=True,

        hide_index=True

    )

    # ==================================================
    # KESIMPULAN MODEL
    # ==================================================

    st.markdown("## 📝 Kesimpulan")

    if accuracy >= 0.90:

        kategori = "Sangat Baik"

    elif accuracy >= 0.80:

        kategori = "Baik"

    elif accuracy >= 0.70:

        kategori = "Cukup"

    else:

        kategori = "Perlu Peningkatan"

    st.success(

        f"""
Model Random Forest berhasil dilatih.

• Accuracy  : {accuracy:.2%}

• Precision : {precision:.2%}

• Recall    : {recall:.2%}

• F1 Score  : {f1:.2%}

Kategori Performa Model : **{kategori}**
"""

    )

    # ==================================================
    # GENERATE PDF
    # ==================================================

    logo_path = (

        BASE_DIR /

        "assets" /

        "yamaha_logo.png"

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

        top_features=

        importance_grouped[
            "Fitur"
        ].head(5).tolist()

    )

    # ==================================================
    # DOWNLOAD PDF
    # ==================================================

    st.markdown("## 📄 Laporan")

    with open(

        pdf_path,

        "rb"

    ) as pdf_file:

        st.download_button(

            label="📥 Download Laporan PDF",

            data=pdf_file,

            file_name="Laporan_Training_Model.pdf",

            mime="application/pdf",

            use_container_width=True

        )

except Exception as e:

    st.error("Terjadi kesalahan saat menjalankan sistem.")

    st.exception(e)
