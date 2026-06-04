import streamlit as st
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).parent

logo_path = BASE_DIR / "assets" / "yamaha_logo.png"

st.set_page_config(
    page_title="Yamaha Random Forest",
    page_icon=str(logo_path),
    layout="wide"
)

st.image(str(logo_path), width=180)

st.title("Klasifikasi Layanan Servis Yamaha")

st.write(
    "Penerapan algoritma Random Forest untuk klasifikasi layanan servis kendaraan Yamaha."
)

col1, col2 = st.columns(2)

with col1:
    st.info("Algoritma : Random Forest")

with col2:
    st.info("Dataset : CSV")

st.success(
    "Gunakan menu sidebar untuk memulai proses."
)
