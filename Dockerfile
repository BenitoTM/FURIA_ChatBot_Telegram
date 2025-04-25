FROM rasa/rasa:3.5.11

USER root
WORKDIR /app
COPY . /app

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN chmod -R 777 /opt/venv

RUN pip install -r requirements.txt

# Expõe as portas reais usadas
EXPOSE 5005
EXPOSE 7860

CMD ["python", "main.py"]
