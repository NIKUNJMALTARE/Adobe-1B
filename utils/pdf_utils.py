import fitz  # PyMuPDF
import os

def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []
    for page_num, page in enumerate(doc, 1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                text = " ".join([span['text'] for line in block["lines"] for span in line["spans"]])
                if 20 < len(text) < 400:  # avoid junk
                    sections.append({
                        "title": text.strip().split('.')[0],
                        "content": text.strip(),
                        "page": page_num
                    })
    return sections

def parse_all_pdfs(document_list):
    parsed = []
    for doc in document_list:
        file_path = os.path.join("input", doc["filename"])
        sections = extract_sections(file_path)
        for s in sections:
            s["document"] = doc["filename"]
        parsed.extend(sections)
    return parsed