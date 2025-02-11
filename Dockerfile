# Use a Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies (ensuring TensorFlow is installed correctly)
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose port 8080 for Vercel
EXPOSE 8080

# Run the Flask app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
