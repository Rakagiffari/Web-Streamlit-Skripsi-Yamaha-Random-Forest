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

    # Split data training dan testing
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Model Random Forest
    model = RandomForestClassifier(
        n_estimators=150,
        max_depth=10,
        random_state=42
    )

    # Training model
    model.fit(X_train, y_train)

    # Prediksi
    y_pred = model.predict(X_test)

    # Evaluasi model
    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(
        y_test,
        y_pred,
        average='weighted'
    )

    recall = recall_score(
        y_test,
        y_pred,
        average='weighted'
    )

    f1 = f1_score(
        y_test,
        y_pred,
        average='weighted'
    )

    # Classification report
    report = classification_report(
        y_test,
        y_pred
    )

    # Confusion matrix
    matrix = confusion_matrix(
        y_test,
        y_pred
    )

    return (
        model,
        accuracy,
        precision,
        recall,
        f1,
        report,
        matrix
    )
