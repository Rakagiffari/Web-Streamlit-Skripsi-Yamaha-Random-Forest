from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

from datetime import datetime
import os


def generate_pdf(
    pdf_path,
    logo_path,
    total_data,
    train_data,
    test_data,
    accuracy,
    precision,
    recall,
    f1,
    cm_image,
    fi_image,
    top_features
):

    doc = SimpleDocTemplate(
        pdf_path,
        leftMargin=20,
        rightMargin=20,
        topMargin=20,
        bottomMargin=20
    )

    styles = getSampleStyleSheet()

    elements = []

    # =====================================
    # HEADER
    # =====================================

    try:

        logo = Image(
            logo_path,
            width=2.0 * cm,
            height=2.0 * cm
        )

        logo_table = Table([[logo]])

        logo_table.setStyle(
            TableStyle([
                ("ALIGN", (0, 0), (-1, -1), "CENTER")
            ])
        )

        elements.append(logo_table)

    except Exception as e:

        print("ERROR LOGO:", e)

    elements.append(
        Paragraph(
            "<para align='center'><b>PT YAMAHA TJAHAJA BARU TABING</b></para>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            "<para align='center'><b>LAPORAN TRAINING MODEL</b></para>",
            styles["Title"]
        )
    )

    tanggal = datetime.now().strftime(
        "%d-%m-%Y %H:%M"
    )

    elements.append(
        Paragraph(
            f"<para align='center'>Tanggal Training : {tanggal}</para>",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    # =====================================
    # DATASET + METRIK
    # =====================================

    dataset_text = f"""
    <b>INFORMASI DATASET</b><br/><br/>
    Jumlah Data : {total_data}<br/>
    Data Training : {train_data}<br/>
    Data Testing : {test_data}
    """

    metric_text = f"""
    <b>HASIL EVALUASI</b><br/><br/>
    Accuracy : {accuracy:.2%}<br/>
    Precision : {precision:.2%}<br/>
    Recall : {recall:.2%}<br/>
    F1 Score : {f1:.2%}
    """

    info_table = Table(
        [[
            Paragraph(
                dataset_text,
                styles["BodyText"]
            ),

            Paragraph(
                metric_text,
                styles["BodyText"]
            )
        ]],
        colWidths=[250, 250]
    )

    info_table.setStyle(
        TableStyle([
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BACKGROUND", (0, 0), (0, 0), colors.whitesmoke),
            ("BACKGROUND", (1, 0), (1, 0), colors.whitesmoke)
        ])
    )

    elements.append(info_table)

    elements.append(
        Spacer(1, 10)
    )

    # =====================================
    # GAMBAR
    # =====================================

    print("CM IMAGE:", cm_image)
    print("FI IMAGE:", fi_image)

    print("CM EXISTS:", os.path.exists(cm_image))
    print("FI EXISTS:", os.path.exists(fi_image))

    try:

        if not os.path.exists(cm_image):
            raise FileNotFoundError(
                f"File tidak ditemukan: {cm_image}"
            )

        cm_img = Image(
            cm_image,
            width=6.5 * cm,
            height=5 * cm
        )

    except Exception as e:

        print("ERROR CONFUSION MATRIX:", e)

        cm_img = Paragraph(
            f"Error: {e}",
            styles["BodyText"]
        )

    try:

        if not os.path.exists(fi_image):
            raise FileNotFoundError(
                f"File tidak ditemukan: {fi_image}"
            )

        fi_img = Image(
            fi_image,
            width=6.5 * cm,
            height=5 * cm
        )

    except Exception as e:

        print("ERROR FEATURE IMPORTANCE:", e)

        fi_img = Paragraph(
            f"Error: {e}",
            styles["BodyText"]
        )

    grafik_table = Table(
        [
            [
                Paragraph(
                    "<b>CONFUSION MATRIX</b>",
                    styles["BodyText"]
                ),

                Paragraph(
                    "<b>FEATURE IMPORTANCE</b>",
                    styles["BodyText"]
                )
            ],

            [
                cm_img,
                fi_img
            ]
        ],
        colWidths=[250, 250]
    )

    grafik_table.setStyle(
        TableStyle([
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
        ])
    )

    elements.append(
        grafik_table
    )

    elements.append(
        Spacer(1, 10)
    )

    # =====================================
    # TOP FITUR
    # =====================================

    fitur_text = ""

    for i, fitur in enumerate(top_features):
        fitur_text += f"{i+1}. {fitur}<br/>"

    elements.append(
        Paragraph(
            f"""
            <b>FITUR PALING BERPENGARUH</b><br/><br/>
            {fitur_text}
            """,
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    # =====================================
    # KESIMPULAN
    # =====================================

    kesimpulan = f"""
    <b>KESIMPULAN</b><br/><br/>

    Model Random Forest berhasil dilatih menggunakan
    dataset layanan servis Yamaha.

    Model memperoleh Accuracy {accuracy:.2%},
    Precision {precision:.2%},
    Recall {recall:.2%},
    dan F1 Score {f1:.2%}.

    Berdasarkan hasil tersebut, model dapat digunakan
    sebagai alat bantu klasifikasi Service Ringan dan
    Service Berat.
    """

    kesimpulan_table = Table(
        [[
            Paragraph(
                kesimpulan,
                styles["BodyText"]
            )
        ]],
        colWidths=[500]
    )

    kesimpulan_table.setStyle(
        TableStyle([
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, -1), colors.whitesmoke)
        ])
    )

    elements.append(
        kesimpulan_table
    )

    doc.build(elements)

    return pdf_path
