import subprocess
import time
import threading

def run_rasa_actions():
    subprocess.call(["rasa", "run", "actions", "--port", "5055", "--debug"])

def run_rasa_server():
    time.sleep(5)  # espera o actions subir primeiro
    subprocess.call(["rasa", "run", "--enable-api", "--cors", "*", "--port", "5005", "--debug"])

if __name__ == "__main__":
    t1 = threading.Thread(target=run_rasa_actions)
    t2 = threading.Thread(target=run_rasa_server)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
