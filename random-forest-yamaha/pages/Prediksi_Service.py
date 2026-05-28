import streamlit as st
import pandas as pd
import joblib

st.title("🔍 Prediksi Layanan Service")

try:

    # Load model
    model = joblib.load(
        'model/random_forest_model.pkl'
    )

    # =========================
    # INPUT USER
    # =========================
    col1, col2 = st.columns(2)

    with col1:

        usia_motor = st.number_input(
            'Usia Motor',
            min_value=0,
            max_value=30,
            value=5
        )

        kilometer = st.number_input(
            'Last Kilometer',
            min_value=0,
            value=20000
        )

    with col2:

        harga = st.number_input(
            'Harga Service',
            min_value=0,
            value=300000
        )

        tahun_motor = st.number_input(
            'Tahun Motor',
            min_value=2000,
            max_value=2026,
            value=2020
        )

    # =========================
    # PREDIKSI
    # =========================
    if st.button("🚀 Prediksi Service"):

        input_data = pd.DataFrame({
            'Usia Motor': [usia_motor],
            'Last Kilometer': [kilometer],
            'Harga': [harga],
            'Tahun Motor': [tahun_motor]
        })

        prediction = model.predict(input_data)

        probability = model.predict_proba(input_data)

        hasil = (
            'Service Berat'
            if prediction[0] == 1
            else 'Service Ringan'
        )

        st.success(
            f'Hasil Prediksi: {hasil}'
        )

        # =========================
        # PROBABILITAS
        # =========================
        st.subheader("📊 Probabilitas")

        st.write(
            f"Service Ringan: {probability[0][0]*100:.2f}%"
        )

        st.write(
            f"Service Berat: {probability[0][1]*100:.2f}%"
        )

except:

    st.warning(
        "Silakan training model terlebih dahulu."
    )
