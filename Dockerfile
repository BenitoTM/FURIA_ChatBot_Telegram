FROM rasa/rasa:3.5.11

USER root
WORKDIR /app
COPY . /app

# Garante permissões de escrita no venv
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN chmod -R 777 /opt/venv

RUN pip install -r requirements.txt

EXPOSE 7860
EXPOSE 5005

CMD ["python", "main.py"]
