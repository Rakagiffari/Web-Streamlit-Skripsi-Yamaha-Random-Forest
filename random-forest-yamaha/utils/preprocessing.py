import pandas as pd

def preprocess_data(df):

    # Hapus duplikat
    df = df.drop_duplicates()

    # Missing value kategori
    categorical_cols = [
        "Category",
        "Brand",
        "Model Name",
        "Status"
    ]

    for col in categorical_cols:

        if col in df.columns:

            df[col] = df[col].fillna("Unknown")

    # Missing value numerik
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

    # Feature engineering
    tahun_sekarang = 2026

    df["Usia Motor"] = (
        tahun_sekarang - df["Tahun Motor"]
    )

    # Target
    y = df["Service"].map({
        "Ringan": 0,
        "Berat": 1
    })

    # Drop column
    drop_columns = [

        "Service",

        "Nama",
        "KTP",
        "Telepon",
        "Invoice",

        "Plate",
        "Technical Name",

        "Dealer",
        "Point",
        "YSS",
        "Order",
        "No Work Order",

        "Reg Date",

        "Parts Name",
        "Parts Qty",
        "Total Payment",

        "Tahun Motor"
    ]

    X = df.drop(
        columns=drop_columns,
        errors='ignore'
    )

    # One Hot Encoding
    X = pd.get_dummies(
        X,
        drop_first=True
    )

    return X, y
