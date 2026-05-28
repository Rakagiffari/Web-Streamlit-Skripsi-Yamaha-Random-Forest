import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Yamaha Random Forest",
    page_icon="🏍️",
    layout="wide"
)

BASE_DIR = Path(__file__).parent

logo_path = BASE_DIR / "assets" / "yamaha_logo.png"

if logo_path.exists():

    st.sidebar.image(
        str(logo_path),
        width=180
    )

st.sidebar.title(
    "🏍️ Yamaha ML Dashboard"
)

st.title(
    "🏍️ Klasifikasi Layanan Servis Yamaha"
)

st.markdown("""
### Penerapan Algoritma Random Forest

Sistem machine learning untuk klasifikasi layanan servis kendaraan Yamaha.
""")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Algoritma", "Random Forest")

with col2:
    st.metric("Target", "2 Class")

with col3:
    st.metric("Dataset", "CSV")

with col4:
    st.metric("Status", "Ready")

st.success(
    "Gunakan menu sidebar untuk memulai."
)
