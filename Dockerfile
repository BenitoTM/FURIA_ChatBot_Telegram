FROM rasa/rasa:3.5.11

USER root
WORKDIR /app
COPY . /app

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN chmod -R 777 /opt/venv

RUN pip install -r requirements.txt

EXPOSE 5005
EXPOSE 7860

# Remove o entrypoint "rasa" que vem da imagem base
ENTRYPOINT []

# Agora o CMD é interpretado corretamente
CMD ["python", "main.py"]
