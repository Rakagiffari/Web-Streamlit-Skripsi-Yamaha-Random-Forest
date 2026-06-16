from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    filename,
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

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "LAPORAN HASIL TRAINING RANDOM FOREST",
            styles["Title"]
        )
    )

    story.append(Spacer(1,10))

    story.append(
        Paragraph(
            f"Jumlah Data : {total_data}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Data Training : {train_data}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Data Testing : {test_data}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,10))

    story.append(
        Paragraph(
            f"Accuracy : {accuracy:.2%}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Precision : {precision:.2%}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Recall : {recall:.2%}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"F1 Score : {f1:.2%}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,10))

    story.append(
        Paragraph(
            "Confusion Matrix",
            styles["Heading2"]
        )
    )

    story.append(
        Image(
            cm_image,
            width=220,
            height=180
        )
    )

    story.append(
        Paragraph(
            "Feature Importance",
            styles["Heading2"]
        )
    )

    story.append(
        Image(
            fi_image,
            width=250,
            height=180
        )
    )

    fitur_text = "<br/>".join(
        [
            f"{i+1}. {fitur}"
            for i, fitur
            in enumerate(top_features)
        ]
    )

    story.append(
        Paragraph(
            fitur_text,
            styles["Normal"]
        )
    )

    story.append(Spacer(1,10))

    story.append(
        Paragraph(
            f"""
            Berdasarkan hasil training menggunakan
            algoritma Random Forest, model memperoleh
            akurasi sebesar {accuracy:.2%}.
            Model memiliki performa yang baik dan
            dapat digunakan sebagai alat bantu
            klasifikasi layanan servis Yamaha.
            """,
            styles["Normal"]
        )
    )

    doc.build(story)

    return filename
