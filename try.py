import fitz  # PyMuPDF
import qrcode
from PIL import Image

def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    return text

def generate_qr_code(text, output_path, dimension):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((550, 550))

    img.save(output_path)

if __name__ == "__main__":
    pdf_path = "t.pdf"
    output_path = "tqr.png"
    dimension = 550

    text = pdf_to_text(pdf_path)
    generate_qr_code(text, output_path, dimension)
