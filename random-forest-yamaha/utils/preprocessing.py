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
    # HANDLE NUMERIK
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

    if "Tahun Motor" in df.columns:

        df["Usia Motor"] = (
            tahun_sekarang - df["Tahun Motor"]
        )

    # =====================================
    # SEDERHANAKAN MODEL NAME
    # =====================================

    if "Model Name" in df.columns:

        top_model = (

            df["Model Name"]
            .value_counts()
            .nlargest(5)
            .index

        )

        df["Model Name"] = df["Model Name"].apply(

            lambda x: x
            if x in top_model
            else "Lainnya"

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
    # BOOL -> INT
    # =====================================

    bool_cols = X.select_dtypes(
        include=['bool']
    ).columns

    for col in bool_cols:

        X[col] = X[col].astype(int)

    # =====================================
    # INFO FITUR
    # =====================================

    print("Jumlah fitur :", X.shape[1])

    print("\nDaftar fitur:")

    for col in X.columns:

        print(col)

    return X, y
