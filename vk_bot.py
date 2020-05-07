import random
import os
import telegram
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkApi
from bots_tg_logger import get_logger
from dialogflow_utils import detect_intent_texts, implicit

TOKEN = os.environ['VK_BOT_TOKEN']
PROJECT_ID = os.environ['DIALOGFLOW_PROJECT_ID']
LANGUAGE_CODE = 'ru-RU'


def reply(event, vk_api):
    reply = detect_intent_texts(PROJECT_ID, event.user_id, event.text, LANGUAGE_CODE)
    if reply is None:
        return
    vk_api.messages.send(
        user_id=event.user_id,
        message=reply,
        random_id=random.randint(1, 1000)
    )


def main():
    logger.info('VK бот запущен')
    try:
        implicit()
        vk_session = VkApi(token=TOKEN)
        vk_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                reply(event, vk_api)
    except Exception:
        logger.exception('Бот упал с ошибкой:')


if __name__ == "__main__":
    logging_bot_token = os.environ['LOGGING_BOT_TOKEN']
    logging_chat_id = os.environ['LOGGING_BOT_CHAT_ID']
    logging_bot = telegram.Bot(token=logging_bot_token)
    logger = get_logger(logging_bot, logging_chat_id)
    main()
