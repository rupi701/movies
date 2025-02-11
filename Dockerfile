# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the application code to the working directory
COPY . /app

# Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose the port the app runs on machine
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]