import requests
import logging
from dotenv import load_dotenv
import sys
import os
import telegram
import argparse


def make_bot_message(attempt):
    bot_message = 'У вас проверили работу: "{}"\n\n'.format(
        attempt['lesson_title'])
    if attempt['is_negative']:
        bot_message += 'К сожалению, в работе нашлись ошибки'
    else:
        bot_message += 'Преподавателю все понравилось, можно'
        ' приступать к следующему уроку'
    return bot_message


class MyLogsHandler(logging.Handler):

    def __init__(self, telegram_bot):
        super().__init__()
        self.telegram_bot = telegram_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.telegram_bot.send_message(chat_id=chat_id, text=log_entry)


if __name__ == '__main__':
    load_dotenv()
    dvmn_token = os.getenv('dvmn_token')
    telegram_token = os.getenv('telegram_token')
    chat_id = os.getenv('chat_id')
    url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': f'Token {dvmn_token}',
    }
    params = {}
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.INFO)
    while True:
        try:
            bot_loger = telegram.Bot(token=telegram_token)
            handler = MyLogsHandler(bot_loger)
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            bot_checker = telegram.Bot(token=telegram_token)
            logger.info('Bot has been started')
            while True:
                try:
                    response = requests.get(url,
                                            params=params,
                                            headers=headers,
                                            timeout=91)
                    logger.debug('Sent request to Devman')
                    response.raise_for_status()
                    dvmn_check_info = response.json()
                    if 'error' in dvmn_check_info.keys():
                        raise requests.exceptions.HTTPError(dvmn_check_info['error'])
                    if 'new_attempts' in dvmn_check_info.keys():
                        logger.debug('New attempts found')
                        bot_messages = []
                        for attempt in dvmn_check_info['new_attempts']:
                            bot_messages.append(make_bot_message(attempt))
                        for bot_message in bot_messages:
                            bot_checker.send_message(chat_id=chat_id,
                                                     text=bot_message)
                        params['timestamp'] = dvmn_check_info['last_attempt_timestamp']
                        continue
                    logger.debug('No new attempts found')
                    params['timestamp'] = dvmn_check_info['timestamp_to_request']
                except requests.exceptions.ReadTimeout as read_timeout_err:
                    logger.error(read_timeout_err)
                except requests.exceptions.ConnectionError as conn_err:
                    logger.error(conn_err)
                except requests.exceptions.HTTPError as http_err:
                    logger.error(http_err)
        except Exception as err:
            logger.error(err)
