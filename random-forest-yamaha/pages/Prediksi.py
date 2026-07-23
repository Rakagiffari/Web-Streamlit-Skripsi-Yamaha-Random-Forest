import streamlit as st

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="Prediksi Layanan",
    page_icon="🔍",
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
    font-size:14px;
    margin-top:-10px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown(
    '<p class="main-title">🔍 Prediksi Layanan Service</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Masukkan informasi kendaraan untuk melakukan prediksi layanan service menggunakan Random Forest.</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# =========================================
# MAPPING MODEL -> JENIS
# =========================================

def get_jenis(model):

    model = model.upper()

    if any(x in model for x in ["XMAX","NMAX","AEROX","LEXI","TMAX"]):
        return "MAXi"

    elif any(x in model for x in ["FAZZIO","FILANO"]):
        return "Classy"

    elif any(x in model for x in [
        "MIO","SOUL","XEON","FINO",
        "GEAR","FREEGO","X-RIDE",
        "XRIDE","NOUVO","LEXAM"
    ]):
        return "Matic"

    elif any(x in model for x in [
        "R15","R25","R6","R1",
        "VIXION","BYSON",
        "SCORPIO","RX",
        "XSR","MT"
    ]):
        return "Sport"

    elif any(x in model for x in [
        "WR","YZ"
    ]):
        return "Off-road"

    elif any(x in model for x in [
        "JUPITER","VEGA",
        "CRYPTON","ALFA",
        "SIGMA","F1ZR",
        "MX KING"
    ]):
        return "Moped"

    return "Unknown"

col1, col2 = st.columns(2)
with col1:

    model = st.selectbox(
        "Model Kendaraan",
        [
            "NMAX 155",
            "AEROX 155",
            "LEXI 125",
            "XMAX 250",
            "FAZZIO",
            "GRAND FILANO",
            "MIO M3",
            "GEAR 125",
            "FREEGO 125",
            "VIXION",
            "R15",
            "WR155R",
            "JUPITER Z1"
        ]
    )

with col2:

    jenis = get_jenis(model)

    st.text_input(
        "Jenis Motor",
        value=jenis,
        disabled=True
    )

col3, col4 = st.columns(2)
with col3:

    tahun = st.number_input(
        "Tahun Motor",
        min_value=2000,
        max_value=2030,
        value=2022
    )
with col4:

    km = st.number_input(
        "Kilometer",
        min_value=0,
        value=10000,
        step=100
    )

indikasi = st.selectbox(
    "Indikasi",
    [
        "Mesin",
        "Transmisi",
        "Kelistrikan",
        "Pengereman",
        "Roda dan Suspensi",
        "Body",
        "Umum"
    ]
)

st.button(
    "🔍 Prediksi Layanan",
    use_container_width=True
)

import joblib
import pandas as pd
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent

model = joblib.load(
    BASE_DIR / "model" / "random_forest_model.pkl"
)

tahun_sekarang = datetime.now().year

usia_motor = tahun_sekarang - tahun

input_data = pd.DataFrame({

    "Jenis":[jenis],

    "Km":[km],

    "Usia Motor":[usia_motor],

    "Indikasi":[indikasi]

})

input_data = pd.get_dummies(

    input_data,

    columns=[
        "Jenis",
        "Indikasi"
    ],

    drop_first=False

)

feature_names = model.feature_names_in_

input_data = input_data.reindex(

    columns=feature_names,

    fill_value=0

)

hasil = model.predict(input_data)[0]

if hasil == 0:

    hasil_prediksi = "Service Ringan"

else:

    hasil_prediksi = "Service Berat"

st.success(f"Hasil Prediksi : {hasil_prediksi}")

st.markdown("---")

st.markdown("""
<h2 style='text-align:center;color:white;'>
📋 Hasil Prediksi
</h2>
""", unsafe_allow_html=True)
if hasil == 0:
    hasil_prediksi = "Service Ringan"
else:
    hasil_prediksi = "Service Berat"

st.markdown(f"""
<div style="
background:#111827;
border:1px solid #334155;
padding:25px;
border-radius:18px;
text-align:center;
margin-top:15px;
">

<div style="
font-size:16px;
color:#9ca3af;
margin-bottom:10px;
">

Kategori Layanan

</div>

<div style="
font-size:34px;
font-weight:bold;
color:#ffffff;
">

{hasil_prediksi}

</div>

</div>
""", unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)
with col1:

    st.info("⏱️ Estimasi\n\n± 3 Jam")

with col2:

    st.info("👨‍🔧 Mekanik\n\nAndi Saputra")

with col3:

    st.info("📅 Jadwal\n\nHari Ini")

if hasil_prediksi == "Service Ringan":

    st.success("""
Kendaraan dapat langsung dilakukan service ringan.
Estimasi pengerjaan relatif singkat.
""")

else:

    st.warning("""
Disarankan dilakukan pemeriksaan menyeluruh karena
kendaraan diprediksi memerlukan service berat.
""")
