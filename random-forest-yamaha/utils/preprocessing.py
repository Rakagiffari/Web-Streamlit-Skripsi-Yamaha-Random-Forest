# =========================================
# utils/preprocessing.py
# =========================================

import pandas as pd

def preprocess_data(df):

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

    tahun_sekarang = 2026

    df["Usia Motor"] = (
        tahun_sekarang - df["Tahun Motor"]
    )

    # =====================================
    # TARGET
    # =====================================

    y = df["Service"].map({

        "Ringan": 0,
        "Berat": 1

    })

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

    # TIDAK PENTING
    "Dealer",
    "Point",
    "YSS",
    "Order",
    "No Work Order",

    # TANGGAL
    "Reg Date",

    # SUDAH DIGANTI
    "Tahun Motor"
]
    
    X = df.drop(
        columns=drop_columns,
        errors='ignore'
    )

    # =====================================
    # ONE HOT ENCODING
    # =====================================

    X = pd.get_dummies(
        X,
        drop_first=True
    )

    return X, y
