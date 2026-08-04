import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ContextTypes

load_dotenv()

ADMIN_ID = int(os.getenv("ADMIN_ID"))


async def receive_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            "📩 رسالة جديدة:\n\n"
            f"👤 من: {user.first_name}\n"
            f"🆔 ID: {user.id}\n\n"
            f"💬 الرسالة:\n{update.message.text}"
        )
    )

    await update.message.reply_text(
        "✅ تم إرسال رسالتك للمطور."
    )
