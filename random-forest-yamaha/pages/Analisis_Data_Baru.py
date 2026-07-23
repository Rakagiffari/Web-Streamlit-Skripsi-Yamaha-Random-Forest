# ==========================================================
# IMPORT
# ==========================================================

import streamlit as st
import pandas as pd
import joblib

from pathlib import Path

from utils.preprocessing import preprocess_new_data

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Analisis Data Baru",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# MODEL
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "model"

MODEL_PATH = MODEL_DIR / "random_forest_model.pkl"

FEATURE_PATH = MODEL_DIR / "feature_names.pkl"

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

/* ==========================================================
HASIL PREDIKSI
========================================================== */

.prediksi-wrapper{
    margin-top:10px;
}

.prediksi-left{
    background:#f3faf5;
    border:1px solid #d8eadc;
    border-radius:10px;
    height:180px;

    display:flex;
    align-items:center;
    justify-content:center;

    padding:20px;
}

.prediksi-left-danger{
    background:#fff1f1;
    border:1px solid #f0c7c7;
}

.prediksi-content{
    text-align:center;
}

.prediksi-title{

    font-size:15px;

    color:#6b7280;

    margin-bottom:10px;

    font-weight:500;

}

.prediksi-service-ringan{

    font-size:36px;

    font-weight:700;

    color:#15803d;

    letter-spacing:0.5px;

}

.prediksi-service-berat{

    font-size:36px;

    font-weight:700;

    color:#dc2626;

    letter-spacing:0.5px;

}

/* =============================== */

.info-box{

    border:1px solid #dfe3e8;

    border-radius:8px;

    padding:16px 18px;

    margin-bottom:12px;

    background:transparent;

}

.info-row{

    display:flex;

    justify-content:space-between;

    align-items:center;

}

.info-label{

    display:flex;

    align-items:center;

    gap:10px;

    font-size:15px;

    font-weight:500;

}

.info-value{

    font-size:17px;

    font-weight:700;

}

/* =============================== */

.badge-ringan{

    background:#e9f9ee;

    color:#15803d;

    padding:5px 14px;

    border-radius:20px;

    font-size:13px;

    font-weight:700;

}

