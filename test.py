import requests
SERVER_DADOS = "https://furiaservidordedados-production.up.railway.app/llm"

def process_message(user_message, sender_id="test_user"):
    try:
        """response = requests.post(
            RASA_API,
            json={"sender": sender_id, "message": user_message}
        )"""
        response = requests.post(
            SERVER_DADOS,
            json={
                  "question": user_message
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

print(process_message("Qual a lineup atual da FURIA de CS?"))