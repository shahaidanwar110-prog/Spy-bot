import telebot
from telebot import types

BOT_TOKEN = 8810423842:AAG3JLiKwko3M4gJZBXd8MssQ0JX93sqdXM
ADMIN_ID = 7436643183

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_trace = types.KeyboardButton("🔍 Trace")
    markup.row(btn_trace)
    bot.reply_to(message, "Choose option:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == "🔍 Trace":
        bot.reply_to(message, f"Searching... Admin ID: {ADMIN_ID}")

print("Bot is running...")
bot.infinity_polling()