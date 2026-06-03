# =========================================
# utils/training.py
# =========================================

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

import pandas as pd

def train_model(X, y):

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
        y_pred
    )

    recall = recall_score(
        y_test,
        y_pred
    )

    f1 = f1_score(
        y_test,
        y_pred
    )

    report = classification_report(
        y_test,
        y_pred
    )

    matrix = confusion_matrix(
        y_test,
        y_pred
    )

    # =====================================
    # FEATURE IMPORTANCE
    # =====================================

    importance = pd.DataFrame({

        'Fitur': X.columns,
        'Importance': rf.feature_importances_

    })

    grouped_importance = {

        'Last Kilometer': 0,
        'Usia Motor': 0,
        'Model Name': 0,
        'Category': 0,
        'Brand': 0,
        'Status': 0

    }

    for index, row in importance.iterrows():

        fitur = row['Fitur']
        nilai = row['Importance']

        if fitur.startswith('Model Name_'):

            grouped_importance['Model Name'] += nilai

        elif fitur.startswith('Category_'):

            grouped_importance['Category'] += nilai

        elif fitur.startswith('Brand_'):

            grouped_importance['Brand'] += nilai

        elif fitur.startswith('Status_'):

            grouped_importance['Status'] += nilai

        elif fitur == 'Last Kilometer':

            grouped_importance['Last Kilometer'] += nilai

        elif fitur == 'Usia Motor':

            grouped_importance['Usia Motor'] += nilai

    importance_df = pd.DataFrame({

        'Fitur': grouped_importance.keys(),
        'Importance': grouped_importance.values()

    })

    importance_df = importance_df.sort_values(

        by='Importance',
        ascending=False

    )

    # =====================================
    # RETURN
    # =====================================

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
