from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_buttons():
    keyboard = [
        [
            InlineKeyboardButton(
                "📺 اليوتيوب",
                url="https://www.youtube.com/@King_games7072"
            )
        ],
        [
            InlineKeyboardButton(
                "📱 الواتساب",
                url="https://wa.me/201090950141"
            )
        ],
        [
            InlineKeyboardButton(
                "صارحني 💬",
                url="https://t.me/cco162BOT?start=mldqlmc3p3"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
