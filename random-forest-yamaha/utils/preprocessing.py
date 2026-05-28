import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):

    # Hapus data duplikat
    df = df.drop_duplicates()

    # Isi missing value kategori
    categorical_cols = df.select_dtypes(include='object').columns

    for col in categorical_cols:
        df[col] = df[col].fillna('Unknown')

    # Kolom numerik
    numeric_cols = [
        'Tahun Motor',
        'Last Kilometer',
        'Harga'
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
    df['Usia Motor'] = 2026 - df['Tahun Motor']

    # Target
    y = df['Service']

    # Kolom yang tidak dipakai
    drop_columns = [
        'Service',
        'Nama',
        'Telepon',
        'KTP',
        'Invoice'
    ]

    X = df.drop(
        columns=drop_columns,
        errors='ignore'
    )

    # Encoding fitur kategori
    label_encoders = {}

    for col in X.select_dtypes(include='object').columns:

        le = LabelEncoder()

        X[col] = le.fit_transform(
            X[col].astype(str)
        )

        label_encoders[col] = le

    # Encoding target
    target_encoder = LabelEncoder()

    y = target_encoder.fit_transform(y)

    return X, y, label_encoders, target_encoder
