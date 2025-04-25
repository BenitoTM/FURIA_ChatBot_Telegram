FROM rasa/rasa:3.5.11

USER root
WORKDIR /app
COPY . /app

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN chmod -R 777 /opt/venv

RUN pip install -r requirements.txt

EXPOSE $PORT

# Use shell para garantir que a expansão e o comando funcionem no ambiente Render
CMD sh -c "rasa run --enable-api --cors '*' -p $PORT -i 0.0.0.0"
