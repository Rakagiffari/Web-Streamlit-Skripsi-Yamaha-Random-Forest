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

            df[col] = df[col].fillna("Unknown")

    # =====================================
    # HANDLE NUMERIC
    # =====================================

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

    tahun_sekarang = 2025

    df["Usia Motor"] = (
        tahun_sekarang - df["Tahun Motor"]
    )

    # =====================================
    # TARGET
    # =====================================

    target = "Service"

    y = df[target].map({

        "Ringan": 0,
        "Berat": 1

    })

    # =====================================
    # DROP COLUMNS
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

    # =====================================
    # ONE HOT ENCODING
    # =====================================

    X = pd.get_dummies(

        X,
        drop_first=True

    )

    # =====================================
    # PASTIKAN BOOLEAN JADI INTEGER
    # =====================================

    bool_cols = X.select_dtypes(include=['bool']).columns

    for col in bool_cols:

        X[col] = X[col].astype(int)

    return X, y
