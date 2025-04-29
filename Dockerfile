#FROM rasa/rasa:3.5.11

#USER root
#WORKDIR /app
#COPY . /app

#COPY models /app/models

#RUN pip install --no-cache-dir --upgrade pip
#RUN pip install -r requirements.txt

#EXPOSE 5005

#CMD ["run", "actions", "--enable-api", "--cors", "*", "--debug", "--port", "5005"]

FROM rasa/rasa:3.5.11

USER root
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

COPY models /app/models

# Adiciona o script que executa rasa + actions
COPY entrypoint.py .

CMD ["python", "entrypoint.py"]
