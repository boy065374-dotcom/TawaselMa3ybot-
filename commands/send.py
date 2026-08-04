from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

MESSAGE = 1

async def send_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✍️ اكتب الرسالة التي تريد إرسالها للمطور:"
    )
    return MESSAGE


async def receive_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    admin_id = 123456789  # حط ID المطور هنا

    await context.bot.send_message(
        chat_id=admin_id,
        text=(
            "📩 رسالة جديدة من مستخدم:\n\n"
            f"{update.message.text}"
        )
    )

    await update.message.reply_text(
        "✅ تم إرسال رسالتك للمطور."
    )

    return ConversationHandler.END
