from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# 🔴 ضع التوكن هنا مرة واحدة فقط
BOT_TOKEN = "8199542853:AAF96STZ83OoTIV34rdPpL1J32vHOnxbc7Y"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 البوت يعمل بنجاح!\n\n"
        "الأوامر:\n"
        "/start - تشغيل البوت\n"
        "/help - المساعدة"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 هذا بوت تجريبي\n"
        "سيتم لاحقًا إضافة تحليل الشموع والصور"
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
