import gradio as gr
import requests
import os


RASA_API = os.getenv("RASA_API", "https://furia-chatbot-telegram-docker.onrender.com/webhooks/rest/webhook")
SERVER_DADOS = "https://furiaservidordedados-production.up.railway.app/llm"

# Função que envia mensagem para o Rasa
def process_message(user_message, sender_id="test_user"):
    if "line" in user_message.lower():
        user_message = user_message.strip() + " (segundo a HLTV)"
    try:
        """response = requests.post(
            RASA_API,
            json={"sender": sender_id, "message": user_message}
        )"""
        response = requests.post(
            SERVER_DADOS,
            json={
                "question": f"{user_message.strip()} (sobre o time de CS2 da FURIA, 100% atualizado)."
            }
        )

        if response.ok:
            mensagens = response.json()
            respostas = mensagens.get("answer")
            return respostas if respostas else "Nenhuma resposta recebida."
        else:
            return "Ocorreu um erro ao se comunicar com o LLM."
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
