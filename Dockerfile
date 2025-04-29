FROM rasa/rasa:3.5.11

USER root
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5005

CMD ["python", "init_rasa.py"]
