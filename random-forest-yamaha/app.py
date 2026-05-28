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

/* ================================
MAIN BACKGROUND
================================ */

[data-testid="stAppViewContainer"] {

    background: linear-gradient(
        135deg,
        #050816 0%,
        #09111f 50%,
        #0b1220 100%
    );

    color: white;
}

/* ================================
HEADER
================================ */

[data-testid="stHeader"] {

    background: rgba(0,0,0,0);
}

/* ================================
SIDEBAR
================================ */

[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #111827 0%,
        #0f172a 100%
    );

    border-right: 1px solid rgba(255,255,255,0.08);
}

/* ================================
TITLE
================================ */

.main-title {

    font-size: 52px;

    font-weight: 800;

    color: white;

    margin-bottom: 10px;
}

.sub-title {

    font-size: 18px;

    color: #94a3b8;

    margin-bottom: 35px;
}

/* ================================
CARD
================================ */

.card {

    padding: 28px;

    border-radius: 24px;

    background: rgba(255,255,255,0.06);

    backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.08);

    box-shadow:
        0 8px 30px rgba(0,0,0,0.35);

    transition: 0.3s;
}

.card:hover {

    transform: translateY(-5px);

    border: 1px solid rgba(59,130,246,0.4);
}

/* ================================
METRIC
================================ */

.metric-title {

    color: rgba(255,255,255,0.7);

    font-size: 14px;

    margin-bottom: 10px;
}

.metric-value {

    font-size: 30px;

    font-weight: 800;

    color: white;
}

/* ================================
CARD COLORS
================================ */

.green {

    background:
        linear-gradient(
            135deg,
            rgba(34,197,94,0.25),
            rgba(22,163,74,0.15)
        );
}

.blue {

    background:
        linear-gradient(
            135deg,
            rgba(59,130,246,0.25),
            rgba(37,99,235,0.15)
        );
}

.orange {

    background:
        linear-gradient(
            135deg,
            rgba(249,115,22,0.25),
            rgba(234,88,12,0.15)
        );
}

.purple {

    background:
        linear-gradient(
            135deg,
            rgba(168,85,247,0.25),
            rgba(124,58,237,0.15)
        );
}

/* ================================
STATUS BOX
================================ */

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

    border: 1px solid rgba(34,197,94,0.20);

    text-align: center;

    font-weight: 700;

    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# LOGO
# =========================================

BASE_DIR = Path(__file__).parent

logo_path = BASE_DIR / "assets" / "yamaha_logo.png"

# =========================================
# SIDEBAR
# =========================================

if logo_path.exists():

    st.sidebar.image(
        str(logo_path),
        width=180
    )

st.sidebar.title(
    "Yamaha Machine Learning Dashboard"
)

st.sidebar.markdown(
    "Random Forest Classification System"
)

st.sidebar.success("✅ System Ready")

# =========================================
# HEADER
# =========================================

st.markdown(
    """
    <div class="main-title">
        🏍️ Klasifikasi Layanan Servis Yamaha
    </div>

    <div class="sub-title">
        Penerapan Algoritma Random Forest untuk klasifikasi layanan servis kendaraan Yamaha
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================
# CARDS
# =========================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(
        """
        <div class="card green">

            <div class="metric-title">
                Algoritma
            </div>

            <div class="metric-value">
                Random Forest
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="card blue">

            <div class="metric-title">
                Target
            </div>

            <div class="metric-value">
                2 Class
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
        <div class="card orange">

            <div class="metric-title">
                Dataset
            </div>

            <div class="metric-value">
                CSV
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with col4:

    st.markdown(
        """
        <div class="card purple">

            <div class="metric-title">
                Status
            </div>

            <div class="metric-value">
                Ready
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================
# STATUS
# =========================================

st.markdown(
    """
    <div class="status-box">
        ✅ Sistem siap digunakan untuk training dan klasifikasi layanan servis Yamaha
    </div>
    """,
    unsafe_allow_html=True
)
