FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "init_gradio.py"]
