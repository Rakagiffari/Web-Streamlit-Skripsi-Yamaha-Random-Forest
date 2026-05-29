import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

from pathlib import Path

st.set_page_config(

    page_title="Feature Importance",

    layout="wide"
)

st.title("📈 Feature Importance")

uploaded_file = st.file_uploader(

    "📂 Upload Dataset",

    type=['csv']
)

if uploaded_file:

    # =========================
    # BASE DIRECTORY
    # =========================

    BASE_DIR = Path(__file__).parent.parent

    # =========================
    # MODEL PATH
    # =========================

    model_path = (
        BASE_DIR / "model" / "random_forest_model.pkl"
    )

    feature_path = (
        BASE_DIR / "model" / "feature_names.pkl"
    )

    # =========================
    # CEK FILE
    # =========================

    if not model_path.exists():

        st.warning(
            "Silakan training model terlebih dahulu."
        )

    elif not feature_path.exists():

        st.warning(
            "Feature names belum tersedia."
        )

    else:

        # =========================
        # LOAD MODEL
        # =========================

        model = joblib.load(model_path)

        feature_names = joblib.load(feature_path)

        # =========================
        # VALIDASI
        # =========================

        if len(feature_names) != len(model.feature_importances_):

            st.error(
                "Jumlah feature tidak sesuai dengan model."
            )

            st.stop()

        # =========================
        # FEATURE IMPORTANCE
        # =========================

        importance = pd.DataFrame({

            'Fitur': feature_names,

            'Importance':
            model.feature_importances_

        })

        # =========================
        # GROUP FEATURE
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

            'Fitur':
            grouped_importance.keys(),

            'Importance':
            grouped_importance.values()

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

        # =========================
        # TABLE
        # =========================

        st.dataframe(

            importance_grouped,

            use_container_width=True
        )
