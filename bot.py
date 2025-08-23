from config import BOT_TOKEN
from telegram.ext import(
    Updater,
    CommandHandler,    
)
from handlers import (
    start,
)


def main() -> None:
    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))


    updater.start_polling()
    updater.idle()

main()    
