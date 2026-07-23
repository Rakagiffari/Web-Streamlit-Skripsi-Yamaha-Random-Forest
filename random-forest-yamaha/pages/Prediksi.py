import streamlit as st

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="Prediksi Layanan",
    page_icon="🔍",
    layout="wide"
)

# =========================================
# STYLE
# =========================================

st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:700;
    color:white;
    margin-bottom:0px;
}

.sub-title{
    color:#9ca3af;
    font-size:14px;
    margin-top:-10px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown(
    '<p class="main-title">🔍 Prediksi Layanan Service</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Masukkan informasi kendaraan untuk melakukan prediksi layanan service menggunakan Random Forest.</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# =========================================
# MAPPING MODEL -> JENIS
# =========================================

def get_jenis(model):

    model = model.upper()

    if any(x in model for x in ["XMAX","NMAX","AEROX","LEXI","TMAX"]):
        return "MAXi"

    elif any(x in model for x in ["FAZZIO","FILANO"]):
        return "Classy"

    elif any(x in model for x in [
        "MIO","SOUL","XEON","FINO",
        "GEAR","FREEGO","X-RIDE",
        "XRIDE","NOUVO","LEXAM"
    ]):
        return "Matic"

    elif any(x in model for x in [
        "R15","R25","R6","R1",
        "VIXION","BYSON",
        "SCORPIO","RX",
        "XSR","MT"
    ]):
        return "Sport"

    elif any(x in model for x in [
        "WR","YZ"
    ]):
        return "Off-road"

    elif any(x in model for x in [
        "JUPITER","VEGA",
        "CRYPTON","ALFA",
        "SIGMA","F1ZR",
        "MX KING"
    ]):
        return "Moped"

    return "Unknown"

col1, col2 = st.columns(2)
with col1:

    model = st.selectbox(
        "Model Kendaraan",
        [
            "NMAX 155",
            "AEROX 155",
            "LEXI 125",
            "XMAX 250",
            "FAZZIO",
            "GRAND FILANO",
            "MIO M3",
            "GEAR 125",
            "FREEGO 125",
            "VIXION",
            "R15",
            "WR155R",
            "JUPITER Z1"
        ]
    )

with col2:

    jenis = get_jenis(model)

    st.text_input(
        "Jenis Motor",
        value=jenis,
        disabled=True
    )

col3, col4 = st.columns(2)
with col3:

    tahun = st.number_input(
        "Tahun Motor",
        min_value=2000,
        max_value=2030,
        value=2022
    )
with col4:

    km = st.number_input(
        "Kilometer",
        min_value=0,
        value=10000,
        step=100
    )

indikasi = st.selectbox(
    "Indikasi",
    [
        "Mesin",
        "Transmisi",
        "Kelistrikan",
        "Pengereman",
        "Roda dan Suspensi",
        "Body",
        "Umum"
    ]
)

st.button(
    "🔍 Prediksi Layanan",
    use_container_width=True
)
