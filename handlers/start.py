from telegram import Update
from telegram.ext import ContextTypes
from buttons import main_buttons


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بك في بوت تواصل معي\n\n"
        "اختر من الأزرار بالأسفل:",
        reply_markup=main_buttons()
    )
