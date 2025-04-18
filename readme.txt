Este projeto implementa um chatbot com foco no time de CS da FURIA,
utilizando o framework Rasa para NLP e gerenciamento de diálogo, e integrando:
- Telegram (via bot personalizado)
- Um modelo LLM externo (via OpenRouter)
- Um servidor auxiliar em Node.js com dados da HLTV (matches, lineup, resultados)

Esse projeto foi criado para funcionar de forma concomitante ao projeto FURIA_servidor_de_dados.

Intents treinadas:
- inform_proximo_jogo
- inform_resultados_recentes
- inform_lineup
- cumprimentar
- despedir

Ações:
- action_inform_lineup: faz requisição GET para http://localhost:3000/team e retorna os jogadores da FURIA.
- action_fallback_llm: fallback que envia a pergunta do usuário ao modelo LLM (via POST http://localhost:5000/llm).

Integração com Telegram (telegram_custom_bot.py):
- Usa python-telegram-bot para enviar mensagens do usuário ao Rasa e retornar a resposta.
- Utiliza requests.post() para enviar a mensagem ao Rasa (/webhooks/rest/webhook).

Observações Técnicas
- A integração com o LLM (OpenRouter) só ocorre via fallback (nlu_fallback), ou intencionalmente, para intents específicas como inform_resultados_recentes e inform_proximo_jogo.
- O modelo LLM usado foi o Perplexity LLaMA 3.1 Sonar Small (128k) via OpenRouter API.


Execução:

Instale as dependencias:
- pip install -r requirements.txt

Treine o modelo:
- rasa train

Inicie o servidor Rasa:
- rasa run --enable-api

Inicie o action server:
- rasa run actions

Execute o bot do Telegram:
- python telegram_custom_bot.py