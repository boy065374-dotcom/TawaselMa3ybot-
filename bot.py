import os
from dotenv import load_dotenv

from telegram.ext import (
    Application,
    CommandHandler
)

from handlers.start import start
from commands.help import help_command
from commands.about import about_command


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
