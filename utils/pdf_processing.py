from PyPDF2 import PdfReader

def extract_text_from_pdf(uploaded_pdf):
    pdf_reader = PdfReader(uploaded_pdf)
    page_texts = []
    for page in pdf_reader.pages:
        page_texts.append(page.extract_text())
    return page_texts
