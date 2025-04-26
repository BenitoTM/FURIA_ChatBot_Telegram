import subprocess
import time
import os
import requests

def wait_for_rasa(url="http://localhost:5005/"):
    """Espera até o Rasa ficar disponível."""
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200 or response.status_code == 404:
                print("✅ Rasa API disponível!")
                break
        except Exception:
            pass
        print("⏳ Esperando o Rasa ficar disponível...")
        time.sleep(2)

# Inicia o Rasa com API habilitada
rasa_server = subprocess.Popen(
    ["rasa", "run", "--enable-api", "--cors", "*", "--port", "5005"]
)

# Aguarda o Rasa realmente ficar disponível
wait_for_rasa()

# Importa e inicia o Gradio depois que o Rasa está pronto
from gradio_app import launch_interface

launch_interface()
