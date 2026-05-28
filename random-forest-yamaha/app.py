with col3:
    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            Tanggal & Jam WIB
        </div>

        <div style="
            color:white;
            font-size:20px;
            font-weight:700;
            margin-bottom:8px;
        ">
            {tanggal}
        </div>

        <div style="
            color:#ef4444;
            font-size:34px;
            font-weight:900;
            letter-spacing:2px;
        ">
            {jam}
        </div>

    </div>
    """, unsafe_allow_html=True)
