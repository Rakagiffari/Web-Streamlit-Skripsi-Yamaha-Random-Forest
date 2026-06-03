from sklearn.model_selection import (
    train_test_split
)

from sklearn.ensemble import (
    RandomForestClassifier
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


def train_model(X, y):

    # ========================================
    # SPLIT DATA
    # ========================================
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # ========================================
    # MODEL
    # ========================================
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    # ========================================
    # TRAINING
    # ========================================
    model.fit(
        X_train,
        y_train
    )

    # ========================================
    # PREDIKSI
    # ========================================
    y_pred = model.predict(
        X_test
    )

    # ========================================
    # EVALUASI
    # ========================================
    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    precision = precision_score(
        y_test,
        y_pred,
        average="weighted",
        zero_division=0
    )

    recall = recall_score(
        y_test,
        y_pred,
        average="weighted",
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        y_pred,
        average="weighted",
        zero_division=0
    )

    report = classification_report(
        y_test,
        y_pred
    )

    matrix = confusion_matrix(
        y_test,
        y_pred
    )

    # ========================================
    # RETURN
    # ========================================
    return (
        model,
        accuracy,
        precision,
        recall,
        f1,
        report,
        matrix
    )
