import os
from dotenv import load_dotenv

from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters
)

from handlers.start import start
from commands.help import help_command
from commands.about import about_command
from commands.send import send_command, receive_send_message, MESSAGE


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


def main():
    app = Application.builder().token(TOKEN).build()

    # /start
    app.add_handler(CommandHandler("start", start))

    # /help
    app.add_handler(CommandHandler("help", help_command))

    # /about
    app.add_handler(CommandHandler("about", about_command))

    # /send
    send_handler = ConversationHandler(
        entry_points=[
            CommandHandler("send", send_command)
        ],
        states={
            MESSAGE: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    receive_send_message
                )
            ]
        },
        fallbacks=[]
    )

    app.add_handler(send_handler)

    print("✅ TawaselMa3ybot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
