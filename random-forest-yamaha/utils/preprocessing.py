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
        "Xmax 250", 
        "Xmax 300", 
        "Xmax 400", 
        "Nmax 155",
        "Aerox 125", 
        "Aerox 155",
        "Lexi 125", 
        "Lexi LX 155", 
        "Tmax 530", 
        "Tmax 560"
    ]):
        return "MAXi"

    # CLASSY
    elif any(x in model for x in [
        "Grand Filano 125", 
        "Fazzio 125"
    ]):
        return "Classy"

    # MATIC
    elif any(x in model for x in [
        "Mio Sporty",
        "Mio Smile", 
        "Mio J", 
        "Mio GT", 
        "Mio M3",
        "Mio Z", 
        "Mio S",
        "Soul GT 115", 
        "Soul GT 125", 
        "Xeon 125", 
        "Xeon RC", 
        "Xeon GT 125", 
        "Fino 115", 
        "Fino 125", 
        "Gear 125", 
        "Freego 125", 
        "X-Ride 115", 
        "X-Ride 125", 
        "Nouvo Generasi 1", 
        "Nouvo Elegance", 
        "Lexam"
    ]):
        return "Matic"

    # SPORT
    elif any(x in model for x in [
        "YZF-R15 V1", 
        "YZF-R15 V2", 
        "YZF-R15 V3", 
        "YZF-R15 V4", 
        "R15M", 
        "YZF-R25", 
        "YZF-R6", 
        "YZF-R1", 
        "Vixion Generasi 1", 
        "Vixion New NVL", 
        "Vixion Advance", 
        "Vixion R", 
        "Byson Generasi 1", 
        "Byson FI", 
        "Scorpio 225", 
        "Scorpio Z", 
        "Scorpio King", 
        "RX-King", 
        "RX-K", 
        "RX-S", 
        "RX-Z", 
        "XSR 155", 
        "MT-15", 
        "MT-25", 
        "MT-07", 
        "MT-09", 
        "MT-10"
    ]):
        return "Sport"

    # OFFROAD
    elif any(x in model for x in [
        "WR 155R", 
        "WR 250R", 
        "YZ 125", 
        "YZ 125X", 
        "YZ 250", 
        "YZ 250F", 
        "YZ 250X", 
        "YZ 450F"
    ]):
        return "Off-road"

    # MOPED
    elif any(x in model for x in [
        "Jupiter MX 135 Generasi 1", 
        "Jupiter MX 135 Generasi 2", 
        "MX King 150", 
        "Jupiter Z Generasi 3", 
        "Jupiter Z Generasi 1", 
        "Jupiter Z Generasi 2", 
        "Jupiter Z1", 
        "Vega R", 
        "Vega ZR", 
        "Vega RR", 
        "Vega Force", 
        "Crypton", 
        "Alfa", 
        "Sigma", 
        "F1ZR"
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
