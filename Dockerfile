FROM rasa/rasa:3.5.11

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 7860
EXPOSE 5005

CMD ["python", "main.py"]