.badge-berat{

    background:#fdeaea;

    color:#dc2626;

    padding:5px 14px;

    border-radius:20px;

    font-size:13px;

    font-weight:700;

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
# PEKERJAAN BERDASARKAN INDIKASI
# ==========================================================

with st.container(border=True):

    # ======================================================
    # DATABASE PEKERJAAN
    # ======================================================

    pekerjaan_db = {

        "Mesin":[

            {
                "Pilih": True,
                "Pekerjaan":"Ganti Oli Mesin",
                "Deskripsi":"Penggantian oli mesin",
                "Estimasi Waktu":10
            },

            {
                "Pilih":True,
                "Pekerjaan":"Ganti Busi",
                "Deskripsi":"Penggantian busi",
                "Estimasi Waktu":10
            },

            {
                "Pilih":True,
                "Pekerjaan":"Bersihkan Filter Udara",
                "Deskripsi":"Pembersihan filter udara",
                "Estimasi Waktu":10
            },

            {
                "Pilih":False,
                "Pekerjaan":"Setel Klep",
                "Deskripsi":"Penyetelan klep / valve",
                "Estimasi Waktu":40
            },

            {
                "Pilih":False,
                "Pekerjaan":"Cleaning Throttle Body",
                "Deskripsi":"Pembersihan throttle body",
                "Estimasi Waktu":30
            },

            {
                "Pilih":False,
                "Pekerjaan":"Cek Kompresi Mesin",
                "Deskripsi":"Pemeriksaan kompresi mesin",
                "Estimasi Waktu":20
            }

        ],

        "Transmisi":[

            {
                "Pilih":True,
                "Pekerjaan":"Servis CVT",
                "Deskripsi":"Pembersihan CVT",
                "Estimasi Waktu":35
            },

            {
                "Pilih":False,
                "Pekerjaan":"Ganti V-Belt",
                "Deskripsi":"Penggantian V-Belt",
                "Estimasi Waktu":25
            },

            {
                "Pilih":False,
                "Pekerjaan":"Ganti Roller",
                "Deskripsi":"Penggantian roller",
                "Estimasi Waktu":20
            },

            {
                "Pilih":False,
                "Pekerjaan":"Ganti Kampas Kopling",
                "Deskripsi":"Penggantian kampas kopling",
                "Estimasi Waktu":30
            },

            {
                "Pilih":False,
                "Pekerjaan":"Ganti Oli Gardan",
                "Deskripsi":"Penggantian oli gardan",
                "Estimasi Waktu":10
            }

        ],

        "Sistem Bahan Bakar":[

            {
                "Pilih":True,
                "Pekerjaan":"Cleaning Injector",
                "Deskripsi":"Pembersihan injektor",
                "Estimasi Waktu":30
            },

            {
                "Pilih":False,
                "Pekerjaan":"Cek Fuel Pump",
                "Deskripsi":"Pemeriksaan fuel pump",
                "Estimasi Waktu":20
            },

            {
                "Pilih":False,
                "Pekerjaan":"Cek Selang Bahan Bakar",
                "Deskripsi":"Pemeriksaan selang bahan bakar",
                "Estimasi Waktu":15
            },

            {
                "Pilih":False,
                "Pekerjaan":"Pembersihan Tangki",
                "Deskripsi":"Pembersihan tangki bahan bakar",
                "Estimasi Waktu":45
            }

        ],

        "Kelistrikan":[

            {
                "Pilih":True,
                "Pekerjaan":"Cek Aki",
                "Deskripsi":"Pemeriksaan aki",
                "Estimasi Waktu":10
            },

            {
                "Pilih":True,
                "Pekerjaan":"Cek Lampu",
                "Deskripsi":"Pemeriksaan lampu",
                "Estimasi Waktu":10
            },

            {
                "Pilih":False,
                "Pekerjaan":"Cek Starter",
                "Deskripsi":"Pemeriksaan starter",
                "Estimasi Waktu":20
            },

            {
                "Pilih":False,
                "Pekerjaan":"Cek Sistem Charging",
                "Deskripsi":"Pemeriksaan sistem charging",
                "Estimasi Waktu":20
            },

            {
                "Pilih":False,
                "Pekerjaan":"Cek Sekring",
                "Deskripsi":"Pemeriksaan sekring",
                "Estimasi Waktu":10
            }

        ],

        "Pengereman":[

            {
                "Pilih":True,
                "Pekerjaan":"Ganti Kampas Rem",
                "Deskripsi":"Penggantian kampas rem",
                "Estimasi Waktu":20
            },

            {
                "Pilih":False,
                "Pekerjaan":"Ganti Minyak Rem",
                "Deskripsi":"Penggantian minyak rem",
                "Estimasi Waktu":15
            },

            {
                "Pilih":False,
                "Pekerjaan":"Bleeding Rem",
                "Deskripsi":"Bleeding sistem rem",
                "Estimasi Waktu":20
            },

            {
                "Pilih":False,
                "Pekerjaan":"Cek Cakram",
                "Deskripsi":"Pemeriksaan cakram rem",
                "Estimasi Waktu":10
            }

        ],

        "Roda dan Suspensi":[

            {
                "Pilih":True,
                "Pekerjaan":"Cek Ban",
                "Deskripsi":"Pemeriksaan ban",
                "Estimasi Waktu":10
            },

            {
                "Pilih":False,
                "Pekerjaan":"Cek Bearing",
                "Deskripsi":"Pemeriksaan bearing roda",
                "Estimasi Waktu":20
            },

            {
                "Pilih":False,
                "Pekerjaan":"Ganti Shockbreaker",
                "Deskripsi":"Penggantian shockbreaker",
                "Estimasi Waktu":35
            }

        ],

        "Body":[

            {
                "Pilih":True,
                "Pekerjaan":"Perbaikan Cover Body",
                "Deskripsi":"Perbaikan cover body",
                "Estimasi Waktu":20
            },

            {
                "Pilih":False,
                "Pekerjaan":"Pengencangan Baut Body",
                "Deskripsi":"Pemeriksaan baut body",
                "Estimasi Waktu":10
            }

        ],

        "Umum":[

            {
                "Pilih":True,
                "Pekerjaan":"General Check",
                "Deskripsi":"Pemeriksaan umum kendaraan",
                "Estimasi Waktu":20
            }

        ]

    }

    df_pekerjaan = pd.DataFrame(
        pekerjaan_db.get(indikasi, [])
    )

    edited_df = st.data_editor(

        df_pekerjaan,

        hide_index=True,

        use_container_width=True,

        num_rows="fixed",

        column_config={

            "Pilih": st.column_config.CheckboxColumn(
                "Pilih"
            ),

            "Pekerjaan": st.column_config.TextColumn(
                "Pekerjaan",
                width="medium"
            ),

            "Deskripsi": st.column_config.TextColumn(
                "Deskripsi",
                width="large"
            ),

            "Estimasi Waktu": st.column_config.NumberColumn(
                "Estimasi Waktu",
                format="%d menit"
            )

        },

        disabled=[
            "Pekerjaan",
            "Deskripsi",
            "Estimasi Waktu"
        ]

    )

    # ======================================================
    # TOTAL ESTIMASI
    # ======================================================

    total_estimasi = edited_df.loc[
        edited_df["Pilih"],
        "Estimasi Waktu"
    ].sum()

    st.success(
        f"Total Estimasi Waktu Pekerjaan : **{int(total_estimasi)} menit**"
    )

# ==========================================================
# TOMBOL PREDIKSI
# ==========================================================

left, center, right = st.columns([2, 2, 2])

with center:

    prediksi_button = st.button(
        "🔍 Prediksi Layanan",
        use_container_width=True,
        type="primary"
    )

# ==========================================================
# PROSES PREDIKSI RANDOM FOREST
# ==========================================================

if prediksi_button:

    try:

        # ==================================================
        # LOAD MODEL RANDOM FOREST
        # ==================================================

        model = joblib.load(MODEL_PATH)

        # ==================================================
        # PREPROCESS DATA INPUT
        # ==================================================

        X_new = preprocess_new_data(
            model_motor=model_motor,
            tahun_motor=tahun_motor,
            kilometer=kilometer,
            indikasi=indikasi
        )

        # ==================================================
        # PREDIKSI
        # ==================================================

        prediksi = model.predict(X_new)[0]

        probabilitas = model.predict_proba(X_new)[0]

        confidence = float(max(probabilitas) * 100)

        # ==================================================
        # KONVERSI LABEL
        # ==================================================

        # Sesuaikan jika label model berbeda
        if str(prediksi).lower() in ["ringan", "service ringan"]:
            hasil_prediksi = "SERVICE RINGAN"
            kategori = "Ringan"

        elif str(prediksi).lower() in ["berat", "service berat"]:
            hasil_prediksi = "SERVICE BERAT"
            kategori = "Berat"

        elif prediksi == 0:
            hasil_prediksi = "SERVICE RINGAN"
            kategori = "Ringan"

        else:
            hasil_prediksi = "SERVICE BERAT"
            kategori = "Berat"

        # ==================================================
        # SIMPAN KE SESSION STATE
        # ==================================================

        st.session_state["hasil_prediksi"] = hasil_prediksi
        st.session_state["kategori"] = kategori
        st.session_state["confidence"] = confidence
        st.session_state["estimasi"] = int(total_estimasi)

        st.session_state["nama"] = nama
        st.session_state["no_polisi"] = no_polisi
        st.session_state["model_motor"] = model_motor
        st.session_state["jenis_motor"] = jenis_motor
        st.session_state["kilometer"] = kilometer
        st.session_state["tahun_motor"] = tahun_motor
        st.session_state["indikasi"] = indikasi
        st.session_state["pekerjaan"] = edited_df.loc[
            edited_df["Pilih"],
            "Pekerjaan"
        ].tolist()

        st.success("Prediksi berhasil dilakukan.")

    except Exception as e:

        st.error(f"Terjadi kesalahan saat melakukan prediksi.\n\n{e}")
        
st.markdown(
    """
    <div style="
        text-align:center;
        color:#9ca3af;
        font-size:14px;
        margin-top:-8px;
        margin-bottom:20px;
    ">
        Tekan tombol untuk menjalankan prediksi menggunakan model Random Forest.
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# HASIL PREDIKSI (RANDOM FOREST)
# ==========================================================

if "hasil_prediksi" in st.session_state:

    st.markdown("### 3. Hasil Prediksi (Random Forest)")

    # ======================================================
    # BADGE KATEGORI
    # ======================================================

    if st.session_state["kategori"] == "Ringan":

        left_class = "prediksi-left"

        service_class = "prediksi-service-ringan"

        badge = '<span class="badge-ringan">Ringan</span>'

    else:

        left_class = "prediksi-left prediksi-left-danger"

        service_class = "prediksi-service-berat"

        badge = '<span class="badge-berat">Berat</span>'

    # ======================================================
    # LAYOUT
    # ======================================================

    left, right = st.columns([1.15, 1.85], gap="large")

    # ======================================================
    # KOLOM KIRI
    # ======================================================

    with left:

        st.markdown(

            f"""

            <div class="{left_class}">

                <div class="prediksi-content">

                    <div class="prediksi-title">

                        Prediksi Layanan

                    </div>

                    <div class="{service_class}">

                        {st.session_state["hasil_prediksi"]}

                    </div>

                </div>

            </div>

            """,

            unsafe_allow_html=True

        )

    # ======================================================
    # KOLOM KANAN
    # ======================================================

    with right:

        # ------------------------------
        # Confidence
        # ------------------------------

        st.markdown(

            f"""

            <div class="info-box">

                <div class="info-row">

                    <div class="info-label">

                        🎯 Tingkat Keyakinan Model

                    </div>

                    <div class="info-value">

                        {st.session_state["confidence"]:.2f}%

                    </div>

                </div>

            </div>

            """,

            unsafe_allow_html=True

        )

        # ------------------------------
        # Estimasi
        # ------------------------------

        st.markdown(

            f"""

            <div class="info-box">

                <div class="info-row">

                    <div class="info-label">

                        🕒 Total Estimasi Waktu

                    </div>

                    <div class="info-value">

                        {st.session_state["estimasi"]} menit

                    </div>

                </div>

            </div>

            """,

            unsafe_allow_html=True

        )

        # ------------------------------
        # Kategori
        # ------------------------------

        st.markdown(

            f"""

            <div class="info-box">

                <div class="info-row">

                    <div class="info-label">

                        ⚙️ Kategori Berdasarkan Model

                    </div>

                    <div>

                        {badge}

                    </div>

                </div>

            </div>

            """,

            unsafe_allow_html=True

        )
