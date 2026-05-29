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

        max_depth=20,

        min_samples_split=2,

        min_samples_leaf=1,

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
    # EVALUASI
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

    return (

        rf,

        accuracy,
        precision,
        recall,
        f1,

        report,
        matrix
    )
