import base64
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler

TOKEN = "YOUR_BOT_TOKEN"
CHANNEL = "@mediapenikmat"  # ganti dengan username channel publik

def handle_photo(update: Update, context: CallbackContext):
    # ambil file_id foto
    file_id = update.message.photo[-1].file_id

    # posting ke channel
    sent_msg = context.bot.send_photo(
        chat_id=CHANNEL,
        photo=file_id,
        caption="Foto baru diposting via bot"
    )

    # bikin payload unik (misalnya message_id)
    payload = base64.urlsafe_b64encode(str(sent_msg.message_id).encode()).decode()

    # generate deep link
    bot_username = context.bot.username
    deeplink = f"https://t.me/{bot_username}?start={payload}"

    # balas ke user dengan link
    update.message.reply_text(f"Foto kamu sudah diposting!\nLink unik: {deeplink}")

def start(update: Update, context: CallbackContext):
    if context.args:
        try:
            decoded = base64.urlsafe_b64decode(context.args[0]).decode()
            update.message.reply_text(f"Ini deskripsi untuk postingan ID {decoded}")
        except Exception:
            update.message.reply_text("Payload tidak valid.")
    else:
        update.message.reply_text("Halo, kirim foto untuk diposting ke channel.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.photo, handle_photo))
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
