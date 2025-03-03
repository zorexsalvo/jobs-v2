# Use Python 3.11 as base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        nodejs \
        npm \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Install Tailwind dependencies and build
RUN npm i
RUN python manage.py tailwind install
RUN python manage.py tailwind build

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 
