# Devman task-control checking Telegram bot

This simple telegram bot sends message every time when your task is checked on [dvmn.org](https://dvmn.org). It has two types of messages, depending on is there any mistakes found by your course tutor.

### How to install

python has to be installed on your system. Use pip (or pip3 if there is conflict with Python 2) to install dependences.
```
pip install -r requirements.txt
```
It is recommended to use virtual environment [virtualenv/venv](https://docs.python.org/3/library/venv.html) to isolate your project.  

Besides that you must create `.env` file in your project's folder, containing environment variables. It should look like this(all data except environment variable's names are fake):  
```
dvmn_token=b234bc234cd23423a123242
telegram_token=95132391:wP3db3301vnrob33BZdb33KwP3db3F1I
HTTP_PROXY=http://123.12.12.123:1223
chat_id=654578
```
Variables description:  
`dvmn_token` - your personal token from [dvmn.org](https://dvmn.org), used for api requests authorization. Usually could be found [here](https://dvmn.org/api/docs/).  
`telegram_token` - your telegram bot token, you would get it from [BotFather](https://telegram.me/BotFather) after you bot's been registered.  
`HTTP_PROXY` - if telegram is blocked in your country you should use proxy to access it. Find one in the internet for free or pay for it. You must specify schema, ip-adress and port like in the example above.  
`chat_id` - Your chat id. You can find out it from @userinfobot in Telegram.

Warning! All of environment variables are required. 

### Quickstart

After installation type into console:
```
$python main.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
