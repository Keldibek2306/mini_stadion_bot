import datetime
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
from database import add_booking, get_bookings   # <-- database.py dan chaqiramiz

def start(update: Update, context: CallbackContext):
    """ /start komandasi """
    keyboard = [
        [KeyboardButton("🕒 Vaqtni bron qilish")],
        [KeyboardButton("📅 Bugungi bronlar")]
    ]
    update.message.reply_text(
        "🏟 Mini Stadion Bron Botiga xush kelibsiz!\n"
        "Siz 07:00 dan 00:00 gacha stadionni bron qilishingiz mumkin.",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

def book_time(update: Update, context: CallbackContext):
    """ Bo‘sh vaqtlarni chiqarish """
    today = str(datetime.date.today())
    bookings = get_bookings(today)

    inline_keyboard = []
    for hour in range(7, 24):
        slot = f"{hour:02d}:00-{(hour+1)%24:02d}:00"
        if slot not in bookings:
            inline_keyboard.append([InlineKeyboardButton(slot, callback_data=f"bron:{slot}")])

    if inline_keyboard:
        update.message.reply_text(
            "⏰ Bron qilish uchun vaqtni tanlang:",
            reply_markup=InlineKeyboardMarkup(inline_keyboard)
        )
    else:
        update.message.reply_text("Bugun hamma vaqtlar bron qilingan.")

def handle_booking(update: Update, context: CallbackContext):
    """ CallbackQuery orqali bron qilish """
    query = update.callback_query
    user = query.from_user
    action, hour = query.data.split(":", 1)

    today = str(datetime.date.today())
    bookings = get_bookings(today)

    if hour not in bookings:
        add_booking(today, hour, user.id, user.username or "NoName")
        query.message.reply_text(f"✅ Siz {hour} vaqtiga bron qildingiz!")
    else:
        query.message.reply_text("❌ Bu vaqt allaqachon band qilingan.")

    query.answer()

def today_bookings(update: Update, context: CallbackContext):
    """ Bugungi bronlarni chiqarish """
    today = str(datetime.date.today())
    bookings = get_bookings(today)

    if not bookings:
        update.message.reply_text("Bugun bronlar yo‘q.")
        return

    text = "📅 Bugungi bronlar:\n\n"
    for slot, user in bookings.items():
        text += f"🕒 {slot} — @{user['username']} (ID: {user['user_id']})\n"

    update.message.reply_text(text)
