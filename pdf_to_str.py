# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 02:31:02 2023

@author: PC
"""
import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages

        for page_number in range(num_pages):
            page = pdf_reader.getPage(page_number)
            text += page.extractText()

    return text

# PDF belgesinin yolunu belirtin
pdf_path = "TRT1 - 18.033.552.pdf"

# Metni çıkarın
extracted_text = extract_text_from_pdf(pdf_path)

# Çıkarılan metni yazdırın
print(extracted_text)