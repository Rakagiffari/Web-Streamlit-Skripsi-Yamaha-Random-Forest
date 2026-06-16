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
        rightMargin=20,
        leftMargin=20,
        topMargin=20,
        bottomMargin=20
    )

    styles = getSampleStyleSheet()

    content = []

    # =====================================
    # LOGO
    # =====================================
    try:

        logo = Image(
            logo_path,
            width=2.5 * cm,
            height=2.5 * cm
        )

        content.append(logo)

    except:
        pass

    # =====================================
    # HEADER
    # =====================================
    content.append(
        Paragraph(
            "<b>PT YAMAHA TJAHAJA BARU TABING</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            "<b>LAPORAN TRAINING MODEL</b>",
            styles["Title"]
        )
    )

    tanggal = datetime.now().strftime(
        "%d-%m-%Y %H:%M"
    )

    content.append(
        Paragraph(
            f"Tanggal Training : {tanggal}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # =====================================
    # DATASET
    # =====================================
    dataset_table = Table(

        [
            ["Jumlah Data", total_data],
            ["Data Training", train_data],
            ["Data Testing", test_data]
        ],

        colWidths=[180, 180]
    )

    dataset_table.setStyle(

        TableStyle([

            ("GRID", (0,0), (-1,-1), 1, colors.black),

            ("BACKGROUND", (0,0), (0,-1), colors.lightgrey),

            ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold")
        ])
    )

    content.append(
        Paragraph(
            "<b>INFORMASI DATASET</b>",
            styles["Heading3"]
        )
    )

    content.append(dataset_table)

    content.append(
        Spacer(1, 10)
    )

    # =====================================
    # METRIK
    # =====================================
    metric_table = Table(

        [
            ["Accuracy", f"{accuracy:.2%}"],
            ["Precision", f"{precision:.2%}"],
            ["Recall", f"{recall:.2%}"],
            ["F1 Score", f"{f1:.2%}"]
        ],

        colWidths=[180, 180]
    )

    metric_table.setStyle(

        TableStyle([

            ("GRID", (0,0), (-1,-1), 1, colors.black),

            ("BACKGROUND", (0,0), (0,-1), colors.lightgrey),

            ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold")
        ])
    )

    content.append(
        Paragraph(
            "<b>HASIL EVALUASI MODEL</b>",
            styles["Heading3"]
        )
    )

    content.append(metric_table)

    content.append(
        Spacer(1, 10)
    )

    # =====================================
    # CONFUSION MATRIX
    # =====================================
    content.append(
        Paragraph(
            "<b>CONFUSION MATRIX</b>",
            styles["Heading3"]
        )
    )

    try:

        content.append(

            Image(
                cm_image,
                width=7 * cm,
                height=5 * cm
            )
        )

    except:
        pass

    content.append(
        Spacer(1, 10)
    )

    # =====================================
    # FEATURE IMPORTANCE
    # =====================================
    content.append(
        Paragraph(
            "<b>FITUR PALING BERPENGARUH</b>",
            styles["Heading3"]
        )
    )

    fitur_text = ""

    for i, fitur in enumerate(top_features):

        fitur_text += f"{i+1}. {fitur}<br/>"

    content.append(
        Paragraph(
            fitur_text,
            styles["Normal"]
        )
    )

    try:

        content.append(

            Image(
                fi_image,
                width=8 * cm,
                height=5 * cm
            )
        )

    except:
        pass

    content.append(
        Spacer(1, 10)
    )

    # =====================================
    # KESIMPULAN
    # =====================================
    content.append(
        Paragraph(
            "<b>KESIMPULAN</b>",
            styles["Heading3"]
        )
    )

    content.append(

        Paragraph(

            f"""
            Model Random Forest berhasil dilatih
            menggunakan dataset layanan servis Yamaha.

            Berdasarkan hasil evaluasi, model memperoleh
            akurasi sebesar {accuracy:.2%},
            precision sebesar {precision:.2%},
            recall sebesar {recall:.2%},
            dan F1-score sebesar {f1:.2%}.

            Hasil tersebut menunjukkan bahwa model
            memiliki kemampuan yang baik dalam
            mengklasifikasikan layanan servis
            Ringan dan Berat.
            """,

            styles["Normal"]
        )
    )

    doc.build(content)

    return pdf_path
