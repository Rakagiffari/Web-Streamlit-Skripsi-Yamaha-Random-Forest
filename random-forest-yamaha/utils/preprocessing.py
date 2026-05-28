import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_data(df):

    df = df.drop_duplicates()

    categorical_cols = [
        'Category',
        'Brand',
        'Model Name',
        'Status'
    ]

    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].fillna('Unknown')

    numeric_cols = [
        'Tahun Motor',
        'Last Kilometer'
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col] = df[col].fillna(df[col].median())

    tahun_sekarang = 2026

    df['Usia Motor'] = (
        tahun_sekarang - df['Tahun Motor']
    )

    drop_columns = [
        'Service',
        'Nama',
        'KTP',
        'Telepon',
        'Invoice',
        'Plate',
        'Technical Name',
        'Dealer'
    ]

    X = df.drop(columns=drop_columns, errors='ignore')

    y = df['Service']

    label_encoders = {}

    for col in X.select_dtypes(include='object').columns:

        le = LabelEncoder()

        X[col] = le.fit_transform(X[col].astype(str))

        label_encoders[col] = le

    target_encoder = LabelEncoder()

    y = target_encoder.fit_transform(y)

    return X, y, label_encoders, target_encoder
