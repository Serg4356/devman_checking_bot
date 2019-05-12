# Devman task-control checking Telegram bot

This simple telegram bot sends message every time when your task is checked on [dvmn.org](https://dvmn.org). It has two types of messages, depending on is there any mistakes found by your course tutor. Besides that, it sends some service information (like bot execution status, and errors if they occure).   

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
chat_id=654578
```
Variables description:  
`dvmn_token` - your personal token from [dvmn.org](https://dvmn.org), used for api requests authorization. Usually could be found [here](https://dvmn.org/api/docs/).  
`telegram_token` - your telegram bot token, you would get it from [BotFather](https://telegram.me/BotFather) after you bot's been registered.  
`chat_id` - Your chat id. You can find out it from @userinfobot in Telegram.

Warning! All of environment variables are required. 

### Quickstart

After installation type into console:
```
$python main.py
```

### Deploing on Heroku

This bot can be deployed on Heroku platform. There is a Procfile in project's repository with all required instructions in it.   
   
Just do the following to make successfull deploy:  
   
1. Register on [Heroku](https://heroku.com)  
2. Add new app and name it.  
3. Fork this repository to your github account, and deploy it on Heroku. (You can also choose automatic github deploy, to refresh your project from latests commits).  
4. Turn on new proccess on your heroku account resourses page.   
5. Have fun)  


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
