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

1. Opens the PDF file using PyMuPDF.
2. Iterates through each page of the PDF.
3. Extracts the text from each page using PyMuPDF's get_text() method.
4. Returns the combined text from all pages.

***generate_qr_code(text, output_path, dimension):***

1. Creates a QR code object using the qrcode library.
2. Sets the error correction level to ensure robustness.
3. Adds the extracted text to the QR code.
4. Generates the QR code image.
5. Resizes the image to the desired dimensions.
6. Saves the image to the specified output path.
