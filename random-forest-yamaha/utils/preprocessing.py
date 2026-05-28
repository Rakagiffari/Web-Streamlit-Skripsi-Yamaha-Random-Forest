import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):

    df = df.copy()

    target_column = "Service"

    categorical_columns = df.select_dtypes(include=['object']).columns

    label_encoders = {}

    for col in categorical_columns:

        le = LabelEncoder()

        df[col] = le.fit_transform(df[col].astype(str))

        label_encoders[col] = le

    X = df.drop(target_column, axis=1)

    y = df[target_column]

    return X, y, label_encoders
