from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 أوامر بوت تواصل معي:\n\n"
        "/start - تشغيل البوت وإظهار القائمة\n"
        "/help - شرح استخدام البوت\n"
        "/about - معلومات عن البوت\n\n"
        "📩 يمكنك استخدام البوت للتواصل وإرسال الرسائل."
    )
