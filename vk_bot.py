import random
import os
import logging
from dotenv import load_dotenv
import telegram
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkApi
from logs_handler import MyLogsHandler
from dialogflow_utils import detect_intent_texts, implicit

logger = logging.getLogger('bots_logger')


def reply(event, vk_api):
    reply = detect_intent_texts(project_id, event.user_id, event.text, language_code)
    if reply is None:
        return
    vk_api.messages.send(
        user_id=event.user_id,
        message=reply,
        random_id=random.randint(1, 1000)
    )


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.DEBUG)
    logging_bot_token = os.environ['LOGGING_BOT_TOKEN']
    logging_chat_id = os.environ['LOGGING_BOT_CHAT_ID']
    logging_bot = telegram.Bot(token=logging_bot_token)
    logger.addHandler(MyLogsHandler(logging_bot, logging_chat_id))

    token = os.environ['VK_BOT_TOKEN']
    project_id = os.environ['DIALOGFLOW_PROJECT_ID']
    language_code = 'ru-RU'

    logger.info('VK бот запущен')
    try:
        implicit()
        vk_session = VkApi(token=token)
        vk_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                reply(event, vk_api)
    except Exception:
        logger.exception('Бот упал с ошибкой:')
