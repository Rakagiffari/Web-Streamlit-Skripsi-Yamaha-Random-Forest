import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

from utils.preprocessing import preprocess_data

st.title("📈 Feature Importance")

uploaded_file = st.file_uploader(
    'Upload Dataset CSV',
    type=['csv']
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    X, y, label_encoders, target_encoder = preprocess_data(df)

    model = joblib.load('model/random_forest_model.pkl')

    importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': model.feature_importances_
    })

    importance = importance.sort_values(
        by='Importance',
        ascending=False
    )

    fig = px.bar(
        importance,
        x='Importance',
        y='Feature',
        orientation='h',
        title='Feature Importance'
    )

    st.plotly_chart(fig, use_container_width=True)
