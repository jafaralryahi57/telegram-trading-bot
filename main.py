import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بك في بوت التحليل الفني\n\n"
        "📸 أرسل لقطة شاشة من Quotex\n"
        "📊 وسيتم تحليل الشموع وإعطاؤك إشارة:\n"
        "📈 صعود أو 📉 هبوط"
    )


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⏳ تم استلام الصورة...\n\n"
        "🔍 جاري تحليل الشموع\n"
        "⚠️ التحليل المتقدم سيتم إضافته لاحقًا"
    )


def main():
    if not TOKEN:
        print("BOT_TOKEN not set")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
