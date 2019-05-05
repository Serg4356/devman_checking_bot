import requests
from dotenv import load_dotenv
import os
import telegram



def make_bot_messages(attempts):
    bot_messages = []
    for attempt in attempts:
        bot_message = ''
        lesson_title = attempt['lesson_title']
        bot_message += f'У вас проверили работу {lesson_title}\n\n'
        if attempt['is_negative']:
            bot_message += 'К сожалению, в работе нашлись ошибки'
        else:
            bot_message += 'Преподавателю все понравилось, можно'
            ' приступать к следующему уроку'
        bot_messages.append(bot_message)
    return bot_messages


if __name__ == '__main__':
    load_dotenv()
    dvmn_token = os.getenv('dvmn_token')
    telegram_token = os.getenv('telegram_token')
    http_proxy = os.getenv('HTTP_PROXY')
    chat_id = os.getenv('chat_id')
    bot_proxy = telegram.utils.request.Request(proxy_url=http_proxy)
    bot = telegram.Bot(token=telegram_token, request=bot_proxy)
    url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': f'Token {dvmn_token}',
    }
    params = {}
    while True:
        try:
            response = requests.get(url,
                                    params=params,
                                    headers=headers,
                                    timeout=91)
            if 'new_attempts' in response.json().keys():
                bot_messages = make_bot_messages(response.json()['new_attempts'])
                for bot_message in bot_messages:
                    bot.send_message(chat_id=chat_id, text=bot_message)
                params['timestamp'] = response.json()['last_attempt_timestamp']
                continue
            params['timestamp'] = response.json()['timestamp_to_request']
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            pass
