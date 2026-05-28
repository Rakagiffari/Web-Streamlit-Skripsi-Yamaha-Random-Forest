import streamlit as st

</style>
""", unsafe_allow_html=True)

# ======================================
# LOGO
# ======================================

BASE_DIR = Path(__file__).parent
logo_path = BASE_DIR / "assets" / "yamaha_logo.png"

if logo_path.exists():
    st.sidebar.image(str(logo_path), width=180)

st.sidebar.title("Yamaha ML Dashboard")
st.sidebar.success("✅ Connected System")

# ======================================
# HEADER
# ======================================

st.markdown("""
<div class="main-title">
🏍️ Klasifikasi Layanan Servis Yamaha
</div>

<div class="sub-title">
Penerapan Algoritma Random Forest untuk klasifikasi layanan servis kendaraan Yamaha
</div>
""", unsafe_allow_html=True)

# ======================================
# CARDS
# ======================================

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

st.markdown("""
<div class="status-box">
✅ Sistem terhubung dan siap digunakan
</div>
""", unsafe_allow_html=True)
