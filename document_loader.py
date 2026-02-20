import os
import pandas as pd
from PyPDF2 import PdfReader
from docx import Document

def _read_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def _read_docx(path):
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def _read_csv_sample(path):
    df = pd.read_csv(path)
    summary = df.head(5).to_string()
    return f"Columns: {', '.join(df.columns)}\nSample Data:\n{summary}"

def _read_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_documents_from_folder(base_folder):
    documents = []
    for root, _, files in os.walk(base_folder):
        for file in files:
            path = os.path.join(root, file)

            if file.endswith(".pdf"):
                text = _read_pdf(path)
            elif file.endswith(".docx"):
                text = _read_docx(path)
            elif file.endswith(".csv"):
                text = _read_csv_sample(path)
            elif file.endswith(".txt"):
                text = _read_txt(path)
            else:
                continue

            documents.append({
                "content": text,
                "source": path,
                "department": os.path.basename(os.path.dirname(path))
            })

    return documents