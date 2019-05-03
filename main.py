import requests
from dotenv import load_dotenv
import os
import telegram
from pprint import pprint


def check_devman(dvmn_token):
    url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': f'Token {token}',
    }
    params = {}
    while True:
        try:
            response = requests.get(url,
                                    params=params,
                                    headers=headers,
                                    timeout=120)
            print(response.json())
            params['timestamp'] = response.json()['timestamp_to_request']
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            pass
        except KeyError:
            params['timestamp'] = response.json()['last_attempt_timestamp']



if __name__ == '__main__':
    load_dotenv()
    dvmn_token = os.getenv('dvmn_token')
    telegram_token = os.getenv('telegram_token')
    http_proxy = os.getenv('HTTP_PROXY')
    chat_id = 390121493
    bot_request = telegram.utils.request.Request(proxy_url=http_proxy)
    bot = telegram.Bot(token=telegram_token, request=bot_request)
    bot.send_message(chat_id=chat_id, text='Света, жопа')

