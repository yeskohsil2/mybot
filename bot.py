import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Включим логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен вашего бота (замените на свой)
BOT_TOKEN = "8494335344:AAEVoSie3E02bNuOi5UXe4ckhpHs4p6daKY"

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Напиши любое слово, и я отвечу "привет"!')

# Функция для обработки любых текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Отвечаем "привет" на любое сообщение
    await update.message.reply_text('привет')

# Функция для обработки неизвестных команд
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('привет')

def main():
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    
    # Обработчик для любых текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Обработчик для неизвестных команд
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()