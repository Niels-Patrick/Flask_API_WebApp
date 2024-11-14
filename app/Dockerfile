# Use a lightweight Python image as the base
FROM python:3.12-slim-bullseye

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt
# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app will listen on
EXPOSE 8000

# Define the command to run the app
CMD ["python", "api.py", "--host='0.0.0.0'", "--port=5000"]