FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port your Flask app will run on
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
