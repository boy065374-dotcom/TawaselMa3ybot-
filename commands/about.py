from telegram import Update
from telegram.ext import ContextTypes


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ معلومات عن البوت:\n\n"
        "🤖 بوتات المطور:\n\n"
        "1- ChatBotGbot\n"
        "   - بوت دردشة ومساعد ذكي.\n\n"
        "2- Diverse11Zbot\n"
        "   - بوت خدمات وأدوات متنوعة.\n\n"
        "📌 هذا البوت: TawaselMa3ybot\n"
        "وظيفته تسهيل التواصل وإرسال الرسائل."
    )
