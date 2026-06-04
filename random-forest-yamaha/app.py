import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime, timedelta

BASE_DIR = Path(__file__).parent

logo_path = BASE_DIR / "assets" / "yamaha_logo.png"

st.set_page_config(
    page_title="Yamaha Random Forest",
    page_icon=str(logo_path),
    layout="wide"
)

# WIB
tanggal_jam = (
    datetime.utcnow() + timedelta(hours=7)
).strftime("%d-%m-%Y | %H:%M")

# Logo
st.image(str(logo_path), width=180)

# Judul
st.title("Klasifikasi Layanan Servis Yamaha")

st.markdown("""
Penerapan algoritma Random Forest untuk
klasifikasi layanan servis kendaraan Yamaha.
""")

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Algoritma",
        "Random Forest"
    )

with col2:
    st.metric(
        "Dataset",
        "CSV File"
    )

with col3:
    st.metric(
        "Tanggal & Jam WIB",
        tanggal_jam
    )

st.success(
    "Gunakan menu sidebar untuk memulai sistem klasifikasi layanan servis Yamaha."
)
