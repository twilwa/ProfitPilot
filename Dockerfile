FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python -c "from transformers import AutoModelForCausalLM, AutoTokenizer; AutoTokenizer.from_pretrained('TheBloke/Llama-2-7B-Chat-GGML'); AutoModelForCausalLM.from_pretrained('TheBloke/Llama-2-7B-Chat-GGML')"
COPY . .
CMD [ "python3", "app.py" ]