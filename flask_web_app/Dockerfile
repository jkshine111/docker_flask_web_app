# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install any Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir -r requirement.txt


# DockerFile/requirement.txt

# Expose the port the app runs on (if applicable)
EXPOSE 5011

# Command to run the application
CMD ["python3", "TestDocker.py"]
