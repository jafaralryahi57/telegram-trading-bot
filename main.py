import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # التوكن من Render

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🤖 بوت التداول يعمل بنجاح\n\n"
        "/start - تشغيل البوت\n"
        "/help - المساعدة"
    )

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(
        message,
        "📊 لاحقًا سيتم إضافة تحليل فني وإشارات تداول"
    )

print("Bot is running...")
bot.infinity_polling()
