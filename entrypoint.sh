#!/bin/bash

# Inicia actions em background
rasa run actions --port 5055 --debug &

# Aguarda 5 segundos para o actions subir
sleep 5

# Inicia o servidor principal do Rasa
rasa run --enable-api --cors "*" --port 5005 --debug
