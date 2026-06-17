# =========================================
# utils/preprocessing.py
# =========================================

import pandas as pd


def preprocess_data(df):

    # =========================================
    # HAPUS DUPLIKAT
    # =========================================

    df = df.drop_duplicates()

    # =========================================
    # HANDLE MISSING VALUE
    # =========================================

    # -------------------------
    # KATEGORIKAL
    # -------------------------

    if "Brand" in df.columns:
        df["Brand"] = df["Brand"].fillna("Unknown")

    if "Jenis" in df.columns:
        df["Jenis"] = df["Jenis"].fillna("Unknown")

    if "Indikasi" in df.columns:
        df["Indikasi"] = df["Indikasi"].fillna("Unknown")

    # -------------------------
    # NUMERIK
    # -------------------------

    df["Kilometer"] = pd.to_numeric(
        df["Kilometer"],
        errors="coerce"
    )

    df["Usia Motor"] = pd.to_numeric(
        df["Usia Motor"],
        errors="coerce"
    )

    df["Qty"] = pd.to_numeric(
        df["Qty"],
        errors="coerce"
    )

    df["Kilometer"] = df["Kilometer"].fillna(
        df["Kilometer"].median()
    )

    df["Usia Motor"] = df["Usia Motor"].fillna(
        df["Usia Motor"].median()
    )

    df["Qty"] = df["Qty"].fillna(
        df["Qty"].median()
    )

    # =========================================
    # TARGET
    # =========================================

    if "Service" not in df.columns:
        raise ValueError(
            "Kolom 'Service' tidak ditemukan."
        )

    y = df["Service"].map({

        "Ringan": 0,
        "Berat": 1

    })

    # =========================================
    # FITUR FINAL SKRIPSI
    # =========================================

    fitur = [

        "Brand",
        "Jenis",
        "Kilometer",
        "Usia Motor",
        "Indikasi",
        "Qty"

    ]

    # cek kolom wajib

    kolom_tidak_ada = [

        col for col in fitur
        if col not in df.columns

    ]

    if len(kolom_tidak_ada) > 0:

        raise ValueError(
            f"Kolom tidak ditemukan: {kolom_tidak_ada}"
        )

    X = df[fitur].copy()

    # =========================================
    # ONE HOT ENCODING
    # =========================================

    X = pd.get_dummies(

        X,

        columns=[

            "Brand",
            "Jenis",
            "Indikasi"

        ],

        drop_first=False

    )

    # =========================================
    # PASTIKAN NUMERIK
    # =========================================

    X = X.astype(float)

    # =========================================
    # RETURN
    # =========================================

    return X, y
