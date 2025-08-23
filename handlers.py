from telegram.ext import Updater

from telegram.ext import CallbackContext

def start(updater, context = CallbackContext):
    updater.message.reply_text("Salom")