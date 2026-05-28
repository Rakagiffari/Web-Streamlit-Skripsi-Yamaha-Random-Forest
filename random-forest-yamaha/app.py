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

/* =========================================
GLOBAL
========================================= */

html, body, [class*="css"] {

    font-family: 'Segoe UI', sans-serif;
}

/* =========================================
MAIN BACKGROUND
========================================= */

[data-testid="stAppViewContainer"] {

    background: #ffffff;

    color: #111827;
}

/* =========================================
HEADER
========================================= */

[data-testid="stHeader"] {

    background: rgba(0,0,0,0);
}

/* =========================================
SIDEBAR
========================================= */

[data-testid="stSidebar"] {

    background: #111111;

    border-right: 2px solid #dc2626;
}

[data-testid="stSidebar"] * {

    color: white;
}

/* =========================================
MAIN CONTAINER
========================================= */

.block-container {

    padding-top: 2rem;

    padding-bottom: 2rem;

    padding-left: 3rem;

    padding-right: 3rem;
}

/* =========================================
TITLE
========================================= */

.main-title {

    font-size: 55px;

    font-weight: 800;

    color: #111827;

    line-height: 1.1;
}

.sub-title {

    margin-top: 12px;

    font-size: 18px;

    color: #6b7280;

    margin-bottom: 45px;
}

/* =========================================
BUBBLE METRIC CARD
========================================= */

.metric-box {

    background: linear-gradient(
        135deg,
        #dc2626,
        #b91c1c
    );

    border-radius: 30px;

    padding: 30px 25px;

    color: white;

    position: relative;

    overflow: hidden;

    transition: 0.3s ease;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.25);
}

/* bubble effect */

.metric-box::before {

    content: "";

    position: absolute;

    width: 160px;

    height: 160px;

    background: rgba(255,255,255,0.08);

    border-radius: 50%;

    top: -70px;

    right: -70px;
}

.metric-box:hover {

    transform: translateY(-6px);

    box-shadow:
        0 25px 50px rgba(0,0,0,0.35);
}

/* title */

.metric-title {

    font-size: 15px;

    font-weight: 600;

    opacity: 0.9;

    margin-bottom: 15px;
}

/* value */

.metric-value {

    font-size: 40px;

    font-weight: 800;

    line-height: 1;
}

/* icon */

.metric-icon {

    position: absolute;

    right: 20px;

    bottom: 15px;

    font-size: 45px;

    opacity: 0.18;
}

/* =========================================
STATUS BOX
========================================= */

.status-box {

    margin-top: 45px;

    background: white;

    border-left: 8px solid #dc2626;

    padding: 24px;

    border-radius: 22px;

    font-size: 17px;

    font-weight: 600;

    color: #111827;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.08);
}

/* =========================================
SECTION TITLE
========================================= */

.section-title {

    margin-top: 50px;

    margin-bottom: 20px;

    font-size: 28px;

    font-weight: 800;

    color: #111827;
}

/* =========================================
UPLOAD FILE
========================================= */

[data-testid="stFileUploader"] {

    background: white;

    border: 2px dashed #dc2626;

    border-radius: 25px;

    padding: 20px;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

/* =========================================
BUTTON
========================================= */

.stButton > button {

    background: #dc2626;

    color: white;

    border: none;

    border-radius: 14px;

    padding: 12px 25px;

    font-weight: 700;

    transition: 0.3s ease;
}

.stButton > button:hover {

    background: #b91c1c;

    transform: scale(1.02);

    box-shadow:
        0 12px 25px rgba(0,0,0,0.20);
}

/* =========================================
DATAFRAME
========================================= */

[data-testid="stDataFrame"] {

    border-radius: 22px;

    overflow: hidden;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

/* =========================================
SUCCESS ALERT
========================================= */

.stSuccess {

    border-radius: 16px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# LOGO
# =========================================

BASE_DIR = Path(__file__).parent

logo_path = BASE_DIR / "assets" / "yamaha_logo.png"

if logo_path.exists():

    st.sidebar.image(
        str(logo_path),
        width=180
    )

# =========================================
# SIDEBAR
# =========================================

st.sidebar.markdown("## 🏍️ Yamaha Dashboard")

st.sidebar.success("System Connected")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### Navigasi Menu

- Dashboard
- Upload Dataset
- Training Model
- Evaluasi Model
- Prediksi Data
""")

# =========================================
# SESSION STATE
# =========================================

accuracy = st.session_state.get("accuracy", 74)

total_data = st.session_state.get("total_data", 1500)

total_feature = st.session_state.get("total_feature", 12)

# =========================================
# HEADER
# =========================================

st.markdown(
    """
    <div class="main-title">
        Klasifikasi Layanan Servis Yamaha
    </div>

    <div class="sub-title">
        Penerapan Algoritma Random Forest untuk klasifikasi layanan servis kendaraan Yamaha
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================
# METRIC BUBBLE COLUMN
# =========================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(f"""
    <div class="metric-box">

        <div class="metric-title">
            Accuracy Model
        </div>

        <div class="metric-value">
            {accuracy}%
        </div>

        <div class="metric-icon">
            🎯
        </div>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="metric-box">

        <div class="metric-title">
            Total Data
        </div>

        <div class="metric-value">
            {total_data}
        </div>

        <div class="metric-icon">
            📊
        </div>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="metric-box">

        <div class="metric-title">
            Total Feature
        </div>

        <div class="metric-value">
            {total_feature}
        </div>

        <div class="metric-icon">
            ⚙️
        </div>

    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown("""
    <div class="metric-box">

        <div class="metric-title">
            Algoritma
        </div>

        <div class="metric-value" style="font-size:28px;">
            Random Forest
        </div>

        <div class="metric-icon">
            🌲
        </div>

    </div>
    """, unsafe_allow_html=True)

# =========================================
# STATUS
# =========================================

st.markdown("""
<div class="status-box">
    🚀 Sistem siap digunakan untuk training dan klasifikasi layanan servis Yamaha menggunakan algoritma Random Forest.
</div>
""", unsafe_allow_html=True)

# =========================================
# SECTION TITLE
# =========================================

st.markdown("""
<div class="section-title">
    Upload Dataset
</div>
""", unsafe_allow_html=True)

# =========================================
# FILE UPLOAD
# =========================================

uploaded_file = st.file_uploader(
    "📂 Upload file CSV",
    type=["csv"]
)

if uploaded_file:

    st.success("Dataset berhasil diupload")

# =========================================
# SAMPLE BUTTON
# =========================================

st.markdown("""
<div class="section-title">
    Training Model
</div>
""", unsafe_allow_html=True)

if st.button("🚀 Mulai Training"):

    st.success("Training model berhasil dilakukan")

```
