# =========================================
# utils/training.py
# =========================================

import pandas as pd
import joblib

from pathlib import Path

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
    # PASTIKAN NUMERIK
    # =====================================

    X = X.apply(
        pd.to_numeric,
        errors="coerce"
    )

    X = X.fillna(0)

    # =====================================
    # TRAIN TEST SPLIT
    # =====================================

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=0.20,

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

        class_weight="balanced",

        random_state=42,

        n_jobs=-1

    )

    # =====================================
    # TRAINING
    # =====================================

    rf.fit(
        X_train,
        y_train
    )

    # =====================================
    # SIMPAN MODEL
    # =====================================

    BASE_DIR = Path(__file__).resolve().parent.parent

    MODEL_DIR = BASE_DIR / "model"

    MODEL_DIR.mkdir(

        parents=True,

        exist_ok=True

    )

    # Simpan Model

    joblib.dump(

        rf,

        MODEL_DIR / "random_forest_model.pkl"

    )

    # Simpan Urutan Fitur

    joblib.dump(

        X.columns.tolist(),

        MODEL_DIR / "feature_columns.pkl"

    )

    # =====================================
    # PREDIKSI
    # =====================================

    y_pred = rf.predict(
        X_test
    )

    # =====================================
    # EVALUASI
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

    importance = pd.DataFrame({

        "Fitur": X.columns,
        "Importance": rf.feature_importances_

    })

    # =====================================
    # KELOMPOK FEATURE IMPORTANCE
    # =====================================

    grouped_importance = {

        "Indikasi": 0.0,
        "Km": 0.0,
        "Usia Motor": 0.0,
        "Jenis": 0.0,
        "Brand": 0.0

    }

    for _, row in importance.iterrows():

        fitur = row["Fitur"]
        nilai = float(row["Importance"])

        # =================================
        # FITUR NUMERIK
        # =================================

        if fitur == "Km":

            grouped_importance["Km"] += nilai

        elif fitur == "Usia Motor":

            grouped_importance["Usia Motor"] += nilai

        # =================================
        # FITUR KATEGORI
        # =================================

        elif fitur.startswith("Brand_"):

            grouped_importance["Brand"] += nilai

        elif fitur.startswith("Jenis_"):

            grouped_importance["Jenis"] += nilai

        elif fitur.startswith("Indikasi_"):

            grouped_importance["Indikasi"] += nilai

    # =====================================
    # DATAFRAME FEATURE IMPORTANCE
    # =====================================

    importance_grouped = pd.DataFrame({

        "Fitur": list(grouped_importance.keys()),
        "Importance": list(grouped_importance.values())

    })

    importance_grouped = importance_grouped.sort_values(

        by="Importance",

        ascending=False

    )

    importance_grouped = importance_grouped.reset_index(

        drop=True

    )
    
