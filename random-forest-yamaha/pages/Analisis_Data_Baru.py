# ==========================================================
# IMPORT
# ==========================================================

import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Analisis Data Baru",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# STYLE
# ==========================================================

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

/* ===================================================
SUCCESS BOX
=================================================== */

.stAlert{
    border-radius:8px;
}

.stAlert p{
    font-size:12.5px !important;
    font-weight:450 !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    """
    <p class="main-title">
        📊 Analisis Data Baru
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="sub-title">
        Random Forest untuk Analisis dan Prediksi Layanan Service Kendaraan Yamaha
    </p>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# DATA KENDARAAN
# ==========================================================

with st.container(border=True):

    st.markdown("### 1. Data Kendaraan")

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================
    # BARIS 1
    # =====================================

    col1, col2 = st.columns(2, gap="large")

    with col1:

        nama = st.text_input(
            "Nama Pelanggan",
            placeholder="Masukkan nama pelanggan"
        )

    with col2:

        no_polisi = st.text_input(
            "No. Polisi",
            placeholder="Contoh : BA 1234 XX"
        )

    # =====================================
    # BARIS 2
    # =====================================

    col3, col4 = st.columns(2, gap="large")

    with col3:

        jenis_motor = st.selectbox(

            "Jenis Motor",

            [

                "Pilih Jenis Motor",

                "NMAX 155",
                "AEROX 155",
                "LEXI 155",
                "XMAX 250",

                "FAZZIO 125",
                "GRAND FILANO",

                "MIO M3",
                "MIO SPORTY",
                "FREEGO 125",
                "GEAR 125",

                "JUPITER Z",
                "JUPITER MX",

                "VIXION",
                "R15",
                "R25"

            ]

        )

    with col4:

        tahun_motor = st.selectbox(

            "Tahun Motor",

            list(range(2026, 1999, -1))

        )

    # =====================================
    # BARIS 3
    # =====================================

    col5, col6 = st.columns(2, gap="large")

    with col5:

        kilometer = st.number_input(

            "Kilometer",

            min_value=0,

            step=500,

            placeholder="Masukkan kilometer"

        )

    with col6:

        indikasi = st.selectbox(

            "Indikasi Utama",

            [

                "Mesin",

                "Transmisi",

                "Sistem Bahan Bakar",

                "Kelistrikan",

                "Pengereman",

                "Roda dan Suspensi",

                "Body",

                "Umum"

            ]

        )

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")
