import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hola! Soy Lumen, tu editor. 🔥\n\n"
        "Mandame un video y lo edito para Facebook.\n\n"
        "Por ahora estoy en modo prueba, pero ya estoy vivo."
    )

async def echo_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Recibi tu video! En un rato te lo devuelvo editado. 🎬")
    await update.message.reply_video(video=update.message.video.file_id, caption="Aqui va tu video de prueba - Lumen")

async def echo_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Recibi tu mensaje: {update.message.text}")

def main():
    token = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VIDEO, echo_video))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_text))
    print("Bot encendido...")
    app.run_polling()

if __name__ == "__main__":
    main()
