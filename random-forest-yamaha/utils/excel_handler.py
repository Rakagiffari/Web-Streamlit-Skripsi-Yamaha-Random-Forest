# ==========================================================
# EXCEL HANDLER
# Mengelola Riwayat Layanan
# ==========================================================

from pathlib import Path
from datetime import datetime

import pandas as pd

# ==========================================================
# FOLDER
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(
    parents=True,
    exist_ok=True
)

EXCEL_PATH = DATA_DIR / "riwayat_layanan.xlsx"

# ==========================================================
# NAMA SHEET
# ==========================================================

SHEET_NAME = "Riwayat"

# ==========================================================
# KOLOM EXCEL
# ==========================================================

KOLOM = [

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
# MEMBUAT FILE EXCEL
# ==========================================================

def buat_excel():

    """
    Membuat file Excel apabila belum ada.
    """

    if EXCEL_PATH.exists():

        return

    df = pd.DataFrame(
        columns=KOLOM
    )

    df.to_excel(

        EXCEL_PATH,

        sheet_name=SHEET_NAME,

        index=False

    )

# ==========================================================
# MEMBACA EXCEL
# ==========================================================

def baca_excel():

    """
    Membaca seluruh data riwayat.
    """

    buat_excel()

    try:

        df = pd.read_excel(

            EXCEL_PATH,

            sheet_name=SHEET_NAME

        )

    except Exception:

        df = pd.DataFrame(
            columns=KOLOM
        )

    return df

# ==========================================================
# MENYIMPAN EXCEL
# ==========================================================

def simpan_excel(df):

    """
    Menyimpan dataframe ke Excel.
    """

    df.to_excel(

        EXCEL_PATH,

        sheet_name=SHEET_NAME,

        index=False

    )

# ==========================================================
# TOTAL DATA
# ==========================================================

def total_data():

    """
    Menghitung jumlah seluruh data.
    """

    df = baca_excel()

    return len(df)

# ==========================================================
# TOTAL DATA HARI INI
# ==========================================================

def total_hari_ini():

    """
    Menghitung jumlah layanan hari ini.
    """

    df = baca_excel()

    if df.empty:

        return 0

    hari_ini = datetime.now().strftime("%Y-%m-%d")

    df["Tanggal"] = pd.to_datetime(

        df["Tanggal"]

    ).dt.strftime("%Y-%m-%d")

    return len(

        df[
            df["Tanggal"] == hari_ini
        ]

    )

# ==========================================================
# MEMBUAT FILE SAAT PERTAMA DIIMPORT
# ==========================================================

buat_excel()

# ==========================================================
# MENAMBAHKAN DATA LAYANAN BARU
# ==========================================================

def simpan_layanan(
    nama_pelanggan,
    no_polisi,
    model_motor,
    jenis_motor,
    kilometer,
    tahun_motor,
    indikasi,
    kategori,
    confidence,
    estimasi,
    mekanik,
    jam_mulai,
    jam_selesai,
    status,
    nomor_antrean
):
    """
    Menambahkan satu data layanan baru ke Excel.
    """

    df = baca_excel()

    data_baru = {

        "Tanggal": datetime.now().strftime("%Y-%m-%d"),

        "Nomor Antrean": nomor_antrean,

        "Nama Pelanggan": nama_pelanggan,

        "No Polisi": no_polisi,

        "Model Motor": model_motor,

        "Jenis Motor": jenis_motor,

        "Kilometer": kilometer,

        "Tahun Motor": tahun_motor,

        "Indikasi": indikasi,

        "Kategori": kategori,

        "Confidence": round(float(confidence), 2),

        "Estimasi": estimasi,

        "Mekanik": mekanik,

        "Jam Mulai": jam_mulai,

        "Jam Selesai": jam_selesai,

        "Status": status

    }

    df = pd.concat(

        [

            df,

            pd.DataFrame([data_baru])

        ],

        ignore_index=True

    )

    simpan_excel(df)

    return data_baru


# ==========================================================
# MEMBACA DATA HARI INI
# ==========================================================

def baca_hari_ini():
    """
    Mengambil seluruh layanan pada hari ini.
    """

    df = baca_excel()

    if df.empty:

        return df

    hari_ini = datetime.now().strftime("%Y-%m-%d")

    df["Tanggal"] = pd.to_datetime(

        df["Tanggal"]

    ).dt.strftime("%Y-%m-%d")

    return df[
        df["Tanggal"] == hari_ini
    ].reset_index(drop=True)


# ==========================================================
# RIWAYAT BERDASARKAN MEKANIK
# ==========================================================

def riwayat_mekanik(
    nama_mekanik
):
    """
    Mengambil riwayat hari ini berdasarkan mekanik.
    """

    df = baca_hari_ini()

    if df.empty:

        return df

    return df[
        df["Mekanik"] == nama_mekanik
    ].reset_index(drop=True)


# ==========================================================
# MENCARI BERDASARKAN NOMOR ANTREAN
# ==========================================================

def cari_antrean(
    nomor_antrean
):
    """
    Mencari data berdasarkan nomor antrean.
    """

    df = baca_excel()

    if df.empty:

        return None

    hasil = df[
        df["Nomor Antrean"] == nomor_antrean
    ]

    if hasil.empty:

        return None

    return hasil.iloc[0].to_dict()


# ==========================================================
# ANTREAN HARI INI
# ==========================================================

def daftar_antrean_hari_ini():
    """
    Mengembalikan seluruh antrean hari ini.
    """

    df = baca_hari_ini()

    if df.empty:

        return df

    return df.sort_values(
        by="Nomor Antrean"
    ).reset_index(drop=True)

# ==========================================================
# UPDATE STATUS LAYANAN
# ==========================================================

def update_status(
    nomor_antrean,
    status_baru
):
    """
    Mengubah status layanan berdasarkan nomor antrean.
    """

    df = baca_excel()

    if df.empty:
        return False

    index = df[
        df["Nomor Antrean"] == nomor_antrean
    ].index

    if len(index) == 0:
        return False

    df.loc[
        index,
        "Status"
    ] = status_baru

    simpan_excel(df)

    return True


# ==========================================================
# UPDATE MEKANIK
# ==========================================================

def update_mekanik(
    nomor_antrean,
    mekanik_baru
):
    """
    Mengubah mekanik yang menangani layanan.
    """

    df = baca_excel()

    if df.empty:
        return False

    index = df[
        df["Nomor Antrean"] == nomor_antrean
    ].index

    if len(index) == 0:
        return False

    df.loc[
        index,
        "Mekanik"
    ] = mekanik_baru

    simpan_excel(df)

    return True


# ==========================================================
# UPDATE JAM MULAI
# ==========================================================

def update_jam_mulai(
    nomor_antrean,
    jam_mulai
):
    """
    Mengubah jam mulai layanan.
    """

    df = baca_excel()

    if df.empty:
        return False

    index = df[
        df["Nomor Antrean"] == nomor_antrean
    ].index

    if len(index) == 0:
        return False

    df.loc[
        index,
        "Jam Mulai"
    ] = jam_mulai

    simpan_excel(df)

    return True


# ==========================================================
# UPDATE JAM SELESAI
# ==========================================================

def update_jam_selesai(
    nomor_antrean,
    jam_selesai
):
    """
    Mengubah jam selesai layanan.
    """

    df = baca_excel()

    if df.empty:
        return False

    index = df[
        df["Nomor Antrean"] == nomor_antrean
    ].index

    if len(index) == 0:
        return False

    df.loc[
        index,
        "Jam Selesai"
    ] = jam_selesai

    simpan_excel(df)

    return True


# ==========================================================
# UPDATE ESTIMASI
# ==========================================================

def update_estimasi(
    nomor_antrean,
    estimasi
):
    """
    Mengubah estimasi waktu servis.
    """

    df = baca_excel()

    if df.empty:
        return False

    index = df[
        df["Nomor Antrean"] == nomor_antrean
    ].index

    if len(index) == 0:
        return False

    df.loc[
        index,
        "Estimasi"
    ] = estimasi

    simpan_excel(df)

    return True


# ==========================================================
# HAPUS DATA
# ==========================================================

def hapus_layanan(
    nomor_antrean
):
    """
    Menghapus layanan berdasarkan nomor antrean.
    """

    df = baca_excel()

    if df.empty:
        return False

    df = df[
        df["Nomor Antrean"] != nomor_antrean
    ]

    simpan_excel(
        df.reset_index(drop=True)
    )

    return True

# ==========================================================
# STATISTIK HARI INI
# ==========================================================

def statistik_hari_ini():
    """
    Menghasilkan statistik layanan hari ini.
    """

    df = baca_hari_ini()

    if df.empty:

        return {

            "total": 0,

            "ringan": 0,

            "berat": 0,

            "menunggu": 0,

            "diproses": 0,

            "selesai": 0

        }

    return {

        "total": len(df),

        "ringan": len(
            df[df["Kategori"] == "Ringan"]
        ),

        "berat": len(
            df[df["Kategori"] == "Berat"]
        ),

        "menunggu": len(
            df[df["Status"] == "Menunggu"]
        ),

        "diproses": len(
            df[df["Status"] == "Diproses"]
        ),

        "selesai": len(
            df[df["Status"] == "Selesai"]
        )

    }


# ==========================================================
# STATUS MASING-MASING MEKANIK
# ==========================================================

def status_mekanik():
    """
    Menampilkan status seluruh mekanik.
    """

    from utils.scheduler import MEKANIK

    df = baca_hari_ini()

    hasil = []

    for mekanik in MEKANIK:

        nama = mekanik["nama"]

        data = df[
            (df["Mekanik"] == nama)
            &
            (df["Status"] != "Selesai")
        ]

        if data.empty:

            hasil.append({

                "Mekanik": nama,

                "Status": "Tersedia"

            })

        else:

            hasil.append({

                "Mekanik": nama,

                "Status": "Sedang Servis"

            })

    return pd.DataFrame(hasil)


# ==========================================================
# ANTREAN YANG MASIH BERJALAN
# ==========================================================

def antrean_aktif():
    """
    Menampilkan antrean yang belum selesai.
    """

    df = baca_hari_ini()

    if df.empty:

        return df

    return df[
        df["Status"] != "Selesai"
    ].reset_index(drop=True)


# ==========================================================
# RIWAYAT BERDASARKAN TANGGAL
# ==========================================================

def riwayat_tanggal(tanggal):
    """
    Mengambil riwayat berdasarkan tanggal.
    Format:
    YYYY-MM-DD
    """

    df = baca_excel()

    if df.empty:

        return df

    df["Tanggal"] = pd.to_datetime(
        df["Tanggal"]
    ).dt.strftime("%Y-%m-%d")

    return df[
        df["Tanggal"] == tanggal
    ].reset_index(drop=True)


# ==========================================================
# EXPORT EXCEL
# ==========================================================

def export_excel(path_export):
    """
    Mengekspor seluruh data ke lokasi baru.
    """

    df = baca_excel()

    df.to_excel(

        path_export,

        index=False,

        sheet_name=SHEET_NAME

    )

    return path_export


# ==========================================================
# RESET DATA HARI INI
# ==========================================================

def reset_hari_ini():
    """
    Menghapus seluruh data layanan hari ini.
    """

    df = baca_excel()

    if df.empty:

        return

    hari_ini = datetime.now().strftime("%Y-%m-%d")

    df["Tanggal"] = pd.to_datetime(
        df["Tanggal"]
    ).dt.strftime("%Y-%m-%d")

    df = df[
        df["Tanggal"] != hari_ini
    ]

    simpan_excel(
        df.reset_index(drop=True)
    )
