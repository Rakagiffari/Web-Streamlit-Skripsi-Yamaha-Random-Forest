# ==========================================================
# SCHEDULER
# Penjadwalan Otomatis Mekanik
# ==========================================================

from datetime import datetime, timedelta, time
from pathlib import Path

import pandas as pd

# ==========================================================
# KONFIGURASI FOLDER
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

RIWAYAT_PATH = DATA_DIR / "riwayat_layanan.xlsx"

# ==========================================================
# JAM OPERASIONAL BENGKEL
# ==========================================================

JAM_BUKA = time(8, 0)

JAM_TUTUP = time(17, 0)

# ==========================================================
# JAM ISTIRAHAT
# ==========================================================

# Istirahat + Sholat Zuhur
ISTIRAHAT_ZUHUR_MULAI = time(12, 0)
ISTIRAHAT_ZUHUR_SELESAI = time(13, 0)

# Sholat Ashar
ISTIRAHAT_ASHAR_MULAI = time(15, 30)
ISTIRAHAT_ASHAR_SELESAI = time(16, 0)

# ==========================================================
# DATA MEKANIK
# ==========================================================

MEKANIK = [

    {
        "id": 1,
        "nama": "BINTANG FEBRUHAJI"
    },

    {
        "id": 2,
        "nama": "RAHBIL SAPUTRA"
    },

    {
        "id": 3,
        "nama": "RISKY MEMET PUTRA"
    },

    {
        "id": 4,
        "nama": "SEPTIO YALDRI PUTRA"
    }

]

# ==========================================================
# KOLOM FILE RIWAYAT
# ==========================================================

KOLOM_RIWAYAT = [

    "Tanggal",

    "Nomor Antrean",

    "Nama Pelanggan",

    "No Polisi",

    "Model Motor",

    "Jenis Motor",

    "Kilometer",

    "Tahun Motor",

    "Indikasi",

    "Kategori",

    "Confidence",

    "Estimasi",

    "Mekanik",

    "Jam Mulai",

    "Jam Selesai",

    "Status"

]

# ==========================================================
# STATUS LAYANAN
# ==========================================================

STATUS_MENUNGGU = "Menunggu"

STATUS_DIPROSES = "Diproses"

STATUS_SELESAI = "Selesai"

STATUS_PENUH = "Penuh"

# ==========================================================
# STATUS MEKANIK
# ==========================================================

MEKANIK_TERSEDIA = "Tersedia"

MEKANIK_SERVIS = "Sedang Servis"

MEKANIK_ISTIRAHAT = "Istirahat"

MEKANIK_PULANG = "Pulang"

# ==========================================================
# MEMBUAT FILE RIWAYAT JIKA BELUM ADA
# ==========================================================

def buat_file_riwayat():
    """
    Membuat file riwayat_layanan.xlsx apabila belum tersedia.
    """

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not RIWAYAT_PATH.exists():

        df = pd.DataFrame(columns=KOLOM_RIWAYAT)

        df.to_excel(
            RIWAYAT_PATH,
            index=False
        )


# ==========================================================
# MEMBACA SELURUH RIWAYAT
# ==========================================================

def baca_riwayat():
    """
    Membaca seluruh data riwayat layanan.
    """

    buat_file_riwayat()

    try:

        df = pd.read_excel(RIWAYAT_PATH)

    except Exception:

        df = pd.DataFrame(columns=KOLOM_RIWAYAT)

    return df


# ==========================================================
# RIWAYAT HARI INI
# ==========================================================

def riwayat_hari_ini():
    """
    Mengambil data layanan pada tanggal hari ini.
    """

    df = baca_riwayat()

    if df.empty:
        return df

    hari_ini = datetime.now().strftime("%Y-%m-%d")

    df["Tanggal"] = pd.to_datetime(
        df["Tanggal"]
    ).dt.strftime("%Y-%m-%d")

    return df[df["Tanggal"] == hari_ini]


# ==========================================================
# NOMOR ANTREAN OTOMATIS
# ==========================================================

def nomor_antrian_otomatis():
    """
    Menghasilkan nomor antrean berikutnya.
    """

    df = riwayat_hari_ini()

    if df.empty:
        return "A001"

    nomor = len(df) + 1

    return f"A{nomor:03d}"


# ==========================================================
# JUMLAH PELANGGAN HARI INI
# ==========================================================

def total_pelanggan_hari_ini():

    return len(riwayat_hari_ini())


# ==========================================================
# CEK APAKAH FILE SUDAH SIAP
# ==========================================================

buat_file_riwayat()

# ==========================================================
# KONVERSI WAKTU
# ==========================================================

def gabung_tanggal_jam(jam_obj):
    """
    Menggabungkan tanggal hari ini dengan objek time.
    """

    hari_ini = datetime.now().date()

    return datetime.combine(
        hari_ini,
        jam_obj
    )


def format_jam(dt):
    """
    Mengubah datetime menjadi format HH:MM.
    """

    return dt.strftime("%H:%M")


# ==========================================================
# CEK JAM ISTIRAHAT
# ==========================================================

def dalam_istirahat(dt):
    """
    Mengecek apakah waktu berada pada jam istirahat.
    """

    jam = dt.time()

    if ISTIRAHAT_ZUHUR_MULAI <= jam < ISTIRAHAT_ZUHUR_SELESAI:
        return True

    if ISTIRAHAT_ASHAR_MULAI <= jam < ISTIRAHAT_ASHAR_SELESAI:
        return True

    return False


# ==========================================================
# LOMPAT KE AKHIR ISTIRAHAT
# ==========================================================

