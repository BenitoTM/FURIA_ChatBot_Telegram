import gradio as gr
import requests
import os


RASA_API = os.getenv("RASA_API", "https://furia-chatbot-telegram-docker.onrender.com")

# Função que envia mensagem para o Rasa
def process_message(user_message, sender_id="test_user"):
    print("rasa_api = ", RASA_API)
    try:
        response = requests.post(
            RASA_API,
            json={"sender": sender_id, "message": user_message}
        )

        if response.ok:
            mensagens = response.json()
            respostas = [msg.get("text", "") for msg in mensagens if "text" in msg]
            return "\n".join(respostas) if respostas else "Nenhuma resposta recebida."
        else:
            return "Ocorreu um erro ao se comunicar com o Rasa."
    except Exception as e:
        return f"Erro: {str(e)}"

# Lançar interface Gradio
def launch_interface():
    gr.ChatInterface(
        fn=process_message,
        title="Chatbot FURIA CS2",
        description="Pergunte qualquer coisa sobre o time da FURIA de CS.",
        theme="soft"
    ).launch(server_name="0.0.0.0", server_port=8000)
