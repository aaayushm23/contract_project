# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN python -m venv /opt/venv && /opt/venv/bin/pip install --upgrade pip && /opt/venv/bin/pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Set environment variables for Django settings
ENV PATH="/opt/venv/bin:$PATH"

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the application
CMD ["gunicorn", "contract_project.wsgi:application", "--bind", "0.0.0.0:8000"]