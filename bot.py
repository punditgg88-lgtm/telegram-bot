from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Halo! Bot sudah jalan 🚀")

def main():
    # Ganti TOKEN_BOT dengan token bot kamu dari BotFather
    updater = Updater("TOKEN_BOT", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
