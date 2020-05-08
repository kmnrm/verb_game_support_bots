import os
import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from bots_tg_logger import get_logger
from dialogflow_utils import detect_intent_texts, implicit

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
PROJECT_ID = os.environ['DIALOGFLOW_PROJECT_ID']
LANGUAGE_CODE = 'ru-RU'


def start(bot, update):
    update.message.reply_text("Здравствуйте! Чем могу Вам помочь?")


def reply_user(bot, update):
    text = update.message.text
    reply = detect_intent_texts(PROJECT_ID, CHAT_ID, text, LANGUAGE_CODE)
    if reply is None:
        update.message.reply_text('Ваш запрос непонятен.')
        return
    update.message.reply_text(reply)


def main():
    logger.info('Telegram бот запущен')
    try:
        implicit()
        updater = Updater(TOKEN)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(MessageHandler(Filters.text, reply_user))
        updater.start_polling()
    except Exception:
        logger.exception('Бот упал с ошибкой:')


if __name__ == '__main__':
    logging_bot_token = os.environ['LOGGING_BOT_TOKEN']
    logging_chat_id = os.environ['LOGGING_BOT_CHAT_ID']
    logging_bot = telegram.Bot(token=logging_bot_token)
    logger = get_logger(logging_bot, logging_chat_id)
    main()
