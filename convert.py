from PIL import Image
import img2pdf


def convert_to(file, ctype: str):
    img = Image.open(file)
    if ctype == "pdf":
        pdf_bytes = img2pdf.convert(img.filename)
        # Save the PDF
        with open('file.pdf', 'wb') as pdf_file:
            pdf_file.write(pdf_bytes)
    else:
        img.save("image.%s" % ctype)