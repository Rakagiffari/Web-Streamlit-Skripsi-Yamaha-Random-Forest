```python
import pandas as pd

from sklearn.preprocessing import (
    LabelEncoder
)


def preprocess_data(df):

    # ========================================
    # HAPUS TARGET KOSONG
    # ========================================
    df = df.dropna(
        subset=["Service"]
    )

    # ========================================
    # ISI DATA KOSONG
    # ========================================
    if "Parts Name" in df.columns:

        df["Parts Name"] = df[
            "Parts Name"
        ].fillna("Tidak Ada Part")

    if "Last Kilometer" in df.columns:

        df["Last Kilometer"] = df[
            "Last Kilometer"
        ].fillna(0)

    if "Parts Qty" in df.columns:

        df["Parts Qty"] = df[
            "Parts Qty"
        ].fillna(0)

    if "Total Payment" in df.columns:

        df["Total Payment"] = df[
            "Total Payment"
        ].fillna(0)

    # ========================================
    # PILIH FITUR
    # ========================================
    selected_columns = [
        "Category",
        "Brand",
        "Model Name",
        "Tahun Motor",
        "Last Kilometer",
        "Parts Qty",
        "Total Payment",
        "Parts Name"
    ]

    available_columns = [
        col for col in selected_columns
        if col in df.columns
    ]

    # ========================================
    # DATA FINAL
    # ========================================
    df = df[
        available_columns + ["Service"]
    ]

    # ========================================
    # UBAH OBJECT JADI STRING
    # ========================================
    for col in df.columns:

        if df[col].dtype == "object":

            df[col] = df[col].astype(str)

    # ========================================
    # ENCODING
    # ========================================
    for col in available_columns:

        if df[col].dtype == "object":

            le = LabelEncoder()

            df[col] = le.fit_transform(
                df[col]
            )

    # ========================================
    # TARGET ENCODER
    # ========================================
    target_encoder = LabelEncoder()

    df["Service"] = target_encoder.fit_transform(
        df["Service"]
    )

    # ========================================
    # X DAN y
    # ========================================
    X = df.drop(
        "Service",
        axis=1
    )

    y = df["Service"]

    return X, y
```
