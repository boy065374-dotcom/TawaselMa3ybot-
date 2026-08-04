import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

load_dotenv()

ADMIN_ID = int(os.getenv("ADMIN_ID"))

MESSAGE = 1


async def send_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✍️ اكتب الرسالة التي تريد إرسالها للمطور:"
    )

    return MESSAGE


async def receive_send_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            "📩 رسالة جديدة للمطور:\n\n"
            f"👤 الاسم: {user.first_name}\n"
            f"🆔 ID: {user.id}\n\n"
            f"💬 الرسالة:\n{update.message.text}"
        )
    )

    await update.message.reply_text(
        "✅ تم إرسال رسالتك للمطور."
    )

    return ConversationHandler.END
