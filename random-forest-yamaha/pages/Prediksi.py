import streamlit as st

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="Prediksi Layanan",
    page_icon="🔍",
    layout="wide"
)

# =========================================
# STYLE
# =========================================

st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:700;
    color:white;
    margin-bottom:0px;
}

.sub-title{
    color:#9ca3af;
    font-size:14px;
    margin-top:-10px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown(
    '<p class="main-title">🔍 Prediksi Layanan Service</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Masukkan informasi kendaraan untuk melakukan prediksi layanan service menggunakan Random Forest.</p>',
    unsafe_allow_html=True
)

st.markdown("---")
