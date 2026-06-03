# =========================================
# utils/preprocessing.py
# =========================================

import pandas as pd

def preprocess_data(df):

    # =====================================================
    # HAPUS DUPLIKAT
    # =====================================================

    df = df.drop_duplicates()

    # =====================================================
    # HANDLE MISSING VALUE
    # =====================================================

    # =========================
    # KOLOM KATEGORIKAL
    # =========================

    df["Category"] = df["Category"].fillna(
        "Unknown"
    )

    df["Brand"] = df["Brand"].fillna(
        "Unknown"
    )

    df["Model Name"] = df["Model Name"].fillna(
        "Unknown"
    )

    df["Status"] = df["Status"].fillna(
        "Unknown"
    )

    # =========================
    # KOLOM NUMERIK
    # =========================

    df["Tahun Motor"] = pd.to_numeric(
        df["Tahun Motor"],
        errors='coerce'
    )

    df["Last Kilometer"] = pd.to_numeric(
        df["Last Kilometer"],
        errors='coerce'
    )

    df["Tahun Motor"] = df["Tahun Motor"].fillna(
        df["Tahun Motor"].median()
    )

    df["Last Kilometer"] = df["Last Kilometer"].fillna(
        df["Last Kilometer"].median()
    )

    # =====================================================
    # FEATURE ENGINEERING
    # =====================================================

    tahun_sekarang = 2025

    df["Usia Motor"] = (
        tahun_sekarang - df["Tahun Motor"]
    )

    # =====================================================
    # TARGET
    # =====================================================

    target = "Service"

    y = df[target].map({

        "Ringan": 0,
        "Berat": 1

    })

    # =====================================================
    # DROP COLUMN
    # =====================================================

    drop_columns = [

        # TARGET
        "Service",

        # IDENTITAS
        "Nama",
        "KTP",
        "Telepon",
        "Invoice",
        "Plate",
        "Technical Name",

        # KOLOM TIDAK PENTING
        "Dealer",
        "Point",
        "YSS",
        "Order",
        "No Work Order",

        # TANGGAL
        "Reg Date",

        # LEAKAGE
        "Parts Name",
        "Total Payment",

        # SUDAH DIGANTI
        "Tahun Motor"
    ]

    X = df.drop(
        columns=drop_columns,
        errors='ignore'
    )

    # =====================================================
    # ONE HOT ENCODING
    # =====================================================

    X = pd.get_dummies(
        X,
        drop_first=True
    )

    # =====================================================
    # PASTIKAN NUMERIK
    # =====================================================

    X = X.astype(float)

    return X, y
