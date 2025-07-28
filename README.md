# 🧠 Adobe-1B

A fully containerized solution to process and analyze PDF documents using local NLP models — ensuring **data privacy**, **offline compatibility**, and **structured output** generation.

---

## 🧰 Features

- 📄 Extracts text, images, and metadata from PDFs using `PyMuPDF`
- 🧹 Cleans and formats content for consistency
- 🤖 Infers document semantics using **local NLP models** 
- 🧠 Embedding-based similarity for smart content classification
- 📦 Containerized using Docker (Python 3.12-slim)
- 🔒 Completely offline, secure, and reproducible

---

## 🧭 Methodology and Approach

### 📥 Step 1: PDF Ingestion
- PDFs are placed in a designated `input/` directory.
- Text, images, and metadata are extracted using `PyMuPDF (fitz)`, ensuring flexibility across diverse document types.

### 🧼 Step 2: Preprocessing and Cleaning
- Text is preprocessed:
  - Tokenization  
  - Noise removal  
  - Structural formatting
- Ensures consistent and clean data for downstream NLP inference.

### 🤖 Step 3: Local Model Inference
- Uses **`sentence-transformers`** such as:
  - `all-MiniLM-L12-v2`
- Models are stored locally in `local_models/` to ensure:
  - ✅ Offline compatibility  
  - ✅ No data leakage  
  - ✅ Fast inference
- Embeddings are computed for content and matched against predefined query vectors using **cosine similarity** to extract:
  - Table of contents  
  - Summary  
  - Keywords  
  - Custom semantic segments

### 📊 Step 4: Structured Output
- Output is saved in `JSON` format, placed alongside its input collection:
  - Example:  
    Input → `/input/Collection_A/input.pdf`  
    Output → `/input/Collection_A/output.json`

### 🐳 Step 5: Containerization
- Everything runs inside a Docker container:
  - Base image: `python:3.12-slim`
  - Includes: `PyMuPDF`, `sentence-transformers` etc.
- Uses `--network none` to ensure **no internet access**
- Fully reproducible and isolated from host machine

---

## 🛠️ How to Build and Run
1) Clone the Repository
2) Create a Virtual Environment: python -m venv venv (command)
3) For Activating Virtual Environment: venv\Scripts\activate (activate command)
4) Install All Dependencies: pip install -r requirements.txt (command)
5) Download the Model Locally (One-Time): python download_model.py (command)
6) Place your .pdf files into the /input/Collection/PDFs folder, and also add your input.json
7) Run the main file: python main.py (command)

### 🔧 Docker Commands (Run in Powershell)

1) Build Command: docker build --platform Linux/amd64 -t adobe1b.personachallenge .
2) Run Command: docker run --rm -v ${PWD}:/app adobe1b.personachallenge
