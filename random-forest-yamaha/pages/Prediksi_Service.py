import streamlit as st
import pandas as pd
import joblib

st.title("🔍 Prediksi Layanan Service")

try:

    model = joblib.load('model/random_forest_model.pkl')

    usia_motor = st.number_input(
        'Usia Motor',
        min_value=0,
        max_value=30,
        value=5
    )

    kilometer = st.number_input(
        'Last Kilometer',
        min_value=0,
        value=15000
    )

    harga = st.number_input(
        'Harga Service',
        min_value=0,
        value=300000
    )

    if st.button('Prediksi'):

        input_data = pd.DataFrame({
            'Usia Motor': [usia_motor],
            'Last Kilometer': [kilometer],
            'Harga': [harga]
        })

        prediction = model.predict(input_data)

        hasil = 'Service Berat' if prediction[0] == 1 else 'Service Ringan'

        st.success(f'Hasil Prediksi: {hasil}')

except:

    st.warning('Silakan lakukan training model terlebih dahulu.')
