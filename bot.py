import os
import base64
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# Token bot dari environment (GitHub Secrets atau langsung diisi manual saat testing)
TOKEN = os.getenv("BOT_TOKEN", "7888010367:AAHHodQ6VY14d5P8TRXg3DE3q5aRZvMcpwI")

# Handler untuk command /start
def start(update: Update, context: CallbackContext):
    if context.args:  # kalau ada payload dari link
        try:
            # decode base64
            decoded = base64.urlsafe_b64decode(context.args[0]).decode()
            update.message.reply_text(f"✅ Kamu buka link dengan deskripsi:\n\n{decoded}")
        except Exception:
            update.message.reply_text("❌ Payload tidak valid")
    else:
        update.message.reply_text("Halo! Kirim teks atau klik link dengan payload untuk mulai.")

# Handler untuk teks biasa (optional, kalau mau test manual)
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"Kamu bilang: {update.message.text}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command /start
    dp.add_handler(CommandHandler("start", start))

    # Pesan teks biasa
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
