FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    tesseract-ocr \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY local_models /app/local_models

COPY . .

RUN mkdir -p /app/input /app/output

ENV TOKENIZERS_PARALLELISM=false

CMD ["python", "main.py"]