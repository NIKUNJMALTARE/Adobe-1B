import json
import os
from datetime import datetime
from utils.pdf_utils import parse_all_pdfs
from utils.scoring import rank_sections_by_relevance
from utils.summarizer import summarize_section

INPUT_DIR = "input"

def load_input(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def process_collection(collection_path):
    input_path = os.path.join(collection_path, "input.json")
    output_path = os.path.join(collection_path, "output.json")
    
    if not os.path.exists(input_path):
        print(f"⚠️ Skipping {collection_path}: No input.json found.")
        return

    data = load_input(input_path)
    persona = data["persona"]["role"]
    job = data["job_to_be_done"]["task"]
    query = f"As an {persona}, I need to {job}. I'm looking for instructions, tools, or workflows that help me complete this task in Acrobat."

    documents = data["documents"]
    parsed_docs = parse_all_pdfs(documents)
    results = rank_sections_by_relevance(query, parsed_docs)

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

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"Processed: {collection_path}")

def main():
    for name in os.listdir(INPUT_DIR):
        collection_path = os.path.join(INPUT_DIR, name)
        if os.path.isdir(collection_path):
            process_collection(collection_path)

if __name__ == "__main__":
    main()