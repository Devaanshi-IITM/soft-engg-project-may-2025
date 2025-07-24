FROM python:3.9

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update

# Copy dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy app source
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI app with uvicorn
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
CMD ["fastapi", "run", "main.py", "--port", "8000"]
