# =========================================
# utils/preprocessing.py
# =========================================

import pandas as pd
from datetime import datetime


# =========================================
# PEMBENTUKAN JENIS MOTOR
# =========================================

def get_jenis(model):

    model = str(model).upper()

    # MAXI
    if any(x in model for x in [
        "XMAX",
        "NMAX",
        "AEROX",
        "LEXI",
        "TMAX"
    ]):
        return "MAXi"

    # CLASSY
    elif any(x in model for x in [
        "FAZZIO",
        "FILANO"
    ]):
        return "Classy"

    # MATIC
    elif any(x in model for x in [
        "MIO",
        "SOUL",
        "XEON",
        "FINO",
        "GEAR",
        "FREEGO",
        "X-RIDE",
        "XRIDE",
        "NOUVO",
        "LEXAM"
    ]):
        return "Matic"

    # SPORT
    elif any(x in model for x in [
        "R15",
        "R25",
        "R6",
        "R1",
        "VIXION",
        "BYSON",
        "SCORPIO",
        "RX",
        "XSR",
        "MT"
    ]):
        return "Sport"

    # OFFROAD
    elif any(x in model for x in [
        "WR",
        "YZ"
    ]):
        return "Off-road"

    # MOPED
    elif any(x in model for x in [
        "JUPITER",
        "VEGA",
        "CRYPTON",
        "ALFA",
        "SIGMA",
        "F1ZR",
        "MX KING"
    ]):
        return "Moped"

    return "Unknown"


# =========================================
# PREPROCESSING
# =========================================

def preprocess_data(df):

    # =====================================
    # HAPUS DUPLIKAT
    # =====================================

    df = df.drop_duplicates()

    # =====================================
    # VALIDASI KOLOM
    # =====================================

    required_columns = [
        
        "Model",
        "Tahun",
        "Km",
        "Indikasi",
        "Service"

    ]

    missing_columns = [

        col for col in required_columns
        if col not in df.columns

    ]

    if missing_columns:

        raise ValueError(
            f"Kolom tidak ditemukan: {missing_columns}"
        )

    # =====================================
    # HANDLE MISSING VALUE
    # =====================================

    df["Brand"] = df["Brand"].fillna(
        "Unknown"
    )

    df["Model"] = df["Model"].fillna(
        "Unknown"
    )

    df["Indikasi"] = df["Indikasi"].fillna(
        "Unknown"
    )

    # =====================================
    # NUMERIK
    # =====================================

    df["Tahun"] = pd.to_numeric(
        df["Tahun"],
        errors="coerce"
    )

    df["Km"] = pd.to_numeric(
        df["Km"],
        errors="coerce"
    )

    df["Tahun"] = df["Tahun"].fillna(
        df["Tahun"].median()
    )

    df["Km"] = df["Km"].fillna(
        df["Km"].median()
    )

    # =====================================
    # FEATURE ENGINEERING
    # =====================================

    tahun_sekarang = datetime.now().year

    df["Usia Motor"] = (
        tahun_sekarang - df["Tahun"]
    )

    df["Jenis"] = df["Model"].apply(
        get_jenis
    )

    # =====================================
    # TARGET
    # =====================================

    y = df["Service"].map({

        "Ringan": 0,
        "Berat": 1

    })

    if y.isnull().sum() > 0:

        raise ValueError(
            "Kolom Service harus berisi Ringan atau Berat"
        )

    # =====================================
    # FITUR FINAL
    # =====================================

    X = df[

        [
            "Jenis",
            "Km",
            "Usia Motor",
            "Indikasi"
        ]

    ].copy()

    # =====================================
    # ONE HOT ENCODING
    # =====================================

    X = pd.get_dummies(

        X,

        columns=[
            "Jenis",
            "Indikasi"
        ],

        drop_first=False

    )

    # =====================================
    # PASTIKAN NUMERIK
    # =====================================

    X = X.astype(float)

    return X, y
