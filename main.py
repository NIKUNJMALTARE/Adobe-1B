import json
import os
from datetime import datetime
from utils.pdf_utils import parse_all_pdfs
from utils.scoring import rank_sections_by_relevance
from utils.summarizer import summarize_section

INPUT_FILE = "input/input.json"
OUTPUT_FILE = "output/output.json"

def load_input():
    with open(INPUT_FILE, "r") as f:
        return json.load(f)

def main():
    data = load_input()
    persona = data["persona"]["role"]
    job = data["job_to_be_done"]["task"]
    query = f"{persona}. Task: {job}"

    documents = data["documents"]
    parsed_docs = parse_all_pdfs(documents)

    results = rank_sections_by_relevance(query, parsed_docs)

    # Output formatting
    output = {
        "metadata": {
            "input_documents": [doc["filename"] for doc in documents],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": str(datetime.now())
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    for i, (section, score) in enumerate(results[:5], 1):
        output["extracted_sections"].append({
            "document": section["document"],
            "section_title": section["title"],
            "importance_rank": i,
            "page_number": section["page"]
        })

        refined_text = summarize_section(section["content"])
        output["subsection_analysis"].append({
            "document": section["document"],
            "refined_text": refined_text,
            "page_number": section["page"]
        })

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main()
