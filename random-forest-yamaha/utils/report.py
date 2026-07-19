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
from pathlib import Path
import os


# ==========================================================
# GENERATE PDF
# ==========================================================

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

    # =====================================
    # VALIDASI PATH
    # =====================================

    pdf_path = str(Path(pdf_path))
    logo_path = str(Path(logo_path))
    cm_image = str(Path(cm_image))
    fi_image = str(Path(fi_image))

    # =====================================
    # MEMBUAT DOKUMEN
    # =====================================

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

    if os.path.exists(logo_path):

        logo = Image(
            logo_path,
            width=2.2 * cm,
            height=2.2 * cm
        )

        logo_table = Table([[logo]])

        logo_table.setStyle(
            TableStyle([
                ("ALIGN", (0, 0), (-1, -1), "CENTER")
            ])
        )

        elements.append(logo_table)

        elements.append(
            Spacer(1, 5)
        )

    elements.append(

        Paragraph(

            "<para align='center'><b>PT. YAMAHA TJAHAJA BARU TABING</b></para>",

            styles["Heading2"]

        )

    )

    elements.append(

        Paragraph(

            "<para align='center'><b>LAPORAN HASIL PELATIHAN MODEL RANDOM FOREST</b></para>",

            styles["Title"]

        )

    )

    tanggal = datetime.now().strftime(
        "%d %B %Y %H:%M"
    )

    elements.append(

        Paragraph(

            f"<para align='center'>Tanggal Pembuatan : {tanggal}</para>",

            styles["Normal"]

        )

    )

    elements.append(
        Spacer(1, 12)
    )

        # =====================================
    # INFORMASI DATASET & HASIL EVALUASI
    # =====================================

    dataset_text = f"""
    <b>INFORMASI DATASET</b><br/><br/>
    • Jumlah Data : {total_data}<br/>
    • Data Training : {train_data}<br/>
    • Data Testing : {test_data}
    """

    metric_text = f"""
    <b>HASIL EVALUASI MODEL</b><br/><br/>
    • Accuracy : {accuracy:.2%}<br/>
    • Precision : {precision:.2%}<br/>
    • Recall : {recall:.2%}<br/>
    • F1-Score : {f1:.2%}
    """

    info_table = Table(
        [[
            Paragraph(dataset_text, styles["BodyText"]),
            Paragraph(metric_text, styles["BodyText"])
        ]],
        colWidths=[240, 240]
    )

    info_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,colors.grey),

            ("BOX",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,0),(-1,-1),colors.whitesmoke),

            ("VALIGN",(0,0),(-1,-1),"TOP"),

            ("BOTTOMPADDING",(0,0),(-1,-1),10)

        ])

    )

    elements.append(info_table)

    elements.append(
        Spacer(1,15)
    )

    # =====================================
    # VISUALISASI
    # =====================================

    cm_obj = None
    fi_obj = None

    if os.path.exists(cm_image):

        cm_obj = Image(
            cm_image,
            width=7*cm,
            height=6*cm
        )

    else:

        cm_obj = Paragraph(
            "Confusion Matrix tidak tersedia.",
            styles["BodyText"]
        )

    if os.path.exists(fi_image):

        fi_obj = Image(
            fi_image,
            width=7*cm,
            height=6*cm
        )

    else:

        fi_obj = Paragraph(
            "Feature Importance tidak tersedia.",
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

                cm_obj,
                fi_obj

            ]

        ],

        colWidths=[240,240]

    )

    grafik_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,colors.grey),

            ("BOX",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#F3F4F6")),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("VALIGN",(0,0),(-1,-1),"MIDDLE"),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8)

        ])

    )

    elements.append(grafik_table)

    elements.append(
        Spacer(1,15)
    )
