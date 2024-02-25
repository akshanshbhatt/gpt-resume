import fitz
import os


def convert_pdf_to_text(pdf_path, text_path):
    doc = fitz.open(pdf_path)

    with open(text_path, 'wb') as text_file:
        for page in doc:
            text = page.get_text().encode('utf-8')
            text_file.write(text)

    doc.close()


def convert_pdfs_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            text_filename = os.path.splitext(filename)[0] + ".txt"
            text_path = os.path.join(output_folder, text_filename)
            convert_pdf_to_text(pdf_path, text_path)
            print(f"Converted {filename} to {text_filename}")
