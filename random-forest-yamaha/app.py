import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# =========================================
# PAGE CONFIG
# =========================================
BASE_DIR = Path(__file__).parent

logo_path = BASE_DIR / "assets" / "yamaha_logo.png"
logo = Image.open(logo_path)

st.set_page_config(
    page_title="Yamaha Random Forest",
    page_icon=logo,
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# AUTO REFRESH
# =========================================
st_autorefresh(interval=1000, key="clock_refresh")
