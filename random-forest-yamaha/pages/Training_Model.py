import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from utils.preprocessing import preprocess_data
from utils.training import train_model

st.title("🤖 Training Random Forest")

uploaded_file = st.file_uploader(
    "Upload Dataset CSV",
    type=['csv']
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    X, y, label_encoders, target_encoder = preprocess_data(df)

    model, accuracy, report, matrix = train_model(X, y)

    st.success("Training berhasil dilakukan")

    st.metric("Accuracy", f"{accuracy:.2%}")

    st.subheader("Classification Report")
    st.text(report)

    st.subheader("Confusion Matrix")

    fig, ax = plt.subplots(figsize=(5,4))

    sns.heatmap(
        matrix,
        annot=True,
        fmt='d',
        cmap='Reds',
        ax=ax
    )

    st.pyplot(fig)

    joblib.dump(model, 'model/random_forest_model.pkl')

    st.success("Model berhasil disimpan")