def lewati_istirahat(dt):
    """
    Jika waktu berada pada jam istirahat,
    langsung lompat ke akhir jam istirahat.
    """

    jam = dt.time()

    if ISTIRAHAT_ZUHUR_MULAI <= jam < ISTIRAHAT_ZUHUR_SELESAI:

        return gabung_tanggal_jam(
            ISTIRAHAT_ZUHUR_SELESAI
        )

    if ISTIRAHAT_ASHAR_MULAI <= jam < ISTIRAHAT_ASHAR_SELESAI:

        return gabung_tanggal_jam(
            ISTIRAHAT_ASHAR_SELESAI
        )

    return dt


# ==========================================================
# HITUNG JAM SELESAI SERVIS
# ==========================================================

def hitung_jam_selesai(
    jam_mulai,
    estimasi_menit
):
    """
    Menghitung jam selesai dengan memperhatikan
    jam istirahat.
    """

    sekarang = jam_mulai

    sisa = estimasi_menit

    while sisa > 0:

        sekarang = lewati_istirahat(sekarang)

        jam = sekarang.time()

        # ==============================
        # Sebelum Zuhur
        # ==============================

        if jam < ISTIRAHAT_ZUHUR_MULAI:

            batas = gabung_tanggal_jam(
                ISTIRAHAT_ZUHUR_MULAI
            )

        # ==============================
        # Setelah Zuhur
        # ==============================

        elif jam < ISTIRAHAT_ASHAR_MULAI:

            batas = gabung_tanggal_jam(
                ISTIRAHAT_ASHAR_MULAI
            )

        # ==============================
        # Setelah Ashar
        # ==============================

        else:

            batas = gabung_tanggal_jam(
                JAM_TUTUP
            )

        menit_tersedia = int(

            (batas - sekarang).total_seconds()

            / 60

        )

        if sisa <= menit_tersedia:

            sekarang += timedelta(
                minutes=sisa
            )

            sisa = 0

        else:

            sekarang = batas

            sisa -= menit_tersedia

    return sekarang


# ==========================================================
# CEK MASIH DALAM JAM OPERASIONAL
# ==========================================================

def masih_jam_operasional(
    jam_selesai
):
    """
    Mengecek apakah servis selesai
    sebelum jam tutup.
    """

    return jam_selesai.time() <= JAM_TUTUP


# ==========================================================
# WAKTU SEKARANG YANG VALID
# ==========================================================

def waktu_sekarang():

    sekarang = datetime.now()

    if sekarang.time() < JAM_BUKA:

        return gabung_tanggal_jam(
            JAM_BUKA
        )

    sekarang = lewati_istirahat(
        sekarang
    )

    return sekarang

# ==========================================================
# JAM TERSEDIA MASING-MASING MEKANIK
# ==========================================================

def waktu_tersedia_mekanik():
    """
    Mengembalikan jam tersedia setiap mekanik.
    """

    df = riwayat_hari_ini()

    sekarang = waktu_sekarang()

    hasil = {}

    # jika belum ada riwayat
    if df.empty:

        for mekanik in MEKANIK:

            hasil[mekanik["nama"]] = sekarang

        return hasil

    # pastikan format datetime
    df["Jam Selesai"] = pd.to_datetime(
        df["Jam Selesai"],
        format="%H:%M",
        errors="coerce"
    )

    for mekanik in MEKANIK:

        nama = mekanik["nama"]

        data = df[df["Mekanik"] == nama]

        if data.empty:

            hasil[nama] = sekarang

            continue

        terakhir = data["Jam Selesai"].max()

        if pd.isna(terakhir):

            hasil[nama] = sekarang

            continue

        tersedia = datetime.combine(
            sekarang.date(),
            terakhir.time()
        )

        tersedia = lewati_istirahat(tersedia)

        if tersedia < sekarang:

            tersedia = sekarang

        hasil[nama] = tersedia

    return hasil


# ==========================================================
# MEMILIH MEKANIK PALING CEPAT TERSEDIA
# ==========================================================

def pilih_mekanik():
    """
    Mengembalikan mekanik yang paling cepat tersedia.
    """

    tersedia = waktu_tersedia_mekanik()

    nama = min(
        tersedia,
        key=tersedia.get
    )

    return nama, tersedia[nama]


# ==========================================================
# MEMBUAT JADWAL BARU
# ==========================================================

def buat_jadwal(
    estimasi_menit
):
    """
    Membuat jadwal servis otomatis.
    """

    nomor = nomor_antrian_otomatis()

    mekanik, mulai = pilih_mekanik()

    selesai = hitung_jam_selesai(
        mulai,
        estimasi_menit
    )

    if masih_jam_operasional(selesai):

        status = "Dalam Jam Operasional"

    else:

        status = "Penuh Hari Ini"

    return {

        "Nomor Antrean": nomor,

        "Mekanik": mekanik,

        "Jam Mulai": format_jam(mulai),

        "Jam Selesai": format_jam(selesai),

        "Estimasi": estimasi_menit,

        "Status": status

    }


# ==========================================================
# INFO SEMUA MEKANIK
# ==========================================================

def daftar_status_mekanik():
    """
    Menghasilkan status seluruh mekanik.
    """

    tersedia = waktu_tersedia_mekanik()

    data = []

    sekarang = waktu_sekarang()

    for nama, jam in tersedia.items():

        if jam <= sekarang:

            status = "Tersedia"

            kembali = "Sekarang"

        else:

            status = "Sedang Servis"

            kembali = format_jam(jam)

        data.append({

            "Mekanik": nama,

            "Status": status,

            "Tersedia Kembali": kembali

        })

    return pd.DataFrame(data)
