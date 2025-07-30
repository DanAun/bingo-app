# Use the latest official Python image from the Docker Hub
FROM python:3.10-slim

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 80

# Command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:80", "wsgi:app"]
