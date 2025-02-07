from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler

def start(update, context):
    web_app = WebAppInfo(url="https://artem-lehkosherst.github.io/luvsu.github.io/")
    keyboard = [[InlineKeyboardButton("Открыть открытку", web_app=web_app)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Нажми на кнопку, чтобы открыть открытку:", reply_markup=reply_markup)

updater = Updater("7880413074:AAFkEYhsOqbmI2qt9vaGAPvEjNZQdM_c6Ik", use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
