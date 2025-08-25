from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from handlers import start, book_time, handle_booking, today_bookings
from config import TOKEN

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text("🕒 Vaqtni bron qilish"), book_time))
    dispatcher.add_handler(MessageHandler(Filters.text("📅 Bugungi bronlar"), today_bookings))
    dispatcher.add_handler(CallbackQueryHandler(handle_booking))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
