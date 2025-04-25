FROM rasa/rasa:3.5.11

USER root
WORKDIR /app
COPY . /app

# Ambiente virtual
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN chmod -R 777 /opt/venv

# Instala dependências
RUN pip install -r requirements.txt

# Exponha as portas usadas (Gradio e Rasa)
EXPOSE 5005
EXPOSE 7860
EXPOSE $PORT  # para compatibilidade com Render

# Aqui rodamos o seu script que sobe tudo
CMD ["python", "main.py"]
