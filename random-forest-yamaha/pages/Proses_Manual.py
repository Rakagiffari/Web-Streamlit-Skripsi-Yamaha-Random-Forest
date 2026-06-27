import streamlit as st
import pandas as pd
import joblib

from pathlib import Path
from datetime import datetime

from utils.preprocessing import get_jenis

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Prediksi Manual",
    page_icon="🔍",
    layout="wide"
)

# =========================================
# PATH
# =========================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "random_forest_model.pkl"

FEATURE_PATH = BASE_DIR / "model" / "feature_columns.pkl"

# =========================================
# LOAD MODEL
# =========================================

try:

    model = joblib.load(MODEL_PATH)

    feature_columns = joblib.load(FEATURE_PATH)

except:

    st.error(
        "Model belum tersedia.\n\nSilakan lakukan Training Model terlebih dahulu."
    )

    st.stop()

# =========================================
# CSS
# =========================================

st.markdown("""

<style>

.main-title{

    text-align:center;
    font-size:38px;
    font-weight:800;
    color:white;

}

.card{

    background:#111827;
    border-radius:18px;
    padding:25px;

    border:1px solid #374151;

}

.result{

    text-align:center;
    font-size:30px;
    font-weight:bold;

}

</style>

""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown(

"""
<div class="main-title">

🔍 PREDIKSI LAYANAN SERVICE

</div>

""",

unsafe_allow_html=True

)

st.markdown("---")

# =========================================
# INPUT
# =========================================

col1,col2 = st.columns(2)

with col1:

    indikasi = st.selectbox(

        "Indikasi",

        [

            "Mesin",

            "CVT",

            "Kelistrikan",

            "Rem",

            "Ban",

            "Suspensi",

            "Oli",

            "Body"

        ]

    )

    tahun = st.number_input(

        "Tahun Motor",

        min_value=2000,

        max_value=datetime.now().year,

        value=2022

    )

with col2:

    jenis = st.selectbox(

        "Jenis Motor",

        [

            "Matic",

            "MAXi",

            "Classy",

            "Sport",

            "Moped",

            "Off-road"

        ]

    )

    km = st.number_input(

        "Kilometer",

        min_value=0,

        value=25000,

        step=500

    )

brand = st.selectbox(

    "Brand",

    [

        "Yamaha"

    ]

)

st.markdown("")

prediksi = st.button(

    "🚀 PREDIKSI",

    use_container_width=True

)
# =========================================
# PROSES PREDIKSI
# =========================================

if prediksi:

    usia_motor = datetime.now().year - tahun

    data = pd.DataFrame({

        "Brand": [brand],
        "Jenis": [jenis],
        "Km": [km],
        "Usia Motor": [usia_motor],
        "Indikasi": [indikasi]

    })

    # =====================================
    # ONE HOT ENCODING
    # =====================================

    data = pd.get_dummies(

        data,

        columns=[

            "Brand",
            "Jenis",
            "Indikasi"

        ]

    )

    # =====================================
    # MENYAMAKAN FITUR
    # =====================================

    data = data.reindex(

        columns=feature_columns,

        fill_value=0

    )

    # =====================================
    # PREDIKSI
    # =====================================

    hasil = model.predict(data)[0]

    probabilitas = model.predict_proba(data)[0]

    persen_ringan = round(probabilitas[0] * 100, 2)

    persen_berat = round(probabilitas[1] * 100, 2)

    st.markdown("---")

    st.subheader("HASIL PREDIKSI")

    if hasil == 1:

        st.success("🟠 Service Berat")

    else:

        st.success("🟢 Service Ringan")

    st.markdown("### Probabilitas")

    # =====================================
    # SERVICE BERAT
    # =====================================

    st.write("**🟠 Service Berat**")

    col1, col2 = st.columns([4,1])

    with col1:

        st.progress(
            int(persen_berat)
        )

    with col2:

        st.write(
            f"{persen_berat:.2f}%"
        )

    # =====================================
    # SERVICE RINGAN
    # =====================================

    st.write("**🟢 Service Ringan**")

    col1, col2 = st.columns([4,1])

    with col1:

        st.progress(
            int(persen_ringan)
        )

    with col2:

        st.write(
            f"{persen_ringan:.2f}%"
        )

    st.markdown("---")

    # =====================================
    # DETAIL HASIL
    # =====================================

    confidence = max(

        persen_ringan,

        persen_berat

    )

    st.subheader("Detail Prediksi")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            "Jenis Motor",

            jenis

        )

    with c2:

        st.metric(

            "Usia Motor",

            f"{usia_motor} Tahun"

        )

    with c3:

        st.metric(

            "Kilometer",

            f"{km:,} Km"

        )

    st.markdown("")

    st.metric(

        "Tingkat Keyakinan Model",

        f"{confidence:.2f}%"

    )

    st.markdown("---")

    # =====================================
    # REKOMENDASI
    # =====================================

    st.subheader("Rekomendasi")

    if hasil == 1:

        st.warning(
            """
Motor diprediksi membutuhkan **Service Berat**.

Disarankan dilakukan pemeriksaan menyeluruh terhadap komponen mesin maupun komponen pendukung agar kerusakan tidak berkembang menjadi lebih serius.
"""
        )

    else:

        st.success(
            """
Motor diprediksi hanya membutuhkan **Service Ringan**.

Disarankan tetap melakukan servis berkala sesuai jadwal agar performa kendaraan tetap optimal.
"""
        )
