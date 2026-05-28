```python
import streamlit as st
from pathlib import Path

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="Yamaha Random Forest",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# CUSTOM CSS
# =========================================
st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
}

/* MAIN BACKGROUND */
[data-testid="stAppViewContainer"]{
    background: linear-gradient(
        135deg,
        #050816 0%,
        #081120 45%,
        #0b1220 100%
    );
    color: white;
}

/* HEADER */
[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}

/* SIDEBAR */
[data-testid="stSidebar"]{
    background: linear-gradient(
        180deg,
        #111827 0%,
        #0f172a 100%
    );
    border-right: 1px solid rgba(255,255,255,0.05);
}

/* TITLE */
.main-title{
    font-size: 58px;
    font-weight: 800;
    color: white;
    text-align: center;
    margin-bottom: 5px;
    letter-spacing: 1px;
}

/* SUBTITLE */
.sub-title{
    text-align: center;
    color: #ef4444;
    font-size: 18px;
    margin-bottom: 35px;
    font-weight: 500;
}

/* METRIC CARD */
[data-testid="metric-container"]{
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 22px;
    border-radius: 22px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.30);
    transition: 0.3s;
}

/* HOVER */
[data-testid="metric-container"]:hover{
    transform: translateY(-4px);
    border: 1px solid rgba(239,68,68,0.5);
}

/* STATUS BOX */
.status-box{
    margin-top: 35px;
    padding: 24px;
    border-radius: 24px;

    background: linear-gradient(
        135deg,
        rgba(34,197,94,0.20),
        rgba(22,163,74,0.10)
    );

    border: 1px solid rgba(34,197,94,0.30);

    text-align: center;
    font-size: 18px;
    font-weight: 700;

    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
}

/* SECTION */
.section-title{
    font-size: 28px;
    font-weight: 700;
    margin-top: 45px;
    margin-bottom: 15px;
    color: white;
}

/* UPLOAD AREA */
.upload-box{
    background: rgba(255,255,255,0.04);
    padding: 30px;
    border-radius: 24px;
    border: 1px dashed rgba(255,255,255,0.15);
}

</style>
""", unsafe_allow_html=True)

# =========================================
# LOGO
# =========================================
BASE_DIR = Path(__file__).parent
logo_path = BASE_DIR / "assets" / "yamaha_logo.png"

if logo_path.exists():
    st.sidebar.image(str(logo_path), width=180)

# =========================================
# SIDEBAR
# =========================================
st.sidebar.markdown("## 🏍️ Yamaha ML Dashboard")
st.sidebar.success("System Connected")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 📌 Menu Sistem
- Dashboard
- Upload Dataset
- Training Model
- Prediksi Data
- Evaluasi Model
""")

st.sidebar.markdown("---")

st.sidebar.info(
    "Model menggunakan algoritma Random Forest "
    "untuk klasifikasi layanan servis kendaraan Yamaha."
)

# =========================================
# SESSION STATE
# =========================================
accuracy = st.session_state.get("accuracy", 0)
total_data = st.session_state.get("total_data", 0)
total_feature = st.session_state.get("total_feature", 0)

# =========================================
# HEADER
# =========================================
st.markdown("""
<div class="main-title">
KLASIFIKASI LAYANAN SERVIS YAMAHA
</div>

<div class="sub-title">
Penerapan Algoritma Random Forest untuk klasifikasi layanan servis kendaraan Yamaha
</div>
""", unsafe_allow_html=True)

# =========================================
# METRIC
# =========================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="🎯 Accuracy Model",
        value=f"{accuracy}%"
    )

with col2:
    st.metric(
        label="📊 Total Data",
        value=total_data
    )

with col3:
    st.metric(
        label="🧠 Total Feature",
        value=total_feature
    )

with col4:
    st.metric(
        label="⚙️ Algoritma",
        value="Random Forest"
    )

# =========================================
# STATUS
# =========================================
st.markdown("""
<div class="status-box">
✅ Sistem siap digunakan untuk training dan klasifikasi layanan servis Yamaha
</div>
""", unsafe_allow_html=True)

# =========================================
# SECTION
# =========================================
st.markdown(
    '<div class="section-title">📂 Upload Dataset CSV</div>',
    unsafe_allow_html=True
)

# =========================================
# UPLOAD FILE
# =========================================
uploaded_file = st.file_uploader(
    "Upload dataset layanan servis Yamaha",
    type=["csv"]
)

if uploaded_file is not None:
    st.success("Dataset berhasil diupload!")

```
