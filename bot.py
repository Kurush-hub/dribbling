from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Замените токен на свой
TOKEN = "7350966339:AAG6vUatEPs6XfqTxNiT_gotMNNa1BWgI4Q"

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚽ Открыть Dribbling", web_app=WebAppInfo(url="https://dribbling-bot.vercel.app"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Добро пожаловать в Dribbling ⚽",
        reply_markup=reply_markup
    )

# Запуск приложения
if __name__ == '__main__':

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Бот запущен и ждёт сообщений...")
    app.run_polling()