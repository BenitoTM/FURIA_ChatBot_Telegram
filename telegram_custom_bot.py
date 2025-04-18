import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import requests

RASA_WEBHOOK_URL = "http://localhost:5005/webhooks/rest/webhook"  # ou use o ngrok para testes externos

TELEGRAM_TOKEN = "TELEGRAM_TOKEN"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Fala, torcedor! Manda sua pergunta sobre a FURIA 🎯")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    sender_id = update.message.chat_id

    # Envia mensagem para o Rasa
    response = requests.post(RASA_WEBHOOK_URL, json={"sender": str(sender_id), "message": user_message})

    if response.ok:
        responses = response.json()
        for r in responses:
            await update.message.reply_text(r.get("text"))
    else:
        await update.message.reply_text("Algo deu errado, tente novamente.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot rodando... Aguarde mensagens no Telegram")
    app.run_polling()
