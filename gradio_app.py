import gradio as gr
import requests
import os

RASA_API = os.getenv("RASA_API")

# Simula o envio de mensagem para o Rasa
def process_message(user_message, sender_id="test_user"):
    try:
        response = requests.post(
            RASA_API,#RASA_WEBHOOK_URL,
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

# Interface do chat com título e instruções
gr.ChatInterface(
    fn=process_message,
    title="Chatbot FURIA CS2",
    description="Pergunte qualquer coisa sobre o time da FURIA de CS.",
    theme="soft"
).launch()
