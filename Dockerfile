FROM rasa/rasa:3.5.11

USER root
WORKDIR /app
COPY . /app

# Garante permissões de escrita no venv
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN chmod -R 777 /opt/venv

RUN pip install -r requirements.txt

# Exponha a porta definida pelo Render
EXPOSE $PORT

# Comando de inicialização padrão do Rasa com suporte à API
CMD ["rasa", "run", "--enable-api", "--cors", "*", "-p", "8000", "-i", "0.0.0.0"]
