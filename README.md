# PDF to QR Code Generator

This Python code extracts text from a PDF file and generates a QR code containing that text.

**Installation**
Before running the code, ensure you have the following libraries installed:

* PyMuPDF (fitz)
* qrcode
* Pillow (PIL)

**Usage**
1. Edit the pdf_path variable to specify the path to your PDF file.
2. Edit the output_path variable to indicate where you want to save the generated QR code.
3. Optionally, adjust the dimension variable to change the size of the QR code (defaults to 550x550 pixels).

**Functionality**
The code consists of two main functions:

***pdf_to_text(pdf_path):***

. Opens the PDF file using PyMuPDF.
. Iterates through each page of the PDF.
. Extracts the text from each page using PyMuPDF's get_text() method.
. Returns the combined text from all pages.

***generate_qr_code(text, output_path, dimension):***

. Creates a QR code object using the qrcode library.
. Sets the error correction level to ensure robustness.
. Adds the extracted text to the QR code.
. Generates the QR code image.
. Resizes the image to the desired dimensions.
. Saves the image to the specified output path.
