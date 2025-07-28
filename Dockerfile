# Dockerfile
FROM --platform=linux/amd64 python:3.10-slim


# Copy entire app codebase
COPY . .

# Install dependencies (CPU only, offline safe)
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python", "main.py"]
