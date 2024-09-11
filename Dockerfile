# Base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy the app source code to the container
COPY app.py /app

# Install Flask
RUN pip install Flask

# Define the command to run the app
CMD ["python", "app.py"]

