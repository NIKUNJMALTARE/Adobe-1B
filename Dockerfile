# Use an official Python 3.12 base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies required by PyMuPDF, torch, etc.
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    tesseract-ocr \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Ensure input/output directories exist
RUN mkdir -p /app/input /app/output

# Default command to run your processing script
CMD ["python", "main.py"]
