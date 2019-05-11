import requests
import logging
from dotenv import load_dotenv
import sys
import os
import telegram


def make_bot_message(attempt):
    bot_message = 'У вас проверили работу: "{}"\n\n'.format(
        attempt['lesson_title'])
    if attempt['is_negative']:
        bot_message += 'К сожалению, в работе нашлись ошибки'
    else:
        bot_message += 'Преподавателю все понравилось, можно'
        ' приступать к следующему уроку'
    return bot_message


if __name__ == '__main__':
    load_dotenv()
    dvmn_token = os.getenv('dvmn_token')
    telegram_token = os.getenv('telegram_token')
    #http_proxy = os.getenv('HTTP_PROXY')
    chat_id = os.getenv('chat_id')
    #bot_proxy = telegram.utils.request.Request(proxy_url=http_proxy)
    #bot = telegram.Bot(token=telegram_token, request=bot_proxy)
    bot = telegram.Bot(token=telegram_token)
    url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': f'Token {dvmn_token}',
    }
    params = {}
    logging.basicConfig(
        format='%(asctime)s %(process)d %(levelname)s %(message)s',
        level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logging.info('Bot has been started')
    while True:
        try:
            response = requests.get(url,
                                    params=params,
                                    headers=headers,
                                    timeout=91)
            logging.info('Sent request to Devman')
            dvmn_check_info = response.json()
            if 'new_attempts' in dvmn_check_info.keys():
                logging.info('New attempts found')
                bot_messages = []
                for attempt in dvmn_check_info['new_attempts']:
                    bot_messages.append(make_bot_message(attempt))
                for bot_message in bot_messages:
                    bot.send_message(chat_id=chat_id, text=bot_message)
                params['timestamp'] = dvmn_check_info['last_attempt_timestamp']
                continue
            logging.info('No new attempts found')
            params['timestamp'] = dvmn_check_info['timestamp_to_request']
        except requests.exceptions.ReadTimeout as read_timeout_err:
            logging.error(read_timeout_err, exc_info=True)
        except requests.exceptions.ConnectionError as conn_err:
            logging.error(conn_err, exc_info=True)
