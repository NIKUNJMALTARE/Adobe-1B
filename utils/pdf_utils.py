from concurrent.futures import ProcessPoolExecutor
import fitz
import os
import re

collection_path = "input/Collection-1/PDFs"


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"Page \d+", "", text)
    return text.strip()

def extract_sections_single_pdf(pdf_path, filename):
    doc = fitz.open(pdf_path)
    sections = []
    for page_num, page in enumerate(doc, 1):
        text = page.get_text("text")
        cleaned_text = clean_text(text)
        chunks = re.split(r'(?<=\.)\s+', cleaned_text)
        buffer = ""
        for part in chunks:
            if len(buffer) + len(part) < 1000:
                buffer += part + " "
            else:
                if 300 < len(buffer) < 1200:
                    sections.append({
                        "title": buffer.split('.')[0],
                        "content": buffer.strip(),
                        "page": page_num,
                        "document": filename
                    })
                buffer = part + " "
    return sections

def parse_all_pdfs(document_list):
    # List all PDF files in the folder
    pdf_files = [f for f in os.listdir(collection_path) if f.endswith(".pdf")]
    document_list = [{"filename": f} for f in pdf_files]

    with ProcessPoolExecutor() as executor:
        futures = []
        for doc in document_list:
            file_path = os.path.join(collection_path, doc["filename"])
            futures.append(executor.submit(extract_sections_single_pdf, file_path, doc["filename"]))

        parsed = []
        for future in futures:
            parsed.extend(future.result())
        return parsed
