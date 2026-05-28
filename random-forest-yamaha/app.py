import streamlit as st

st.set_page_config(
    page_title="Yamaha ML Dashboard",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#050816,#09111f,#0b1220);
    color: white;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#111827,#0f172a);
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

.card {
    padding: 28px;
    border-radius: 26px;
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 30px rgba(0,0,0,0.35);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-6px);
}

.metric-title {
    color: rgba(255,255,255,0.7);
    font-size: 15px;
    margin-bottom: 10px;
}

.metric-value {
    font-size: 32px;
    font-weight: 800;
    color: white;
}

.green {
    background: linear-gradient(
        135deg,
        rgba(34,197,94,0.25),
        rgba(22,163,74,0.18)
    );
}

.blue {
    background: linear-gradient(
        135deg,
        rgba(59,130,246,0.25),
        rgba(37,99,235,0.18)
    );
}

.orange {
    background: linear-gradient(
        135deg,
        rgba(249,115,22,0.25),
        rgba(234,88,12,0.18)
    );
}

.purple {
    background: linear-gradient(
        135deg,
        rgba(168,85,247,0.25),
        rgba(124,58,237,0.18)
    );
}

.status-box {
    margin-top: 30px;
    padding: 22px;
    border-radius: 22px;
    background: linear-gradient(
        135deg,
        rgba(34,197,94,0.20),
        rgba(22,163,74,0.12)
    );
    text-align: center;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.image("assets/yamaha.png", width=180)

st.sidebar.markdown("## Yamaha Dashboard")
st.sidebar.markdown("Machine Learning Random Forest")

# =========================
# HEADER
# =========================

st.markdown("""
<div class="main-title">
🏍️ Klasifikasi Layanan Servis Yamaha
</div>

<div class="sub-title">
Penerapan Algoritma Random Forest untuk klasifikasi layanan servis kendaraan Yamaha
</div>
""", unsafe_allow_html=True)

# =========================
# CARDS
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card green">
        <div class="metric-title">Algoritma</div>
        <div class="metric-value">Random Forest</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card blue">
        <div class="metric-title">Target</div>
        <div class="metric-value">2 Class</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card orange">
        <div class="metric-title">Dataset</div>
        <div class="metric-value">CSV</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card purple">
        <div class="metric-title">Status</div>
        <div class="metric-value">Ready</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# STATUS
# =========================

st.markdown("""
<div class="status-box">
✅ Sistem siap digunakan untuk klasifikasi layanan servis Yamaha
</div>
""", unsafe_allow_html=True)
