Methodology and Approach
Our solution is designed to process and analyze PDF documents using local models in a controlled, secure environment. The overall goal is to extract relevant content, apply inference using NLP models, and generate structured output in a reproducible and isolated manner using Docker.

Step 1: PDF Ingestion
The system begins by reading PDF files placed in a designated input directory. These files are extracted using the PyMuPDF library (fitz), which offers fast and flexible access to text, images, and metadata embedded in PDFs. This ensures robustness across a wide variety of document types.

Step 2: Preprocessing and Cleaning
Extracted text undergoes preprocessing including tokenization, noise removal, and structural formatting. This prepares the content for further inference and ensures consistency in outputs regardless of input formatting variation.

Step 3: Local Model Inference
We use sentence-transformers (e.g., all-mpnet-base-v2 or all-mini-lm-l6-v2) from Hugging Face to compute semantic embeddings for extracted content. These models are pre-downloaded into a local_models directory to ensure offline compatibility and data privacy.

We compute cosine similarity between document embeddings and predefined query vectors or templates to classify and extract relevant data (such as table of contents, summary, keywords, etc.).

This step enables smart data understanding without relying on cloud-based APIs, ensuring full control and security.

Step 4: Structured Output
Based on the inference results, JSON output files are generated and saved. Each output file is saved in the same collection (folder) from which its input PDF was retrieved, maintaining organizational traceability.

For example, if input is from /input/Collection_A/input.json, the corresponding output is saved in /input/Collection_A/output.json.

Step 5: Containerization
The solution is fully containerized using Docker. All dependencies (Tesseract, poppler-utils, PyTorch, etc.) are installed in a Python 3.12-slim image. This ensures reproducibility and isolates the runtime environment from the host machine. No internet access is used inside the container (--network none), supporting secure offline execution.
