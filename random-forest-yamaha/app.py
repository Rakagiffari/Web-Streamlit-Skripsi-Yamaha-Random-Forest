import streamlit as st
from pathlib import Path
from PIL import Image

# =========================================
# PAGE CONFIG
# =========================================
BASE_DIR = Path(__file__).parent

logo_path = BASE_DIR / "assets" / "yamaha_logo.png"

logo = Image.open(logo_path)

st.set_page_config(
    page_title="Yamaha Random Forest",
    page_icon=logo,
    layout="wide"
)

# =========================================
# LOAD GLOBAL CSS
# =========================================
css_path = BASE_DIR / "styles" / "global.css"

with open(css_path) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================================
# HOME PAGE
# =========================================
st.image(logo, width=240)

st.title("KLASIFIKASI LAYANAN SERVIS YAMAHA")

st.markdown("""
### Penerapan Algoritma Random Forest
Untuk Klasifikasi Layanan Servis Kendaraan Yamaha
""")
