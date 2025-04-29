FROM rasa/rasa:3.5.11

USER root
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt

RUN rasa train

EXPOSE 5005

CMD ["run", "--enable-api", "--cors", "*", "--port", "5005"]
