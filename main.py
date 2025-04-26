import subprocess
import time
import os

# Inicia o Rasa com API
rasa_server = subprocess.Popen(
    ["rasa", "run", "--enable-api", "--cors", "*", "--port", "5005"]
)

# Espera alguns segundos pra garantir que o Rasa suba antes do Gradio
time.sleep(10)

# Inicia a interface do Gradio
from gradio_app import launch_interface  # Certifique-se de ter isso em um método

launch_interface()
