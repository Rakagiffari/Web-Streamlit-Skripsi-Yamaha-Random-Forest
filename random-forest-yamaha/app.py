import streamlit as st

st.set_page_config(
    page_title="Random Forest Yamaha",
    page_icon="🏍️",
    layout="wide"
)

st.title("🏍️ Klasifikasi Layanan Servis Yamaha")

st.markdown("""
## Penerapan Algoritma Random Forest

Sistem ini digunakan untuk mengklasifikasi layanan servis kendaraan Yamaha.

### Fitur Sistem
- Upload dataset CSV
- Training model Random Forest
- Prediksi layanan servis
- Visualisasi data
- Feature importance
""")

st.info("Gunakan menu sidebar untuk memulai analisis.")
