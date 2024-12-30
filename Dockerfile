FROM python:3.10-slim

WORKDIR /app

COPY . .

# Dependency installation
RUN pip install --no-cache-dir flask

# Opening port 5000
EXPOSE 8000

# App run
CMD ["python", "web.py"]

