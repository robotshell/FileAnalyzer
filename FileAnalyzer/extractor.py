import pdfplumber
from docx import Document
from openpyxl import load_workbook
from pptx import Presentation
import logging

def extract_text(file_path):
    text, metadata = "", []

    try:
        if file_path.endswith(".pdf"):
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
                if pdf.metadata:
                    metadata.extend([f"{k}: {v}" for k, v in pdf.metadata.items()])

        elif file_path.endswith(".docx"):
            doc = Document(file_path)
            for p in doc.paragraphs:
                text += p.text + "\n"
            if doc.core_properties.author:
                metadata.append(f"Author: {doc.core_properties.author}")

        elif file_path.endswith(".xlsx"):
            wb = load_workbook(file_path, data_only=True)
            for sheet in wb:
                for row in sheet.iter_rows(values_only=True):
                    for cell in row:
                        if cell:
                            text += str(cell) + " "

        elif file_path.endswith(".pptx"):
            prs = Presentation(file_path)
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, "text"):
                        text += shape.text + "\n"

    except Exception as e:
        logging.warning(f"Failed to extract {file_path}: {e}")

    return text, metadata
