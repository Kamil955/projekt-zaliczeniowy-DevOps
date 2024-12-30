FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Dependency installation
RUN pip install flask

# Opening port 5000
EXPOSE 5000

# App run
CMD ["python", "web.py"]
