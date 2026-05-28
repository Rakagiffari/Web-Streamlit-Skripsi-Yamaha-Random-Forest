import pandas as pd

def preprocess_data(df):

    # =========================
    # HAPUS DUPLIKAT
    # =========================
    df = df.drop_duplicates()

    # =========================
    # HANDLE MISSING VALUE
    # =========================
    df["Category"] = df["Category"].fillna("Unknown")

    df["Brand"] = df["Brand"].fillna("Unknown")

    df["Model Name"] = df["Model Name"].fillna("Unknown")

    df["Status"] = df["Status"].fillna("Unknown")

    # =========================
    # NUMERIK
    # =========================
    df["Tahun Motor"] = pd.to_numeric(
        df["Tahun Motor"],
        errors='coerce'
    )

    df["Last Kilometer"] = pd.to_numeric(
        df["Last Kilometer"],
        errors='coerce'
    )

    df["Tahun Motor"] = df[
        "Tahun Motor"
    ].fillna(
        df["Tahun Motor"].median()
    )

    df["Last Kilometer"] = df[
        "Last Kilometer"
    ].fillna(
        df["Last Kilometer"].median()
    )

    # =========================
    # FEATURE ENGINEERING
    # =========================
    tahun_sekarang = 2026

    df["Usia Motor"] = (
        tahun_sekarang - df["Tahun Motor"]
    )

    # =========================
    # DROP COLUMN
    # =========================
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

    # =========================
    # TARGET
    # =========================
    y = df["Service"].map({

        "Ringan": 0,
        "Berat": 1

    })

    # =========================
    # ONE HOT ENCODING
    # =========================
    X = pd.get_dummies(
        X,
        drop_first=True
    )

    return X, y
