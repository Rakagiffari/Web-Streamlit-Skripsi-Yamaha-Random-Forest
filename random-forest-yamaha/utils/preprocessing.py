# =========================================
# utils/preprocessing.py
# =========================================

import pandas as pd

def preprocess_data(df):

    # =====================================
    # COPY DATA
    # =====================================

    df = df.copy()

    # =====================================
    # HAPUS DUPLIKAT
    # =====================================

    df = df.drop_duplicates()

    # =====================================
    # HANDLE MISSING VALUE
    # =====================================

    categorical_cols = [
        "Category",
        "Brand",
        "Model Name",
        "Status"
    ]

    for col in categorical_cols:

        if col in df.columns:

            df[col] = df[col].fillna(
                "Unknown"
            )

    numeric_cols = [
        "Tahun Motor",
        "Last Kilometer"
    ]

    for col in numeric_cols:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors='coerce'
            )

            df[col] = df[col].fillna(
                df[col].median()
            )

    # =====================================
    # FEATURE ENGINEERING
    # =====================================

    if "Tahun Motor" in df.columns:

        tahun_sekarang = 2026

        df["Usia Motor"] = (
            tahun_sekarang - df["Tahun Motor"]
        )

    # =====================================
    # TARGET
    # =====================================

    if "Service" not in df.columns:

        raise ValueError(
            "Kolom 'Service' tidak ditemukan"
        )

    y = df["Service"].map({

        "Ringan": 0,
        "Berat": 1

    })

    # =====================================
    # HAPUS TARGET NULL
    # =====================================

    valid_index = y.notna()

    df = df.loc[valid_index]

    y = y.loc[valid_index]

    # =====================================
    # DROP COLUMN
    # =====================================

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

        # DATA LEAKAGE
        "Parts Name",
        "Parts Qty",
        "Total Payment",

        # SUDAH DIGANTI
        "Tahun Motor"
    ]

    X = df.drop(
        columns=drop_columns,
        errors='ignore'
    )

    # =====================================
    # KONVERSI OBJECT YANG TERSISA
    # =====================================

    object_cols = X.select_dtypes(
        include=['object']
    ).columns

    for col in object_cols:

        X[col] = X[col].astype(str)

    # =====================================
    # ONE HOT ENCODING
    # =====================================

    X = pd.get_dummies(
        X,
        drop_first=True
    )

    # =====================================
    # PASTIKAN SEMUA NUMERIK
    # =====================================

    X = X.astype(float)

    return X, y
