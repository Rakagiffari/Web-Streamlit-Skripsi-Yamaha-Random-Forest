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
BACKGROUND
========================================= */

[data-testid="stAppViewContainer"] {
    background: #ffffff;
    color: #111827;
}

[data-testid="stHeader"] {
    background: rgba(255,255,255,0);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
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
TITLE
========================================= */

.main-title {
    font-size: 52px;
    font-weight: 800;
    color: #111827;
    line-height: 1.1;
}

.sub-title {
    color: #6b7280;
    font-size: 18px;
    margin-top: 10px;
    margin-bottom: 40px;
}

/* =========================================
METRIC CARD
========================================= */

[data-testid="metric-container"] {
    background: white;
    border-radius: 24px;
    padding: 28px 20px;
    border: 1px solid #e5e7eb;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);

    transition: 0.3s ease;
}

[data-testid="metric-container"]:hover {

    transform: translateY(-5px);

    box-shadow:
        0 20px 40px rgba(0,0,0,0.15);
}

/* metric label */

[data-testid="metric-container"] label {
    color: #6b7280 !important;
    font-size: 15px !important;
    font-weight: 600;
}

/* metric value */

[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #dc2626;
    font-size: 34px;
    font-weight: 800;
}

/* =========================================
BUBBLE CHAT STYLE
========================================= */

.bubble-container {
    margin-top: 45px;
}

.chat-bubble {

    background: #dc2626;

    color: white;

    padding: 22px 28px;

    border-radius: 24px;

    font-size: 18px;

    font-weight: 600;

    width: fit-content;

    max-width: 850px;

    position: relative;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.30);
}

/* bubble tail */

.chat-bubble::after {

    content: "";

    position: absolute;

    bottom: -12px;

    left: 40px;

    width: 25px;

    height: 25px;

    background: #dc2626;

    transform: rotate(45deg);
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
BUTTON
========================================= */

.stButton > button {

    background: #dc2626;

    color: white;

    border: none;

    border-radius: 14px;

    padding: 12px 24px;

    font-weight: 700;

    transition: 0.3s;
}

.stButton > button:hover {

    background: #b91c1c;

    transform: scale(1.02);

    box-shadow:
        0 10px 20px rgba(0,0,0,0.20);
}

/* =========================================
UPLOAD FILE
========================================= */

[data-testid="stFileUploader"] {

    background: white;

    border: 2px dashed #dc2626;

    border-radius: 20px;

    padding: 20px;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

/* =========================================
TABLE
========================================= */

[data-testid="stDataFrame"] {

    border-radius: 20px;

    overflow: hidden;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
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
### Menu Navigasi

- Dashboard
- Training Model
- Upload Dataset
- Evaluasi Model
- Prediksi Data
""")

# =========================================
# SESSION STATE
# =========================================

accuracy = st.session_state.get("accuracy", 0)

total_data = st.session_state.get("total_data", 0)

total_feature = st.session_state.get("total_feature", 0)

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
# METRIC
# =========================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        label="Accuracy Model",
        value=f"{accuracy}%"
    )

with col2:

    st.metric(
        label="Total Data",
        value=total_data
    )

with col3:

    st.metric(
        label="Total Feature",
        value=total_feature
    )

with col4:

    st.metric(
        label="Algoritma",
        value="Random Forest"
    )

# =========================================
# BUBBLE CHAT STATUS
# =========================================

st.markdown(
    """
    <div class="bubble-container">
        <div class="chat-bubble">
            🚀 Sistem siap digunakan untuk training dan klasifikasi layanan servis Yamaha menggunakan algoritma Random Forest.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================
# SECTION
# =========================================

st.markdown(
    """
    <div class="section-title">
        Dashboard Overview
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================
# SAMPLE CONTENT
# =========================================

uploaded_file = st.file_uploader(
    "📂 Upload Dataset CSV",
    type=["csv"]
)

if uploaded_file:

    st.success("Dataset berhasil diupload")
