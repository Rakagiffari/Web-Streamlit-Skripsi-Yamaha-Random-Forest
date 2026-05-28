# =========================================
# REALTIME DATE & TIME
# =========================================
clock_placeholder = st.empty()

while True:

    now = datetime.now()

    hari_indonesia = {
        "Monday": "Senin",
        "Tuesday": "Selasa",
        "Wednesday": "Rabu",
        "Thursday": "Kamis",
        "Friday": "Jumat",
        "Saturday": "Sabtu",
        "Sunday": "Minggu"
    }

    hari = hari_indonesia[now.strftime("%A")]

    tanggal = now.strftime("%d-%m-%Y")

    jam = now.strftime("%H:%M:%S")

    with clock_placeholder.container():

        col1, col2, col3, col4 = st.columns(4)

        # =========================================
        # CARD 1
        # =========================================
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">
                    Algoritma
                </div>

                <div class="metric-value">
                    Random Forest
                </div>
            </div>
            """, unsafe_allow_html=True)

        # =========================================
        # CARD 2
        # =========================================
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">
                    Dataset
                </div>

                <div class="metric-value">
                    CSV File
                </div>
            </div>
            """, unsafe_allow_html=True)

        # =========================================
        # CARD 3
        # =========================================
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">
                    Tanggal & Jam
                </div>

                <div class="date-text">
                    {tanggal}
                </div>

                <div class="time-text">
                    {jam}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # =========================================
        # CARD 4
        # =========================================
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">
                    Hari
                </div>

                <div class="metric-value">
                    {hari}
                </div>
            </div>
            """, unsafe_allow_html=True)

    time.sleep(1)
