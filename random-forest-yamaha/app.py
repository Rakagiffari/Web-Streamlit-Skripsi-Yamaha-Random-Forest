import streamlit as st

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Yamaha Random Forest",
    page_icon="🏍️",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

/* ==============================
BACKGROUND
============================== */

[data-testid="stAppViewContainer"] {
    background-color: white;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* ==============================
SIDEBAR
============================== */

[data-testid="stSidebar"] {
    background-color: #111111;
}

[data-testid="stSidebar"] * {
    color: white;
}

/* ==============================
TITLE
============================== */

.main-title {
    font-size: 50px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 10px;
}

.sub-title {
    font-size: 18px;
    color: #6b7280;
    margin-bottom: 40px;
}

/* ==============================
METRIC BUBBLE
============================== */

.metric-box {

    background: linear-gradient(
        135deg,
        #dc2626,
        #b91c1c
    );

    padding: 28px;

    border-radius: 28px;

    position: relative;

    overflow: hidden;

    color: white;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.25);

    transition: 0.3s ease;
}

.metric-box:hover {

    transform: translateY(-5px);

    box-shadow:
        0 25px 45px rgba(0,0,0,0.35);
}

/* bubble effect */

.metric-box::before {

    content: "";

    position: absolute;

    width: 140px;

    height: 140px;

    background: rgba(255,255,255,0.08);

    border-radius: 50%;

    top: -60px;

    right: -60px;
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

    font-size: 38px;

    font-weight: 800;

    line-height: 1;
}

/* icon */

.metric-icon {

    position: absolute;

    right: 20px;

    bottom: 10px;

    font-size: 42px;

    opacity: 0.18;
}

/* ==============================
STATUS BOX
============================== */

.status-box {

    margin-top: 40px;

    background: white;

    border-left: 7px solid #dc2626;

    padding: 24px;

    border-radius: 20px;

    font-size: 17px;

    font-weight: 600;

    color: #111827;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

/* ==============================
UPLOAD FILE
============================== */

[data-testid="stFileUploader"] {

    background: white;

    border: 2px dashed #dc2626;

    border-radius: 20px;

    padding: 20px;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

/* ==============================
BUTTON
============================== */

.stButton > button {

    background-color: #dc2626;

    color: white;

    border: none;

    border-radius: 12px;

    padding: 12px 25px;

    font-weight: 700;

    transition: 0.3s;
}

.stButton > button:hover {

    background-color: #b91c1c;

    transform: scale(1.02);
}

/* ==============================
DATAFRAME
============================== */

[data-testid="stDataFrame"] {

    border-radius: 20px;

    overflow: hidden;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================

st.sidebar.title("🏍️ Yamaha Dashboard")

st.sidebar.success("System Connected")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### Menu

- Dashboard
- Upload Dataset
- Training Model
- Evaluasi
- Prediksi
""")

# =========================================
# HEADER
# =========================================

st.markdown("""
<div class="main-title">
    Klasifikasi Layanan Servis Yamaha
</div>

<div class="sub-title">
    Penerapan Algoritma Random Forest untuk klasifikasi layanan servis kendaraan Yamaha
</div>
""", unsafe_allow_html=True)

# =========================================
# DUMMY DATA
# =========================================

accuracy = 74
total_data = 1500
total_feature = 12

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
    🚀 Sistem siap digunakan untuk training dan klasifikasi layanan servis Yamaha.
</div>
""", unsafe_allow_html=True)

# =========================================
# FILE UPLOAD
# =========================================

st.markdown("## 📂 Upload Dataset")

uploaded_file = st.file_uploader(
    "Upload file CSV",
    type=["csv"]
)

if uploaded_file:

    st.success("Dataset berhasil diupload")

# =========================================
# BUTTON
# =========================================

st.markdown("## 🚀 Training Model")

if st.button("Mulai Training"):

    st.success("Training model berhasil dilakukan")
