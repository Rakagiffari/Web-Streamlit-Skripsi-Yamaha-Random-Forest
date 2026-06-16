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

from pathlib import Path
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

    logo_file = Path(logo_path)

    if logo_file.exists():

        logo = Image(
            str(logo_file),
            width=2*cm,
            height=2*cm
        )

        elements.append(
            Table(
                [[logo]],
                style=[
                    ("ALIGN",(0,0),(-1,-1),"CENTER")
                ]
            )
        )

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

    elements.append(
        Paragraph(
            f"<para align='center'>Tanggal Training : {datetime.now().strftime('%d-%m-%Y %H:%M')}</para>",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1,10)
    )

    # =====================================
    # DATASET + METRIK
    # =====================================

    info_table = Table(

        [[

            Paragraph(
                f"""
                <b>INFORMASI DATASET</b><br/><br/>
                Jumlah Data : {total_data}<br/>
                Data Training : {train_data}<br/>
                Data Testing : {test_data}
                """,
                styles["BodyText"]
            ),

            Paragraph(
                f"""
                <b>HASIL EVALUASI</b><br/><br/>
                Accuracy : {accuracy:.2%}<br/>
                Precision : {precision:.2%}<br/>
                Recall : {recall:.2%}<br/>
                F1 Score : {f1:.2%}
                """,
                styles["BodyText"]
            )

        ]],

        colWidths=[250,250]

    )

    info_table.setStyle(

        TableStyle([

            ("BOX",(0,0),(-1,-1),1,colors.black),
            ("GRID",(0,0),(-1,-1),1,colors.black)

        ])

    )

    elements.append(info_table)

    elements.append(
        Spacer(1,10)
    )

    # =====================================
    # GAMBAR
    # =====================================

    cm_file = Path(cm_image)
    fi_file = Path(fi_image)

    if cm_file.exists():

        cm = Image(
            str(cm_file),
            width=6*cm,
            height=4.5*cm
        )

    else:

        cm = Paragraph(
            f"Gambar tidak ditemukan:<br/>{cm_file}",
            styles["BodyText"]
        )

    if fi_file.exists():

        fi = Image(
            str(fi_file),
            width=6*cm,
            height=4.5*cm
        )

    else:

        fi = Paragraph(
            f"Gambar tidak ditemukan:<br/>{fi_file}",
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

                cm,
                fi

            ]

        ],

        colWidths=[250,250]

    )

    grafik_table.setStyle(

        TableStyle([

            ("BOX",(0,0),(-1,-1),1,colors.black),
            ("GRID",(0,0),(-1,-1),1,colors.black),
            ("ALIGN",(0,0),(-1,-1),"CENTER"),
            ("VALIGN",(0,0),(-1,-1),"MIDDLE")

        ])

    )

    elements.append(
        grafik_table
    )

    elements.append(
        Spacer(1,10)
    )

    # =====================================
    # FITUR
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
        Spacer(1,10)
    )

    # =====================================
    # KESIMPULAN
    # =====================================

    kesimpulan = Table(

        [[

            Paragraph(

                f"""
                <b>KESIMPULAN</b><br/><br/>

                Model Random Forest memperoleh:

                Accuracy : {accuracy:.2%}<br/>
                Precision : {precision:.2%}<br/>
                Recall : {recall:.2%}<br/>
                F1 Score : {f1:.2%}<br/><br/>

                Model dapat digunakan sebagai
                alat bantu klasifikasi Service
                Ringan dan Service Berat.
                """,

                styles["BodyText"]

            )

        ]],

        colWidths=[500]

    )

    kesimpulan.setStyle(

        TableStyle([

            ("BOX",(0,0),(-1,-1),1,colors.black)

        ])

    )

    elements.append(
        kesimpulan
    )

    doc.build(elements)

    return pdf_path
