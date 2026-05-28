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
# CSS
# =========================================

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {

    background: linear-gradient(
        135deg,
        #050816 0%,
        #09111f 50%,
        #0b1220 100%
    );

    color: white;
}

[data-testid="stHeader"] {

    background: rgba(0,0,0,0);
}

[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #111827 0%,
        #0f172a 100%
    );
}

.main-title {

    font-size: 52px;

    font-weight: 800;

    color: white;
}

.sub-title {

    color: #94a3b8;

    font-size: 18px;

    margin-bottom: 35px;
}

[data-testid="metric-container"] {

    background: rgba(255,255,255,0.05);

    border: 1px solid rgba(255,255,255,0.08);

    padding: 20px;

    border-radius: 20px;

    backdrop-filter: blur(10px);

    box-shadow:
        0 8px 30px rgba(0,0,0,0.25);
}

.status-box {

    margin-top: 30px;

    padding: 20px;

    border-radius: 20px;

    background:
        linear-gradient(
            135deg,
            rgba(34,197,94,0.20),
            rgba(22,163,74,0.12)
        );

    text-align: center;

    font-weight: 700;
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

st.sidebar.title("Yamaha ML Dashboard")

st.sidebar.success("System Connected")

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
# STATUS
# =========================================

st.markdown(
    """
    <div class="status-box">
        Sistem siap digunakan untuk training dan klasifikasi layanan servis Yamaha
    </div>
    """,
    unsafe_allow_html=True
)
