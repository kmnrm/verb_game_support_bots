import logging


class MyLogsHandler(logging.Handler):
    def __init__(self, logging_bot, chat_id):
        super().__init__()
        self.logging_bot = logging_bot
        self.chat_id = chat_id

    def emit(self, record):
        log_entry = self.format(record)
        self.logging_bot.send_message(chat_id=self.chat_id, text=log_entry)


def get_logger(logging_bot, chat_id):
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('bots_logger')
    logger.setLevel(logging.DEBUG)
    handler = MyLogsHandler(logging_bot, chat_id)
    logger.addHandler(handler)
    return logger

