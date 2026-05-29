import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

from pathlib import Path
from utils.preprocessing import preprocess_data

st.title("📈 Feature Importance")

uploaded_file = st.file_uploader(
"📂 Upload Dataset",
type=['csv']
)

if uploaded_file:

```
# =========================
# LOAD DATASET
# =========================
df = pd.read_csv(uploaded_file)

X, y = preprocess_data(df)

# =========================
# LOAD MODEL
# =========================
BASE_DIR = Path(__file__).parent.parent

model_path = (
    BASE_DIR / "model" / "random_forest_model.pkl"
)

if not model_path.exists():

    st.warning(
        "Silakan training model terlebih dahulu."
    )

else:

    model = joblib.load(model_path)

    # =========================
    # FEATURE IMPORTANCE
    # =========================
    importance = pd.DataFrame({
        'Fitur': X.columns,
        'Importance': model.feature_importances_
    })

    # =========================
    # GABUNGKAN FEATURE
    # =========================
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

        # =========================
        # MODEL NAME
        # =========================
        if fitur.startswith('Model Name_'):

            grouped_importance[
                'Model Name'
            ] += nilai

        # =========================
        # CATEGORY
        # =========================
        elif fitur.startswith('Category_'):

            grouped_importance[
                'Category'
            ] += nilai

        # =========================
        # BRAND
        # =========================
        elif fitur.startswith('Brand_'):

            grouped_importance[
                'Brand'
            ] += nilai

        # =========================
        # STATUS
        # =========================
        elif fitur.startswith('Status_'):

            grouped_importance[
                'Status'
            ] += nilai

        # =========================
        # LAST KILOMETER
        # =========================
        elif fitur == 'Last Kilometer':

            grouped_importance[
                'Last Kilometer'
            ] += nilai

        # =========================
        # USIA MOTOR
        # =========================
        elif fitur == 'Usia Motor':

            grouped_importance[
                'Usia Motor'
            ] += nilai

    # =========================
    # DATAFRAME
    # =========================
    importance_grouped = pd.DataFrame({
        'Fitur': grouped_importance.keys(),
        'Importance': grouped_importance.values()
    })

    importance_grouped = (
        importance_grouped.sort_values(
            by='Importance',
            ascending=False
        )
    )

    # =========================
    # VISUALISASI
    # =========================
    fig = px.bar(
        importance_grouped,
        x='Importance',
        y='Fitur',
        orientation='h',
        title='Feature Importance',
        text_auto='.3f'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
```
