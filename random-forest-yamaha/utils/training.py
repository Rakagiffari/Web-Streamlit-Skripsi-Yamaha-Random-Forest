# =========================================
# utils/training.py
# =========================================

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (

    accuracy_score,
    classification_report,
    confusion_matrix,

    precision_score,
    recall_score,
    f1_score
)

def train_model(X, y):

    # =====================================
    # VALIDASI DATA
    # =====================================

    if len(X) == 0:

        raise ValueError(
            "Dataset kosong"
        )

    if y.isnull().sum() > 0:

        raise ValueError(
            "Target masih memiliki nilai kosong"
        )

    # =====================================
    # PASTIKAN SEMUA FITUR NUMERIK
    # =====================================

    X = X.apply(
        pd.to_numeric,
        errors='coerce'
    )

    X = X.fillna(0)

    # =====================================
    # SPLIT DATA
    # =====================================

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=0.2,

        random_state=42,

        stratify=y
    )

    # =====================================
    # RANDOM FOREST
    # =====================================

    rf = RandomForestClassifier(

        n_estimators=300,

        max_depth=15,

        min_samples_split=5,

        min_samples_leaf=2,

        class_weight='balanced',

        random_state=42,

        n_jobs=-1
    )

    # =====================================
    # TRAINING
    # =====================================

    rf.fit(X_train, y_train)

    # =====================================
    # PREDIKSI
    # =====================================

    y_pred = rf.predict(X_test)

    # =====================================
    # METRIK
    # =====================================

    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    precision = precision_score(
        y_test,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        y_pred,
        zero_division=0
    )

    report = classification_report(
        y_test,
        y_pred,
        zero_division=0
    )

    matrix = confusion_matrix(
        y_test,
        y_pred
    )

    # =====================================
    # FEATURE IMPORTANCE
    # =====================================

    importance_df = pd.DataFrame({

        "Fitur": X.columns,
        "Importance": rf.feature_importances_

    })

    importance_df = importance_df.sort_values(

        by="Importance",
        ascending=False
    )

    return (

        rf,

        accuracy,
        precision,
        recall,
        f1,

        report,
        matrix,

        importance_df
    )
