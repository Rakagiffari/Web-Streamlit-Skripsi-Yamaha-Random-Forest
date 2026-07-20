from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from reportlab.lib.enums import (
    TA_LEFT,
    TA_CENTER,
    TA_RIGHT
)
from reportlab.platypus import (
    HRFlowable
)
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
    nama_file,
    total_data,
    duplicate_data,
    missing_value,
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
        leftMargin=1 * cm,
        rightMargin=1 * cm,
        topMargin=1 * cm,
        bottomMargin=1 * cm
    )

    styles = getSampleStyleSheet()

    elements = []

    # ==========================================================
    # HEADER
    # ==========================================================

    company_style = ParagraphStyle(
        "CompanyStyle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=22,
        alignment=TA_LEFT,
        textColor=colors.black
    )

    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=12,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#555555")
    )

    contact_style = ParagraphStyle(
        "ContactStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=11,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#666666")
    )

    report_title_style = ParagraphStyle(
        "ReportTitleStyle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=17,
        leading=20,
        alignment=TA_CENTER
    )

    # ==========================================================
    # LOGO
    # ==========================================================

    if os.path.exists(logo_path):

        logo = Image(
            logo_path,
            width=3.8 * cm,
            height=2.5 * cm
        )
    else:
        logo = Spacer(3.8 * cm, 2.5 * cm)

    # ==========================================================
    # INFORMASI PERUSAHAAN
    # ==========================================================

    tanggal = datetime.now().strftime("%d %B %Y %H:%M:%S")

    company_info = Table(
        [
            [
                Paragraph(
                    "PT. YAMAHA INDONESIA MOTOR MANUFACTURING",
                    company_style
                )
            ],
            [
                Paragraph(
                    "YAMAHA TJAHAJA BARU TABING",
                    subtitle_style
                )
            ],
            [
                Paragraph(
                    "Jl. Prof. Dr. Hamka No.56, Parupuk Tabing, Kec. Koto Tangah, Kota Padang, Sumatera Barat 25173",
                    contact_style
                )
            ],
            [
                Paragraph(
                    "08116606631  |  https://tjahaja-baru.com/",
                    contact_style
                )
            ],
            [
                Paragraph(
                    f"{tanggal}",
                    contact_style
                )
            ],
        ],
        colWidths=[13.5 * cm]
    )

    company_info.setStyle(
        TableStyle([
            ("LEFTPADDING",(0,0),(-1,-1),0),
            ("RIGHTPADDING",(0,0),(-1,-1),0),
            ("TOPPADDING",(0,0),(-1,-1),0),
            ("BOTTOMPADDING",(0,0),(-1,-1),1),
            ("VALIGN",(0,0),(-1,-1),"TOP")
        ])
    )

    # ==========================================================
    # HEADER TABLE
    # ==========================================================

    header_table = Table(
        [
            [
                logo,
                company_info
            ]
        ],
        colWidths=[4.2 * cm, 13.8 * cm]
    )

    header_table.setStyle(
        TableStyle([
            ("VALIGN",(0,0),(-1,-1),"TOP"),
            ("LEFTPADDING",(0,0),(-1,-1),0),
            ("RIGHTPADDING",(0,0),(-1,-1),0),
            ("TOPPADDING",(0,0),(-1,-1),0),
            ("BOTTOMPADDING",(0,0),(-1,-1),0)
        ])
    )

    elements.append(header_table)

    elements.append(
        Spacer(1, 8)
    )

    # ==========================================================
    # GARIS PEMBATAS
    # ==========================================================

    elements.append(
        HRFlowable(
            width="100%",
            thickness=2,
            color=colors.HexColor("#C00000")
        )
    )

    elements.append(
        Spacer(1, 8)
    )

    # =====================================
    # PENJELASAN LAPORAN
    # =====================================

    elements.append(
        Spacer(1, 8)
    )

    penjelasan = """
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    Laporan ini menyajikan informasi hasil klasifikasi layanan service
    kendaraan yamaha yang dihasilkan oleh sistem menggunakan algoritma
    random forest. Informasi yang ditampilkan bertujuan untuk
    memberikan gambaran mengenai proses klasifikasi layanan service
    berdasarkan data kendaraan yang telah diproses oleh sistem.
    """

    elements.append(
        Paragraph(
            penjelasan,
            styles["BodyText"]
        )
    )

    # =====================================
    # INFORMASI DATASET
    # =====================================
    
    elements.append(
        Paragraph(
            """
            Berikut informasi mengenai dataset yang digunakan
            pada klasifikasi layanan service kendaraan.
            """,
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 5)
    )

    dataset_table = Table(
        [
            ["Nama File", ":", nama_file],
            ["Jumlah Data", ":", f"{total_data} data"],
            ["Data Duplikat", ":", f"{duplicate_data} data"],
            ["Missing Value", ":", f"{missing_value} data"],
        ],
        colWidths=[165, 10, 305]
    )

    dataset_table.setStyle(
        TableStyle([
            ("FONTNAME", (0,0), (-1,-1), "Helvetica"),
            ("FONTSIZE", (0,0), (-1,-1), 10),
            ("BOTTOMPADDING", (0,0), (-1,-1), 3),
            ("TOPPADDING", (0,0), (-1,-1), 3),
            ("LEFTPADDING", (0,0), (-1,-1), 18),
            ("RIGHTPADDING", (0,0), (-1,-1), 0),
            ("VALIGN", (0,0), (-1,-1), "TOP"),

            # Tidak ada garis sehingga tampil seperti dokumen Word
            ("LINEBELOW", (0,0), (-1,-1), 0, colors.white),
            ("LINEABOVE", (0,0), (-1,-1), 0, colors.white),
            ("LINEBEFORE", (0,0), (-1,-1), 0, colors.white),
            ("LINEAFTER", (0,0), (-1,-1), 0, colors.white),
        ])
    )

    elements.append(dataset_table)

    elements.append(
        Spacer(1,5)
    )

    # =====================================
    # HASIL EVALUASI MODEL
    # =====================================

    hasil_evaluasi = f"""
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    Model Random Forest dievaluasi menggunakan
    {train_data} data training dan
    {test_data} data testing. Berdasarkan hasil pengujian,
    model memperoleh Accuracy sebesar {accuracy:.2%},
    Precision {precision:.2%},
    Recall {recall:.2%}, dan
    F1-Score {f1:.2%}. Nilai tersebut menunjukkan bahwa model
    memiliki kemampuan yang baik dalam mengklasifikasikan layanan
    Service Ringan dan Service Berat.

    <br/><br/>
    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    Visualisasi Confusion Matrix pada bagian berikut
    menunjukkan perbandingan antara hasil prediksi model dengan
    data aktual.
    """

    elements.append(
        Paragraph(
            hasil_evaluasi,
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 5)
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

    # =====================================
    # FITUR PALING BERPENGARUH
    # =====================================

    elements.append(

        Paragraph(

            "<b>FITUR PALING BERPENGARUH</b>",

            styles["Heading3"]

        )

    )

    elements.append(
        Spacer(1,5)
    )

    fitur_data = [

        ["No", "Nama Fitur"]

    ]

    for i, fitur in enumerate(top_features, start=1):

        fitur_data.append([

            str(i),

            fitur

        ])

    fitur_table = Table(

        fitur_data,

        colWidths=[45, 420]

    )

    fitur_table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,colors.grey),

            ("BOX",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#E5E7EB")),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("ALIGN",(0,0),(0,-1),"CENTER"),

            ("VALIGN",(0,0),(-1,-1),"MIDDLE"),

            ("BOTTOMPADDING",(0,0),(-1,-1),8)

        ])

    )

    elements.append(fitur_table)

    elements.append(
        Spacer(1,15)
    )

    # =====================================
    # KESIMPULAN
    # =====================================

    elements.append(

        Paragraph(

            "<b>KESIMPULAN</b>",

            styles["Heading3"]

        )

    )

    elements.append(
        Spacer(1,5)
    )

    kesimpulan = f"""
    Model Random Forest berhasil dilatih menggunakan dataset
    layanan service kendaraan Yamaha.

    Berdasarkan proses pelatihan diperoleh nilai Accuracy sebesar
    <b>{accuracy:.2%}</b>, Precision sebesar
    <b>{precision:.2%}</b>, Recall sebesar
    <b>{recall:.2%}</b>, dan F1-Score sebesar
    <b>{f1:.2%}</b>.

    Hasil evaluasi menunjukkan bahwa model mampu melakukan
    klasifikasi layanan <b>Service Ringan</b> dan
    <b>Service Berat</b> dengan performa yang baik.

    Feature Importance menunjukkan bahwa beberapa fitur utama
    memiliki kontribusi paling besar terhadap proses klasifikasi,
    sehingga dapat digunakan sebagai dasar dalam pengambilan
    keputusan layanan service kendaraan.
    """

    kesimpulan_table = Table(

        [[

            Paragraph(

                kesimpulan,

                styles["BodyText"]

            )

        ]],

        colWidths=[470]

    )

    kesimpulan_table.setStyle(

        TableStyle([

            ("BOX",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,0),(-1,-1),colors.whitesmoke),

            ("BOTTOMPADDING",(0,0),(-1,-1),10),

            ("TOPPADDING",(0,0),(-1,-1),10)

        ])

    )

    elements.append(kesimpulan_table)

    elements.append(
        Spacer(1,10)
    )

    # =====================================
    # PENUTUP LAPORAN
    # =====================================

    elements.append(
        Paragraph(
            "<para align='center'><font size='9' color='grey'>"
            "Laporan ini dibuat secara otomatis oleh Sistem "
            "Klasifikasi Layanan Service Kendaraan Yamaha "
            "menggunakan algoritma Random Forest."
            "</font></para>",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 8)
    )

    # =====================================
    # MEMBUAT PDF
    # =====================================

    try:

        doc.build(elements)

    except Exception as e:

        raise Exception(
            f"Gagal membuat laporan PDF: {str(e)}"
        )

    # =====================================
    # RETURN PATH PDF
    # =====================================

    return pdf_path
