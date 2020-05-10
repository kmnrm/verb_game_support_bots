import os
import logging
from dotenv import load_dotenv
import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from logs_handler import MyLogsHandler
from dialogflow_utils import detect_intent_texts, implicit

logger = logging.getLogger('bots_logger')


def start(bot, update):
    update.message.reply_text("Здравствуйте! Чем могу Вам помочь?")


def reply_user(bot, update):
    text = update.message.text
    reply = detect_intent_texts(project_id, chat_id, text, language_code)
    if reply is None:
        update.message.reply_text('Ваш запрос непонятен.')
        return
    update.message.reply_text(reply)


if __name__ == '__main__':
    load_dotenv()
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.DEBUG)
    logging_bot_token = os.environ['LOGGING_BOT_TOKEN']
    logging_chat_id = os.environ['LOGGING_BOT_CHAT_ID']
    logging_bot = telegram.Bot(token=logging_bot_token)
    logger.addHandler(MyLogsHandler(logging_bot, logging_chat_id))

    token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    project_id = os.environ['DIALOGFLOW_PROJECT_ID']
    language_code = 'ru-RU'

    logger.info('Telegram бот запущен')
    try:
        implicit()
        updater = Updater(token)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(MessageHandler(Filters.text, reply_user))
        updater.start_polling()
    except Exception:
        logger.exception('Бот упал с ошибкой:')
