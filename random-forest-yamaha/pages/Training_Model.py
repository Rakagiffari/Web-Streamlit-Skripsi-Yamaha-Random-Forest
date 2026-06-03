import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from pathlib import Path

from utils.preprocessing import preprocess_data
from utils.training import train_model

st.title("⚙️ Training Random Forest")

uploaded_file = st.file_uploader(
    "📂 Upload Dataset",
    type=['csv']
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    X, y = preprocess_data(df)

    if st.button("🚀 Training Model"):

        (
            model,
            accuracy,
            precision,
            recall,
            f1,
            report,
            matrix,
            feature_names
        ) = train_model(X, y)

        # =========================
        # SAVE MODEL
        # =========================

        BASE_DIR = Path(__file__).parent.parent

        model_dir = BASE_DIR / "model"

        model_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        model_path = (
            model_dir / "random_forest_model.pkl"
        )

        feature_path = (
            model_dir / "feature_columns.pkl"
        )

        joblib.dump(
            model,
            model_path
        )

        joblib.dump(
            list(feature_names),
            feature_path
        )

        st.success(
            "✅ Model berhasil disimpan"
        )

        # =========================
        # METRIK
        # =========================

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Accuracy",
                f"{accuracy:.2%}"
            )

        with col2:
            st.metric(
                "Precision",
                f"{precision:.2%}"
            )

        with col3:
            st.metric(
                "Recall",
                f"{recall:.2%}"
            )

        with col4:
            st.metric(
                "F1 Score",
                f"{f1:.2%}"
            )

        # =========================
        # REPORT
        # =========================

        st.subheader(
            "📋 Classification Report"
        )

        st.text(report)

        # =========================
        # CONFUSION MATRIX
        # =========================

        st.subheader(
            "📉 Confusion Matrix"
        )

        fig, ax = plt.subplots(figsize=(5, 4))

        sns.heatmap(
            matrix,
            annot=True,
            fmt='d',
            cmap='Reds',
            ax=ax
        )

        st.pyplot(fig)

        # =========================
        # FEATURE IMPORTANCE
        # =========================

        st.subheader(
            "📊 Feature Importance"
        )

        importance = pd.DataFrame({

            'Fitur': feature_names,
            'Importance': model.feature_importances_

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

        importance_grouped = pd.DataFrame({

            'Fitur': grouped_importance.keys(),
            'Importance': grouped_importance.values()

        })

        importance_grouped = importance_grouped.sort_values(

            by='Importance',
            ascending=False

        )

        fig2, ax2 = plt.subplots(figsize=(8,5))

        sns.barplot(

            data=importance_grouped,

            x='Importance',
            y='Fitur',

            palette='Reds',
            ax=ax2

        )

        st.pyplot(fig2)

        st.dataframe(
            importance_grouped,
            use_container_width=True
        )
