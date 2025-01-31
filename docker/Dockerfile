# ─────────────── STAGE 1: Builder ───────────────
FROM python:3.9 AS builder

# Set working directory
WORKDIR /app

# Copy dependency file separately for better caching
COPY app/requirements.txt /app/requirements.txt

# Install dependencies inside a temporary layer
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ─────────────── STAGE 2: Runtime ───────────────
FROM python:3.9-slim

WORKDIR /app

# Copy only necessary files from builder stage
COPY --from=builder /install /usr/local
COPY app /app

# Set default port
ENV FLASK_PORT=5001

# Expose the port dynamically
EXPOSE ${FLASK_PORT}

# Run Flask directly
CMD ["python", "app.py"]


