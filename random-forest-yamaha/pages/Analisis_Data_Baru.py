# ==========================================================
# IMPORT
# ==========================================================

import pandas as pd
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
# LANGKAH 1 - BAGIAN 2
# DATA KENDARAAN
# ==========================================================

with st.container(border=True):

    st.markdown("### 1. Data Kendaraan")

    st.markdown("<br>", unsafe_allow_html=True)

    # ======================================================
    # MAPPING MODEL -> JENIS
    # ======================================================

    jenis_mapping = {

        # ================= MAXi =================
        "NMAX 155"         : "MAXi",
        "AEROX 155"        : "MAXi",
        "LEXI 125"         : "MAXi",
        "LEXI LX 155"      : "MAXi",
        "XMAX 250"         : "MAXi",
        "XMAX 300"         : "MAXi",
        "TMAX 560"         : "MAXi",

        # ================= Classy =================
        "FAZZIO 125"       : "Classy",
        "GRAND FILANO 125" : "Classy",

        # ================= Matic =================
        "MIO M3"           : "Matic",
        "MIO SPORTY"       : "Matic",
        "MIO J"            : "Matic",
        "MIO GT"           : "Matic",
        "MIO Z"            : "Matic",
        "MIO S"            : "Matic",
        "FREEGO 125"       : "Matic",
        "GEAR 125"         : "Matic",
        "FINO 125"         : "Matic",
        "FINO 115"         : "Matic",
        "XEON 125"         : "Matic",
        "SOUL GT 125"      : "Matic",
        "X-RIDE 125"       : "Matic",

        # ================= Moped =================
        "JUPITER Z"        : "Moped",
        "JUPITER MX"       : "Moped",
        "VEGA FORCE"       : "Moped",
        "CRYPTON"          : "Moped",

        # ================= Sport =================
        "VIXION"           : "Sport",
        "VIXION R"         : "Sport",
        "R15"              : "Sport",
        "R15M"             : "Sport",
        "R25"              : "Sport",
        "MT-15"            : "Sport",
        "XSR 155"          : "Sport",

        # ================= Off-road =================
        "WR155R"           : "Off-road",
        "YZ125X"           : "Off-road"

    }

    # ======================================================
    # BARIS 1
    # ======================================================

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

    # ======================================================
    # BARIS 2
    # ======================================================

    col3, col4 = st.columns(2, gap="large")

    with col3:

        model_motor = st.selectbox(

            "Model Motor",

            sorted(jenis_mapping.keys())

        )

    jenis_motor = jenis_mapping.get(
        model_motor,
        "-"
    )

    with col4:

        st.text_input(
            "Jenis",
            value=jenis_motor,
            disabled=True
        )

    # ======================================================
    # BARIS 3
    # ======================================================

    col5, col6 = st.columns(2, gap="large")

    with col5:

        kilometer = st.number_input(

            "Kilometer",

            min_value=0,

            value=0,

            step=500,

            format="%d"

        )

    with col6:

        tahun_motor = st.number_input(

            "Tahun Motor",

            min_value=1990,

            max_value=2100,

            value=2020,

            step=1,

            format="%d"

        )

    # ======================================================
    # BARIS 4
    # ======================================================

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

# ==========================================================
# LANGKAH 1 - BAGIAN 3
# PEKERJAAN BERDASARKAN INDIKASI
# ==========================================================

with st.container(border=True):

    st.markdown("### 2. Pekerjaan Berdasarkan Indikasi")

    st.markdown(
        f"**Indikasi Terpilih :** :blue[{indikasi}]"
    )

    # ======================================================
    # DATABASE PEKERJAAN
    # ======================================================

    pekerjaan_db = {

        "Mesin":[

            ["Ganti Oli", "Penggantian oli mesin", 10],
            ["Ganti Busi", "Penggantian busi", 15],
            ["Bersihkan Filter Udara", "Pembersihan filter udara", 10],
            ["Setel Klep", "Penyetelan klep / valve", 40],
            ["Bersihkan Throttle Body", "Pembersihan throttle body", 30],
            ["Cek Kompresi Mesin", "Pemeriksaan kompresi mesin", 30]

        ],

        "Transmisi":[

            ["Servis CVT", "Pembersihan CVT", 35],
            ["Ganti V-Belt", "Penggantian V-Belt", 40],
            ["Ganti Roller", "Penggantian roller", 25],
            ["Cek Kampas Kopling", "Pemeriksaan kampas kopling", 30]

        ],

        "Kelistrikan":[

            ["Cek Aki", "Pemeriksaan aki", 10],
            ["Cek Lampu", "Pemeriksaan lampu", 10],
            ["Cek Starter", "Pemeriksaan starter", 15],
            ["Cek Sistem Charging", "Pemeriksaan sistem pengisian", 20]

        ],

        "Pengereman":[

            ["Ganti Kampas Rem", "Penggantian kampas rem", 25],
            ["Bleeding Rem", "Penggantian minyak rem", 20],
            ["Cek Cakram", "Pemeriksaan cakram", 15]

        ],

        "Roda dan Suspensi":[

            ["Cek Ban", "Pemeriksaan ban", 10],
            ["Cek Bearing", "Pemeriksaan bearing", 20],
            ["Cek Shockbreaker", "Pemeriksaan shockbreaker", 30]

        ],

        "Body":[

            ["Perbaikan Cover", "Perbaikan body kendaraan", 25],
            ["Pengencangan Baut", "Pemeriksaan baut", 15]

        ],

        "Sistem Bahan Bakar":[

            ["Cleaning Injector", "Pembersihan injektor", 35],
            ["Cleaning Throttle Body", "Pembersihan throttle body", 30],
            ["Cek Fuel Pump", "Pemeriksaan fuel pump", 25]

        ],

        "Umum":[

            ["General Service", "Pemeriksaan umum kendaraan", 30]

        ]

    }

    data = pekerjaan_db.get(indikasi, [])

    df = pd.DataFrame(
        data,
        columns=[
            "Pekerjaan",
            "Deskripsi",
            "Estimasi Waktu (menit)"
        ]
    )

    df.insert(
        0,
        "Pilih",
        [True]*len(df)
    )

    edited_df = st.data_editor(

        df,

        use_container_width=True,

        hide_index=True,

        column_config={

            "Pilih": st.column_config.CheckboxColumn(
                "Pilih"
            ),

            "Pekerjaan": st.column_config.TextColumn(
                "Pekerjaan"
            ),

            "Deskripsi": st.column_config.TextColumn(
                "Deskripsi"
            ),

            "Estimasi Waktu (menit)": st.column_config.NumberColumn(
                "Estimasi Waktu",
                format="%d menit"
            )

        },

        disabled=[
            "Pekerjaan",
            "Deskripsi",
            "Estimasi Waktu (menit)"
        ]

    )

    # ======================================================
    # TOTAL ESTIMASI
    # ======================================================

    total_menit = edited_df.loc[
        edited_df["Pilih"],
        "Estimasi Waktu (menit)"
    ].sum()

    st.success(
        f"⏱️ Total Estimasi Waktu Pekerjaan : **{total_menit} menit**"
    )

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
