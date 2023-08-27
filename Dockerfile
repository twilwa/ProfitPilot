FROM python:3.8-slim-buster

# Install dependencies:
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy local code to container image:
WORKDIR /app
COPY . /app

# Download model
RUN python -c "from transformers import AutoTokenizer; AutoTokenizer.from_pretrained('TheBloke/Llama-2-7B-Chat-GGML')"

# Command to run the application:
CMD ["python", "app.py"]

# Expose any ports the app is expecting in the environment:
EXPOSE 8501