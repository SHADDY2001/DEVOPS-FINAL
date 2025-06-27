<<<<<<< HEAD
# Base image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy files to container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask prometheus_client


# Expose port
EXPOSE 5000

# Run the app
=======
FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install flask prometheus_client

EXPOSE 5000

>>>>>>> master
CMD ["python", "app.py"]
