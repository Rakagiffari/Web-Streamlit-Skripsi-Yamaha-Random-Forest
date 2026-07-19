from pathlib import Path
import streamlit as st

from utils.report import generate_pdf


def tampilkan_download_pdf(
    base_dir,
    df,
    train_size,
    test_size,
    accuracy,
    precision,
    recall,
    f1,
    importance_grouped,
    cm_path,
    fi_path,
):
    """
    Membuat PDF kemudian menampilkan tombol download.
    """

    logo_path = base_dir / "assets" / "yamaha_logo.png"

    pdf_path = generate_pdf(

        pdf_path=base_dir / "laporan_training_model.pdf",

        logo_path=logo_path,

        total_data=len(df),

        train_data=train_size,

        test_data=test_size,

        accuracy=accuracy,

        precision=precision,

        recall=recall,

        f1=f1,

        cm_image=cm_path,

        fi_image=fi_path,

        top_features=importance_grouped["Fitur"]
        .head(5)
        .tolist()

    )

    st.success("✅ Laporan PDF berhasil dibuat.")

    st.markdown("<br>", unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:

        with open(pdf_path, "rb") as pdf:

            st.download_button(

                label="📄 Download Laporan PDF",

                data=pdf.read(),

                file_name="Laporan_Training_Model.pdf",

                mime="application/pdf",

                use_container_width=True,

                key="download_pdf"

            )

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#9ca3af;
            font-size:14px;
            margin-top:-8px;
            margin-bottom:15px;
        ">
            Tekan tombol di atas untuk mengunduh laporan hasil pelatihan model dalam format PDF.
        </div>
        """,
        unsafe_allow_html=True
    )

    return pdf_path
