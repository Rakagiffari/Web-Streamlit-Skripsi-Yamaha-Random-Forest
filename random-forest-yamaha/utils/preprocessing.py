import pandas as pd

def preprocess_data(df):

    # =========================
    # HAPUS DUPLIKAT
    # =========================
    df = df.drop_duplicates()

    # =========================
    # HANDLE MISSING VALUE
    # =========================
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

    # =========================
    # FEATURE ENGINEERING
    # =========================
    df["Usia Motor"] = (
        2026 - df["Tahun Motor"]
    )

    # =========================
    # TARGET
    # =========================
    y = df["Service"].map({

        "Ringan": 0,
        "Berat": 1

    })

    # =========================
    # DROP KOLOM
    # =========================
    drop_columns = [

        "Service",

        "Nama",
        "KTP",
        "Telepon",
        "Invoice",

        "Parts Name",
        "Parts Qty",
        "Total Payment"
    ]

    X = df.drop(
        columns=drop_columns,
        errors='ignore'
    )

    # =========================
    # ONE HOT ENCODING
    # =========================
    X = pd.get_dummies(
        X,
        drop_first=True
    )

    return X, y
