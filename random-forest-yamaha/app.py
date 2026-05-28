import streamlit as st

# ========================================
# PAGE CONFIG
# ========================================

st.set_page_config(
    page_title="Yamaha Random Forest",
    page_icon="🏍️",
    layout="wide"
)

# ========================================
# CUSTOM CSS
# ========================================

st.markdown("""
<style>

/* ========================================
BACKGROUND
======================================== */

[data-testid="stAppViewContainer"] {

    background-color: white;
}

[data-testid="stHeader"] {

    background: rgba(0,0,0,0);
}

/* ========================================
SIDEBAR
======================================== */

[data-testid="stSidebar"] {

    background-color: #111111;
}

[data-testid="stSidebar"] * {

    color: white;
}

/* ========================================
MAIN CONTAINER
======================================== */

.block-container {

    padding-top: 2rem;

    padding-left: 3rem;

    padding-right: 3rem;
}

/* ========================================
MAIN TITLE
======================================== */

.main-title {

    text-align: center;

    font-size: 56px;

    font-weight: 800;

    color: #111827;

    text-transform: uppercase;

    letter-spacing: 2px;

    margin-bottom: 5px;
}

/* ========================================
SUB TITLE
======================================== */

.sub-title {

    text-align: center;

    font-size: 20px;

    color: #dc2626;

    margin-top: -5px;

    margin-bottom: 40px;

    font-weight: 600;
}

/* ========================================
METRIC BUBBLE
======================================== */

.metric-box {

    background: linear-gradient(
        135deg,
        #dc2626,
        #b91c1c
    );

    padding: 35px 25px;

    border-radius: 30px;

    position: relative;

    overflow: hidden;

    color: white;

    text-align: center;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.25);

    transition: 0.3s ease;
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

/* hover effect */

.metric-box:hover {

    transform: translateY(-5px);

    box-shadow:
        0 25px 50px rgba(0,0,0,0.35);
}

/* metric title */

.metric-title {

    font-size: 16px;

    font-weight: 600;

    opacity: 0.9;

    margin-bottom: 18px;
}

/* metric value */

.metric-value {

    font-size: 42px;

    font-weight: 800;

    line-height: 1;
}

/* metric icon */

.metric-icon {

    margin-top: 18px;

    font-size: 42px;

    opacity: 0.25;
}

/* ========================================
STATUS BOX
======================================== */

.status-box {

    margin-top: 45px;

    background: white;

    border-left: 8px solid #dc2626;

    padding: 25px;

    border-radius: 22px;

    font-size: 18px;

    font-weight: 600;

    color: #111827;

    text-align: center;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

/* ========================================
SECTION TITLE
======================================== */

.section-title {

    text-align: center;

    margin-top: 50px;

    margin-bottom: 20px;

    font-size: 30px;

    font-weight: 800;

    color: #111827;
}

/* ========================================
UPLOAD FILE
======================================== */

[data-testid="stFileUploader"] {

    background: white;

    border: 2px dashed #dc2626;

    border-radius: 20px;

    padding: 20px;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

/* ========================================
BUTTON
======================================== */

.stButton {

    display: flex;

    justify-content: center;
}

.stButton > button {

    background-color: #dc2626;

    color: white;

    border: none;

    border-radius: 14px;

    padding: 14px 35px;

    font-weight: 700;

    font-size: 16px;

    transition: 0.3s ease;
}

.stButton > button:hover {

    background-color: #b91c1c;

    transform: scale(1.03);

    box-shadow:
        0 12px 25px rgba(0,0,0,0.20);
}

/* ========================================
DATAFRAME
======================================== */

[data-testid="stDataFrame"] {

    border-radius: 20px;

    overflow: hidden;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ========================================
# SIDEBAR
# ========================================

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

# ========================================
# HEADER
# ========================================

st.markdown("""
<div class="main-title">
    KLASIFIKASI LAYANAN SERVIS YAMAHA
</div>

<div class="sub-title">
    Penerapan Algoritma Random Forest untuk klasifikasi layanan servis kendaraan Yamaha
</div>
""", unsafe_allow_html=True)

# ========================================
# DATA
# ========================================

accuracy = 74
total_data = 1500
total_feature = 12

# ========================================
# METRIC CARDS
# ========================================

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

# ========================================
# STATUS BOX
# ========================================

st.markdown("""
<div class="status-box">
    🚀 Sistem siap digunakan untuk training dan klasifikasi layanan servis Yamaha
</div>
""", unsafe_allow_html=True)

# ========================================
# UPLOAD SECTION
# ========================================

st.markdown("""
<div class="section-title">
    Upload Dataset CSV
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload file CSV",
    type=["csv"]
)

if uploaded_file:

    st.success("Dataset berhasil diupload")

# ========================================
# TRAINING SECTION
# ========================================

st.markdown("""
<div class="section-title">
    Training Model
</div>
""", unsafe_allow_html=True)

if st.button("🚀 Mulai Training"):

    st.success("Training model berhasil dilakukan")
